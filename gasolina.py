import pandas as pd
import matplotlib.pyplot as plt

# lendo arquivo
df = pd.read_csv("gasolina.csv")

# Criando uma sequência de dias de 1 a 10
dias = range(1, 11)

# Plotando o gráfico de linha
plt.figure(figsize=(8, 6))
plt.plot(dias, df['venda'][:10], marker='o', color='red', label='Preço da gasolina')
plt.title('Preço da gasolina ao longo dos dias')
plt.xlabel('Dia')
plt.ylabel('Preço da gasolina')
plt.grid(True)
plt.legend()
plt.savefig("gasolina.png")

plt.show()