import sys
import time
import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.Point import Point
from rtlsdr import RtlSdr

# own modules from dsp.py libraries:
from dsp import find_max
from dsp import mult_signal_on_sin
from dsp import make_average

# from dsp import mult_signals
# from dsp import fast_ft
# from dsp import get_window

sdr = RtlSdr()


if sys.argv[1]:
    cf = float(sys.argv[1])
else:
    cf = 103e6

	
sample_rate = 2500e3

sdr.sample_rate = sample_rate  #250e3 260 300 1000 2000 1500 2500
sdr.center_freq = cf
sdr.gain = 30


p = pg.plot()
p.setWindowTitle('rtlsdr spectrum') # title of window
curve = p.plot(pen="g") # colour of curves

def update():

    time.sleep(0.2) # rate update
    global sdr, curve, p, cf
    
    count_samples = 8192 # size of window
    cycles_averaging = 2
    list_samples = []
	
    for _ in range(cycles_averaging):
        samples = sdr.read_samples(count_samples)
        list_samples.append(samples)
        
    average_samples = make_average(list_samples)


    shifted_samples = mult_signal_on_sin(signal = average_samples,
                                     window = count_samples,
                                     harmonic = count_samples/2,
                                     samp_rate = 1.024e6)
    sp = np.fft.fft(np.array(shifted_samples))


    drawing_spectrum = abs(np.array(sp))
    ordinata_limit = find_max(drawing_spectrum) + 30
    p.setRange(QtCore.QRectF(0, 0, int(len(drawing_spectrum)), int(ordinata_limit))) 
    cf_Mhz = cf / 1000000
    p.setTitle('Central frequency: %0.2f MHz' % cf_Mhz)
    curve.setData(abs(drawing_spectrum))

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()