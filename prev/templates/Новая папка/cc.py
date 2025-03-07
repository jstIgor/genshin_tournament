from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Ключ для хранения сессий (замени на свой)

# Список одноразовых паролей
one_time_passwords = ["password1", "password2", "password3", "password4", "password5", "password6"]
used_passwords = []  # Список использованных паролей

admin_password = ['secret_admin_password']

# Главная страница
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("status_input")

        if user_input in one_time_passwords and user_input not in used_passwords:
            used_passwords.append(user_input)  # Добавляем пароль в использованные
            session["status"] = "player"
            return redirect(url_for("index"))
        elif user_input == "secret_admin_password":  # Пароль админа
            session["status"] = "admin"
            return redirect(url_for("index"))
        else:
            return "Неверный ввод или этот пароль уже использован, попробуйте снова."

    return render_template("index.html")

# Страница 2 (только для игрока и админа)
@app.route("/page2")
def page2():
    if session.get("status") in ["player", "admin"]:
        return render_template("page2.html")
    return redirect(url_for("index"))

# Страница 3 (только для админа)
@app.route("/page3")
def page3():
    if session.get("status") == "admin":
        return render_template("page3.html")
    return redirect(url_for("index"))

# Выход (очистка сессии)
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
