# NF-protocol-method
# Author: Beatrice Barbazzeni 
# Otto-von-Guericke University of Magdeburg

# Block_NF_Alpha.py


"""
@author: beatrice barbazzeni
"""

# ======= PSYCHOPY ======
from __future__ import absolute_import, division
from psychopy import gui, visual, core, event
import os
from random import shuffle
from PIL import Image as image
import numpy as np
import time
from scipy.signal import firwin, lfilter, iirnotch
from scipy.fftpack import fft2
from pylsl import StreamInlet, resolve_stream
import random
import pandas as pd
import sys
import glob


try:
    
    
     event.globalKeys.add(key='q', modifiers=['ctrl'], func=core.quit, name='shutdown')
     startClock = core.Clock() #creates a clock time
     time1_start_trial = startClock.getTime() # gets time at this point 
     dataList1=[]
     
     # Ensure that relative paths start from the same directory as this script
     _thisDir = os.path.dirname(os.path.abspath(__file__))
     os.chdir(_thisDir)
     
     # Store info about the experiment session
     expName = 'Patient Study'  # from the Builder filename that created this script
     expInfo = {u'gender': u'', u'age': u'', u'participant': u'', u'group' : u'',
               u'nBlocks' : u'', u'Day' : u'', u'Alpha1' : u'', u'Alpha2' : u'' }
     dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
     if dlg.OK == False: 
        core.quit() 

# ===== initialisation of var ==== ========== 
        
     trial=range(1, 13)
     BlockCount=2         #no. of blocks
     TrialCount=24 
     dataList1=[]
     Magnitude=list(np.zeros(int(TrialCount/2)))
     BallPos=np.zeros(int(TrialCount/2)) # CHANGE HERE
     streams = []
     inlet = ()
     sample = ()
     Reward=np.zeros(int(TrialCount/2))
     NoReward=np.zeros(int(TrialCount/2))
     
    
    
    
# ============= Start of the experiment =========     
     """Creating Window for the Experiments"""
     win = visual.Window(size=(1650, 1050),fullscr=True, screen=0, allowGUI=False, allowStencil=False,
                     monitor='testMonitor', color='grey', colorSpace='rgb',
                     blendMode='avg', useFBO=True, units='norm')
     
     # full screen parameter is size=size=(1650, 1050),fullscr=True
 
     message1 = visual.TextStim(win, text='Drücken Sie die Leertaste, um das Experiment zu starten', color='black', pos=(0.5,0.0), alignHoriz='center')
     
     message1.draw()
     win.flip()
    
     
     keyPressed = event.waitKeys(keyList=['period','slash','space'], modifiers=False)#, timeStamped=exampleClock) 
       
     if keyPressed: 
        time2_star_trial = startClock.getTime()
        responseStartTime = time2_star_trial - time1_start_trial
        responseStartTime=round(responseStartTime,3)
        
        
        # ===== Instruction of the experiment ============
        message2 = visual.TextStim(win, text='Jetzt sehen Sie eine weiße Kugel, die sich bewegt', color='black', pos=(0.5,0.0), alignHoriz='center')
        #cube=visual.Rect(win, width=0.035, height=0.06, autoLog=None)
        message2.draw()
        win.flip() 
        core.wait(6.0)
        
        message3 = visual.TextStim(win, text='Versuchen Sie, die Bewegung des Balls nach oben zu steuern', color='black', pos=(0.5,0.0), alignHoriz='center')
        message3.draw()
        win.flip() 
        core.wait(6.0)
        
        
        
        
     for i in range (0,12):
         
           #from baseline import baselineNormValue
           message_fixBase = visual.TextStim(win, text='+', color='black', pos=(0.97,0.0),alignHoriz='center')
           message_fixBase.draw()# change properties of existing stim
           win.flip()
           from baseline import baselineNormValue
          
   
        # =====                =============== #
        # ====== NEUROFEEDBACK =============== # 
        # ======               =============== #
        
           ntaps = 101 ###filter order
           fs = 250.0  ###sample freq
           lowcut = int(expInfo['Alpha1'])  ###band pass f1
           highcut = int(expInfo['Alpha2']) ###band pass f2
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
    
        
           ball = visual.Circle(
                    win=win,
                    units="pix",
                    radius=50,
                    fillColor='white',
                    lineColor=[-1, -1, -1],
                    edges=128,
                    pos=[0,50]
                    )
           ballpos=[]#### ball position for the loop
            
           line=visual.Line(win=win, start=(-0.5,0), end=(0.5,0), pos=[0,0])
        
            ############Time set for NF 20 sec
           timeout = time.time() + 20 #60*16   # interger value result should be in seconds for 5 minutes 60*5 from now
       
           while True:
                     print("looking for an EEG stream...")
                     streams = resolve_stream('type', 'EEG')
                     inlet = StreamInlet(streams[0])
                     line.draw()
                     ball.draw()
                     win.flip()
                     timeout2 = time.time() + 0.25
                
                     while True: #time.time() < timeout2:  
                           sample=inlet.pull_sample() 
                           sample=list(sample)
                           sample=sample.pop(0)
                
                           dataList1.append(sample)
    
                           if time.time() > timeout2: 
                              break
    
                     dataMatrix=np.matrix(dataList1)
                
    
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
                     magnitude=fftAbsMatrix.mean()
                
                     mag = (100*(magnitude-baselineNormValue))/baselineNormValue
                     mag=abs(mag) 
                     Magnitude[i]=mag
            
                
                
                     if mag < 40:
                         mag = random.randint(280,300)+baselineNormValue
                     elif mag >=40 and mag < 80:
                         mag = random.randint(200,220)+baselineNormValue
                     elif mag >=80 and mag < 120:
                         mag = random.randint(110,150)+baselineNormValue
                     elif mag >=120:
                         mag = random.randint(50,70)+baselineNormValue
                    
                    
                     ballpos.append(mag)   
                
    
                
                
                     ball.pos=[0,mag]
                     
                     if time.time() > timeout: 
                         break
                                
       
            
           del sys.modules["baseline"]
           BallPos[i]=round(sum(ballpos)/len(ballpos))
           
           
           ###### display the reward ######
           
           if  200+baselineNormValue <= BallPos[i] <= 300+baselineNormValue:
               
              img = visual.ImageStim(win=win,image="/Users/barbazze/Documents/Psychopy/Patient Study I/images/smile.png",units="pix") # HERE UPDATE THE FOLDER YOU HAVE STORED THE REWARD IMAGES
              Reward[i] = 1
              size_x = img.size[0]
              size_y = img.size[1]

              img.size = [size_x * 1.5, size_y * 1.5]

              img.draw()

              win.flip()
              core.wait(2.0)
           
           else: 
              img2 = visual.ImageStim(win=win,image="/Users/barbazze/Documents/Psychopy/Patient Study I/images/neutral.png",units="pix") # HERE UPDATE THE FOLDER YOU HAVE STORED THE REWARD IMAGES
              NoReward[i] = 1
              size_x = img2.size[0]
              size_y = img2.size[1]

              img2.size = [size_x * 1.5, size_y * 1.5]

              img2.draw()

              win.flip()
              core.wait(2.0)
           
        
        # ====== End of the BLOCK =========== 
     
        
     message4 = visual.TextStim(win, text='Ende des Blocks', color='black', pos=(0.5,0.0), alignHoriz='center')
     message4.draw()
     win.flip()
     event.waitKeys()
     
        
 
     df = pd.DataFrame({'SubID':expInfo['participant'] , 'SubAge': expInfo['age'], 'Gender': expInfo['gender'],
                           'Group':expInfo['group'],'Day':expInfo['Day'],'Block':expInfo['nBlocks'], 
                           'Alpha 1':expInfo['Alpha1'], 'Alpha 2':expInfo['Alpha2'],
                           'BallPos':BallPos,'StartingRT':responseStartTime,
                           "Reward":Reward, "NoReward":NoReward})
     
     df.to_excel(expInfo['participant']+"_Day"+expInfo['Day']+"_Block"+expInfo['nBlocks']+"_Alpha"+".xlsx", index = False)
        
     win.close()
     core.quit()
     exit()
        


except Exception as e:
    print(e)
    win.close()