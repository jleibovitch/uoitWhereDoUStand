
# coding: utf-8

# In[814]:


import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.svm.libsvm import predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
from sklearn.metrics import classification_report, accuracy_score


# In[815]:


yearOne = pd.read_csv('normal_y1_gpa.csv')
yearTwo = pd.read_csv('y2_gpa.csv')


# In[816]:


del yearOne['Unnamed: 0']
del yearTwo['Unnamed: 0']
del yearOne['hashedID']
yearOne.head()


# In[817]:


#del yearOne['hashedID']


# In[818]:


# def calc_gpa(as):
#     data = [r for r in row]
#     print(data)
#     return np.round(np.mean(data), 2)


# In[819]:


# yearOne['gpa'] = yearOne.iloc[0:10].apply(calc_gpa, axis=1)


# In[820]:


#yearOne.head()


# In[821]:


def gpa_cat(gpa):
    if 0 <= gpa <= 2.7:
        return 0 
    elif 2.7 < gpa <= 2.9:
        return 1
    else:
        return 2


# In[822]:


yearOne['gpa'] = yearOne['gpa'].apply(gpa_cat)


# In[823]:


yearOne.head()


# In[824]:


#yearOne.tail()


# In[825]:


np.unique(yearOne['gpa'])


# In[826]:


X = yearOne.drop('gpa', axis=1)
y = yearOne['gpa']


# In[827]:


xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.30, random_state=42)


# In[828]:


scaler = StandardScaler()
xScaled = scaler.fit_transform(xTrain)


# In[829]:


svmmodel = SVC()
svmmodel.fit(xScaled, yTrain)


# In[830]:


xScaledTest = scaler.transform(xTest)
predictions = svmmodel.predict(xScaledTest)


# In[831]:


print(classification_report(yTest, predictions))
print("Accuracy: {}".format(accuracy_score(yTest, predictions)))


# In[832]:


newData = pd.DataFrame({
        #'hashedID':[1111], 
        'course1':[2.83],
        'course2':[3.29], 
        'course3':[2.55],
        'course4':[1.78],
        'course5':[2.24], 
        'course6':[3.44], 
        'course7':[2.23],
        'course8':[3.23],
        'course9':[2.79],
        'course10':[2.1],  
        'course11':[3.2],
        'course12':[2.79]
})


# In[833]:


#testScale = scaler.transform(newData)
predictions = svmmodel.predict(newData)
predictions


# In[834]:


newData2 = pd.DataFrame({
        #'hashedID':[2222], 
        'course1':[0],
        'course2':[0], 
        'course3':[0],
        'course4':[0],
        'course5':[0], 
        'course6':[0], 
        'course7':[0],
        'course8':[0],
        'course9':[0],
        'course10':[0],  
        'course11':[0],
        'course12':[0]
})


# In[835]:


testScale2 = scaler.transform(newData2)
print(testScale2)
# predictions2 = svmmodel.predict(newData2)
# predictions2

