import serial
import socket
import time

# LiDAR Setup
SERIAL_PORT = '/dev/ttyAMA0'  # Enter correct serial port for LiDAR
BAUD_RATE = 115200

# Socket Setup
HOST = '192.168.0.104'  # Local system's IP address
PORT = 7600  # Port number

def parse_data(recv):
    """Parse the serial data and return the distance."""
    if recv[0] == 0x59 and recv[1] == 0x59:  # Check for correct data packet start
        distance = recv[2] + recv[3] * 256
        return distance
    else:
        return None

def get_tfmini_data(ser, sock):
    """Read and process data from the TFmini LiDAR sensor, then send via socket."""
    while True:
        try:
            if ser.in_waiting >= 9:
                recv = ser.read(9)
                ser.reset_input_buffer()

                distance = parse_data(recv)
                if distance is not None:
                    print("Distance: {} cm".format(distance))
                    # Send the distance data via socket
                    sock.sendall(str(distance).encode())

        except serial.SerialException as e:
            print("Serial error: ", e)
            break
        except OSError as e:
            print("OS error: ", e)
            break

def main():
    """Main function to initialize serial connection and socket, then read and send data."""
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE) as ser:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((HOST, PORT))
                get_tfmini_data(ser, sock)
    except serial.serialutil.SerialException as e:
        print("SerialException: ", e)
    except Exception as e:
        print("An unexpected error occurred: ", e)

if __name__ == '__main__':
    main()
