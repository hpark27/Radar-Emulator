import time
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import functions as funcs
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Button

### Function
# Function to regenerate plot axes
def regenerateAxes():
    ax.cla()                                           # clear axes
    ax.grid('both',color='#02fe14',linewidth=1)        # grid configuration
    ax.set_xlim(0,2*np.pi)                             # set x axis limit - 360 deg
    ax.set_ylim(0,110)                                 # set y axis limit - upto 110 m

    # plot line
    ax.plot([0,0],[0,100], color='#03ff69', linewidth='2', linestyle='solid')

# Function to animate line rotation
def animate(i):
    # Global variable
    # lineangle - search line angle
    # theta     - angle of random target positions
    # r         - distance of random target positions
    global lineangle, theta, r

    if round(lineangle,12)==round(2*np.pi,12):    # when angle is 360 deg
        lineangle = 0                             # reset deg into 0 deg
        ax.cla()                                  # clear plot
        time.sleep(0.5)                           # time delay
        regenerateAxes()                          # re-generate plot axes

    lineangle = lineangle + np.deg2rad(10)        # increase angle by 1 deg
    
    ax.lines.pop()                                # delete previous line
    
    for j in range(len(theta)):
        if theta[j] < lineangle:                  # when target is located in search area
            ax.scatter(theta[j],r[j],c='#03ff69') # plot target location

    # plot line
    line = ax.plot([0,lineangle],[0,100], color='#03ff69', linewidth='2', linestyle='solid')

    return line

## Function for button click event
# start animation
def start(event):
    global anim, begin, resume, running

    print('Start button clicked')

    if begin:    # start
        begin = False
        running = True
        startbtn.label.set_text('Pause')
        anim = animation.FuncAnimation(fig, animate, init_func=lambda:line, interval=100)
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

    print('Stop button clicked')

    if running: # if animation is running
        anim.event_source.stop()  # pause animation 
    
    plt.close()                   # close window
    
### System
begin = True       # True means that the system needs to start animation for its first time
resume = False     # True means that the system needs to resume animation
running = False    # True means that the system is running
lineangle = 0      # line angle at default condition

theta, r = funcs.randpos()                         # random target positions

### Graph
fig = plt.figure(facecolor='k', figsize=[8,6])     # add figure on window
ax = fig.add_subplot(111,polar=True,facecolor='k') # add plot on figure
ax.grid('both',color='#02fe14',linewidth=1)        # grid configuration
startax = plt.axes([0.75, 0.05, 0.075, 0.05])      # axes for start button
stopax = plt.axes([0.85, 0.05, 0.075, 0.05])       # axes for stop button
startbtn = Button(startax,'Start')                 # set button
stopbtn = Button(stopax,'Close')                   # set button
ax.set_xlim(0,2*np.pi)                             # set x axis limit - 360 deg
ax.set_ylim(0,110)                                 # set y axis limit - upto 110 m

# plot line
line = ax.plot([0,0],[0,100], color='#03ff69', linewidth='2', linestyle='solid')

### System operation
# button click event
startbtn.on_clicked(start) # start animation
stopbtn.on_clicked(stop)   # close window

plt.show()
