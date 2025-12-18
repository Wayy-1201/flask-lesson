from flask import Flask , jsonify , request

app = Flask(__name__)

items = [
    {"id": 1 , "name": "TV"},
    {"id": 2 , "name": "COMPUTER"}
]
#методы - функиця
#анотация - пометка ддя мето-информации как в тг бота 
@app.route('/api/items' , methods=['GET'])
def get_items():
    return jsonify(items)
    

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404



@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    new_id = max((i["id"] for i in items), default=0) + 1 #увеличение id
    new_item = {"id": new_id, "name": data["name"]}  #новый прдмет
    items.append(new_item) #доблавние
    return jsonify(new_item), 201

#скачать post_man

if __name__ == "__main__":
    app.run(debug=True)