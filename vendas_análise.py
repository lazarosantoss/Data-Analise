import pandas as pd
import matplotlib.pyplot as plt

# Simular dados de vendas
data = {
    "Data": ["2024-01-15", "2024-01-20", "2024-02-15", "2024-03-10", "2024-03-15"],
    "Produto": ["A", "B", "A", "C", "A"],
    "Quantidade": [5, 3, 8, 2, 4],
    "Preço Unitário": [20.0, 50.0, 20.0, 100.0, 20.0]
}
df = pd.DataFrame(data)
df["Receita"] = df["Quantidade"] * df["Preço Unitário"]

# Insights
top_produtos = df.groupby("Produto")["Receita"].sum().sort_values(ascending=False)
print("Receita por Produto:\n", top_produtos)

df["Data"] = pd.to_datetime(df["Data"])
df["Mês"] = df["Data"].dt.month
receita_mensal = df.groupby("Mês")["Receita"].sum()

# Visualização
plt.bar(receita_mensal.index, receita_mensal.values)
plt.title("Receita Mensal")
plt.xlabel("Mês")
plt.ylabel("Receita")
plt.show()
