from scipy.io.wavfile import read as wread
import os

wbb = os.listdir('.')[-2]

r, d = wread(wbb)
