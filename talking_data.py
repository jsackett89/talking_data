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
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Create list of csv filepaths in working project directory
filePaths = [f for f in glob.glob(os.path.join('data', '*.csv'))]
# File names
fileNames = ['app_events', 'app_labels', 'events', 'ga_test', 'ga_train', 'labels', 'label_categories', 'pbdm', 'sample_sub']
# Create tuples for dictionary comprehension
fileKeyVal = zip(fileNames, filePaths)
# Create dictionary of files
fileDict = {name: pd.read_csv(file) for name, file in fileKeyVal}

# Explore files
for filename, file in fileDict.items():
    logger.info("File name: {0}".format(filename))
    logger.info("File columns: {0}".format(file.columns))


app_events = fileDict.get("app_events")
print(app_events.describe)
