from flask import Flask, render_template, request  

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/set_budget", methods=['POST'])
def set_budget():
    data = request.values
    # call your function with data['Date'] & data['Amount']
    status = f'Create budget {data["Date"]}: {data["Amount"]} successfully'
    return status
    
if __name__ == "__main__":
    app.run(debug=True)