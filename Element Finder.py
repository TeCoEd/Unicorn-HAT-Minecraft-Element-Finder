  #!/usr/bin/env python

import unicornhat as UH
import time
import sys
from mcpi import minecraft
mc = minecraft.Minecraft.create()

UH.brightness(0.10)

def water():
  for y in range(8):
    for x in range(8):
      UH.set_pixel(x,y, 0, 0, 255)
      UH.show()
      time.sleep(0.02)

def air():
  for y in range(8):
    for x in range(8):
      UH.set_pixel(x,y, 0, 0, 0)
      UH.show()
      time.sleep(0.02)

def TNT():
  for y in range(8):
    for x in range(8):
      UH.set_pixel(x,y, 255, 0, 100)
      UH.show()
      time.sleep(0.02)


def dirt():
  for y in range(8):
    for x in range(8):
      UH.set_pixel(x,y, 0, 255, 0)
      UH.show()
      time.sleep(0.02)

def sand():
  for y in range(8):
    for x in range(8):
      UH.set_pixel(x,y, 148, 0, 211)
      UH.show()
      time.sleep(0.02)

      

while True:
  x,y,z = mc.player.getPos()

  blockID =  mc.getBlock(x, y-1, z)
  print blockID

  time.sleep(0.1)

  if blockID == 9:
      water()
  elif blockID == 0:
      air()
  elif blockID == 2:
      dirt()
  elif blockID ==12:
      sand()
   
       
