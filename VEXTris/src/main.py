# --------------------------------------------------------------------------------- #
#                                                                                   #
#    Project:          Base Robot With Sensors                                      #
#    Module:           main.py                                                      #
#    Author:           VEX                                                          #
#    Created:          Fri Aug 05 2022                                              #
#    Description:      Base IQ Gen 2 robot with controls and with sensors           #
#                                                                                   #
#    Configuration:    BaseBot with Sensors (Drivetrain 2-motor, Inertial)          #
#                      Left Motor in Port 1                                         #
#                      Right Motor in Port 6                                        #
#                      TouchLED in Port 2                                           #
#                      Optical Sensor in Port 3                                     #
#                      Distance Sensor in Port 7                                    #
#                      Bumper in Port 8                                             #
#                                                                                   #
# --------------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
left_drive_smart = Motor(Ports.PORT1, 1, False)
right_drive_smart = Motor(Ports.PORT6, 1, True)

drivetrain = SmartDrive(left_drive_smart, right_drive_smart, brain_inertial, 200)
touchled_2 = Touchled(Ports.PORT2)
optical_3 = Optical(Ports.PORT3)
distance_7 = Distance(Ports.PORT7)
bumper_8 = Bumper(Ports.PORT8)


def calibrate_drivetrain():
    # Calibrate the Drivetrain Inertial
    sleep(200, MSEC)
    brain.screen.print("Calibrating")
    brain.screen.next_row()
    brain.screen.print("Inertial")
    brain_inertial.calibrate()
    while brain_inertial.is_calibrating():
        sleep(25, MSEC)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)


# Begin project code

from vex import *


L_BLOCK = [
    [
    [False,True,False,False],
    [False,True,False,False],
    [False,True,True,False],
    [False,False,False,False],
    ],
    [
    [False,False,False,False],
    [False,False,False,True],
    [False,True,True,True],
    [False,False,False,False],
    ],
    [
    [False,True,True,False],
    [False,False,True,False],
    [False,False,True,False],
    [False,False,False,False],
    ],
    [
    [False,False,False,False],
    [True,True,True,False],
    [True,False,False,False],
    [False,False,False,False],
    ]
]
O_BLOCK = [
    [
    [False,False,False,False],
    [False,True,True,False],
    [False,True,True,False],
    [False,False,False,False],
    ],
    [
    [False,False,False,False],
    [False,True,True,False],
    [False,True,True,False],
    [False,False,False,False],
    ],
    [
    [False,False,False,False],
    [False,True,True,False],
    [False,True,True,False],
    [False,False,False,False],
    ],
    [
    [False,False,False,False],
    [False,True,True,False],
    [False,True,True,False],
    [False,False,False,False],
    ]
]
T_BLOCK = [
        [
    [False,False,False,False],
    [False,False,True,False],
    [False,True,True,True],
    [False,False,False,False],
    ],
    [
    [False,False,False,False],
    [False,True,False,False],
    [False,True,True,False],
    [False,True,False,False],
    ],
    [
    [False,False,False,False],
    [True,True,True,False],
    [False,True,False,False],
    [False,False,False,False],
    ],
    [
    [False,False,False,False],
    [False,False,False,False],
    [True,True,True,False],
    [False,True,False,False],
    ]
]
I_BLOCK =   [  
    [
    [True,False,False,False],
    [True,False,False,False],
    [True,False,False,False],
    [True,False,False,False],
    ],
    [
    [False,False,False,False],
    [False,False,False,False],
    [False,False,False,False],
    [True,True,True,True],
    ],
    [
    [True,False,False,False],
    [True,False,False,False],
    [True,False,False,False],
    [True,False,False,False],
    ],
    [
    [False,False,False,False],
    [False,False,False,False],
    [False,False,False,False],
    [True,True,True,True],
    ]
]
Z_BLOCK = [
    [
    [False,False,False,False],
    [True,True,False,False],
    [False,True,True,False],
    [False,False,False,False],
    ],
    [
    [False,False,True,False],
    [False,True,True,False],
    [False,True,False,False],
    [False,False,False,False],
    ],
    [
    [False,False,False,False],
    [False,True,True,False],
    [False,False,True,True],
    [False,False,False,False],
    ],
    [
    [False,False,True,False],
    [False,True,True,False],
    [False,True,False,False],
    [False,False,False,False],
    ]
]
LR_BLOCK = [
    [
    [False,False,True,False],
    [False,False,True,False],
    [False,True,True,False],
    [False,False,False,False],
    ],
    [
    [False,False,False,False],
    [True,False,False,False],
    [True,True,True,False],
    [False,False,False,False],
    ],
    [
    [False,True,True,False],
    [False,True,False,False],
    [False,True,False,False],
    [False,False,False,False],
    ],
    [
    [False,False,False,False],
    [False,True,True,True],
    [False,False,False,True],
    [False,False,False,False],
    ]
]
ZR_BLOCK = [
    [
    [False,False,False,False],
    [False,False,True,True],
    [False,True,True,False],
    [False,False,False,False],
    ],
    [
    [False,True,False,False],
    [False,True,True,False],
    [False,False,True,False],
    [False,False,False,False],
    ],
    [
    [False,False,False,False],
    [False,False,True,True],
    [False,True,True,False],
    [False,False,False,False],
    ],
    [
    [False,True,False,False],
    [False,True,True,False],
    [False,False,True,False],
    [False,False,False,False],
    ],
]

def get_block(block_num):
    if block_num == 0:
        return L_BLOCK
    elif block_num == 1:
        return LR_BLOCK
    elif block_num == 2:
        return O_BLOCK
    elif block_num == 3:
        return I_BLOCK
    elif block_num == 4:
        return T_BLOCK
    elif block_num == 5:
        return Z_BLOCK
    elif block_num == 6:
        return ZR_BLOCK
    else:
        return None
    
brain=Brain()
controller = Controller()

brain_inertial = Inertial()
left_drive_smart = Motor(Ports.PORT1, 1, False)
right_drive_smart = Motor(Ports.PORT6, 1, True)

drivetrain = SmartDrive(left_drive_smart, right_drive_smart, brain_inertial, 200)
touchled_2 = Touchled(Ports.PORT2)
optical_3 = Optical(Ports.PORT3)
distance_7 = Distance(Ports.PORT7)
bumper_8 = Bumper(Ports.PORT8)


def calibrate_drivetrain():
    sleep(200, MSEC)
    brain.screen.print("Calibrating")
    brain.screen.next_row()
    brain.screen.print("Inertial")
    brain_inertial.calibrate()
    while brain_inertial.is_calibrating():
        sleep(25, MSEC)
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
brain.screen.render()

herni_pole = [[False]*10 for i in range(20)]
# herni_pole[0][5] = True
# herni_pole[1][3] = True
# herni_pole[0][0] = True
velikost_bloku = 8
def vykresli_pole():
    for y in range(20):
        for x in range(10):
            if herni_pole[y][x]:
                brain.screen.draw_rectangle(y*velikost_bloku, (10-x)*velikost_bloku, velikost_bloku, velikost_bloku)
def vykresli_blok(x_pos, y_pos, cislo_bloku, rotace):
    blok = get_block(cislo_bloku)
    if blok == None:
        return
    blok = blok[rotace]
    for y in range(4):
        for x in range(4):
            if blok[y][x]:
                brain.screen.draw_rectangle((y+y_pos)*velikost_bloku, (10-(x+x_pos))*velikost_bloku, velikost_bloku, velikost_bloku)


while True:
    vykresli_pole()
    vykresli_blok(0,0,0,0)
    brain.screen.render()