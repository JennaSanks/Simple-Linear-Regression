from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        # Get input from HTML form
        years = float(request.form["years"])

        # Make prediction
        prediction = model.predict([[years]])[0]

        # Round prediction
        prediction = round(prediction, 2)

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)