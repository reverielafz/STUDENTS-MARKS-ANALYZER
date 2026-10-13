
students={ }
i=0
while i<5:
  name=input("enter name:")
  marks=int(input("enter marks:"))
  i+=1
  students[name]=marks

  
print("\n")
print("\n")

print("\nSTUDENTS MARKS ANALYZER")
print("-"*30)

for name, marks in students.items():
    print(name, ":", marks)


total=0
for marks in students.values():
  
  total+=marks

print ("\n Average marks:",(total)/len(students))




topper = max(students, key=students.get)
print("\nTopper:", topper)
print("Highest marks:", students[topper])

lower = min(students, key=students.get)
print("\nLowest:", lower)
print("Lowest marks:", students[lower])

count=0
for marks in students.values():
  if marks>40:
    count+=1
    
print("\nStudents who scored more than 40 marks:", count)
