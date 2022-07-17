# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 21:41:45 2022

@author: Tomas
"""

import pandas as pd
from sodapy import Socrata


client = Socrata("odn.data.socrata.com", "VTGB0DNnS1HP1pKSPDRrwkU0A", 
                 username = "seminarioseconomia@udesa.edu.ar", 
                 password= "EconUdesa2020+")


results = client.get("tt5s-y5fc", limit=100000)


results_df = pd.DataFrame.from_records(results)
results_df.to_csv('crime1.csv', header=True, index=False)




