# rtlsdr spectrum
 Using RTL-SDR Dongle to watching spectrum, some DSP...
 
## Run: python 103e6 
 
### Modules:
    
    + numpy (pip install numpy)
    + pyrtlsdr (pip install pyrtlsdr, https://pypi.org/project/pyrtlsdr/#files)
    + pyqtgraph (pip install pyqtgraph, https://pypi.org/project/pyqtgraph/#files)
    
## pyrtlsdr:
    Installation pyrtlsdr on Win:
       1. Download and extract: https://osmocom.org/attachments/download/2242/RelWithDebInfo.zip 
          to your folder (c:\path)
       2. Add your folder to SYSTEMPATH (example: PATH: "C:\_py\Libs\rtlsdr_dll")
       3. Attention. There must be the same bit depth of the Python interpreter and the downloaded libraries. I'm working with x64.
                          on Linux (Ubuntu):
       1. sudo apt install librtlsdr
    

![](https://github.com/weider938/rtlsdr-spectrum/blob/master/src/spectrum2.PNG)
