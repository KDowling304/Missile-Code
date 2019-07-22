#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:58:51 2019

@author: karadowling
"""

class OffensiveMissile():
  def __init__(self, oloc, target, probHit, timeDest):
    self.cloc = oloc #origin of missile on 1D scale
    self.target = target #target ship (Red Ship or Blue Ship)
    #probability that missile will hit intended target if unimpeded
    self.probHit = probHit 
    self.timeDest = timeDest
   
  #print current information about instance of Ship
  def printMissile(self):
    print("Current location of missile: " + str(self.oloc) + " on the 1D scale")
    print("Missile target: " + str(self.dloc) + " on the 1D scale")
    print("Probability of success of missile: " + str(self.probHit))
    print("Time until missile reachest destination: " + str(self.timeDest))
    print('')
    