# ReportCard.py
#
#
#

# declare variables and get user inputs
from cmath import e


student_name=input("Enter in your name : ")
date_of_birth = input("Enter in your date of birth (dd/mm/yyyy) :")
grade_programming=int(input("Enter in your programming grade % : "))
grade_networking=int(input("Enter in your networking grade % "))


# start of if statement for programming result
if (grade_programming >79):
                    result_programming="Distinction"
elif (grade_programming >64):
                    result_programming="Merit"
elif (grade_programming >49):
                    result_programming="Pass"
else:
                    result_programming="Unsuccessful"

if (grade_networking >79):
                    result_networking="Distinction"
elif (grade_networking >64):
                    result_networking="Merit"
 
elif (grade_networking >49):
                    result_networking="Pass"
else:
                    result_networking="Unsuccessful"


# Screen Print Out
print ("\n\t*************************************************")
print ("\t*\t\tReport Card\t\t\t*")
print ("\t*\t\t\t\t\t\t\t\t\t\t\t*")
print("\t*"+student_name +"\t"+date_of_birth+"*")
print ("\n\t*************************************************\n")
print ("Module\t\tGrade\t\tResult")
print("Programming\t"+str(grade_programming)+"\t\t"+str(result_programming))
print("Networking\t"+str(grade_networking)+"\t\t"+str(result_networking))


