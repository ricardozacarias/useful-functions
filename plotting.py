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

# makes a horizontal colorbar with the provided arguments
def make_hcolorbar(data, units, cmap, filename):
    
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    
    fig, ax = plt.subplots(figsize=(6, 2))
    fig.subplots_adjust(bottom=0.5)
    
    # normalize colormap
    norm = mpl.colors.Normalize(vmin=min(data), vmax=max(data))

    # plot the colorbar
    cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, orientation='horizontal')
    
    # set label
    cb1.set_label(units)
    
    # save figure
    plt.savefig(filename, dpi=600)
    
# this function manually truncates colormaps in order to get the colors that we want.
# it has the option of inverting the truncated version aswell.
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100, reverse=False):
    
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import numpy as np
    
   
    if reverse:
        new_cmap = mpl.colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(maxval, minval, n))) 
        
        arr = np.linspace(0, 50, 100).reshape((10, 10))
        fig, ax = plt.subplots(ncols=2)
        ax[0].imshow(arr, interpolation='nearest', cmap=cmap)
        ax[1].imshow(arr, interpolation='nearest', cmap=new_cmap)
        plt.show()
                
        return new_cmap
   
    else:
        new_cmap = mpl.colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
        
        arr = np.linspace(0, 50, 100).reshape((10, 10))
        fig, ax = plt.subplots(ncols=2)
        ax[0].imshow(arr, interpolation='nearest', cmap=cmap)
        ax[1].imshow(arr, interpolation='nearest', cmap=new_cmap)
        plt.show()
        
        return new_cmap

# extract n colors from a colormap and plots the results in a palplot
def get_colors(cmap, n):
    
    import matplotlib as mpl
    import seaborn as sns
    import numpy as np
    
    cmap = mpl.cm.get_cmap(cmap)
    rgba = [cmap(x) for x in np.linspace(0.01, 0.99, n)]
    sns.palplot(sns.color_palette(rgba));    
    return rgba

# extract a single color from a colormap
def get_single_color(cmap, n):
    
    import matplotlib as mpl   
    
    cmap = mpl.cm.get_cmap(cmap)
    rgba = cmap(n)
    return rgba
    