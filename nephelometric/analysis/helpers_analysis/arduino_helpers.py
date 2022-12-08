import sys
import glob
import serial
import time
import json
import itertools
list2d = [[1,2,3], [4,5,6], [7], [8,9]]
merged = list(itertools.chain(*list2d))

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


def main_arduino(port_string):
    serial_arduino = serial.Serial(port_string, 9600)
    limpiar_buffer(serial_arduino)
    serial_arduino.write(bytes("sensor_0", 'utf-8'))
    los_datos = []
    while 1:
        data = serial_arduino.readline()
        data_i = data.decode("utf-8")
        if data ==  (b'END\r\n'):
            break
        try:
            los_datos.append(json.loads(data_i))
        except ValueError:
            print("Error")
            pass
    return los_datos

def parser_values_to_voltage(dato):
            try:
                print(dato)
                return int(dato) *  (5 /65636)
            except ValueError:
                pass

def create_array_structure(datos_arduino):
    general_list = []
    for i in datos_arduino:
            data_list = i.get("sensor1",None)
            if data_list is not None:
                data_list = data_list.replace('[','').replace(']','').split(',')
                data_list = [ parser_values_to_voltage(value) for value in data_list]
                general_list.append(data_list)
    return list(itertools.chain(*general_list))
