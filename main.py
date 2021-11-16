import numpy as np
import random
import matplotlib.pyplot as plt

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

T = 10000
a = 5
r=0.0

def snr(b,a1,a2,len):

    for R in range(1,7):
        r=(a2-a1)/(2**R+1)
        quant = np.zeros(2**R)
        for i in range(2**R):
            quant[i] = a2-r*(i+1)
        c=b.copy()
        for j in range(len):
            c[j] = find_nearest(quant,c[j])
        SNR = 10*np.log10(sum(b**2)/sum((b-c)**2))
        print(SNR)

b = np.zeros(T)
for i in range(T):
    b[i] = random.uniform(-a, a)
snr(b,-a,a,T)
b = np.random.normal(0, a/3, 10000)
snr(b,-a,a,T)

bright = plt.imread("bright1.bmp")
dark = plt.imread("dark1.bmp")
normal = plt.imread("normal1.bmp")
Yb = bright[:,:,0] * 0.299 + bright[:,:,1] * 0.587 + bright[:,:,2] * 0.114
Yd = dark[:,:,0] * 0.299 + dark[:,:,1] * 0.587 + dark[:,:,2] * 0.114
Yn = normal[:,:,0] * 0.299 + normal[:,:,1] * 0.587 + normal[:,:,2] * 0.114
#plt.hist(Yb)
#plt.hist(Yd)
#plt.hist(Yn)
#plt.show()

print("\n")

snr(Yb.flatten(),0,255,Yb.flatten().size)
snr(Yd.flatten(),0,255,Yb.flatten().size)
snr(Yn.flatten(),0,255,Yb.flatten().size)
