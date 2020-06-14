import pandas as pd
import glob
from datetime import timedelta

# Function to dynamically find CSV


def pd_read_pattern(*Args):
    files = glob.glob(*Args)
    data = pd.DataFrame()
    for f in files:
        data = data.append(pd.read_csv(f, header=9))
        data['Outbound'].dropna(how='all')
    return data.reset_index(drop=True)


# Open CSV
data = pd_read_pattern('*- Traffic -*.csv')


# Define spans of weeks
Week1 = data.iloc[0:85]
Week2 = data.iloc[85:169]
Week3 = data.iloc[169:253]
Week4 = data.iloc[253:337]

Month = [Week1, Week2, Week3, Week4]

print('Week 1 - ', str(round(Week1['Outbound'].max() / 1000000, 2)), 'Mbps')
print('Week 2 - ', str(round(Week2['Outbound'].max() / 1000000, 2)), 'Mbps')
print('Week 3 - ', str(round(Week3['Outbound'].max() / 1000000, 2)), 'Mbps')
print('Week 4 - ', str(round(Week4['Outbound'].max() / 1000000, 2)), 'Mbps')
