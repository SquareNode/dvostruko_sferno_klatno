from formule_superast import teta1_tacka_tacka, teta2_tacka_tacka, fi1_tacka_tacka,\
fi2_tacka_tacka, poz1, poz2

def dvostruko_sferno_klatno(l1,l2,m1,m2,fi1,fi2,teta1,teta2,fi1_tacka,
                            fi2_tacka, teta1_tacka, teta2_tacka, tmax):
    t = 0
    dt = 1e-3
    
    k1s, k2s = [],[]
    
    while t < tmax:
        
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
        
        k1s.append(k1)
        k2s.append(k2)
        
        t+=dt