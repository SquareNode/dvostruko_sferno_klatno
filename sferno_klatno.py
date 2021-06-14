import numpy as np
import vpython as vp

def alfa_tacka_tacka(alfa, alfa_tacka, beta, beta_tacka):
    return -2*alfa_tacka*beta_tacka*np.cos(beta)/np.sin(beta)

def beta_tacka_tacka(alfa, alfa_tacka, beta, beta_tacka):
    return (l*alfa_tacka**2*np.sin(beta)*np.cos(beta) - g*np.sin(beta))/l

if __name__ == '__main__':
	t = 0
	dt = 1e-4
	g = 9.81
	m = 1
	l = 1

	alfa = np.deg2rad(30)
	beta = np.deg2rad(10)

	#dobro izgleda: 4,2 4,1
	#parametri: dt 1e-4, alfa 30, beta 10, t < 100 rate 10000

	alfa_tacka = 4
	beta_tacka = 2

	kuglica = vp.sphere(pos=vp.vector(l*np.sin(beta)*np.cos(alfa),
		l*np.sin(beta)*np.sin(alfa), l*np.cos(beta)), radius = l/10.0)
				 
	nit = vp.cylinder(pos=vp.vector(0,0,0),
		axis=kuglica.pos,radius=kuglica.radius*0.1, color=vp.color.cyan)
	
	nit_ref = vp.cylinder(pos=vp.vector(0,0,0), axis = vp.vector(0,0,2),
		radius=kuglica.radius*0.1, length = 1.5*l)

	pedestal = vp.box(pos=nit_ref.axis, size=vp.vector(0.4,0.4,0.1))

	# x,y,z = np.array([]), np.array([]), np.array([])

	while t < 100:
		
		vp.rate(10000)
		
		old_alfa_tacka = alfa_tacka
		alfa_tacka = alfa_tacka + alfa_tacka_tacka(alfa,alfa_tacka,beta,beta_tacka)*dt
		beta_tacka = beta_tacka + beta_tacka_tacka(alfa,old_alfa_tacka,beta,beta_tacka)*dt
		
		alfa = alfa + alfa_tacka*dt
		beta = beta + beta_tacka*dt
		
		x1 = l*np.sin(beta)*np.cos(alfa)
		y1 = l*np.sin(beta)*np.sin(alfa)
		z1 = l*np.cos(beta)
		
		# x.append(x1)
		# y.append(y1)
		# z.append(z1)
		
		kuglica.pos = vp.vector(x1,y1,z1)
		nit.axis = kuglica.pos
		
		t+=dt
