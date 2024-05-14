from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('templates/model.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    # Assuming prediction is a list in the format [0.00, 0.67, 0.33]
    #prediction_probability = prediction[0][1]  # Access the second element of the list
    #output='{0:.{1}f}'.format(prediction[0][1], 2)
    output = '{:.2f}'.format(prediction[0][1])

    if prediction[0][1] > 0.5:
       pred_message = 'You are Diabetic.\nProbability of diabetes occurring is {:.2f}'.format(prediction[0][1])
    else:
       pred_message = 'You are not Diabetic.\nProbability of diabetes occurring is {:.2f}'.format(prediction[0][1])

    #if output > 0.5:
       #pred_message = 'You are Diabetic.\nProbability of diabetes occurring is {:.2f}'.format(output)
    #else:
       #pred_message = 'You are not Diabetic.\nProbability of diabetes occurring is {:.2f}'.format(output)

# Return the template with the prediction message
    return render_template('index.html', pred=pred_message, bhai="kuch karna hain iska ab?")

if __name__ == '__main__':
    app.run(debug=True)
    
