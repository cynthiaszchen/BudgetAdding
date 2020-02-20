from flask import Flask, render_template, request  
from db import db
from Model import Budget_Manager
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/set_budget", methods=['POST'])
def set_budget():
    data = request.values
    # call your function with data['Date'] & data['Amount']
    budget_manager = Budget_Manager()
    status = budget_manager.Add_budget(data['Date'], data['Amount'])
    #status = f'Create budget {data["Date"]}: {data["Amount"]} successfully'
    return status

@app.route("/query")
def query():
    return render_template("query.html") 
    
@app.route("/query_budget", methods=['POST'])
def query_budget():
    data = request.values
    # call your function with data['start_date'], data['end_date']
    start_date = datetime.strptime(data['start_date'], "%Y%m%d")
    end_date = datetime.strptime(data['end_date'], "%Y%m%d")
    #status = f'Query budget {start_date}: {end_date} successfully'
    budget_manager = Budget_Manager()
    total_amount = budget_manager.totalAmount(start_date, end_date)
    return f'Total amout from {start_date} to {end_date} is {total_amount}0'

if __name__ == "__main__":
    app.run(debug=True)