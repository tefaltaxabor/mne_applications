import mne
import numpy as np
import matplotlib.pyplot as plt 

sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = (
    sample_data_folder / "MEG" / "sample" / "sample_audvis_filt-0-40_raw.fif"
)
raw = mne.io.read_raw_fif(sample_data_raw_file)

print("\n")
print("el largo es", raw.__len__())
print("\n")

print(raw)
print(raw.info)

#since the data is alredy filtered by a low pass filter f_g = 50 Hz 
#dice 40 como low pass wtf
raw.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False) 
raw.plot(duration=5, n_channels=30) #mne method plot EEG data

plt.show() #para mantener los graficos abiertos
