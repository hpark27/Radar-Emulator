import time
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.ticker as tic
from matplotlib import animation
from matplotlib.widgets import Button

### Function
# Function to animate line rotation
def animate(i):
    global lineangle

    if round(lineangle,12)==round(2*np.pi,12): # when angle is 360 deg
        lineangle = 0                          # reset deg into 0 deg
        time.sleep(0.5)                        # time delay

    lineangle = lineangle + np.deg2rad(1)      # increase angle by 1 deg
    
    ax.lines.pop()                             # delete previous line
    # plot line
    line = ax.plot([0,lineangle],[0,100], color='#03ff69', linewidth='2', linestyle='solid')

    return line

## Function for button click event
# start animation
def start(event):
    global anim, begin, resume, running

    if begin:    # start
        begin = False
        running = True
        startbtn.label.set_text('Pause')
        anim = animation.FuncAnimation(fig, animate, init_func=lambda:line, interval=10)
    elif resume: # resume
        resume = False
        running = True
        startbtn.label.set_text('Pause')
        anim.event_source.start() # resume animation
    else:        # pause
        resume = True
        startbtn.label.set_text('Resume')
        anim.event_source.stop()  # pause animation
        
    
# pause animation
def stop(event):
    global running

    if running: # if animation is running
        anim.event_source.stop()  # pause animation 
    
    plt.close()                   # close window
    
### System
begin = True       # True means that the system needs to start animation for its first time
resume = False     # True means that the system needs to resume animation
running = False    # True means that the system is running
lineangle = 0      # line angle at default condition

### graph
fig = plt.figure(facecolor='k', figsize=[8,6])     # add figure on window
ax = fig.add_subplot(111,polar=True,facecolor='k') # add plot on figure
ax.grid('both',color='#02fe14',linewidth=1)        # grid configuration
startax = plt.axes([0.75, 0.05, 0.075, 0.05])      # axes for start button
stopax = plt.axes([0.85, 0.05, 0.075, 0.05])       # axes for stop button
startbtn = Button(startax,'Start')                 # set button
stopbtn = Button(stopax,'Stop')                    # set button

# plot line
line = ax.plot([0,0],[0,100], color='#03ff69', linewidth='2', linestyle='solid')

startbtn.on_clicked(start)
stopbtn.on_clicked(stop)

plt.show()
