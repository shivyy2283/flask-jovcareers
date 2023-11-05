from flask import Flask , render_template , jsonify

app = Flask(__name__)
#app is an object of the class flask
#we have to give a name to every flask application - it tells how a particukar script was invoked if invoked using python app.py it is going to be __main__
#@ is a decorator in python to provide some advanced functionality from libraries
#@ tells that when the url \ is accessed show the function hello world
#jobs dictionary
JOBS = [
    {
        'id':1,
        'title':'data analyst',
        'location':'Bengaluru',
        'salary':'10LPA'
    },
    {
        'id':2,
        'title':'data scientist',
        'location':'Bengaluru',
        'salary':'30LPA'
    },
    {
        'id':3,
        'title':'Frontend engineer',
        'location':'Remote',
        'salary':'10LPA'
    },
    {
        'id':4,
        'title':'Backend engineer',
        'location':'Delhi',
        'salary':'15LPA'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs = JOBS,company_name = 'shivani industries pvt ltd')

@app.route("/api/jobs") #url which doesnt return html but returns structured data to be analysed
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug = True)