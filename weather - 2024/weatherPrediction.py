import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import warnings

# Load the dataset
file_path = "/content/tennis.csv"
data = pd.read_csv(file_path)

# Drop the "Formatted Date" attribute
data = data.drop(columns=["day"])#,"Precip Type","Summary"

label_encoder = LabelEncoder()
for i in data.columns:
  data[i] = label_encoder.fit_transform(data[i])

data.head(10)

#to get the shape of the data
print(data.shape) #expected output: (1599, 12)

#to get the head values of our data set i.e first 5 table values of our dataset
data.tail()
len(data)

#to check weather the dataset had any missing values
data.isnull().sum()

# #to check weather the dataset had duplicate row values
# num_duplicate_rows = data.duplicated().sum()

# print("Number of duplicate rows:", num_duplicate_rows)

#to remove the duplicate data rows from the dataset and give the shape of the dataset
# data_cleaned = data.drop_duplicates()
# print("Shape of cleaned DataFrame:", data_cleaned.shape)
# data=data_cleaned

#to get the statistical measures of the dataset
data.describe()

x=data[['humidity', 'wind']]
#to see the quality values print them in next step
print(x)

y=data['play']
#to check weather the the labels of quality had changed print the next statement.
print(y)



from sklearn.ensemble import AdaBoostClassifier
import sklearn.model_selection as sm

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = sm.train_test_split(x, y, test_size=0.2, random_state=2)

# Check the shapes of the data
print(y.shape, y_train.shape, y_test.shape)

# Model training using AdaBoostClassifier
model = AdaBoostClassifier(n_estimators=5, random_state=3)  # You can adjust the number of estimators as needed
model.fit(x_train, y_train)
 #x_train contains all the training data and y train contains the label data
#that is quality values (0,1)
print(x_train, y_train)

#8th step  Evaluate the model (model evaluation)
#We are going to use accuracy score values
# accuracy on test data
x_test_prediction = model.predict(x_test)
#we are predicting the label values
# now compare the values predicted by model with actual data values
test_data_accuracy = accuracy_score(x_test_prediction, y_test) #y_test contain real actual values
#to print the accuracy of the model
print('The accuracy of our trained model is: ', test_data_accuracy*100,'%')

#step 8 Building a predictive system and preditc
#Build a code that will predict all the chemical values
# Your processing logic here, for example:
Input_data = (2,    0   )
Input_data_as_numpy_array = np.asarray(Input_data)
Input_data_reshape = Input_data_as_numpy_array.reshape(1,-1)
# Suppress the specific warning using exception handling
try:
  with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=UserWarning, message="X does not have valid feature names")
    prediction = model.predict(Input_data_reshape)
except Warning:
  # Handle the warning if needed
  pass  # You can customize this part to handle the warning in a specific way
print(prediction)