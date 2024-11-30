immutable_var = (1,2,"Green",4,5,6,True,8)
print("Immutable tuple:",immutable_var)
#immutable_var[0] = 3 кортеж неизменяемый, потому что в нем содержится не сам список, а ссылка на него. Ее изменить нельзя.
mutable_list = [7,2,"a","b","Modified"]
mutable_list[0] = 1
print("Mutable list:",mutable_list)
