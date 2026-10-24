import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("my_quotes2.csv")
counts = df["author"].value_counts().head(10)
counts.plot(kind="bar")
plt.tight_layout()
plt.savefig("authors.png")
