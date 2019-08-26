#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:51:24 2019

@author: karadowling

CIWS Class for both Red and Blue Ships
A 30mm gun that fires about 3000 rounds each time it is used
A Point Defense System
Used when incoming offensive missile is 1-0 NM from its target
Method of last defense
"""

import random

class CIWS():
    
   #initialize a single Defensive Missile 
   def __init__(self, loc, target, bulletSpeed, ciwsHitProb):
       self.loc = loc #location of missile on 1D scale
       self.target = target #target missile
       #is the missile flying
       #false if reached destination already or if has been hit 
       self.flying = False
       #nullet speed when flying
       self.bulletSpeed = bulletSpeed
       #direction of missile flight
       self.directionalVelocity = None
       #CIWS success probability
       self.HitProb = ciwsHitProb
       
   #print current information about instance of a Defensive Missile
   def printMissile(self):
       print("Current location of missile: " + str(self.loc) + " on the 1D scale")
       print("Missile target: " + str(self.dloc) + " on the 1D scale")
       print("Missile still flying: " + str(self.flying))
       print('')
       
   #moves particular missile the specified distance per timeStep
   def moveCIWS(self, timeStep, shipLoc):
       if(self.flying == True):
           self.loc = self.loc + self.directionalVelocity * self.bulletSpeed * (1/60) * timeStep
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
       
   #fires one set of 3000 bullet rounds
   #which means giving CIWS a target and setting it to flying
   def fireBulletRounds(self, target):
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
     