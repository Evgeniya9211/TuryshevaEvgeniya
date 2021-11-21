class Cat:
    def __init__(self, name="", gender="", age=0):
        self.name = name
        self.gender = gender
        self.age = age

    def _init_from_dict(self, cat_dict):
        self.name = cat_dict.get("name")
        self.gender = cat_dict.get("gender")
        self.age = cat_dict.get("age")