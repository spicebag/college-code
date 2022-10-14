# ReportCard.py
# Lets the user enter there results and determines if they get a pass or a fail.
# 13/10/22
# @Author : Killian

# declare variables and get user inputs
from cmath import e


student_name=input("Enter in your name : ")
date_of_birth = input("Enter in your date of birth (dd/mm/yyyy) :")
grade_programming=int(input("Enter in your programming grade % : "))
grade_networking=int(input("Enter in your networking grade % "))
grade_systemhardware=int(input("Enter in your Systems & Hardware grade % : "))
grade_virtualization=int(input("Enter in your virtualization grade % : "))
grade_operatingsystems=int(input("Enter in your operating systems grade % : "))
grade_maths=int(input("Enter in your maths grade % : "))
grade_communications=int(input("Enter in your communications grade % :"))
grade_workexperience=int(input("Enter in your work experience grade % : "))


# start of if statement for programming result
if (grade_programming >79):
                    result_programming="Distinction"
elif (grade_programming >64):
                    result_programming="Merit"
elif (grade_programming >49):
                    result_programming="Pass"
else:
                    result_programming="Unsuccessful"
# end  of if statement for programming result

# start of if statement for networking result
if (grade_networking >79):
                    result_networking="Distinction"
elif (grade_networking >64):
                    result_networking="Merit"
 
elif (grade_networking >49):
                    result_networking="Pass" 
else:
                    result_networking="Unsuccessful"
# end of if statement for networking result

# start of if statement for system hardware result
if (grade_systemhardware >79):
                    result_systemhardware="Dictinction"
elif (grade_systemhardware >64):
                    result_systemhardware="Merit"
elif (grade_systemhardware >49):
                    result_systemhardware="Pass"
else:
                    result_systemhardware="Unsuccessful"
# end of it statement for system hardware result

# start of it statement for virtualization result
if (grade_virtualization >79):
                    result_virtualization="Dictinction"
elif (grade_virtualization >64):
                    result_virtualization="Merit"
elif (grade_virtualization >49):
                    result_virtualization="Pass"
else:
                    result_virtualization="Unsuccessful"
# end of it statement for virtualization result

# start of it statement for operating systems result
if (grade_operatingsystems >79):
                    result_operatingsystems="Dictinction"
elif (grade_operatingsystems >64):
                    result_operatingsystems="Merit"
elif (grade_operatingsystems >49):
                    result_operatingsystems="Pass"
else:
                    result_operatingsystems="Unsuccessful"
# end of it statement for operating systems result

# start of it statement for work experience result
if (grade_workexperience >79):
                    result_workexperience="Dictinction"
elif (grade_operatingsystems >64):
                    result_workexperience="Merit"
elif (grade_operatingsysttems >49):
                    result_workexperience="Pass"
else:
                    result_workexperience="Unsuccessful"
# end of it statement for work experience result

# start of it statement for maths result
if (grade_maths >79):
                    result_maths="Dictinction"
elif (grade_operatingsystems >64):
                    result_maths="Merit"
elif (grade_maths >49):
                    result_maths="Pass"
else:
                    result_maths="Unsuccessful"
# end of it statement for maths result

# start of it statement for communications result
if (grade_communications >79):
                    result_communications="Dictinction"
elif (grade_communications >64):
                    result_communications="Merit"
elif (grade_communications >49):
                    result_communications="Pass"
else:
                    result_communications="Unsuccessful"
# end of it statement for communications result


# Screen Print Out
print ("\n\t*************************************************")
print ("\t*\t\tReport Card\t\t\t*")
print ("\t*\t\t\t\t\t\t\t*")
print("\t*\t"+student_name +"\t"+date_of_birth+"\t\t*")
print ("*************************************************\n")
print ("Module\t\tGrade\t\tResult")
print("Programming\t"+str(grade_programming)+"\t\t"+str(result_programming))
print("Networking\t"+str(grade_networking)+"\t\t"+str(result_networking))
print("Systems Hardware\t"+str(grade_systemhardware)+"\t\t"+str(result_systemhardware))
print("Virtualization\t"+str(grade_virtualization)+"\t\t"+str(result_virtualization))
print("Operating Systems\t"+str(grade_operatingsystems)+"\t\t"+str(result_operatingsystems))
print("Maths\t"+str(grade_maths)+"\t\t"+str(result_maths))
print("Communications\t"+str(grade_communications)+"\t\t"+str(result_communications))
print("Work Experience\t"+str(grade_workexperience)+"\t\t"+str(result_workexperience))





# Outputs the given results into a file that can be read by the user
f=open ("demofile3.txt", "w")
f.write("*************************\n")
f.write("*\tReport Card\t*\n")
f.write("*\t\t\t\t\t\n")
f.write("*************************\n")
f.close()
 
# open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
