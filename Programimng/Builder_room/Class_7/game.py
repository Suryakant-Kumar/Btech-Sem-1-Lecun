import random
sub = ['FSD','Python','Maths']
student = ['Devang','Surya','Yash','Rohit','Aarav','Aarush','Aaryan','Aditya','Advait','Ahaan']
chosen_stu = random.choice(student)
chosen_sub = random.choice(sub)
print(f"{chosen_stu} is assigned to {chosen_sub} subject.")
remarks = input("Enter your remarks: ")
print(f"Remarks for {chosen_stu}: {remarks}")