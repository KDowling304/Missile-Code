#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:43:13 2019

@author: karadowling
"""
from OffensiveMissile import OffensiveMissile
from DefensiveMissile import DefensiveMissile

class Ship():
    def __init__(self, shipName, loc, offensiveMissileTotal, defensiveMissileTotal, 
                 shipSpeed, missileSpeed, timeStep, missileRange, defHitProb):
        self.name = shipName
        self.hit = False #ship hit by missile
        #best known location of destroyer in 1D scale (to compare to other ship)
        self.loc = loc 
        self.omf = 0 #offensive missiles already fired (start with 0)
        #offensive missiles starting in ship's arsenal (typically start with 20)
        self.offensiveMissileTotal =  offensiveMissileTotal
        self.dmf = 0 #defensive missiles left in ship's arsenal (start with 0)
        #defensive missiles starting in ship's arsenal ( typically start with 60)
        self.defensiveMissileTotal = defensiveMissileTotal
        #speed of ship when moving
        self.shipSpeed = shipSpeed
        #speed of all missiles when launched
        self.missileSpeed = missileSpeed
        #time step between iterations
        self.timeStep = timeStep
        #range of ship's missiles
        self.missileRange = missileRange
        #Missiles Lists
        #initialize empty lists with size of arsenals
        #list of offensive missiles fired by particular ship
        self.offensiveMissileList = [None] * self.offensiveMissileTotal
        for missile in self.offensiveMissileList:
            missile = OffensiveMissile(loc, None, missileSpeed)
        #list of defensive missiles fired by particular ship
        self.defensiveMissileList = [None] * self.defensiveMissileTotal
        for missile in self.defensiveMissileList:
            missile = DefensiveMissile(loc, None, missileSpeed)
        #defensive missile success probability
        self.defHitProb = defHitProb
            
   
    #print current information about instance of Ship
    def printShip(self):
        print(self.name + ":")
        if self.hit == True :
            print("The ship has been hit!!")
        else:
            print("Ship has not been hit")
        print("Current best known location is " + str(self.loc) + " NM on the 1D scale")
        print(str(self.omf) + " offensive missiles already fired")
        print(str(self.offensiveMissileTotal - self.omf) + " offensive missiles left in ship's arsenal") 
        print(str(self.dmf) + " defensive missiles already fired")
        print(str(self.defensiveMissileTotal - self.dmf) + " defensive missiles left in ship's arsenal") 
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
    
    
    def findShipTargets(self, otherShip):
        #if ship is in range, has it been shot at?, decide to shoot again or not
        if (abs(otherShip.loc - self.loc) <= self.missileRange):
            shootCount = 0
            for missile in self.offensiveMissileList:
                #only need to check if flying because simulation ends when a ship is hit
                #therefore either the offensive missile was unsuccessful already or hasn't been shot at
                if(missile.flying == True):
                    shootCount = shootCount + 1       
            if(shootCount < 1):
                self.launchOffensiveMissile(otherShip)
                
    def launchOffensiveMissile(self, otherShip):
        self.offensiveMissileList[self.omf].launchMissile(otherShip)
        self.omf = self.omf + 1
                
                    
    def findMissileTargets(self, otherShip):       
        #go through all incoming offensive missiles
        for incomingMissile in otherShip.offensiveMissileList:
            shootCount = 0
            if(incomingMissile.flying and (abs(incomingMissile.loc - self.loc) <= 2 * self.missileRange)):
                for defensiveMissile in self.defensiveMissileList:
                    if(defensiveMissile.flying):
                        if(incomingMissile == defensiveMissile):
                            shootCount = shootCount + 1
                if(shootCount < int(1/self.defHitProb)):
                    self.launchDefensiveMissile(incomingMissile)
                    
    def launchDefensiveMissile(self, targetMissile):
        self.defensiveMissileList[self.dmf].launchMissile(targetMissile)
        self.dmf = self.dmf + 1
                            
        
        
            
    
    
#test = Ship("Test Ship", 0, 20, 60)
#test.printShip()