from models import db

class Feedback(db.Model):
    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    poi_id = db.Column(db.Integer, db.ForeignKey("pois.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 star rating
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    @classmethod
    def get_by_poi(cls, poi_id):
        return cls.query.filter_by(poi_id=poi_id).all()

    @classmethod
    def create(cls, data):
        feedback = cls(**data)
        db.session.add(feedback)
        db.session.commit()
        return feedback

    @classmethod
    def update(cls, feedback_id, data):
        feedback = cls.query.get(feedback_id)
        if feedback:
            for key, value in data.items():
                setattr(feedback, key, value)
            db.session.commit()
            return feedback
        return None
