#!/usr/bin/python3
# Environment variable
# source virtualenv_name/bin/activate

import datetime
from prettytable import PrettyTable
import pyfiglet 
import os
import re

text = pyfiglet.figlet_format(text="scorpiontechsoft")
print(text)


class Resume:
    def add(self):
        print()
        # Personal Information Adding

        print("Enter personal Information")
        
        while True:
            Name = (input("[*]  Enter your Name : ")).strip()
            if re.match(r"^[a-zA-Z\s]+$", Name):
                Name = Name
                break
            else :
                print("[*]  Name should have only Alphabetics\n")    

        while True:
            try :
                mobileno = int(input("[*]  Enter your Mobile No : "))
                mobileno_str = str(mobileno)    
                if (10 == len(mobileno_str)):
                    break
                else:
                    print("\n[*]  Error : Enter a valid mobile number\n")
            except Exception :
                print("\n[*]  Mobile number do not have a characters || Try Again \n")   

        while True:
            emailid = input("[*]  Enter your Email ID : ").strip().lower()
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', emailid):
                emailid = emailid
                break
            else :
                print("\n[*]  Email Id Syntax is not matching \n")   

        while True:
            try :  
                dob = input("[*]  Enter your Date of Birth (dd/mm/yyyy): ")
                dob = datetime.datetime.strptime(dob, "%d/%m/%Y")
                break
            except Exception as e :
                print("[*]  ",e)  
        print()

        career_objective = input("[*]  Enter Career Objective : ")

        #Expirience Adding
        jobTitle = []
        jobDescription = []

        expierence = input("\n[*]  Do you Have any Expirence : (y/n)")

        while True:

            if expierence == 'n':
                break

            elif (expierence == 'y'):
                
                while True:   

                    jobTitle.append(input("[*]  Enter Job Role : "))
                    jobDescription.append(input("[*]  Enter Job Description : "))

                    expierence = input("[*]  Do you want to add another (y/n) ")
                    expierence = expierence.lower() 

                    if expierence == 'n':
                        break
                    elif expierence == 'y':
                        pass
                    else :
                        print("\n[*]  Enter Vaild key\n")

            else :
                print("[*]  Enter valid input")
                expierence = input("[*]  Do you have any Experience : ")        
                
        #Skills Adding
        skills=[]
        while True:
            skillsChoice = input("\n[*]  Do you want to add skills (y/n) : ")
            skillsChoice = skillsChoice.lower() 
            if skillsChoice == 'n':
                break
            elif skillsChoice == 'y':
                skills.append(input("[*]  "))
            else :
                print("[*]  Enter Vaild key")

        # Education Adding    
        
        while True:
            try :
                print("\n[*]  Select your highest qualification :")
                edu = int(input("[*]  1 : Masters || 2. Bachelors || 3. Pre University Education || 4. sslc  : "))
                t = PrettyTable(['stream','College Name','Marks / Grade','year of pass'])
                break
            except Exception :
                print("\n[*]Enter a correct choice") 

        while True:

            if edu == 1:
                masters_stream = input("\n[*]  Enter your Masters Stream :").strip()
                masters_clgname = input("[*]  Enter College Name : ").strip()
                masters_cgpa = input("[*]  Enter cgpa : ").strip()
                masters_yearofpass = input("[*]  Enter year of pass : ").strip()
                t.add_row([masters_stream,masters_clgname,masters_cgpa,masters_yearofpass])
                edu=edu+1
            elif edu == 2:
                bachelors_stream = input("\n[*]  Enter your Bachelors Stream :").strip()
                bachelors_clgname = input("[*]  Enter College Name : ").strip()
                bachelors_cgpa = input("[*]  Enter cgpa : ").strip()
                bachelors_yearofpass = input("[*]  Enter year of pass :").strip()
                t.add_row([bachelors_stream,bachelors_clgname,bachelors_cgpa,bachelors_yearofpass]) 
                edu = edu+1
            elif edu == 3:
                pu_stream = input("\n[*]  Enter a pu Stream : ").strip()
                pu_clgname = input("[*]  Enter College Name : " ).strip()
                pu_marks  = int(input("[*]  Enter marks or grade : ").strip())
                pu_yearofpass = input("[*]  Enter year of pass : ").strip()
                t.add_row([pu_stream,pu_clgname,pu_marks,pu_yearofpass])
                edu = edu+1
            elif edu == 4:
                schoolname = input("\n[*]  Enter School Name : ").strip()
                school_marks  = input("[*]  Enter marks or grade : ").strip()
                school_yearofpass = input("[*]  Enter year of pass :").strip()
                t.add_row(["school",schoolname,school_marks,school_yearofpass])
                edu = 'end'
            elif edu == 'end':
                break
            else :
                edu = input("\n[*]  Enter a vaild key : ")


        # Projects Adding
        projects = [] 
        projects_description = []
        projects_choice = input("\n[*]  Do you Have any Academic Projects : (y/n)")
        while True:
            if projects_choice == 'n':
                break

            elif (projects_choice == 'y'):
                
                while True:   

                    projects.append(input("[*]  Enter Project Name : "))
                    projects_description.append(input("[*]  Enter project Description : "))

                    projects_choice = input("\n[*]  Do you want to add another (y/n)")
                    projects_choice = projects_choice.lower() 

                    if projects_choice == 'n':
                        break
                    elif projects_choice == 'y':
                        pass
                    else :
                        print("\n[*]  Please Enter Vaild ")

            else :
                print("[*]  Enter valid input")
                projects_choice = input("[*]  Do you have any projects : ")        
        
        
        # Hobbies Adding
        hobbies = [] 
        hobbies_choice = input("\n[*]  Do you Have any Hobbies : (y/n)")
        while True:
            if hobbies_choice == 'n':
                break

            elif (hobbies_choice == 'y'):
                
                while True:   

                    hobbies.append(input("[*]  Enter Hobby : "))

                    hobbies_choice = input("\n[*]  Do you want to add another (y/n)")
                    hobbies_choice = hobbies_choice.lower() 

                    if hobbies_choice == 'n':
                        break
                    elif hobbies_choice == 'y':
                        pass
                    else :
                        print("\n[*]  Enter Vaild key")

            else :
                print("[*]  Enter valid input")
                hobbies_choice = input("[*]  Do you have any Hobbies : ")      

         #Strengths Adding   
        strengths=[]
        while True:
            strengthChoice = input("\n[*]  Do you want to add Strengths (y/n) : ")
            strengthChoice = strengthChoice.lower() 
            if strengthChoice == 'n':
                break
            elif strengthChoice == 'y':
                strengths.append(input("[*]  "))
            else :
                print("\n[*]  Enter Vaild key")      

        #weakness Adding
        weakness=[]
        while True:
            weaknessChoice = input("\n[*]  Do you want to add Weakness (y/n) : ")
            weaknessChoice = weaknessChoice.lower() 
            if weaknessChoice == 'n':
                break
            elif weaknessChoice == 'y':
                weakness.append(input("[*]  "))
            else :
                print("\n[*]  Enter Vaild key")      


        print("\n[*]  Data Saved\n")



        # File creation

        directory = "/home/scorpion/Desktop/programming/python/"
        filepath = directory + Name
        filepath = filepath + ".txt"
            
        #password = input("\n [*]  Enter password for secure your information : ")

        #printing personal information    
        with open(filepath , "w") as file:
            file.write("Personal Information\n")
            file.write("\n")
            lines = ["Name : {}  \nMobile No : {} \nEmail ID : {} \nDOB : {} ".format(Name,mobileno,emailid,dob.strftime("%d %b, %Y"))]
            file.writelines(lines)
            file.write("\n\nCarear Objective : {}".format(career_objective))
            file.write("\n\n\n")
            
            #expirence printing
            file.write("Expirence : \n")
            if len(jobTitle) == 0:
                file.write("             Fresher")
            else :
                for i in range(len(jobTitle)):
                    lines = ["             Job Title : {} \n             job description : {}\n".format(jobTitle[i],jobDescription[i])]
                    file.writelines(lines)
            
            #skills printing
            file.write("\n")
            if len(projects) == 0:
                pass
            else :
                file.write("Skills : \n")
                for s in range(len(skills)):
                    lines = ["       * {}".format(skills[s])]
                    file.writelines(lines)

            #Education printing
            file.write("\n\n")
            file.write("Education Details : \n")
            file.write("\n")
            lines = ["        "]
            file.write(str(t))


            #projects printing
            if len(projects) == 0:
                pass
            else :
                file.write("\n")
                file.write("\nAcademic Projects : \n")
                for i in range(len(projects)):
                    lines = ["             Project Name : {} \n             Project Description : {}\n\n".format(projects[i],projects_description[i])]
                file.writelines(lines)

            #Hobbies printing
            if len(hobbies) == 0:
                pass
            else :
                file.write("\n")
                file.write("\nHobbies : \n")
                for i in range(len(hobbies)):
                    lines = ["             {} \n".format(hobbies[i])]
                file.writelines(lines)    


            #strengths printing

            if len(strengths) == 0:
                pass
            else :
                file.write("\nStrengths : \n")
                for i in range(len(strengths)):
                    lines = ["             *{} ".format(strengths[i])]
                    file.writelines(lines)

            #weakness printing
            if len(weakness) == 0:
                pass
            else :
                file.write("\nWeakness : \n")
                for i in range(len(weakness)):
                    lines = ["             *{} ".format(weakness[i])]
                    file.writelines(lines)
                
                
            print("\n[*]  File created\n")
        file.close()


        print("[*]  Your File Name : {}.txt\n\n ".format(Name))
    
    # Edit the file   
    # def edit(self):
    #     while True:
    #         fileName = input("\n[*]  Enter File Name : ")
    #         directory = "/home/scorpion/Desktop/programming/python/"
    #         filepath = directory + fileName
            
    #         print("\n\n")
    #         try :
    #             isExist = os.path.exists(filepath) 
    #             with open(filepath,"w") as file :
    #                 break     
    #         except Exception:
    #             print("File not found Please enter correct file name")    


    #     print("\n[*]  Select Edit Section : ")
    #     print("[*]  1. Personal Information")
    #     print("[*]  2. Experience")
    #     print("[*]  3. Skills")
    #     print("[*]  4. Education")
    #     print("[*]  5. Projects")
    #     print("[*]  6. Hobbies")
    #     print("[*]  7. Skills")
    #     print("[*]  8. Education")
    #     print("[*]  9. Exit")

    #     try :
    #         edit_choice = int(input("[*]  Enter your choice : "))

    #         if edit_choice == 1:

    #             while True:
    #                 print("\n[*]  Select the context")
    #                 print("[*]  1.Name")
    #                 print("[*]  2.Mobile No")
    #                 print("[*]  3.Email ID")
    #                 print("[*]  4.DOB")
    #                 perinfo = input("[*]  Enter your choice : ")
    #                 if perinfo == 1:
    #                     newName = input("[*]  Enter of Enter Name : ") 
    #                     search_text = ""
    #                     replace_text = newName

    #                     with open(r'filepath', 'r') as file: 
    #                         data = file.read() 
    #                         data = data.replace(search_text, replace_text) 

    #                     with open(r'filepath', 'w') as file: 
                        
    #                         file.write(data) 
    #                     print("Text replaced") 

    #                 elif choice == 2:   
    #                     pass
    #                 elif choice == 3:
    #                     pass
    #                 elif choice == 4:
    #                     pass
    #                 else:
    #                         print("\n[*]  Invaild! please enter correct choice\n")

    #         elif edit_choice == 2:   
    #             pass
    #         elif edit_choice == 3:
    #             pass
    #         elif edit_choice == 4:
    #             pass
    #         elif edit_choice == 5:
    #             pass
    #         elif edit_choice == 6:
    #             pass
    #         elif edit_choice == 7:
    #             pass
    #         elif edit_choice == 8:
    #             pass
    #         elif edit_choice == 9:
    #             exit()
    #         else:
    #             print("\n[*]  Invaild! please enter correct choice\n")
    #     except Exception:
    #         print("\n[*]  Invaild! please enter correct choice\n")    

            
    def view(self):

        while True:
            fileName = input("\n[*]  Enter File Name : ")
            directory = "/home/scorpion/Desktop/programming/python/"
            filepath = directory + fileName
            filepath = filepath + ".txt"
            
            print("\n\n")
            try :
                isExist = os.path.exists(filepath) 
                with open(filepath,"r") as file :
                    for x in file:
                        print(x) 
                    print("\n\n")    
                    break     
            except Exception:
                print("File not found Please enter correct file name")    


resume = Resume()

    
print("[*]   Build your resume with Command line interface")
print("---------------------------------------------------")
while True:
    print("[*]  Enter 1 for Create Resume")
    print("[*]  Enter 2 for View resume")
    print("[*]  Enter 3 for exit")
    
    try :
        choice = int(input("[*]  Enter your choice : "))

        if choice == 1:
            resume.add()
        elif choice == 2:
            resume.view()
        elif choice == 3:
            exit()   
        else:
            print("\n[*]  Invaild! please enter correct choice\n")
    except Exception:
        print("\n[*]  Invaild! please enter correct choice\n")