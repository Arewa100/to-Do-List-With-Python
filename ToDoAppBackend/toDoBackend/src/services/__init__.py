from pymongo import MongoClient
from flask import Flask,request, jsonify

client = MongoClient('localhost', 27017)

current_db = client["miracle"]

app = Flask(__name__)


@app.route("/", methods=["POST"])
def register():
    data = request.json
    current_db.users.insert_one(data)
    return jsonify({"msg": "user was saved successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True)


