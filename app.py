from flask import Flask, render_template, request
import pickle
import numpy as np

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = 'Model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value


@app.route('/', methods=['POST', 'GET'])
def index():
   
    pred_value = 0
    if request.method == 'POST':
        ram = request.form['ram']
        storage = request.form['storage']
        BatteryCapacity = request.form['battery_capacity']
        Brand = request.form['brand_t']
        # print(ram)
        # print(storage)
        # print(BatteryCapacity)
        # print(Brand)
        feature_list = []
        feature_list.append(int(storage))
        feature_list.append(int(ram))
        feature_list.append(int(BatteryCapacity))
        
   

       
        
        Brand_list = ['apple','huawei', 'motorola', 'nokia',  'onePlus','oppo','other', 'realme', 'samsung', 'vivo', 'xiaomi']
        
        #check select brand and brand list name    
        for br in Brand_list:
            if br == Brand:
                 index_number = Brand_list.index(br)
                 feature_list.append(index_number)
                 break

             
    pred_value=prediction(feature_list)*301.50
    pred_value = np.round(pred_value[0])
    
    return render_template('index.html', pred_value=pred_value)  
if __name__ == '__main__':
    app.run(debug=True)