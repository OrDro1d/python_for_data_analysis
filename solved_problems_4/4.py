# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# import numpy as np
#
# fig, ax = plt.subplots(1, 3)
# plt.subplots_adjust(wspace=0.3)
#
# x, y = np.array([0, 80, 240, 355], dtype=float), np.array([0, 5.1, -2.5, 0], dtype=float)
# ax[0].plot(x, y, color='#49F')
# ax[0].set_xlabel("Angle (degrees)")
# ax[0].set_ylabel("Position (in)")
# ax[0].set_title('Position vs Angle')
#
# x, y = (np.array([0, 25, 152, 225, 300, 355], dtype=int),
#         np.array([150, 185, -170, -50, 40, 155], dtype=int))
# ax[1].plot(x, y, color='#49F', label='True Speed')
# ax[1].plot([0, 355], [50, 50], color='orange', label='Mean Piston Speed')
# ax[1].scatter(90, 0, marker='.', label='Top Dead Center', color='black', zorder=2)
# ax[1].scatter(266, 0, marker='*', label='Bottom Dead Center', color='black', zorder=2)
# ax[1].set_xlabel("Angle (degrees)")
# ax[1].set_ylabel("Piston Velocity (mph)")
# ax[1].set_title('Piston Speed vs Angle')
# ax[1].legend(loc='lower right', fontsize=8)
#
# x, y = (np.array([0, 0, 90, 195, 280, 340, 355], dtype=int),
#         np.array([0, 4050, -8100, 4500, 2050, 4500, 4050], dtype=int))
# ax[2].plot(x, y, color='#49F')
# ax[2].set_xlabel("Angle (degrees)")
# ax[2].set_ylabel("Piston Acceleration (g)")
# ax[2].set_title('Piston Net Force vs Angle')
#
# [axes.set_xlim(-20, 390) for axes in ax]
# formatter = ticker.MultipleLocator(50, 0)
#
# ax[0].set_ylim(-2.8, 5.5)
# ax[1].set_ylim(-210, 210)
# ax[2].set_ylim(-9000, 5000)
#
# for axes in ax:
#     axes.xaxis.set_major_locator(formatter)
#     axes.grid(True)
#     axes.set_axisbelow(True)
#
# plt.show()
