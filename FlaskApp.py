from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('dt_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_default(GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE,
                    ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN):
    
    # Making predictions
    prediction = model.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE,
                                 ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])

    # Convert the prediction to a more understandable form
    if prediction == 1:  # Assuming 1 indicates presence of cancer
        pred = 'Presence of lung cancer'
    else:
        pred = 'Absence of lung cancer'
    
    return pred

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        AGE = int(request.form['AGE'])
        SMOKING = int(request.form['SMOKING'])
        YELLOW_FINGERS = int(request.form['YELLOW_FINGERS'])
        ANXIETY = int(request.form['ANXIETY'])
        PEER_PRESSURE = int(request.form['PEER_PRESSURE'])
        CHRONIC_DISEASE = int(request.form['CHRONIC_DISEASE'])
        FATIGUE = int(request.form['FATIGUE'])
        ALLERGY = int(request.form['ALLERGY'])
        WHEEZING = int(request.form['WHEEZING'])
        ALCOHOL_CONSUMING = int(request.form['ALCOHOL_CONSUMING'])
        COUGHING = int(request.form['COUGHING'])
        SHORTNESS_OF_BREATH = int(request.form['SHORTNESS_OF_BREATH'])
        SWALLOWING_DIFFICULTY = int(request.form['SWALLOWING_DIFFICULTY'])
        CHEST_PAIN = int(request.form['CHEST_PAIN'])

        # Get the prediction
        prediction = predict_default(AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE,
                                     ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN)
        
        # Return the result to a template or just render the result directly
        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

