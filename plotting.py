# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:39:32 2020

@author: Zaca
"""

def default_plot(ax, spines): 
    
    import matplotlib.pyplot as plt
    
    ax = plt.gca()
    # Remove unnecessary axes and ticks (top and bottom)
    ax.spines["top"].set_visible(False)   
    ax.spines["right"].set_visible(False)
    ax.get_xaxis().tick_bottom()  
    ax.get_yaxis().tick_left()
    
    # Set the ticks facing OUTWARD
    ax.get_yaxis().set_tick_params(direction='out')
    ax.get_xaxis().set_tick_params(direction='out')
    
    # Remove grid
    #ax.grid('off')
    
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # outward by 10 points

    # turn off ticks where there is no spine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
        
    if 'right' in spines:
        ax.yaxis.set_ticks_position('right')

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')

    return ax


def make_hcolorbar(data, units, cmap, filename):
    
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    
    fig, ax = plt.subplots(figsize=(6, 1))
    fig.subplots_adjust(bottom=0.5)
    
    # normalize colormap
    norm = mpl.colors.Normalize(vmin=min(data), vmax=max(data))

    # plot the colorbar
    cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, orientation='horizontal')
    
    # set label
    cb1.set_label(units)
    
    # save figure
    plt.savefig(filename)
    