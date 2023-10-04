#create a dictionary
student_scores ={
    "Mahfuz" : 82,
    "Santa" : 90,
    "Akash" : 80,
    "Masud" : 85,
}

print("Masud's score: ",student_scores["Masud"])
student_scores["Mruf sir"] = 100
print("Adding a score: ",student_scores)
#cheak a if a key is exist or not
if "Mahfuz" in student_scores:
    print("Mahfuz's score is: ",student_scores["Mahfuz"])
else:
    print("Mahfuz's score is not existed")

#Iterating dictionary through key & values
print("After itaretion the discionary is:")
for student,score in student_scores.items():
    print(student, ":", score)

