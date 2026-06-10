from sqlalchemy import Column, Integer, String, Text, Float, Boolean
from app.db.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    role = Column(String)
    content = Column(Text)
    session_id = Column(String)


class EvalLog(Base):
    __tablename__ = "eval_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    groundedness = Column(Float)
    relevance = Column(Float)
    confidence = Column(Float)
    flagged = Column(Boolean)
    reasoning = Column(Text)