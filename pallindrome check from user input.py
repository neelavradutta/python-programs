dict={
"hello": "hi everyone",
"bye": 52,
"class": {
    "num1":1,
    "num2":10,
    "num3":3
}
}
print(dict.values())
print(dict.items())
print(dict.get("bye"))
new_dict={"hello":2, "hell":3}
dict.update(new_dict)
print(dict)