from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route("/")
def show_users():
    # call the get all classmethod to get all users
    users = User.get_all()
    return render_template("read_all.html", users = users)

@app.route("/user/new")
def display_create_user():
    return render_template("create.html")

@app.route("/user/new", methods = ['POST'])
def create_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }

    User.create(data)

    return redirect("/user/new")

@app.route("/user/<int:id>")
def show_user(id):
    data = {
        "id" : id
    }
    one_user = User.get_user(data)
    return render_template("show.html", one_user = one_user)

@app.route("/user/<int:id>/edit")
def display_edit_user(id):
    data = {
        "id" : id
    }
    one_user = User.get_user(data)
    return render_template("edit.html", one_user = one_user)

@app.route("/user/<int:id>/edit", methods=['POST'])
def edit_user(id):
    data = {
        "id" : id,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.edit(data)
    return redirect(f"/user/{id}")

@app.route("/user/<int:id>/delete")
def delete_user(id):
    data = {
        "id" : id
    }
    User.delete(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)