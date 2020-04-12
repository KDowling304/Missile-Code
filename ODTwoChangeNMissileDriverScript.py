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


HeatMap Code Adapted from: 
https://matplotlib.org/gallery/images_contours_and_fields/image_annotated_heatmap.html
"""

#from collections import namedtuple
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker
import numpy as np
#from matplotlib.ticker import MaxNLocator
#from copy import copy
#import math
from Ship import Ship
from HeatMap import heatmap
#from HeatMap import annotate_heatmap


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
    
    offensiveMissileSalvoSize = list(range(1, sheet1['Offensive Missiles'][0] + 1))
    defensiveMissileSalvoSize = list(range(1, 21))
    
    #offensiveMissileSalvoSize = list(range(1, 5))
    #offensiveMissileSuccessProbability = [0, 1/9, 2/9, 3/9] 
    
    BlueShipHitNumber2 = []
    BlueShipHitProp2 = []
    RedShipHitNumber2 = []
    RedShipHitProp2 = []
    BothShipHitNumber2 = []
    NoShipHitNumber2 = []
    BothShipHitProp2 = []
    NoShipHitProp2 = []
    
    AvgBlueOMF2 = []
    StdDevBlueOMF2 = []
    AvgRedOMF2 = []
    StdDevRedOMF2 = []
    
    AvgBlueDMF2 = []
    StdDevBlueDMF2 = []
    AvgRedDMF2 = []
    StdDevRedDMF2 = []
    
    AvgBlueEMF2 = []
    StdDevBlueEMF2 = []
    AvgRedEMF2 = []
    StdDevRedEMF2 = []
    
    AvgBlueSMF2 = []
    StdDevBlueSMF2 = []
    AvgRedSMF2 = []
    StdDevRedSMF2 = []
    
    AvgBlueCMF2 = []
    StdDevBlueCMF2 = []
    AvgRedCMF2 = []
    StdDevRedCMF2 = []
    
    AvgBlueOMR2 = []
    AvgRedOMR2 = []
    AvgRange2 = []
    StdDevRange2 = []
    
    AvgBlueCost2 = []
    StdDevBlueCost2 = []
    AvgRedCost2 = []
    StdDevRedCost2 = []
    
    AvgBlueMissileCost2 = []
    StdDevBlueMissileCost2 = []
    AvgRedMissileCost2 = []
    StdDevRedMissileCost2 = []
    
    
    for defSavSize in defensiveMissileSalvoSize:
        print(defSavSize)

        BlueShipHitNumberArr = []
        BlueShipHitPropArr = []
        RedShipHitNumberArr = []
        RedShipHitPropArr = []
        BothShipHitNumberArr = []
        NoShipHitNumberArr = []
        BothShipHitPropArr = []
        NoShipHitPropArr = []
        
        AvgBlueOMFArr = []
        StdDevBlueOMFArr = []
        AvgRedOMFArr = []
        StdDevRedOMFArr = []
        
        AvgBlueDMFArr = []
        StdDevBlueDMFArr = []
        AvgRedDMFArr = []
        StdDevRedDMFArr = []
        
        AvgBlueEMFArr = []
        StdDevBlueEMFArr = []
        AvgRedEMFArr = []
        StdDevRedEMFArr = []
        
        AvgBlueSMFArr = []
        StdDevBlueSMFArr = []
        AvgRedSMFArr = []
        StdDevRedSMFArr = []
        
        AvgBlueCMFArr = []
        StdDevBlueCMFArr = []
        AvgRedCMFArr = []
        StdDevRedCMFArr = []
        
        AvgBlueOMRArr = []
        AvgRedOMRArr = []
        AvgRangeArr = []
        StdDevRangeArr = []
        
        AvgBlueCostArr = []
        StdDevBlueCostArr = []
        AvgRedCostArr = []
        StdDevRedCostArr = []
        
        AvgBlueMissileCostArr = []
        StdDevBlueMissileCostArr = []
        AvgRedMissileCostArr = []
        StdDevRedMissileCostArr = []
        
    
        
        for offSavSize in offensiveMissileSalvoSize:
           
        
        
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
                            offSavSize,
                            defSavSize,
                            initialBlue[20],
                            initialBlue[21],
                            initialBlue[22],
                            initialBlue[23], initialBlue[24], 
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
                            initialRed[23], initialRed[24], 
                            initialRed[25], 
                            initialRed[26],
                            initialRed[27], initialRed[28])
            #print("Initial Ship Inputs")
            #blueShip.printShipInputs(redShip)
        
            
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
                                offSavSize,
                                defSavSize,
                                initialBlue[20],
                                initialBlue[21],
                                initialBlue[22],
                                initialBlue[23], initialBlue[24], 
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
                                initialRed[23], initialRed[24], 
                                initialRed[25], 
                                initialRed[26],
                                initialRed[27], initialRed[28])
                
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
                    
                    else:
                        if(redShip.hit or blueShip.hit):
                            break
                        #stop simulation if both ships are out of ammunition(missiles)
                        if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
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
                        
                        #move all flying missiles forward to next state according to time and speed
                        blueShip.moveAllMissiles()
                        redShip.moveAllMissiles()
 
                        #increment the simulation time
                        simulationTime = simulationTime + 0.25
                        
                        
                animationFile.close()
                #print("Iteration: " + str(i + 1))
                #print()
                #blueShip.printShip()
                #redShip.printShip()
                #if(redShip.outOfMissiles() and blueShip.outOfMissiles()):
                    #print("Both ships out of missiles")
                    #print()
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
                
            #Number of simulation runs Blue Ship Hit
            BlueShipHitNumber = BlueShipHit.count(True)
            BlueShipHitNumberArr.append(BlueShipHitNumber)
    
            #Proportion of total simulation runs that blue ship is hit (loses)
            BlueShipHitProp = BlueShipHitNumber/len(BlueShipHit)
            BlueShipHitPropArr.append(BlueShipHitProp)
            
            #Number of simulation runs Blue Ship Hit
            RedShipHitNumber = RedShipHit.count(True)
            RedShipHitNumberArr.append(RedShipHitNumber)
            
            #Proportion of total simulation runs that red ship is hit (loses)
            RedShipHitProp = RedShipHitNumber/len(RedShipHit)
            RedShipHitPropArr.append(RedShipHitProp)
            
            BothShipHitNumber = 0
            NoShipHitNumber = 0
            for s in range(len(RedShipHit)):
                if(RedShipHit[s] == True and BlueShipHit[s] == True):
                    BothShipHitNumber = BothShipHitNumber + 1
                if(RedShipHit[s] == False and BlueShipHit[s] == False):
                    NoShipHitNumber = NoShipHitNumber + 1
            BothShipHitNumberArr.append(BothShipHitNumber)
            NoShipHitNumberArr.append(NoShipHitNumber)
                
            BothShipHitProp = BothShipHitNumber/len(RedShipHit)
            BothShipHitPropArr.append(BothShipHitProp)
            NoShipHitProp = NoShipHitNumber/len(RedShipHit)
            NoShipHitPropArr.append(NoShipHitProp)
            
            AvgBlueOMFArr.append(np.mean(BlueNumberOffensiveMissiles))
            StdDevBlueOMFArr.append(np.sqrt(np.var(BlueNumberOffensiveMissiles)))
            AvgRedOMFArr.append(np.mean(RedNumberOffensiveMissiles))
            StdDevRedOMFArr.append(np.sqrt(np.var(RedNumberOffensiveMissiles)))
            
            AvgBlueDMFArr.append(np.mean(BlueNumberDefensiveMissiles))
            StdDevBlueDMFArr.append(np.sqrt(np.var(BlueNumberDefensiveMissiles)))
            AvgRedDMFArr.append(np.mean(RedNumberDefensiveMissiles))
            StdDevRedDMFArr.append(np.sqrt(np.var(RedNumberDefensiveMissiles)))
            
            AvgBlueEMFArr.append(np.mean(BlueNumberESSMs))
            StdDevBlueEMFArr.append(np.sqrt(np.var(BlueNumberESSMs)))
            AvgRedEMFArr.append(np.mean(RedNumberESSMs))
            StdDevRedEMFArr.append(np.sqrt(np.var(RedNumberESSMs)))
            
            AvgBlueSMFArr.append(np.mean(BlueNumberSeaRAMs))
            StdDevBlueSMFArr.append(np.sqrt(np.var(BlueNumberSeaRAMs)))
            AvgRedSMFArr.append(np.mean(RedNumberSeaRAMs))
            StdDevRedSMFArr.append(np.sqrt(np.var(RedNumberSeaRAMs)))
            
            AvgBlueCMFArr.append(np.mean(BlueNumberCIWS))
            StdDevBlueCMFArr.append(np.sqrt(np.var(BlueNumberCIWS)))
            AvgRedCMFArr.append(np.mean(RedNumberCIWS))
            StdDevRedCMFArr.append(np.sqrt(np.var(RedNumberCIWS)))
            
            AvgBlueOMRArr.append(blueShip.offensiveMissileRange)
            AvgRedOMRArr.append(redShip.offensiveMissileRange)
            AvgRangeArr.append(np.mean(ShipRange))
            StdDevRangeArr.append(np.sqrt(np.var(ShipRange)))
            
            AvgBlueCostArr.append(np.mean(BlueShipCost))
            StdDevBlueCostArr.append(np.sqrt(np.var(BlueShipCost)))
            AvgRedCostArr.append(np.mean(RedShipCost))
            StdDevRedCostArr.append(np.sqrt(np.var(RedShipCost)))
            
            AvgBlueMissileCostArr.append(np.mean(BlueShipMissileCost))
            StdDevBlueMissileCostArr.append(np.sqrt(np.var(BlueShipMissileCost)))
            AvgRedMissileCostArr.append(np.mean(RedShipMissileCost))
            StdDevRedMissileCostArr.append(np.sqrt(np.var(RedShipMissileCost)))
            print(offSavSize)
           
        #Number of simulation runs Blue Ship Hit
        BlueShipHitNumber2.append(BlueShipHitNumberArr)

        #Proportion of total simulation runs that blue ship is hit (loses)
        BlueShipHitProp2.append(BlueShipHitPropArr)
        
        #Number of simulation runs Blue Ship Hit
        RedShipHitNumber2.append(RedShipHitNumberArr)
        
        #Proportion of total simulation runs that red ship is hit (loses)
        RedShipHitProp2.append(RedShipHitPropArr)
        
        BothShipHitNumber2.append(BothShipHitNumberArr)
        NoShipHitNumber2.append(NoShipHitNumberArr)
            
        BothShipHitProp2.append(BothShipHitPropArr)
        NoShipHitProp2.append(NoShipHitPropArr)
        
        AvgBlueOMF2.append(AvgBlueOMFArr)
        StdDevBlueOMF2.append(StdDevBlueOMFArr)
        AvgRedOMF2.append(AvgRedOMFArr)
        StdDevRedOMF2.append(StdDevRedOMFArr)
        
        AvgBlueDMF2.append(AvgBlueDMFArr)
        StdDevBlueDMF2.append(StdDevBlueDMFArr)
        AvgRedDMF2.append(AvgRedDMFArr)
        StdDevRedDMF2.append(StdDevRedDMFArr)
        
        AvgBlueEMF2.append(AvgBlueEMFArr)
        StdDevBlueEMF2.append(StdDevBlueEMFArr)
        AvgRedEMF2.append(AvgRedEMFArr)
        StdDevRedEMF2.append(StdDevRedEMFArr)
        
        AvgBlueSMF2.append(AvgBlueSMFArr)
        StdDevBlueSMF2.append(StdDevBlueSMFArr)
        AvgRedSMF2.append(AvgRedSMFArr)
        StdDevRedSMF2.append(StdDevRedSMFArr)
        
        AvgBlueCMF2.append(AvgBlueCMFArr)
        StdDevBlueCMF2.append(StdDevBlueCMFArr)
        AvgRedCMF2.append(AvgRedCMFArr)
        StdDevRedCMF2.append(StdDevRedCMFArr)
        
        AvgBlueOMR2.append(AvgBlueOMRArr)
        AvgRedOMR2.append(AvgRedOMRArr)
        AvgRange2.append(AvgRangeArr)
        StdDevRange2.append(StdDevRangeArr)
        
        AvgBlueCost2.append(AvgBlueCostArr)
        StdDevBlueCost2.append(StdDevBlueCostArr)
        AvgRedCost2.append(AvgRedCostArr)
        StdDevRedCost2.append(StdDevRedCostArr) 
        
        AvgBlueMissileCost2.append(AvgBlueMissileCostArr)
        StdDevBlueMissileCost2.append(StdDevBlueMissileCostArr)
        AvgRedMissileCost2.append(AvgRedMissileCostArr)
        StdDevRedMissileCost2.append(StdDevRedMissileCostArr) 
    
    
    
    
    AvgBlueCost2 = np.array(AvgBlueCost2) 
    fig, ax = plt.subplots()
    im, cbar = heatmap(AvgBlueCost2, defensiveMissileSalvoSize, 
                       offensiveMissileSalvoSize, ax=ax,
                   cmap="YlGnBu", cbarlabel="Cost (USD)")
    #texts = annotate_heatmap(im, valfmt="${x:.1f} USD")
    ax.set_xlabel("Blue Offensive Missile Salvo Size")
    ax.set_ylabel("Blue Defensive Missile Salvo Size")
    ax.set_title("Cost of Engagement for Blue (USD)")
    fig.tight_layout()
    plt.savefig('CostChangingBlueOffDefSalvoSize.png', dpi=600, bbox_inches='tight')
    plt.show()    
    
    AvgBlueMissileCost2 = np.array(AvgBlueMissileCost2) 
    fig, ax = plt.subplots()
    im, cbar = heatmap(AvgBlueMissileCost2, defensiveMissileSalvoSize, 
                       offensiveMissileSalvoSize, ax=ax,
                   cmap="YlGnBu", cbarlabel="Cost (USD)")
    #texts = annotate_heatmap(im, valfmt="${x:.1f} USD")
    ax.set_xlabel("Blue Offensive Missile Salvo Size")
    ax.set_ylabel("Blue Defensive Missile Salvo Size")
    ax.set_title("Blue Missile Cost (USD)")
    fig.tight_layout()
    plt.savefig('MissileCostChangingBlueOffDefSalvoSize.png', dpi=600, bbox_inches='tight')
    plt.show()   
    
    
    AvgRedCost2 = np.array(AvgRedCost2)
    fig, ax = plt.subplots()
    im, cbar = heatmap(AvgRedCost2, defensiveMissileSalvoSize, 
                       offensiveMissileSalvoSize, ax=ax,
                   cmap="YlOrRd", cbarlabel="Cost (USD)")
    #texts = annotate_heatmap(im, valfmt="${x:.1f} USD")
    ax.set_xlabel("Blue Offensive Missile Salvo Size")
    ax.set_ylabel("Blue Defensive Missile Salvo Size")
    ax.set_title("Cost of Engagement for Red (USD)")
    fig.tight_layout()
    plt.savefig('RedCostChangingBlueOffDefSalvoSize.png', dpi=600, bbox_inches='tight')
    plt.show() 
    
    AvgRedMissileCost2 = np.array(AvgRedMissileCost2)
    fig, ax = plt.subplots()
    im, cbar = heatmap(AvgRedMissileCost2, defensiveMissileSalvoSize, 
                       offensiveMissileSalvoSize, ax=ax,
                   cmap="YlOrRd", cbarlabel="Cost (USD)")
    #texts = annotate_heatmap(im, valfmt="${x:.1f} USD")
    ax.set_xlabel("Blue Offensive Missile Salvo Size")
    ax.set_ylabel("Blue Defensive Missile Salvo Size")
    ax.set_title("Red Missile Cost (USD)")
    fig.tight_layout()
    plt.savefig('RedMissileCostChangingBlueOffDefSalvoSize.png', dpi=600, bbox_inches='tight')
    plt.show() 
    
    BlueShipHitProp2 = np.array(BlueShipHitProp2)
    fig, ax = plt.subplots()
    im, cbar = heatmap(BlueShipHitProp2, defensiveMissileSalvoSize, 
                       offensiveMissileSalvoSize, ax=ax,
                   cmap="YlGnBu", cbarlabel="Proportion")
    #texts = annotate_heatmap(im, valfmt="{x:.1f}")
    ax.set_xlabel("Blue Offensive Missile Salvo Size")
    ax.set_ylabel("Blue Defensive Missile Salvo Size")
    ax.set_title("Proportion of Iterations Blue Ship Hit")
    fig.tight_layout()
    plt.savefig('BlueHitChangingBlueOffDefSalvoSize.png', dpi=600, bbox_inches='tight')
    plt.show()    
    
    RedShipHitProp2 = np.array(RedShipHitProp2)
    fig, ax = plt.subplots()
    im, cbar = heatmap(RedShipHitProp2, defensiveMissileSalvoSize, 
                       offensiveMissileSalvoSize, ax=ax,
                   cmap="YlOrRd", cbarlabel="Proportion")
    #texts = annotate_heatmap(im, valfmt="{x:.1f}")
    ax.set_xlabel("Blue Offensive Missile Salvo Size")
    ax.set_ylabel("Blue Defensive Missile Salvo Size")
    ax.set_title("Proportion of Iterations Red Ship Hit")
    fig.tight_layout()
    plt.savefig('RedHitChangingBlueOffDefSalvoSize.png', dpi=600, bbox_inches='tight')
    plt.show()  
    
    BothShipHitProp2 = np.array(BothShipHitProp2)
    fig, ax = plt.subplots()
    im, cbar = heatmap(BothShipHitProp2, defensiveMissileSalvoSize, 
                       offensiveMissileSalvoSize, ax=ax,
                   cmap="Purples", cbarlabel="Proportion")
    #texts = annotate_heatmap(im, valfmt="{x:.1f}")
    ax.set_xlabel("Blue Offensive Missile Salvo Size")
    ax.set_ylabel("Blue Defensive Missile Salvo Size")
    ax.set_title("Proportion of Iterations Both Ships Hit")
    fig.tight_layout()
    plt.savefig('BothHitChangingBlueOffDefSalvoSize.png', dpi=600, bbox_inches='tight')
    plt.show()  
    
    NoShipHitProp2 = np.array(NoShipHitProp2)
    fig, ax = plt.subplots()
    im, cbar = heatmap(NoShipHitProp2, defensiveMissileSalvoSize, 
                       offensiveMissileSalvoSize, ax=ax,
                   cmap="YlGn", cbarlabel="Proportion")
    #texts = annotate_heatmap(im, valfmt="{x:.1f}")
    ax.set_xlabel("Blue Offensive Missile Salvo Size")
    ax.set_ylabel("Blue Defensive Missile Salvo Size")
    ax.set_title("Proportion of Iterations Neither Ship Hit")
    fig.tight_layout()
    plt.savefig('NoHitChangingBlueOffDefSalvoSize.png', dpi=600, bbox_inches='tight')
    plt.show()  

    AvgRange2 = np.array(AvgRange2)
    fig, ax = plt.subplots()
    im, cbar = heatmap(AvgRange2, defensiveMissileSalvoSize, 
                       offensiveMissileSalvoSize, ax=ax,
                   cmap="Purples", cbarlabel="Range (NM)")
    #texts = annotate_heatmap(im, valfmt="{x:.1f}")
    ax.set_xlabel("Blue Offensive Missile Salvo Size")
    ax.set_ylabel("Blue Defensive Missile Salvo Size")
    ax.set_title("Range Between Ships at End of Simulation")
    fig.tight_layout()
    plt.savefig('RangeChangingBlueOffDefSalvoSize.png', dpi=600, bbox_inches='tight')
    plt.show()  
    
    
        
        
        
    
    
    
    
        
        
        
        