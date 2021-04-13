"import the required libraries"
from flask import Flask, redirect, request, render_template
from helper import Operations

app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder='templates')
# home route
@app.route('/', methods = ['GET', 'POST'])
def predictions():
    pred = 'Submit Data to Get Predictions!'
    if request.method == "POST":
        req = request.form
        tenure = req.get('tenure')
        mlines = req.get('mlines')
        internet = req.get('internet')
        gender = req.get("gender")
        contract = req.get("contract")
        online_sec =  req.get("onlines")
        pred = Operations.get_predictions(
                                tenure, mlines, internet, 
                                online_sec, gender, contract)

    return render_template("main.html", pred = pred)


if __name__ == "__main__":
    app.run(debug=True)