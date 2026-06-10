from app.memory.sqlite_memory import SQLiteMemory

memory = SQLiteMemory()


def get_user_memory(user_id):

    history = memory.get_history(user_id)

    formatted_history = []

    for msg in history:

        formatted_history.append(
            f"{msg.role}: {msg.content}"
        )

    return "\n".join(formatted_history)