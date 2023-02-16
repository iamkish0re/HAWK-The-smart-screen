"""utils.py"""

def reduce_brightness(BRIGHTFLAG):
    brightness = BRIGHTFLAG #Brightness in perentage 
    #Basically does what we needs to be done xD
    c = wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness, 0)
