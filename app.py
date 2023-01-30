from datetime import datetime
from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/exchange_rate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api()


class UAN(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.date)
    rate_to_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<ExchangeRate %r>' % self.id


class PLN(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.date)
    rate_to_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<ExchangeRate %r>' % self.id


class EUR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.date)
    rate_to_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<ExchangeRate %r>' % self.id


class CAD(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.date)
    rate_to_usd = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<ExchangeRate %r>' % self.id


class Main(Resource):
    def get(self):
        return {"info": "Some info", "nun": 56}


api.add_resource(Main, "/api/main")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")

