#築年数と㎡単価の散布図を作る
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Meiryo"

df = pd.read_csv("clean_mansion.csv")

# 築年数が欠けている行を除く
d = df.dropna(subset=["築年数"])

plt.figure(figsize=(8, 5))
plt.scatter(d["築年数"], d["UnitPriceM2"] / 10000, alpha=0.4)
plt.xlabel("築年数(年)")
plt.ylabel("㎡単価(万円)")
plt.title("築年数と㎡単価(中古マンション、中央区、2015年)")
plt.tight_layout()
plt.savefig("age_price.png", dpi=150)

print(df["Municipality"].unique())
