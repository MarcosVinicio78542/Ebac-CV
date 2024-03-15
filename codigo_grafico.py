import pandas as pd
import matplotlib.pyplot as plt

# lendo arquivo
df = pd.read_csv("gasolina.csv")

# Plotando o gráfico de linha
plt.figure(figsize=(8, 6))
plt.plot(df['dia'], df['venda'], marker='o', color='blue')
plt.title('Preço da gasolina ao longo dos dias')
plt.xlabel('Dia')
plt.ylabel('Preço da gasolina')
plt.grid(True)
plt.savefig("gasolina.png")
plt.show()