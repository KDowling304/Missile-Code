#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:14:19 2019

@author: karadowling
code adapted from ORF 411 AssetSelling problem code found at link below
https://github.com/wbpowell328/stochastic-optimization/tree/master/AssetSelling
"""

from collections import namedtuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from copy import copy
import math
from Ship import Ship
from OffensiveMissile import OffensiveMissile
from DefensiveMissile import DefensiveMissile


if __name__ == "__main__":
    #read in policy parameters from an Excel spreadsheet, "missile_policy_parameters.xlsx"
    sheet1 = pd.read_excel("missile_policy_parameters.xlsx", sheet_name="Sheet1")
    sheet2 = pd.read_excel("missile_policy_parameters.xlsx", sheet_name="Sheet2")
    
    #state variables
    #Ships
    blueShip = Ship(sheet1['Ship\'s Name'][0], sheet1['Location'][0], 
                sheet1['Offensive Missiles'][0], sheet1['Defensive Missiles'][0])
    redShip = Ship(sheet1['Ship\'s Name'][1], sheet1['Location'][1], 
                sheet1['Offensive Missiles'][1], sheet1['Defensive Missiles'][1])
    blueShip.printShip()
    redShip.printShip()
    
    #Missiles Lists
    #initialize empty lists with size of arsenals
    #list of offensive missiles fired by blueShip
    blueOffensiveMissiles = [None] * blueShip.oml
    #list of defensive missiles fired by blueShip
    blueDefensiveMissiles = [None] * blueShip.dml
    #list of offensive missiles fired by redShip
    redOffensiveMissiles = [None] * redShip.oml
    #list of defensive missiles fired by redShip
    redDefensiveMissiles = [None] * redShip.dml
    
    #speeds of missiles/ships from Excel spreadsheet
    #missileSpeed in knots
    missileSpeed = sheet2['Missile Speed (kn)'][0]
    shipSpeed = sheet2['Ship Speed (kn)'][0]
    print("Missile Speed: " + str(missileSpeed) + " knots")
    print("Ship Speed: " + str(shipSpeed) + " knots")
    
    #time step for each iteration of "game" in minuntes
    timeStep = sheet2['Time Step (minutes)'][0]
    print("Time Step: " + str(timeStep) + " minutes")
    
    #Decision variables that determine scouting effectiveness but also have cost
    satellite = False #not communicating with satellite
    radar = False #active radar turned off
    electronicSurveillance = False #electronic surveillance equipment off
    passiveSensors = False #passive acoustic sensors off
    uav = False #Unmanned Aerial Vehicle (UAV) not deployed
    usv = False #Unmanned Surface Vehicle (USV) not deployed
   
    #Weather affects scouting effectiveness
    goodWeather = False #bad weather (True is good weather)
    
    
    