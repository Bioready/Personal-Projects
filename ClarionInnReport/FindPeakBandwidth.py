import pandas as pd

data = pd.read_csv('ClarionInnUsage.csv')
data_index = data.set_index('Date')

print('----- WEEKLY BANDWIDTH USAGE -----')


Week1 = data.loc[1:92, 'Outbound'].max() / 1000000
Week2 = data.loc[92:188, 'Outbound'].max() / 1000000
Week3 = data.loc[189:284, 'Outbound'].max() / 1000000
Week4 = data.loc[285:374, 'Outbound'].max() / 1000000

WeeklyBandwidth = (Week1, Week2, Week3, Week4)

for weeks in WeeklyBandwidth:
    print(str(round(weeks, 2)), 'Mbps')
