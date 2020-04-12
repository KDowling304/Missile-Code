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
import matplotlib as mpl 
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
    RedNumberOffensiveMissiles = []
    RedNumberDefensiveMissiles = []
    RedNumberESSMs = []
    RedNumberSeaRAMs = []
    RedNumberCIWS = []
    RedShipOffensiveMissileRange = []
    RedShipHit = []
    RedShipCost = []
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
        #goodWeather = False #bad weather (True is good weather)
        
        
        #Run Missile Simulation
        #keeps track of iterations that are representative of minutes
        simulationTime = 0.25 #in minutes
        #simulation ends when certain time passes to ensure no infinite loop 
        #can occur
        animationFile = open("animationFile.txt", "w")
        while(simulationTime <= 1000):
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
        RedNumberOffensiveMissiles.append(redShip.omf)
        RedNumberDefensiveMissiles.append(redShip.dmf)
        RedNumberESSMs.append(redShip.essmf)
        RedNumberSeaRAMs.append(redShip.seaRamf)
        RedNumberCIWS.append(redShip.ciwsf)
        RedShipOffensiveMissileRange.append(redShip.offensiveMissileRange)
        RedShipHit.append(redShip.hit)
        RedShipCost.append(redShip.engagementCost())
        ShipRange.append(abs(blueShip.loc-redShip.loc))

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
        
    BothShipHitProp = BothShipHitNumber/len(RedShipHit)
    print("Proportion of Iterations Both Ships Hit: " + str(BothShipHitProp))
    NoShipHitProp = NoShipHitNumber/len(RedShipHit)
    print("Proportion of Iterations No Ships Hit: " + str(NoShipHitProp))
    print()
    
    print("Median Blue Offensive Missiles Fired: " + str(np.median(BlueNumberOffensiveMissiles)) + " of total " + str(blueShip.offensiveMissileTotal))
    print("Average Blue Offensive Missiles Fired: " + str(np.mean(BlueNumberOffensiveMissiles)) + " of total " + str(blueShip.offensiveMissileTotal))
    print("Standard Deviation of Blue Offensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberOffensiveMissiles))))
    print("Median Red Offensive Missiles Fired: " + str(np.median(RedNumberOffensiveMissiles)) + " of total " + str(redShip.offensiveMissileTotal))
    print("Average Red Offensive Missiles Fired: " + str(np.mean(RedNumberOffensiveMissiles)) + " of total " + str(redShip.offensiveMissileTotal))
    print("Standard Deviation of Red Offensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberOffensiveMissiles))))
    print()
    
    print("Median Blue Defensive Missiles Fired: " + str(np.median(BlueNumberDefensiveMissiles)) + " of total " + str(blueShip.defensiveMissileTotal))
    print("Average Blue Defensive Missiles Fired: " + str(np.mean(BlueNumberDefensiveMissiles)) + " of total " + str(blueShip.defensiveMissileTotal))
    print("Standard Deviation of Blue Defensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberDefensiveMissiles))))
    print("Median Red Defensive Missiles Fired: " + str(np.median(RedNumberDefensiveMissiles)) + " of total " + str(redShip.defensiveMissileTotal))
    print("Average Red Defensive Missiles Fired: " + str(np.mean(RedNumberDefensiveMissiles)) + " of total " + str(redShip.defensiveMissileTotal))
    print("Standard Deviation of Red Defensive Missiles Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberDefensiveMissiles))))
    print()
    
    print("Median Blue ESSMs Fired: " + str(np.median(BlueNumberESSMs)) + " of total " + str(blueShip.essmTotal))
    print("Average Blue ESSMs Fired: " + str(np.mean(BlueNumberESSMs)) + " of total " + str(blueShip.essmTotal))
    print("Standard Deviation of Blue ESSMs Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberESSMs))))
    print("Median Red ESSMs Fired: " + str(np.median(RedNumberESSMs))+ " of total " + str(redShip.essmTotal))
    print("Average Red ESSMs Fired: " + str(np.mean(RedNumberESSMs))+ " of total " + str(redShip.essmTotal))
    print("Standard Deviation of Red ESSMs Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberESSMs))))
    print()
    
    print("Median Blue SeaRAMs Fired: " + str(np.median(BlueNumberSeaRAMs)) + " of total " + str(blueShip.seaRamTotal))
    print("Average Blue SeaRAMs Fired: " + str(np.mean(BlueNumberSeaRAMs)) + " of total " + str(blueShip.seaRamTotal))
    print("Standard Deviation of Blue SeaRAMs Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberSeaRAMs))))
    print("Median Red SeaRAMs Fired: " + str(np.median(RedNumberSeaRAMs)) + " of total " + str(redShip.seaRamTotal))
    print("Average Red SeaRAMs Fired: " + str(np.mean(RedNumberSeaRAMs)) + " of total " + str(redShip.seaRamTotal))
    print("Standard Deviation of Red SeaRAMs Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberSeaRAMs))))
    print()
    
    print("Median Blue CIWS Iterations Fired: " + str(np.median(BlueNumberCIWS)) + " of total " + str(blueShip.ciwsTotal))
    print("Average Blue CIWS Iterations Fired: " + str(np.mean(BlueNumberCIWS)) + " of total " + str(blueShip.ciwsTotal))
    print("Standard Deviation of Blue CIWS Iterations Fired: " + '{:,.2f}'.format(np.sqrt(np.var(BlueNumberCIWS))))
    print("Median Red CIWS Iterations Fired: " + str(np.median(RedNumberCIWS)) + " of total " + str(redShip.ciwsTotal))
    print("Average Red CIWS Iterations Fired: " + str(np.mean(RedNumberCIWS)) + " of total " + str(redShip.ciwsTotal))
    print("Standard Deviation of Red CIWS Iterations Fired: " + '{:,.2f}'.format(np.sqrt(np.var(RedNumberCIWS))))
    print()
    
    print("Blue Offensive Missile Range: " + str(blueShip.offensiveMissileRange))
    print("Red Offensive Missile Range: " + str(redShip.offensiveMissileRange))
    print("Median Range Between Ships at Simulation End: " + str(np.median(ShipRange)))
    print("Average Range Between Ships at Simulation End: " + str(np.mean(ShipRange)))
    print("Standard Deviation of Range Between Ships at Simulation End: " + '{:,.2f}'.format(np.sqrt(np.var(ShipRange))))
    print()
    
    print("Median Blue Cost: " + '{:,.2f}'.format(np.median(BlueShipCost)))
    print("Average Blue Cost: " + '{:,.2f}'.format(np.mean(BlueShipCost)))
    print("Standard Deviation of Blue Cost: " + '{:,.2f}'.format(np.sqrt(np.var(BlueShipCost))))
    print("Median Red Cost: " + '{:,.2f}'.format(np.median(RedShipCost)))
    print("Average Red Cost: " + '{:,.2f}'.format(np.mean(RedShipCost)))
    print("Standard Deviation of Red Cost: " + '{:,.2f}'.format(np.sqrt(np.var(RedShipCost))))
    print()
    
    plt.scatter(iterationArray, BlueNumberOffensiveMissiles, color='blue', label='Blue Ship')
    plt.scatter(iterationArray, RedNumberOffensiveMissiles, color='red', label='Red Ship')
    plt.legend()
    #plt.ylim(0, 1 + max(redShip.offensiveMissileTotal, blueShip.offensiveMissileTotal))
    plt.axes
    plt.xlabel('Iteration')
    plt.ylabel('Offensive Missiles Fired')
    plt.title('Offensive Missiles Fired Per Iteration')
    plt.savefig('OffensiveMissilesIterations.png', dpi=600)
    plt.show()
    
    plt.scatter(iterationArray, BlueNumberDefensiveMissiles, color='blue', label='Blue Ship')
    plt.scatter(iterationArray, RedNumberDefensiveMissiles, color='red', label='Red Ship')
    plt.legend()
    plt.axes
    plt.xlabel('Iteration')
    plt.ylabel('Defensive Missiles Fired')
    plt.title('Defensive Missiles Fired Per Iteration')
    plt.savefig('DefensiveMissilesIterations.png', dpi=600)
    plt.show()
    
    plt.scatter(iterationArray, BlueNumberESSMs, color='blue', label='Blue Ship')
    plt.scatter(iterationArray, RedNumberESSMs, color='red', label='Red Ship')
    plt.legend()
    plt.axes
    plt.xlabel('Iteration')
    plt.ylabel('ESSMs Fired')
    plt.title('ESSMs Fired Per Iteration')
    plt.savefig('ESSMsIterations.png', dpi=600)
    plt.show()
    
    plt.scatter(iterationArray, BlueNumberSeaRAMs, color='blue', label='Blue Ship')
    plt.scatter(iterationArray, RedNumberSeaRAMs, color='red', label='Red Ship')
    plt.legend()
    plt.axes
    plt.xlabel('Iteration')
    plt.ylabel('SeaRAMs Fired')
    plt.title('SeaRAMs Fired Per Iteration')
    plt.savefig('SeaRAMsIterations.png', dpi=600)
    plt.show()
    
    plt.scatter(iterationArray, BlueNumberCIWS, color='blue', label='Blue Ship')
    plt.scatter(iterationArray, RedNumberCIWS, color='red', label='Red Ship')
    plt.legend()
    plt.axes
    plt.xlabel('Iteration')
    plt.ylabel('CIWS Sets of 1,500 Rounds Fired')
    plt.title('CIWS Sets Fired Per Iteration')
    plt.savefig('CIWSIterations.png', dpi=600)
    plt.show()
    
    plt.scatter(iterationArray, ShipRange, color='black', label='Range Between Ships')
    plt.plot(iterationArray, BlueShipOffensiveMissileRange, color='blue', label='Blue Offensive Missile Range')
    plt.plot(iterationArray, RedShipOffensiveMissileRange, color='red', label='Red Offensive Missile Range')
    plt.legend()
    plt.axes
    plt.xlabel('Iteration')
    plt.ylabel('Range (NM)')
    plt.title('Range Between Ships at the End of Each Iteration')
    plt.savefig('RangeIterations.png', dpi=600)
    plt.show()
    
    plt.scatter(iterationArray, BlueShipCost, color='blue', label='Blue')
    plt.scatter(iterationArray, RedShipCost, color='red', label='Red')
    plt.legend()
    plt.axes
    plt.xlabel('Iteration')
    plt.ylabel('Cost in USD')
    plt.title('Missile Engagement Cost')
    plt.savefig('CostIterations.png', dpi=600)
    plt.show()
    
    intervals = len(RedShipHit)/10
    intervalsRedHitArr = []
    intervalsBlueHitArr = []
    place = 0
    while(place < len(RedShipHit)):
        z = 0
        propIntervalRedArr = []
        propIntervalBlueArr = []
        while(z < intervals):
            propIntervalRedArr.append(RedShipHit[place])
            propIntervalBlueArr.append(BlueShipHit[place])
            z = z + 1
            place = place + 1
        intervalsRedHitArr.append(np.mean(propIntervalRedArr))
        intervalsBlueHitArr.append(np.mean(propIntervalBlueArr))
    #print(intervalsRedHitArr)
    #print(intervalsBlueHitArr)
    #print(len(intervalsBlueHitArr))
    
    #create box-plot
    #Code adapted from link below
    #http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    data_to_plot = [intervalsBlueHitArr, intervalsRedHitArr]
    fig = plt.figure(1, figsize=(7, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    ## change outline color, fill color and linewidth of the boxes
    bp['boxes'][0].set( color='midnightblue', linewidth=2)
    bp['boxes'][0].set( facecolor = 'blue' )
    bp['boxes'][1].set( color='darkred', linewidth=2)
    bp['boxes'][1].set( facecolor = 'red' )
    ## change color and linewidth of the whiskers
    bp['whiskers'][0].set(color='midnightblue', linewidth=2)
    bp['whiskers'][1].set(color='midnightblue', linewidth=2)
    bp['whiskers'][2].set(color='darkred', linewidth=2)
    bp['whiskers'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the caps
    bp['caps'][0].set(color='midnightblue', linewidth=2)
    bp['caps'][1].set(color='midnightblue', linewidth=2)
    bp['caps'][2].set(color='darkred', linewidth=2)
    bp['caps'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the medians
    bp['medians'][0].set(color='paleturquoise', linewidth=2)
    bp['medians'][1].set(color='mistyrose', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)             
    ## Custom x-axis labels
    ax.set_xticklabels(['Blue', 'Red'])
    ax.set_title('Proportion of Iterations Ship Hit over 1,000 Simulations')
    ax.set_ylabel('Proportion Hit (groups of 100 simulations)')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    fig.savefig('boxPlotShipHit.png', bbox_inches='tight', dpi=600)
    plt.show()
            
    #create box-plot
    #Code adapted from link below
    #http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    data_to_plot = [BlueNumberOffensiveMissiles, RedNumberOffensiveMissiles]
    fig = plt.figure(1, figsize=(7, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    ## change outline color, fill color and linewidth of the boxes
    bp['boxes'][0].set( color='midnightblue', linewidth=2)
    bp['boxes'][0].set( facecolor = 'blue' )
    bp['boxes'][1].set( color='darkred', linewidth=2)
    bp['boxes'][1].set( facecolor = 'red' )
    ## change color and linewidth of the whiskers
    bp['whiskers'][0].set(color='midnightblue', linewidth=2)
    bp['whiskers'][1].set(color='midnightblue', linewidth=2)
    bp['whiskers'][2].set(color='darkred', linewidth=2)
    bp['whiskers'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the caps
    bp['caps'][0].set(color='midnightblue', linewidth=2)
    bp['caps'][1].set(color='midnightblue', linewidth=2)
    bp['caps'][2].set(color='darkred', linewidth=2)
    bp['caps'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the medians
    bp['medians'][0].set(color='paleturquoise', linewidth=2)
    bp['medians'][1].set(color='mistyrose', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)             
    ## Custom x-axis labels
    ax.set_xticklabels(['Blue', 'Red'])
    ax.set_title('Offensive Missiles Fired over 1,000 Simulations')
    ax.set_ylabel('Number of Missiles')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    fig.savefig('boxPlotOffensive.png', bbox_inches='tight', dpi=600)
    plt.show()
    
    #create box-plot
    #Code adapted from link below
    #http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    data_to_plot = [BlueNumberDefensiveMissiles, RedNumberDefensiveMissiles]
    fig = plt.figure(1, figsize=(7, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    ## change outline color, fill color and linewidth of the boxes
    bp['boxes'][0].set( color='midnightblue', linewidth=2)
    bp['boxes'][0].set( facecolor = 'blue' )
    bp['boxes'][1].set( color='darkred', linewidth=2)
    bp['boxes'][1].set( facecolor = 'red' )
    ## change color and linewidth of the whiskers
    bp['whiskers'][0].set(color='midnightblue', linewidth=2)
    bp['whiskers'][1].set(color='midnightblue', linewidth=2)
    bp['whiskers'][2].set(color='darkred', linewidth=2)
    bp['whiskers'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the caps
    bp['caps'][0].set(color='midnightblue', linewidth=2)
    bp['caps'][1].set(color='midnightblue', linewidth=2)
    bp['caps'][2].set(color='darkred', linewidth=2)
    bp['caps'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the medians
    bp['medians'][0].set(color='paleturquoise', linewidth=2)
    bp['medians'][1].set(color='mistyrose', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)             
    ## Custom x-axis labels
    ax.set_xticklabels(['Blue', 'Red'])
    ax.set_title('Defensive Missiles Fired over 1,000 Simulations')
    ax.set_ylabel('Number of Missiles')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    fig.savefig('boxPlotDefensive.png', bbox_inches='tight', dpi=600)
    plt.show()
    
    #create box-plot
    #Code adapted from link below
    #http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    data_to_plot = [BlueNumberESSMs, RedNumberESSMs]
    fig = plt.figure(1, figsize=(7, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    ## change outline color, fill color and linewidth of the boxes
    bp['boxes'][0].set( color='midnightblue', linewidth=2)
    bp['boxes'][0].set( facecolor = 'blue' )
    bp['boxes'][1].set( color='darkred', linewidth=2)
    bp['boxes'][1].set( facecolor = 'red' )
    ## change color and linewidth of the whiskers
    bp['whiskers'][0].set(color='midnightblue', linewidth=2)
    bp['whiskers'][1].set(color='midnightblue', linewidth=2)
    bp['whiskers'][2].set(color='darkred', linewidth=2)
    bp['whiskers'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the caps
    bp['caps'][0].set(color='midnightblue', linewidth=2)
    bp['caps'][1].set(color='midnightblue', linewidth=2)
    bp['caps'][2].set(color='darkred', linewidth=2)
    bp['caps'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the medians
    bp['medians'][0].set(color='paleturquoise', linewidth=2)
    bp['medians'][1].set(color='mistyrose', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)             
    ## Custom x-axis labels
    ax.set_xticklabels(['Blue', 'Red'])
    ax.set_title('ESSMs Fired over 1,000 Simulations')
    ax.set_ylabel('Number of Missiles')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    fig.savefig('boxPlotESSM.png', bbox_inches='tight', dpi=600)
    plt.show()
    
    #create box-plot
    #Code adapted from link below
    #http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    data_to_plot = [BlueNumberSeaRAMs, RedNumberSeaRAMs]
    fig = plt.figure(1, figsize=(7, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    ## change outline color, fill color and linewidth of the boxes
    bp['boxes'][0].set( color='midnightblue', linewidth=2)
    bp['boxes'][0].set( facecolor = 'blue' )
    bp['boxes'][1].set( color='darkred', linewidth=2)
    bp['boxes'][1].set( facecolor = 'red' )
    ## change color and linewidth of the whiskers
    bp['whiskers'][0].set(color='midnightblue', linewidth=2)
    bp['whiskers'][1].set(color='midnightblue', linewidth=2)
    bp['whiskers'][2].set(color='darkred', linewidth=2)
    bp['whiskers'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the caps
    bp['caps'][0].set(color='midnightblue', linewidth=2)
    bp['caps'][1].set(color='midnightblue', linewidth=2)
    bp['caps'][2].set(color='darkred', linewidth=2)
    bp['caps'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the medians
    bp['medians'][0].set(color='paleturquoise', linewidth=2)
    bp['medians'][1].set(color='mistyrose', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)             
    ## Custom x-axis labels
    ax.set_xticklabels(['Blue', 'Red'])
    ax.set_title('SeaRAMs Fired over 1,000 Simulations')
    ax.set_ylabel('Number of Missiles')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    fig.savefig('boxPlotSeaRAM.png', bbox_inches='tight', dpi=600)
    plt.show()
    
    #create box-plot
    #Code adapted from link below
    #http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    data_to_plot = [BlueNumberCIWS, RedNumberCIWS]
    fig = plt.figure(1, figsize=(7, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    ## change outline color, fill color and linewidth of the boxes
    bp['boxes'][0].set( color='midnightblue', linewidth=2)
    bp['boxes'][0].set( facecolor = 'blue' )
    bp['boxes'][1].set( color='darkred', linewidth=2)
    bp['boxes'][1].set( facecolor = 'red' )
    ## change color and linewidth of the whiskers
    bp['whiskers'][0].set(color='midnightblue', linewidth=2)
    bp['whiskers'][1].set(color='midnightblue', linewidth=2)
    bp['whiskers'][2].set(color='darkred', linewidth=2)
    bp['whiskers'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the caps
    bp['caps'][0].set(color='midnightblue', linewidth=2)
    bp['caps'][1].set(color='midnightblue', linewidth=2)
    bp['caps'][2].set(color='darkred', linewidth=2)
    bp['caps'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the medians
    bp['medians'][0].set(color='paleturquoise', linewidth=2)
    bp['medians'][1].set(color='mistyrose', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)             
    ## Custom x-axis labels
    ax.set_xticklabels(['Blue', 'Red'])
    ax.set_title('CIWS Sets Fired over 1,000 Simulations')
    ax.set_ylabel('Sets of 1,500 Rounds')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    fig.savefig('boxPlotCIWS.png', bbox_inches='tight', dpi=600)
    plt.show()
    
    #create box-plot
    #Code adapted from link below
    #http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    data_to_plot = [BlueShipCost, RedShipCost]
    fig = plt.figure(1, figsize=(7, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    ## change outline color, fill color and linewidth of the boxes
    bp['boxes'][0].set( color='midnightblue', linewidth=2)
    bp['boxes'][0].set( facecolor = 'blue' )
    bp['boxes'][1].set( color='darkred', linewidth=2)
    bp['boxes'][1].set( facecolor = 'red' )
    ## change color and linewidth of the whiskers
    bp['whiskers'][0].set(color='midnightblue', linewidth=2)
    bp['whiskers'][1].set(color='midnightblue', linewidth=2)
    bp['whiskers'][2].set(color='darkred', linewidth=2)
    bp['whiskers'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the caps
    bp['caps'][0].set(color='midnightblue', linewidth=2)
    bp['caps'][1].set(color='midnightblue', linewidth=2)
    bp['caps'][2].set(color='darkred', linewidth=2)
    bp['caps'][3].set(color='darkred', linewidth=2)
    ## change color and linewidth of the medians
    bp['medians'][0].set(color='paleturquoise', linewidth=2)
    bp['medians'][1].set(color='mistyrose', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)             
    ## Custom x-axis labels
    ax.set_xticklabels(['Blue', 'Red'])
    ax.set_title('Missile Engagement Cost over 1,000 Simulations')
    ax.set_ylabel('Cost (USD)')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    fig.savefig('boxPlotCost.png', bbox_inches='tight', dpi=600)
    plt.show()
           
           
    #create box-plot
    #Code adapted from link below
    #http://blog.bharatbhole.com/creating-boxplots-with-matplotlib/
    data_to_plot = [ShipRange]
    fig = plt.figure(1, figsize=(7, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, patch_artist=True)
    ## change outline color, fill color and linewidth of the boxes
    for box in bp['boxes']:
        # change outline color
        box.set( color='#7570b3', linewidth=2)
        # change fill color
        box.set( facecolor = '#1b9e77' )
    ## change color and linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)
    ## change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color='#7570b3', linewidth=2)
    ## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='#b2df8a', linewidth=2)
    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)           
    ## Custom x-axis labels
    ax.set_xticklabels([''])
    ax.set_title('Range Between Ships at Simulation End over 1,000 Simulations')
    ax.set_ylabel('Range (NM)')
    ## Remove top axes and right axes ticks
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    fig.savefig('boxPlotShipRange.png', bbox_inches='tight', dpi=600)
    plt.show()
    
    #print(BlueNumberESSMs)
    
  
  
  
  
    
    
        
    
    
    
    
    