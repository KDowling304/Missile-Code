#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:14:19 2019

@author: karadowling
code adapted from ORF 411 AssetSelling problem code found at link below
https://github.com/wbpowell328/stochastic-optimization/tree/master/AssetSelling

This script runs multiple simulations of a two-agent surface ship missile engagement.  
The simulation starts with one or both of the ships firing offensive missiles and ends when 
either ship is hit by a missle or both ships are out of missiles.

The script changes Red and Blue's use of satellite and creates boxplots to show the output.
"""

#from collections import namedtuple
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import numpy as np
#from matplotlib.ticker import MaxNLocator
#from copy import copy
#import math
from Ship import Ship

if __name__ == "__main__":
    #read in policy parameters from an Excel spreadsheet, "missile_policy_parameters.xlsx"
    sheet1 = pd.read_excel("missile_policy_parameters.xlsx", sheet_name="Sheet1")
    sheet2 = pd.read_excel("missile_policy_parameters.xlsx", sheet_name="Sheet2")
    
    #state variables


    #time step for each iteration of "game" in minuntes
    timeStep = sheet2['Time Step (minutes)'][0]
    #print("Time step each iteration is " + str(timeStep) + " minutes")
    #print('')
    
    iterations = sheet2['Iterations of Simulation'][0]
    print("Simulation Iterations: " + str(iterations) + "\n")
    
    #initial data blueShip
    initialBlue = [sheet1['Ship\'s Name'][0], sheet1['Location (NM) 1D scale'][0], 
                sheet1['Offensive Missiles'][0], sheet1['Defensive Missiles'][0],
                sheet1['ESSMs'][0], sheet1['SeaRAMs'][0], 
                sheet1['CIWS (each has 1500 rounds)'][0],
                sheet1['Ship Speed (kn)'][0], sheet1['Missile Speed (kn)'][0], 
                timeStep, sheet1['Offensive Missile Range (NM)'][0], 
                sheet1['Offensive Missile Success Probability'][0],
                sheet1['Defensive Missile Success Probability (if target offensive missile is 100-20 NM from its target - phase 1)'][0],
                sheet1['Defensive Missile Success Probability (if target offensive missile is 20-5 NM from its target - phase 2)'][0],
                sheet1['Defensive Missile Success Probability (if target offensive missile is 5-1 NM from its target - phase 3)'][0],
                sheet1['ESSM Success Probability'][0],
                sheet1['SeaRAM Success Probability'][0],
                sheet1['CIWS Success Probability'][0],
                sheet1['Offensive Missile Salvo Size'][0],
                sheet1['Defensive Missile Salvo Size'][0],
                sheet1['ESSM Salvo Size'][0],
                sheet1['SeaRAM Salvo Size'][0],
                sheet1['CIWS Iteration Salvo Size'][0],
                sheet1['Satellite'][0], sheet1['Radar'][0], 
                sheet1['Electronic Surveillance'][0], 
                sheet1['Passive Sensors (Acoustic)'][0],
                sheet1['UAV'][0], sheet1['USV'][0]]
    
    initialRed = [sheet1['Ship\'s Name'][1], sheet1['Location (NM) 1D scale'][1], 
                sheet1['Offensive Missiles'][1], sheet1['Defensive Missiles'][1], 
                sheet1['ESSMs'][1], sheet1['SeaRAMs'][1], 
                sheet1['CIWS (each has 1500 rounds)'][1],
                sheet1['Ship Speed (kn)'][1], sheet1['Missile Speed (kn)'][1], 
                timeStep, sheet1['Offensive Missile Range (NM)'][1], 
                sheet1['Offensive Missile Success Probability'][1],
                sheet1['Defensive Missile Success Probability (if target offensive missile is 100-20 NM from its target - phase 1)'][1],
                sheet1['Defensive Missile Success Probability (if target offensive missile is 20-5 NM from its target - phase 2)'][1],
                sheet1['Defensive Missile Success Probability (if target offensive missile is 5-1 NM from its target - phase 3)'][1],
                sheet1['ESSM Success Probability'][1],
                sheet1['SeaRAM Success Probability'][1],
                sheet1['CIWS Success Probability'][1],
                sheet1['Offensive Missile Salvo Size'][1],
                sheet1['Defensive Missile Salvo Size'][1],
                sheet1['ESSM Salvo Size'][1],
                sheet1['SeaRAM Salvo Size'][1],
                sheet1['CIWS Iteration Salvo Size'][1],
                sheet1['Satellite'][1], sheet1['Radar'][1], 
                sheet1['Electronic Surveillance'][1], 
                sheet1['Passive Sensors (Acoustic)'][1],
                sheet1['UAV'][1 ], sheet1['USV'][1]]
    
    
    #ALL SATELLITES OFF
    print("BOTH RED AND BLUE SATELLITES OFF")
    print()
    #Create Plot List for Missile Count Over Time
    iterationArray = [] 
    simulationTimeArray = []
    BlueNumberOffensiveMissiles = []
    BlueNumberDefensiveMissiles = []
    BlueNumberESSMs = []
    BlueNumberSeaRAMs = []
    BlueNumberCIWS = []
    BlueShipOffensiveMissileRange = []
    BlueShipHit = []
    BlueShipCost = []
    BlueShipMissileCost = []
    RedNumberOffensiveMissiles = []
    RedNumberDefensiveMissiles = []
    RedNumberESSMs = []
    RedNumberSeaRAMs = []
    RedNumberCIWS = []
    RedShipOffensiveMissileRange = []
    RedShipHit = []
    RedShipCost = []
    RedShipMissileCost = []
    ShipRange = []
    

    
    for i in range(iterations):
    
        #Initialize Ships
        blueShip = Ship(initialBlue[0], initialBlue[1], 
                        initialBlue[2], initialBlue[3],
                        initialBlue[4], initialBlue[5], 
                    initialBlue[6],
                    initialBlue[7], initialBlue[8], 
                    initialBlue[9], initialBlue[10], 
                    initialBlue[11],
                    initialBlue[12],
                    initialBlue[13],
                    initialBlue[14],
                    initialBlue[15],
                    initialBlue[16],
                    initialBlue[17],
                    initialBlue[18],
                    initialBlue[19],
                    initialBlue[20],
                    initialBlue[21],
                    initialBlue[22],
                    False, initialBlue[24], 
                    initialBlue[25], 
                    initialBlue[26],
                    initialBlue[27], initialBlue[28])
        redShip = Ship(initialRed[0], initialRed[1], 
                    initialRed[2], initialRed[3],
                    initialRed[4], initialRed[5], 
                    initialRed[6],
                    initialRed[7], initialRed[8], 
                    initialRed[9], initialRed[10], 
                    initialRed[11],
                    initialRed[12],
                    initialRed[13],
                    initialRed[14],
                    initialRed[15],
                    initialRed[16],
                    initialRed[17],
                    initialRed[18],
                    initialRed[19],
                    initialRed[20],
                    initialRed[21],
                    initialRed[22],
                    False, initialRed[24], 
                    initialRed[25], 
                    initialRed[26],
                    initialRed[27], initialRed[28])
        
        
        #Run Missile Simulation
        #keeps track of iterations that are representative of minutes
        simulationTime = 0.25 #in minutes
        #simulation ends when certain time passes to ensure no infinite loop 
        #can occur
        animationFile = open("animationFile.txt", "w")
        while(simulationTime <= 1000):
            #determines whether Blue or Red goes first each time step
            BlueFirst = np.random.binomial(1,0.5)
            #print(BlueFirst)
            
            if(BlueFirst == 1):
                if(blueShip.hit or redShip.hit):
                    break
                #stop simulation if both ships are out of ammunition(missiles)
                if(blueShip.outOfMissiles() and redShip.outOfMissiles()):
                    break 
                #if(redShip.offensiveMissileTotal - redShip.omf <= 0):
                    #break
                #move ships if they are out of range
                blueShip.moveShip(redShip, animationFile, simulationTime)
                redShip.moveShip(blueShip, animationFile, simulationTime)
                
                #determine if there are target ships or missiles for the ships
                blueShip.findShipTargets(redShip)
                blueShip.findMissileTargets(redShip)
                redShip.findShipTargets(blueShip)
                redShip.findMissileTargets(blueShip)
            
                #check if any flying missiles have hit their targets
                blueShip.checkHitTargets(animationFile, simulationTime)
                redShip.checkHitTargets(animationFile, simulationTime)
    
                #move all flying missiles forward to next state according to 
                #time and speed
                blueShip.moveAllMissiles()
                redShip.moveAllMissiles()
 
                #increment the simulation time
                simulationTime = simulationTime + 0.25
                
            else:
                #checking for exit conditions
                #stop simulation if either ship is hit
                if(redShip.hit or blueShip.hit):
                    break
                #stop simulation if both ships are out of ammunition(missiles)
                if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
                    break 
                #if(redShip.offensiveMissileTotal - redShip.omf <= 0):
                    #break
                #move ships if they are out of range
                redShip.moveShip(blueShip, animationFile, simulationTime)
                blueShip.moveShip(redShip, animationFile, simulationTime)
                
                #determine if there are target ships or missiles for the ships
                redShip.findShipTargets(blueShip)
                redShip.findMissileTargets(blueShip)
                blueShip.findShipTargets(redShip)
                blueShip.findMissileTargets(redShip)
            
                #check if any flying missiles have hit their targets
                redShip.checkHitTargets(animationFile, simulationTime)
                blueShip.checkHitTargets(animationFile, simulationTime)
    
                #move all flying missiles forward to next state according to time and speed
                redShip.moveAllMissiles()
                blueShip.moveAllMissiles()
                
                #increment the simulation time
                simulationTime = simulationTime + 0.25
            
        animationFile.close()
        print("Iteration: " + str(i + 1))
        print()
        blueShip.printShip()
        redShip.printShip()
        #blueShip.printShipInputs(redShip)
        if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
            print("Both ships out of missiles")
            print()
        iterationArray.append(i)
        simulationTimeArray.append(simulationTime)
        BlueNumberOffensiveMissiles.append(blueShip.omf)
        BlueNumberDefensiveMissiles.append(blueShip.dmf)
        BlueNumberESSMs.append(blueShip.essmf)
        BlueNumberSeaRAMs.append(blueShip.seaRamf)
        BlueNumberCIWS.append(blueShip.ciwsf)
        BlueShipOffensiveMissileRange.append(blueShip.offensiveMissileRange)
        BlueShipHit.append(blueShip.hit)
        BlueShipCost.append(blueShip.engagementCost())
        BlueShipMissileCost.append(blueShip.missileCost())
        RedNumberOffensiveMissiles.append(redShip.omf)
        RedNumberDefensiveMissiles.append(redShip.dmf)
        RedNumberESSMs.append(redShip.essmf)
        RedNumberSeaRAMs.append(redShip.seaRamf)
        RedNumberCIWS.append(redShip.ciwsf)
        RedShipOffensiveMissileRange.append(redShip.offensiveMissileRange)
        RedShipHit.append(redShip.hit)
        RedShipCost.append(redShip.engagementCost())
        RedShipMissileCost.append(redShip.missileCost())
        ShipRange.append(abs(blueShip.loc-redShip.loc))
        #print(redShip.satellite)
        #print(blueShip.satellite)
        
    #Number of simulation runs Blue Ship Hit
    BlueShipHitNumber = BlueShipHit.count(True)
    #print(BlueShipHitNumber)
    #Proportion of total simulation runs that blue ship is hit (loses)
    BlueShipHitProp = BlueShipHitNumber/len(BlueShipHit)
    print("Proportion of Iterations Blue Ship Hit: " + str(BlueShipHitProp))
    
    #Number of simulation runs Blue Ship Hit
    RedShipHitNumber = RedShipHit.count(True)
    #print(RedShipHitNumber)
    #Proportion of total simulation runs that red ship is hit (loses)
    RedShipHitProp = RedShipHitNumber/len(RedShipHit)
    print("Proportion of Iterations Red Ship Hit: " + str(RedShipHitProp))
    
    BothShipHitNumber = 0
    NoShipHitNumber = 0
    BlueShipHitNumber = 0
    RedShipHitNumber = 0
    for s in range(len(RedShipHit)):
        if(RedShipHit[s] == True and BlueShipHit[s] == True):
            BothShipHitNumber = BothShipHitNumber + 1
        if(RedShipHit[s] == False and BlueShipHit[s] == False):
            NoShipHitNumber = NoShipHitNumber + 1
            
    
    
    #BLUE SATELLITE OFF, RED ON
    print("BLUE SATELLITE OFF, RED ON")
    print()
    #Create Plot List for Missile Count Over Time
    iterationArray2 = [] 
    simulationTimeArray2 = []
    BlueNumberOffensiveMissiles2 = []
    BlueNumberDefensiveMissiles2 = []
    BlueNumberESSMs2 = []
    BlueNumberSeaRAMs2 = []
    BlueNumberCIWS2 = []
    BlueShipOffensiveMissileRange2 = []
    BlueShipHit2 = []
    BlueShipCost2 = []
    BlueShipMissileCost2 = []
    RedNumberOffensiveMissiles2 = []
    RedNumberDefensiveMissiles2 = []
    RedNumberESSMs2 = []
    RedNumberSeaRAMs2 = []
    RedNumberCIWS2 = []
    RedShipOffensiveMissileRange2 = []
    RedShipHit2 = []
    RedShipCost2 = []
    RedShipMissileCost2 = []
    ShipRange2 = []
    

    
    for i in range(iterations):
    
        #Initialize Ships
        blueShip = Ship(initialBlue[0], initialBlue[1], 
                        initialBlue[2], initialBlue[3],
                        initialBlue[4], initialBlue[5], 
                    initialBlue[6],
                    initialBlue[7], initialBlue[8], 
                    initialBlue[9], initialBlue[10],
                    initialBlue[11],
                    initialBlue[12],
                    initialBlue[13],
                    initialBlue[14],
                    initialBlue[15],
                    initialBlue[16],
                    initialBlue[17],
                    initialBlue[18],
                    initialBlue[19],
                    initialBlue[20],
                    initialBlue[21],
                    initialBlue[22],
                    False, initialBlue[24], 
                    initialBlue[25], 
                    initialBlue[26],
                    initialBlue[27], initialBlue[28])
        redShip = Ship(initialRed[0], initialRed[1], 
                    initialRed[2], initialRed[3],
                    initialRed[4], initialRed[5], 
                    initialRed[6],
                    initialRed[7], initialRed[8], 
                    initialRed[9], initialRed[10], 
                    initialRed[11],
                    initialRed[12],
                    initialRed[13],
                    initialRed[14],
                    initialRed[15],
                    initialRed[16],
                    initialRed[17],
                    initialRed[18],
                    initialRed[19],
                    initialRed[20],
                    initialRed[21],
                    initialRed[22],
                    True, initialRed[24], 
                    initialRed[25], 
                    initialRed[26],
                    initialRed[27], initialRed[28])
        
        
        #Run Missile Simulation
        #keeps track of iterations that are representative of minutes
        simulationTime = 0.25 #in minutes
        #simulation ends when certain time passes to ensure no infinite loop 
        #can occur
        animationFile = open("animationFile.txt", "w")
        while(simulationTime <= 1000):
            #determines whether Blue or Red goes first each time step
            BlueFirst = np.random.binomial(1,0.5)
            #print(BlueFirst)
            
            if(BlueFirst == 1):
                if(blueShip.hit or redShip.hit):
                    break
                #stop simulation if both ships are out of ammunition(missiles)
                if(blueShip.outOfMissiles() and redShip.outOfMissiles()):
                    break 
                #if(redShip.offensiveMissileTotal - redShip.omf <= 0):
                    #break
                #move ships if they are out of range
                blueShip.moveShip(redShip, animationFile, simulationTime)
                redShip.moveShip(blueShip, animationFile, simulationTime)
                
                #determine if there are target ships or missiles for the ships
                blueShip.findShipTargets(redShip)
                blueShip.findMissileTargets(redShip)
                redShip.findShipTargets(blueShip)
                redShip.findMissileTargets(blueShip)
            
                #check if any flying missiles have hit their targets
                blueShip.checkHitTargets(animationFile, simulationTime)
                redShip.checkHitTargets(animationFile, simulationTime)
    
                #move all flying missiles forward to next state according to 
                #time and speed
                blueShip.moveAllMissiles()
                redShip.moveAllMissiles()
 
                #increment the simulation time
                simulationTime = simulationTime + 0.25
                
            else:
                #checking for exit conditions
                #stop simulation if either ship is hit
                if(redShip.hit or blueShip.hit):
                    break
                #stop simulation if both ships are out of ammunition(missiles)
                if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
                    break 
                #if(redShip.offensiveMissileTotal - redShip.omf <= 0):
                    #break
                #move ships if they are out of range
                redShip.moveShip(blueShip, animationFile, simulationTime)
                blueShip.moveShip(redShip, animationFile, simulationTime)
                
                #determine if there are target ships or missiles for the ships
                redShip.findShipTargets(blueShip)
                redShip.findMissileTargets(blueShip)
                blueShip.findShipTargets(redShip)
                blueShip.findMissileTargets(redShip)
            
                #check if any flying missiles have hit their targets
                redShip.checkHitTargets(animationFile, simulationTime)
                blueShip.checkHitTargets(animationFile, simulationTime)
    
                #move all flying missiles forward to next state according to time and speed
                redShip.moveAllMissiles()
                blueShip.moveAllMissiles()
                
                #increment the simulation time
                simulationTime = simulationTime + 0.25
            
        animationFile.close()
        print("Iteration: " + str(i + 1))
        print()
        blueShip.printShip()
        redShip.printShip()
        #blueShip.printShipInputs(redShip)
        if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
            print("Both ships out of missiles")
            print()
        iterationArray2.append(i)
        simulationTimeArray2.append(simulationTime)
        BlueNumberOffensiveMissiles2.append(blueShip.omf)
        BlueNumberDefensiveMissiles2.append(blueShip.dmf)
        BlueNumberESSMs2.append(blueShip.essmf)
        BlueNumberSeaRAMs2.append(blueShip.seaRamf)
        BlueNumberCIWS2.append(blueShip.ciwsf)
        BlueShipOffensiveMissileRange2.append(blueShip.offensiveMissileRange)
        BlueShipHit2.append(blueShip.hit)
        BlueShipCost2.append(blueShip.engagementCost())
        BlueShipMissileCost2.append(blueShip.missileCost())
        RedNumberOffensiveMissiles2.append(redShip.omf)
        RedNumberDefensiveMissiles2.append(redShip.dmf)
        RedNumberESSMs2.append(redShip.essmf)
        RedNumberSeaRAMs2.append(redShip.seaRamf)
        RedNumberCIWS2.append(redShip.ciwsf)
        RedShipOffensiveMissileRange2.append(redShip.offensiveMissileRange)
        RedShipHit2.append(redShip.hit)
        RedShipCost2.append(redShip.engagementCost())
        RedShipMissileCost2.append(redShip.missileCost())
        ShipRange2.append(abs(blueShip.loc-redShip.loc))
        #print(redShip.satellite)
        #print(blueShip.satellite)
        
    #Number of simulation runs Blue Ship Hit
    BlueShipHitNumber2 = BlueShipHit2.count(True)
    #print(BlueShipHitNumber)
    #Proportion of total simulation runs that blue ship is hit (loses)
    BlueShipHitProp2 = BlueShipHitNumber2/len(BlueShipHit2)
    print("Proportion of Iterations Blue Ship Hit: " + str(BlueShipHitProp2))
    
    #Number of simulation runs Blue Ship Hit
    RedShipHitNumber2 = RedShipHit2.count(True)
    #print(RedShipHitNumber)
    #Proportion of total simulation runs that red ship is hit (loses)
    RedShipHitProp2 = RedShipHitNumber2/len(RedShipHit2)
    print("Proportion of Iterations Red Ship Hit: " + str(RedShipHitProp2))
    
    BothShipHitNumber2 = 0
    NoShipHitNumber2 = 0
    BlueShipHitNumber2 = 0
    RedShipHitNumber2 = 0
    for s in range(len(RedShipHit2)):
        if(RedShipHit2[s] == True and BlueShipHit2[s] == True):
            BothShipHitNumber2 = BothShipHitNumber2 + 1
        if(RedShipHit2[s] == False and BlueShipHit2[s] == False):
            NoShipHitNumber2 = NoShipHitNumber2 + 1
            
    
    #BLUE SATELLITE ON, RED OFF
    print("BLUE SATELLITE ON, RED OFF")
    print()
    #Create Plot List for Missile Count Over Time
    iterationArray3 = [] 
    simulationTimeArray3 = []
    BlueNumberOffensiveMissiles3 = []
    BlueNumberDefensiveMissiles3 = []
    BlueNumberESSMs3 = []
    BlueNumberSeaRAMs3 = []
    BlueNumberCIWS3 = []
    BlueShipOffensiveMissileRange3 = []
    BlueShipHit3 = []
    BlueShipCost3 = []
    BlueShipMissileCost3 = []
    RedNumberOffensiveMissiles3 = []
    RedNumberDefensiveMissiles3 = []
    RedNumberESSMs3 = []
    RedNumberSeaRAMs3 = []
    RedNumberCIWS3 = []
    RedShipOffensiveMissileRange3 = []
    RedShipHit3 = []
    RedShipCost3 = []
    RedShipMissileCost3 = []
    ShipRange3 = []
    

    
    for i in range(iterations):
    
        #Initialize Ships
        blueShip = Ship(initialBlue[0], initialBlue[1], 
                        initialBlue[2], initialBlue[3],
                        initialBlue[4], initialBlue[5], 
                    initialBlue[6],
                    initialBlue[7], initialBlue[8], 
                    initialBlue[9], initialBlue[10],
                    initialBlue[11],
                    initialBlue[12],
                    initialBlue[13],
                    initialBlue[14],
                    initialBlue[15],
                    initialBlue[16],
                    initialBlue[17],
                    initialBlue[18],
                    initialBlue[19],
                    initialBlue[20],
                    initialBlue[21],
                    initialBlue[22],
                    True, initialBlue[24], 
                    initialBlue[25], 
                    initialBlue[26],
                    initialBlue[27], initialBlue[28])
        redShip = Ship(initialRed[0], initialRed[1], 
                    initialRed[2], initialRed[3],
                    initialRed[4], initialRed[5], 
                    initialRed[6],
                    initialRed[7], initialRed[8], 
                    initialRed[9], initialRed[10], 
                    initialRed[11],
                    initialRed[12],
                    initialRed[13],
                    initialRed[14],
                    initialRed[15],
                    initialRed[16],
                    initialRed[17],
                    initialRed[18],
                    initialRed[19],
                    initialRed[20],
                    initialRed[21],
                    initialRed[22],
                    False, initialRed[24], 
                    initialRed[25], 
                    initialRed[26],
                    initialRed[27], initialRed[28])
        
        
        #Run Missile Simulation
        #keeps track of iterations that are representative of minutes
        simulationTime = 0.25 #in minutes
        #simulation ends when certain time passes to ensure no infinite loop 
        #can occur
        animationFile = open("animationFile.txt", "w")
        while(simulationTime <= 1000):
            #determines whether Blue or Red goes first each time step
            BlueFirst = np.random.binomial(1,0.5)
            #print(BlueFirst)
            
            if(BlueFirst == 1):
                if(blueShip.hit or redShip.hit):
                    break
                #stop simulation if both ships are out of ammunition(missiles)
                if(blueShip.outOfMissiles() and redShip.outOfMissiles()):
                    break 
                #if(redShip.offensiveMissileTotal - redShip.omf <= 0):
                    #break
                #move ships if they are out of range
                blueShip.moveShip(redShip, animationFile, simulationTime)
                redShip.moveShip(blueShip, animationFile, simulationTime)
                
                #determine if there are target ships or missiles for the ships
                blueShip.findShipTargets(redShip)
                blueShip.findMissileTargets(redShip)
                redShip.findShipTargets(blueShip)
                redShip.findMissileTargets(blueShip)
            
                #check if any flying missiles have hit their targets
                blueShip.checkHitTargets(animationFile, simulationTime)
                redShip.checkHitTargets(animationFile, simulationTime)
    
                #move all flying missiles forward to next state according to 
                #time and speed
                blueShip.moveAllMissiles()
                redShip.moveAllMissiles()
 
                #increment the simulation time
                simulationTime = simulationTime + 0.25
                
            else:
                #checking for exit conditions
                #stop simulation if either ship is hit
                if(redShip.hit or blueShip.hit):
                    break
                #stop simulation if both ships are out of ammunition(missiles)
                if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
                    break 
                #if(redShip.offensiveMissileTotal - redShip.omf <= 0):
                    #break
                #move ships if they are out of range
                redShip.moveShip(blueShip, animationFile, simulationTime)
                blueShip.moveShip(redShip, animationFile, simulationTime)
                
                #determine if there are target ships or missiles for the ships
                redShip.findShipTargets(blueShip)
                redShip.findMissileTargets(blueShip)
                blueShip.findShipTargets(redShip)
                blueShip.findMissileTargets(redShip)
            
                #check if any flying missiles have hit their targets
                redShip.checkHitTargets(animationFile, simulationTime)
                blueShip.checkHitTargets(animationFile, simulationTime)
    
                #move all flying missiles forward to next state according to time and speed
                redShip.moveAllMissiles()
                blueShip.moveAllMissiles()
                
                #increment the simulation time
                simulationTime = simulationTime + 0.25
            
        animationFile.close()
        print("Iteration: " + str(i + 1))
        print()
        blueShip.printShip()
        redShip.printShip()
        #blueShip.printShipInputs(redShip)
        if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
            print("Both ships out of missiles")
            print()
        iterationArray3.append(i)
        simulationTimeArray3.append(simulationTime)
        BlueNumberOffensiveMissiles3.append(blueShip.omf)
        BlueNumberDefensiveMissiles3.append(blueShip.dmf)
        BlueNumberESSMs3.append(blueShip.essmf)
        BlueNumberSeaRAMs3.append(blueShip.seaRamf)
        BlueNumberCIWS3.append(blueShip.ciwsf)
        BlueShipOffensiveMissileRange3.append(blueShip.offensiveMissileRange)
        BlueShipHit3.append(blueShip.hit)
        BlueShipCost3.append(blueShip.engagementCost())
        BlueShipMissileCost3.append(blueShip.missileCost())
        RedNumberOffensiveMissiles3.append(redShip.omf)
        RedNumberDefensiveMissiles3.append(redShip.dmf)
        RedNumberESSMs3.append(redShip.essmf)
        RedNumberSeaRAMs3.append(redShip.seaRamf)
        RedNumberCIWS3.append(redShip.ciwsf)
        RedShipOffensiveMissileRange3.append(redShip.offensiveMissileRange)
        RedShipHit3.append(redShip.hit)
        RedShipCost3.append(redShip.engagementCost())
        RedShipMissileCost3.append(redShip.missileCost())
        ShipRange3.append(abs(blueShip.loc-redShip.loc))
        #print(redShip.satellite)
        #print(blueShip.satellite)
        
    #Number of simulation runs Blue Ship Hit
    BlueShipHitNumber3 = BlueShipHit3.count(True)
    #print(BlueShipHitNumber)
    #Proportion of total simulation runs that blue ship is hit (loses)
    BlueShipHitProp3 = BlueShipHitNumber3/len(BlueShipHit3)
    print("Proportion of Iterations Blue Ship Hit: " + str(BlueShipHitProp3))
    
    #Number of simulation runs Blue Ship Hit
    RedShipHitNumber3 = RedShipHit3.count(True)
    #print(RedShipHitNumber)
    #Proportion of total simulation runs that red ship is hit (loses)
    RedShipHitProp3 = RedShipHitNumber3/len(RedShipHit3)
    print("Proportion of Iterations Red Ship Hit: " + str(RedShipHitProp3))
    
    BothShipHitNumber3 = 0
    NoShipHitNumber3 = 0
    BlueShipHitNumber3 = 0
    RedShipHitNumber3 = 0
    for s in range(len(RedShipHit3)):
        if(RedShipHit3[s] == True and BlueShipHit3[s] == True):
            BothShipHitNumber3 = BothShipHitNumber3 + 1
        if(RedShipHit3[s] == False and BlueShipHit3[s] == False):
            NoShipHitNumber3 = NoShipHitNumber3 + 1
        
    
        #BLUE SATELLITE ON, RED ON
    print("BLUE SATELLITE ON, RED ON")
    print()
    #Create Plot List for Missile Count Over Time
    iterationArray4= [] 
    simulationTimeArray4 = []
    BlueNumberOffensiveMissiles4 = []
    BlueNumberDefensiveMissiles4 = []
    BlueNumberESSMs4 = []
    BlueNumberSeaRAMs4 = []
    BlueNumberCIWS4 = []
    BlueShipOffensiveMissileRange4 = []
    BlueShipHit4 = []
    BlueShipCost4 = []
    BlueShipMissileCost4 = []
    RedNumberOffensiveMissiles4 = []
    RedNumberDefensiveMissiles4 = []
    RedNumberESSMs4 = []
    RedNumberSeaRAMs4 = []
    RedNumberCIWS4 = []
    RedShipOffensiveMissileRange4 = []
    RedShipHit4 = []
    RedShipCost4 = []
    RedShipMissileCost4 = []
    ShipRange4 = []
    

    
    for i in range(iterations):
    
        #Initialize Ships
        blueShip = Ship(initialBlue[0], initialBlue[1], 
                        initialBlue[2], initialBlue[3],
                        initialBlue[4], initialBlue[5], 
                    initialBlue[6],
                    initialBlue[7], initialBlue[8], 
                    initialBlue[9], initialBlue[10],
                    initialBlue[11],
                    initialBlue[12],
                    initialBlue[13],
                    initialBlue[14],
                    initialBlue[15],
                    initialBlue[16],
                    initialBlue[17],
                    initialBlue[18],
                    initialBlue[19],
                    initialBlue[20],
                    initialBlue[21],
                    initialBlue[22],
                    True, initialBlue[24], 
                    initialBlue[25], 
                    initialBlue[26],
                    initialBlue[27], initialBlue[28])
        redShip = Ship(initialRed[0], initialRed[1], 
                    initialRed[2], initialRed[3],
                    initialRed[4], initialRed[5], 
                    initialRed[6],
                    initialRed[7], initialRed[8], 
                    initialRed[9], initialRed[10], 
                    initialRed[11],
                    initialRed[12],
                    initialRed[13],
                    initialRed[14],
                    initialRed[15],
                    initialRed[16],
                    initialRed[17],
                    initialRed[18],
                    initialRed[19],
                    initialRed[20],
                    initialRed[21],
                    initialRed[22],
                    True, initialRed[24], 
                    initialRed[25], 
                    initialRed[26],
                    initialRed[27], initialRed[28])
        
        
        #Run Missile Simulation
        #keeps track of iterations that are representative of minutes
        simulationTime = 0.25 #in minutes
        #simulation ends when certain time passes to ensure no infinite loop 
        #can occur
        animationFile = open("animationFile.txt", "w")
        while(simulationTime <= 1000):
            #determines whether Blue or Red goes first each time step
            BlueFirst = np.random.binomial(1,0.5)
            #print(BlueFirst)
            
            if(BlueFirst == 1):
                if(blueShip.hit or redShip.hit):
                    break
                #stop simulation if both ships are out of ammunition(missiles)
                if(blueShip.outOfMissiles() and redShip.outOfMissiles()):
                    break 
                #if(redShip.offensiveMissileTotal - redShip.omf <= 0):
                    #break
                #move ships if they are out of range
                blueShip.moveShip(redShip, animationFile, simulationTime)
                redShip.moveShip(blueShip, animationFile, simulationTime)
                
                #determine if there are target ships or missiles for the ships
                blueShip.findShipTargets(redShip)
                blueShip.findMissileTargets(redShip)
                redShip.findShipTargets(blueShip)
                redShip.findMissileTargets(blueShip)
            
                #check if any flying missiles have hit their targets
                blueShip.checkHitTargets(animationFile, simulationTime)
                redShip.checkHitTargets(animationFile, simulationTime)
    
                #move all flying missiles forward to next state according to 
                #time and speed
                blueShip.moveAllMissiles()
                redShip.moveAllMissiles()
 
                #increment the simulation time
                simulationTime = simulationTime + 0.25
                
            else:
                #checking for exit conditions
                #stop simulation if either ship is hit
                if(redShip.hit or blueShip.hit):
                    break
                #stop simulation if both ships are out of ammunition(missiles)
                if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
                    break 
                #if(redShip.offensiveMissileTotal - redShip.omf <= 0):
                    #break
                #move ships if they are out of range
                redShip.moveShip(blueShip, animationFile, simulationTime)
                blueShip.moveShip(redShip, animationFile, simulationTime)
                
                #determine if there are target ships or missiles for the ships
                redShip.findShipTargets(blueShip)
                redShip.findMissileTargets(blueShip)
                blueShip.findShipTargets(redShip)
                blueShip.findMissileTargets(redShip)
            
                #check if any flying missiles have hit their targets
                redShip.checkHitTargets(animationFile, simulationTime)
                blueShip.checkHitTargets(animationFile, simulationTime)
    
                #move all flying missiles forward to next state according to time and speed
                redShip.moveAllMissiles()
                blueShip.moveAllMissiles()
                
                #increment the simulation time
                simulationTime = simulationTime + 0.25
            
        animationFile.close()
        print("Iteration: " + str(i + 1))
        print()
        blueShip.printShip()
        redShip.printShip()
        #blueShip.printShipInputs(redShip)
        if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
            print("Both ships out of missiles")
            print()
        iterationArray4.append(i)
        simulationTimeArray4.append(simulationTime)
        BlueNumberOffensiveMissiles4.append(blueShip.omf)
        BlueNumberDefensiveMissiles4.append(blueShip.dmf)
        BlueNumberESSMs4.append(blueShip.essmf)
        BlueNumberSeaRAMs4.append(blueShip.seaRamf)
        BlueNumberCIWS4.append(blueShip.ciwsf)
        BlueShipOffensiveMissileRange4.append(blueShip.offensiveMissileRange)
        BlueShipHit4.append(blueShip.hit)
        BlueShipCost4.append(blueShip.engagementCost())
        BlueShipMissileCost4.append(blueShip.missileCost())
        RedNumberOffensiveMissiles4.append(redShip.omf)
        RedNumberDefensiveMissiles4.append(redShip.dmf)
        RedNumberESSMs4.append(redShip.essmf)
        RedNumberSeaRAMs4.append(redShip.seaRamf)
        RedNumberCIWS4.append(redShip.ciwsf)
        RedShipOffensiveMissileRange4.append(redShip.offensiveMissileRange)
        RedShipHit4.append(redShip.hit)
        RedShipCost4.append(redShip.engagementCost())
        RedShipMissileCost4.append(redShip.missileCost())
        ShipRange4.append(abs(blueShip.loc-redShip.loc))
        #print(redShip.satellite)
        #print(blueShip.satellite)
        
    #Number of simulation runs Blue Ship Hit
    BlueShipHitNumber4 = BlueShipHit4.count(True)
    #print(BlueShipHitNumber)
    #Proportion of total simulation runs that blue ship is hit (loses)
    BlueShipHitProp4 = BlueShipHitNumber4/len(BlueShipHit4)
    print("Proportion of Iterations Blue Ship Hit: " + str(BlueShipHitProp4))
    
    #Number of simulation runs Blue Ship Hit
    RedShipHitNumber4 = RedShipHit4.count(True)
    #print(RedShipHitNumber)
    #Proportion of total simulation runs that red ship is hit (loses)
    RedShipHitProp4 = RedShipHitNumber4/len(RedShipHit4)
    print("Proportion of Iterations Red Ship Hit: " + str(RedShipHitProp3))
    
    BothShipHitNumber4 = 0
    NoShipHitNumber4 = 0
    BlueShipHitNumber4 = 0
    RedShipHitNumber4 = 0
    for s in range(len(RedShipHit4)):
        if(RedShipHit4[s] == True and BlueShipHit4[s] == True):
            BothShipHitNumber4 = BothShipHitNumber4 + 1
        if(RedShipHit4[s] == False and BlueShipHit4[s] == False):
            NoShipHitNumber4 = NoShipHitNumber4 + 1
    
    intervals = len(RedShipHit)/10
    intervalsRedHitArr = []
    intervalsBlueHitArr = []
    intervalsRedHitArr2 = []
    intervalsBlueHitArr2 = []
    intervalsRedHitArr3 = []
    intervalsBlueHitArr3 = []
    intervalsRedHitArr4 = []
    intervalsBlueHitArr4 = []
    place = 0
    while(place < len(RedShipHit)):
        z = 0
        propIntervalRedArr = []
        propIntervalBlueArr = []
        propIntervalRedArr2 = []
        propIntervalBlueArr2 = []
        propIntervalRedArr3 = []
        propIntervalBlueArr3 = []
        propIntervalRedArr4 = []
        propIntervalBlueArr4 = []
        while(z < intervals):
            propIntervalRedArr.append(RedShipHit[place])
            propIntervalBlueArr.append(BlueShipHit[place])
            propIntervalRedArr2.append(RedShipHit2[place])
            propIntervalBlueArr2.append(BlueShipHit2[place])
            propIntervalRedArr3.append(RedShipHit3[place])
            propIntervalBlueArr3.append(BlueShipHit3[place])
            propIntervalRedArr4.append(RedShipHit4[place])
            propIntervalBlueArr4.append(BlueShipHit4[place])
            z = z + 1
            place = place + 1
        intervalsRedHitArr.append(np.mean(propIntervalRedArr))
        intervalsBlueHitArr.append(np.mean(propIntervalBlueArr))
        intervalsRedHitArr2.append(np.mean(propIntervalRedArr2))
        intervalsBlueHitArr2.append(np.mean(propIntervalBlueArr2))
        intervalsRedHitArr3.append(np.mean(propIntervalRedArr3))
        intervalsBlueHitArr3.append(np.mean(propIntervalBlueArr3))
        intervalsRedHitArr4.append(np.mean(propIntervalRedArr4))
        intervalsBlueHitArr4.append(np.mean(propIntervalBlueArr4))
    
    
    
    print("Both Off")
    print("Proportion of Iterations Blue Ship Hit: " + str(BlueShipHitProp))
    print("Proportion of Iterations Red Ship Hit: " + str(RedShipHitProp))
    print("Blue Off, Red On")
    print("Proportion of Iterations Blue Ship Hit: " + str(BlueShipHitProp2))
    print("Proportion of Iterations Red Ship Hit: " + str(RedShipHitProp2))
    print("Blue On, Red Off")
    print("Proportion of Iterations Blue Ship Hit: " + str(BlueShipHitProp3))
    print("Proportion of Iterations Red Ship Hit: " + str(RedShipHitProp3))
    print("Both On")
    print("Proportion of Iterations Blue Ship Hit: " + str(BlueShipHitProp4))
    print("Proportion of Iterations Red Ship Hit: " + str(RedShipHitProp4))
    print()
    
    print("Both Off")
    print("Median Blue Offensive Missiles Fired: " + str(np.median(BlueNumberOffensiveMissiles)) + " of total " + str(blueShip.offensiveMissileTotal))
    print("Average Blue Offensive Missiles Fired: " + str(np.mean(BlueNumberOffensiveMissiles)) + " of total " + str(blueShip.offensiveMissileTotal))
    print("Standard Deviation of Blue Offensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberOffensiveMissiles))))
    print("Median Red Offensive Missiles Fired: " + str(np.median(RedNumberOffensiveMissiles)) + " of total " + str(redShip.offensiveMissileTotal))
    print("Average Red Offensive Missiles Fired: " + str(np.mean(RedNumberOffensiveMissiles)) + " of total " + str(redShip.offensiveMissileTotal))
    print("Standard Deviation of Red Offensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberOffensiveMissiles))))
    print("Blue Off, Red On")
    print("Median Blue Offensive Missiles Fired: " + str(np.median(BlueNumberOffensiveMissiles2)) + " of total " + str(blueShip.offensiveMissileTotal))
    print("Average Blue Offensive Missiles Fired: " + str(np.mean(BlueNumberOffensiveMissiles2)) + " of total " + str(blueShip.offensiveMissileTotal))
    print("Standard Deviation of Blue Offensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberOffensiveMissiles2))))
    print("Median Red Offensive Missiles Fired: " + str(np.median(RedNumberOffensiveMissiles2)) + " of total " + str(redShip.offensiveMissileTotal))
    print("Average Red Offensive Missiles Fired: " + str(np.mean(RedNumberOffensiveMissiles2)) + " of total " + str(redShip.offensiveMissileTotal))
    print("Standard Deviation of Red Offensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberOffensiveMissiles2))))
    print("Blue On, Red Off")
    print("Median Blue Offensive Missiles Fired: " + str(np.median(BlueNumberOffensiveMissiles3)) + " of total " + str(blueShip.offensiveMissileTotal))
    print("Average Blue Offensive Missiles Fired: " + str(np.mean(BlueNumberOffensiveMissiles3)) + " of total " + str(blueShip.offensiveMissileTotal))
    print("Standard Deviation of Blue Offensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberOffensiveMissiles3))))
    print("Median Red Offensive Missiles Fired: " + str(np.median(RedNumberOffensiveMissiles3)) + " of total " + str(redShip.offensiveMissileTotal))
    print("Average Red Offensive Missiles Fired: " + str(np.mean(RedNumberOffensiveMissiles3)) + " of total " + str(redShip.offensiveMissileTotal))
    print("Standard Deviation of Red Offensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberOffensiveMissiles3))))
    print("Both On")
    print("Median Blue Offensive Missiles Fired: " + str(np.median(BlueNumberOffensiveMissiles4)) + " of total " + str(blueShip.offensiveMissileTotal))
    print("Average Blue Offensive Missiles Fired: " + str(np.mean(BlueNumberOffensiveMissiles4)) + " of total " + str(blueShip.offensiveMissileTotal))
    print("Standard Deviation of Blue Offensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberOffensiveMissiles4))))
    print("Median Red Offensive Missiles Fired: " + str(np.median(RedNumberOffensiveMissiles4)) + " of total " + str(redShip.offensiveMissileTotal))
    print("Average Red Offensive Missiles Fired: " + str(np.mean(RedNumberOffensiveMissiles4)) + " of total " + str(redShip.offensiveMissileTotal))
    print("Standard Deviation of Red Offensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberOffensiveMissiles4))))
    print()
    
    
    print("Both Off")
    print("Median Blue Defensive Missiles Fired: " + str(np.median(BlueNumberDefensiveMissiles)) + " of total " + str(blueShip.defensiveMissileTotal))
    print("Average Blue Defensive Missiles Fired: " + str(np.mean(BlueNumberDefensiveMissiles)) + " of total " + str(blueShip.defensiveMissileTotal))
    print("Standard Deviation of Blue Defensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberDefensiveMissiles))))
    print("Median Red Defensive Missiles Fired: " + str(np.median(RedNumberDefensiveMissiles)) + " of total " + str(redShip.defensiveMissileTotal))
    print("Average Red Defensive Missiles Fired: " + str(np.mean(RedNumberDefensiveMissiles)) + " of total " + str(redShip.defensiveMissileTotal))
    print("Standard Deviation of Red Defensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberDefensiveMissiles))))
    print("Blue Off, Red On")
    print("Median Blue Defensive Missiles Fired: " + str(np.median(BlueNumberDefensiveMissiles2)) + " of total " + str(blueShip.defensiveMissileTotal))
    print("Average Blue Defensive Missiles Fired: " + str(np.mean(BlueNumberDefensiveMissiles2)) + " of total " + str(blueShip.defensiveMissileTotal))
    print("Standard Deviation of Blue Defensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberDefensiveMissiles2))))
    print("Median Red Defensive Missiles Fired: " + str(np.median(RedNumberDefensiveMissiles2)) + " of total " + str(redShip.defensiveMissileTotal))
    print("Average Red Defensive Missiles Fired: " + str(np.mean(RedNumberDefensiveMissiles2)) + " of total " + str(redShip.defensiveMissileTotal))
    print("Standard Deviation of Red Defensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberDefensiveMissiles2))))
    print("Blue On, Red Off")
    print("Median Blue Defensive Missiles Fired: " + str(np.median(BlueNumberDefensiveMissiles3)) + " of total " + str(blueShip.defensiveMissileTotal))
    print("Average Blue Defensive Missiles Fired: " + str(np.mean(BlueNumberDefensiveMissiles3)) + " of total " + str(blueShip.defensiveMissileTotal))
    print("Standard Deviation of Blue Defensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberDefensiveMissiles3))))
    print("Median Red Defensive Missiles Fired: " + str(np.median(RedNumberDefensiveMissiles3)) + " of total " + str(redShip.defensiveMissileTotal))
    print("Average Red Defensive Missiles Fired: " + str(np.mean(RedNumberDefensiveMissiles3)) + " of total " + str(redShip.defensiveMissileTotal))
    print("Standard Deviation of Red Defensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberDefensiveMissiles3))))
    print("Both On")
    print("Median Blue Defensive Missiles Fired: " + str(np.median(BlueNumberDefensiveMissiles4)) + " of total " + str(blueShip.defensiveMissileTotal))
    print("Average Blue Defensive Missiles Fired: " + str(np.mean(BlueNumberDefensiveMissiles4)) + " of total " + str(blueShip.defensiveMissileTotal))
    print("Standard Deviation of Blue Defensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberDefensiveMissiles4))))
    print("Median Red Defensive Missiles Fired: " + str(np.median(RedNumberDefensiveMissiles4)) + " of total " + str(redShip.defensiveMissileTotal))
    print("Average Red Defensive Missiles Fired: " + str(np.mean(RedNumberDefensiveMissiles4)) + " of total " + str(redShip.defensiveMissileTotal))
    print("Standard Deviation of Red Defensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberDefensiveMissiles4))))
    print()
    
    print("Both Off")
    print("Median Blue Cost: " + '{:,.2f}'.format(np.median(BlueShipCost)))
    print("Average Blue Cost: " + '{:,.2f}'.format(np.mean(BlueShipCost)))
    print("Standard Deviation of Blue Cost: " + '{:,.2f}'.format(np.sqrt(np.var(BlueShipCost))))
    print("Median Red Cost: " + '{:,.2f}'.format(np.median(RedShipCost)))
    print("Average Red Cost: " + '{:,.2f}'.format(np.mean(RedShipCost)))
    print("Standard Deviation of Red Cost: " + '{:,.2f}'.format(np.sqrt(np.var(RedShipCost))))
    print("Blue Off, Red On")
    print("Median Blue Cost: " + '{:,.2f}'.format(np.median(BlueShipCost2)))
    print("Average Blue Cost: " + '{:,.2f}'.format(np.mean(BlueShipCost2)))
    print("Standard Deviation of Blue Cost: " + '{:,.2f}'.format(np.sqrt(np.var(BlueShipCost2))))
    print("Median Red Cost: " + '{:,.2f}'.format(np.median(RedShipCost2)))
    print("Average Red Cost: " + '{:,.2f}'.format(np.mean(RedShipCost2)))
    print("Standard Deviation of Red Cost: " + '{:,.2f}'.format(np.sqrt(np.var(RedShipCost2))))
    print("Blue On, Red Off")
    print("Median Blue Cost: " + '{:,.2f}'.format(np.median(BlueShipCost3)))
    print("Average Blue Cost: " + '{:,.2f}'.format(np.mean(BlueShipCost3)))
    print("Standard Deviation of Blue Cost: " + '{:,.2f}'.format(np.sqrt(np.var(BlueShipCost3))))
    print("Median Red Cost: " + '{:,.2f}'.format(np.median(RedShipCost3)))
    print("Average Red Cost: " + '{:,.2f}'.format(np.mean(RedShipCost3)))
    print("Standard Deviation of Red Cost: " + '{:,.2f}'.format(np.sqrt(np.var(RedShipCost3))))
    print("Both On")
    print("Median Blue Cost: " + '{:,.2f}'.format(np.median(BlueShipCost4)))
    print("Average Blue Cost: " + '{:,.2f}'.format(np.mean(BlueShipCost4)))
    print("Standard Deviation of Blue Cost: " + '{:,.2f}'.format(np.sqrt(np.var(BlueShipCost4))))
    print("Median Red Cost: " + '{:,.2f}'.format(np.median(RedShipCost4)))
    print("Average Red Cost: " + '{:,.2f}'.format(np.mean(RedShipCost4)))
    print("Standard Deviation of Red Cost: " + '{:,.2f}'.format(np.sqrt(np.var(RedShipCost4))))
    print()
  
    
    
    
    #create box-plot
    #Code adapted from link below
    #http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    data_to_plot = [intervalsBlueHitArr, intervalsRedHitArr, 
                    intervalsBlueHitArr2, intervalsRedHitArr2, 
                    intervalsBlueHitArr3, intervalsRedHitArr3, 
                    intervalsBlueHitArr4, intervalsRedHitArr4]
    fig = plt.figure(1, figsize=(10, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    bp['boxes'][0].set( color='midnightblue', linewidth=2)
    bp['boxes'][0].set( facecolor = 'blue' )
    bp['boxes'][1].set( color='darkred', linewidth=2)
    bp['boxes'][1].set( facecolor = 'red' )
    bp['boxes'][2].set( color='midnightblue', linewidth=2)
    bp['boxes'][2].set( facecolor = 'blue' )
    bp['boxes'][3].set( color='darkred', linewidth=2)
    bp['boxes'][3].set( facecolor = 'red' )
    bp['boxes'][4].set( color='midnightblue', linewidth=2)
    bp['boxes'][4].set( facecolor = 'blue' )
    bp['boxes'][5].set( color='darkred', linewidth=2)
    bp['boxes'][5].set( facecolor = 'red' )
    bp['boxes'][6].set( color='midnightblue', linewidth=2)
    bp['boxes'][6].set( facecolor = 'blue' )
    bp['boxes'][7].set( color='darkred', linewidth=2)
    bp['boxes'][7].set( facecolor = 'red' )
    ## change color and linewidth of the whiskers
    bp['whiskers'][0].set(color='midnightblue', linewidth=2)
    bp['whiskers'][1].set(color='midnightblue', linewidth=2)
    bp['whiskers'][2].set(color='darkred', linewidth=2)
    bp['whiskers'][3].set(color='darkred', linewidth=2)
    bp['whiskers'][4].set(color='midnightblue', linewidth=2)
    bp['whiskers'][5].set(color='midnightblue', linewidth=2)
    bp['whiskers'][6].set(color='darkred', linewidth=2)
    bp['whiskers'][7].set(color='darkred', linewidth=2)
    bp['whiskers'][8].set(color='midnightblue', linewidth=2)
    bp['whiskers'][9].set(color='midnightblue', linewidth=2)
    bp['whiskers'][10].set(color='darkred', linewidth=2)
    bp['whiskers'][11].set(color='darkred', linewidth=2)
    bp['whiskers'][12].set(color='midnightblue', linewidth=2)
    bp['whiskers'][13].set(color='midnightblue', linewidth=2)
    bp['whiskers'][14].set(color='darkred', linewidth=2)
    bp['whiskers'][15].set(color='darkred', linewidth=2)
    ## change color and linewidth of the caps
    bp['caps'][0].set(color='midnightblue', linewidth=2)
    bp['caps'][1].set(color='midnightblue', linewidth=2)
    bp['caps'][2].set(color='darkred', linewidth=2)
    bp['caps'][3].set(color='darkred', linewidth=2)
    bp['caps'][4].set(color='midnightblue', linewidth=2)
    bp['caps'][5].set(color='midnightblue', linewidth=2)
    bp['caps'][6].set(color='darkred', linewidth=2)
    bp['caps'][7].set(color='darkred', linewidth=2)
    bp['caps'][8].set(color='midnightblue', linewidth=2)
    bp['caps'][9].set(color='midnightblue', linewidth=2)
    bp['caps'][10].set(color='darkred', linewidth=2)
    bp['caps'][11].set(color='darkred', linewidth=2)
    bp['caps'][12].set(color='midnightblue', linewidth=2)
    bp['caps'][13].set(color='midnightblue', linewidth=2)
    bp['caps'][14].set(color='darkred', linewidth=2)
    bp['caps'][15].set(color='darkred', linewidth=2)
    ## change color and linewidth of the medians
    bp['medians'][0].set(color='paleturquoise', linewidth=2)
    bp['medians'][1].set(color='mistyrose', linewidth=2)
    bp['medians'][2].set(color='paleturquoise', linewidth=2)
    bp['medians'][3].set(color='mistyrose', linewidth=2)
    bp['medians'][4].set(color='paleturquoise', linewidth=2)
    bp['medians'][5].set(color='mistyrose', linewidth=2)
    bp['medians'][6].set(color='paleturquoise', linewidth=2)
    bp['medians'][7].set(color='mistyrose', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)            
    ## Custom x-axis labels
    ax.set_xticklabels(['Both Off','Both Off','Blue Off,\n Red On','Blue Off,\n Red On', 'Blue On,\n Red Off','Blue On,\n Red Off', 'Both On','Both On'])
    ax.set_xlabel('Satellite Capabilities On/Off')
    ax.set_title('Proportion of Iterations Ship Hit over 1,000 Simulations')
    ax.set_ylabel('Proportion Hit (groups of 100 simulations)')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    fig.savefig('boxPlotShipHitSatellite.png', bbox_inches='tight', dpi=600)
    plt.show()
    
    
    #create box-plot
    #Code adapted from link below
    #http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    data_to_plot = [BlueNumberOffensiveMissiles, RedNumberOffensiveMissiles, 
                    BlueNumberOffensiveMissiles2, RedNumberOffensiveMissiles2,
                    BlueNumberOffensiveMissiles3, RedNumberOffensiveMissiles3,
                    BlueNumberOffensiveMissiles4, RedNumberOffensiveMissiles4]
    fig = plt.figure(1, figsize=(10, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    bp['boxes'][0].set( color='midnightblue', linewidth=2)
    bp['boxes'][0].set( facecolor = 'blue' )
    bp['boxes'][1].set( color='darkred', linewidth=2)
    bp['boxes'][1].set( facecolor = 'red' )
    bp['boxes'][2].set( color='midnightblue', linewidth=2)
    bp['boxes'][2].set( facecolor = 'blue' )
    bp['boxes'][3].set( color='darkred', linewidth=2)
    bp['boxes'][3].set( facecolor = 'red' )
    bp['boxes'][4].set( color='midnightblue', linewidth=2)
    bp['boxes'][4].set( facecolor = 'blue' )
    bp['boxes'][5].set( color='darkred', linewidth=2)
    bp['boxes'][5].set( facecolor = 'red' )
    bp['boxes'][6].set( color='midnightblue', linewidth=2)
    bp['boxes'][6].set( facecolor = 'blue' )
    bp['boxes'][7].set( color='darkred', linewidth=2)
    bp['boxes'][7].set( facecolor = 'red' )
    ## change color and linewidth of the whiskers
    bp['whiskers'][0].set(color='midnightblue', linewidth=2)
    bp['whiskers'][1].set(color='midnightblue', linewidth=2)
    bp['whiskers'][2].set(color='darkred', linewidth=2)
    bp['whiskers'][3].set(color='darkred', linewidth=2)
    bp['whiskers'][4].set(color='midnightblue', linewidth=2)
    bp['whiskers'][5].set(color='midnightblue', linewidth=2)
    bp['whiskers'][6].set(color='darkred', linewidth=2)
    bp['whiskers'][7].set(color='darkred', linewidth=2)
    bp['whiskers'][8].set(color='midnightblue', linewidth=2)
    bp['whiskers'][9].set(color='midnightblue', linewidth=2)
    bp['whiskers'][10].set(color='darkred', linewidth=2)
    bp['whiskers'][11].set(color='darkred', linewidth=2)
    bp['whiskers'][12].set(color='midnightblue', linewidth=2)
    bp['whiskers'][13].set(color='midnightblue', linewidth=2)
    bp['whiskers'][14].set(color='darkred', linewidth=2)
    bp['whiskers'][15].set(color='darkred', linewidth=2)
    ## change color and linewidth of the caps
    bp['caps'][0].set(color='midnightblue', linewidth=2)
    bp['caps'][1].set(color='midnightblue', linewidth=2)
    bp['caps'][2].set(color='darkred', linewidth=2)
    bp['caps'][3].set(color='darkred', linewidth=2)
    bp['caps'][4].set(color='midnightblue', linewidth=2)
    bp['caps'][5].set(color='midnightblue', linewidth=2)
    bp['caps'][6].set(color='darkred', linewidth=2)
    bp['caps'][7].set(color='darkred', linewidth=2)
    bp['caps'][8].set(color='midnightblue', linewidth=2)
    bp['caps'][9].set(color='midnightblue', linewidth=2)
    bp['caps'][10].set(color='darkred', linewidth=2)
    bp['caps'][11].set(color='darkred', linewidth=2)
    bp['caps'][12].set(color='midnightblue', linewidth=2)
    bp['caps'][13].set(color='midnightblue', linewidth=2)
    bp['caps'][14].set(color='darkred', linewidth=2)
    bp['caps'][15].set(color='darkred', linewidth=2)
    ## change color and linewidth of the medians
    bp['medians'][0].set(color='paleturquoise', linewidth=2)
    bp['medians'][1].set(color='mistyrose', linewidth=2)
    bp['medians'][2].set(color='paleturquoise', linewidth=2)
    bp['medians'][3].set(color='mistyrose', linewidth=2)
    bp['medians'][4].set(color='paleturquoise', linewidth=2)
    bp['medians'][5].set(color='mistyrose', linewidth=2)
    bp['medians'][6].set(color='paleturquoise', linewidth=2)
    bp['medians'][7].set(color='mistyrose', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)            
    ## Custom x-axis labels
    ax.set_xticklabels(['Both Off','Both Off','Blue Off,\n Red On','Blue Off,\n Red On', 'Blue On,\n Red Off','Blue On,\n Red Off', 'Both On','Both On'])
    ax.set_xlabel('Satellite Capabilities On/Off')
    ax.set_title('Offensive Missiles Fired over 1,000 Simulations')
    ax.set_ylabel('Number of Missiles')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    fig.savefig('boxPlotOffensiveSatellite.png', bbox_inches='tight', dpi=600)
    plt.show()
    
    #create box-plot
    #Code adapted from link below
    #http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    data_to_plot = [BlueNumberDefensiveMissiles, RedNumberDefensiveMissiles, 
                    BlueNumberDefensiveMissiles2, RedNumberDefensiveMissiles2,
                    BlueNumberDefensiveMissiles3, RedNumberDefensiveMissiles3,
                    BlueNumberDefensiveMissiles4, RedNumberDefensiveMissiles4]
    fig = plt.figure(1, figsize=(10, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    bp['boxes'][0].set( color='midnightblue', linewidth=2)
    bp['boxes'][0].set( facecolor = 'blue' )
    bp['boxes'][1].set( color='darkred', linewidth=2)
    bp['boxes'][1].set( facecolor = 'red' )
    bp['boxes'][2].set( color='midnightblue', linewidth=2)
    bp['boxes'][2].set( facecolor = 'blue' )
    bp['boxes'][3].set( color='darkred', linewidth=2)
    bp['boxes'][3].set( facecolor = 'red' )
    bp['boxes'][4].set( color='midnightblue', linewidth=2)
    bp['boxes'][4].set( facecolor = 'blue' )
    bp['boxes'][5].set( color='darkred', linewidth=2)
    bp['boxes'][5].set( facecolor = 'red' )
    bp['boxes'][6].set( color='midnightblue', linewidth=2)
    bp['boxes'][6].set( facecolor = 'blue' )
    bp['boxes'][7].set( color='darkred', linewidth=2)
    bp['boxes'][7].set( facecolor = 'red' )
    ## change color and linewidth of the whiskers
    bp['whiskers'][0].set(color='midnightblue', linewidth=2)
    bp['whiskers'][1].set(color='midnightblue', linewidth=2)
    bp['whiskers'][2].set(color='darkred', linewidth=2)
    bp['whiskers'][3].set(color='darkred', linewidth=2)
    bp['whiskers'][4].set(color='midnightblue', linewidth=2)
    bp['whiskers'][5].set(color='midnightblue', linewidth=2)
    bp['whiskers'][6].set(color='darkred', linewidth=2)
    bp['whiskers'][7].set(color='darkred', linewidth=2)
    bp['whiskers'][8].set(color='midnightblue', linewidth=2)
    bp['whiskers'][9].set(color='midnightblue', linewidth=2)
    bp['whiskers'][10].set(color='darkred', linewidth=2)
    bp['whiskers'][11].set(color='darkred', linewidth=2)
    bp['whiskers'][12].set(color='midnightblue', linewidth=2)
    bp['whiskers'][13].set(color='midnightblue', linewidth=2)
    bp['whiskers'][14].set(color='darkred', linewidth=2)
    bp['whiskers'][15].set(color='darkred', linewidth=2)
    ## change color and linewidth of the caps
    bp['caps'][0].set(color='midnightblue', linewidth=2)
    bp['caps'][1].set(color='midnightblue', linewidth=2)
    bp['caps'][2].set(color='darkred', linewidth=2)
    bp['caps'][3].set(color='darkred', linewidth=2)
    bp['caps'][4].set(color='midnightblue', linewidth=2)
    bp['caps'][5].set(color='midnightblue', linewidth=2)
    bp['caps'][6].set(color='darkred', linewidth=2)
    bp['caps'][7].set(color='darkred', linewidth=2)
    bp['caps'][8].set(color='midnightblue', linewidth=2)
    bp['caps'][9].set(color='midnightblue', linewidth=2)
    bp['caps'][10].set(color='darkred', linewidth=2)
    bp['caps'][11].set(color='darkred', linewidth=2)
    bp['caps'][12].set(color='midnightblue', linewidth=2)
    bp['caps'][13].set(color='midnightblue', linewidth=2)
    bp['caps'][14].set(color='darkred', linewidth=2)
    bp['caps'][15].set(color='darkred', linewidth=2)
    ## change color and linewidth of the medians
    bp['medians'][0].set(color='paleturquoise', linewidth=2)
    bp['medians'][1].set(color='mistyrose', linewidth=2)
    bp['medians'][2].set(color='paleturquoise', linewidth=2)
    bp['medians'][3].set(color='mistyrose', linewidth=2)
    bp['medians'][4].set(color='paleturquoise', linewidth=2)
    bp['medians'][5].set(color='mistyrose', linewidth=2)
    bp['medians'][6].set(color='paleturquoise', linewidth=2)
    bp['medians'][7].set(color='mistyrose', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)            
    ## Custom x-axis labels
    ax.set_xticklabels(['Both Off','Both Off','Blue Off,\n Red On','Blue Off,\n Red On', 'Blue On,\n Red Off','Blue On,\n Red Off', 'Both On','Both On'])
    ax.set_xlabel('Satellite Capabilities On/Off')
    ax.set_title('Defensive Missiles Fired over 1,000 Simulations')
    ax.set_ylabel('Number of Missiles')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    fig.savefig('boxPlotDefensiveSatellite.png', bbox_inches='tight', dpi=600)
    plt.show()
    
    #create box-plot
    #Code adapted from link below
    #http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    data_to_plot = [BlueShipCost, RedShipCost, 
                    BlueShipCost2, RedShipCost2, 
                    BlueShipCost3, RedShipCost3, 
                    BlueShipCost4, RedShipCost4]
    fig = plt.figure(1, figsize=(10, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    bp['boxes'][0].set( color='midnightblue', linewidth=2)
    bp['boxes'][0].set( facecolor = 'blue' )
    bp['boxes'][1].set( color='darkred', linewidth=2)
    bp['boxes'][1].set( facecolor = 'red' )
    bp['boxes'][2].set( color='midnightblue', linewidth=2)
    bp['boxes'][2].set( facecolor = 'blue' )
    bp['boxes'][3].set( color='darkred', linewidth=2)
    bp['boxes'][3].set( facecolor = 'red' )
    bp['boxes'][4].set( color='midnightblue', linewidth=2)
    bp['boxes'][4].set( facecolor = 'blue' )
    bp['boxes'][5].set( color='darkred', linewidth=2)
    bp['boxes'][5].set( facecolor = 'red' )
    bp['boxes'][6].set( color='midnightblue', linewidth=2)
    bp['boxes'][6].set( facecolor = 'blue' )
    bp['boxes'][7].set( color='darkred', linewidth=2)
    bp['boxes'][7].set( facecolor = 'red' )
    ## change color and linewidth of the whiskers
    bp['whiskers'][0].set(color='midnightblue', linewidth=2)
    bp['whiskers'][1].set(color='midnightblue', linewidth=2)
    bp['whiskers'][2].set(color='darkred', linewidth=2)
    bp['whiskers'][3].set(color='darkred', linewidth=2)
    bp['whiskers'][4].set(color='midnightblue', linewidth=2)
    bp['whiskers'][5].set(color='midnightblue', linewidth=2)
    bp['whiskers'][6].set(color='darkred', linewidth=2)
    bp['whiskers'][7].set(color='darkred', linewidth=2)
    bp['whiskers'][8].set(color='midnightblue', linewidth=2)
    bp['whiskers'][9].set(color='midnightblue', linewidth=2)
    bp['whiskers'][10].set(color='darkred', linewidth=2)
    bp['whiskers'][11].set(color='darkred', linewidth=2)
    bp['whiskers'][12].set(color='midnightblue', linewidth=2)
    bp['whiskers'][13].set(color='midnightblue', linewidth=2)
    bp['whiskers'][14].set(color='darkred', linewidth=2)
    bp['whiskers'][15].set(color='darkred', linewidth=2)
    ## change color and linewidth of the caps
    bp['caps'][0].set(color='midnightblue', linewidth=2)
    bp['caps'][1].set(color='midnightblue', linewidth=2)
    bp['caps'][2].set(color='darkred', linewidth=2)
    bp['caps'][3].set(color='darkred', linewidth=2)
    bp['caps'][4].set(color='midnightblue', linewidth=2)
    bp['caps'][5].set(color='midnightblue', linewidth=2)
    bp['caps'][6].set(color='darkred', linewidth=2)
    bp['caps'][7].set(color='darkred', linewidth=2)
    bp['caps'][8].set(color='midnightblue', linewidth=2)
    bp['caps'][9].set(color='midnightblue', linewidth=2)
    bp['caps'][10].set(color='darkred', linewidth=2)
    bp['caps'][11].set(color='darkred', linewidth=2)
    bp['caps'][12].set(color='midnightblue', linewidth=2)
    bp['caps'][13].set(color='midnightblue', linewidth=2)
    bp['caps'][14].set(color='darkred', linewidth=2)
    bp['caps'][15].set(color='darkred', linewidth=2)
    ## change color and linewidth of the medians
    bp['medians'][0].set(color='paleturquoise', linewidth=2)
    bp['medians'][1].set(color='mistyrose', linewidth=2)
    bp['medians'][2].set(color='paleturquoise', linewidth=2)
    bp['medians'][3].set(color='mistyrose', linewidth=2)
    bp['medians'][4].set(color='paleturquoise', linewidth=2)
    bp['medians'][5].set(color='mistyrose', linewidth=2)
    bp['medians'][6].set(color='paleturquoise', linewidth=2)
    bp['medians'][7].set(color='mistyrose', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)            
    ## Custom x-axis labels
    ax.set_xticklabels(['Both Off','Both Off','Blue Off,\n Red On','Blue Off,\n Red On', 'Blue On,\n Red Off','Blue On,\n Red Off', 'Both On','Both On'])
    ax.set_xlabel('Satellite Capabilities On/Off')
    ax.set_title('Total Engagement Cost over 1,000 Simulations')
    ax.set_ylabel('Cost (USD)')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    fig.savefig('boxPlotCostSatellite.png', bbox_inches='tight', dpi=600)
    plt.show()
    
    
           

    
    
    
    
    