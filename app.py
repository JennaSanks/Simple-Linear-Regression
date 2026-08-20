from flask import Flask,render_template,request
import pickle
import numpy as np

# Templates are stored in the project's HTML folder rather than Flask's
# default "templates" folder.
app=Flask(__name__, template_folder="HTML")

model=pickle.load(open("SLRModel.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])


def predict():

    cgpa=float(request.form['cgpa'])

    prediction=model.predict(np.array([[cgpa]]))

    return render_template(
        "index.html",
        prediction_text=f"Predicted Package : {prediction[0]:.2f} LPA"
    )

if __name__=="__main__":
    app.run(debug=True)