import pandas as pd
import PrepareDataForModel as pdm
import cnnAlgorithm as cnna

class Main:
    def __init__(self):
        self.covidData =pd.read_csv('NepalCovidDataSample.csv', header=0, squeeze=True)
        self.covidData = self.covidData[['new_cases','date']]

    def prepareDataset(self):
        normalizedData = pdm.normalize(self.covidData)
        self.train, self.test, self.forecast = pdm.splitData(normalizedData)

    def trainData(self):
        cnna.fit_model(self.train, self.test)
        # lstmAlgorithm()

    # def testModel(self):
    #
    # def forecast(self):


m = Main()
m.prepareDataset()
m.trainData()
