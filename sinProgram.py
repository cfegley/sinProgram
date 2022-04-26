import numpy as np
import matplotlib.pyplot as plt

def main():


	sinx = np.linspace(0, 2*np.pi, 1000)

	x = np.array(sinx)

	for i, val in enumerate(x, start=1):
		print(f"x = {i}, sin(x) = {val}")




main()



