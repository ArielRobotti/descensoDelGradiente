import numpy as np
import matplotlib.pyplot as plt

# dibujamos una funcion cualquiera en un grafico por ejemplo f(x)= cos(x) + cos(2x)
resol=1000
x=np.linspace(1,9,resol)

f=lambda _x: np.cos(_x)+np.cos(2*_x)
plt.plot(x,f(x))
#-----------------------------------------------
# "Tiramos" una bolita en algun punto x,f(x)  de esa grafica 

bolita=np.random.rand(1)*8+1
plt.plot(bolita,f(bolita),'o',c='red')
#------------------------------------------------

h=0.001		# h vendria a ser el diferencial de x o delta de x para calcular la derivada 
lr=0.05		# radio de aprendisaje: determina cuan "grande" es el paso hacia abajo en la curva

for i in range(60):

	deriv=(f(bolita+h)-f(bolita))/h  	#calculamos la derivada deriv=(f(x+h)-f(x))/h con h tendiendo a 0					
	bolita-=deriv*lr					#avanzamos un paso en direccion contraria a la pendiente en el punto 'bolita'
	plt.plot(bolita,f(bolita),'o',c='blue')
	

print(f'la bolita bajó hasta la posicion {f(bolita)}')
plt.grid()
plt.show()