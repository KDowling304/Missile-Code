#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:14:19 2019

@author: karadowling
code adapted from ORF 411 AssetSelling problem code found at link below
https://github.com/wbpowell328/stochastic-optimization/tree/master/AssetSelling

This is a single simulation of a two-agent surface ship missile engagement.  
The simulation starts with one or both of the ships firing offensive missiles and ends when 
either ship is hit by a missle or both ships are out of missiles.

Use the output animationFile.txt from this script to use in the Java visual simulation.
"""

#from collections import namedtuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
    print("Time step each iteration is " + str(timeStep) + " minutes")
    print('')
    
    #Initialize Ships
    blueShip = Ship(sheet1['Ship\'s Name'][0], sheet1['Location (NM) 1D scale'][0], 
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
                sheet1['UAV'][0], sheet1['USV'][0])
    redShip = Ship(sheet1['Ship\'s Name'][1], sheet1['Location (NM) 1D scale'][1], 
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
                sheet1['UAV'][1], sheet1['USV'][1])
    
    #Print Initialized Ships
    #redShip.printShip()
    #blueShip.printShip()
   
    #not incorporated yet
    #Weather affects scouting effectiveness
    goodWeather = False #bad weather (True is good weather)
    
    #Create Plot List for Missile Count Over Time
    simulationTimeArray = [] #
    BlueNumberOffensiveMissiles = []
    BlueNumberDefensiveMissiles = []
    BlueNumberESSMs = []
    BlueNumberSeaRAMs = []
    BlueNumberCIWS = []
    BlueShipOffensiveMissileRange = []
    BlueCost = []
    BlueShipLoc = []
    RedNumberOffensiveMissiles = []
    RedNumberDefensiveMissiles = []
    RedNumberESSMs = []
    RedNumberSeaRAMs = []
    RedNumberCIWS = []
    RedShipOffensiveMissileRange = []
    RedCost = []
    RedShipLoc = []
    ShipRange = []
    simulationTimeArray.append(0)
    BlueNumberOffensiveMissiles.append(blueShip.offensiveMissileTotal)
    BlueNumberDefensiveMissiles.append(blueShip.defensiveMissileTotal)
    BlueNumberESSMs.append(blueShip.essmTotal)
    BlueNumberSeaRAMs.append(blueShip.seaRamTotal)
    BlueNumberCIWS.append(blueShip.ciwsTotal)
    BlueShipOffensiveMissileRange.append(blueShip.offensiveMissileRange)
    BlueCost.append(0)
    BlueShipLoc.append(blueShip.loc)
    RedNumberOffensiveMissiles.append(redShip.offensiveMissileTotal)
    RedNumberDefensiveMissiles.append(redShip.defensiveMissileTotal)
    RedNumberESSMs.append(redShip.essmTotal)
    RedNumberSeaRAMs.append(redShip.seaRamTotal)
    RedNumberCIWS.append(redShip.ciwsTotal)
    RedShipOffensiveMissileRange.append(redShip.offensiveMissileRange)
    RedCost.append(0)
    RedShipLoc.append(redShip.loc)
    ShipRange.append(abs(redShip.loc-blueShip.loc))
    
    
    #Run Missile Simulation
    #keeps track of iterations that are representative of minutes
    simulationTime = 0.25 #in minutes
    #simulation ends when certain time passes to ensure no infinite loop can occur
    animationFile = open("animationFile.txt", "w")
    
    while(simulationTime <= 1000):
        
        #determines whether Blue or Red goes first each time step
        BlueFirst = np.random.binomial(1,0.5)
        #print(BlueFirst)
        
        if(BlueFirst == 1):
            #checking for exit conditions
            #stop simulation if either ship is hit
            if(redShip.hit or blueShip.hit):
                break
            #stop simulation if both ships are out of ammunition(missiles)
            if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
                print("Both ships out of missiles")
                print()
                break 
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
            #print the time elapsed in the simulation
            print("Time Elapsed: " + str(simulationTime))
            print('')
            #print the ship summaries
            blueShip.printShip()
            redShip.printShip()
            print('')
            simulationTimeArray.append(simulationTime)
            BlueNumberOffensiveMissiles.append(blueShip.offensiveMissileTotal - blueShip.omf)
            BlueNumberDefensiveMissiles.append(blueShip.defensiveMissileTotal - blueShip.dmf)
            BlueNumberESSMs.append(blueShip.essmTotal - blueShip.essmf)
            BlueNumberSeaRAMs.append(blueShip.seaRamTotal - blueShip.seaRamf)
            BlueNumberCIWS.append(blueShip.ciwsTotal - blueShip.ciwsf)
            BlueShipOffensiveMissileRange.append(blueShip.offensiveMissileRange)
            BlueCost.append(blueShip.engagementCost())
            BlueShipLoc.append(blueShip.loc)
            RedNumberOffensiveMissiles.append(redShip.offensiveMissileTotal - redShip.omf)
            RedNumberDefensiveMissiles.append(redShip.defensiveMissileTotal - redShip.dmf)
            RedNumberESSMs.append(redShip.essmTotal - redShip.essmf)
            RedNumberSeaRAMs.append(redShip.seaRamTotal - redShip.seaRamf)
            RedNumberCIWS.append(redShip.ciwsTotal - redShip.ciwsf)
            RedShipOffensiveMissileRange.append(redShip.offensiveMissileRange)
            RedCost.append(redShip.engagementCost())
            RedShipLoc.append(redShip.loc)
            ShipRange.append(abs(redShip.loc-blueShip.loc))
            #move all flying missiles forward to next state according to time and speed
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
                print("Both ships out of missiles")
                print()
                break 
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
            #print the time elapsed in the simulation
            print("Time Elapsed: " + str(simulationTime))
            print('')
            #print the ship summaries
            blueShip.printShip()
            redShip.printShip()
            print('')
            simulationTimeArray.append(simulationTime)
            BlueNumberOffensiveMissiles.append(blueShip.offensiveMissileTotal - blueShip.omf)
            BlueNumberDefensiveMissiles.append(blueShip.defensiveMissileTotal - blueShip.dmf)
            BlueNumberESSMs.append(blueShip.essmTotal - blueShip.essmf)
            BlueNumberSeaRAMs.append(blueShip.seaRamTotal - blueShip.seaRamf)
            BlueNumberCIWS.append(blueShip.ciwsTotal - blueShip.ciwsf)
            BlueShipOffensiveMissileRange.append(blueShip.offensiveMissileRange)
            BlueCost.append(blueShip.engagementCost())
            BlueShipLoc.append(blueShip.loc)
            RedNumberOffensiveMissiles.append(redShip.offensiveMissileTotal - redShip.omf)
            RedNumberDefensiveMissiles.append(redShip.defensiveMissileTotal - redShip.dmf)
            RedNumberESSMs.append(redShip.essmTotal - redShip.essmf)
            RedNumberSeaRAMs.append(redShip.seaRamTotal - redShip.seaRamf)
            RedNumberCIWS.append(redShip.ciwsTotal - redShip.ciwsf)
            RedShipOffensiveMissileRange.append(redShip.offensiveMissileRange)
            RedCost.append(redShip.engagementCost())
            RedShipLoc.append(redShip.loc)
            ShipRange.append(abs(redShip.loc-blueShip.loc))
            #move all flying missiles forward to next state according to time and speed
            redShip.moveAllMissiles()
            blueShip.moveAllMissiles()
            #increment the simulation time
            simulationTime = simulationTime + 0.25
    animationFile.close()
 
    plt.plot(simulationTimeArray, BlueNumberOffensiveMissiles, color='blue', label='Blue Ship')
    plt.plot(simulationTimeArray, RedNumberOffensiveMissiles, color='red', label='Red Ship')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('Offensive Missiles Left')
    plt.title('Offensive Missiles Left in Ships\' Arsenals over Time')
    plt.savefig('OffensiveMissilesOverTime.png', dpi=600)
    plt.show()
    
    plt.plot(simulationTimeArray, BlueNumberDefensiveMissiles, color='blue', label='Blue Ship')
    plt.plot(simulationTimeArray, RedNumberDefensiveMissiles, color='red', label='Red Ship')
    plt.legend()
    #plt.ylim((0, 5 + max(redShip.defensiveMissileTotal, blueShip.defensiveMissileTotal)))
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('Defensive Missiles Left')
    plt.title('Defensive Missiles Left in Ships\' Arsenals over Time')
    plt.savefig('DefensiveMissilesOverTime.png', dpi=600)
    plt.show()
    
    plt.plot(simulationTimeArray, BlueNumberESSMs, color='blue', label='Blue Ship')
    plt.plot(simulationTimeArray, RedNumberESSMs, color='red', label='Red Ship')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('ESSMs Left')
    plt.title('ESSMs Left in Ships\' Arsenals over Time')
    plt.savefig('ESSMs.png', dpi=600)
    plt.show()
    
    plt.plot(simulationTimeArray, BlueNumberSeaRAMs, color='blue', label='Blue Ship')
    plt.plot(simulationTimeArray, RedNumberSeaRAMs, color='red', label='Red Ship')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('SeaRAMs Left')
    plt.title('SeaRAMs Left in Ships\' Arsenals over Time')
    plt.savefig('SeaRAMs.png', dpi=600)
    plt.show()
    
    plt.plot(simulationTimeArray, BlueNumberCIWS, color='blue', label='Blue Ship')
    plt.plot(simulationTimeArray, RedNumberCIWS, color='red', label='Red Ship')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('CIWS Left')
    plt.title('CIWS Left in Ships\' Arsenals over Time')
    plt.savefig('CIWS.png', dpi=600)
    plt.show()
    
    plt.plot(simulationTimeArray, BlueShipOffensiveMissileRange, color='blue', label='Blue Offensive Missile Range')
    plt.plot(simulationTimeArray, RedShipOffensiveMissileRange, color='red', label='Red Offensive Missile Range')
    plt.plot(simulationTimeArray, ShipRange, color='black', label='Range Between Ships over Time')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('Range (NM)')
    plt.title('Distance between Red and Blue Ships')
    plt.savefig('ShipDistance.png', dpi=600)
    plt.show()
    
    plt.plot(simulationTimeArray, BlueShipLoc, color='blue', label='Location of Blue Ship')
    plt.plot(simulationTimeArray, RedShipLoc, color='red', label='Location of Red Ship')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('Location on 1D scale (NM)')
    plt.title('Location of Ships over Time')
    plt.savefig('ShipLocation.png', dpi=600)
    plt.show()
    
    plt.plot(simulationTimeArray, BlueCost, color='blue', label='Blue')
    plt.plot(simulationTimeArray, RedCost, color='red', label='Red')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('Cost (USD)')
    plt.title('Missile Engagement Cost over Time')
    plt.savefig('Cost.png', dpi=600)
    plt.show()
    
    
    
    
        
    
    
    
    
    