# rtlsdr spectrum
 Using RTL-SDR Dongle to watching spectrum, some python, some DSP...
 
## running: python 103e6 
 
![](https://github.com/weider938/rtlsdr-spectrum/blob/master/src/spectrum1.PNG)

### Modules:
    
    + numpy (pip install numpy)
    + pyrtlsdr (pip install pyrtlsdr, https://pypi.org/project/pyrtlsdr/#files)
    + pyqtgraph (pip install pyqtgraph, https://pypi.org/project/pyqtgraph/#files)
    
## pyrtlsdr:
    Installation pyrtlsdr on Win:
       1. You must install drivers Zadig (https://zadig.akeo.ie/);
       2. Download and extract: https://osmocom.org/attachments/download/2242/RelWithDebInfo.zip  
          to your folder (c:\path);
       3. Add your folder to SYSTEMPATH (example: PATH: "C:\_py\Libs\rtlsdr_dll");
       4. Attention. There must be the same bit depth of the Python interpreter and the downloaded libraries. I'm working with x64.
                          on Linux (Ubuntu):
       1. sudo apt install librtlsdr.
    
## pyqtgraph:
     Visit: http://www.pyqtgraph.org/
