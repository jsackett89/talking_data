# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 22:35:30 2016

@author: sackettj
"""

# Load necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

# Create list of csv filepaths in working project directory
cwd = os.getcwd()
filePaths = [cwd + "\\" + f for f in glob.glob("*.csv")]
# File names
fileNames = ['app_labels', 'events', 'ga_test', 'ga_train', 'labels', 'pbdm', 'sample_sub']
# Create tuples for dictionary comprehension
fileKeyVal = zip(fileNames, filePaths)
# Create dictionary of files
fileDict = {name : pd.read_csv(file) for name, file in  fileKeyVal}

# Explore files

