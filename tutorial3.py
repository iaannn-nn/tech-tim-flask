from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
#	return render_template("index.html", content = "Testing")
#	return render_template("index.html", content="Testing", x=4)
	return render_template("index.html", content={"a":2, "b":"hello"})

@app.route("/<name>")
def user(name):
	return f"Hello {name}!"

@app.route("/admin")
def hello_admin():
	return redirect(url_for("user", name="Admin!"))  # Now we when we go to /admin we will redirect to user with the argument "Admin!"

if __name__ == "__main__":
	app.run(debug=True, port = 8080, host = '0.0.0.0')