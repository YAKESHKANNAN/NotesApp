from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/NotesAppData.notes"
mongo = PyMongo(app)

@app.route("/")
def index():
    notes = list(mongo.db.notes.find())  # fetch all notes
    return render_template("index.html", notes=notes)


@app.route("/add", methods=["POST"])
def add_note():
    title = request.form.get("title")
    content = request.form.get("content")

    if title and content:
        mongo.db.notes.insert_one({"title": title, "content": content})
    return redirect(url_for("index"))

@app.route("/edit/<id>", methods=["POST"])
def edit_note(id):
    title = request.form.get("title")
    content = request.form.get("content")

    if title and content:
        mongo.db.notes.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"title":title, "content":content}}
            )
        return redirect(url_for("index"))


@app.route("/delete/<id>")
def delete_note(id):
    mongo.db.notes.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)