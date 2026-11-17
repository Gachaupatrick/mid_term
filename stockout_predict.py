import pickle

from flask import Flask
from flask import request
from flask import jsonify #turn python dict in our result back to json


model_file = "xgb_model.bin"

with open(model_file, "rb") as f_in: #change wb to rb for reading
    xgb_model = pickle.load(f_in)
    
app = Flask("stockout")

@app.route("/predict", methods=["POST"])
def predict():
    sku = request.get_json()  #will get the json file below and return it as a python dictionary 
    
    # Get probability
    y_pred = xgb_model.predict_proba(sku)[0,1]
    
    # Binary decision    
    is_stockout = bool(y_pred >= 0.5)
    
    result = {
        
        # Cast both values explicitly to standard Python float() and bool() types inside your dictionary
        # Why : because Flask is returning a NumPy boolean or float type, which standard Python jsonify cannot serialize into JSON.
        'stockout_probability': float(y_pred), 
        'stockout': is_stockout
        
    }
    
    return jsonify(result)

if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement.
    app.run(host= "127.0.0.1", debug=True, port=9696)
    
#the information will be sent and received in JSON format that uses double quotes instead of single qoutes
  