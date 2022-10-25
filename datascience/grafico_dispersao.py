import matplotlib.pyplot as plt

x = [1, 2, 5, 7, 9]
y = [2, 3, 7, 1, 0]


titulo = "Scatterplot: Gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label='Meus pontos', color='g', marker='h', s=100)
plt.plot(x, y, color='k', linestyle=':')
plt.legend()
# plt.show()
plt.savefig("figura1.png", dpi=500)
