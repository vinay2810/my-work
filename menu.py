import json
input_file = open('menu_students.json','r')
input_file_decode = json.load(input_file)
print(input_file_decode)

for i,j in input_file_decode.items():
    print(i)
    for x in j:
        print(x.Name)