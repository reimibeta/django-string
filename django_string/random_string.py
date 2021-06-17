import uuid


class RandomString:

    # def __init__(self):
    def ustring(self):
        return uuid.uuid4().hex[:8].upper()


random_string = RandomString()
