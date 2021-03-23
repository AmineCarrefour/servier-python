import os.path
from datetime import datetime
import pandas as pd
import json
import numpy as np


class Configs:

    def __init__(self):
        self.PUBMED_CSV_PATH = os.path.realpath('resources/raw/pubmed.csv')
        self.PUBMED_JSON_PATH = os.path.realpath('resources/raw/pubmed.json')
        self.DRUGS_PATH = os.path.realpath('resources/raw/drugs.csv')
        self.CLINICAL_TRIALS_PATH = os.path.realpath('resources/raw/clinical_trials.csv')
        self.RESULTS_PATH_JSON = os.path.realpath('resources/results/results.json')
