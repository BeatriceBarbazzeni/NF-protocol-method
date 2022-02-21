# NF-protocol-method
# Author: Beatrice Barbazzeni 
# Otto-von-Guericke University of Magdeburg

# receiveLslData_Alpha.py


"""Example program to show how to read a multi-channel time series from LSL."""
import time
from pylsl import StreamInlet, resolve_stream
import numpy as np
 
# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

timeout = time.time() + 60*7    # interger value result should be in seconds for 5 minutes 60*5 from now (5 min is the time for each NF-training run)
dataList=[]
while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample=inlet.pull_sample() 
    sample=list(sample)
    sample=sample.pop(0)
    
   
    dataList.append(sample)
        
    print(sample)
    
    """test+=1+
    print(str(test))"""
    if time.time() > timeout: 
        break
dataMatrix=np.matrix(dataList)
dataMatrix.mean()
np.savetxt('S00_Day1_Block1.txt', dataMatrix)
