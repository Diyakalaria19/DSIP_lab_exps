import numpy as np
import matplotlib.pyplot as plt

def simulate_discrete_exponential(num_samples, amplitude, coefficient):
    exponential_signal = amplitude * np.exp(coefficient * np.arange(num_samples))
    return exponential_signal

num_samples = 17
amplitude = 5
coefficient = -0.5 

discrete_exponential = simulate_discrete_exponential(num_samples, amplitude, coefficient)

plt.stem(discrete_exponential)
plt.title('Discrete Exponential Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()