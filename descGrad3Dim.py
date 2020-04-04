import numpy as np
import matplotlib.pyplot as plt
# dibujamos una funcion tridimensional cualquiera en un grafico
resol=1000
x=np.linspace(-6,6,resol)
y=np.linspace(-6,6,resol)
z=np.zeros([resol,resol])

f=lambda _x : np.sin(_x[0])+np.sin(_x[1])	#esta funcion va a determinar los valores para el vector z

for indX, ix in enumerate(x):
	for indY, iy in enumerate(y):
		z[indX][indY]=f([ix,iy])

plt.contourf(x,y,z,300)
plt.colorbar()

# "Tiramos" una bolita en algun punto x, y  de esa grafica 
bolita=np.random.rand(2)*6-3
plt.plot(bolita[0],bolita[1],'o',c='red')
#-------------------------------------------------------
h=0.01
lr=0.04
grad=np.zeros(2)
ya_casi=10e-6

# calculamos la derivada  de la funcion en el punto 'bolita' y en las subsiguientes posiciones 
# en las que se encontrará dicho punto para cada una de las variables intependientes (x, y)
for paso in range(1000):
	for i, th in enumerate(bolita):
		temp=np.copy(bolita)
		temp[i] += h
		deriv= (f(temp)-f(bolita))/h 	#derivada del punto 'bolita'
		grad[i]= deriv
	bolita-= lr*grad					#damos un paso 'pendiente abajo'
	plt.plot(bolita[0],bolita[1],'.',c='blue')

	if abs(grad[0]) < ya_casi and abs(grad[1]) < ya_casi:
		print(f"la bolita ha llegado al minimo de {f(bolita)} en {paso} pasos")
		break
plt.plot(bolita[0],bolita[1],'o',c='green')
plt.show()
