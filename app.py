from flask import Flask, render_template, request
app = Flask(__name__)
transaction=[("2020-08-25",70.00,"checking"),
              ("2020-09-25",170.00,"savings"),
              ("2020-10-25",150.00,"checking"),
              ]
l=[]
@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        print(request.form)
        transaction.append(
                (
                    request.form.get("date"),
                    float(request.form.get("amount")),
                    request.form.get("account"),
                )
            )
        return render_template("index.html")
        
            

@app.route("/transactions")
def show_transactions():
    return render_template("index(2).html",entries=transaction)




