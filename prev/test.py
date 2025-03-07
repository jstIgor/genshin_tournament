from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Список пользователей с никнеймами и одноразовыми паролями
users = {
    "player1": "password1",
    "player2": "password2",
    "player3": "password3",
    "player4": "password4",
    "player5": "password5",
    "player6": "password6",
}

# Админские данные
admin_username = "admin"
admin_password = "secret_admin_password"

# Храним использованные пароли
used_passwords = []

# Список персонажей с картинками
characters = {
    "char1": {"name": "Character 1", "image": "static/image//tg.png"},
    "char2": {"name": "Character 2", "image": "char2.png"},
    "char3": {"name": "Character 3", "image": "char3.png"},
    "char4": {"name": "Character 4", "image": "char4.png"},
    "char5": {"name": "Character 5", "image": "char5.png"},
    "char6": {"name": "Character 6", "image": "char6.png"},
}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password and password not in used_passwords:
            used_passwords.append(password)
            session["status"] = "player"
            session["username"] = username
            session["selected_characters"] = []  # Пустой список для выбранных персонажей
            return redirect(url_for("select_characters"))

        elif username == admin_username and password == admin_password:
            session["status"] = "admin"
            return redirect(url_for("index"))

        else:
            return redirect(url_for("index"))

    return render_template("about.html")


@app.route("/select_characters", methods=["GET", "POST"])
def select_characters():
    if session.get("status") != "player":
        return redirect(url_for("index"))

    if request.method == "POST":
        # Сохраняем выбранных персонажей в сессии
        selected = request.form.getlist("characters")
        session["selected_characters"] = selected
        return redirect(url_for("view_characters"))

    # Отображаем список персонажей
    return render_template("select_characters.html", characters=characters)

@app.route("/regist", methods=["GET", "POST"])
def page2():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password and password not in used_passwords:
            used_passwords.append(password)
            session["status"] = "player"
            session["username"] = username
            return redirect(url_for("page5"))

        elif username == 'admin' :
            session["status"] = "admin"
            return redirect(url_for("index"))

        else:
            return redirect(url_for("page2"))
    return render_template("regist.html")

@app.route("/regis_zap")
def page5():
    if session.get("status") == "player":
        return render_template("regis_zapolnenie.html")
    return redirect(url_for("index"))

@app.route("/view_characters")
def view_characters():
    if session.get("status") != "player":
        return redirect(url_for("index"))

    # Получаем выбранных персонажей из сессии
    selected_characters = session.get("selected_characters", [])
    selected_character_images = [characters[char]["image"] for char in selected_characters]

    return render_template("view_characters.html", selected_character_images=selected_character_images)



@app.route("/get_characters")
def get_characters():
    return jsonify(characters)

@app.route("/logout")
def logout():
    session.pop("status", None)
    session.pop("username", None)
    session.pop("selected_characters", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
