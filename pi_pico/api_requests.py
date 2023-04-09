"""
Program: Pico requester

Device: Raspberry Pi Pico
Description: Make API Requests with a Pi Pico (needs http url)

"""
import time
import network
import urequests as requests

ssid = '<SSID>'
password = '<PASS>'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connect or fail
max_wait = 10

while max_wait > 0:

    if wlan.status() < 0 or wlan.status() >= 3:
        break

    max_wait -= 1

    print('waiting for wireless connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:

    raise RuntimeError('network connection failed')

else:

    print('connected via WiFi')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

while True:

    # Do things here, perhaps measure something using a sensor?
    # ...and then define the headers and payloads
    headers = ''
    payload = ''

    # Then send it in a try/except block
    try:

        print("sending request...")
        # response = requests.post("https://www.google.com", headers=headers, data=payload)
        response = requests.get("http://www.raspberrypi.com/")

        print("sent (" + str(response.status_code) + "), status = " + str(wlan.status()) )

        # print(dir(response))
        # ['__class__', '__init__', '__module__', '__qualname__', 'close', '__dict__', 'encoding', 'text', 'json', 'status_code', 'reason', 'raw', '_cached', 'content']
        print(f"encoding: {response.encoding}")
        print(f"text: {response.text}")
        print(f"json: {response.json()}")
        
        response.close()
    
    except:
    
        print("could not connect to server (Wlan status =" + str(wlan.status()) + ")")
        
        if wlan.status() < 0 or wlan.status() >= 3:
        
            print("trying to reconnect...")
        
            wlan.disconnect()
            wlan.connect(ssid, password)
            
            if wlan.status() == 3:
        
                print('connected')
            else:
        
                print('failed')
    
    time.sleep(5)


# Sample -->

# sent (302), status = 3
# ['__class__', '__init__', '__module__', '__qualname__', 'close', '__dict__', 'encoding', 'text', 'json', 'status_code', 'reason', 'raw', '_cached', 'content']
# encoding: utf-8
# text: 
# json: <bound_method>
# reason: b'Found'
# content: b''
