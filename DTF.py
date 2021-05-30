#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from math import sin, cos, pi, atan

def DTF(x):
	X = []
	j = complex(0, 1)
	N = len(x)
	def rotate(n, k, N):
		return cos(2*pi*n*k/N)+j*sin(2*pi*n*k/N)
	for k in range(N):
		temp = 0
		for n in range(N):
			temp += x[n]*rotate(n, k, N)
		if abs(temp.real) < 0.001:
			temp = complex(0, temp.imag)
		if abs(temp.imag) < 0.001:
			temp = complex(temp.real, 0)
		X.append(temp)
	return X

def Amplitude(X):
	Ampl = []
	for i in range(len(X)):
		Ampl.append(((X[i].real**2+X[i].imag**2)**0.5)/2)
	return Ampl
	
def Faza(X):
	F = []
	for i in range(len(X)):
		try:
			F.append(atan(X[i].imag/X[i].real))
		except:
			F.append(0)
	return F

# Step discreting
step = 8

time = [sin(i*pi/step)+ sin(i*2*pi/step + pi/4)for i in range(step*2)]
freq = DTF(time)
AF = Amplitude(freq)
F = Faza(freq)

fig = plt.figure()

ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

ax1.stem(time)
ax2.stem(AF)
ax3.stem(F)

plt.show()