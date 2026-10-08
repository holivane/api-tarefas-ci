from flask import Flask, jsonify, request

app = Flask(__name__)
tarefas = []

@app.route('/health')
def health():
    return {"status": "ok"}

@app.route('/tarefas', methods=['POST'])
def add_tarefa():
    data = request.get_json()
    tarefa = {"id": len(tarefas) + 1, "titulo": data["titulo"]}
    tarefas.append(tarefa)
    return tarefa, 201

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)
