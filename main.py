from database import get_connection
import pandas as pd

def add_expense(date, category, amount, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (date, category, amount, description)
        VALUES (%s, %s, %s, %s);
    ''', (date, category, amount, description))
    conn.commit()
    conn.close()
    print("Expense added successfully!")

def input_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Travel): ")
    amount = float(input("Enter the amount: "))
    description = input("Enter a description (optional): ")
    add_expense(date, category, amount, description)


def fetch_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses;')
    rows = cursor.fetchall()
    conn.close()
    return rows


def view_expenses():
    data = fetch_expenses()
    df = pd.DataFrame(data, columns=["ID", "Date", "Category", "Amount", "Description"])
    print(df)

def generate_summary():
    data = fetch_expenses()
    df = pd.DataFrame(data, columns=["ID", "Date", "Category", "Amount", "Description"])
    print("\nCategory-wise Spending:")
    print(df.groupby("Category")["Amount"].sum())
    print("\nMonthly Spending:")
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    print(df.groupby("Month")["Amount"].sum())

if __name__ == "__main__":
    input_expense()
