import matplotlib.pyplot as plt
import numpy as np

lp_2_3 = np.loadtxt('lp_2_3.txt')
lpcc_2_3 = np.loadtxt('lpcc_2_3.txt')
mfcc_2_3 = np.loadtxt('mfcc_2_3.txt')

plt.figure()

plt.subplot(311)
plt.plot(lp_2_3[:,0], lp_2_3[:,1])
plt.grid()
plt.title('LP')


plt.subplot(312)
plt.plot(lpcc_2_3[:,0], lpcc_2_3[:,1])
plt.grid()
plt.title('LPCC')


plt.subplot(313)
plt.plot(mfcc_2_3[:,0], mfcc_2_3[:,1])
plt.grid()
plt.title('MFCC')


plt.show()