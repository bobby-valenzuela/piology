# pico
from utime import sleep
import machine

def blink_led(led,duration):
    # Begin in off state
    try:
        led.off()
        
        for i in range(0, 5):
            led.toggle()
            sleep(duration)
            led.toggle()
            sleep(duration)
    except:
        pass
    
def get_temp(units='c'):
    
    sensor_temp = machine.ADC(4)
    convert = 3.3 / (65535)
    reading = sensor_temp.read_u16() * convert
    temperature = 27 - (reading - 0.706)/0.001721
    
    # If seeking Fahrenheit because 'murica
    if units == 'f':    
        temperature = temperature * 1.8 + 32

    return round(temperature,2)

def get_html(temp):
    

    html = """ <!DOCTYPE html>
    <html>
    <head>
        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

        <!-- Compiled and minified JavaScript -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
        
        <!-- icons -->
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

                
        <title>PicoPlayTime</title>
    </head>
    <body>
        <h1>Pico W</h1>
        <p>Hello World</p>
        
        <!-- Navbar goes here -->
        <nav>
            <div class="nav-wrapper">
              <a href="#" class="brand-logo">PicoPlay</a>                                                                                                                                                                                                       
              <ul id="nav-mobile" class="right hide-on-med-and-down">
                <li><a href="sass.html">Sass</a></li>
                <li><a href="badges.html">Components</a></li>
                <li><a href="collapsible.html">JavaScript</a></li>
              </ul>
            </div>
      </nav>
            

        <!-- Page Layout here -->
        <div class="row">

            <div class="col s12 m4 l3"> <!-- Note that "m4 l3" was added -->
            <!-- Grey navigation panel

                  This content will be:
              3-columns-wide on large screens,
              4-columns-wide on medium screens,
              12-columns-wide on small screens  -->

          </div>

          <div class="col s12 m8 l9"> <!-- Note that "m8 l9" was added -->
            <!-- Teal page content

                  This content will be:
              9-columns-wide on large screens,
              8-columns-wide on medium screens,
              12-columns-wide on small screens  -->

                <a class="waves-effect waves-light btn-large" href="/lighton">
                    <i class="material-icons right">highlight</i>Turn On
                </a>
                <a class="waves-effect waves-light btn-large" href="/lightoff">
                    <i class="material-icons right">highlight_off</i>Turn Off
                </a>
                
                <p>Current Temp: {0}</p>

                <a class="waves-effect waves-light btn-large" href="/servosensorshort">
                    <i class="material-icons right">highlight</i>Start Sensor (~10s)
                </a>
                <a class="waves-effect waves-light btn-large" href="/servosensor">
                    <i class="material-icons right">highlight_off</i>Stop Sensor (Ongoing)
                </a>
                

    </div>

        </div>

        
    </body>
    </html>
    """
    html = html.format(temp)
    
    return html


