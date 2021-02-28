import uuid


class RandomString:

    # def __init__(self):

    @staticmethod
    def ustring():
        return uuid.uuid4().hex[:8].upper()
