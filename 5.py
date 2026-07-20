import numpy as np
import matplotlib.pyplot as plt

def simulate_discrete_sine_wave(num_samples, sampling_frequency, amplitude, frequency,
phase):
    time = np.arange(num_samples) / sampling_frequency
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * time + phase)
    return sine_wave

num_samples = 100 
sampling_frequency = 10 
amplitude = 1 
frequency = 2 
phase = 0 

discrete_sine_wave = simulate_discrete_sine_wave(num_samples, sampling_frequency,
amplitude, frequency, phase)
plt.stem(discrete_sine_wave)
plt.title('Discrete Sine Wave Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()