# NF-protocol-method
# Author: Beatrice Barbazzeni 
# Otto-von-Guericke University of Magdeburg

# baseline.py



import time
from pylsl import StreamInlet, resolve_stream
import numpy as np
from scipy.signal import firwin, lfilter, iirnotch
from scipy.fftpack import fft2


try:
    
    dataList=[]
    
    if len(resolve_stream()) != 0:
    
        print("looking for an EEG stream...")  
        streams = resolve_stream('type', 'EEG')
        
                
        # create a new inlet to read from the stream
        inlet = StreamInlet(streams[0])

        timeout = time.time() + 6
        while True:
            # get a new sample (you can also omit the timestamp part if you're not
            # interested in it)
            sample=inlet.pull_sample()
            sample=list(sample)
            sample=sample.pop(0)
        
            dataList.append(sample)
        
            print(sample)
  
            """test+=1
            print(str(test))"""
            if time.time() > timeout: 
                break
        

        dataMatrix=np.matrix(dataList)

        ntaps = 101 ###filter order
        fs = 250.0  ###sample freq
        lowcut = 4  ###band pass f1
        
        highcut = 8  ###band pass f2
        cutoff=50     ###low pass cut off
        hpCutoff=1
        nyq = 0.5 * fs
        f0 = 50.0  # Frequency to be removed from signal (Hz)
        Q = 30.0  # Quality factor
        w0 = f0/(fs/2)
        nFilt, a=iirnotch(w0, Q) ###Notch Filter
        lFilt=firwin(ntaps, cutoff=50, fs=fs, window = "hanning") ### Lowpass Filter
        bFilt=firwin(ntaps, [lowcut, highcut], fs=fs, pass_zero=False, 
                     window="hanning", scale=False)####Bandpass Filter
        hFilt=firwin(ntaps, hpCutoff, fs=fs, window = "hanning", pass_zero=False)
        
        """LowPass Filter"""
        lpFilterData=lfilter(lFilt, 1.0, dataMatrix)
        """HigPass Filter"""
        hpFilterData=lfilter(hFilt,1.0,lpFilterData)
        """Notch Filter"""
        
        nFilterData=lfilter(nFilt, 1.0, hpFilterData)
        """BandPass Filter"""
        bpFilterData = lfilter(bFilt, 1.0, nFilterData)

        # FFT algorithm
        fftMatrix = fft2(bpFilterData) # "raw" FFT with both + and - frequencies
        fftAbsMatrix=np.abs(fftMatrix) # positive freqs only
        baselineNormValue=fftAbsMatrix.mean()
        
    else:
        
        quit()
        exit()
except Exception as e:
    print(e)




