from flask import Flask, request, jsonify
app = Flask(__name__)

from repository.grocery_loader import read_csv_to_dict
from repository.grocery_loader import write_list_of_dicts_to_csv


#Carga en memoria
data = read_csv_to_dict('src/sample_grocery.csv')

#GET
# http://localhost:8081/items
@app.route("/items", methods=["GET"])
def hello_get():
    return jsonify(data)

#GET SKU
# http://localhost:8081/items
@app.route("/get/<string:sku>", methods=["GET"])
def get(sku):
    for item in data:
        if item['SKU'] == sku:
            return jsonify(item)
    return jsonify({})

#POST
# http://localhost:8081/items
@app.route("/post", methods=["POST"])
def post():
    new_post = request.json
    data.append(new_post)
    write_list_of_dicts_to_csv("src/sample_grocery.csv", data)
    return jsonify(new_post)

# DELETE
# http://localhost:8081/items
@app.route("/delete/<string:sku>", methods=["DELETE"])
def delete(sku):
    for item in data:
        if item['SKU'] == sku:
            data.remove(item)
            write_list_of_dicts_to_csv("src/sample_grocery.csv", data)
            return jsonify()
    return jsonify()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
