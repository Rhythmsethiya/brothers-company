from flask import Flask,render_template
# creating the flask application
app = Flask(__name__)

# JOBS is a list conatining different dictionaries 
JOBS=[
    {
        'id':1,
        'title':'Data analyst',
        'location':'Bangaluru,India',
        'salary':'Rs 10,00,000'
    },
    {
        'id':2,
        'title':'Data Analyst',
        'location':'Delhi,India',
        'salary':'Rs 1,50,000'
    },
    {
        'id':3,
        'title':'Frontend engineer',
        'location':'Rajasthan,India',
        'salary':'Rs 5,00,000'
    }
]

# register the route to the application
@app.route("/")

def hello_world():
    return render_template('Home.html',jobs=JOBS,company_name= 'Sethiya')   #we have to pass JOBS in other arguement

# we can run the file using flask command
# but if we run the command without long flask command('flask --app index run')
# we can run with index.run and python index.py

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)  #values of host and debug are bydefault
