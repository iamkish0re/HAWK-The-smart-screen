#For this code to run install the following
# --> pip install wmi
# --> pip install pywin32
import wmi
def reduce_brightness():
    brightness = 40 #Brightness in perentage 
    #Basically does what we needs to be done xD
    c = wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness, 0)