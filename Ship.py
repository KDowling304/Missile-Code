#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:43:13 2019

@author: karadowling

Ship Class that holds all information about each Ship in the simulation
"""
from OffensiveMissile import OffensiveMissile
from DefensiveMissile import DefensiveMissile
from ESSM import ESSM
from SeaRAM import SeaRAM
from CIWS import CIWS
import random
from texttable import Texttable

class Ship():
    
    #initialize Ship object
    def __init__(self, shipName, loc, offensiveMissileTotal, defensiveMissileTotal, 
                 essmTotal, seaRamTotal, ciwsTotal, 
                 shipSpeed, missileSpeed, timeStep, offensiveMissileRange, offHitProb, 
                 defHitProbP1, defHitProbP2, defHitProbP3, 
                 essmHitProb, seaRamHitProb, ciwsHitProb,
                 offensiveMissileSS, defensiveMissileSS, essmSS, seaRamSS, ciwsSS,
                 satellite, radar, electronicSurveillance, passiveSensors, 
                 uav, usv):
        #name of ship
        self.name = shipName
        self.hit = False #whether ship hit by missile
        #best known location of destroyer in 1D scale (to compare to other ship)
        self.loc = loc 
        self.omf = 0 #offensive missiles already fired (start with 0)
        #offensive missiles starting in ship's arsenal (typically start with 20)
        self.offensiveMissileTotal =  offensiveMissileTotal
        self.dmf = 0 #defensive missiles left in ship's arsenal (start with 0)
        #defensive missiles starting in ship's arsenal (typically start with 60)
        self.defensiveMissileTotal = defensiveMissileTotal
        #Point Defense System
        #Extended NATO SeaSparrow Missiles (ESSM) starting in ship's arsenal (typically 32)
        self.essmTotal = essmTotal
        self.essmf = 0 #ESSMs fired (start with 0)
        #Sea RAMs (Rolling Air Frame Missile) starting in ship's arsenal (typically 20)
        self.seaRamTotal = seaRamTotal
        self.seaRamf = 0 #Sea RAMs fired (start with 0)
        #CIWS - 30mm gun fires about 3000 rounds each time we use it 
        #(typically start with 3 times)
        self.ciwsTotal = ciwsTotal
        self.ciwsf = 0 #times we decide to fire CIWS (start with 0) 
        #speed of ship when moving
        self.shipSpeed = shipSpeed
        #speed of all missiles when launched
        self.missileSpeed = missileSpeed
        #time step between iterations
        self.timeStep = timeStep
        #range of ship's missiles
        self.offensiveMissileRange = offensiveMissileRange
        #Don't need all of these because they are saved as a part of each missile
        #offensive missile success probability
        self.offHitProb = offHitProb
        #probability of success of missile when reached target 
        #depending on target offensive missile's phase of flight
        #Phase 1 (100-20 NM from ship)
        self.defHitProbP1 = defHitProbP1
        #Phase 2 (20-5 NM from ship)
        self.defHitProbP2 = defHitProbP2
        #Phase 3 (5-0 NM from ship)
        self.defHitProbP3 = defHitProbP3
        #ESSM success probability
        self.essmHitProb = essmHitProb
        #Sea RAM success probability
        self.seaRamHitProb = seaRamHitProb
        #CIWS success probability
        self.ciwsHitProb = ciwsHitProb
        #Missiles Lists
        #initialize lists with size of arsenals
        #list of offensive missiles on/fired by particular ship
        self.offensiveMissileList = [OffensiveMissile(loc, None, missileSpeed, offHitProb) for i in range(self.offensiveMissileTotal)]
        #list of defensive missiles on/fired by particular ship
        self.defensiveMissileList = [DefensiveMissile(loc, None, missileSpeed, defHitProbP1, defHitProbP2, defHitProbP3) for i in range(self.defensiveMissileTotal)]
        #list of ESSMs on/fired by particular ship
        self.essmList = [ESSM(loc, None, missileSpeed, essmHitProb) for i in range(self.essmTotal)]
        #list of SeaRAMs on/fired by particular ship
        self.seaRamList = [SeaRAM(loc, None, missileSpeed, seaRamHitProb) for i in range(self.seaRamTotal)]
        #list of CIWS groups of 3000 rounds on/fired by particular ship
        self.ciwsList = [CIWS(loc, None, missileSpeed, ciwsHitProb) for i in range(self.ciwsTotal)]
        #scouting variables
        #each comment corresponds with true value
        #communicating with satellite
        self.offensiveMissileSS = offensiveMissileSS
        self.defensiveMissileSS = defensiveMissileSS
        self.essmSS = essmSS
        self.seaRamSS = seaRamSS
        self.ciwsSS = ciwsSS
        self.satellite = bool(satellite)
        #active radar on
        self.radar = bool(radar)
        #electronic surveillance equipment turned on
        self.electronicSurveillance = bool(electronicSurveillance)
        #passive acoustic sensors on
        self.passiveSensors = bool(passiveSensors)
        #Unmanned Aerial Vehicle (UAV) deployed
        self.uav = bool(uav)
        #Unmanned Surface Vehicle (USV) deployed
        self.usv = bool(usv)

    #print ship inputs when they are changing in code
    def printShipInputs(self, otherShip):
        t = Texttable()
        #t.add_rows([['Name', 'Age'], ['Alice', 24], ['Bob', 19]])
        if(self.satellite == 1):
            selfSatellite = 'TRUE'
        else:
            selfSatellite = 'FALSE'
        if(self.radar == 1):
            selfRadar = 'TRUE'
        else:
            selfRadar = 'FALSE'
        if(self.electronicSurveillance == 1):
            selfElectronicSurveillance = 'TRUE'
        else:
            selfElectronicSurveillance = 'FALSE'
        if(self.passiveSensors == 1):
            selfPassiveSensors = 'TRUE'
        else:
            selfPassiveSensors = 'FALSE'
        if(self.uav == 1):
            selfUav = 'TRUE'
        else:
            selfUav = 'FALSE'
        if(self.usv == 1):
            selfUsv = 'TRUE'
        else:
            selfUsv = 'FALSE'
            
        if(otherShip.satellite == 1):
            otherShipSatellite = 'TRUE'
        else:
            otherShipSatellite = 'FALSE'
        if(otherShip.radar == 1):
            otherShipRadar = 'TRUE'
        else:
            otherShipRadar = 'FALSE'
        if(otherShip.electronicSurveillance == 1):
            otherShipElectronicSurveillance = 'TRUE'
        else:
            otherShipElectronicSurveillance = 'FALSE'
        if(otherShip.passiveSensors == 1):
            otherShipPassiveSensors = 'TRUE'
        else:
            otherShipPassiveSensors = 'FALSE'
        if(otherShip.uav == 1):
            otherShipUav = 'TRUE'
        else:
            otherShipUav = 'FALSE'
        if(otherShip.usv == 1):
            otherShipUsv = 'TRUE'
        else:
            otherShipUsv = 'FALSE'

        
        t.add_rows([['', self.name, otherShip.name], 
                    ['Starting Location (NM) 1D Scale', self.loc, otherShip.loc], 
                    ['Ship Speed (kn)', self.shipSpeed, otherShip.shipSpeed],
                    ['Missile Speed (kn)', self.missileSpeed, otherShip.missileSpeed],
                    ['Offensive Missile Inventory', self.offensiveMissileTotal, otherShip.offensiveMissileTotal],
                    ['Offensive Missile Range (NM)', self.offensiveMissileRange, otherShip.offensiveMissileRange],
                    ['Offensive Missile Success Probability', self.offHitProb, otherShip.offHitProb],
                    ['Offensive Missile Salvo Size', self.offensiveMissileSS, otherShip.offensiveMissileSS],
                    ['Defensive Missile Inventory', self.defensiveMissileTotal, otherShip.defensiveMissileTotal],
                    ['Defensive Missile Success Probability\n(if target offensive missile is\n100-20 NM from its target - phase 1)', self.defHitProbP1, otherShip.defHitProbP1],
                    ['Defensive Missile Success Probability\n(if target offensive missile is\n20-5 NM from its target - phase 2)', self.defHitProbP2, otherShip.defHitProbP2],
                    ['Defensive Missile Success Probability\n(if target offensive missile is\n5-1 NM from its target - phase 3)', self.defHitProbP3, otherShip.defHitProbP3],
                    ['Defensive Missile Salvo Size', self.defensiveMissileSS, otherShip.defensiveMissileSS],
                    ['ESSM Inventory', self.essmTotal, otherShip.essmTotal],
                    ['ESSM Success Probability', self.essmHitProb, otherShip.essmHitProb],
                    ['ESSM Salvo Size', self.essmSS, otherShip.essmSS],
                    ['Sea RAM Inventory', self.seaRamTotal, otherShip.seaRamTotal],
                    ['Sea RAM Success Probability', self.seaRamHitProb, otherShip.seaRamHitProb],
                    ['Sea RAM Salvo Size', self.seaRamSS, otherShip.seaRamSS],
                    ['CIWS Inventory (1500 rounds each)', self.ciwsTotal, otherShip.ciwsTotal],
                    ['CIWS Iteration Success Probability', self.ciwsHitProb, otherShip.ciwsHitProb],
                    ['CIWS Iteration Salvo Size', self.ciwsSS, otherShip.ciwsSS],
                    ['Satellite', selfSatellite, otherShipSatellite],
                    ['Radar', selfRadar, otherShipRadar],
                    ['Electronic Surveillance', selfElectronicSurveillance, otherShipElectronicSurveillance],
                    ['Passive Sensors', selfPassiveSensors, otherShipPassiveSensors],
                    ['Unmanned Aerial Vehicle (UAV)', selfUav, otherShipUav],
                    ['Unmanned Surface Vehicle (USV)', selfUsv, otherShipUsv]])
        print(t.draw())
        print()
        

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
        print(str(self.essmf) + " ESSMs already fired")
        print(str(self.essmTotal - self.essmf) + " ESSMs left in ship's arsenal") 
        print(str(self.seaRamf) + " Sea RAMs already fired")
        print(str(self.seaRamTotal - self.seaRamf) + " Sea RAMs left in ship's arsenal") 
        print(str(self.ciwsf) + " sets of 3000 CIWS bullets already fired")
        print(str(self.ciwsTotal - self.ciwsf) + " sets of 3000 CIWS bullets left in ship's arsenal") 
        print("Current cost of engagement: $" + f"{self.engagementCost():,d}")
        print('')
  
    #calls function in missile classes to move each missile that is flying
    def moveAllMissiles(self):
        for missile in self.offensiveMissileList:
            missile.moveMissile(self.timeStep, self.loc)
        for missile in self.defensiveMissileList:
            missile.moveMissile(self.timeStep, self.loc)
        for missile in self.essmList:
            missile.moveMissile(self.timeStep, self.loc)
        for missile in self.seaRamList:
            missile.moveMissile(self.timeStep, self.loc)
        for bulletRound in self.ciwsList:
            bulletRound.moveCIWS(self.timeStep, self.loc)
    
    #determine if ships should be moved
    #current policy is to move ships closer if they are out of range and do nothing otherwise
    def moveShip(self, otherShip, animationFile, simulationTime):
        '''if (abs(self.loc - otherShip.loc) > self.offensiveMissileRange):
            directionalVelocity = (otherShip.loc - self.loc)/abs(otherShip.loc - self.loc) 
            self.loc = self.loc + directionalVelocity * self.shipSpeed * (1/60) * self.timeStep'''
        if(self.offensiveMissileTotal - self.omf <= 0):
            directionalVelocity = -1*((otherShip.loc - self.loc)/abs(otherShip.loc - self.loc))
            self.loc = self.loc + directionalVelocity * self.shipSpeed * (1/60) * self.timeStep    
            animationFile.write(str(simulationTime) + " " + str(self.loc) + " " + self.name + " ship " + str(False) + "\n")
        #move until they get 5 NM from each other 
        elif (abs(self.loc - otherShip.loc) > 5):
            directionalVelocity = (otherShip.loc - self.loc)/abs(otherShip.loc - self.loc) 
            self.loc = self.loc + directionalVelocity * self.shipSpeed * (1/60) * self.timeStep
            animationFile.write(str(simulationTime) + " " + str(self.loc) + " " + self.name + " ship " + str(False) + "\n")
           
    #determine if should shoot at opposing ship
    def findShipTargets(self, otherShip):
        #distance between ships
        shipDistance = abs(otherShip.loc - self.loc)
        
        #determine if ship has targeting data for other ship
        targetingData = False
        if(self.satellite):
            targetingData = True
        elif(shipDistance <= 100 and shipDistance > 40):
            if(self.uav):
                if(random.random() < .5):
                    targetingData = True
            if(self.usv):
                if(random.random() < .2):
                    targetingData = True
        elif(shipDistance <= 40 and shipDistance > 30):
            if(self.passiveSensors):
                targetingData = True
            if(self.uav):
                if(random.random() < .5):
                    targetingData = True
            if(self.usv):
                if(random.random() < .2):
                    targetingData = True
        elif(shipDistance <= 30 and shipDistance > 20):
            if(self.electronicSurveillance and otherShip.radar):
                targetingData = True
            if(self.uav):
                if(random.random() < .5):
                    targetingData = True
            if(self.usv):
                if(random.random() < .2):
                    targetingData = True     
        elif(shipDistance <= 20):
            if(self.radar):
                targetingData = True
            if(self.electronicSurveillance and otherShip.radar):
                targetingData = True
            if(self.uav):
                if(random.random() < .5):
                    targetingData = True
            if(self.usv):
                if(random.random() < .2):
                    targetingData = True
        
        #if targeting data is present
        #if ship is in range, has it been shot at?, decide to shoot again or not                     
        #print(targetingData)
        if(targetingData):
            if (shipDistance <= self.offensiveMissileRange):
                shootCount = 0
                for missile in self.offensiveMissileList:
                    #only need to check if flying because simulation ends when a ship is hit
                    #therefore either the offensive missile was unsuccessful already or hasn't been shot at
                    if(missile.flying == True):
                        shootCount = shootCount + 1       
                if(shootCount < self.offensiveMissileSS):
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
            if(incomingMissile.flying and (abs(incomingMissile.loc - self.loc) <= 100)):
                for defensiveMissile in self.defensiveMissileList:
                    if(defensiveMissile.flying):
                        if(incomingMissile == defensiveMissile.target):
                            shootCount = shootCount + 1
                
                #current distance between incoming missile and its target
                incomingTargetDistance = abs(incomingMissile.loc - incomingMissile.target.loc)
                #old policy based on probability number shot (using more realistic one now)
                '''currentHitProb = 0
                if(incomingTargetDistance <= 5 and incomingTargetDistance > 0):
                    currentHitProb = self.defHitProbP3
                elif(incomingTargetDistance <=20 and incomingTargetDistance > 5):
                   currentHitProb = self.defHitProbP2
                elif(incomingTargetDistance <=100 and incomingTargetDistance > 20):
                    currentHitProb = self.defHitProbP1
                
                if(shootCount < int(1/currentHitProb)):
                    self.launchDefensiveMissile(incomingMissile)
                    #print(shootCount)'''
                #determine how we shoot based on where incoming missile is
                #less than 5NM we are using Point Defense System
                #Extended NATO Seasparrow Missile (ESSM) from 3-5 NM
                #Sea RAM (Rolling Air Frame Missile) from 1-3 NM
                #CIWS from 0-1 NM
                #Also use Soft Kill ECM (Decoy, Jamming)
                if(incomingTargetDistance <= 5 and incomingTargetDistance > 0):
                    self.launchPointDefense(incomingMissile, incomingTargetDistance)
                #simplified shoot, look, shoot method with SM-2
                elif(incomingTargetDistance <=20 and incomingTargetDistance > 5):
                    if(shootCount < self.defensiveMissileSS):
                        self.launchDefensiveMissile(incomingMissile)
                #simplified shoot, shoot, look, shoot method with SM-2
                elif(incomingTargetDistance <=100 and incomingTargetDistance > 20):
                    if(shootCount < self.defensiveMissileSS):
                        self.launchDefensiveMissile(incomingMissile)
    
    #called by findMissileTargets when wanting to launch any Point Defense System
    def launchPointDefense(self, targetMissile, incomingTargetDistance):
        #determine how we shoot based on where incoming missile is
        #less than 5NM we are using Point Defense System
        #Extended NATO SeaSparrow Missile (ESSM) from 3-5 NM
        if(incomingTargetDistance <= 5 and incomingTargetDistance > 3):
            shootCount = 0
            for essm in self.essmList:
                if(essm.flying):
                    if(targetMissile == essm.target):
                        shootCount = shootCount + 1
            if(shootCount < self.essmSS):
                  #can only launch missile if there are missiles left to be fired
                  if(self.essmTotal - self.essmf > 0):
                      self.essmList[self.essmf].launchMissile(targetMissile)
                      self.essmf = self.essmf + 1
        #Sea RAM (Rolling Air Frame Missile) from 1-3 NM
        if(incomingTargetDistance <= 3 and incomingTargetDistance > 1):
            shootCount = 0
            for seaRam in self.seaRamList:
                if(seaRam.flying):
                    if(targetMissile == seaRam.target):
                        shootCount = shootCount + 1
            if(shootCount < self.seaRamSS):
                  #can only launch missile if there are missiles left to be fired
                  if(self.seaRamTotal - self.seaRamf > 0):
                      self.seaRamList[self.seaRamf].launchMissile(targetMissile)
                      self.seaRamf = self.seaRamf + 1
        #CIWS from 0-1 NM
        if(incomingTargetDistance <= 1 and incomingTargetDistance > 0):
            shootCount = 0
            for ciws in self.ciwsList:
                if(ciws.flying):
                    if(targetMissile == ciws.target):
                        shootCount = shootCount + 1
            if(shootCount < self.ciwsSS):
                  #can only fire bullets if there are bullets left
                  if(self.ciwsTotal - self.ciwsf > 0):
                      self.ciwsList[self.ciwsf].fireBulletRounds(targetMissile)
                      self.ciwsf = self.ciwsf + 1
        #Also use Soft Kill ECM (Decoy, Jamming)
    
    #called by findMissileTargets when wanting to launch a defensive missile               
    def launchDefensiveMissile(self, targetMissile):
        #can only launch missile if there are missiles left to be fired
        if(self.defensiveMissileTotal - self.dmf > 0):
            self.defensiveMissileList[self.dmf].launchMissile(targetMissile)
            self.dmf = self.dmf + 1
    
    #check all missiles/bullets to determine if they've hit their targets
    def checkHitTargets(self, animationFile, simulationTime):
        for missile in self.offensiveMissileList:
            #missile.checkHitTarget()
            if(missile.flying):
                animationFile.write(str(simulationTime) + " " + str(missile.loc) + " " + self.name + " offensive " + str(missile.checkHitTarget()) + "\n")
        for missile in self.defensiveMissileList:
            #missile.checkHitTarget()
            if(missile.flying):
                animationFile.write(str(simulationTime) + " " + str(missile.loc) + " " + self.name + " defensive " + str(missile.checkHitTarget()) + "\n")    
        for missile in self.essmList:
            #missile.checkHitTarget()
            if(missile.flying):
                animationFile.write(str(simulationTime) + " " + str(missile.loc) + " " + self.name + " ESSM " + str(missile.checkHitTarget()) + "\n") 
        for missile in self.seaRamList:
            #missile.checkHitTarget()
            if(missile.flying):
                animationFile.write(str(simulationTime) + " " + str(missile.loc) + " " + self.name + " SeaRAM " + str(missile.checkHitTarget()) + "\n") 
        for bulletRound in self.ciwsList:
            #missile.checkHitTarget()
            if(bulletRound.flying):
                animationFile.write(str(simulationTime) + " " + str(bulletRound.loc) + " " + self.name + " CIWS " + str(bulletRound.checkHitTarget()) + "\n")     
    
    #determine if the ship is out of all missiles
    #returns True if no missiles left, false otherwise        
    def outOfMissiles(self):
        #if all offensive missiles fired and are not currently flying
        offenseFiredDown = True
        for missile in self.offensiveMissileList:
            if missile.target == None or (missile.target != None and missile.flying):
                offenseFiredDown = False
    
        if(self.offensiveMissileTotal - self.omf <= 0 and self.defensiveMissileTotal - self.dmf <= 0 and self.essmTotal - self.essmf <=0 and self.seaRamTotal - self.seaRamf <= 0 and self.ciwsTotal - self.ciwsf <=0):
            return True
        elif(offenseFiredDown):
            return True
        else:
            return False
        
    def engagementCost(self):
        currentCost = 0
        if self.hit == True :
            currentCost = currentCost + 2000000000
        if self.offensiveMissileRange >= 300:
            currentCost = currentCost + self.omf * 2000000
        else:
            currentCost = currentCost + self.omf * 1000000
        currentCost = currentCost + self.dmf * 1000000
        currentCost = currentCost + self.essmf * 956000
        currentCost = currentCost + self.seaRamf * 998000
        currentCost = currentCost + self.ciwsf * 200000
        return(currentCost)
  
        
            