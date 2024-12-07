# students={"name": "hammad" , "age":22 , "grade":"A"}
# print(students["grade"])
# students.update ({"age":20})
# print(students)
# st2={"city":" New york"}
# students.update(st2)
# print(students)
# students.pop("city")
# print(students)
# print(students.keys())
# print(students.values())
# print(students.items())
# print(len(students))
# if "grade" in students:
#     print("true")
# else:
#     print("false")
# a=dict(sorted(students.items()))
# print(a)
# a=dict(sorted(students.items(),reverse=True))
# print(a)

# o=[('name', 'Alice'), ('age', 25), ('city', 'Paris')]
# s=dict(o)
# print(s)

# dict_a = {"name": "hammad", "age": 22, "grade": "A"}
# dict_b = {"name": "hammad", "age": 22, "grade": "A"}

# if dict_a == dict_b:
#     print("dict_a and dict_b are identical.")
# else:
#     print("dict_a and dict_b are not identical.")
# nested={
#     "Person":{"name":"John","age":30},
#     "Address":{"Street":"123 Elm St","City":"Lhr"}
# }
# print(nested["Address"]["City"])
# nested["Address"]["phone"]={654598593}
# print(nested)
# del nested["Address"]
# print(nested)
# for keys in nested:
#     print(keys)
# x={'a': 10, 'b': 15, 'c': 7 , 'd':45}
# s=max(x.values())
# print(s)

# squares = {num: num ** 2 for num in range(1, 6)}
# print(squares)

# x = {'a': 10, 'b': 15, 'c': 10, 'd': 15}b
# unique = {}
# for key, value in x.items():
#     if value not in unique.values():
#         unique[key] = value
# print(unique)

# x = {'a': 10, 'b': 18, 'c': 100, 'd': 15}
# y=input("enter an alphabet:  " )
# if y in x.keys():
#     print(x[y])
# else:
#     print("Key not found")

# count=0
# o={"a":"hello world hello python world"}
# for i in o.values():
#     count= i.split().count("hello")
# print(count)

# dict1 = {'a': 5, 'c': 10}
# dict2 = {'a': 3, 'b': 7}
# result = {}
# for key in dict1:
#     if key in dict2:  
#         result[key] = dict1[key] + dict2[key]
# print(result)

# y=int(input("enter an alphabet:  " ))
# x={num: num ** 3 for num in range(1,y+1)}
# print(x)

# original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# filtered_dict = {key: value for key, value in original_dict.items() if value >= 3}

# print(filtered_dict)

# original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# filtered_dict_even = {key: value for key, value in original_dict.items() if value %2==0 }
# filtered_dict_odd = {key: value for key, value in original_dict.items() if value %2!=0 }
# print(filtered_dict_odd)
# print(filtered_dict_even)


