# -*- coding: utf-8 -*-
"""Churn_Modelling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VH8JTI_jz9U69y5Z0w-o9ipdP_5B3aor

<h1><center>Explaination On Artificial Neural Netowrk</center></h1>
<p align="center">
  <img src="https://github.com/amit17133129/codes/blob/master/Brain.gif?raw=true" alt="Sublime's custom image"/>
</p>

<center>An ANN is based on a collection of connected units or nodes called artificial neurons, which loosely model the neurons in a biological brain. Each connection, like the synapses in a biological brain, can transmit a signal to other neurons. An artificial neuron that receives a signal then processes it and can signal neurons connected to it. The "signal" at a connection is a real number, and the output of each neuron is computed by some non-linear function of the sum of its inputs. The connections are called edges. Neurons and edges typically have a weight that adjusts as learning proceeds. The weight increases or decreases the strength of the signal at a connection. Neurons may have a threshold such that a signal is sent only if the aggregate signal crosses that threshold. Typically, neurons are aggregated into layers. Different layers may perform different transformations on their inputs. Signals travel from the first layer (the input layer), to the last layer (the output layer), possibly after traversing the layers multiple times.</center>

## **Importing Pandas**

<center>Pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.</center>
"""

import pandas as pd

"""## **Importing Dataset**

Here i have imported dataset of churn modelling in which you have features like 'RowNumber', 'CustomerId', 'Surname', 'CreditScore', 'Geography',
       'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
       'IsActiveMember', 'EstimatedSalary', 'Exited'.
"""

dataset = pd.read_csv("/content/Churn_Modelling.csv")
dataset

dataset.columns

"""As the *Exited* feature is to be in Y variable so below i am creating a y variable with *Exited* feature in that variable."""

y = dataset['Exited']

"""X will contains `['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
                  'IsActiveMember', 'EstimatedSalary']` features.
"""

X = dataset[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
                  'IsActiveMember', 'EstimatedSalary']]
X.shape

"""# **One Hot Encoding For Geography Feature**
Here as you can see in the *Geography* reason you have you have three columns after one hot encoding i.e Germany, Spain, France. So to avoid dummy trap i have used a fn from pandas i.e `get_dummies` in which i have use  `drop_first=True` that will helps us to avoid dummy trap.
"""

Geo = pd.get_dummies(dataset['Geography'], drop_first=True)
Geo

"""## **One Hot Encoding For *Gender* Feature**
Here as you can see in the Geography reason you have you have three columns after `one hot encoding` i.e Germany, Spain, France. So to avoid dummy trap i have used a fn from pandas i.e `get_dummies` in which i have use `drop_first=True` that will helps us to avoid dummy trap.
"""

Gender = pd.get_dummies(dataset['Gender'], drop_first=True)
Gender

"""**Concatinating X, Geo, Gender**"""

X = pd.concat([X, Geo, Gender], axis=1)
X.shape

"""**importing *train_test_split***

Before feeding your data into the neural network you need to split that data into `training set` and `testing set`. this can be done using 

```
train_test_split method from sklearn library and from model_selection module
```

<p align="center">
  <img src="https://github.com/amit17133129/codes/blob/master/train_test_split.gif?raw=true" alt="Sublime's custom image"/>
</p>
"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=40)



"""## importing Sequrntial Model From keras """

from keras.models import Sequential
model = Sequential()            # creating Empty model

"""#**Importing Dense Layer**"""

from keras.layers import Dense

"""**Adding First Layer to model with neurons=8, input_feature=11 and activation fn = relu (rectified linear unit)**"""

model.add(Dense(units=8, activation='relu', input_dim=11))

"""`Relu`  is an activation function i.e its will activate the neurons in the hidden layers. The main functions of `relu` is that all the output from a layers from all the neuron will pass to another layers of the respective neurons.

<p align="center">
  <img src="https://github.com/amit17133129/codes/blob/master/Relu.gif?raw=true" alt="Sublime's custom image"/>
</p>

## Adding Second Layer with neurons=6 and activation fn = relu  
In this layer i have used `6 neurons` and with the `relu` activation fn.
"""

model.add(Dense(units=6, activation='relu'))

"""# Adding third layer with neurons=6 and activation fn = relu
In this layer i have used `6 neurons` and with the `relu` activation fn.
"""

model.add(Dense(units=6, activation='relu'))

"""# Adding last layer with neurons=1 and activation fn = relu
In this layer i have used `1 neuron` and with the `sigmoid` activation fn. As you can see in the below image after summation from all the neurons then the output goes to `sigmoid` fn and that fn will gives you a `binary` output (1/0). As it is giving onlu one output then only `one neuron` is required.

<p align="center">
  <img src="https://eecs.wsu.edu/~cook/dm/lectures/l5/img43.gif" alt="Sublime's custom image"/>
</p>
"""

model.add(Dense(units=1, activation='sigmoid'))

model.get_config()

"""## A  visaul Explaination of the Artificial Neural Network

![DeeepLearning](https://github.com/amit17133129/codes/blob/master/Deep%20learning.gif?raw=true)
"""

model.summary()

"""As you can see in below <b> `Optimizers Comaprision` </b> You will find that there are different tyes of optimizers are shown. In which they have different speed to move. This speed denotes the learning from the weights. if your optimizers have less speed then it will learn more things but as you can see in terms of <i> `Ada Delta` </i> the speed is quite high. So its jups and moves out of the graph. where as in case of <i>`Adam`</i> because i have used Adam you will find that speed of learning from the weights is quite slow compare to <i>`Ada Delta`</i>. Also you need to set the ```learning rate``` to move your optimizers very slowly. So, it can learn much more from the respective weights.

<p align="center">
  <img src="https://mlfromscratch.com/content/images/2019/12/saddle.gif" alt="Sublime's custom image"/>
</p>
"""

from keras.optimizers import Adam

"""As i have only one output that whether the Employee is exited from the company or not. i.e  Binary output (Exited/notexited). So the loss will be generating in binary. To handle the binary loss we have `binary_crossentropy`."""

model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.000001))

"""<center><h1>Below You will find the weights of the model</h1></center>"""

model.get_weights()

"""<center><h1>Training Phase</h1></center>

For training the model we need to fit the model and it require training data i.e `X_train`, `y_train`. And the `epochs is 100`. That means your training data will goes 100 times through the neural network which you have build above with the respective layers.

<p align="center">
  <img src="https://github.com/amit17133129/codes/blob/master/feedforward_backpropagation.gif?raw=true" alt="Sublime's custom image"/>
</p>
"""

model.fit(X_train, y_train, epochs=100)

loss = pd.DataFrame(model.history.history)
loss

"""## Plotting Loss Graph
As you can see the graph of the loss is slowly decreasing. So this can be possible because of `Adam` Optimizers
"""

loss.plot()

"""## Prediction
To predict i am just giving random iputs but you can use the right values and it will predict on that case.

"""

print("The employee will  :", model.predict([[1,2,3,4,5,6,7,8,9,10,11]])[0][0])

