from app.memory.sqlite_memory import SQLiteMemory

memory = SQLiteMemory()

memory.save_message(
    user_id="divyansh",
    role="user",
    content="What is enterprise pricing?",
    session_id="123"
)

history = memory.get_history("divyansh")

for msg in history:
    print(msg.role, ":", msg.content)