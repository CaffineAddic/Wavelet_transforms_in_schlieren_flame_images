import pywt
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 200)

# Finding signal by adding three different signals
signal = np.cos(2 * np.pi * 7 * t) + np.real(np.exp(-7 * (t-0.4)**2)*np.exp(1j*2*np.pi*2*(t-0.4)))
scales = np.arange(1, 31)  # No. of scales

coef, freqs = pywt.cwt(signal, scales, 'gaus1')  # Finding CWT using gaussian wavelet

# Plotting scalogram
plt.figure(figsize=(15, 10))
plt.imshow(abs(coef), extent=[0, 200, 30, 1], interpolation='bilinear', cmap='bone',
           aspect='auto', vmax=abs(coef).max(), vmin=abs(coef).max())
plt.gca().invert_yaxis()
plt.yticks(np.arange(1, 31, 1))
plt.xticks(np.arange(0, 201, 10))
plt.show()