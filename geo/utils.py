# geo/utils.py

import math

def pythagoras(a, b):
    """
    a와 b 길이를 입력받아 빗변 c의 길이를 계산하여 반환합니다.
    """
    c = math.sqrt(a**2 + b**2)
    return c

def circle(r):
    """
    반지름 r을 입력받아 원의 넓이를 계산하여 반환합니다.
    """
    area = math.pi * r**2
    return area

