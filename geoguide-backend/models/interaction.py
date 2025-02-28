from models import db

class UserInteraction(db.Model):
    __tablename__ = "user_interactions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    poi_id = db.Column(db.Integer, db.ForeignKey("pois.id"), nullable=False)
    interaction_type = db.Column(db.String(50), nullable=False)  # e.g., "visited", "liked"
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    @classmethod
    def get_by_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()
