# Yongdong Xi
my_grades = {'End S1 Labs': 100, 'Start S2 Labs': 100, 'Mid-year Project Proposal': 90, 
'Cycle 10 Practice Quiz': 100, 'Cycle 10 Quiz' : 60}
grades = list(my_grades.values())
print(grades)
assignments = list(my_grades.keys())
print(assignments)

for (k,v) in my_grades.items():
    print("name of assignment", k)


for (k,v) in my_grades.items():   
        if v >= 70:
            print(k, ':', v)

for (k,v) in my_grades.items():
    if v <= 50:
        print(k, ':', v)



