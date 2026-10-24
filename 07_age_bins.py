#築年数の区間ごとに、件数と中央値を出す
import pandas as pd

df = pd.read_csv("clean_mansion.csv")

# 築年数が欠けている行を除く
d = df.dropna(subset=["築年数"])

bins = pd.cut(d["築年数"], [-1, 10, 20, 30, 50])
print(d.groupby(bins)["UnitPriceM2"].agg(["count", "median"]))
