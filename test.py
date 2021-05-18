list = [1,2]

try:
    print(list[3])
except Exception as e:
    print(str(e).capitalize())