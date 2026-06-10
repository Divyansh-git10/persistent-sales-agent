from abc import ABC, abstractmethod


class BaseMemory(ABC):

    @abstractmethod
    def save_message(self, user_id, role, content, session_id):
        pass

    @abstractmethod
    def get_history(self, user_id):
        pass

    @abstractmethod
    def clear_memory(self, user_id):
        pass