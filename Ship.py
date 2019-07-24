#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:43:13 2019

@author: karadowling
"""

class Ship():
    def __init__(self, shipName, loc, offensiveMissileTotal, defensiveMissileTotal, shipSpeed, missileSpeed, timeStep, missileRange):
        self.name = shipName
        self.hit = False #ship hit by missile
        #best known location of destroyer in 1D scale (to compare to other ship)
        self.loc = loc 
        self.omf = 0 #offensive missiles already fired (start with 0)
        #offensive missiles left in ship's arsenal (typically start with 20)
        self.oml = offensiveMissileTotal - self.omf 
        self.dmf = 0 #defensive missiles left in ship's arsenal (start with 0)
        #defensive missiles left in ship's arsenal ( typically start with 60)
        self.dml = defensiveMissileTotal - self.dmf 
        #Missiles Lists
        #initialize empty lists with size of arsenals
        #list of offensive missiles fired by particular ship
        self.offensiveMissileList = [None] * self.oml
        #list of defensive missiles fired by particular ship
        self.defensiveMissileList = [None] * self.dml
        #speed of ship when moving
        self.shipSpeed = shipSpeed
        #speed of all missiles when launched
        self.missileSpeed = missileSpeed
        #time step between iterations
        self.timeStep = timeStep
        #range of ship's missiles
        self.missileRange = missileRange
   
    #print current information about instance of Ship
    def printShip(self):
        print(self.name + ":")
        if self.hit == True :
            print("The ship has been hit!!")
        else:
            print("Ship has not been hit")
        print("Current best known location is " + str(self.loc) + " NM on the 1D scale")
        print(str(self.omf) + " offensive missiles already fired")
        print(str(self.oml) + " offensive missiles left in ship's arsenal") 
        print(str(self.dmf) + " defensive missiles already fired")
        print(str(self.dml) + " defensive missiles left in ship's arsenal") 
        print("Ship speed: " + str(self.shipSpeed) + " knots")
        print("Missile speed: " + str(self.missileSpeed) + " knots")
        print("Missile range: " + str(self.missileRange) + " NM")
        print('')
  
    #calls function in missile classes to move each missile that is flying
    def moveAllMissiles(self):
        for missile in self.offensiveMissileList:
            missile.moveMissile(self.timeStep)
        for missile in self.defensiveMissileList:
            missile.moveMissile(self.timeStep)
    
    
    #def findTargets(self, otherShip):
        #if ship is in range, has it been shot at?, decide to shoot again or not
        #if abs(otherShip.loc - self.loc) <= self.missileRange:
            
        
            
    
    
#test = Ship("Test Ship", 0, 20, 60)
#test.printShip()