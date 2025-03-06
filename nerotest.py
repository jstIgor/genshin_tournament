import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('site_data.db')
cursor = conn.cursor()

# Список персонажей с изображениями
characters = {
    "char1": {"name": "Aalto", "image": "static/image/characters/Aalto_Icon.png"},
    "char2": {"name": "Baizhi", "image": "static/image/characters/Baizhi_Icon.png"},
    "char3": {"name": "Brant", "image": "static/image/characters/Brant_Icon.png"},
    "char4": {"name": "Calcharo", "image": "static/image/characters/Calcharo_Icon.png"},
    "char5": {"name": "Camellya", "image": "static/image/characters/Camellya_Icon.png"},
    "char6": {"name": "Carlotta", "image": "static/image/characters/Carlotta_Icon.png"},
    "char7": {"name": "Youhu", "image": "static/image/characters/Youhu_Icon.png"},
    "char8": {"name": "Yuanwu", "image": "static/image/characters/Yuanwu_Icon.png"},
    "char9": {"name": "Zhezhi", "image": "static/image/characters/Zhezhi_Icon.png"},
    "char10": {"name": "Jianxin", "image": "static/image/characters/Jianxin_Icon.png"},
    "char11": {"name": "Changli", "image": "static/image/characters/Changli_Icon.png"},
    "char12": {"name": "Chixia", "image": "static/image/characters/Chixia_Icon.png"},
    "char13": {"name": "Lumi", "image": "static/image/characters/Lumi_Icon.png"},
    "char14": {"name": "Jinhsi", "image": "static/image/characters/Jinhsi_Icon.png"},
    "char15": {"name": "Jiyan", "image": "static/image/characters/Jiyan_Icon.png"},
    "char16": {"name": "lingyang", "image": "static/image/characters/lingyang_Icon.png"},
    "char17": {"name": "Danjin", "image": "static/image/characters/Danjin_Icon.png"},
    "char18": {"name": "Encore", "image": "static/image/characters/Encore_Icon.png"},
    "char19": {"name": "Mortefi", "image": "static/image/characters/Mortefi_Icon.png"},
    "char20": {"name": "Phoebe", "image": "static/image/characters/Phoebe_Icon.png"},
    "char21": {"name": "Roccia", "image": "static/image/characters/Roccia_Icon.png"},
    "char22": {"name": "Rover-Havoc", "image": "static/image/characters/Rover-Havoc_Icon.png"},
    "char23": {"name": "Rover-Spectro", "image": "static/image/characters/Rover-SpectroF_Icon.png"},
    "char24": {"name": "Sanhua", "image": "static/image/characters/Sanhua_Icon.png"},
    "char25": {"name": "Shorekeeper", "image": "static/image/characters/Shorekeeper_Icon.png"},
    "char26": {"name": "Taoqi", "image": "static/image/characters/Taoqi_Icon.png"},
    "char27": {"name": "Verina", "image": "static/image/characters/Verina_Icon.png"},
    "char28": {"name": "Xiangli Yao", "image": "static/image/characters/Xiangli Yao_Icon.png"},
    "char29": {"name": "Yangyang", "image": "static/image/characters/Yangyang_Icon.png"},
    "char30": {"name": "Yinlin", "image": "static/image/characters/Yinlin_Icon.png"},
}

# Добавляем персонажей в таблицу
for char in characters.values():
    cursor.execute("""
        INSERT INTO characters (name, image) 
        VALUES (?, ?);
    """, (char["name"], char["image"]))

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()
