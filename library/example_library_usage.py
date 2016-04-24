"""
Title:
Goal:
Author:
Date:
"""
from utils import taxicab_circle_x, taxicab_circle_y, set_points, translate_points, rotate_points
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

def tunnel_y(height, size, pos=None):
    if pos is None:
        pos = mc.player.getPos()
    x,y,z = pos
    points = taxicab_circle_y(size)
    for i in range(height):
        new_points = translate_points(points, x, y+i, z)
        set_points(new_points, mc, 17)

def tunnel_x(length, size, pos=None):
    if pos is None:
        pos = mc.player.getPos()
    x,y,z = pos
    points = taxicab_circle_x(size)
    for i in range(length):
        new_points = translate_points(points, x+i, y, z)
        set_points(new_points, mc, 17)


def tree():
    p = mc.player
    pos = p.getPos()
    tunnel_y(35, 10, pos)
    x,y,z = pos
    for h in range(5,35,5):
        sidepos = (x+6, y+h, z)
        tunnel_x(10, 3, sidepos)

        sidepos = (x-13, y+h, z)
        tunnel_x(10, 3, sidepos)


tree()