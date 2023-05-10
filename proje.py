import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# create an initial heatmap with zeros pressure data
pressure_data = np.zeros((15, 15))

# create a color map that goes from blue (low pressure) to red (high pressure) to green (medium pressure)
# cmap = plt.cm.get_cmap('RdBu_r').copy()
cmap = matplotlib.colors.LinearSegmentedColormap.from_list('', ['white','blue', 'green','yellow', 'red'])

# create a figure and axis object
fig, ax = plt.subplots()

# create the heatmap object and set its properties
im = ax.imshow(pressure_data, cmap=cmap, interpolation='gaussian', vmin=pressure_data.min(), vmax=pressure_data.max())
ax.set_xticks(np.arange(len(pressure_data)))
ax.set_yticks(np.arange(len(pressure_data)))
ax.set_xticklabels(np.arange(1, len(pressure_data)+1))
ax.set_yticklabels(np.arange(1, len(pressure_data)+1))
plt.setp(ax.get_xticklabels(), fontsize=8)
plt.setp(ax.get_yticklabels(), fontsize=8)
ax.grid(color='black', linestyle='-', linewidth=0.5)
ax.set_title('Pressure Heatmap')
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Pressure', rotation=-90, va="bottom")



# show the plot and keep it open
plt.show(block=False)

# update the heatmap in a loop
while True:
    # generate random pressure data
    pressure_data = np.random.rand(15, 15)

    # update the data displayed in the heatmap
    im.set_data(pressure_data)

    # adjust the color scale based on the new pressure data
    im.set_clim(vmin=pressure_data.min(), vmax=pressure_data.max())

    # redraw the plot with the updated data and color scale
    fig.canvas.draw_idle()

    # add a delay of 0.1 seconds between iterations
    plt.pause(0.5)