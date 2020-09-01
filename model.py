import pandas as pd
import numpy as np
import pickle

final_car=pd.read_csv('./final_car.csv')
from sklearn.model_selection import train_test_split
x = final_car.iloc[:, :-1]
y = final_car['Price']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor()
rf_reg.fit(X_train, y_train)
print(final_car.dtypes)

# Saving model to disk

pickle.dump(rf_reg, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
