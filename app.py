from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "")
    email = request.form.get("email", "")
    message = request.form.get("message", "")

    if not name or not email or not message:
        return "Please fill in all fields.", 400

    return "Thank you! Your message was submitted."

if __name__ == "__main__":
    app.run(debug=True)
