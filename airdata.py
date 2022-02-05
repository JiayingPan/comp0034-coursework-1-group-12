from pathlib import Path
import numpy as np
import pandas as pd
from datetime import datetime

class RecyclingData:
    """Class for retrieving and structuring the data.
    TODO: Add error handling for file read issues.
    TODO: Improve the efficiency of the stats calcs.
    """

    def __init__(self):
        self.recycling = pd.DataFrame()
        self.area_list = []
        self.recycling_eng = []
        self.recycling_area = []
        self.get_data()

    def get_data(self):
        datafolder = Path('data')
        csvfile = 'all.csv'
        self.recycling = pd.read_csv(datafolder/csvfile)
        #self.recycling = pd.read_csv('data/household_recycling.csv')
        self.area_list = self.recycling["location_x"].unique().tolist()

    def process_data_for_area(self, area,start_date,end_date):
        self.recycling['utc'] = pd.to_datetime(self.recycling['utc'])
        mask_1 = (self.recycling['utc']> start_date) & (self.recycling['utc'] <= end_date) & (self.recycling['location_x'] == 'London')
        mask_2 = (self.recycling['utc']> start_date) & (self.recycling['utc'] <= end_date) & (self.recycling['location_x'] == area)
        # Data for England
        self.recycling_eng = self.recycling.loc[mask_1]
        #by_yr_e = self.recycling_eng.sort_values('utc', ascending=False)
        #by_yr_e = by_yr_e.reset_index(drop=True)

        # Data for the selected area
        self.recycling_area = self.recycling.loc[mask_2]
        # Calculate the change from the previous year
        #by_yr = self.recycling_area.sort_values('utc', ascending=False)
        #by_yr = by_yr.reset_index(drop=True)


