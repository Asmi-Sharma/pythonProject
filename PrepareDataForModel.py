# import pandas as pd
# class PrepareData:
#     def __init__(self, timeSeriesData):
#         self.timeSeriesData = timeSeriesData
#
#     def timeSeries(self):
#         # print(timeSeriesData.head(10))
#         # print("Index=\n ",timeSeriesData.index)
#         resampledData = timeSeriesData.resample('D').mean()
#         # print("Resample data= \n",resampledData)
#         return resampledData
#
#
#
#
# timeSeriesData = pd.read_csv('NepalCovidDataSample.csv', header=0, parse_dates=['date'], index_col='date', squeeze=True)
# print(timeSeriesData)
# # timeSeriesData.info()
#
# p = PrepareData(timeSeriesData)
# resampledData = p.timeSeries()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import csv

def normalize(covidData):
    # timeSeriesData = covidData.set_index(pd.DatetimeIndex(covidData['date']))
    # resampledData = timeSeriesData.resample('M').mean()
    # scalar = MinMaxScaler(feature_range=(0,1))
    # scalar = scalar.fit(resampledData)
    # normalizedData = scalar.transform(resampledData)
    # normalizedData = pd.DataFrame([normalizedData.flatten()])
    # normalizedData = normalizedData.T
    # normalizedData = normalizedData.set_index(pd.DatetimeIndex(resampledData.index))
    # normalizedData = normalizedData.rename(columns={0: 'new_cases'})
    # return normalizedData

    # data = pd.read_csv("NepalCovidDataSample.csv")
    # print(data)
    new_case = covidData['new_cases']
    # print('new cases\n',new_case)
    print('Length = ', len(new_case))
    # mean and standard deviation
    mean_value = new_case.mean()
    SD_value = new_case.std()
    print('Mean =', mean_value)
    print('SD = ', SD_value)

    # z-score calculation
    # cols = list(new_case.columns)
    # print(cols)
    zscore_value = []
    for i in range(len(new_case)):
        z_score = (new_case[i] - mean_value) / SD_value
        zscore_value.append(z_score)
    print(zscore_value)
    z = pd.DataFrame(zscore_value)
    return z

def splitData(normalizedData):
    train, test = train_test_split(normalizedData, test_size = 0.25, shuffle=False)
    test, forecast = train_test_split(test, test_size = 0.45, shuffle=False)
    return train,test,forecast

    # f = open("train.csv","w") #csit.csv file open garya write mode ma
    # csvwrite = csv.writer(f)
    # header = ['new_case']
    # csvwrite.writerow(header)
    # csvwrite.writerows(train)
    # f.close()




