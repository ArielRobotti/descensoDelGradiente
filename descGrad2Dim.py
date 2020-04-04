import numpy as np
import matplotlib.pyplot as plt

# dibujamos una funcion cualquiera en un grafico por ejemplo f(x)= cos(x) + cos(2x)
resol=1000
x=np.linspace(-5,5,resol)
f=lambda _x: np.cos(_x)+np.cos(2*_x)
plt.plot(x,f(x))
#-----------------------------------------------
# "Tiramos" una bolita en algun punto x,f(x)  de esa grafica 

bolita=np.random.rand(1)*10-5
plt.plot(bolita,f(bolita),'o',c='red')
#------------------------------------------------

h=0.001		# h vendria a ser la diferencial (delta) de x para calcular la derivada 
lr=0.05		# radio de aprendizaje: determina cuan "grande" es el paso hacia abajo en la curva

for i in range(60):				
	
	deriv=(f(bolita+h)-f(bolita))/h  	#calculamos la derivada de f(x) en el punto "bolita". Es decir, 
						#la pendiente de la recta tangente que pasa por ese punto de la curva					
	bolita-=deriv*lr			#damos un paso (deriv*lr) hacia donde la pendiente disminuye
	plt.plot(bolita,f(bolita),'o',c='blue')
	
print(f'la bolita bajó hasta la posicion {f(bolita)}')
plt.show()
