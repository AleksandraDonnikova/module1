my_dict = {"Vasya": 1975, "Kamila": 1981, "Masha": 2003 }
print("Dict:", my_dict)
print("Existing value:", my_dict["Vasya"])
print("Not existing value:", my_dict.get("Artem"))
my_dict["Artem"] = 1998
my_dict.update({"Leo": 1999})
#попробовала два способа добавления, знаю что через команду update можно добавить сразу два ключа со значением
a = my_dict.pop("Kamila")
print("Deleted value:", a)
print("Modified dictionary:", my_dict)
#множества
my_set = { 1, 2, 2, "lol", "lol", False, False, 6, 6, 6}
print("Set:", my_set)
my_set.add(3)
my_set.add("Bruno")
my_set.discard(6)
print("Modified set:",my_set)
