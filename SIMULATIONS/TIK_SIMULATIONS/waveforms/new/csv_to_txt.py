import numpy as np

path_to_file = "./20220223-0001_03.csv"
delimiter = ";"

diezmado = 40


units = np.loadtxt(path_to_file,  
				   delimiter=delimiter, 
				   dtype=str,
				   skiprows=1,
				   max_rows=1)

# lectura de los datos como números en coma flotante
t, ch_a, ch_b = np.loadtxt(path_to_file, 
						   delimiter=delimiter, 
						   unpack=True, 
						   skiprows=3, 
						   dtype=str)
                           
t = np.array([float(item.replace(",", ".")) for item in t])
ch_a = np.array([float(item.replace(",", ".")) for item in ch_a])
ch_b = np.array([float(item.replace(",", ".")) for item in ch_b])


# ----------------------- ADECUACIÓN DE LOS DATOS ------------------------ #

t = t - t[0] # start at t0 = 0

if units[0] == "(ms)":
	t *= 1e-3;  # ms to s
elif units[0] == "(us)":
	t *= 1e-6;  # us to s
	
if units[1] == "(mV)":
	ch_a *= 1e-3;  # mV to V
if units[2] == "(mV)":
	ch_b *= 1e-3;  # mV to V
	
L = len(t)      # longitud del vector de muestras
Ts = t[-1] / L  # periodo de muestreo
Fs = int(1/Ts)  # frecuencia de muestreo

print(f"Frecuencia de muestreo: {Fs/1e3:.3f} kHz")
print(f"Frecuencia de muestreo diezmada: {Fs/(diezmado * 1e3):.3f} kHz")

t2 = np.arange(0, L, 1) * Ts  # nuevo vector temporal
tmax = t2[-1]  # tiempo máximo, final del vector
freq_rep = int(1/tmax)  # frecuencia de repetición de la señal completa


with open(f"emitter.txt", "w") as f:  # Emisor
    for i in range(0, L, diezmado):
        f.write(f"{t2[i]} ")
        f.write(f"{ch_a[i]} ")
    
with open(f"receiver.txt", "w") as f:  # Emisor
    for i in range(0, L, diezmado):
        f.write(f"{t2[i]} ")
        f.write(f"{ch_b[i]} ")