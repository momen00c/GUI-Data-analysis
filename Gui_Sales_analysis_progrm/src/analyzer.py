import pandas as pd
import numpy as np
def calc_kpis(df):
    return {
        "total_sales": df['total'].sum(),
        "avg_rating": df['rating'].mean(),
        "total_tax": df['tax'].sum(),
        "total_quantity_sold": df['quantity'].sum(),
        "total_revenue": (df['unit_price'] * df['quantity']).sum() if df['quantity'].iloc[5]==np.nan else (df['total'] - df['unit_price']).sum()

    }
def sales_eda(df):
    return {
        "sales_by_day": df.groupby("Day")['total'].sum(),
        "sales_by_payment_type": df.groupby("payment_type")['total'].sum(),
        "sales_by_product_line": df.groupby("product_line")['total'].sum(),
        "sales_by_city": df.groupby("city")['total'].sum()
    }

def customer_eda(df):
    return {
        "avg_rating_by_customer_type": df.groupby("customer_type")['rating'].mean(),
        "sales_by_customer_type": df.groupby("customer_type")['total'].sum(),
        "count_by_gender": df.groupby("gender")['invoice_id'].count()
    }
def product_eda(df):
    return {
        "avg_unit_price_by_product": df.groupby("product_line")['unit_price'].mean(),
        "quantity_sold_by_product": df.groupby("product_line")['quantity'].sum(),
        "count_product_by_category": df.groupby("product_line")['product_line'].count(),
        "gross_income_by_product": df.groupby("product_line")['gross_income'].sum()
    }
