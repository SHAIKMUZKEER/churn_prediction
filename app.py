from flask import Flask,request , render_template

from src.pipeline.predict_pipeline import customdata ,Pipeline
app = Flask(__name__)

@app.route("/" , methods = ["GET"])
def index():
    return render_template("index.html")



@app.route("/predictdata" , methods = ["GET" , "POST"])
def predict_datapoint():
    print("entered the predict function")
    if request.method  == "GET":
        return render_template("home.html")
    else: 
        data = customdata(
            Contract = request.form.get("Contract"),
            tenure = int(request.form.get("tenure")),
            MonthlyCharges = float(request.form.get("MonthlyCharges")),
            TotalCharges =float(request.form.get("TotalCharges")),
            InternetService = request.form.get("InternetService"),
            TechSupport = request.form.get("TechSupport"),
            PaymentMethod = request.form.get("PaymentMethod"),
            Dependents = request.form.get("Dependents")
        )
        features = data.get_data_as_dataframe()

        print("features : " , features)

        pipeline_obj = Pipeline()

        prediction = pipeline_obj.predict(features)

        print("prediction : " , prediction[0])

        prediction = prediction[0]
        
        if prediction == 1:
            prediction = "Yes"
        else:
            prediction = "No"

        return render_template("home.html" , result = prediction)

if __name__ == "__main__": 
    app.run(debug= True)




