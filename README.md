###Introduction

The project might help someone who is trying to sell a used car. The user need to to put following inputs to get the predicted selling price of the car.

1. Location - The user need to select from the given location from the given list.
2. Fuel Type - The user need to select the fuel type of the car from the given list.
3. Transmission - The user need to select the transimission type of the car from the list.
4. Year - The year in which the car was purchased.
5. Kilometers Driven - Total kilometer driven by the car till present.
6. Owner - The owner need to mention whether he/she is the first , second or third user of the car as 1 , 2 or 3 respectively.
7. Mileage - The user need to input the mileage of the car in kmpl.
8. Engine - The user need to input the engine displacement of the car in CC.
9. Power - The user need to input the power of the car in bph.

###Model

Random Forest Regression model is used to predict the output. It was used because it can handle all the input variables without variable deletion andiIt gives estimates of what variables that are important in the classification.
The linear regression as well as lasso regression was used to predict the model. But it yield less accuracy rate. So, random forest regression was choosen with the accuacy rate of 86%.

###Deploy

Heroku cloud platform as a service was used to deploy the model.
Link for the webpage to predict the selling price of used car ( https://usedcar-prediction-api.herokuapp.com/ )
