# pi pico
import network, socket, time, re, utilities
from utime import sleep
from machine import Pin, PWM

# IR Sensor
prox_sensor = Pin(0, Pin.IN)

# Servo motor
servo_01 = PWM(Pin(1))
servo_01.freq(50)

# Servo Config
MIN = 1000000
MAX = 2000000

# Functions for the servo sensor feature
def detected_obj():
    return 1 if prox_sensor.value() == 0 else 0
    
def move_servo(dir):
    
    if dir == 'l':
        servo_01.duty_ns(MAX)
    else:        
        servo_01.duty_ns(MIN)

# Onboard led
led = Pin("LED", Pin.OUT)
led.off()

# Connect to Network
ssid = '<SSID>'
password = '<PASS>'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Get current temperature
temp = utilities.get_temp('f')

print(f"Temp: {temp}")

html = utilities.get_html(temp)

# Wait for connect or fail
max_wait = 10

while max_wait > 0:

    if wlan.status() < 0 or wlan.status() >= 3:
        break

    max_wait -= 1
    print('Connecting via WiFi...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:

    raise RuntimeError('Could not connect to WiFi network')

    # If no wireless connection - show five slow (1s) blinks
    utilities.blink_led(led,1)
        
else:

    print(f'Network connected via {ssid}')

    status = wlan.ifconfig()
    print( 'Pico Local IP: ' + status[0] )

    # Show five quick led blinks
    utilities.blink_led(led,0.03)
    
# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()

# Attempt to bind socket - if already bound, close and rebind
try:   
    s.bind(addr)
    
except:
    s.close()
    s.bind(addr)
    
    
s.listen(1)

print('Server listening on', addr)

# Listen for connections
while True:
    try:
        # Returns connection object (cl) and client address (addr)
        cl, addr = s.accept()
        print('client connected from', addr)
        
        request = cl.recv(1024)
        request = str(request)
        # print(f"Request: {request}")
        
        led_on = request.find('/lighton')
        led_on = 0 if led_on == -1 else 1
        
        # Activate Proximity Sensor and Motor feature 
        start_detection_short = request.find('/servosensorshort')
        start_detection_short = 1 if start_detection_short != -1 else 0
        start_detection = request.find('/servosensor')
        start_detection = 1 if start_detection != -1 else 0        

        print(f"Lighton: {led_on}")

        if led_on :
            led.on()
        else:
            led.off()
   
        print(f"Start: {start_detection} Short: {start_detection_short}")
        counter = 0
        counter_limit = 100 # about 10s
        
        if start_detection  or start_detection_short :
                        
            # Initiate servo left
            move_servo('l')

            while counter < counter_limit:
                
                if detected_obj() == 0 :
                    move_servo('l') 
                else:
                    move_servo('r')
                    
                sleep(0.10)
                
                # If using short method, use counter to limit to 10s (100 runs)
                if start_detection_short:
                    counter += 1
                
        response = html
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        sleep(1)
    
    except OSError as e:
        cl.close()
        print('connection closed')
        
        


