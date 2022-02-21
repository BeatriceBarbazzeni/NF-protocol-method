# NF-protocol-method
# Author: Beatrice Barbazzeni 
# Otto-von-Guericke University of Magdeburg

# parallelBlock_Alpha.py


import os 
from multiprocessing import Pool

processes = {'receiveLslData_Alpha.py','Block_NF_Alpha.py'}

def run_process(process):
    os.system('python {}'.format(process))
    
    
pool = Pool(processes=2)
pool.map(run_process, processes)

