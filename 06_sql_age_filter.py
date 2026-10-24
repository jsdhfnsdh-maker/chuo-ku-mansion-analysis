#築年数を絞って、地区別に集計する
import sqlite3
import pandas as pd

conn = sqlite3.connect("trades.db")

sql = """
SELECT DistrictName, COUNT(*) AS n, AVG(UnitPriceM2) AS avg_price
FROM mansion
WHERE 築年数 BETWEEN 10 AND 20
GROUP BY DistrictName
HAVING COUNT(*) >= 5
ORDER BY avg_price DESC
"""

result = pd.read_sql_query(sql, conn)
print(result)

conn.close()
