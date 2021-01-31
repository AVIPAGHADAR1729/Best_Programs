import numpy as np
import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OneHotEncoder


class aviApp:
    read = pd.read_csv('abcd.csv').drop(columns=['Unnamed: 0'])
    df = read.select_dtypes(include=['object']).copy()
    Result = None
    model = GaussianNB()
    Line = None
    

    def __init__(self,data):
        
        df = self.df.replace(self.cleanObjects())
        trainX = df.drop(columns=['play'],axis=1)
        trainY = self.read['play']
        dt = {
            'outlook':[data[0]],
            'temprature':[data[1]],
            'humidity':[data[2]]
        }
        self.model.fit(trainX,trainY)
        self.Result = list(self.model.predict(self.testData(dt)))

        self.Line = self.inputTestSetDict(data)
        self.Line['play'] = self.Result

        from csv import reader,writer

        addData = list(map(lambda x: "".join(x),self.Line.values()))
        #print(addData)
        file_name = 'abcd.csv'
        A = list(reader(open(file_name)))
        A.remove([])
        addData.insert(0,str(int(A[-1][0])+1))
        #print(addData)
        A = list(map(lambda x: x[1:],A))
        #print(A)

        with open(file_name,'a+',newline='') as obj:
            if addData[1:] in A:
                pass
            else:
                write = writer(obj)
                write.writerow(addData)
        
        
    def getPrediction(self):
        return self.Result
    
    
    def __str__(self):
        return str(self.Line)

    def cleanObjects(self):
        clean_data = {
            'outlook' : {'sunny':1,'rainy':2,'overcast':3},
            'temprature' : {'hot':1,'mild':2,'cool':3},
            'humidity' : {'high':1,'normal':2}
        }
        return clean_data

    def testData(self,dt):
        testData = pd.DataFrame(dt)
        testData = testData.select_dtypes(include=['object']).copy()
        testData = testData.replace(self.cleanObjects())
        return testData
    

    def inputTestSetDict(self,data):
        dt = {
        'outlook':[data[0]],
        'temprature':[data[1]],
        'humidity':[data[2]]
        }
        return dt

    
    
    
    

    
##if __name__ == '__main__':
##    avi = aviApp(['sunny','cool','normal'])

  
        
