from crypt import methods
from flask import Flask, render_template, request, redirect
from database import db 

app = Flask(__name__)

@app.route("/")
def get_notes():
    get_list = db.sql("SELECT * FROM note.note_list")
    return render_template("main.html", get_note=get_list)

@app.route("/add", methods=["POST"])
def add_notes():
    get_data = request.form.get('name')
    add_list = db.insert("note", "note_list", [{"title":get_data}])
    return redirect("/")

@app.route("/delete/<string:id>")
def delete_notes(id):
    get_list = db.delete("note", "note_list", [id])
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)