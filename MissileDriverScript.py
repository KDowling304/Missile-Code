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
from Missile import Missile


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
    #list of offensive missiles fired by blueShip
    blueOffensiveMissiles = []
    #list of defensive missiles fired by blueShip
    blueDefensiveMissiles = []
    #list of offensive missiles fired by redShip
    redOffensiveMissiles = []
    #list of defensive missiles fired by redShip
    redDefensiveMissiles = []
    
    #speeds of missiles/ships from Excel spreadsheet
    #missileSpeed in knots
    missileSpeed = sheet2['Missile Speed (kn)'][0]
    shipSpeed = sheet2['Ship Speed (kn)'][0]
    print("Missile speed: " + str(missileSpeed) + " knots")
    print("Ship speed: " + str(shipSpeed) + " knots")
    
    