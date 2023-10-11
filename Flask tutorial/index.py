from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import inspect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the SQLAlchemy model for 'MarketItem'
class MarketItem(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

# Function to insert items if they don't exist
def insert_items():
    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.has_table('market_item'):
            db.create_all()

            # Insert items into the 'market_item' table
            item1 = MarketItem(name='Phone', price=600, barcode='8932212299897', description='A mobile phone.')
            item2 = MarketItem(name='Laptop', price=900, barcode='123985473165', description='A laptop computer.')
            item3 = MarketItem(name='Keyboard', price=150, barcode='2319851228446', description='A computer keyboard.')

            db.session.add_all([item1, item2, item3])
            db.session.commit()

# Check if the 'market_item' table exists in the database; if not, create it
insert_items()

# Routes for your application
@app.route('/')
@app.route('/home')
def helloworld():
    return render_template('home.html', market_items=MarketItem.query.all())

@app.route('/market')
def marketPage():
    return render_template('market.html', market_items=MarketItem.query.all())

@app.route('/base')
def basePage():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
