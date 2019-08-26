#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:51:24 2019

@author: karadowling

Sea RAM (Rolling Air Frame Missile) Class for both Red and Blue Ships
A Point Defense System
Used when incoming offensive missile is 3-1 NM from its target
Shoot-Shoot doctrine 
"""

import random

class SeaRAM():
    
   #initialize a single Defensive Missile 
   def __init__(self, loc, target, missileSpeed, seaRamHitProb):
       self.loc = loc #location of missile on 1D scale
       self.target = target #target missile
       #is the missile flying
       #false if reached destination already or if has been hit 
       self.flying = False
       #missile speed when flying
       self.missileSpeed = missileSpeed
       #direction of missile flight
       self.directionalVelocity = None
       #Sea RAM success probability
       self.HitProb = seaRamHitProb
       
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
               if(self.target.flying and randomHit <= self.HitProb):
                   self.target.setFlyingStatus(False)  
                   return True
       return False
     