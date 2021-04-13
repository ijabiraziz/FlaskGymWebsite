from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

"""initialize the app"""
app = Flask(__name__)

"""create a database for the webpage using flask_Sqlalchemy"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gym.db'

"""also create a secret key to prevent webpage from different attacks"""
app.config['SECRET_KEY'] = 'thisisasecret'

"""start database"""
db = SQLAlchemy(app)


"""create a database model or you can say a table that will store 
info about the user that is interested in taking admission in our Gym."""


class Client(db.Model):
    # id will be assign automatically to every user.
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200), nullable=False)


@app.route('/')
@app.route('/home', methods=['Get', 'POST'])
def home():
    # when user is about to post the data or send the data to the server.
    if request.method == 'POST':
        try:
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            message = request.form["message"]

            """ add all the data that is coming from the contact form to a 
            variable."""
            entry = Client(name=name, email=email, phone=phone, message=message)

            db.session.add(entry)
            db.session.commit()
            return redirect('/')
        except:
            return redirect('/')

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
