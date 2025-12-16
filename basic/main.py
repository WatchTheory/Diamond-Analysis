from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired
import pickle
import numpy as np

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"

# Load the pickle file with error handling
try:
    with open('EDA_alumni.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Error: Pickle file not found!")
    model = None
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

class PredictionForm(FlaskForm):
    # Updated features for alumni dataset
    salary = FloatField('Salary', validators=[DataRequired()])
    fee = FloatField('Fee', validators=[DataRequired()])
    Year_Graduated = FloatField('Year Graduated', validators=[DataRequired()])
    
    submit = SubmitField('Predict Price')

# Route to pages 
@app.route("/")
def index():
    return render_template("home.html")

# Works -- about the author page
@app.route("/about")
def about():
    return render_template("about.html")

# Works -- view profile 
@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = PredictionForm()
    prediction = None
    
    if model is None:
        prediction = "Error: Model could not be loaded. Check server logs."
    elif form.validate_on_submit():
        try:
            # Create input array with correct shape: (1, 3) – adjust order if your model expects different
            input_features = np.array([[ 
                float(form.salary.data),
                float(form.fee.data),
                float(form.Year_Graduated.data)
            ]])

            # Make prediction (assuming regression for a continuous "price" value)
            raw_prediction = model.predict(input_features)[0]
            
            # Format as a price (e.g., $1234.56) – customize if it's not monetary
            prediction = f"Predicted: <strong>${raw_prediction:,.2f}</strong>"
            
            # If your model is classification (e.g., binary outcome like "Will Donate: Yes/No"), uncomment/adapt this instead:
            # if raw_prediction > 0.5:
            #     prediction = "Predicted Outcome: Positive (e.g., Will Donate) – Confidence: {raw_prediction:.1%}"
            # else:
            #     prediction = "Predicted Outcome: Negative (e.g., Won't Donate) – Confidence: {1 - raw_prediction:.1%}"

        except Exception as e:
            prediction = f"Prediction error: {str(e)}"
    
    return render_template("predict.html", form=form, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

#-----------------------------------------------
# Uncomment 
# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# import pickle
# import numpy


# app = Flask(__name__)

# # load your picke file here 
# app.config["SECRET_KEY"] = "your_secret_key"
# upload_model = pickle.load(open('EDA_churn_pkl_file','rb'))


# # Route to pages 
# @app.route("/")
# def index():
#     return render_template("home.html")

##---------------------------------------------





# @app.route("/member", methods=["GET", "POST"])
# def member():
#     name = False
#     email = False
#     form = MemberInfo()
#     if form.validate_on_submit():
#         name = form.name.data
#         email = form.email.data
#         form.name.data = ""
#     return render_template("member.html", name=name, email=email, form=form)


# @app.route("/member/<name>")
# def member(name):
#     return render_template("member.html", name=name)

## Uncomment 
## -----------------------------------------------
# # Works -- about the auther page
# @app.route("/about")
# def about():
#     return render_template("about.html")


# # Works -- view profile 
# @app.route("/profile")
# def profile():
#     return render_template("profile.html")

## --------------------------------------------------
# if __name__ == "__main__":
#     app.run(debug=True)

# def main():
#     print("Hello from basic!")


# if __name__ == "__main__":
#     main(debug=True)



