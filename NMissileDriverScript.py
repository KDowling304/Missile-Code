#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:14:19 2019

@author: karadowling
code adapted from ORF 411 AssetSelling problem code found at link below
https://github.com/wbpowell328/stochastic-optimization/tree/master/AssetSelling

This is a simulation of a two-agent surface ship missile engagement.  
The simulation starts with the Red Ship firing at the Blue Ship and ends when 
either ship is hit by a missle or both ships are out of missiles.
"""

#from collections import namedtuple
import pandas as pd
#import numpy as np
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
    #print("Time step each iteration is " + str(timeStep) + " minutes")
    #print('')
    
    iterations = sheet2['Iterations of Simulation'][0]
    print("Simulation Iterations: " + str(iterations) + "\n")
    
    #initial data blueShip
    initialBlue = [sheet1['Ship\'s Name'][0], sheet1['Location (NM) 1D scale'][0], 
                sheet1['Offensive Missiles'][0], sheet1['Defensive Missiles'][0],
                sheet1['ESSMs'][0], sheet1['Sea RAMs'][0], 
                sheet1['CIWS (each has 3000 rounds)'][0],
                sheet1['Ship Speed (kn)'][0], sheet1['Missile Speed (kn)'][0], 
                timeStep, sheet1['Offensive Missile Range (NM)'][0], 
                sheet1['Offensive Missile Success Probability'][0],
                sheet1['Defensive Missile Success Probability (if target offensive missile is 100-20 NM from its target - phase 1)'][0],
                sheet1['Defensive Missile Success Probability (if target offensive missile is 20-5 NM from its target - phase 2)'][0],
                sheet1['Defensive Missile Success Probability (if target offensive missile is 5-1 NM from its target - phase 3)'][0],
                sheet1['ESSM Success Probability'][0],
                sheet1['Sea RAM Success Probability'][0],
                sheet1['CIWS Success Probability'][0],
                sheet1['Satellite'][0], sheet1['Radar'][0], 
                sheet1['Electronic Surveillance'][0], 
                sheet1['Passive Sensors (Acoustic)'][0],
                sheet1['UAV'][0], sheet1['USV'][0]]
    
    initialRed = [sheet1['Ship\'s Name'][1], sheet1['Location (NM) 1D scale'][1], 
                sheet1['Offensive Missiles'][1], sheet1['Defensive Missiles'][1], 
                sheet1['ESSMs'][1], sheet1['Sea RAMs'][1], 
                sheet1['CIWS (each has 3000 rounds)'][1],
                sheet1['Ship Speed (kn)'][1], sheet1['Missile Speed (kn)'][1], 
                timeStep, sheet1['Offensive Missile Range (NM)'][1], 
                sheet1['Offensive Missile Success Probability'][1],
                sheet1['Defensive Missile Success Probability (if target offensive missile is 100-20 NM from its target - phase 1)'][1],
                sheet1['Defensive Missile Success Probability (if target offensive missile is 20-5 NM from its target - phase 2)'][1],
                sheet1['Defensive Missile Success Probability (if target offensive missile is 5-1 NM from its target - phase 3)'][1],
                sheet1['ESSM Success Probability'][1],
                sheet1['Sea RAM Success Probability'][1],
                sheet1['CIWS Success Probability'][1],
                sheet1['Satellite'][1], sheet1['Radar'][1], 
                sheet1['Electronic Surveillance'][1], 
                sheet1['Passive Sensors (Acoustic)'][1],
                sheet1['UAV'][1 ], sheet1['USV'][1]]
    
    #Create Plot List for Missile Count Over Time
    iterationArray = [] 
    simulationTimeArray = []
    RedNumberOffensiveMissiles = []
    RedNumberDefensiveMissiles = []
    RedNumberESSMs = []
    RedNumberSeaRAMs = []
    RedNumberCIWS = []
    BlueNumberOffensiveMissiles = []
    BlueNumberDefensiveMissiles = []
    BlueNumberESSMs = []
    BlueNumberSeaRAMs = []
    BlueNumberCIWS = []

    
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
                    initialBlue[18], initialBlue[19], 
                    initialBlue[20], 
                    initialBlue[21],
                    initialBlue[22], initialBlue[23])
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
                    initialRed[18], initialRed[19], 
                    initialRed[20], 
                    initialRed[21],
                    initialRed[22], initialRed[23])
        
        #Print Initialized Ships
        #redShip.printShip()
        #blueShip.printShip()
       
        #not incorporated yet
        #Weather affects scouting effectiveness
        goodWeather = False #bad weather (True is good weather)
        
        
        #Run Missile Simulation
        #keeps track of iterations that are representative of minutes
        simulationTime = 0.25 #in minutes
        #simulation ends when certain time passes to ensure no infinite loop can occur
        animationFile = open("animationFile.txt", "w")
        while(simulationTime <= 1000):
            #checking for exit conditions
            #stop simulation if either ship is hit
            if(redShip.hit or blueShip.hit):
                break
            #stop simulation if both ships are out of ammunition(missiles)
            if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
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
            '''#print the time elapsed in the simulation
            print("Time Elapsed: " + str(simulationTime))
            print('')
            #print the ship summaries
            redShip.printShip()
            blueShip.printShip()
            print('')'''
            #move all flying missiles forward to next state according to time and speed
            redShip.moveAllMissiles()
            blueShip.moveAllMissiles()
            #increment the simulation time
            simulationTime = simulationTime + 0.25
        animationFile.close()
        redShip.printShip()
        blueShip.printShip()
        iterationArray.append(i)
        simulationTimeArray.append(simulationTime)
        RedNumberOffensiveMissiles.append(redShip.omf)
        RedNumberDefensiveMissiles.append(redShip.dmf)
        RedNumberESSMs.append(redShip.essmf)
        RedNumberSeaRAMs.append(redShip.seaRamf)
        RedNumberCIWS.append(redShip.ciwsf)
        BlueNumberOffensiveMissiles.append(blueShip.omf)
        BlueNumberDefensiveMissiles.append(blueShip.dmf)
        BlueNumberESSMs.append(blueShip.essmf)
        BlueNumberSeaRAMs.append(blueShip.seaRamf)
        BlueNumberCIWS.append(blueShip.ciwsf)
        
    plt.scatter(iterationArray, RedNumberOffensiveMissiles, color='red', label='Red Ship')
    plt.scatter(iterationArray, BlueNumberOffensiveMissiles, color='blue', label='Blue Ship')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Iteration')
    plt.ylabel('Offensive Missiles Fired')
    plt.title('Offensive Missiles Fired Per Iteration')
    plt.savefig('OffensiveMissilesIterations.png', dpi=600)
    plt.show()
  
    
    
    '''plt.plot(simulationTimeArray, RedNumberOffensiveMissiles, color='red', label='Red Ship')
    plt.plot(simulationTimeArray, BlueNumberOffensiveMissiles, color='blue', label='Blue Ship')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('Offensive Missiles Left')
    plt.title('Offensive Missiles Left in Ships\' Arsenals over Time')
    plt.savefig('OffensiveMissilesOverTime.png', dpi=600)
    plt.show()
    plt.plot(simulationTimeArray, RedNumberDefensiveMissiles, color='red', label='Red Ship')
    plt.plot(simulationTimeArray, BlueNumberDefensiveMissiles, color='blue', label='Blue Ship')
    plt.legend()
    #plt.ylim((0, 5 + max(redShip.defensiveMissileTotal, blueShip.defensiveMissileTotal)))
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('Defensive Missiles Left')
    plt.title('Defensive Missiles Left in Ships\' Arsenals over Time')
    plt.savefig('DefensiveMissilesOverTime.png', dpi=600)
    plt.show()
    plt.plot(simulationTimeArray, RedNumberESSMs, color='red', label='Red Ship')
    plt.plot(simulationTimeArray, BlueNumberESSMs, color='blue', label='Blue Ship')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('ESSMs Left')
    plt.title('ESSMs Left in Ships\' Arsenals over Time')
    plt.savefig('ESSMs.png', dpi=600)
    plt.show()
    plt.plot(simulationTimeArray, RedNumberSeaRAMs, color='red', label='Red Ship')
    plt.plot(simulationTimeArray, BlueNumberSeaRAMs, color='blue', label='Blue Ship')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('Sea RAMs Left')
    plt.title('Sea RAMs Left in Ships\' Arsenals over Time')
    plt.savefig('SeaRAMs.png', dpi=600)
    plt.show()
    plt.plot(simulationTimeArray, RedNumberCIWS, color='red', label='Red Ship')
    plt.plot(simulationTimeArray, BlueNumberCIWS, color='blue', label='Blue Ship')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Simulation Time (minutes)')
    plt.ylabel('CIWS Left')
    plt.title('CIWS Left in Ships\' Arsenals over Time')
    plt.savefig('CIWS.png', dpi=600)
    plt.show()'''
    
    
        
    
    
    
    
    