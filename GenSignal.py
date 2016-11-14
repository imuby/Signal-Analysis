import numpy as np

def genSine(f0, fs, dur):
    t = np.arange(dur)
    sinusoid = np.sin(2*np.pi*t*(f0/fs))
    return sinusoid
    
def genNoise(dur):
    noise = np.random.normal(0,1,dur)
    return noise

def genSignal(sinusoid, noise):
    signal = sinusoid + noise
    return signal