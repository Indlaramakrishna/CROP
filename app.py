from flask import Flask, render_template,jsonify,request
import pickle


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')



@app.route('/prediction',methods = ['GET','POST'])
def prediction():
    if request.method == 'POST':
        nitro = request.form.get('nitrogen')
        phos  = request.form.get('phosphorus')
        kp    = request.form.get('potassium')
        temp  = request.form.get('temperature')
        hum   = request.form.get('humidity')
        ph    = request.form.get('ph')
        rain  = request.form.get('rainfall')
    
        with open('model.pkl','rb') as model_file:
            mlmodel = pickle.load(model_file)
        res = mlmodel.predict([[float(nitro),float(phos),float(kp),float(temp),float(hum),float(ph),float(rain)]])
        return render_template("result.html",res=res)
    else:
        return render_template('prediction.html')

if __name__=='__main__':
    app.run()
