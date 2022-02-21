clear str rt EEG x numbers text everything start;

x = xlsread("/Users/barbazze/Documents/Psychopy/Patient Study I/S00_Day1_Block1_Alpha.xlsx");
x1 = x(1,2);

%[numbers, text, everything]=xlsread("/Users/barbazze/Documents/Psychopy/Patient Study/S01_Day1_Block1.xlsx");%\S24\S24_Day5\S24_Day5_Block2.xlsx");
%x=numbers(:,2);
%text(1,:)=[];
%start=numbers(1,12); %%%for NF (1,12) for CO (1,11)
%str=text(:,8);
% rt=x;%input('Please insert Response Time as an array: ');
% reward=str;%input('Please insert Reward/No Reward as an array: ');
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
    
    EEG =eeg_addnewevents(EEG,{[lat_ency]},{'Reward'});
    
    
    %%%%%% End & Save %%%%%%%%%%%%
    
    
    events = eeg_eventtable(EEG, 'exportFile', 'S00_Day1_Block1_Alpha.txt');

end



%EEG = eeg_addnewevents(EEG, {[0 200] [200 800] [800 1400] [1400 2000] [2000 4000]}, {'type1' 'type2' 'type3' 'type4' 'type5'}, {'Text1' 'Text2' 'Baseline' 'Text3' 'Neurofeedback'})

