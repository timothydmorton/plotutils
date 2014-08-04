plotutils
=========

Matplotlib-related plotting utility functions I have found useful.

setfig
------
This will create a new figure (same as plt.figure() call in matplotlib):
   from plotutils.plotutils import setfig
   setfig(None)

You can also set the current figure to be a given figure number, clear it, and start over, e.g.:
   setfig(3)

A value of 0 will do nothing, implying you want to overplot on whatever the currently active figure is:
   setfig(0)

I use the `setfig` function in every function that I write that makes a plot, almost always as follows:
   def my_plot(x,y,fig=None,**kwargs):
     setfig(fig)
     plt.plot(x,y,**kwargs)
