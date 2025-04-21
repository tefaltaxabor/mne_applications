import mne
import numpy as np
import matplotlib.pyplot as plt 

raw = mne.io.read_raw_edf(r"C:\\Users\\gabri\\Desktop\\project\\data\\S001R03.edf",preload=True)

print(raw.info)

raw.plot(n_channels=10, title="EEG Raw", block=True)

#unreadable data 
#events = mne.read_events("C:\\Users\\gabri\\Desktop\\project\\data\\S001R01.edf.event")
#mne.viz.plot_events(events, sfreq=raw.info['sfreq'])

# Extraer eventos desde anotaciones embebidas
events, event_id = mne.events_from_annotations(raw)

print("\nEventos extraídos:")
print(events[:5])
print("\nDiccionario de etiquetas:")
print(event_id)

# Visualizar eventos
mne.viz.plot_events(events, sfreq=raw.info['sfreq'])

#etiquetas con puntos extras (eliminar)
def clean_name(name):
    return name.replace('.', '').upper()

raw.rename_channels(clean_name)

# Mostrar posiciones de electrodos
raw.set_montage("standard_1020", on_missing='ignore')
raw.plot_sensors(show_names=True)


print(raw.info['ch_names'])
#comprobar el montaje
#template_s1020_montage = mne.channels.make_standard_montage("standard_1020")
#print(template_s1020_montage.ch_names)

input("Press enter to exit")