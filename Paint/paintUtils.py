import math

def distanceBetween(x1 , y1 , x2, y2):
   print(x1 , x2)
   return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))


def angleBetween(x1 , y1 , x2, y2):
  return math.atan2( x1 - x2, y1 - y2)