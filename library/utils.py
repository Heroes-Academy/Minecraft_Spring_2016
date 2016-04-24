"""
A collection of general utilities 
"""

import math

def taxicab_circle_y(r):
    point_set = set()
    y = 0
    for angle in range(360):
        theta = math.radians(angle)
        x = r*math.sin(theta)
        z = r*math.cos(theta)
        if (x,y, z) not in point_set:
            point_set.add((x, y, z))
    return point_set

def taxicab_circle_x(r):
    point_set = set()
    x = 0
    for angle in range(360):
        theta = math.radians(angle)
        y = r*math.sin(theta)
        z = r*math.cos(theta)
        if (x,y, z) not in point_set:
            point_set.add((x, y, z))
    return point_set

def set_points(point_set, mc, block_num):
    for point in point_set:
        x,y,z = point
        mc.setBlock(x, y, z, block_num)

def translate_points(point_set, xdiff, ydiff, zdiff):
    new_point_set = set()
    for point in point_set:
        x,y,z = point
        new_point = (x+xdiff, y+ydiff, z+zdiff)
        new_point_set.add(new_point)
    return new_point_set

def rotate_x(point, theta):
    x,y,z = point
    nx = x
    ny = y*math.cos(theta) + z*math.sin(theta)
    nz = -y*math.sin(theta) + z*math.cos(theta)
    return nx,ny,nz

def rotate_y(point, theta):
    x,y,z = point
    nx = x * math.cos(theta) + z*math.sin(theta)
    ny = y
    nz = -x * math.sin(theta)+z*math.cos(theta)
    return nx,ny,nz

def rotate_z(point, theta):
    x,y,z, = point
    nx = x*math.cos(theta) + y*math.sin(theta)
    ny = -x*math.sin(theta) + y*math.cos(theta)
    nz = z
    return nx,ny,nz


def rotate_points(point_set, angle, axis='x'):
    # note: this is not working.
    # http://www.bioinfo.rpi.edu/~bystrc/courses/biol4550/lecture3/sld005.htm
    theta = math.radians(angle)
    new_point_set = set()
    for point in point_set:
        if axis == 'x':
            new_point = rotate_x(point, theta)
        elif axis == 'y':
            new_point = rotate_y(point, theta)
        elif axis == 'z':
            new_point = rotate_z(point, theta)
        else:
            raise Exception("bad axis!")
        #print(theta, point, new_point, math.cos(theta), math.sin(theta))
        new_point_set.add(new_point)
    return new_point_set