import os
import serial
from time import time

TEMPOMAXIMO = 3 #SEGUNDOS

with open('./dados.csv', "w") as file:
    s = serial.Serial("COM3", 1000000)
    t_inicio = time()
    file.write('Tempo(us);Tempo(ms);Valor\r')
    while time() - t_inicio < TEMPOMAXIMO:
        linha = s.readline().decode().replace('\n', '')
        file.write(linha)


os.startfile(os.path.abspath('./dados.csv'))
