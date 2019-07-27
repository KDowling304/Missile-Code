#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:58:51 2019

@author: karadowling
"""

class OffensiveMissile():
    
    def __init__(self, loc, target, missileSpeed):
        self.loc = loc #location of missile on 1D scale
        self.target = target #target ship (Red Ship or Blue Ship)
        #is the missile flying
        #false if reached destination already or if has been hit 
        self.flying = False
        #missile speed when flying
        self.missileSpeed = missileSpeed
        #direction of missile flight
        self.directionalVelocity = None

        
    #moves particular missile the specified distance per timeStep
    def moveMissile(self, timeStep):
        if(self.flying == True):
            self.loc = self.loc + self.directionalVelocity * self.missileSpeed * (1/60) * timeStep
      
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
     
    #print current information about instance of Ship
    def printMissile(self):
        print("Current location of missile: " + str(self.loc) + " on the 1D scale")
        print("Missile target: " + str(self.dloc) + " on the 1D scale")
        print("Missile still flying: " + str(self.flying))
        print('')
    