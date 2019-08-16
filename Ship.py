#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:43:13 2019

@author: karadowling

Ship Class that holds all information about each Ship in the simulation
"""
from OffensiveMissile import OffensiveMissile
from DefensiveMissile import DefensiveMissile

class Ship():
    
    #initialize Ship object
    def __init__(self, shipName, loc, offensiveMissileTotal, defensiveMissileTotal, 
                 shipSpeed, missileSpeed, timeStep, missileRange, offHitProb, 
                 defHitProbP1, defHitProbP2, defHitProbP3):
        #name of ship
        self.name = shipName
        self.hit = False #whether ship hit by missile
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
        #offensive missile success probability
        self.offHitProb = offHitProb
        #probability of success of missile when reached target 
        #depending on target offensive missile's phase of flight
        #Phase 1 (300-100 NM from ship)
        self.defHitProbP1 = defHitProbP1
        #Phase 2 (100-20 NM from ship)
        self.defHitProbP2 = defHitProbP2
        #Phase 3 (20-0 NM from ship)
        self.defHitProbP3 = defHitProbP3
        #Missiles Lists
        #initialize empty lists with size of arsenals
        #list of offensive missiles fired by particular ship
        self.offensiveMissileList = [OffensiveMissile(loc, None, missileSpeed, offHitProb) for i in range(self.offensiveMissileTotal)]
        #list of defensive missiles fired by particular ship
        self.defensiveMissileList = [DefensiveMissile(loc, None, missileSpeed, defHitProbP1, defHitProbP2, defHitProbP3) for i in range(self.defensiveMissileTotal)]

   
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
        print('')
  
    #calls function in missile classes to move each missile that is flying
    def moveAllMissiles(self):
        for missile in self.offensiveMissileList:
            missile.moveMissile(self.timeStep, self.loc)
        for missile in self.defensiveMissileList:
            missile.moveMissile(self.timeStep, self.loc)
    
    #determine if ships should be moved
    #current policy is to move ships closer if they are out of range and do nothing otherwise
    def moveShip(self, otherShip, animationFile, simulationTime):
        if (abs(self.loc - otherShip.loc) > self.missileRange):
            directionalVelocity = (otherShip.loc - self.loc)/abs(otherShip.loc - self.loc) 
            self.loc = self.loc + directionalVelocity * self.shipSpeed * (1/60) * self.timeStep
        animationFile.write(str(simulationTime) + " " + str(self.loc) + " " + self.name + " ship " + str(False) + "\n")
           
    #determine if should shoot at opposing ship
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
                
    #called by findShipTargets when wanting to launch an offensive missile            
    def launchOffensiveMissile(self, otherShip):
        #can only launch missile if there are missiles left to be fired
        if (self.offensiveMissileTotal - self.omf > 0):
            self.offensiveMissileList[self.omf].launchMissile(otherShip)
            self.omf = self.omf + 1
                
    #determine if should shoot at incoming missiles (if there are any)                
    def findMissileTargets(self, otherShip):       
        #go through all incoming offensive missiles
        for incomingMissile in otherShip.offensiveMissileList:
            shootCount = 0
            if(incomingMissile.flying and (abs(incomingMissile.loc - self.loc) <= 2 * self.missileRange)):
                for defensiveMissile in self.defensiveMissileList:
                    if(defensiveMissile.flying):
                        if(incomingMissile == defensiveMissile.target):
                            shootCount = shootCount + 1
                currentHitProb = 0
                if(abs(incomingMissile.loc - incomingMissile.target.loc) < 20):
                    currentHitProb = self.defHitProbP3
                elif(abs(incomingMissile.loc - incomingMissile.target.loc) < 100):
                   currentHitProb = self.defHitProbP2
                else:
                    currentHitProb = self.defHitProbP1
                
                if(shootCount < int(1/currentHitProb)):
                    self.launchDefensiveMissile(incomingMissile)
                    #print(shootCount)
     
    #called by findMissileTargets when wanting to launch a defensive missile               
    def launchDefensiveMissile(self, targetMissile):
        #can only launch missile if there are missiles left to be fired
        if(self.defensiveMissileTotal - self.dmf > 0):
            self.defensiveMissileList[self.dmf].launchMissile(targetMissile)
            self.dmf = self.dmf + 1
    
    #check all missiles to determine if they've hit their targets
    def checkHitTargets(self, animationFile, simulationTime):
        for missile in self.offensiveMissileList:
            #missile.checkHitTarget()
            animationFile.write(str(simulationTime) + " " + str(missile.loc) + " " + self.name + " offensive " + str(missile.checkHitTarget()) + "\n")
        for missile in self.defensiveMissileList:
            #missile.checkHitTarget()
            animationFile.write(str(simulationTime) + " " + str(missile.loc) + " " + self.name + " defensive " + str(missile.checkHitTarget()) + "\n")     
    
    #determine if the ship is out of all missiles
    #returns True if no missiles left, false otherwise        
    def outOfMissiles(self):
        if(self.offensiveMissileTotal - self.omf <= 0 and self.defensiveMissileTotal - self.dmf <= 0):
            return True
        else:
            return False
            