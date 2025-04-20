#https://github.com/curiositry/EEGrunt/blob/master/data/eegrunt-obci-ovibe-test-data.csv

import pandas as pd 
import mne
import matplotlib as plt

link = "https://raw.githubusercontent.com/curiositry/EEGrunt/refs/heads/master/data/eegrunt-obci-ovibe-test-data.csv"

data_file = pd.read_csv(link)
print(data_file.head())

#time not important for this analysis

#data_file.drop("Time (s)" , axis=1, inplace=True) 

#print(data_file.head())

sfreq = 250
#lista * cantidad de columnas que hay
ch_types = ["eeg"]*data_file.shape[1]
ch_names = ["Fp1","Fp2","F3","F4","Cz","C3","C4","T5","T6","P3","P4","O1","O2","Fz","Cz","Pz"]
#create standard montage of 11 electrodes 
montage = mne.channels.make_standard_montage("standard_1020")
info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)
samples = data_file.T*1e-6
loadedRaw = mne.io.RawArray(samples, info)
loadedRaw.set_montage(montage = montage)

print(loadedRaw.info)

loadedRaw.plot() 

#show sensors positions
loadedRaw.plot_sensors(show_names=True)

loadedRaw.plot_psd()

input("press enter to exit")
