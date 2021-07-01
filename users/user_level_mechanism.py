from enum import Enum

class Level(Enum):
    level_1 = 100
    level_2 = 150
    level_3 = 200
    level_4 = 250
    level_5 = 300
    level_6 = 350
    level_7 = 400
    level_8 = 450
    level_9 = 500
    level_10 = 550
    level_11 = 650
    level_12 = 750
    level_13 = 850
    level_14 = 950
    level_15 = 1050
    level_16 = 1250
    level_17 = 1450
    level_18 = 1650
    level_19 = 1850
    level_20 = 2050
    level_21 = 2550
    level_22 = 3050
    level_23 = 3550
    level_24 = 4050
    level_25 = 5000


def is_increase_user_level(exp):
    for lvl in Level:
        if lvl.value == exp:
            return True
        else:
            return False   