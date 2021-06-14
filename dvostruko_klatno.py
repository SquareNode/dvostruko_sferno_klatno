import numpy as np
import vpython as vp

def fi1_dot_dot(fi1, fi2, fi1_dot, fi2_dot):
    return (-g*(2*m1 + m2)*np.sin(fi1) - m2*g*np.sin(fi1 - 2*fi2)-
2*np.sin(fi1 - fi2)*m2*(fi2_dot**2*l2 + fi1_dot**2*l1*np.cos(fi1-fi2))/
(l1*(2*m1 + m2 - m2*np.cos(2*fi1 - 2*fi2))))


def fi2_dot_dot(fi1, fi2, fi1_dot, fi2_dot):
    return (2*np.sin(fi1 - fi2)*(fi1_dot**2*l1*(m1+m2)
* g*(m1+m2)*np.cos(fi1)+fi2_dot**2*l2*m2*
np.cos(fi1-fi2))/(l2*(2*m1 + m2 - m2*np.cos(2*fi1 - 2*fi2))))

if __name__ == '__main__':

	t = 0
	dt = 1e-4
	g = 9.81

	m1 = 1
	m2 = 1
	l1 = 1
	l2 = 1
	fi1 = np.deg2rad(40)
	fi2 = np.deg2rad(10)
	fi1_dot = 0
	fi2_dot = 0

	ball = vp.sphere(pos=vp.vector(l1*np.sin(fi1),-l1*np.cos(fi1),0),
				 radius = l1/10.0)

	thread = vp.cylinder(pos=vp.vector(0,0,0),axis=ball.pos,radius=ball.radius*0.1,
				   color=vp.color.cyan)
	ball2 = vp.sphere(pos=vp.vector(l2*np.sin(fi2),-l1*np.cos(fi2),0),
				 radius = l2/10.0)

	thread2 = vp.cylinder(pos=ball.pos ,axis=ball2.pos,radius=ball.radius*0.1,
				   color=vp.color.cyan, length=l2)

	while t < 10:
		
		vp.rate(6000)
		old_fi1_dot = fi1_dot
		fi1_dot = fi1_dot + fi1_dot_dot(fi1, fi2, fi1_dot, fi2_dot) * dt
		fi2_dot = fi2_dot + fi2_dot_dot(fi1, fi2, old_fi1_dot, fi2_dot) * dt
		
		fi1 = fi1 + fi1_dot*dt
		fi2 = fi2 + fi2_dot*dt
		
		x1 = l1*np.sin(fi1)
		y1 = -l1 * np.cos(fi1)
		
		x2 = x1 + l2*np.sin(fi2)
		y2 = y1 - l2*np.cos(fi2)
		
		ball.pos = vp.vector(x1,y1,0)
		thread.axis = ball.pos
		ball2.pos = vp.vector(x2,y2,0)
		thread2.pos = ball.pos
		thread2.axis = -(ball.pos - ball2.pos)
		
		t+=dt