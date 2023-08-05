from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for demonstration purposes
pokemon_data = [
    {"id": 1, "name": "Bulbasaur", "type": "Grass/Poison"},
    {"id": 2, "name": "Charmander", "type": "Fire"},
    {"id": 3, "name": "Squirtle", "type": "Water"},
]

# Route for getting a single Pokemon by its ID
@app.route('/api/pokemon/detail/<int:id>', methods=['GET'])
def get_pokemon_detail(id):
    pokemon = next((p for p in pokemon_data if p['id'] == id), None)
    if pokemon:
        return jsonify(pokemon)
    else:
        return jsonify({"error": "Pokemon not found"}), 404

# Route for getting a list of all Pokemon
@app.route('/api/pokemon/list', methods=['GET'])
def get_pokemon_list():
    return jsonify(pokemon_data)

# Route for getting a list of Pokemon by type
@app.route('/api/pokemon/type/<string:typeId>', methods=['GET'])
def get_pokemon_by_type(typeId):
    pokemon_by_type = [p for p in pokemon_data if typeId.lower() in p['type'].lower()]
    if pokemon_by_type:
        return jsonify(pokemon_by_type)
    else:
        return jsonify({"error": "No Pokemon found with the specified type"}), 404

if __name__ == '__main__':
    app.run(debug=True)
