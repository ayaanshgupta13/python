from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)    
fake = Faker()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

def seed_data():
    """Create DB and seed if it doesn't exist."""
    if not os.path.exists("products.db"):
        db.create_all()
        print("Seeding database with fake products...")
        products = [
            Product(
                name=fake.catch_phrase(),
                description=fake.paragraph(nb_sentences=5),
                price=round(fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=10, max_value=999), 2)
            )
            for _ in range(10000)
        ]
        db.session.bulk_save_objects(products)
        db.session.commit()
        print("Done seeding!")

@app.route('/')
def index():
    products = Product.query.limit(20).all()
    return render_template('index3.html', products=products)

@app.route('/product/<int:product_id>')
def product_page(product_id):
    product = Product.query.get(product_id)
    if not product:
        abort(404)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    with app.app_context():  # Required to work with the DB outside a request
        seed_data()
    app.run(debug=True)
