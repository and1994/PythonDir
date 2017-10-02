# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:34:05 2017

@author: zx825273
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

nh_temperature=np.genfromtxt('nh_temperature.txt')
plt.figure(1)
plt.plot(nh_temperature[:,0],nh_temperature[:,1],label="January")
plt.plot(nh_temperature[:,0],nh_temperature[:,7],label="July")
plt.xlabel("Year")
plt.ylabel("Temperature anomaly (K)")
plt.legend()
plt.title("January and July temperature anomaly time series")
plt.show()

plt.figure(2)
recent_anom=np.mean(nh_temperature[160:166,1:13],axis=0)
remote_anom=np.mean(nh_temperature[0:6,1:13],axis=0)
months=np.linspace(1,12,12)
plt.plot(months,recent_anom,label="2010-2015")
plt.plot(months,remote_anom,label="1850-1855")
plt.xlabel("Months")
plt.ylabel("Mean temperature anomaly (K)")
plt.legend()
plt.title("Mean temperature anomaly time series ove two periods")
plt.show()

plt.figure(3)
plt.hist(np.hstack(nh_temperature[160:166,1:13]),bins=20,label="2010-2015")
plt.hist(np.hstack(nh_temperature[0:6,1:13]),bins=20,label="1850-1855")
plt.xlabel("Anomalies")
plt.ylabel("Anomaly's occurrence")
plt.legend()
plt.title("Anomalies occurrence over two periods of time")
plt.show()

plt.figure(4)
data=np.zeros([33,np.size(nh_temperature[160:166,1:13].reshape((1,72)))])
for i in range(33):
    data[i,:]=nh_temperature[i*5:i*5+6,1:13].reshape((1,72))
plt.boxplot(data.transpose())
#when plotting check if python is reading properly the data (i.e. it might be necessary to transpose it)