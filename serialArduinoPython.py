#####################################################
##        Comunicação serial Python Arduino        ##
##            Autor: Raul Melo - TrixLog           ##
##             Data:  15/12/2017 17:14             ##
#####################################################

import serial
from serial import SerialException
import time

port = 'COM4'
connected = 0

# Captura exception caso a comunicação falhe
try:
    ard = serial.Serial(port,9600,timeout=5)
    connected = 1
except SerialException:
    print("Conexão com o dispositivo não estabelecida!!!")
    print("Desconecte e conecte o dispositivo novamente!!!")

if connected:
    while 1:
        # Escreve 'l' para ligar o led
        ard.write(b'l')
        # Recebe confirmação do arduino
        arduinoData = ard.readline()[:-2]
        # Printa na tela o status do led
        print(arduinoData)
        time.sleep(1)
        # Escreve 'd' para desligar o led
        ard.write(b'd')
        # Recebe confirmação do arduino
        arduinoData = ard.readline()[:-2]
        # Printa na tela o status do led
        print(arduinoData)
        time.sleep(1)
