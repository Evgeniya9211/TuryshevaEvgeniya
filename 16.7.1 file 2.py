from class_cat import Cat

cats = [{"name": "Барон", "gender": "мальчик", "age": 2},
        {"name": "Сэм", "gender": "мальчик",  "age": 2}]

for cat in cats:
    cat_obj = Cat()
    cat_obj._init_from_dict(cat)
    print("name cat", cat_obj.name)
    print("gender cat", cat_obj.gender)
    print("age cat", cat_obj.age)
    print('\n')

