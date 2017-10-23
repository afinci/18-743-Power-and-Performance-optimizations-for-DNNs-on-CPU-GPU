import matplotlib.pyplot as plt
import numpy as np
import sys

def main():
    filename = sys.argv[1]

    cpu_power = []
    gpu_power = []
    cpu_temp = []
    gpu_temp = []

    with open(filename) as f:
        for l in f:
            toks = l.split(',')
            cpu_power.append(float(toks[2].split()[-1]))
            gpu_power.append(float(toks[3].split()[-1]))
            cpu_temp.append(float(toks[10].split()[-1]))
            gpu_temp.append(float(toks[11].split()[-1]))
    
    cpu_power = np.array(cpu_power) / 1000
    gpu_power = np.array(gpu_power) / 1000
    cpu_temp = np.array(cpu_temp) / 1000
    gpu_temp = np.array(gpu_temp) / 1000

    print np.mean(cpu_power), np.mean(gpu_power), np.mean(cpu_temp), np.mean(gpu_temp)

    # fig, ax1 = plt.subplots()
    # ax1.plot(cpu_power, 'r-')
    # ax1.plot(gpu_power, 'r--')
    # ax1.set_xlabel('time (s)')
    # Make the y-axis label, ticks and tick labels match the line color.
    # ax1.set_ylabel('Power (W)', color='r')
    # ax1.tick_params('y', colors='r')

    # ax2 = ax1.twinx()
    # ax2.plot(cpu_temp, 'b-')
    # ax2.plot(gpu_temp, 'b--')
    # ax2.set_ylabel('Temperature (C)', color='b')
    # ax2.tick_params('y', colors='b')

    # fig.tight_layout()
    # plt.show()
    
if __name__ == '__main__':
    main()