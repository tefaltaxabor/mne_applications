#https://github.com/tefaltaxabor/mne_applications/blob/main/data/s05.csv

import pandas as pd 
import mne
import scipy.io
import numpy as np

link = "https://raw.githubusercontent.com/curiositry/EEGrunt/refs/heads/master/data/eegrunt-obci-ovibe-test-data.csv"

data_file = pd.read_csv(link)
print(data_file.head())

#time not important for this analysis

data_file.drop("Time (s)" , axis=1, inplace=True) 

#print(data_file.head())

'''
mat = scipy.io.loadmat("C:\\Users\\gabri\\Desktop\\project\\data\\EEG_DATA_S1.mat")

#print(mat.keys()) 

data = mat['data']
#print(data.shape)
#print(type(data[0, 0]))

trial_index = 0
trial_data = data[trial_index, :8] 
label = data[trial_index, 8]

channel_data = [trial_data[ch].flatten() for ch in range(8)]

channel_names = ["Fp1", "Fp2", "F3", "F4", "C3", "C4", "P3", "P4"]

df = pd.DataFrame(np.array(channel_data).T, columns=channel_names)

df["label"] = label[0] if isinstance(label, np.ndarray) else label

df.to_csv("EEG_trial0.csv", index=False)
'''


sfreq = 250
#lista * cantidad de columnas que hay
ch_types = ["eeg"]*data_file.shape[1]
ch_names = ["Fp1", "Fp2", "F3", "F4", "Cz","C3", "C4", "P3", "P4", "O1", "O2"]
#create standard montage of 19 electrodes 
montage = mne.channels.make_standard_montage("standard_1020")
info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)
samples = data_file.T*1e-6
loadedRaw = mne.io.RawArray(samples, info)
loadedRaw.set_montage(montage = montage)

print(loadedRaw.info)

loadedRaw.plot() 

#show sensors positions
loadedRaw.plot_sensors(show_names=True)

loadedRaw.plot_psd(tmin = 0 , tmax = 50 , fmin = 2 , fmax = 120 , average = True)

input("press enter to exit")
