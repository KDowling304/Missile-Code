#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:58:51 2019

@author: karadowling

Defensive Missile Class for each defensive missile for both Red and Blue Ships
"""

import random

class DefensiveMissile():
    
   #initialize a single Defensive Missile 
   def __init__(self, loc, target, missileSpeed, defHitProbP1, defHitProbP2, defHitProbP3):
       self.loc = loc #location of missile on 1D scale
       self.target = target #target missile
       #is the missile flying
       #false if reached destination already or if has been hit 
       self.flying = False
       #missile speed when flying
       self.missileSpeed = missileSpeed
       #direction of missile flight
       self.directionalVelocity = None
       #probability of success of missile when reached target 
       #depending on target offensive missile's phase of flight
       #Phase 1 (300-100 NM from ship)
       self.defHitProbP1 = defHitProbP1
       #Phase 2 (100-20 NM from ship)
       self.defHitProbP2 = defHitProbP2
       #Phase 3 (20-0 NM from ship)
       self.defHitProbP3 = defHitProbP3
       
   #print current information about instance of a Defensive Missile
   def printMissile(self):
       print("Current location of missile: " + str(self.loc) + " on the 1D scale")
       print("Missile target: " + str(self.dloc) + " on the 1D scale")
       print("Missile still flying: " + str(self.flying))
       print('')
       
   #moves particular missile the specified distance per timeStep
   def moveMissile(self, timeStep, shipLoc):
       if(self.flying == True):
           self.loc = self.loc + self.directionalVelocity * self.missileSpeed * (1/60) * timeStep
       if(self.flying == False and self.target == None):
            self.loc = shipLoc
   
   #updates target parameter of the missile
   def setTarget(self, target):
       self.target = target
       #direction of missile flight
       if self.target != None:
           self.directionalVelocity = (self.target.loc - self.loc)/abs(self.target.loc - self.loc) 
   
   #updates flying status of the missile     
   def setFlyingStatus(self, flyingStatus):
       self.flying = flyingStatus
       
   #launches missile which means giving a missile a target and setting it to flying
   def launchMissile(self, target):
       self.setTarget(target)
       self.setFlyingStatus(True)
   
   #checks if the missile hit its target each iteration
   def checkHitTarget(self):
       if(self.flying):
           currentDirectionalVelocity = (self.target.loc - self.loc)/abs(self.target.loc - self.loc) 
           #if the missile has passed or is at its target ship in the current timeStep
           if(self.directionalVelocity/currentDirectionalVelocity == -1):
               self.setFlyingStatus(False) #missile no longer flying
               #use random number generator to determine 
               #if the missile was a success at its target
               randomHit = random.random()
               #print(randomHit)
               #determine which probability to use for effectiveness of defensive missile
               #determined based on how close the offensive missile is to its target
               #offensive missile changes flight path based off this
               currentHitProb = 0
               if(abs(self.target.loc - self.target.target.loc) < 20):
                   currentHitProb = self.defHitProbP3
               elif(abs(self.target.loc - self.target.target.loc) < 100):
                   currentHitProb = self.defHitProbP2
               else:
                   currentHitProb = self.defHitProbP1
               if(self.target.flying and randomHit <= currentHitProb):
                   self.target.setFlyingStatus(False)  
                   return True
       return False
     
