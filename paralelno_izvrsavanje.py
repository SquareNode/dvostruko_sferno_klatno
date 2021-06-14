from time import time, sleep
import sys
import multiprocessing as mp
from paralelno_main import dvostruko_sferno_klatno

if __name__ == '__main__':
    
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
    
    p = []
    for arg in my_args:
        p.append(mp.Process(target = dvostruko_sferno_klatno, args = arg))
        p[-1].start()
        
    for x in range(len(my_args)):
        p[x].join()