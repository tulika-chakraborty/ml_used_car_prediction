## [Machine Learning] Predict used cars resale value 

URL: https://usedcar-prediction.herokuapp.com/
     
###  Introduction
This project might help someone to predict the resale value of his/her car. The user needs to fill in the following fields for the Machine Learning tool to predict the selling price.

1. Location - current city
2. Fuel Type
3. Transmission Type
4. Year - the year of purchase
5. Kilometers Driven - total distance driven in kms
6. Owner - number of owners (1, 2, 3...)
7. Mileage - kmpl
8. Engine - engine displacement of the car in CC.
9. Power - power of the car in bph

### Model

**Random Forest Regression** model is used in the project to predict the resale value of the car. Random Forest Regression can handle all the input variables without variable deletion and it gives an estimate of the variables that are important in the classification.

Random Forest Regression model was chosen over *Linear Regression* and *Lasso Regression* models because the former was able to provide much higher accuracy rates in predicting the selling price.

Random Forest Regression gave an accuracy rate of 86%.

###  Demo

Heroku cloud platform services was used to host the web application.
URL: https://usedcar-prediction-api.herokuapp.com