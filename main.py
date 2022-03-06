# Kajetan Knopp (khknopp) - 2022

# Main flask imports
from flask import Flask, render_template, redirect, request, url_for, session, flash
# Database import (alchemy)
#from flask_sqlalchemy import SQLAlchemy
# Database import (mySQL)
import requests
import mysql.connector 
from mysql.connector import Error

# Form import
from wtforms import Form, StringField, IntegerField, validators

# Main flask definitions
app = Flask(__name__)
app.secret_key = "Code4Ukraine"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'

# # Database definition (alchemy)
# db = SQLAlchemy(app)

# class Person(db.Model):
#     Id = db.Column(db.Integer, primary_key=True)
#     Age = db.Column(db.Integer, nullable=False)
#     Name = db.Column(db.String(50), nullable=False)

#     def __repr__(self):
#         return f"Person: {self.Id}, Age: {self.Age}, Name: {self.Name}"

# db.create_all()

try: 
    connection = mysql.connector.connect(host="localhost",user="root",password="password",port=3308)
    cursor = connection.cursor()
except mysql.connector.Error as error:
    print("Failed to connect to mySQL table".format(error))

# Form definition

class PersonForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    phone = IntegerField('Phone', [validators.NumberRange(min=0)])
    email = StringField('Email', [validators.Length(min=4, max=25)])
    interval = IntegerField('Contact Interval (Days)', [validators.NumberRange(min=0)])

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        if 'add' in request.form:
            return redirect(url_for("add"))
        elif 'all' in request.form:
            return redirect(url_for("all"))
        #elif 'upcoming' in request.form:
            #return redirect(url_for("upcoming"))
        #elif 'new' in request.form:
            #return redirect(url_for("new"))
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = PersonForm(request.form) 
    if request.method == "POST" and form.validate():
        Name = form.name.data.split()
        Phone = form.phone.data
        Email = form.email.data
        ContactInterval =form.interval.data
        mySql_insert_query = """INSERT INTO `remindDB`.`contacts` (`firstName`, `lastName`, `email_0`,`phonenumber_0`) VALUES (%s,%s,%s,%s)"""
        cursor = connection.cursor()
        record = (Name[0],Name[1],Email,Phone)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        # db.session.add(person)
        # db.session.commit()
        # Adding this person as last one added
        session["last"] = form.name.data
        flash("Thanks for adding a new person to the database!")
        return redirect(url_for('main'))
    else:
        return render_template("add.html", form=form)
    if connection.is_connected():
        cursor.close()
        connection.close
        print("MySQL connection is closed")

@app.route('/all')
def all():
    people = Person.query.all()
    return render_template('all.html', people = people)

@app.route('/one/<int:id>')
def one(id):
    person = Person.query.filter_by(Id=id).first()
    return render_template('one.html', person = person)

@app.route('/last')
def last():
    if('last' not in session):
        flash("No people added in this session!")
        return redirect(url_for("main"))
    else:
        last_person = session["last"]
        return redirect(url_for("one", id=last_person))


if __name__ == '__main__':
    app.run(debug=True)
