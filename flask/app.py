from flask import Flask, render_template ,request ,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os




# Initialize app and config
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "todo.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
db = SQLAlchemy(app)

# Define model
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# Routes
@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        title = request.form["title"]
        desc = request.form["desc"]

        todo = Todo(title = title,desc = desc)
        db.session.add(todo)
        db.session.commit()
    alltodo = Todo.query.all()
    return render_template("index.html",alltodo=alltodo)

@app.route("/products")
def products():
    return "This is the products page"

# Optional: Route to create the database (for dev use only)
@app.route("/create-db")
def create_db():
    db.create_all()
    return "Database created successfully!"

@app.route("/update")
def update():
    return "This is the products page"

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo) 
    db.session.commit()
    return redirect("/")


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
