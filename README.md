# NF-protocol-method
Python codes of the NF-training method proposed for the NF-training protocol in preclinical Alzheimer's disease.

The proposed NF-training method is part of the research conducted in my doctoral thesis work: "Cognitive Training Based on EEG Neurofeedback to Improve Working Memory: A Research Study on Healthy Volunteers with an Outlook on Preclinical Alzheimer’s Disease", Faculty of Natural Science at the Otto-von-Guericke University of Magdeburg. 

Supervisors: Prof. Dr. med. Emrah Duezel
             Prof. Dr. Oliver Speck


-------------------------------------------------------------------------------------------------------------------------------------------------------------------
             
* NB: OpenBCI has been used with a Macbook Pro (13-inch, 2018), processor 2.3 GHz Intel   Core i5, 8 GB memory

* I suggest to use OpenBCI with iOS and the instructions below are for iOS users


Task code instructions:

1. Download Python (with Anaconda) and choose your Python IDE. I suggest Spider. The version of Python that I used for coding is 3.7.3

2. Download Psychopy

3. Download Lab Streaming Layer (LSL) https://github.com/sccn/labstreaminglayer and save it in your "Documents/Psychopy" folder make a new folder in "OPENBCI_LSL". 

4. You find a file named "openbci_lsl.py".

5. Open your terminal and set your path to "Documents/Psychopy/OpenBCI_LSL/".

6. In "Documents/Psychopy/OpenBCI_LSL/" path, open the file "openbci_lsl.py /dev/tty.usbserial-DM00QAZP --stream" to start the neurofeedback stream .

7. Type "/start" to start the stream.

8. In your Python interface, run the code "receiveLslData_Alpha.py" to check if the stream works. If yes, click control + C in the Console to stop the stream. Remember to rename the output file that you want to save e.g., S01_Day1_Block1.txt . Clear the work space in the console before to proceed. 

9. If the stream works, run the code "alphaRangeBaseline.py" to individualize alpha range before the NF training block. Once the code finishes to run, check the individual's alpha range in the console. 

10. In the code "baseline.py" remember to update the alpha range ("lowcut" and "highcut" freq. range). Do this for each new range.

11. Now you are ready to start the NF block. Run the code "parallelBlock_Alpha.py".

12. At each run, fill the automatic info box with alpha range informations, participant informations, NF training session informations, participant ID (that should match with the ID you wrote in the receiveLslData_Alpha.py code .

13. Once the parallelBlock_Alpha.py finishes the task, let the stream run until it stops. 

14. Check your data output in your folder. You should have the raw_data.txt and data_info.xls (name of files as you named them)

15. You can use the raw_data.txt in EEGlab or any other software to analyze your EEG data.

16. The data_info.xls can be used to extract the event information (use the "startingRT" parameter to set your msec for each event) or for any other use. 
             
             
 
