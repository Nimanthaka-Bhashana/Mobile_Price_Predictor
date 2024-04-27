from flask import Flask, render_template, request
import pickle
import numpy as np

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = 'Model/predictor1.pickle1'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value


@app.route('/', methods=['POST', 'GET'])
def index():
    pred_value = 0
    feature_list = []  # Initialize feature_list here
    
    if request.method == 'POST':
        ram = request.form['ram']
        storage = request.form['storage']
        BatteryCapacity = request.form['battery_capacity']
        Brand = request.form['brand_t']
        Model=request.form['model_t']
        
       
       
        
        Brand_list = ['apple','huawei', 'motorola', 'nokia',  'onePlus','oppo','other', 'realme', 'samsung', 'vivo', 'xiaomi']
        Model_list = ['Galaxy', 'Mi', 'Moto', 'Narzo', 'Nord', 'Pixel', 'Poco', 'Redmi', 'iPhone', 'Other']
        Battery_Capacity_list = ['2000', '3000', '4000', '5000', '6000', '7000']
        Storage_list = ['32', '64', '128', '256', '512']
        #RAM_list = [4, 6, 8, 3, 12, 2, 5, 16]

        # Check selected Model and add its index to feature_list
        for sl in Storage_list:
            if sl == storage:
                 index_number_sl = Storage_list.index(sl)
                 feature_list.append(index_number_sl)
                 break
         
         # Check selected ram and add to feature_list
        feature_list.append(int(ram))
        
         # Check selected Battery_Capacity and add its index to feature_list
        for bc in Battery_Capacity_list:
            if bc == BatteryCapacity:
                 index_number_bc = Battery_Capacity_list.index(bc)
                 feature_list.append(index_number_bc)
                 break    
        # Check selected brand and add its index to feature_list
        for br in Brand_list:
            if br == Brand:
                 index_number = Brand_list.index(br)
                 feature_list.append(index_number)
                 break
         # Check selected Model and add its index to feature_list
        for md in Model_list:
            if md == Model:
                index_number_md = Model_list.index(md)
                feature_list.append(index_number_md)
                break
          
    # Check if feature_list is not empty before making prediction
    if feature_list:
       
        pred_value = prediction(feature_list) * 301.50
        pred_value = np.round(pred_value[0])
    
    return render_template('index.html', pred_value=pred_value)  


if __name__ == '__main__':
    app.run(debug=True)
