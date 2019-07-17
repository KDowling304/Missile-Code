#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:58:51 2019

@author: karadowling
"""

class Missile():
  def __init__(self, typeMissile, oloc, target, probHit, timeDest):
    self.typeMissile = typeMissile #Offensive or Defensive
    self.cloc = oloc #origin of missile on 1D scale
    self.target = target #target missile or ship
    #probability that missile will hit intended target if unimpeded
    self.probHit = probHit 
    self.timeDest = timeDest
   
  #print current information about instance of Ship
  def printMissile(self):
    print(self.typeMissile + " missile:")
    print("Current location of missile: " + str(self.oloc) + " on the 1D scale")
    print("Missile target: " + str(self.dloc) + " on the 1D scale")
    print("Probability of success of missile: " + str(self.probHit))
    print("Time until missile reachest destination: " + str(self.timeDest))
    print('')
    
#test = Missile("Offensive", 0, 20, .6)
#test.printMissile()