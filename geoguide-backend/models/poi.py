from models import db

class POI(db.Model):
    __tablename__ = "pois"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def create(cls, data):
        poi = cls(**data)
        db.session.add(poi)
        db.session.commit()
        return poi
