import pickle
import pandas as pd
from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance

# Load model
model_path = r'c:\Users\Matheus\Documents\projects\propensao_de_compra\models\model_random_forest.pkl'
try:
    model = pickle.load(open(model_path, 'rb'))
except FileNotFoundError:
    print(f"Model file not found at {model_path}")
    raise

# Initialize API
app = Flask(__name__)

@app.route('/healthinsurance/predict', methods=['POST'])
def health_insurance_predict():

    data = request.get_json()
    
    # Determine the structure of the data
    if isinstance(data, dict):
        # Dictionary: Directly to DataFrame
        df = pd.DataFrame([data]) if not all(isinstance(v, list) for v in data.values()) else pd.DataFrame(data)
    elif isinstance(data, list):
        # List of dictionaries: Directly to DataFrame
        if all(isinstance(item, dict) for item in data):
            df = pd.DataFrame(data)
        else:
            # List of lists: Add column names manually
            df = pd.DataFrame(data, columns=['id', 'gender', 'age', 'driving_license', 'region_code',
       'previously_insured', 'vehicle_age', 'vehicle_damage', 'annual_premium',
       'policy_sales_channel', 'vintage', 'response'])
    else:
        return Response(f'{{"Unsupported format/columns error": "{str(e)}"}}', status=400, mimetype='application/json')
    
    original_data = df.copy()

    try:
        # Instantiate pipeline
        pipeline = HealthInsurance()
        
        # Apply transformations
        df1 = pipeline.data_cleaning(df)
        df2 = pipeline.feature_engineering(df1)
        df3 = pipeline.data_preparation(df2)

        try:
            # Get predictions
            df_response = pipeline.get_prediction(model, original_data, df3)
        except Exception as e:
            return Response(f'{{"Prediction error": "{str(e)}"}}', status=100, mimetype='application/json')

        # Return response
        return Response(df_response, status=200, mimetype='application/json')

    except Exception as e:
        return Response(f'{{"Pipeline error": "{str(e)}"}}', status=500, mimetype='application/json')

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)