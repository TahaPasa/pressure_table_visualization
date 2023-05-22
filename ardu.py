import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import serial

# create an initial heatmap with zeros pressure data
pressure_data = np.zeros((15, 15))

# create a color map that goes from blue (low pressure) to red (high pressure) to green (medium pressure)
cmap = matplotlib.colors.LinearSegmentedColormap.from_list('', ['white', 'blue', 'green', 'yellow', 'red'])

# create a figure and axis object
fig, ax = plt.subplots()

# create the heatmap object and set its properties
im = ax.imshow(pressure_data, cmap=cmap, interpolation='gaussian', vmin=pressure_data.min(), vmax=pressure_data.max())
ax.set_xticks(np.arange(-0.5, 15, 1))
ax.set_yticks(np.arange(-0.5, 15, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(color='black', linestyle='-', linewidth=0.5)
ax.set_title('Pressure Heatmap')
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Pressure', rotation=-90, va="bottom")

# create a list to store the text annotations
annotations = []

# show the plot and keep it open
plt.show(block=False)

# initialize serial communication with the ARDUINO
ser = serial.Serial('COM3', 115200)

# update the heatmap in a loop
while True:

    # # generate random pressure data
    # pressure_data = np.random.rand(15, 15)


    # read the pressure data from the Arduino
    data = ser.readline().decode('utf-8').rstrip()

    

    if data:
    # convert the pressure data to a numpy array
        pressure_data = np.fromstring(data, sep=',')
    
    print(pressure_data)

    # reshape the pressure data into a 15x15 matrix
    pressure_data = pressure_data.reshape((15, 15))


    # update the data displayed in the heatmap
    im.set_data(pressure_data)

    # adjust the color scale based on the new pressure data
    im.set_clim(vmin=pressure_data.min(), vmax=pressure_data.max())

    # remove the previous annotations
    for ann in annotations:
        ann.remove()
    annotations = []

    # add the new annotations
    for i in range(len(pressure_data)):
        for j in range(len(pressure_data[i])):
            text = ax.text(j, i, f'{pressure_data[i][j]:.2f}', ha='center', va='center', color='black', fontsize=8)
            annotations.append(text)

    # redraw the plot with the updated data, color scale, and annotations
    fig.canvas.draw_idle()

    # add a delay of 0.1 seconds between iterations
    plt.pause(0.1)
