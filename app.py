from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        
        print(request.form["q"])
        return render_template("fake_google.html")
    
    return render_template("fake_google.html")


if __name__ == "__main__":
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
