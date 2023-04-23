from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)

COURSES = [
  {
    'id' : '1',
    'sub': 'Data Analyst',
    'cost': '65k$',
    'batch': 'Starts from 1 May 2023'
  },
  {
    'id' : '2',
    'sub': 'Data Scientist',
    'cost': '85k$',
    'batch': 'Starts from 1 May 2023'
  },
  {
    'id' : '3',
    'sub': 'Cyber Security Analyst',
    'cost': '50k$',
    'batch': 'Starts from 1 June 2023'
  },
  {
    'id' : '4',
    'sub': 'UX Designer',
    'cost': '35k$',
    'batch': 'Starts from 1 May 2023'
  }
]

@app.route("/")
def story():
  return render_template('home.html', course = COURSES)

@app.route("/api/Courses")
def list_courses():
  return jsonify(COURSES)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)