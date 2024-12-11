from main import fetch_expenses
from database import get_connection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def vis_cate_spend():
    data = fetch_expenses()
    df = pd.DataFrame(data, columns=["ID", "Date", "Category", "Amount", "Description"])
    plt.figure(figsize=(8, 6))
    sns.barplot(x="Category", y="Amount", data=df.groupby("Category").sum().reset_index())
    plt.title("Categoy-wise-spending")
    plt.ylabel("Total amount")
    plt.savefig("category_wise_spending.png")
    plt.close()

def vis_month_trend():
    data = fetch_expenses()
    df = pd.DataFrame(data, columns=["ID", "Date", "Category", "Amount", "Description"])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df["Date"].dt.to_period("M").astype(str)

    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df = df.dropna(subset=['Amount'])  
    # print(df)
    monthly_data = df.groupby("Month")["Amount"].sum().reset_index()
    # print(monthly_data.dtypes)

    plt.figure(figsize=(8,6))
    # print(monthly_data)
    sns.lineplot(x = 'Month', y = 'Amount', data = monthly_data, markers='o')
    plt.title("Monthly spend trend")
    plt.ylabel("Total Amount")
    print(monthly_data)
    print(monthly_data.dtypes)
    plt.savefig("monthly_trend_spending.png")
    plt.close()


