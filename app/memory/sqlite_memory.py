from app.memory.base import BaseMemory
from app.db.database import SessionLocal
from app.db.models import Message


class SQLiteMemory(BaseMemory):

    def save_message(self, user_id, role, content, session_id):

        db = SessionLocal()

        message = Message(
            user_id=user_id,
            role=role,
            content=content,
            session_id=session_id
        )

        db.add(message)
        db.commit()
        db.close()

    def get_history(self, user_id):

        db = SessionLocal()

        messages = db.query(Message).filter(
            Message.user_id == user_id
        ).all()

        db.close()

        return messages

    def clear_memory(self, user_id):

        db = SessionLocal()

        db.query(Message).filter(
            Message.user_id == user_id
        ).delete()

        db.commit()
        db.close()