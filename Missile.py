#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:58:51 2019

@author: karadowling
"""

class Missile():
  def __init__(self, typeMissile, oloc, dloc, probHit, timeDest):
    self.typeMissile = typeMissile #Offensive or Defensive
    self.cloc = oloc #origin of missile on 1D scale
    self.dloc = dloc #destination of missile on 1D scale
    #probability that missile will hit intended target if unimpeded
    self.probHit = probHit 
    self.timeDest = timeHit
   
  #print current information about instance of Ship
  def printMissile(self):
    print(self.typeMissile + " Missile:")
    print("Current location of missile: " + str(self.oloc) + " on the 1D scale")
    print("Destination of missile: " + str(self.dloc) + " on the 1D scale")
    print("Probability of Success of Missile: " + str(self.probHit))
    print("Time until missile reachest destination: " + str(self.timeDest))
    print('')
    
#test = Missile("Offensive", 0, 20, .6)
#test.printMissile()