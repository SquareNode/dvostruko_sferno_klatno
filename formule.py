from math import sin, cos

g = 9.81
                                                     
def teta1_tacka_tacka(m1, m2, l1, l2, theta1, theta2, phi1, phi2,
                 vtheta1, vtheta2, vphi1, vphi2):
	sintheta1 = sin(theta1)
	sintheta2 = sin(theta2)
	costheta1 = cos(theta1)
	costheta2 = cos(theta2)
	sinphi1   = sin(phi1)
	sinphi2   = sin(phi2)
	cosphi1   = cos(phi1)
	cosphi2   = cos(phi2)
	return -(((l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*sintheta2*sintheta2*sintheta2*vphi2*vphi2 + (((l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1 - (l1*m1 + l1*m2)*cosphi1*cosphi1 + (2*l1*m1*cosphi1*cosphi1 - l1*m1 - l1*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*(l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1 - (l1*m1 + l1*m2)*cosphi1*cosphi1 + (2*l1*m1*cosphi1*cosphi1 - l1*m1 - l1*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + (l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1 - (l1*m1 + l1*m2)*cosphi1*cosphi1 + (2*l1*m1*cosphi1*cosphi1 - l1*m1 - l1*m2)*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*costheta1*sintheta1*vtheta1*vtheta1 - (((g*m1 + g*m2)*cosphi1*cosphi1 + (g*m1 + g*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*((g*m1 + g*m2)*cosphi1*cosphi1 + (g*m1 + g*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + ((g*m1 + g*m2)*cosphi1*cosphi1 + (g*m1 + g*m2)*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2 - ((l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l1*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2*vphi1*vphi1 + 2*(l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l1*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2*vphi1*vphi1 + (l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l1*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2*vphi1*vphi1)*costheta1)*sintheta1)*costheta2*costheta2 - (((l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*vphi1*vphi1 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*vphi1*vphi1 + (l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2*vphi1*vphi1 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*vphi1*vphi1)*sintheta1*sintheta1 - (((l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta1 - ((l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*sintheta1*sintheta1)*vtheta1*vtheta1 - ((g*m2*cosphi1*cosphi1*cosphi1 + g*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (g*m2*cosphi1*cosphi1*sinphi1 + g*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (g*m2*cosphi1*cosphi1*cosphi1 + g*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (g*m2*cosphi1*cosphi1*sinphi1 + g*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1)*costheta2*sintheta2 - (((l2*m2*cosphi1*cosphi1 + l2*m2*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*(l2*m2*cosphi1*cosphi1 + l2*m2*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + (l2*m2*cosphi1*cosphi1 + l2*m2*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*costheta2*sintheta1*vphi2*vphi2 - (2*l1*m2*cosphi1*cosphi2*sinphi1*sinphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1 - l1*m1*cosphi1*cosphi1 + (2*(l1*m1 + l1*m2)*cosphi1*cosphi1 - l1*m1 - l1*m2)*sinphi1*sinphi1)*cosphi2*cosphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1 - (l1*m1 + l1*m2)*cosphi1*cosphi1 + (2*(l1*m1 + l1*m2)*cosphi1*cosphi1 - l1*m1)*sinphi1*sinphi1)*sinphi2*sinphi2)*costheta1*sintheta1*vtheta1*vtheta1 - (2*g*m2*cosphi1*cosphi2*sinphi1*sinphi2 - (g*m1*cosphi1*cosphi1 + (g*m1 + g*m2)*sinphi1*sinphi1)*cosphi2*cosphi2 - (g*m1*sinphi1*sinphi1 + (g*m1 + g*m2)*cosphi1*cosphi1)*sinphi2*sinphi2 + (((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*vphi1*vphi1 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*vphi1*vphi1)*costheta1)*sintheta1)*sintheta2*sintheta2 - (((l2*m2*cosphi1*cosphi1 + l2*m2*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*(l2*m2*cosphi1*cosphi1 + l2*m2*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + (l2*m2*cosphi1*cosphi1 + l2*m2*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*costheta2*costheta2*costheta2*sintheta1 - ((l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta2*costheta2*sintheta2 + ((l2*m2*cosphi1*cosphi1 + l2*m2*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*(l2*m2*cosphi1*cosphi1 + l2*m2*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + (l2*m2*cosphi1*cosphi1 + l2*m2*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*costheta2*sintheta1*sintheta2*sintheta2 - ((l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*sintheta2*sintheta2*sintheta2)*vtheta2*vtheta2)/(2*((l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta2*sintheta1*sintheta2 - (((l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l1*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*(l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l1*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + (l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l1*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*costheta1*costheta1 + (((l1*m1 + l1*m2)*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*((l1*m1 + l1*m2)*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*sintheta1*sintheta1)*costheta2*costheta2 - ((((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2)*costheta1*costheta1 - (2*l1*m2*cosphi1*cosphi2*sinphi1*sinphi2 - (l1*m1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1)*cosphi2*cosphi2 - (l1*m1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*cosphi1*cosphi1)*sinphi2*sinphi2)*sintheta1*sintheta1)*sintheta2*sintheta2)


def teta2_tacka_tacka(m1, m2, l1, l2, theta1, theta2, phi1, phi2,
                 vtheta1, vtheta2, vphi1, vphi2):

	sintheta1 = sin(theta1)
	sintheta2 = sin(theta2)
	costheta1 = cos(theta1)
	costheta2 = cos(theta2)
	sinphi1   = sin(phi1)
	sinphi2   = sin(phi2)
	cosphi1   = cos(phi1)
	cosphi2   = cos(phi2)
	return (((l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*sintheta1*sintheta2*sintheta2*vphi2*vphi2 - (((l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta2*costheta2*sintheta1 - ((l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*sintheta1*sintheta2*sintheta2 + (((l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + (l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2 - ((l2*m1 + l2*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l2*m1 + l2*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2 - ((l2*m1 + l2*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l2*m1 + l2*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1*sinphi1*sinphi1 - 2*(l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2)*sinphi2*sinphi2)*costheta1*costheta1 + (2*l2*m2*cosphi1*cosphi2*sinphi1*sinphi2 + ((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + ((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2 - (l2*m1*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2 - (l2*m1*sinphi1*sinphi1 + (l2*m1 + l2*m2)*cosphi1*cosphi1 - 2*((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2)*sinphi2*sinphi2)*sintheta1*sintheta1)*costheta2*sintheta2)*vtheta2*vtheta2 - ((((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*vphi1*vphi1 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*vphi1*vphi1 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2*vphi1*vphi1 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*vphi1*vphi1)*sintheta1*sintheta1*sintheta1 + (((g*m1 + g*m2)*cosphi1*cosphi1*cosphi1 + (g*m1 + g*m2)*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + ((g*m1 + g*m2)*cosphi1*cosphi1*sinphi1 + (g*m1 + g*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + ((g*m1 + g*m2)*cosphi1*cosphi1*cosphi1 + (g*m1 + g*m2)*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + ((g*m1 + g*m2)*cosphi1*cosphi1*sinphi1 + (g*m1 + g*m2)*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*sintheta1 + ((((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta1*sintheta1 + (((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*sintheta1*sintheta1*sintheta1)*vtheta1*vtheta1)*costheta2 + ((((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*vphi1*vphi1 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*vphi1*vphi1)*costheta1*sintheta1*sintheta1 + (((g*m1 + g*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(g*m1 + g*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (g*m1 + g*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2 + ((g*m1 + g*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(g*m1 + g*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (g*m1 + g*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2)*costheta1*costheta1 + ((((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2)*costheta1*costheta1*costheta1 + (((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2)*costheta1*sintheta1*sintheta1)*vtheta1*vtheta1 - (((l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*(l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + (l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*costheta1*costheta1*vphi2*vphi2 + (((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + ((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*sintheta1*sintheta1*vphi2*vphi2)*costheta2)*sintheta2)/(2*((l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta2*sintheta1*sintheta2 - (((l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*(l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + (l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*costheta1*costheta1 + (((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + ((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*sintheta1*sintheta1)*costheta2*costheta2 - ((((l2*m1 + l2*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l2*m1 + l2*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2 + ((l2*m1 + l2*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l2*m1 + l2*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2)*costheta1*costheta1 - (2*l2*m2*cosphi1*cosphi2*sinphi1*sinphi2 - (l2*m1*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2 - (l2*m1*sinphi1*sinphi1 + (l2*m1 + l2*m2)*cosphi1*cosphi1)*sinphi2*sinphi2)*sintheta1*sintheta1)*sintheta2*sintheta2)



def fi1_tacka_tacka(m1, m2, l1, l2, theta1, theta2, phi1, phi2,
                 vtheta1, vtheta2, vphi1, vphi2):
	
	sintheta1 = sin(theta1)
	sintheta2 = sin(theta2)
	costheta1 = cos(theta1)
	costheta2 = cos(theta2)
	sinphi1   = sin(phi1)
	sinphi2   = sin(phi2)
	cosphi1   = cos(phi1)
	cosphi2   = cos(phi2)
	return ((((l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 - (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 - (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta1*vphi2*vphi2 + (l2*m2*cosphi2*cosphi2*cosphi2*sinphi1 - l2*m2*cosphi1*cosphi2*cosphi2*sinphi2 + l2*m2*cosphi2*sinphi1*sinphi2*sinphi2 - l2*m2*cosphi1*sinphi2*sinphi2*sinphi2)*sintheta1*sintheta1*vphi2*vphi2)*sintheta2*sintheta2*sintheta2 + 2*(((l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l1*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2*vphi1 + 2*(l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l1*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2*vphi1 + (l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l1*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2*vphi1)*costheta1*costheta1*costheta1 + (((l1*m1 + l1*m2)*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2*vphi1 + 2*((l1*m1 + l1*m2)*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2*vphi1 + ((l1*m1 + l1*m2)*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2*vphi1)*costheta1*sintheta1*sintheta1)*costheta2*costheta2*vtheta1 - (4*((l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*vphi1 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*vphi1 + (l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2*vphi1 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*vphi1)*costheta1*costheta1*sintheta1*vtheta1 - ((l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*vphi1*vphi1 - (l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*vphi1*vphi1 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2*vphi1*vphi1 - (l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*vphi1*vphi1)*costheta1*sintheta1*sintheta1 - ((g*m2*cosphi1*cosphi1*sinphi1 + g*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 - (g*m2*cosphi1*cosphi1*cosphi1 + g*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (g*m2*cosphi1*cosphi1*sinphi1 + g*m2*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 - (g*m2*cosphi1*cosphi1*cosphi1 + g*m2*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta1 - (((l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 - (l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 - (l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta1*costheta1 + ((l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 - (l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 - (l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*sintheta1*sintheta1)*vtheta1*vtheta1)*costheta2*sintheta2 + ((l1*m2*cosphi1*cosphi2*cosphi2*sinphi1*vphi1*vphi1 - l1*m2*cosphi1*sinphi1*sinphi2*sinphi2*vphi1*vphi1 - (l1*m2*cosphi1*cosphi1 - l1*m2*sinphi1*sinphi1)*cosphi2*sinphi2*vphi1*vphi1)*sintheta1*sintheta1*sintheta1 + (g*m2*cosphi1*cosphi2*cosphi2*sinphi1 - g*m2*cosphi1*sinphi1*sinphi2*sinphi2 - (g*m2*cosphi1*cosphi1 - g*m2*sinphi1*sinphi1)*cosphi2*sinphi2)*costheta1*sintheta1 + ((l1*m2*cosphi1*cosphi2*cosphi2*sinphi1 - l1*m2*cosphi1*sinphi1*sinphi2*sinphi2 - (l1*m2*cosphi1*cosphi1 - l1*m2*sinphi1*sinphi1)*cosphi2*sinphi2)*costheta1*costheta1*sintheta1 + (l1*m2*cosphi1*cosphi2*cosphi2*sinphi1 - l1*m2*cosphi1*sinphi1*sinphi2*sinphi2 - (l1*m2*cosphi1*cosphi1 - l1*m2*sinphi1*sinphi1)*cosphi2*sinphi2)*sintheta1*sintheta1*sintheta1)*vtheta1*vtheta1 + 2*((((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*vphi1 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*vphi1)*costheta1*costheta1*costheta1 - (2*l1*m2*cosphi1*cosphi2*sinphi1*sinphi2*vphi1 - (l1*m1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*vphi1 - (l1*m1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*cosphi1*cosphi1)*sinphi2*sinphi2*vphi1)*costheta1*sintheta1*sintheta1)*vtheta1)*sintheta2*sintheta2 + ((((l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 - (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 - (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta1 + (l2*m2*cosphi2*cosphi2*cosphi2*sinphi1 - l2*m2*cosphi1*cosphi2*cosphi2*sinphi2 + l2*m2*cosphi2*sinphi1*sinphi2*sinphi2 - l2*m2*cosphi1*sinphi2*sinphi2*sinphi2)*sintheta1*sintheta1)*costheta2*costheta2*sintheta2 + (((l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 - (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 - (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta1 + (l2*m2*cosphi2*cosphi2*cosphi2*sinphi1 - l2*m2*cosphi1*cosphi2*cosphi2*sinphi2 + l2*m2*cosphi2*sinphi1*sinphi2*sinphi2 - l2*m2*cosphi1*sinphi2*sinphi2*sinphi2)*sintheta1*sintheta1)*sintheta2*sintheta2*sintheta2)*vtheta2*vtheta2)/(2*((l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l1*m2*cosphi1*cosphi1*cosphi1 + l1*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l1*m2*cosphi1*cosphi1*sinphi1 + l1*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta2*sintheta1*sintheta1*sintheta2 - (((l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l1*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*(l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l1*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + (l1*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l1*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l1*m1*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*costheta1*costheta1*sintheta1 + (((l1*m1 + l1*m2)*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*((l1*m1 + l1*m2)*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*sintheta1*sintheta1*sintheta1)*costheta2*costheta2 - ((((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2)*costheta1*costheta1*sintheta1 - (2*l1*m2*cosphi1*cosphi2*sinphi1*sinphi2 - (l1*m1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1)*cosphi2*cosphi2 - (l1*m1*sinphi1*sinphi1 + (l1*m1 + l1*m2)*cosphi1*cosphi1)*sinphi2*sinphi2)*sintheta1*sintheta1*sintheta1)*sintheta2*sintheta2)



def fi2_tacka_tacka(m1, m2, l1, l2, theta1, theta2, phi1, phi2,
                 vtheta1, vtheta2, vphi1, vphi2):
	
	sintheta1 = sin(theta1)
	sintheta2 = sin(theta2)
	costheta1 = cos(theta1)
	costheta2 = cos(theta2)
	sinphi1   = sin(phi1)
	sinphi2   = sin(phi2)
	cosphi1   = cos(phi1)
	cosphi2   = cos(phi2)
	return -((l2*m2*cosphi1*cosphi2*cosphi2*sinphi1 - l2*m2*cosphi1*sinphi1*sinphi2*sinphi2 - (l2*m2*cosphi1*cosphi1 - l2*m2*sinphi1*sinphi1)*cosphi2*sinphi2)*sintheta1*sintheta1*sintheta2*sintheta2*sintheta2*vphi2*vphi2 + ((((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*vphi1*vphi1 - ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*vphi1*vphi1 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2*vphi1*vphi1 - ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*vphi1*vphi1)*sintheta1*sintheta1*sintheta1 + (((g*m1 + g*m2)*cosphi1*cosphi1*sinphi1 + (g*m1 + g*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 - ((g*m1 + g*m2)*cosphi1*cosphi1*cosphi1 + (g*m1 + g*m2)*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + ((g*m1 + g*m2)*cosphi1*cosphi1*sinphi1 + (g*m1 + g*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 - ((g*m1 + g*m2)*cosphi1*cosphi1*cosphi1 + (g*m1 + g*m2)*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*sintheta1 + ((((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 - ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 - ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta1*sintheta1 + (((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 - ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + ((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 - ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*sintheta1*sintheta1*sintheta1)*vtheta1*vtheta1)*costheta2*costheta2 + (((l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 - (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 - (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta2*sintheta1*vphi2*vphi2 + (((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*cosphi2*vphi1*vphi1 - ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*sinphi2*vphi1*vphi1)*sintheta1*sintheta1*sintheta1 + (((g*m1 + g*m2)*cosphi1*cosphi1*sinphi1 + (g*m1 + g*m2)*sinphi1*sinphi1*sinphi1)*cosphi2 - ((g*m1 + g*m2)*cosphi1*cosphi1*cosphi1 + (g*m1 + g*m2)*cosphi1*sinphi1*sinphi1)*sinphi2)*costheta1*sintheta1 + ((((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*cosphi2 - ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*sinphi2)*costheta1*costheta1*sintheta1 + (((l1*m1 + l1*m2)*cosphi1*cosphi1*sinphi1 + (l1*m1 + l1*m2)*sinphi1*sinphi1*sinphi1)*cosphi2 - ((l1*m1 + l1*m2)*cosphi1*cosphi1*cosphi1 + (l1*m1 + l1*m2)*cosphi1*sinphi1*sinphi1)*sinphi2)*sintheta1*sintheta1*sintheta1)*vtheta1*vtheta1)*sintheta2*sintheta2 + (((l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 - (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 - (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta2*costheta2*costheta2*sintheta1 + (l2*m2*cosphi1*cosphi2*cosphi2*sinphi1 - l2*m2*cosphi1*sinphi1*sinphi2*sinphi2 - (l2*m2*cosphi1*cosphi1 - l2*m2*sinphi1*sinphi1)*cosphi2*sinphi2)*costheta2*costheta2*sintheta1*sintheta1*sintheta2 + ((l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 - (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 - (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta2*sintheta1*sintheta2*sintheta2 + (l2*m2*cosphi1*cosphi2*cosphi2*sinphi1 - l2*m2*cosphi1*sinphi1*sinphi2*sinphi2 - (l2*m2*cosphi1*cosphi1 - l2*m2*sinphi1*sinphi1)*cosphi2*sinphi2)*sintheta1*sintheta1*sintheta2*sintheta2*sintheta2)*vtheta2*vtheta2 + 2*(2*((l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta2*costheta2*sintheta1*sintheta2*vphi2 - (((l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*(l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + (l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*costheta1*costheta1*vphi2 + (((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + ((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*sintheta1*sintheta1*vphi2)*costheta2*costheta2*costheta2 - ((((l2*m1 + l2*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l2*m1 + l2*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2 + ((l2*m1 + l2*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l2*m1 + l2*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2)*costheta1*costheta1*vphi2 - (2*l2*m2*cosphi1*cosphi2*sinphi1*sinphi2 - (l2*m1*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2 - (l2*m1*sinphi1*sinphi1 + (l2*m1 + l2*m2)*cosphi1*cosphi1)*sinphi2*sinphi2)*sintheta1*sintheta1*vphi2)*costheta2*sintheta2*sintheta2)*vtheta2)/(2*((l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*cosphi1 + l2*m2*cosphi1*sinphi1*sinphi1)*cosphi2*sinphi2*sinphi2 + (l2*m2*cosphi1*cosphi1*sinphi1 + l2*m2*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2)*costheta1*costheta2*sintheta1*sintheta2*sintheta2 - (((l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*(l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + (l2*m1*cosphi1*cosphi1*cosphi1*cosphi1 + 2*l2*m1*cosphi1*cosphi1*sinphi1*sinphi1 + l2*m1*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*costheta1*costheta1 + (((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*cosphi2*cosphi2 + 2*((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2*sinphi2*sinphi2 + ((l2*m1 + l2*m2)*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*sinphi2*sinphi2*sinphi2*sinphi2)*sintheta1*sintheta1)*costheta2*costheta2*sintheta2 - ((((l2*m1 + l2*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l2*m1 + l2*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*cosphi2*cosphi2 + ((l2*m1 + l2*m2)*cosphi1*cosphi1*cosphi1*cosphi1 + 2*(l2*m1 + l2*m2)*cosphi1*cosphi1*sinphi1*sinphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1*sinphi1*sinphi1)*sinphi2*sinphi2)*costheta1*costheta1 - (2*l2*m2*cosphi1*cosphi2*sinphi1*sinphi2 - (l2*m1*cosphi1*cosphi1 + (l2*m1 + l2*m2)*sinphi1*sinphi1)*cosphi2*cosphi2 - (l2*m1*sinphi1*sinphi1 + (l2*m1 + l2*m2)*cosphi1*cosphi1)*sinphi2*sinphi2)*sintheta1*sintheta1)*sintheta2*sintheta2*sintheta2)

#dodato -1 ispred z koordinate
def poz1(m1,l1,theta1,phi1):
    return [l1*sin(theta1)*cos(phi1),l1*sin(theta1)*sin(phi1),-1*l1*cos(theta1)]


def poz2(m1,m2,l1,l2,theta1,theta2, phi1,phi2):
    p1 = poz1(m1,l1,theta1,phi1)
    return [p1[0] + l2*sin(theta2)*cos(phi2),p1[1] + l2*sin(theta2)*sin(phi2),p1[2]-l2*cos(theta2)]