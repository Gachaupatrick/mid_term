import pickle, pandas as pd
from flask import Flask, request, jsonify

# load saved model
model_file = "model/xgb_model.bin"
with open(model_file, "rb") as f_in:
    xgb_model = pickle.load(f_in)
    
# Intialize the Flask app
app = Flask("stockout")

# Define the predict route
@app.route("/predict", methods=["POST"])
def predict():
    sku = request.get_json()  #will get the json file below and return it as a python dictionary
    
    # Convert the dictionary into a Pandas DataFrame so XGBoost can read it
    df = pd.DataFrame([sku]) 
    
    # Get probability
    y_pred = xgb_model.predict_proba(df)[0,1]
    
    # Binary decision    
    is_stockout = bool(y_pred >= 0.5)
    
    result = {
        'stockout_probability': float(y_pred),
        'stockout': is_stockout
    }
    
    return jsonify(result)

if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement.
    app.run(host= "127.0.0.1", debug=True, port=9696)
    
#the information will be sent and received in JSON format that uses double quotes instead of single qoutes
  