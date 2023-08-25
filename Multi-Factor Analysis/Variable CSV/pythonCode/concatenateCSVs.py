import pandas as pd

dataframes = []
file_names = ['averageInternetSpeedBroadband.csv',
              'averageInternetSpeedMobile.csv',
              'digitalCompetetiveness2022.csv',
              'eSportsEarnings.csv',
              'freedomeHouseIndex.csv',
              'genderInequalityIndex2022.csv',
              'humanDevelopmentIndex2022.csv',
              'internetFreedomIndex.csv',
              'nominalGDP.csv',
              'historicOlympicMedals.csv',
              'pppGDP.csv',
              'pppGDPperCapita.csv'
              ]

for file_name in file_names:
    # Annahme: Die Ländernamen befinden sich in der ersten Spalte (0) und die Indexwerte in der zweiten Spalte (1).
    df = pd.read_csv(file_name, header=None, names=['Country', file_name.split('.')[0]])
    dataframes.append(df)

# Führen Sie eine äußere Verknüpfung der DataFrames basierend auf den Ländernamen durch.
combined_df = dataframes[0]
for df in dataframes[1:]:
    combined_df = pd.merge(combined_df, df, on='Country', how='outer')

print(combined_df)
combined_df.to_csv('MulitFactorTable.csv')