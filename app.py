from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)


model = joblib.load('xgboost_solar_model.pkl')
scaler = joblib.load('solar_data_scaler.pkl')


expected_features = list(scaler.feature_names_in_)

@app.route('/')
def home():
    
    return render_template('index.html', features=expected_features, prediction_text="")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        form_data = request.form.to_dict()
        
        
        input_dict = {key: float(value) for key, value in form_data.items()}
        
        
        df = pd.DataFrame([input_dict])
        
        
        df = df[expected_features]
        
        
        scaled_data = scaler.transform(df)
        prediction = model.predict(scaled_data)
        output = round(float(prediction[0]), 2)
        
        return render_template('index.html', features=expected_features, prediction_text=f'⚡ প্রেডিক্টেড সোলার এনার্জি: {output} Wh')
    
    except Exception as e:
        return render_template('index.html', features=expected_features, prediction_text=f'❌ Error: দয়া করে সব ফিল্ডে সঠিক সংখ্যা বসান!')

if __name__ == "__main__":
    app.run(debug=True)