from sr_74hc595_bitbang import SR
from iel_display import display_digit, display_all
from machine import Pin
from secrets import secrets
from get_data import get_time
import network
import time


try:
  import usocket as socket
except:
  import socket
  
  
ssid = secrets['ssid']
pw = secrets['pw']

URI = "http://192.168.1.20:8080"


wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(ssid, pw)


timeout = 10
while timeout > 0:
    if wlan.status() >= 3:
        break
    timeout -= 1
    print('Waiting for connection...')
    time.sleep(1)
   
wlan_status = wlan.status()

    
#instantiate shift register object
ser = Pin(18, Pin.OUT)
rclk = Pin(16, Pin.OUT)
srclk = Pin(17, Pin.OUT)
oe = Pin(3, Pin.OUT, value=0)    # low enables output
srclr = Pin(4, Pin.OUT, value=1) # pulsing low clears data
sr = SR(ser, srclk, rclk, srclr, oe)


while True:
    
    try:
        tm = get_time(URI + "/time")
        
        tm0 = tm[0]
        tm1 = tm[1]
        tm2 = tm[2]
        tm3 = tm[3]
        
        display_digit(tm0, sr)
        display_digit(tm1, sr)
        display_digit(tm2, sr)
        display_digit(tm3, sr)
    
    except:
        display_digit('e', sr)
        display_digit('r', sr)
        display_digit('r', sr)
    
    sleep(60)
    
    