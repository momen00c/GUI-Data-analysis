import pandas as pd
from tkinter import filedialog
df = pd.DataFrame()
def expoert_excl(df):
    df.to_excel('output\data.xlsx', sheet_name='Sheet1', index=False)
