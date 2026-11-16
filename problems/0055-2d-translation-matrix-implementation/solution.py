import numpy as np
def translate_object(points, tx, ty):
    translated_points = []

    for i in range(len(points)):
        translated_points.append([points[i][0]+tx, points[i][1]+ty])
    return translated_points