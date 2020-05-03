#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from time import sleep
from threading import Thread
import os
import socket

client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False
SERVER_IP = '192.168.86.101'
SERVER_PORT = 50001

brick.light(Color.BLACK)
print('running')
j = 0

def connect():
    global client_skt
    client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con_result = client_skt.connect((SERVER_IP, SERVER_PORT))
    except:
        print('connect exception')


def tick():
    global j
    global client_skt
    
    while True:
        j+=1
        print('tick ' + str(j))
        send_result = 0
        try:
            send_result = client_skt.send(bytes('*', 'utf-8'))
        except:
            print('send exception')
        finally:
            sleep(1)
            if (send_result == 0):
                connected = False
                brick.light(Color.RED)
                client_skt.close()
                connect()
            else:
                connection = True
                brick.light(Color.GREEN)
            #print('send_result:' + str(send_result))
            
        
connect()
t = Thread(target=tick)
t.start()

while True:
    sleep(0.1)



