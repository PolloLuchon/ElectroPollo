from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#Creacion de Variables
motor_izquierdo = Motor(Port.E)
motor_derecho = Motor(Port.F)

#Comando de Trabajo
#PasoUnoAvanza
motor_izquierdo.run(-360)
motor_derecho.run(360)

wait(3000)
#GiroUno
motor_izquierdo.run(180)
motor_derecho.run(180)

wait(850)

#PasoDosAvanza
motor_izquierdo.run(-360)
motor_derecho.run(360)

wait(2000)
#GiroDos
motor_izquierdo.run(180)
motor_derecho.run(180)

wait(1050)

#PasoTresAvanza
motor_izquierdo.run(-360)
motor_derecho.run(360)

wait(3000)
#GiroTres
motor_izquierdo.run(180)
motor_derecho.run(180)

wait(850)

#PasoCuatroAvanza
motor_izquierdo.run(-360)
motor_derecho.run(360)

wait(1500)
