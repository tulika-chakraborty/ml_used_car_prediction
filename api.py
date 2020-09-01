import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__,template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    Ahmedabad = 1 if request.form['Location'] == 'Ahmedabad' else 0
    Bangalore=  1 if request.form['Location'] == 'Bangalore' else 0
    Chennai =  1 if request.form['Location'] == 'Chennai' else 0
    Coimbatore =  1 if request.form['Location'] == 'Coimbatore' else 0
    Delhi =  1 if request.form['Location'] == 'Delhi' else 0
    Hyderabad =  1 if request.form['Location'] == 'Hyderabad' else 0
    Jaipur =  1 if request.form['Location'] == 'Jaipur' else 0
    Kochi = 1 if request.form['Location'] == 'Kochi' else 0
    Kolkata =  1 if request.form['Location'] == 'Kolkata' else 0
    Mumbai =  1 if request.form['Location'] == 'Mumbai' else 0
    Pune =  1 if request.form['Location'] == 'Pune' else 0
    CNG = 1 if request.form['FuelType']=='CNG' else 0
    Diesel = 1 if request.form['FuelType']=='Diesel' else 0
    LPG = 1 if request.form['FuelType']=='LPG' else 0
    Petrol = 1 if request.form['FuelType']=='Petrol' else 0
    Automatic = 1 if request.form['Transmission']=='Automatic' else 0
    Manual = 1 if request.form['Transmission']=='Manual' else 0
    Year=int(request.values.get('Year'))
    Kilometers_Driven=float(request.values.get('KilometersDriven'))
    Owner_Type=float(request.values.get('OwnerType'))
    Mileage=float(request.values.get('Mileage'))
    Engine=float(request.values.get('Engine'))
    Power=float(request.values.get('Power'))
    
    features [0] = Ahmedabad
    features [1] = Bangalore
    features [2] = Chennai
    features [3] = Coimbatore
    features [4] = Delhi
    features [5] = Hyderabad
    features [6] = Jaipur
    features [7] = Kochi
    features [8] = Kolkata
    features [9] = Mumbai
    features [10] = Pune
    features [11] = CNG
    features [12] = Diesel
    features [13] = LPG
    features [14] = Petrol
    features [15] = Automatic
    features [16] = Manual
    features [17] = Year
    features [18] = Kilometers_Driven
    features [19] = Owner_Type
    features [20] = Mileage
    features [21] = Engine
    features [22] = Power

    final_features = np.array(features)
    print(final_features)
    prediction = model.predict([final_features])
    output = round(prediction[0], 2)
    

   
    return render_template('./index.html', prediction_text='Selling Price is Rs {} lakhs'.format(output))


if __name__ == "__main__":
    app.run(debug=True)

