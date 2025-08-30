from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load("dbs.jl")  # loads the trained model

@app.route("/", methods=["GET", "POST"])
def i():
    if request.method == "POST":
        num = float(request.form.get("rates"))
        result = model.predict([[num]])[0]  # ML prediction
        result = round(max(0, float(result)), 2) # Set minimum prediction to 0, round to 2 dp
        return render_template("index.html", result=result)
    else:
        return render_template("index.html", result="Waiting……….")
    
if __name__=="__main__":
    app.run()

