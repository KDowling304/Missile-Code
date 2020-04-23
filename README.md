# Missile-Code
This folder has the code for running simulations of the missile engagement described in Kara Dowling's 
Princeton University ORFE senior thesis, 
"A Multi-agent Stochastic Control Model for Adversarial Planning in Naval Operations."

This Excel file has all the inputs into the simulation that can be changed:
missile_policy_parameters.xlsx

These scripts are the backbone for the simulation and used when running the driver scripts:
Ship.py
OffensiveMissile.py
DefensiveMissile.py
ESSM.py
SeaRAM.py
CIWS.py

This script runs one run of the missile simulation and the output text file can be fed into the Java visual simulation:
MissileDriverScript.py

This script runs multiple iterations of the simulation:
NMissileDriverScript.py

These scripts run multiple iterations of the simulation while changing one input into the simulation:
ChangingNMissileDriverScript.py (Blue's offensive missile salvo size)
SuccessProbChangingNMissileDriverScript.py (Blue's offensive missile success probability)
RangeChangingNMissileDriverScript.py (Blue's offensive missile range)
DefensiveChangingNMissileDriverScript.py (Blue's defensive missile salvo size)

This script toggles the satellite use for Both Blue and Red:
SatelliteBoxPlotComparison.py

These scripts run multiple iterations of the simulation while changing two inputs into the simualtion:
TwoChangeNMissileDriverScript.py (Blue's offensive missile salvo size and success probability)
ODTwoChangeNMissileDriverScript.py (Blue's offensive and defensive missile salvo sizes)


