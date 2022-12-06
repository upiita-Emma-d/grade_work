import sys
import glob
import serial
import time
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

def limpiar_buffer(serial_arduino):
    serial_arduino.flushInput()
    serial_arduino.write(bytes("o", 'utf-8'))
    timeout=time.time()+3.0
    data = b""
    while serial_arduino.inWaiting() or time.time()-timeout<0.0:
        if serial_arduino.inWaiting()>0:
            data+=serial_arduino.read(serial_arduino.inWaiting())
            timeout=time.time()+1.0


def open_port_serial(port_string):
    serial_arduino = serial.Serial(port_string, 9600)
    limpiar_buffer(serial_arduino)
    print("Phase 3")
    cadena  = "adc_0"
    serial_arduino.write(bytes(cadena, 'utf-8'))
    print("Phase 4")
    data = serial_arduino.readline()
    print(data)
    data = serial_arduino.readline()
    print(data)
    data = serial_arduino.readline()
    print(data)
    los_datos = []
    while 1:
        data = serial_arduino.readline()
        #print(data)
        data_i = data.decode("utf-8")
        try: 
            los_datos.append(float(data_i.replace(",\r\n","")))
        except:
            pass
        if data ==  (b'FIN\r\n'):
            print(los_datos)
            break
    return los_datos