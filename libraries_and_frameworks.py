#pip install library_name
#numpy - provides support for multi-dimensional arrays and matrices
import numpy as np
a=np.array([1, 2, 3])
print("Array: ",a)
print("Mean of array: ", np.mean(a))

#panda - offers data manipulation and analysis tools
import pandas as pd
data ={"Name":['John', 'Anna', 'James'], 'Age':[28,24,25]}
df=pd.DataFrame(data)
print(df)

#matplotlib =library for creating static, animated, and interactive visualizations in Python
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('Example Numbers')
plt.show()

#scikit-learn = tool for data mining and data analysis
from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(random_state=0)
x=[[1,2,3],[11,12,13]] #2 samples, 3 features
y=[0,1] #classes of each sample
clf.fit(x,y)

#pip install framework_name
#example of Python Frameworks:

#example Django view
from django.http import HttpResponse

def helleWorld(request):
    return HttpResponse("Hello,world")

#Flask - lightweight and easy to extend
from flask import Flask
app =Flask(__name__)
@app.route('/')
def helloWorld():
    return 'Hello world!'

