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


if __name__ == "__main__":
    # read in policy parameters from an Excel spreadsheet, "missile_policy_parameters.xlsx"
    sheet1 = pd.read_excel("missile_policy_parameters.xlsx", sheet_name="Sheet1")
    
    # state variables
    # Ship
    BlueShip = Ship(sheet1['Ship\'s Name'][0], sheet1['Location'][0], 
                sheet1['Offensive Missiles'][0], sheet1['Defensive Missiles'][0])
    RedShip = Ship(sheet1['Ship\'s Name'][1], sheet1['Location'][1], 
                sheet1['Offensive Missiles'][1], sheet1['Defensive Missiles'][1])
    BlueShip.printShip()
    RedShip.printShip()
    
    #hi