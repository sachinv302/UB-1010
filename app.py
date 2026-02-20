from flask import Flask, render_template, request, redirect, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from utils.priority_engine import calculate_priority
from utils.db_setup import init_db
import datetime

app = Flask(__name__)
app.secret_key = "smartcitysecret"

init_db()

def get_db_connection():
    conn = sqlite3.connect("smartcity.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("index.html")

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        role = "user"

        conn = get_db_connection()

        # Check if email already exists
        existing_user = conn.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        ).fetchone()

        if existing_user:
            flash("Email already registered! Please login.")
            conn.close()
            return redirect("/register")

        # Insert new user
        conn.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
            (name, email, password, role)
        )

        conn.commit()
        conn.close()

        flash("Registration Successful! Please Login.")
        return redirect("/login")

    return render_template("register.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["role"] = user["role"]

            if user["role"] == "admin":
                return redirect("/admin_dashboard")
            return redirect("/user_dashboard")

        flash("Invalid Credentials")

    return render_template("login.html")

# ---------------- USER DASHBOARD ----------------
@app.route("/user_dashboard")
def user_dashboard():
    if "user_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    complaints = conn.execute(
        "SELECT * FROM complaints WHERE user_id=?",
        (session["user_id"],)
    ).fetchall()
    conn.close()

    return render_template("user_dashboard.html", complaints=complaints)

# ---------------- SUBMIT COMPLAINT ----------------
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        description = request.form["description"]
        category = request.form["category"]
        location = request.form["location"]

        urgency, score = calculate_priority(description, category, location)

        conn = get_db_connection()
        conn.execute("""
            INSERT INTO complaints 
            (user_id, description, category, location, urgency, priority_score, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            session["user_id"],
            description,
            category,
            location,
            urgency,
            score,
            "Pending",
            datetime.datetime.now()
        ))
        conn.commit()
        conn.close()

        flash("Complaint Submitted Successfully!")
        return redirect("/user_dashboard")

    return render_template("submit_complaint.html")

# ---------------- ADMIN DASHBOARD ----------------
@app.route("/admin_dashboard")
def admin_dashboard():
    if "role" not in session or session["role"] != "admin":
        return redirect("/admin_login")

    conn = get_db_connection()
    complaints = conn.execute("""
        SELECT complaints.*, users.name 
        FROM complaints 
        JOIN users ON complaints.user_id = users.id
        ORDER BY priority_score DESC
    """).fetchall()
    conn.close()

    return render_template("admin_dashboard.html", complaints=complaints)
# ---------------- ADMIN LOGIN ----------------
@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        conn = get_db_connection()
        admin = conn.execute(
            "SELECT * FROM users WHERE email=? AND role='admin'",
            (email,)
        ).fetchone()
        conn.close()

        if admin and check_password_hash(admin["password"], password):
            session["user_id"] = admin["id"]
            session["role"] = "admin"
            flash("Welcome Admin!")
            return redirect("/admin_dashboard")

        flash("Invalid Admin Credentials!")

    return render_template("admin_login.html")

# ---------------- UPDATE STATUS ----------------
@app.route("/update_status/<int:id>", methods=["POST"])
def update_status(id):
    status = request.form["status"]
    conn = get_db_connection()
    conn.execute("UPDATE complaints SET status=? WHERE id=?", (status, id))
    conn.commit()
    conn.close()
    return redirect("/admin_dashboard")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)