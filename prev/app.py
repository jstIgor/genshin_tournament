from flask import Flask, render_template, request, redirect, session, url_for
from flask import jsonify
import sqlite3


app = Flask(__name__)
app.secret_key = "supersecretkey"



# Инициализируем объект SQLAlchemy


# Список пользователей с никнеймами и одноразовыми паролями
# Функция для проверки логина и пароля
def check_user_in_db(username, password):
    conn = sqlite3.connect('site_data.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()

    conn.close()
    return user



# Админские данные
admin_username = "admin"
admin_password = "secret_admin_password"

# Храним использованные пароли
used_passwords = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Проверяем наличие пользователя в базе данных
        user = check_user_in_db(username, password)



        if username in user and users[username] == password and password not in used_passwords:
            used_passwords.append(password)
            session["status"] = "player"
            session["username"] = username
            return redirect(url_for("page5"))

        elif username == 'admin' :
            session["status"] = "admin"
            return redirect(url_for("index"))

        else:
            return redirect(url_for("index"))

    return render_template("about.html")


@app.route("/regist", methods=["GET", "POST"])
def page2():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Проверяем наличие пользователя в базе данных
        user = check_user_in_db(username, password)

        if user:
            session["status"] = "player"
            session["username"] = username
            return redirect(url_for("page5"))
        elif username == 'admin' and password == 'admin_password':  # Простая проверка для admin
            session["status"] = "admin"
            return redirect(url_for("index"))
        else:
            return redirect(url_for("page2"))

    return render_template("regist.html")

@app.route("/pravil")
def page3():
    return render_template("Pravil.html")

@app.route("/tablo")
def page4():
    return render_template("tablo.html")

@app.route("/regis_zap", methods=["GET", "POST"])
def page5():
    if session.get("status") == "player":
        return render_template("regis_zapolnenie.html")
    return redirect(url_for("index"))


# Функция для получения данных из БД
def fetch_from_db(table):
    conn = sqlite3.connect("site_data.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Передаём данные в формате JSON
@app.route('/characters')
def get_characters():
    characters = fetch_from_db("characters")  # Загружаем данные из таблицы characters

    # Преобразуем в нужный формат
    character_dict = {
        f"char{row[0]}": {"name": row[1], "image": row[2]} for row in characters
    }

    return jsonify(character_dict)

@app.route('/weapons')
def get_weapons():
    weapons = fetch_from_db("weapons")  # Загружаем данные из таблицы weapons

    weapon_dict = {
        f"char{row[0]}": {"name": row[1], "image": row[2]} for row in weapons
    }

    return jsonify(weapon_dict)


@app.route('/save_character', methods=['POST'])
def save_character_data():
    data = request.get_json()
    selected_characters = data.get("characters", [])

    # Получаем текущего пользователя
    username = session.get("username")

    if not username:
        return jsonify({"success": False, "message": "User not logged in"})

    conn = sqlite3.connect('site_data.db')
    cursor = conn.cursor()

    # Получаем название таблицы игрока
    cursor.execute('SELECT player_settings FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return jsonify({"success": False, "message": "Player settings not found"})

    player_table = row[0]  # Например, 'player1_settings'

    # Проверяем, существует ли такая таблица (если нет — создаём)
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {player_table} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        character_name TEXT NOT NULL)''')

    # Добавляем персонажей в таблицу игрока
    for image_url in selected_characters:
        cursor.execute('SELECT name FROM characters WHERE image = ?', (image_url,))
        character_row = cursor.fetchone()

        if character_row:
            character_name = character_row[0]

            # Проверяем, есть ли уже такая запись
            cursor.execute(f'SELECT * FROM {player_table} WHERE character_name = ?', (character_name,))
            if not cursor.fetchone():  # Если записи нет, то добавляем
                cursor.execute(f'INSERT INTO {player_table} (character_name) VALUES (?)', (character_name,))
                conn.commit()

    conn.close()
    return jsonify({"success": True})


@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.get_json()
    selected_characters = data.get("characters", [])
    selected_weapons = data.get("weapons", [])

    username = session.get("username")
    if not username:
        return jsonify({"success": False, "message": "User not logged in"})

    conn = sqlite3.connect('site_data.db')
    cursor = conn.cursor()

    # Получаем имя настроек игрока
    cursor.execute('SELECT player_settings FROM users WHERE username = ?', (username,))
    player_settings_name = cursor.fetchone()

    if not player_settings_name:
        return jsonify({"success": False, "message": "Player settings not found"})

    player_settings_name = player_settings_name[0]

    # Проверяем, есть ли уже запись в player_settings для этого игрока
    cursor.execute('SELECT id FROM player_settings WHERE player_name = ?', (player_settings_name,))
    existing_entry = cursor.fetchone()

    # Если записи нет, создаем новую
    if not existing_entry:
        cursor.execute('INSERT INTO player_settings (player_name, character_name, weapon_name) VALUES (?, ?, ?)',
                       (player_settings_name, None, None))
        conn.commit()
        entry_id = cursor.lastrowid  # Получаем ID новой записи
    else:
        entry_id = existing_entry[0]

    # Обновляем персонажа
    for image_url in selected_characters:
        cursor.execute('SELECT name FROM characters WHERE image = ?', (image_url,))
        character_name = cursor.fetchone()
        if character_name:
            cursor.execute('UPDATE player_settings SET character_name = ? WHERE id = ?',
                           (character_name[0], entry_id))
            conn.commit()

    # Обновляем оружие
    for image_url in selected_weapons:
        cursor.execute('SELECT name FROM weapons WHERE image = ?', (image_url,))
        weapon_name = cursor.fetchone()
        if weapon_name:
            cursor.execute('UPDATE player_settings SET weapon_name = ? WHERE id = ?',
                           (weapon_name[0], entry_id))
            conn.commit()

    conn.close()
    return jsonify({"success": True})


@app.route('/save_weapon', methods=['POST'])
def save_weapon_data():
    data = request.get_json()
    selected_weapons = data.get("weapons", [])

    # Получаем текущего пользователя
    username = session.get("username")

    if not username:
        return jsonify({"success": False, "message": "User not logged in"})

    conn = sqlite3.connect('site_data.db')
    cursor = conn.cursor()

    # Получаем название персональной таблицы игрока
    cursor.execute('SELECT player_settings FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return jsonify({"success": False, "message": "Player settings not found"})

    player_table = row[0]  # Например, 'player1_settings'

    # Убеждаемся, что таблица игрока существует
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {player_table} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        character_name TEXT,
                        weapon_name TEXT)''')

    # Добавляем оружие
    for image_url in selected_weapons:
        cursor.execute('SELECT name FROM weapons WHERE image = ?', (image_url,))
        weapon_row = cursor.fetchone()

        if weapon_row:
            weapon_name = weapon_row[0]

            # Проверяем, есть ли уже такое оружие
            cursor.execute(f'SELECT * FROM {player_table} WHERE weapon_name = ?', (weapon_name,))
            if not cursor.fetchone():  # Если нет, то добавляем
                cursor.execute(f'INSERT INTO {player_table} (weapon_name) VALUES (?)', (weapon_name,))
                conn.commit()

    conn.close()
    return jsonify({"success": True})




@app.route("/bans")
def page6():
    if session.get("status") in ["player", "admin"]:
        return render_template("bans.html")
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("status", None)
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
