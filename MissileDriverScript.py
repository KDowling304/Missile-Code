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

from collections import namedtuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from copy import copy
import math
from Ship import Ship

if __name__ == "__main__":
    #read in policy parameters from an Excel spreadsheet, "missile_policy_parameters.xlsx"
    sheet1 = pd.read_excel("missile_policy_parameters.xlsx", sheet_name="Sheet1")
    sheet2 = pd.read_excel("missile_policy_parameters.xlsx", sheet_name="Sheet2")
    
    #state variables


    #time step for each iteration of "game" in minuntes
    timeStep = sheet2['Time Step (minutes)'][0]
    print("Time Step: " + str(timeStep) + " minutes")
    print('')
    
    #Initialize Ships
    blueShip = Ship(sheet1['Ship\'s Name'][0], sheet1['Location'][0], 
                sheet1['Offensive Missiles'][0], sheet1['Defensive Missiles'][0], 
                sheet1['Ship Speed (kn)'][0], sheet1['Missile Speed (kn)'][0], 
                timeStep, sheet1['Missile Range (NM)'][0], 
                sheet1['Offensive Missile Success Probability'][0],
                sheet1['Defensive Missile Success Probability'][0])
    redShip = Ship(sheet1['Ship\'s Name'][1], sheet1['Location'][1], 
                sheet1['Offensive Missiles'][1], sheet1['Defensive Missiles'][1], 
                sheet1['Ship Speed (kn)'][1], sheet1['Missile Speed (kn)'][1], 
                timeStep, sheet1['Missile Range (NM)'][1], 
                sheet1['Offensive Missile Success Probability'][1],
                sheet1['Defensive Missile Success Probability'][1])
    #Print Initialized Ships
    redShip.printShip()
    blueShip.printShip()
    
      
    #not incorporating these yet
    #Decision variables that determine scouting effectiveness but also have cost
    satellite = False #not communicating with satellite
    radar = False #active radar turned off
    electronicSurveillance = False #electronic surveillance equipment off
    passiveSensors = False #passive acoustic sensors off
    uav = False #Unmanned Aerial Vehicle (UAV) not deployed
    usv = False #Unmanned Surface Vehicle (USV) not deployed
   
    #Weather affects scouting effectiveness
    goodWeather = False #bad weather (True is good weather)
    
    #Create Plot List for Missile Count Over Time
    simulationTimeArray = [] #
    RedNumberOffensiveMissiles = []
    RedNumberDefensiveMissiles = []
    BlueNumberOffensiveMissiles = []
    BlueNumberDefensiveMissiles = []
    
    #Run Missile Simulation
    #keeps track of iterations that are representative of minutes
    simulationTime = 0 #in minutes
    #simulation ends when certain time passes to ensure no infinite loop can occur
    animationFile = open("animationFile.txt", "w")
    while(simulationTime <= 500):
        #checking for exit conditions
        #stop simulation if either ship is hit
        if(redShip.hit or blueShip.hit):
            break
        #stop simulation if both ships are out of ammunition(missiles)
        if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
            break 
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
        redShip.printShip()
        blueShip.printShip()
        print('')
        simulationTimeArray.append(simulationTime)
        RedNumberOffensiveMissiles.append(redShip.offensiveMissileTotal - redShip.omf)
        RedNumberDefensiveMissiles.append(redShip.defensiveMissileTotal - redShip.dmf)
        BlueNumberOffensiveMissiles.append(blueShip.offensiveMissileTotal - blueShip.omf)
        BlueNumberDefensiveMissiles.append(blueShip.defensiveMissileTotal - blueShip.dmf)
        #move all flying missiles forward to next state according to time and speed
        redShip.moveAllMissiles()
        blueShip.moveAllMissiles()
        #increment the simulation time
        simulationTime = simulationTime + 0.25
    animationFile.close()
 
    plt.plot(simulationTimeArray, RedNumberOffensiveMissiles, color='red', label='Red Ship')
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
    
        
    
    
    
    
    