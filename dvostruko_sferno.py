import numpy as np
from formule import teta1_tacka_tacka, teta2_tacka_tacka, fi1_tacka_tacka,\
fi2_tacka_tacka, poz1, poz2
import vpython as vp

num_fixed = 0
def fix(alfa):
    global num_fixed
    alfa_check = alfa % np.pi
    sgn = 1
    if alfa < 0:
        sgn = -1
    if alfa_check < 0.01 or alfa_check > 3.13 or \
        np.pi / 2 - 0.01 < alfa_check < np.pi / 2 + 0.01:
        num_fixed += 1
        return alfa + sgn * 0.01
    else:
        return alfa


if __name__ == '__main__':    
    
	g = 9.81
	t = 0
	dt = 1e-3

	l1 = 1
	l2 = 1
	m1 = 1
	m2 = 1

	#primeri
	#4 3 30 20 i fi1_tacka = 1, bez fixalfa
	#-50 130 -60 -70 i teta1_tacka = 10, bez fixalfa

	fi1 = np.deg2rad(-50)
	fi2 = np.deg2rad(130)
	teta1 = np.deg2rad(-60)
	teta2 = np.deg2rad(-70)

	#teta -> ugao sa vertikalom (2D klatno)
	#fi -> ugao sa horizontalom

	fi1_tacka = 0
	fi2_tacka = 0
	teta1_tacka = 10
	teta2_tacka = 0

	init = poz1(m1,l1,teta1,fi1)
	init.extend(poz2(m1,m2,l1,l2,teta1,teta2,fi1,fi2))

	kuglica1 = vp.sphere(pos = vp.vector(init[0], init[1], init[2]), radius = l1/10.0)
						  # ,make_trail = True)

	kuglica2 = vp.sphere(pos = vp.vector(init[3], init[4], init[5]), radius = l2/10.0)
						  # ,make_trail = True, color = vp.color.red)

	nit1 = vp.cylinder(pos=vp.vector(0,0,0),axis=kuglica1.pos,radius=kuglica1.radius*0.1,
				   color=vp.color.cyan)

	nit2 = vp.cylinder(pos = kuglica1.pos, axis = kuglica2.pos, radius=kuglica2.radius*0.1, 
						color=vp.color.cyan)

	nit_r = vp.cylinder(pos = vp.vector(0,0,0), axis = vp.vector(0,0,-1), 
						radius = kuglica1.radius*0.1, color = vp.color.white, 
						length = nit2.length + nit1.length + 0.5)

	postolje = vp.box(pos=nit_r.axis, size=vp.vector(0.4,0.4,0.1))

	vp.scene.camera.pos = vp.vector(0,0,0)

	while t < 10:
		
		vp.rate(1000)
		
		# teta1 = fix(teta1)
		# teta2 = fix(teta2)
		# fi1 = fix(fi1)
		# fi2 = fix(fi2)
		
		teta1 = teta1 + teta1_tacka * dt
		teta2 = teta2 + teta2_tacka * dt
		
		fi1 = fi1 + fi1_tacka * dt
		fi2 = fi2 + fi2_tacka * dt
		
		teta1_tacka = teta1_tacka + teta1_tacka_tacka(m1,m2, l1,l2, teta1, teta2,
		fi1, fi2,teta1_tacka, teta2_tacka,fi1_tacka, fi2_tacka) * dt
		
		teta2_tacka = teta2_tacka + teta2_tacka_tacka(m1,m2, l1,l2, teta1, teta2,
		fi1, fi2,teta1_tacka, teta2_tacka,fi1_tacka, fi2_tacka) * dt
		
		fi1_tacka = fi1_tacka + fi1_tacka_tacka(m1,m2, l1,l2, teta1, teta2,
		fi1, fi2,teta1_tacka, teta2_tacka,fi1_tacka, fi2_tacka)*dt
		
		fi2_tacka = fi2_tacka + fi2_tacka_tacka(m1,m2, l1,l2, teta1, teta2,
		fi1, fi2,teta1_tacka, teta2_tacka,fi1_tacka, fi2_tacka)*dt

		k1 = poz1(m1,l1,teta1,fi1)
		k2 = poz2(m1,m2,l1,l2,teta1,teta2,fi1,fi2)
		
		
		kuglica1.pos = vp.vector(k1[0],k1[1], k1[2])
		kuglica2.pos = vp.vector(k2[0],k2[1], k2[2])
		nit1.axis = kuglica1.pos
		nit2.pos = kuglica1.pos
		nit2.axis = -(kuglica1.pos - kuglica2.pos)
		
		t+=dt
		

	print(num_fixed)