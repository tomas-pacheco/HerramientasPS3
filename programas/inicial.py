# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 20:25:40 2022

@author: Tomas
"""

from wwo_hist import retrieve_hist_data

#### Set working directory to store output csv file(s)
import os
#os.chdir("\\Users\\Tomas\\Desktop\\abi\\herramientasclase3")
os.chdir("/Users/tomaspacheco/Desktop/HerramientasPS3/input/clima")

#### Example code
frequency = 24 
start_date = '1-JAN-2015'
end_date = '31-DEC-2015'
api_key = '53560d256ace4589bd2235034221607'
location_list = ['20637','20653','20688','20735','20871','21040',
                 '21042','21158','21201','21220','21412','21502',
                 '21601','21638','21639','21643','21651','21703',
                 '21742','21801','21811','21853','21902']

hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)

