from rpi_ws281x import Adafruit_NeoPixel, Color
from time import sleep
from datetime import datetime
import math
from random import randint

panel = Adafruit_NeoPixel(64, 18, 800000, 5, False, 50)

panel.begin()

color = Color(255,255,100)


def mfive():
  panel.setPixelColor(16,color)
  panel.setPixelColor(17,color)
  panel.setPixelColor(18,color)
  panel.setPixelColor(19,color)

def mten():
  panel.setPixelColor(1,color)
  panel.setPixelColor(3,color)
  panel.setPixelColor(4,color)

def quarter():
  panel.setPixelColor(8,color)
  panel.setPixelColor(9,color)
  panel.setPixelColor(10,color)
  panel.setPixelColor(11,color)
  panel.setPixelColor(12,color)
  panel.setPixelColor(13,color)
  panel.setPixelColor(14,color)

def twenty():
  panel.setPixelColor(1,color)
  panel.setPixelColor(2,color)
  panel.setPixelColor(3,color)
  panel.setPixelColor(4,color)
  panel.setPixelColor(5,color)
  panel.setPixelColor(6,color)

def half():
  panel.setPixelColor(20,color)
  panel.setPixelColor(21,color)
  panel.setPixelColor(22,color)
  panel.setPixelColor(23,color)

def past():
  panel.setPixelColor(25,color)
  panel.setPixelColor(26,color)
  panel.setPixelColor(27,color)
  panel.setPixelColor(28,color)

def to():
  panel.setPixelColor(28,color)
  panel.setPixelColor(29,color)



def one():
  panel.setPixelColor(57,color)
  panel.setPixelColor(60,color)
  panel.setPixelColor(63,color)

def two():
  panel.setPixelColor(48,color)
  panel.setPixelColor(49,color)
  panel.setPixelColor(57,color)

def three():
  panel.setPixelColor(43,color)
  panel.setPixelColor(44,color)
  panel.setPixelColor(45,color)
  panel.setPixelColor(46,color)
  panel.setPixelColor(47,color)

def four():
  panel.setPixelColor(56,color)
  panel.setPixelColor(57,color)
  panel.setPixelColor(58,color)
  panel.setPixelColor(59,color)

def five():
  panel.setPixelColor(32,color)
  panel.setPixelColor(33,color)
  panel.setPixelColor(34,color)
  panel.setPixelColor(35,color)

def six():
  panel.setPixelColor(40,color)
  panel.setPixelColor(41,color)
  panel.setPixelColor(42,color)

def seven():
  panel.setPixelColor(40,color)
  panel.setPixelColor(52,color)
  panel.setPixelColor(53,color)
  panel.setPixelColor(54,color)
  panel.setPixelColor(55,color)

def eight():
  panel.setPixelColor(35,color)
  panel.setPixelColor(36,color)
  panel.setPixelColor(37,color)
  panel.setPixelColor(38,color)
  panel.setPixelColor(39,color)

def nine():
  panel.setPixelColor(60,color)
  panel.setPixelColor(61,color)
  panel.setPixelColor(62,color)
  panel.setPixelColor(63,color)

def ten():
  panel.setPixelColor(39,color)
  panel.setPixelColor(47,color)
  panel.setPixelColor(55,color)

def eleven():
  panel.setPixelColor(50,color)
  panel.setPixelColor(51,color)
  panel.setPixelColor(52,color)
  panel.setPixelColor(53,color)
  panel.setPixelColor(54,color)
  panel.setPixelColor(55,color)

def twelve():
  panel.setPixelColor(48,color)
  panel.setPixelColor(49,color)
  panel.setPixelColor(50,color)
  panel.setPixelColor(51,color)
  panel.setPixelColor(53,color)
  panel.setPixelColor(54,color)

def update():
  panel.show()

def clear():
  for i in range(0,64):
    panel.setPixelColor(i,Color(0,0,0))



r = 0
g = 60
b = 200
rinc = 1
ginc = 1
binc = 1



while True:
  time = datetime.now().time()
  hour,min,sec = str(time).split(":")
  hour = int(hour)
  min = int(min)

#  min = 34

  clear()

  if r >= 250:
    rinc = 0
  if r <= 5:
    rinc = 1
  if rinc == 1:
    r += randint(0,5)
  else:
    r -= randint(0,5)

  if g >= 250:
    ginc = 0
  if g <= 5:
    ginc = 1
  if ginc == 1:
    g += randint(0,5)
  else:
    g -= randint(0,5)

  if b >= 250:
    binc = 0
  if b <= 5:
    binc = 1
  if binc == 1:
    b += randint(0,5)
  else:
    b -= randint(0,5)

  color = Color(g,r,b)

  if 3 <= min <= 7:
    mfive()
    past()

  if 8 <= min <= 12:
    mten()
    past()

  if 13 <= min <= 17:
    quarter()
    past()

  if 18 <= min <= 22:
    twenty()
    past()

  if 23 <= min <= 27:
    twenty()
    mfive()
    past()

  if 28 <= min <= 32:
    half()
    past()

  if 33 <= min <= 37:
    twenty()
    mfive()
    to()

  if 38 <= min <= 42:
    twenty()
    to()

  if 43 <= min <= 47:
    quarter()
    to()

  if 48 <= min <= 52:
    mten()
    to()

  if 53 <= min <= 57:
    mfive()
    to()


  if min > 32:
    hour = hour + 1



  if hour == 1 or hour == 13:
    one()
  if hour == 2 or hour == 14:
    two()
  if hour == 3 or hour == 15:
    three()
  if hour == 4 or hour == 16:
    four()
  if hour == 5 or hour == 17:
    five()
  if hour == 6 or hour == 18:
    six()
  if hour == 7 or hour == 19:
    seven()
  if hour == 8 or hour == 20:
    eight()
  if hour == 9 or hour == 21:
    nine()
  if hour == 10 or hour == 22:
    ten()
  if hour == 11 or hour == 23:
    eleven()
  if hour == 12 or hour == 0 or hour == 24:
    twelve()

  update()
  sleep(0.5)
