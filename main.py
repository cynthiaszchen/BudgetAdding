from flask import Flask, render_template, request  
from db import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/set_budget", methods=['POST'])
def set_budget():
    data = request.values
    # call your function with data['Date'] & data['Amount']
    status = db.Add_budget(data['Date'], data['Amount'])
    #status = f'Create budget {data["Date"]}: {data["Amount"]} successfully'
    return status

@app.route("/query")
def query():
    return render_template("query.html") 
    
@app.route("/query_budget", methods=['POST'])
def query_budget():
    data = request.values
    # call your function with data['start_date'], data['end_date']
    status = f'Query budget {data["start_date"]}: {data["end_date"]} successfully'
    return status

if __name__ == "__main__":
    app.run(debug=True)