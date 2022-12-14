import time, gc, os
import pwmio
import board
from adafruit_motor import servo

import feathers3
import sensors

motor: servo.ContinuousServo

def setup():
    print("\Booting Active Aero Flight Controller!")
    print("------------------\n")

    print("Memory Info - gc.mem_free()")
    print("---------------------------")
    print("{} Bytes\n".format(gc.mem_free()))

    flash = os.statvfs('/')
    flash_size = flash[0] * flash[2]
    flash_free = flash[0] * flash[3]
    # Show flash size
    print("Flash - os.statvfs('/')")
    print("---------------------------")
    print("Size: {} Bytes\nFree: {} Bytes\n".format(flash_size, flash_free))
    print("---------------------------")
    
    pwm = pwmio.PWMOut(board.A2, frequency=50)
    pwm.duty_cycle = 1500
    global motor
    motor = servo.ContinuousServo(pwm, min_pulse=1000, max_pulse=2000)


def main():
    print(f"{'Time':<15} {'Acceleration':<40} {'Gyro':<45} {'Altitude':<10}")
    while True:
        # Set color of NeoPixel
        # pixel[0] = ( r, g, b, 0.5)
        
        # current_time = time.time()
        # sensor_data = sensors.get_sensor_data()
        # print(f"{current_time:<15} {str(list(sensor_data['acceleration'])):<40} {str(list(sensor_data['gyro'])):<45} {sensor_data['altitude']:<10}")
        throttle = float(input("Input the desired speed: "))
        print(throttle)
        motor.throttle = throttle
        
        time.sleep(0.1)
