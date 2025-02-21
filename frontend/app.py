from flask import Flask, flash, redirect, render_template, request, session, url_for
import requests

app = Flask(__name__)
app.secret_key = "supersecretkey"

BACKEND_URL = "http://127.0.0.1:9000"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        response = requests.post(
            f"{BACKEND_URL}/auth/register",
            json={"username": username, "password": password},
        )
        if response.status_code == 200:
            flash("Registracija uspješna. Prijavite se.", "success")
            return redirect(url_for("login"))
        flash("Greška pri registraciji.", "danger")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        response = requests.post(
            f"{BACKEND_URL}/auth/login",
            data={"username": username, "password": password},
        )
        if response.status_code == 200:
            session["access_token"] = response.json()["access_token"]
            return redirect(url_for("form"))
        flash("Neispravni podaci za prijavu.", "danger")
    return render_template("login.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if "access_token" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        data = {
            "customer_name": request.form["customer_name"],
            "date": request.form["date"],
            "items": request.form["items"].split(","),
            "total": float(request.form["total"]),
        }
        headers = {"Authorization": f"Bearer {session['access_token']}"}
        response = requests.post(
            f"{BACKEND_URL}/invoice/create", json=data, headers=headers
        )

        if response.status_code == 200:
            flash("Račun uspješno dodan!", "success")
            return redirect(url_for("index"))
        flash("Greška pri dodavanju računa.", "danger")

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
