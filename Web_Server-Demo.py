from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

VALID_USERNAME = "admin"
VALID_PASSWORD = "secret123"

login_page = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h2>Login Page</h2>
    <form method="POST">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    <p style="color:red;">{{ message }}</p>
</body>
</html>
"""

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return redirect("/dashboard")
        else:
            return render_template_string(login_page, message="Login failed")

    return render_template_string(login_page, message="")

@app.route("/dashboard")
def dashboard():
    return "<h1>Welcome Admin! Login Successful 🎉</h1>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
