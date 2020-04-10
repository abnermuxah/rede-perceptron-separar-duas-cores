import numpy as np
import matplotlib.pyplot as plt
from random import *
#com epoca
def f(x, p1,p2):
	return -(p1*x)/p2

xx = np.arange(-1, 1, 0.1) 
yy = np.arange(-1, 1, 0.1) 

#x1 = [0.3, -0.6, -0.1, 0.1]
#x2 = [0.7,0.3,-0.8,-0.45]
#classe = [1,0,0,1]

x1 = [0.2, 0.4,-0.2,-0.4]
x2 = [0.2,0.4,-0.2,-0.4]
classe = [1,1,0,0]

peso = []
# defnir pesos aleatorios
for i in range(2):
	n = uniform(-1,1) # gerar aleatorio float
	peso.append(n)
n = 0.1 # taxa de aprendizado
e = 0 # erro 
out = 0 # saida do neuronio
#peso = [0.8,-0.5]
epoca = 1
max_epoca = 100
print(peso) #peso inicial
while (max_epoca != epoca):
	i = 0 
	while (i != (len(classe))-1):
	# calcular a saida do neuronio
		out = x1[i]*peso[0]+x2[i]*peso[1]
		# funcao de ativacao
		if out >= 0:
			out = 1
		else:
			out = 0
		#verificar se classificou de forma correta
		if out != classe[i]:
			e = (classe[i] - out) # calcular o erro e ajustar os pesos
			peso[0] = peso[0] + n*e*x1[i]
			peso[1] = peso[1] + n*e*x2[i]
			print(peso)
			plt.plot(xx, f(xx, peso[0], peso[1]), color='grey')
		i+=1
	epoca +=1

# exibir o grafico
for i in range(len(classe)):
	if classe[i] == 1:
		plt.plot(x1[i], x2[i], 'bo')
	else:
		plt.plot(x1[i], x2[i], 'ro')



plt.plot(xx, f(xx, peso[0], peso[1]), color='m')

plt.show()

