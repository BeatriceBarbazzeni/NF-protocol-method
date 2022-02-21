# NF-protocol-method
# Author: Beatrice Barbazzeni 
# Otto-von-Guericke University of Magdeburg

# alphaRangeBaseline.py


from psychopy import visual, core
from pylsl import StreamInlet, resolve_stream
import numpy as np
from scipy.signal import firwin, lfilter, iirnotch
import time
from scipy.fftpack import fft

alpha1_Peak = []
alpha2_Peak = []
alpha3_Peak = []
 
try:
    
    
    win=visual.Window(size=(1650, 1050),fullscr=True, screen=0, allowGUI=False, allowStencil=False,
                          monitor='testMonitor', color='grey', colorSpace='rgb',
                          blendMode='avg', useFBO=True,
                          units='norm'
                          )
    message_fixBase = visual.TextStim(win, text='+', color='black', pos=(0.97,0.0),alignHoriz='center')
    message_fixBase.draw()#
    win.flip()
    
    if len(resolve_stream()) != 0:
        
        dataList=[]

        streams = resolve_stream('type', 'EEG')

        # create a new inlet to read from the stream
        inlet = StreamInlet(streams[0])

        timeout = time.time() + 60*2
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
        lowcut = 3  ###band pass f1
        
        highcut = 11  ###band pass f2
        cutoff=50     ###low pass cut off
        nyq = 0.5 * fs
        f0 = 50.0  # Frequency to be removed from signal (Hz)
        Q = 30.0  # Quality factor
        w0 = f0/(fs/2)
        hpCutoff=1
        
        
        # you can apply different filters before applying the bandpass for alpha.
        # otherwise you can directly filter for alpha range (thus, only using the bandpass filter)
        
        
        """LowPass Filter"""
        lFilt=firwin(ntaps, cutoff = 50, fs=fs, window = "hanning")
        lpFilterData=lfilter(lFilt, 1.0, dataMatrix)
        """highpass"""
        hFilt=firwin(ntaps, hpCutoff, fs=fs, window = "hanning", pass_zero=False)
        hpFilterData=lfilter(hFilt,1.0,lpFilterData)
        """Notch Filter"""
        nFilt, a=iirnotch(w0, Q)
     
        nFilterData=lfilter(nFilt, 1.0, hpFilterData)
        
        
        """BandPass Filter Range 4-8 Hz"""
        bFilt=firwin(ntaps, [4, 8], fs=fs, pass_zero=False, window="hanning", scale=False)
        bpFilterData_4_8 = lfilter(bFilt, 1.0, nFilterData)
        """BandPass Filter Range 6-9 Hz"""
        bFilt=firwin(ntaps, [6, 9], fs=fs, pass_zero=False, window="hanning", scale=False)
        bpFilterData_6_9 = lfilter(bFilt, 1.0, nFilterData)
        """BandPass Filter Range 7-10 Hz"""
        bFilt=firwin(ntaps, [7, 10], fs=fs, pass_zero=False, window="hanning", scale=False)
        bpFilterData_7_10 = lfilter(bFilt, 1.0, nFilterData)
    
        fftbpFilterData_4_8 =fft(bpFilterData_4_8)
        fftbpFilterData_6_9 =fft(bpFilterData_6_9)
        fftbpFilterData_7_10 =fft(bpFilterData_7_10)
    
    
        alpha_1=np.abs(fftbpFilterData_4_8.max())
        alpha_2=np.abs(fftbpFilterData_6_9.max())
        alpha_3=np.abs(fftbpFilterData_7_10.max())
        
  
   
    
        if alpha_1> alpha_3 and alpha_1>alpha_2:
            print('Alpha Range is 4-8 Hz')
            #print(alpha1_Peak)
        elif alpha_2> alpha_3 and alpha_2>alpha_1:
            print('Alpha Range is 6-9 Hz')
            #print(alpha2_Peak)
        elif alpha_3> alpha_1 and alpha_3>alpha_2:
            print('Alpha Range is 7-10 Hz')
           # print(alpha3_Peak)
        
        
        
   
    
        win.close()
        core.quit()
    else:
        exit()
        quit()
    
except Exception as e:
    print(e)
    win.close()
