import pandas as pd
import datetime as dt
from src.cleaner import clean_data
def add_data_feature_eng(df):
    clean_data(df)

    df['date']=pd.to_datetime(df['date'])
    df['Month'] = df['date'].dt.month
    df['Day'] = df['date'].dt.day

    if 'time' in df.columns:
        df["qu_hour_test"] = df.time.map(lambda x: x[:2])
        df['qu_hour_test'] = pd.to_numeric(
                         df['qu_hour_test'],
                         errors='coerce')
    # q1 --> 0 to 6  qnd  q2 --> 6 to 12  ...
        df["Qu_hour"] = df.qu_hour_test.map(lambda x:"Q6" if x>=20 
                                else "Q5" if x>=16 
                                else "Q4" if x>= 12
                                else "Q3" if x>=8
                                else "Q2" if x>=4
                                else "Q1")
        df.drop('qu_hour_test',axis=1,inplace=True)
    return df