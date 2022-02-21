clear str rt EEG x numbers text everything start;

[numbers, text, everything] = xlsread("/Users/barbazze/Documents/Psychopy/Patient Study I/S00_Day1_Block1_Alpha.xlsx");
%x = xlsread("/Users/barbazze/Documents/Psychopy/Patient Study I/S01_Day1_Block1_Alpha.xlsx");
x = numbers()
%x1 = x(1,2);
x1 = numbers(1,2);

%text(1,:)=[];
%start=numbers(1,12); %%%for NF (1,12) for CO (1,11)
str=numbers(:,3:4);
% rt=x;%input('Please insert Response Time as an array: ');
reward=str;%input('Please insert Reward/No Reward as an array: ');
Reward=reward(:,1)
%startResponseTime=start;%input('Please insert satarting resonse time as a value: ');
startResponseTime=x1

eeglab;
lat_ency=startResponseTime;
%lat_ency=0

%for b=1:24
    
    %EEG= eeg_addnewevents(EEG, {[0 200] [300 900] [1000 1600] [1700 2300] [2400 4400]}, {'Text1' 'Text2' 'Baseline' 'Text3' 'Neurofeedback'})
    
    %%%%%%%%%% Text 1%%%%%%%%%%%%%%%%
    lat_ency=lat_ency;
    
    EEG =eeg_addnewevents(EEG,{[lat_ency]},{'Text_1'});
    
    %%%%%%%%%% Text 2 %%%%%%%%%%%%%%%%%%%%%%
    lat_ency=lat_ency+6;
    
    EEG =eeg_addnewevents(EEG,{[lat_ency]},{'text_2'});
    
    %%%%%%%%%% text 3 %%%%%%%%%%%%%
    lat_ency=lat_ency+6;
    
    EEG =eeg_addnewevents(EEG,{[lat_ency]},{'Text_3'});
    
    
for b = 1:12    
    %%%%%%%%%% Baseline %%%%%%%%%%%%%
    lat_ency=lat_ency+6;
    EEG =eeg_addnewevents(EEG,{[lat_ency]},{'Alpha_Baseline'});
    
    
    %%%%%%%%%%Neurofeedback%%%%%%%%%%%%
    lat_ency=lat_ency+20;
    
    EEG =eeg_addnewevents(EEG,{[lat_ency]},{'Alpha_NF'});
    
    %%%%%%%%%%Reward%%%%%%%%%%%%
    lat_ency=lat_ency+2;
    
    if Reward(b) == 1 ~Reward(b) == 0
    
       EEG =eeg_addnewevents(EEG,{[lat_ency]},{'Reward'});
       
    else
        EEG =eeg_addnewevents(EEG,{[lat_ency]},{'NoReward'});
        
    end
    
    
    %%%%%% End & Save %%%%%%%%%%%%
    
    
    events = eeg_eventtable(EEG, 'exportFile', 'S00_Day1_Block1_Reward.txt');

end