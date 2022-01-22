import pickle
from flask import Flask,render_template,request

# Deployed link
# https://housing-unit.herokuapp.com/

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result',methods = ['GET','POST'])

def predict():
    area = request.form.get('area')
    bedrooms = request.form.get('bedrooms')
    bathrooms = request.form.get('bathrooms')
    stories = request.form.get('stories')
    mainroad = request.form.get('mainroad')
    guestroom = request.form.get('guestroom')
    basement = request.form.get('basement')
    hotwaterheating = request.form.get('hotwaterheating')
    hotwaterheating = request.form.get('airconditioning')
    parking = request.form.get('parking')
    prefarea = request.form.get('prefarea')
    furnishingstatus = request.form.get('furnishingstatus')
    prediction = model.predict([[area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,hotwaterheating,parking,prefarea,furnishingstatus]])
    # print(area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,hotwaterheating,parking,prefarea,furnishingstatus)
    res = round(prediction[0],2)
    # res = int(prediction)
    print(res)
    return render_template('index.html',prediction_test  = f'The Price of house is Rs.{res}/- ')


if __name__=='__main__':
    app.run(debug=True)    