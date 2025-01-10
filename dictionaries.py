b = [13,56,24]
for i in b:
    print(i)

for i in range(len(b)):
    print(i,b[i])


students = {"name": "Laurence",
            "age": 15,
             "marks": 88.86 }

print(students)
for i in students:
    print(i)
for i in students.values():
    print(i)
for i in students.keys():
    print(i)
b[1] = 78

if "Laurence" in students["name"]:
    print("yes")

print(b[1]) 
students["name"] = "leo"
print(students.get("name"))
D = {}
details = { }
for i in range(2):
  details["name"]= input("enter your name")
  details["age"]= input("please enter your age")
  



