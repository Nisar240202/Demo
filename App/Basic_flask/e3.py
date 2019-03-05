from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index1():
    return render_template('temp.html')
    
@app.route("/hi/<int:name>")
def index(name):
	return'Riverdale song %d '%name
if __name__=="__main__":
        app.run(debug=True)
