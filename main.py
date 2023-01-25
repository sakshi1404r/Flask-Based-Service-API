
import os
from flask import Flask, render_template, url_for, request, jsonify, session
#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'qtdata.db')
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# db = SQLAlchemy(app)
# class Store_QTc_data(db.Model):
#   __tablename__ = 'qt_data’
#   id = db.Column('id', db.Integer, primary_key = True)
#   timestamp = db.Column('timestamp', db.DateTime)
#   QTc = db.Column('QTc', db.Integer)
#   prolonged = db.Column('prolonged', db.String(50))
#   heart_rate = db.Column('heart rate', db.Integer)
#   QT = db.Column('QT', db.Integer)
#   sex = db.Column('sex', db.CHAR)
# def __init__(self, QTc, prolonged, heart_rate, QT, sex):
#   self.QTc = QTc
#   self.prolonged = prolonged
#   self.timestamp = datetime.now()
#   self.heart_rate = heart_rate
#   self.QT = QT
#   self.sex = sex
@app.route('/')
def index():
  #if not os.path.exists(os.path.join(basedir, 'qtdata.db')):
    #db.create_all()
  return render_template('index.html')

@app.route('/process_qtc', methods=['POST', 'GET'])
def process_qt_calculation():
  if request.method == "POST":
    qtc_data = request.get_json()
    #db.session.add(Store_QTc_data(qtc_data[0]['QTc'], qtc_data[1]['prolonged'], qtc_data[2]['HR'], qtc_data[3]['QT'], qtc_data[4]['Sex']))
    #db.session.commit()
    #rows = db.session.query(Store_QTc_data).count()
  results = {'rows': qtc_data}
  return jsonify(results)

@app.route('/index2')
def index1():
  #if not os.path.exists(os.path.join(basedir, 'qtdata.db')):
    #db.create_all()
  return render_template('index2.html')

@app.route('/getState', methods=['POST', 'GET'])
def process_qt_calculation1():
  if request.method == "GET":
    stateData = { "AN":"Andaman and Nicobar Islands", "AP":"Andhra Pradesh", "AR":"Arunachal Pradesh", "AS":"Assam", "BR":"Bihar", "CG":"Chandigarh", "CH":"Chhattisgarh", "DN":"Dadra and Nagar Haveli", "DD":"Daman and Diu", "DL":"Delhi", "GA":"Goa", "GJ":"Gujarat", "HR":"Haryana", "HP":"Himachal Pradesh", "JK":"Jammu and Kashmir", "JH":"Jharkhand", "KA":"Karnataka", "KL":"Kerala", "LA":"Ladakh", "LD":"Lakshadweep", "MP":"Madhya Pradesh", "MH":"Maharashtra", "MN":"Manipur", "ML":"Meghalaya", "MZ":"Mizoram", "NL":"Nagaland", "OR":"Odisha", "PY":"Puducherry", "PB":"Punjab", "RJ":"Rajasthan", "SK":"Sikkim", "TN":"Tamil Nadu", "TS":"Telangana", "TR":"Tripura", "UP":"Uttar Pradesh", "UK":"Uttarakhand", "WB":"West Bengal" }
    #qtc_data = request.get_json()
    #db.session.add(Store_QTc_data(qtc_data[0]['QTc'], qtc_data[1]['prolonged'], qtc_data[2]['HR'], qtc_data[3]['QT'], qtc_data[4]['Sex']))
    #db.session.commit()
    #rows = db.session.query(Store_QTc_data).count()
  results =  stateData
  return jsonify(results)

@app.route('/postForm2', methods=['POST', 'GET'])
def process_qt_calculation2():
  if request.method == "POST":
    qtc_data = request.get_json()
    #db.session.add(Store_QTc_data(qtc_data[0]['QTc'], qtc_data[1]['prolonged'], qtc_data[2]['HR'], qtc_data[3]['QT'], qtc_data[4]['Sex']))
    #db.session.commit()
    #rows = db.session.query(Store_QTc_data).count()
  results =  qtc_data
  return jsonify(results)



if __name__ == "__main__":
  app.run(debug=True)