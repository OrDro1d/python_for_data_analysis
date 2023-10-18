import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

index = np.arange(7)
values1 = [320, 270, 190, 150, 145, 120, 280]
values2 = [302, 250, 205, 200, 150, 280, 150]
values3 = [298, 210, 189, 170, 155, 225, 140]
bw = 0.3

fig, ax = plt.subplots(figsize=(6, 3), frameon='False')
ax.bar(index, values1, bw, color='#F56', label="Hornberg")
ax.bar(index+bw, values2, bw, color='#5B5', label="Strick")
ax.bar(index+2*bw, values3, bw, color='#39E', label="Huetten")
plt.xticks(index+0.85*bw, ['January', 'February', 'March', 'April', 'May', 'November', 'December'])
plt.xlabel('Month')
plt.ylabel('Monthly Prescription [mm]')
formatter1 = ticker.FormatStrFormatter("%d")
formatter2 = ticker.MultipleLocator(100, 0)
ax.yaxis.set_major_formatter(formatter1)
ax.yaxis.set_major_locator(formatter2)
ax.legend(loc='center left', title='variable', alignment='left', bbox_to_anchor=(1, 0, 0.5, 1), frameon=False)
ax.set_ylim(-15, 340)
ax.grid(True)
ax.set_axisbelow(True)
plt.show()
