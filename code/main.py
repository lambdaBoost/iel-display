from sr_74hc595_bitbang import SR
from iel_display import display_digit
from machine import Pin
from secrets import secrets
from get_data import get_time
import network
import time
import wifimgr

try:
  import usocket as socket
except:
  import socket
  
  
ssid = secrets['ssid']
pw = secrets['pw']

URI = "http://192.168.1.215:8080"


wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(ssid, pw)

def light_onboard_led():
    led = machine.Pin('LED', machine.Pin.OUT)
    led.on();

timeout = 10
while timeout > 0:
    if wlan.status() >= 3:
        light_onboard_led()
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
    
    tm = get_time(URI + "/time/")
    print(tm)
    
    if len(tm) < 4:
        tm = '0'+tm
    
    d0 = tm[0]
    d1 = tm[1]
    d2 = tm[2]
    d3 = tm[3]
    
    display_digit(d3,sr)
    display_digit(d2,sr)
    display_digit(d1,sr)
    display_digit(d0,sr)
    
    time.sleep(30)
        
        

