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
        #direction of missile flight
        self.directionalVelocity = (self.target.loc - self.loc)/abs(self.target.loc - self.loc) 
        #is the missile still flying
        #false if reached destination already or if has been hit 
        self.flying = True
        #missile speed when flying
        self.missileSpeed = missileSpeed
        
    #moves particular missile the specified distance per timeStep
    def moveMissile(self, timeStep):
        if(self.flying == True):
            self.loc = self.loc + self.directionalVelocity * self.missileSpeed * (1/60) * self.timeStep
        
        
    #print current information about instance of Ship
    def printMissile(self):
        print("Current location of missile: " + str(self.loc) + " on the 1D scale")
        print("Missile target: " + str(self.dloc) + " on the 1D scale")
        print("Missile still flying: " + str(self.flying))
        print('')
    