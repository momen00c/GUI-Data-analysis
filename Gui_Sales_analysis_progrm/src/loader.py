import pandas as pd
import numpy as np
import os
def load_csv_data(name):
    df = pd.read_csv(name)
    return df

def load_excl_data(name):
    df = pd.read_excel(name)
    return df
def preview_columns(df):
    return df.columns.tolist()+[None]
def setting_data(df):
    required_columns = ['invoice_id', 'branch', 'city', 'customer_type', 'gender', 'product_line', 'unit_price', 'quantity', 'tax', 'total', 'date', 'time', 'payment_type', 'cogs', 'gross_margin', 'gross_income', 'rating',]
    missing = [col for col in required_columns if col not in df.columns]
    for i in missing:
        df[i] = np.nan
    return df


def open_power_pi():
   os.startfile(r'super_market_dashboard.pbix')
