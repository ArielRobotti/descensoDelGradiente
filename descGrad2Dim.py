import numpy as np
import matplotlib.pyplot as plt
# dibujamos una funcion cualquiera en un grafico por ejemplo f(x)= cos(x) + cos(2x)
resol=1000
x=np.linspace(-5,5,resol)
f=lambda _x: np.cos(_x)+np.cos(_x*2)

plt.plot(x,f(x))
#-----------------------------------------------
# "Tiramos" una bolita en algun punto x,f(x)  de esa grafica 
bolita=np.random.rand(1)*10-5
plt.plot(bolita,f(bolita),'o',c='red')
#------------------------------------------------
h=10e-4			# h vendria a ser la diferencial (delta) de x para calcular la derivada 
lr=0.02			# radio de aprendisaje: determina cuan "grande" es el paso hacia abajo en la curva
ya_casi=10e-4	#para evaluar si la pendiente esta tan cerca de cero como para detener las iteraciones

for i in range(500):
	deriv=(f(bolita+h)-f(bolita))/h  		#calculamos la derivada de f(x) en el punto "bolita". Es decir, 
											#la pendiente de la recta tangente que pasa por ese punto de la curva					
	bolita-=deriv*lr						#damos un paso (deriv*lr) hacia donde la pendiente disminuye							
	plt.plot(bolita,f(bolita),'.',c='blue')
	if deriv**2< ya_casi**2:				#evaluamos si ya está tan cerca de cero como "ya_casi"
		print(f'la bolita bajó hasta la posicion {f(bolita)} en {i} pasos')
		break	

plt.show()
