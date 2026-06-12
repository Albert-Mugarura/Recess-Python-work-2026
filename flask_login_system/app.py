from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = "recess_python_2026_secret_key"

users = {
    "admin": {"password": "admin123", "role": "Admin", "name": "Administrator"},
    "customer": {"password": "cust123", "role": "Customer", "name": "John Customer"},
    "cashier": {"password": "cash123", "role": "Cashier", "name": "Jane Cashier"},
}


@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not password:
            flash("Please enter both username and password.", "error")
            return render_template("login.html")

        if username in users and users[username]["password"] == password:
            session["username"] = username
            session["role"] = users[username]["role"]
            session["name"] = users[username]["name"]
            flash(f"Welcome back, {users[username]['name']}!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password!", "error")
            return render_template("login.html")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        name = request.form.get("name", "").strip()
        role = request.form.get("role", "Customer").strip()

        if not username or not password or not name:
            flash("All fields are required.", "error")
            return render_template("register.html")

        if username in users:
            flash("Username already exists!", "error")
            return render_template("register.html")

        if len(password) < 6:
            flash("Password must be at least 6 characters.", "error")
            return render_template("register.html")

        users[username] = {"password": password, "role": role, "name": name}
        flash("Registration successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        flash("Please login first.", "error")
        return redirect(url_for("login"))

    role = session["role"]
    if role == "Admin":
        access = "Full access to all features: Users, Products, Reports, Settings"
        features = ["Manage Users", "Manage Products", "View Reports", "System Settings", "Sales Analytics"]
    elif role == "Cashier":
        access = "Access to Sales and Billing features"
        features = ["Process Sales", "Generate Receipts", "View Transactions", "Daily Reports"]
    else:
        access = "Access to Shopping features"
        features = ["Browse Products", "Shopping Cart", "Order History", "My Profile"]

    return render_template("dashboard.html", features=features, access=access)


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    print("=" * 50)
    print("  FLASK LOGIN SYSTEM")
    print("=" * 50)
    print("  URL: http://127.0.0.1:5000")
    print("  Default accounts:")
    print("    admin/admin123 (Admin)")
    print("    customer/cust123 (Customer)")
    print("    cashier/cash123 (Cashier)")
    print("=" * 50)
    app.run(debug=True)
