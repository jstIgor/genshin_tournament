from flask import Flask, render_template, request, redirect, session, url_for
from flask import jsonify
app = Flask(__name__)


# Список персонажей с картинками
characters = {
    "char1": {"name": "Character 1", "image": "static/image/characters/Aalto_Icon.png"},
    "char2": {"name": "Character 2", "image": "static/image/characters/Baizhi_Icon.png"},
    "char3": {"name": "Character 3", "image": "static/image/characters/Brant_Icon.png"},
    "char4": {"name": "Character 4", "image": "static/image/characters/Calcharo_Icon.png"},
    "char5": {"name": "Character 5", "image": "static/image/characters/Camellya_Icon.png"},
    "char6": {"name": "Character 6", "image": "static/image/characters/Carlotta_Icon.png"},
    "char7": {"name": "Character 1", "image": "static/image/characters/Youhu_Icon.png"},
    "char8": {"name": "Character 2", "image": "static/image/characters/Yuanwu_Icon.png"},
    "char9": {"name": "Character 3", "image": "static/image/characters/Zhezhi_Icon.png"},
    "char10": {"name": "Character 4", "image": "static/image/characters/Jianxin_Icon.png"},
    "char11": {"name": "Character 5", "image": "static/image/characters/Changli_Icon.png"},
    "char12": {"name": "Character 6", "image": "static/image/characters/Chixia_Icon.png"},
    "char13": {"name": "Character 1", "image": "static/image/characters/Lumi_Icon.png"},
    "char14": {"name": "Character 2", "image": "static/image/characters/Jinhsi_Icon.png"},
    "char15": {"name": "Character 3", "image": "static/image/characters/Jiyan_Icon.png"},
    "char16": {"name": "Character 4", "image": "static/image/characters/lingyang_Icon.png"},
    "char17": {"name": "Character 5", "image": "static/image/characters/Danjin_Icon.png"},
    "char18": {"name": "Character 6", "image": "static/image/characters/Encore_Icon.png"},
    "char19": {"name": "Character 5", "image": "static/image/characters/Mortefi_Icon.png"},
    "char20": {"name": "Character 6", "image": "static/image/characters/Phoebe_Icon.png"},
    "char21": {"name": "Character 4", "image": "static/image/characters/Roccia_Icon.png"},
    "char22": {"name": "Character 5", "image": "static/image/characters/Rover-Havoc_Icon.png"},
    "char23": {"name": "Character 6", "image": "static/image/characters/Rover-SpectroF_Icon.png"},
    "char24": {"name": "Character 5", "image": "static/image/characters/Sanhua_Icon.png"},
    "char25": {"name": "Character 6", "image": "static/image/characters/Shorekeeper_Icon.png"},
    "char26": {"name": "Character 4", "image": "static/image/characters/Taoqi_Icon.png"},
    "char27": {"name": "Character 5", "image": "static/image/characters/Verina_Icon.png"},
    "char28": {"name": "Character 6", "image": "static/image/characters/Xiangli Yao_Icon.png"},
    "char29": {"name": "Character 5", "image": "static/image/characters/Yangyang_Icon.png"},
    "char30": {"name": "Character 6", "image": "static/image/characters/Yinlin_Icon.png"},


}

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/characters')
def get_characters():
    return jsonify(characters)

if __name__ == "__main__":
    app.run(debug=True)