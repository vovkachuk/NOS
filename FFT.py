import matplotlib.pyplot as plt
from math import log2, sin, cos, pi, atan

def FFT_time(x):
	x_by_time = []
	print("x(n): ",x)

	N = len(x)

	for j in range(N):
		y = 0
		for i in range(int(log2(N))):
			y = (y << 1) | (j & 1)
			j >>= 1
		x_by_time.append(y)
	print("t(n): ",x_by_time)

	def rotate(k, N):
		j = complex(0,1)
		return cos(2*pi*k/N)+j*sin(2*pi*k/N)
	X = [x[i] for i in x_by_time]

	print("Bit-reversed permutation X(n): ",X)
	size = 2
	print("[!] Start bytterfly....")
	while size <= N:
		halfsize = size // 2
		tablestep = N // size
		print("[#] Step:", int(size**1/2))
		for i in range(0, N, size):
			k = 0
			for j in range(i, i + halfsize):
				temp = X[j+halfsize] * rotate(k, N)
				X[j + halfsize] = X[j] - temp
				X[j] = X[j] + temp
				for i in range(len(X)):
					if abs(X[i].real) < 0.001:
						X[i] = complex(0, X[i].imag)
					if abs(X[i].imag) < 0.001:
						X[i] = complex(X[i].real, 0)
                
				print(f"\tX({j}): ",X[j], f"\tX({j+halfsize}): ",X[j+halfsize])
				k+=tablestep
		size *= 2

	for i in range(len(X)):
		if abs(X[i].real) < 0.001:
			X[i] = complex(0, X[i].imag)
		if abs(X[i].imag) < 0.001:
			X[i] = complex(X[i].real, 0)
	print("[+] Done!")
	print(X)
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


step = 4
time = [sin(i*pi/step)+ sin(i*2*pi/step + pi/4)for i in range(step*2)]
freq = FFT_time(time)
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