# NF-protocol-method
Python codes of the NF-training method proposed for the NF-training protocol in preclinical Alzheimer's disease.

The proposed NF-training method is part of the research conducted in my doctoral thesis work: "Cognitive Training Based on EEG Neurofeedback to Improve Working Memory: A Research Study on Healthy Volunteers with an Outlook on Preclinical Alzheimer’s Disease", Faculty of Natural Science at the Otto-von-Guericke University of Magdeburg. 

Supervisors: Prof. Dr. med. Emrah Duezel
             Prof. Dr. Oliver Speck

------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
             
* NB: OpenBCI Cyton Board 8-Channel has been used with a Macbook Pro (13-inch, 2018), processor 2.3 GHz Intel   Core i5, 8 GB memory

* The OpenBCI Cyton Board 8-Channel sample the signal at 250 Hz

* I suggest using OpenBCI with iOS and the instructions below are for iOS users


Task code instructions:

1. Download Python (with Anaconda) and choose your Python IDE. I suggest Spider. The version of Python that I used for coding is 3.7.3

2. Download PsychoPy2 (ref: Peirce, J. W., Gray, J. R., Simpson, S., MacAskill, M. R., Höchenberger, R., Sogo, H., Kastman, E., and Lindeløv, J. (2019). PsychoPy2: experiments in behaviour made easy. Behaviour Research Methods. DOI: 10.3758/s13428-018-01193-y)

3. Download Lab Streaming Layer (LSL) https://github.com/sccn/labstreaminglayer and save it in your "User/Documents/Psychopy" folder under a new folder in "User/Documents/Psychopy/OPENBCI_LSL". 

4. In the folder "User/Documents/Psychopy/OPENBCI_LSL", you can find a file named "openbci_lsl.py".

* switch on the Cyton Board, connected with the USB Dongle

5. Open your terminal and set your path to "Documents/Psychopy/OpenBCI_LSL/".

6. In "Documents/Psychopy/OpenBCI_LSL/" path, open the file "openbci_lsl.py /dev/tty.usbserial-DM00QAZP --stream" to start the neurofeedback stream .

7. Type "/start" to start the stream.

8. In your Python IDE, run the code "receiveLslData_Alpha.py" to check if the stream works. If yes, press "control + C" in the Console to stop the stream. Remember to rename the output file that you want to save (e.g., S00_Day1_Block1.txt). Clear the workspace in the console before proceeding. 

9. If the stream works, run the code "alphaRangeBaseline.py" to individualize the alpha range before starting the NF-training block. Once the code finishes running, check the individual's alpha range in the console. 

10. In the code "baseline.py" remember to update the alpha range ("lowcut" and "highcut" freq. range). Do this for each new range, and before starting a new NF-training block.

11. Now you are ready to start the NF-training block. Run the code "parallelBlock_Alpha.py". This code will call the task "Block_NF_Alpha.py"

12. At each run, fill the automatic info box with alpha range information, participant information, NF-training session information, participant ID (that should match with the ID you wrote in the receiveLslData_Alpha.py code.

13. Once the parallelBlock_Alpha.py finishes the task, let the stream run until it stops. 

14. Check your data output in your folder. You should have the raw_data.txt and data_info.xls (name of files as you named them)

15. You can use the raw_data.txt in EEGlab or any other software to start pre-processing your EEG data.

16. The data_info.xls can be used to extract the event information (use the "startingRT" parameter to set your msec for each event) or for any other use. 

17. When you finish your experiment, you can close the "stream" in your terminal by clicking control+C (in MacBook).


* I also suggested to open the OpenBCI GUI to look at the signal quality before running the experiment. Remember to switch off lab streaming layer in your terminal when the GUI is open. Otherwisw it would not work. 
             
 -----------------------------------------------------------------------------------------------------------------------------------------------------------
 ----------------------------------------------------- Pre-processing in EEGLAB ------------------------------------------------------------------------------------
 
 In the case of pre-processing in EEGLAB, the code to define events and channel locations are provided.
 
 1. to define events, run in Matlab the code "RewardEvents_Alpha_RewardSeparation.m" to define all the events and separated them by the reward type. Or run the code "RewardEvents_NF_Alpha.m" to define events without considering the distinction between the reward types. Rename and save the .txt file.
 2. Open EEGLAB. 
 3. Import the raw data file: file --> import data --> with EEGLAB functions and plugins --> from ASCII/Matlab files --> browse your raw data .txt file, rename "S01_Day1_Block1", and insert the sampling rate of 250. Save dataset.
 4. Import channel locations: Edit --> channel locations --> pop up window "look up channel locations?" click ok --> "read location" button --> browse your file "Chanloc_NF-protocol.ced" --> click ok to all the pop up windows.
 5. Import event file information: file --> import event info --> from Matlab array or ASCII file --> browse your file created in Matlab e.g., "S00_Day1_Block1_Reward.txt" --> in "input field" write "number latency type duration" --> in "number of header lines" write 1 --> elsewehere is fine --> click ok.
 6. Now you have a pre-processed dataset
 7. You can scroll your data for a first check. You should filter your data first. 
 8. If your data look good, you can save your dataset: file --> save your current datasets as --> rename and locate your dataset in your folder "S00_Day1_Block1.set" the extension .set is automatically generated.
 9. You can proceed with other analyses (e.g., in Python, Matlab). 

 
 
