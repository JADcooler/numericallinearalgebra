import matplotlib.pyplot as plt
import numpy as np

t=[3,4,2,1,5]
s=[10,8,6,4,2]
plt.figure()
plt.plot(t, s)
plt.scatter(t,s)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)


plt.figure()
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.show()
