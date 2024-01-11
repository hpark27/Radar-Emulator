import time
import numpy as np
from tkinter import*
import tkinter as tk
import matplotlib
import functions as funcs
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
from matplotlib import animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    
### FUNCTION ###
# Function to animate line rotation
def animate(i):
    global lineangle, numAxes 
    global distance, angle

    if round(lineangle,12)==round(2*np.pi,12): # when angle is 360 deg
        lineangle = 0                          # reset deg into 0 deg
        time.sleep(0.5)                        # time delay

    lineangle = lineangle + np.deg2rad(1)      # increase angle by 1 deg

    # delete previous line
    if i==0:
        ax.lines.pop(numAxes-1)
    else:
        ax.lines.pop()
    
    # plot line
    line = ax.plot([0,lineangle],[0,100], color='#02fe14', linewidth='2', linestyle='solid')

    return line

## Function for button click event
# start animation
def start():
    anim = animation.FuncAnimation(fig, animate, init_func=lambda:line, interval=10)
    canvas.draw()
    return anim

## close window
def stop():
    global window
    window.quit()
    window.destroy()

### system
lineangle = 0      # line angle at default condition

# create target positions - random positions
distance, angle = funcs.randposition()

# sort target position
distance.sort()
angle.sort()

### TKInter GUI Window
window = tk.Tk()                                   # initialize window
window.title('Radar Emulator')                     # window title
window.geometry('800x652')                         # window size
window.configure(background='black')               # window color
window.resizable(False,False)                      # set window size unresizable

fig = plt.figure(facecolor='k', figsize=[8,6])     # add figure on window
ax = fig.add_subplot(111,polar=True,facecolor='k') # add plot on figure

range = 110                                        # radar distance range
rad = 2*np.pi                                      # radar angle range (rad)
ax.set_xlim(0,rad)                                 # set x axis limit - angle
ax.set_ylim(0,range)                               # set y axis limit - distance
ax.grid('both',color='#02fe14',linewidth=1.25)     # add grid for x and y axis

# add scale lines
for i  in np.deg2rad(np.arange(0,360,5)):
    ax.plot([i,i], [range,range*0.98], linewidth=1.25, color="#02fe14")

# add sub-grid for y axis
ax.yaxis.set_major_locator(tic.MultipleLocator(25)) # scale/distance to plot grid
ax.grid('y',alpha=0.5)                              # adjust transparency
line, = ax.plot([0,0], [0,100], color='#02fe14', linewidth='2', linestyle='solid')
numAxes = len(ax.lines)                             # get number of axes drawn on the plot

# Tkinter canvas configuration    
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

# button labels
start_label = 'Start' # start button
close_label = 'Close' # close button

# button configurations
startBtn = Button(window,text=start_label, command=lambda: start())
closeBtn = Button(window,text=close_label, command=lambda: stop())

startBtn.config(foreground='#02fe14', activeforeground='#03ffbf', background='black', 
                activebackground='black', font='14', width='7')

startBtn.place(x=300,y=600) # location

closeBtn.config(foreground='#02fe14', activeforeground='#03ffbf', background='black', 
                activebackground='black', font='14', width='7')

closeBtn.place(x=450,y=600) # location

window.mainloop()
