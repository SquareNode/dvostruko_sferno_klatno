from time import time
import sys
import multiprocessing as mp
from paralelno_main import dvostruko_sferno_klatno

if __name__ == '__main__':
    
    #teta -> ugao sa vertikalom (2D klatno)
    #fi -> ugao sa horizontalom
    #l1 l2 m1 m2 fi1 fi2 teta1 teta2 fi1_tacka fi2_t teta1_t teta2_t tmax
    my_args = [[1,1,1,1,0.14,0.3,0.1,0.13,0,0,0,0,10], 
               [1,1,1.3,1,0.34,0.31,0.12,0.3,3,0.5,0,0,20],
                [1,1,1,1,0.6,-0.1,1.3,-0.3,1,0.5,0,0.1,11],
                [1.5,1,1,1,0,0,0.12,0.3,3,0.5,0,0,10],
                [1,1,1.3,1,0.34,0.31,0.12,0.3,3,0.5,0,0,5],
                [1,1,1.3,1,0.34,0.31,0.12,0.3,3,0.5,0,0,14],
                [1,1,1,1.1,1,-0.31,0.2,-0.3,-0.9,0.5,0,0,15],
                [1,2,1,1.3,-1,0.4,0.12,-0.4,1,0,1,-1,13],
                [1.6,1.3,1.2,0.5,-0.3,1.1,0.2,-0.2,0.1,0.1,-0.1,0.1,10],
                [1.1,0.7,0.6,0.7,1.2,1.3,-1,-2,0.1,-0.6,1,0,10]]
    
    poc = time()
   
    for arg in my_args:
        dvostruko_sferno_klatno(*arg)
    
    print('sekv: ', time() - poc, 's')
    
    poc = time()
    
    p = []
    for arg in my_args:
        p.append(mp.Process(target = dvostruko_sferno_klatno, args = arg))
        p[-1].start()
        
    for x in range(len(my_args)):
        p[x].join()
        
    print('sa paral: ', time() - poc, 's')
    