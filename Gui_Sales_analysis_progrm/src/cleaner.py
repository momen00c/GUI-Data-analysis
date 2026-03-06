import pandas as pd
from tkinter import messagebox
def clean_data(df):
    df.drop_duplicates()
    df['invoice_id']=df['invoice_id'].astype(str)
    df['branch'] = df['branch'].astype(str)
    df['city'] = df['city'].astype(str)
    df['customer_type'] = df['customer_type'].astype(str)
    df['product_line'] = df['product_line'].astype(str)
    df['unit_price'] = df['unit_price'].astype(float)
    df['quantity'] = df['quantity'].astype(int)
    df['payment_type'] = df['payment_type'].astype(str)
    df['cogs'] = df['cogs'].astype(float)
    df['gross_margin'] = df['gross_margin'].astype(float)
    df['gross_income'] = df['gross_income'].astype(float)
    df['time'] = df['time'].astype(str)

    df['rating'] = df['rating'].astype(float)


    return df

def view_nulls(df):
    df.isna().sum()
    return df

def drop_column(df,name,se_top):
    df.drop(columns = name,inplace=True)
    messagebox.showinfo(detail=f"column {name} has deleted")
    se_top.withdraw()

    return df