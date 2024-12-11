# table containing top 5 spending category with their amount
# bar graph of category vs amount
# line plot for monthly spending trend
from database import get_connection
import pandas as pd
from visualization import vis_cate_spend, vis_month_trend
from pathlib import Path

def topCategory():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('select category, sum(amount) as total_amount from expenses group by category order by total_amount desc limit 5;')
    row = cursor.fetchall()
    conn.close()
    top_df  = pd.DataFrame(row, columns=["Category", "Total_Amount"])
    return top_df

def generate_report():
    vis_cate_spend()
    vis_month_trend()

    path = Path('expense_report.md')
    with open(path, 'w') as f:
        f.write("# EXPENSE REPORT \n\n")

        f.write("Top 5 High spending Category: \n")
        f.write(topCategory().to_markdown(index=False))
        f.write("\n\n")

        f.write("# Category wise spending \n")
        f.write("![Category wise spend](category_wise_spending.png) \n\n")

        f.write("# Monthly spending trend \n")
        f.write("![Monthly  Spending trend](monthly_trend_spending.png) \n\n")
    print(f"Report generated: {path.absolute()}")
generate_report()

