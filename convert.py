import pandas as pd

for i in range(1, 5):
    file = pd.read_csv('new_data_{}.txt'.format(i))
    new_csv_file = file.to_csv('new_data_{}.csv'.format(i), index = False)