#SQLiteに保存して、地区別に集計する
import sqlite3
import pandas as pd

df = pd.read_csv("clean_mansion.csv")

conn = sqlite3.connect("trades.db")
df.to_sql("mansion", conn, if_exists="replace", index=False)


sql = """
SELECT DistrictName, COUNT(*) AS n, AVG(UnitPriceM2) AS avg_price
FROM mansion
GROUP BY DistrictName
HAVING COUNT(*) >= 10
ORDER BY avg_price DESC
"""

result = pd.read_sql_query(sql, conn)
print(result)

conn.close()

check = df.groupby("DistrictName")["UnitPriceM2"].agg(["count", "mean"])
print(check[check["count"] >= 10].sort_values("mean", ascending=False))

