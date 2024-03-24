# Program settings
import math
import tkinter
root = tkinter.Tk()
HEIGHT = root.winfo_screenheight()
WIDTH = root.winfo_screenwidth()
# HEIGHT = 800
# WIDTH = 1200
RIGHT_ANGLE = 1.57079632679


# Player settings
player_pos = (WIDTH // 2, HEIGHT // 2)
player_angle = -1.57079632679
player_speed = 2
TILE_WIDTH = WIDTH // 12
# TILE_HEIGHT = HEIGHT // 8
TILE_HEIGHT = WIDTH // 12


# settings of rays
FOV = math.pi / 3   # область видимости
NUM_RAYS = 340  # количество испускаемых лучей
MAX_DEPTH = HEIGHT  # дальность прорисовки
DELTA_ANGLE = FOV / NUM_RAYS  # угол между лучами
#DIST = NUM_RAYS / (2 * math.tan(FOV / 2))
DIST = WIDTH // 12
PROJ_COEFF = DIST * TILE_HEIGHT
SCALE = WIDTH // NUM_RAYS