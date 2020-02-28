from flask import jsonify, request
from app import app, db
from app.models import IMC

@app.route("/")
@app.route("/index")
def index():
    return jsonify({"message": "Hello, world!"})

@app.route("/api", methods=["POST"])
def calculaIMC():
    resp = request.get_json()
    peso, altura = resp["peso"], resp["altura"]
    imc_data = IMC(peso=peso, altura=altura)
    db.session.add(imc_data)
    db.session.commit()
    imc = round(peso / altura ** 2, 2)
    return jsonify({'imc': imc})

@app.route("/api/last5")
def getLast5IMC():
    last5 = IMC.query.all()[-5:]
    result = {}
    for imc in last5:
        result[int(imc.id)] = {
            "peso": float(imc.peso), "altura": float(imc.altura)
        }
    return jsonify(result)