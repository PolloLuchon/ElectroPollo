from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


sensor = ColorSensor(Port.A)
motord = Motor(Port.B)
motori = Motor(Port.F,Direction.COUNTERCLOCKWISE)

contador = 0

Color.WHITE = Color(h=195, s=11, v=75)
Color.BLACK = Color(h=180, s=20, v=29)

Colores_ = (Color.WHITE, Color.BLACK, Color.NONE)

sensor.detectable_colors(Colores_)

motord.run(400)
motori.run(400)
wait(7000)


while True:

    color = sensor.color()
    print(sensor.color())
    wait(100)
    motord.run(250)
    motori.run(250)

    if color == Color.WHITE :
        motord.stop()
        motori.stop()
        motord.run_angle(250,-300, wait= False)
        motori.run_angle(250,300)
        motori.run(250)
        motord.run(250)
        wait(1000)
        motori.run(-250)
        motord.run(-250)
        wait(1000)
        motord.run_angle(250,290, wait= False)
        motori.run_angle(250,-290)
        contador += 1
    # if color == Color.BLACK:
    #     break    

    if contador >= 3:
        break
            
