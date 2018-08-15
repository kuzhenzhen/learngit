import numpy as np
import matplotlib.pyplot as plt  


filename = '2017-12-15T11-56-31.awd'
fileName = open(filename, 'r')
lines = fileName.read().splitlines()


newLines = []
for  linesLetter in lines:
    b = int(linesLetter)
    newLines.append(b)


l1=plt.plot(newLines,'r',label='Pentachlorobenzene')
plt.title('267 nm 100 fs laser ionization for Pentachlorobenzene using TOFMS')
plt.xlabel('channel')
plt.ylabel('intensity')
plt.legend()
plt.show()