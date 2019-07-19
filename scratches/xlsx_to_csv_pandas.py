"""
I used this command to convert the xlsx file Frank
sent me to a csvfile.  it saved in the nexus home folder,
and I moved it to the external_files folder.
"""
import pandas as pd

data = pd.read_excel('HYSG.xlsx', 'Sheet1', index=False)
data = pd.read_excel('external_files/HYSG.xlsx', 'Sheet1', index=False)
data.to_csv('csvfile.csv', encoding='utf-8')
