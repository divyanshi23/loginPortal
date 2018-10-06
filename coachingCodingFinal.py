"""
BLUE BEAM EDUCATION HUB
This program is meant for implementing OOP, File and exception handling 
Submitted by: Priyanshi Agarwal,Anukriti Garg,Divyanshi Agarwal
Submitted to: Ms Meena Dogra
"""
# importing modules
import pickle
import os

# global variable
FormattingLength=80                       #for uniform modifiable formatting of output
Path=os.getcwd()+"/DataFiles/"    #for storing directory of data files

#global functions

def ReadAll(file_name):         # to read a file 
    try:
        fr=open(Path+file_name,"r")
        print fr.read()
        fr.close()
        print "="*FormattingLength
    except IOError:
        print "No such file exists"
        
# to read a file in reverse order
def ReadRev(file_name):     
    try:
        fr=open(Path+file_name,"r")
        l=fr.readlines()
        l.reverse()
        for i in l:
            print i,
        fr.close()
        print "="*FormattingLength
    except IOError:
        print "No such file exists"
    
# repeatedly input a value from a given list
def Inp(prompt,possible_values,char=False): 
    while True:
        try:
                if char==False:
                    x=input(prompt)
                else: #executed when we wish to accept a string as input
                    x=raw_input(prompt).upper()[0]
                    
                if x in possible_values:
                    return x
                else:
                    print "Invalid value Try Again"
                    continue
            
        except NameError:#when global variable or a function is not found
            print  "Invalid Input Try Again"
        except:
            print "Error Try Again"

# to input an integer while handling the TypeError
def InputInt(prompt=""):        
    while True:
        try:
            x=input(prompt)     # doubtful statement
            if type(x)!=int:
                print "You were supposed to enter an Integer:"
                continue#will move the execution back to starting of loop
        except :        # Exception raised when a value incompatible with input is entered
            print "Name Error:You were supposed to enter an Integer:"
            continue 
        else:           # Exception not raised
            return x    #it will automatically terminate the loop
        

# function to calculate Rank Performance Index
"""     Criterion for calculation
Maths --> 37% of marks scored
Physics --> 33% of marks scored
Chemistry --> 30% of marks scored
"""
def calcRPI(marks):  #marks is a nested list   
    Sum=[0,0,0]
    count=0   #counter to calculate the no. of tests
    for i in marks:# i-marks of one test in form of list[P,C,M]
        Sum=[Sum[0]+i[0],Sum[1]+i[1],Sum[2]+i[2]]
        count+=1   
    tot=0.33*Sum[0]+0.3*Sum[1]+.37*Sum[2]
    """Round a number to a given precision in decimal digits (default 0 digits).
    This always returns a floating point number.  Precision may be negative."""
    rpi=round((tot/1.2),2)#(tot/120)*100;;;;;rounds off to 2 digits
    return rpi

#function to input password
def inppswrd():     
        #PASSWORD CONSTRAINT
        print "Password must contain atleast 1 number, 1 alphabet & a special character"
        print "It must be atleast 5 characters long but not more than 16 characters"

        alpha=0
        num=0
        spc=0
        while True:
            pswrd=raw_input("Enter Password:")

            for i in pswrd:
                if ord(i) in range(65,91) or ord(i) in range(97,123):
                    alpha=alpha+1
                elif ord(i) in range(48,58):
                    num=num+1
                else:
                    spc=spc+1

                    
            #checks
                    
            if len(pswrd)<5:
                print "Too Short"
                continue
            elif len(pswrd)>16:
                print "Exceeded Character limit"
                continue
            elif (alpha==0 or num==0 or spc==0):
                print "Invalid Combination"
                continue
            else:       #password Accepted
                break 
        return pswrd




# CENTRAL FUNCTION TO ALLOW A MEMBER TO LOGIN AND THEREBY DEFINE HIS ACCESS & FACILITIES
def login():
    print "=+"*(FormattingLength/2)
    print "Login Portal".center(100)
    print "=+"*(FormattingLength/2)
    m1=Member()#defines it with null values
    while True:
        fr=open(Path+"ID.dat",'r')
        ID=raw_input("Enter your Login ID:")
        try:
            while True:
                m1=pickle.load(fr)
                if m1.id ==ID:
                        break #breaks inner while
        except EOFError:
            print "This ID Does not exists TRY AGAIN"
            fr.close()
            continue #if id does not match
        fr.close()
        break #if id matches, control breaks outer while

    # three possible attempts to enter password
    for i in range(3):
        print "Enter your Password(",3-i,"Try(s) Remaining):",
        pswrd=raw_input()
        if pswrd ==m1.pswrd:
            break # password correct continue ahead normally
        elif pswrd !=m1.pswrd:
           print "Password Incorrect"
           if i==2:
               print "Maximum number of trials expired\nAuthentication Failure\nExiting out of program"
               import sys
               sys.exit()
               
            
    print "="*FormattingLength
    #member found
            
    if m1.type==1:# the user is a student
        obj=Student()
        obj=obj.getValues(m1.eno)# fetching details of the current user
        print ("Hello "+obj.name.split()[0]).center(100) # greeting user by his first name
        while True:
            x=obj.hlp()
            if x==1:
                h1.news()
            elif x==2:
                ReadAll("Timetable.txt")
            elif x==3:
                obj.viewResult()
            elif x==4:
               obj.submitQ()
            elif x==5:
                obj.viewfaq()
            elif x==6:
                m1.changepswrd()
            elif x==7:
                obj.viewInfo()
            elif x==8:
                obj.updatePersonalData()
                
            ch=Inp("Logout <Y/N>:",['Y','N'],True)
            if ch =='Y':
                print "Signing Out"
                break
            
    elif m1.type==2:#login-ed user is a faculty member
        obj=Faculty()
        obj=obj.getValues(m1.eno) #fetching details of the current user
        print ("Hello "+obj.name.split()[0]).center(100) # greeting user by his first name
        
        while True:
            x=obj.hlp()
            if x==1:
                h1.news()
            elif x==2:
                obj.postNews()
            elif x==3:
                ReadAll("Timetable.txt")
            elif x==4:
                obj.viewResult()
            elif x==5:
                obj.viewQ()
            elif x==6:
                obj.updatemarks()
            elif x==7:
                m1.changepswrd()
            elif x==8:
                obj.viewInfo()
            elif x==9:
                obj.updatePersonalData()
                
            ch=Inp("Logout <Y/N>:",['Y','N'],True)
            if ch =='Y':
                print "Signing Out"
                break

    elif m1.type==0:#user is administrator(with full access authorities)
            print "Welcome Admin".center(100)
            while True:
                x=a1.hlp()
                print "="*int(FormattingLength)
                if x == 1:
                    h1.news()
                elif x==2:
                    a1.postNews()
                elif x==3:
                    ReadAll("Timetable.txt")
                elif x==4:
                    a1.updateAch()
                elif x==5:
                    ReadAll("Feedback.txt")
                elif x==6:
                    a1.add()
                elif x==7:
                    a1.viewStuInfo()
                elif x==8:
                    a1.viewFacInfo()
                elif x==9:
                    a1.updateStud()
                elif x==10:
                    a1.updateFaculty()
                elif x==11:
                    a1.addTestMarks()
                elif x==12:
                    a1.delMember()
                elif x==13:
                    a1.delMember(2)#2 for deleting a faculty
                elif x==14:
                    a1.TestResult()
                elif x==15:
                    m1.changepswrd()
                ch=Inp("Logout <Y/N>:",['Y','N'],True)
                if ch =='Y':
                    print "Signing Out"
                    break


# This is the class for the software manager giving him complete access over the data of both faculty and students
class Admin:

    # to display options available to user and accept his choice
    def hlp(self): 
        print "_"*FormattingLength
        print "You can do a lot many things!"
        print "Press 1 To View the Notices and announcements "
        print "Press 2 To Post a Notice "
        print "Press 3 To View the Timetable "
        print "Press 4 To update Achievements "
        print "Press 5 To view feedback submitted"
        print "Press 6 To add a student/faculty "
        print "Press 7 To view student(s) information "
        print "Press 8 To view faculty(s) information "
        print "Press 9 To update student data "
        print "Press 10 To update faculty data "
        print "Press 11 To add marks of latest test"
        print "Press 12 To delete a student's record"
        print "Press 13 To delete a faculty's record"
        print "Press 14 To view Test-wise performance"
        print "Press 15 To change password\n"
        x= Inp("Enter your choice:",range(1,16))
        return x

    # function to add details of either a faculty or a student
    def add(self):
        m1=Member()
        m1.add()
        if m1.type==1:#Student
            s1=Student()
            s1.eno=m1.eno
            s1.name=raw_input("Enter Name:")
            while True:
                s1.batch=raw_input("Enter Batch Code:").upper()
                #BATCH CODE CONSTRAINTS

                if len(s1.batch)!=9:
                    print "Length of Batch Code Must be 9 characters"
                    continue
                elif not s1.batch[0:4].isalpha():
                    print "First Three Letters Must Represent The City Code.TRY AGAIN"
                    continue
                elif not s1.batch[4:6].isdigit():
                    print "Fifth and Sixth character must specify the year of entering and leaving"
                    continue
                elif s1.batch[4] not in ['3','4','5','6']: #No admission for 8th class, '2013' for case:joined in 9 and dropped 
                    print "Invalid Year of Admission"
                    continue
                elif s1.batch[5] not in ['7','8','9','0']: # 9th class student will appear in 2020
                    print "Invalid Year of Appearance in JEE"
                    continue
                elif s1.batch[3] not in ['R','W','O']:
                    print "Invalid Batch Type"
                else: #acceptable Batch Code
                    break
                
                    
            print "Enter marks on the basis of Entrance Exam"
            l=[]
            for i in range(3):
                while True:
                    print "Enter marks in Subject",i+1,":",
                    x=InputInt("")
                    if x>120:
                          print "Maximum marks are 120"
                          continue
                    l.append(x)
                    break
            s1.marks.append(l) #Appending marks of admission test
            s1.rpi=calcRPI(s1.marks)
            s1.assignBatch()    #assigns a batch type

            #fee input
            s1.scholarship()    #finds fee to be paid
            print "Fee Due = Rs",s1.fee
            while True:
                fees=InputInt("Fee Paid:")
                if fees>s1.fee:
                    print "Paid fee exceeds fee due!!! TRY AGAIN"
                    continue
                else:
                    s1.feepaid=fees    #adding to paid fee record
                    break

            # to input personal details
            s1.address=raw_input("Enter Address:")
            s1.contactNo=raw_input("Enter Contact Number:")
        
            fw=open(Path+"StudentData.dat",'ab')
            pickle.dump(s1,fw)
            fw.close()
            print "Student added successfully"
          
        if m1.type==2:#Faculty
            f1=Faculty()
            f1.eno=m1.eno
            f1.name=raw_input("Enter Name:")
            f1.subject=Inp("Enter Subject:",['P','C','M'],True)
            f1.address=raw_input("Enter Address:")
            f1.contactNo=raw_input("Enter Contact Number:")
            f1.salary=input("Enter the salary:")
            fw=open(Path+"FacultyData.dat",'ab')
            pickle.dump(f1,fw)
            fw.close()
            print "Faculty added successfully"
        
    #To post notice to the bulletin board
    def postNews(self):
        fw=open(Path+"News.txt","a")
        s=raw_input("Enter the notice/news:")+'\n'
        fw.write(s)
        print "Notice posted"
        fw.close()

    # function to add milestones of honor and grandeur to the bulletin
    def updateAch(self):
        fw=open(Path+"Achievements.txt","a")
        s=raw_input("Enter the good news:")+'\n'
        fw.write(s)
        print "Achievement added"
        fw.close()

    #function to add marks of students of a particular batch in new test
    def addTestMarks(self):
       while True: 
            inpbatch=raw_input("Enter Batch Code:")
            found=0
            fr=open(Path+"StudentData.dat","rb")
            fw=open(Path+"temp.dat","wb")

            try:
                print "If any Student has not written the test please ENTER  0 in his marks"
                while True:
                    obj=pickle.load(fr)
                    if obj.batch==inpbatch:
                        found=1
                        print "\nEnrollment NO:",obj.eno,"\t\tName:",obj.name
                        l=[0,0,0]
                        subjectname=["Physics","Chemistry","Mathematics"]
                        for i in range(3):
                            l[i]=InputInt("Enter marks in "+subjectname[i]+":")
                            if l[i]>120:
                                print "Maximum Marks are 120 ! Enter Again"
                                i=i-1
                                continue
                        obj.marks.append(l)
                        obj.rpi=calaRPI(obj.marks)
                        obj.assignBatch()
                    pickle.dump(obj,fw)
                        
            except EOFError:
                fr.close()
                fw.close()
                os.remove(Path+"StudentData.dat")
                os.rename(Path+"temp.dat",Path+"StudentData.dat")
            if found==1:
                print "Marks of students of",inpbatch,"added to record"
                print "-"*FormattingLength
                break
            else:
                print "Non Existent Batch Code Entered ! Try again"
                continue

    # function to modify details of student
    def updateStud(self):
        found=0
        try:
            fr=open(Path+"StudentData.dat",'rb')
            fw=open(Path+"temp.dat",'wb')
            x=raw_input("Enter Enrollment Number:")
            while True:
                a=pickle.load(fr)
                if a.eno==x:
                    found=1
                    a.name=raw_input("Enter Name:")
                    
                    ch=Inp("Change marks?Y/N",['Y','N'],True)
                    if ch=='Y':
                        testcode=InputInt("Enter Test serial:")
                        for i in range(3):
                            a.modify(i,testcode)
                            
                    ch=Inp("Change Personal Details?Y/N",['Y','N'],True)
                    if ch=='Y':
                        a.address=raw_input("Enter Address:")
                        a.contactNo=raw_input("Enter Contact Number:")
                        
                    ch=Inp("Update Fee Record?Y/N",['Y','N'],True)
                    if ch=='Y':
                        while True:
                            x=InputInt("Enter fees paid:")
                            if (a.feepaid+x)>a.fee:
                                print "Paid fee exceeds fee due!!! TRY AGAIN"
                                continue
                            else:
                                a.feepaid+=x    #adding to paid fee record
                                break
                            
                pickle.dump(a,fw)
        except EOFError:
            fr.close()
            fw.close()
            os.remove(Path+"StudentData.dat")
            os.rename(Path+"temp.dat",Path+"StudentData.dat")
        except IOError:
            print "No Student Added"
            return
            
        if found==0:
            print "No matching Record"
        else:
            print "Record Updated"

    # To update particulars of a faculty
    def updateFaculty(self):
        found=0
        try:
            fr=open(Path+"FacultyData.dat",'rb')
            fw=open(Path+"temp.dat",'wb')
            x=raw_input("Enter Employee Number:")
            while True:
                a=pickle.load(fr)
                if a.eno==x:
                    found=1
                    a.name=raw_input("Enter Name:")
                    a.subject=Inp("Enter Subject:",['P','C','M'],True)
                    
                    ch=Inp("Change Personal Details?Y/N",['Y','N'],True)
                    if ch=='Y':
                        a.address=raw_input("Enter Address:")
                        a.contactNo=raw_input("Enter Contact Number:")
                pickle.dump(a,fw)
        except EOFError:
            fr.close()
            fw.close()
            os.remove(Path+"FacultyData.dat")
            os.rename(Path+"temp.dat",Path+"FacultyData.dat")
        except IOError:
            print "No Faculty Added"
            return
        
        if found==0:
            print "No matching Record"
        else:
            print "Record Updated"

        
    # function to delete a pre-existing member(student/faculty)
    def delMember(self,ty=1):
        if ty==1:
            s=Path+"StudentData.dat"
        elif ty==2:
            s=Path+"FacultyData.dat"
        dic={1:"Enrollment number",2:"Employee id"}
        found=0
        x=raw_input("Enter "+dic[ty]+" :")
        try:
            fr=open(s,'rb')
            fw=open(Path+"temp.dat","wb")
            while True:
                a=pickle.load(fr)
                if a.eno!=x:
                    pickle.dump(a,fw)
                else: # member to be deleted
                    found=1 
        except EOFError:
                fr.close()
                fw.close()
                os.remove(s)
                os.rename(Path+"temp.dat",s)
        except IOError:
            print "No Member Added"

        # Deleting the user details from ID.dat file as well, if it exists
        if found==1:
            fr=open(Path+"ID.dat","rb")
            fw=open(Path+"temp.dat","wb")
            try:
                while True:
                    a=pickle.load(fr)
                    if a.eno!=x:    # member NOT to be deleted
                        pickle.dump(a,fw)
            except EOFError:
                fr.close()
                fw.close()
                os.remove(Path+"ID.dat")
                os.rename(Path+"temp.dat",Path+"ID.dat")
            print "Record Deleted"
        else:
            print "No record found with the matching ID"
        

    # to view batchwise performance in a particular test
    def TestResult(self):
        try:
            fr=open(Path+"StudentData.dat","rb")
            serial=InputInt("Enter Test Serial of whose performance you wish to view:")
            EnteredBatch=raw_input("Enter Batch Code:")
            print "\t\tTest",serial
            print "Enroll. No  Name\t\tPhysics\tChemistry\tMaths\tAverage marks"
            print "-"*int(FormattingLength*1.4)
            while True:
                x=pickle.load(fr)
                if x.batch==EnteredBatch:
                    print x.eno,'\t',x.name,'\t',x.marks[serial-1][0],'\t',x.marks[serial-1][1],'\t',x.marks[serial-1][2],'\t',x.rpi
        except EOFError:
            fr.close()
        except IOError:
            print "No Student Added"
        except IndexError:
            print "Student has not written Test",serial,"yet"

    # to view the details of particular/all students
    def viewStuInfo(self):
        found=0
        try:
            fr=open(Path+"StudentData.dat","rb")
            choice=raw_input("Enter Enrollment Number/* to view all:")
            if choice=='*':
                print "Enrollment No\tName\t\tBatchCode\tFee Status  ContactNumber\tAddress"
                print "-"*int(FormattingLength*2)
                found=1
            while True:
                x=pickle.load(fr)
                stat="Paid" if x.fee==x.feepaid else "Unpaid"
                if choice=='*':
                    print x.eno,'\t\t', x.name,'\t',x.batch,'\t',stat,'  \t',x.contactNo,'\t',x.address
                else:
                    if x.eno==choice:
                        x.viewInfo()
                        found=1
                        fr.close()
                        return
        except EOFError:
            fr.close()
        except IOError:
            print "No Student Added"
            return
        
        if found==0:
            print "Invalid Enrollment Number Entered"
        print
        
    # to view the details of particular/all faculties
    def viewFacInfo(self):
        try:
            fr=open(Path+"FacultyData.dat","rb")
            choice=raw_input("Enter Employee Number/* to view all:")
            counter=0
            if choice=='*':
                print "Employee No\tName\t\tSubject\tContactNumber\tAddress"
                print "-"*int(FormattingLength*1.5)
            while True:
                x=pickle.load(fr)
                if choice=='*':
                    dic={"P":"Physics","C":"Chem","M":"Maths"}
                    print x.eno,'\t\t', x.name,'\t',dic[x.subject],'\t',x.contactNo,'\t',x.address
                    counter+=1
                else:# for single faculty
                    if x.eno==choice:
                        x.viewInfo()
                        counter=1
                        break
        except EOFError:
            pass
        except IOError:
            print "No Faculty Member Added"
            return
        fr.close()
        if counter==0:
            print "Invalid Employee ID Entered"



# this class provides functions to enable a FACULTY MEMBER to view and interact with the facilities available 
class Faculty:
    
    # basic constructor to initialize instance variables with null values
    def __init__(self):
        self.eno='na'       # Employee Number -- uniquely identifies every faculty member
        self.name='na'
        self.subject='na'
        self.address='na'
        self.contactNo='na'
        self.salary=0

    #function to return faculty details to login module based on employee number
    def getValues(self,eno):
        fr=open(Path+"FacultyData.dat",'rb')
        try:
            while True:
                x=pickle.load(fr)
                if eno==x.eno:
                    fr.close()
                    return x
        except EOFError:
            fr.close()
        
    # to display options available to user and accept his choice
    def hlp(self):  
        print "_"*int(FormattingLength*0.8)  # for uniform length of line
        print "You can do a lot many things!"
        print "Press 1 To View the Notices and announcements "
        print "Press 2 To Post a Notice "
        print "Press 3 To View the Timetable"
        print "Press 4 To View Batch-wise Performance of students in your subject"
        print "Press 5 To view and answer the queries submitted "
        print "Press 6 To update Student's marks"
        print "Press 7 To change your password"
        print "Press 8 To View Personal details"
        print "Press 9 To Update Personal details\n"
        return Inp("Enter your choice:",range(1,10))

    # To View Batch-wise Performance of students 
    def viewResult(self):
        try:
                fr=open(Path+"StudentData.dat",'rb')#doubtful statement- if studentdata.dat is not created ;will raise i/o error
                EnteredBatch=raw_input("Enter batch code:").upper()
                d={'P':0,'C':1,'M':2}
                subject=d[self.subject] #faculty is only able to access the marks of his own sub
                counter=0
                
                while True:
                    x=pickle.load(fr)
                    if x.batch==EnteredBatch:
                        if counter==0:
                            order=range(len(x.marks))[::-1] #will give the test serial index in reverse order
                            print "Enroll no.\tName\t\t",
                            for i in order:
                                print "Test ",i+1,'\t', #displaying the test no.
                            print "\n","-"*(FormattingLength+len(order)*10)
                            counter=1
                        print x.eno,'\t',x.name,'\t',
                        for i in order:
                            print x.marks[i][subject],'\t', #displaying the marks of student in that particular subject
                        print
        except EOFError:
            fr.close()
        except KeyError: #raised in dictionaries if we try to access an invalid key
            print "unexpected situation"
        except IOError:
            print "No Student Added"
        if counter==0:
            print "Invalid/Unexisting Batch Code Entered"

    #To view and answer the queries submitted by students
    def viewQ(self):
        foundq=0 #counter for unanswered queries of his subject
        founda=0#counter for the queries answered by him
        try:
            fr=open(Path+"Question.dat",'rb')
            fw=open(Path+"temp.dat","wb")
            while True:
                x=pickle.load(fr)
                if x[0]==self.subject and len(x)==4:#x=[sub,q,self.name,self.batch] #for unanswered query
                    foundq+=1
                    print "\n",x[1],"\nAsked by:",x[2],'of',x[3]
                    print "Do you want to answer to this query now?:"
                    ch=Inp( "Enter 'Y' for yes or 'N' to proceed to next query:",['Y','N'],True)
                    if ch=='Y':
                        ans=raw_input("Enter your answer:")
                        x.append(ans)
                        x.append(self.name)
                        print "Thank you for answering"
                        founda+=1
                pickle.dump(x,fw)
                            
        except EOFError:
            fr.close()
            fw.close()
            os.remove(Path+"Question.dat")
            os.rename(Path+"temp.dat",Path+"Question.dat")
        except IOError:
            print "No Queries raised yet!!!"
        if foundq==0:
            print "All queries were already answered"
        else:
            print founda,"Queries answered from",foundq,"Queries"
             
    #To post a notice to the bulletin board
    def postNews(self):
        fw=open(Path+"News.txt","a")
        s=raw_input("Enter the notice/news:")+'\n'
        fw.write(s)
        print "Notice Posted"
        fw.close()

    #To change marks of a student in particular subject scored in a particular test
    def updatemarks(self):
        try:
            fr=open(Path+"StudentData.dat","rb")
            fw=open(Path+"temp.dat","ab")
            bat=raw_input("Enter the batch code whose marks you want to modify ")#faculty can change ONLY his own subject marks
            testserial=InputInt("Enter the Test Serial whose marks you want to modify:")
            ch=raw_input("Enter Enrollment Number or * to Update all:")
            dic={'P':0,'C':1,'M':2}
            sub=dic[self.subject]
            c=0
            batchCorrect=False
            while True:
                x=pickle.load(fr)
                if x.batch == bat:  # if batch matches
                    batchCorrect=True
                    if len(x.marks)>=testserial:# whether students of that batch have written that test or not
                        if ch=='*':     # updating all of this batch
                            x.modify(sub,testserial)
                            c+=1
                        elif x.eno==ch:# this will match only ONCE
                            x.modify(sub,testserial)
                            c=1
                    else:   # Wrong test serial
                        c=-1
                pickle.dump(x,fw)
        except EOFError:
            fr.close()
            fw.close()
            os.remove(Path+"StudentData.dat")
            os.rename(Path+"temp.dat",Path+"StudentData.dat")
        except IOError:
            print "No Student Added"
            return
        
        if batchCorrect==False:
            print "Wrong Batch code given"
        elif c==-1:
            print "Students of",bat,"have not written Test",testserial,"yet"
        elif c==0:
            print "No student with Enrollment number",ch,"exists in",bat
        else:
            print c,"records updated"
        
     # To update Personal Details               
    def updatePersonalData(self):
        fr=open(Path+"FacultyData.dat","rb")
        fw=open(Path+"temp.dat","wb")
        try:
            while True:
                x=pickle.load(fr)
                if x.eno==self.eno:
                    self.address=raw_input("Enter Address:")
                    self.contactNo=raw_input("Enter Contact Number:")
                pickle.dump(x,fw)
        except EOFError:
            fr.close()
            fw.close()
            os.remove(Path+"FacultyData.dat")
            os.rename(Path+"temp.dat",Path+"FacultyData.dat")
        print "Details Updated"

    # To view a detailed information of faculty
    def viewInfo(self):
        print "Name:",self.name
        print "Employee Number:",self.eno
        d={"P":"Physics","C":"Chemistry","M":"Mathematics"}
        print "Subject:",d[self.subject]
        print "Address:",self.address
        print "Contact Number:",self.contactNo
          
          
            
# this class provides functions to enable a student to view and interact with the facilities available
# Objects of this class are stored In StudentData.dat
class Student:
    def __init__(self):
        self.eno='na'       # Enrollment number -- uniquely identifies every student
        self.name='na'
        self.batch='na'
        self.marks=[] #[ [P,C,M] , [P,C,M], [PCM] , ......]
        self.rpi=0
        self.address='na'
        self.contactNo='na'
        self.fee=0      # instance variable for storing fee payable
        self.scl=0      # instance variable for scholarship given
        self.feepaid=0

    
     #to allow the change marks of a particular subject scored in a particular test by faculty member   
    def modify(self,sub,serial):#sub-[0,1,2],serial-test number
        """dic={0:'P',1:'C',2:'M'}#giving index values to subjects in nested list
        subject=dic[sub]#extracting index of the subject to be modified using a key"""
        try:
            if serial>len(self.marks):
                raise IndexError
            self.marks[serial-1][sub]=InputInt("Enter marks of "+self.name+" :")
            self.rpi=calcRPI(self.marks)
        except IndexError:#test serial out of range 
            print "Student has not written Test",serial,"yet"
            
    # to display options available to user and accept his choice
    def hlp(self): 
        print "="*int(FormattingLength*1.0)
        print "You can do a lot many things!"
        print "Press 1 To View the Notices and announcements"
        print "Press 2 To View the Timetable"
        print "Press 3 To View your RPI and score"
        print "Press 4 To submit a query"
        print "Press 5 To view answers to queries submitted"    # serves like a FAQ bulletin
        print "Press 6 To change your password"
        print "Press 7 To View personal details"
        print "Press 8 To Update personal details \n"
        return Inp("Enter your choice:",range(1,9))         # taking input
    
    # function to send data & values of a particular student to login module 
    def getValues(self,en):   
        fr=open(Path+"StudentData.dat",'rb')
        try:
            while True:
                x=pickle.load(fr)   #x stores loaded object of student class
                if en == x.eno: #if parameter's id matches with current object id
                    fr.close()  #  stop there and return a copy of the same object 
                    return x
        except EOFError:
            fr.close()

     #function to assign batch to a student based on his RPI by the admin  
    def assignBatch(self): 
        if self.rpi>70:
            bgrade="A"
        elif self.rpi>50:
            bgrade="B"
        else:
            bgrade="C"
        self.batch=self.batch[0:6]+bgrade+self.batch[7:9]

    # this function calculates and modifies the fees payable and scholarship granted
    def scholarship(self):
        #finding percentage marks in admission test (test 1)(index=0)
        avg=(self.marks[0][0]+self.marks[0][1]+self.marks[0][2])*100/360
        print "Average=",avg
        if avg>85:
            sc=0.5#50%
        elif avg>70:
            sc=0.3#30%
        elif avg>60:
            sc=0.1#10%
        else:
            sc=0

        yrs=int(self.batch[5])-int(self.batch[4])#to calculate the no of years for which the student will be enrolled with the institute
        self.scl=sc*80000*yrs   #   scholarship to be given ONLY on tution fee
        self.fee=(80000+20000+10000)*yrs-self.scl

    # function to show marks scored in each test beginning from the latest(reverse order)          
    def viewResult(self):
        print "Your current Rank Performance Index is",self.rpi
        print "Your marks are as follows:"
        print "Test serial  Physics\tChemistry\tMathematics"
        print "-"*int(FormattingLength*0.5)
        for i in range(len(self.marks)-1,-1,-1):#applying reverse loop on marks list
            print i,'\t',self.marks[i][0],'\t',self.marks[i][1],'\t',self.marks[i][2]
        
    #function to enable a student to add a question to query file
    def submitQ(self):
        print "-"*int(FormattingLength*1.5)
        sub=Inp("Enter the subject (P,C,M) in which you have a query:",['P','C','M'],True)
        q=raw_input("Enter your Query:")
        fw=open(Path+"Question.dat","ab")
        pickle.dump([sub,q,self.name,self.batch],fw)
        print "Your Query has been submitted.\nCheck after some time for a response"
        fw.close()

    #function to show only the answered queries
    def viewfaq(self):
        print "-"*int(FormattingLength*1.5)
        subject={0:'P', 1:'C', 2:'M'}
        for i in range(3):
            if i==0:
                print "--------PHYSICS  QUERIES--------"
            elif i==1:
                print "-"*int(FormattingLength*1.5)
                print "--------CHEMISTRY  QUERIES--------"
            else:
                print "-"*int(FormattingLength*1.5)
                print "--------MATHEMATICS  QUERIES--------"
             
            try:
                fr=open(Path+"Question.dat","rb") #query list= [sub , query , stu.name , Stu.batch , solution , facultynam],
                while True:
                    x=pickle.load(fr)
                    if len(x)==6 and x[0]==subject[i] : #constraint for checking the answered queries subjectwise
                        print x[1],"\nAsked By: ",x[2],"of",x[3]
                        print "\nSolution:",x[4]
                        print "Answered by:",x[5],"\n"
            except EOFError:
                fr.close()
            except IOError:
                print "No queries answered yet"
        print '\n',"-"*int(FormattingLength*1.5)

    # function to modify personal details
    def updatePersonalData(self):
        print "-"*int(FormattingLength*1.5)
        fr=open(Path+"StudentData.dat","rb")
        fw=open(Path+"temp.dat","wb")
        try:
            while True:
                x=pickle.load(fr)
                if x.eno==self.eno:
                    self.address=raw_input("\nEnter Address:")
                    self.contactNo=raw_input("Enter Contact Number:")
                pickle.dump(x,fw)
        except EOFError:
            fr.close()
        fw.close()
        os.remove(Path+"StudentData.dat")
        os.rename(Path+"temp.dat",Path+"StudentData.dat")
        print "Details Updated"        

    # function to show a detailed information of student
    def viewInfo(self):
        print "-"*int(FormattingLength*1.5)
        print "Name:",self.name
        print "Enrollment Number:",self.eno
        print "Batch Code:",self.batch
        print "Year of Admission:","201"+self.batch[4]
        print "Year of Appearance in JEE:","201"+self.batch[5]
        typ={'R':"Regular (Weekday)",'W':"Weekend",'O':"Distant Learning"}
        grade={'A':"Cult A+ Batch",'B':"Fierce Batch",'C':"Commoners batch"}
        print "Batch Type:",typ[self.batch[3]],"batch"
        print "Batch Grade:",grade[self.batch[6]]
        print "Rank Performance Index:",self.rpi
        print "\nFees: Rs",(self.fee+self.scl)
        print "Scholarship recieved on basis of Admission test: Rs",self.scl
        print "Total Fees Payable: Rs",self.fee
        print "Fee Status:",
        if self.feepaid==self.fee:
            print "All dues CLEAR"
        else:
            print "Fee Due... Kindly Pay at our office"
            print "Amount Paid: Rs",self.feepaid
            print "Amount Due: Rs",(self.fee-self.feepaid)
        print "Address:",self.address
        print "Contact Number:",self.contactNo        



# This class creates, initializes both faculty and students 
class Member:
    def __init__(self):
        self.id='na'
        self.pswrd='na'
        self.type='na'
        self.eno='na'

    # function to add a member to the institute
    def add(self):  
        fr=open(Path+"ID.dat","rb")#Path-global variable storing current working directory
        IDList=[]
        EnoList=[]
        try:
            while True:
                x=pickle.load(fr)
                IDList.append(x.id)  #to create a list of already existing ids
                EnoList.append(x.eno) #to create a list of already existing enrollment number
        except EOFError: #executed when end of file is reached
            fr.close() #closes the file

        #ID CHECK
        while True:
            self.id=raw_input("Enter ID:")
            if self.id in IDList: #unique id constraint
                print "This User ID is already registered TRY AGAIN"
                continue #skips the current iteration,moves to next iteration
            #executed if id entered by the user is unique
            break 

        #taking password
        self.pswrd=inppswrd() #using global function
            
        #using global function-Inp(prompt,range,char=False)
        self.type=Inp("Enter Type(1 for Student and 2 for Faculty):",[1,2])

        #Unique E NO Generation
        if self.type==1:
            typ='S'
            tynam="Enrollment"
            s=[(str(i).zfill(4)) for i in range(1,10000)] #max no of students
        else:
            typ='F'
            tynam="Employee"
            s=[(str(i).zfill(4)) for i in range(1,500)]   #max no of faculty members

        for i in EnoList:
            try:
                if i[0]==typ:
                    s.remove(i[1:])
            except ValueError:
                pass
            
        self.eno=typ+s[0]
        print "Assigned",tynam,"Number:",self.eno

         #dumping the newly created member to a file so that he may login again using these details   
        fw=open(Path+"ID.dat",'ab')
        pickle.dump(self,fw)
        fw.close()
        
         
    # function to allow change of password and reflect the same in stored file
    def changepswrd(self):
        orig=raw_input("Enter ORIGINAL password:")
        fr=open(Path+"ID.dat","rb")
        fw=open(Path+"temp.dat","wb")
        
        try:
            while True:
                x=pickle.load(fr)
                if x.id==self.id: #matching the ids of file to that of member
                    if orig==self.pswrd:
                         x.pswrd=inppswrd()
                         print "Password Changed"
                    else:
                        print "this is not your password"
                pickle.dump(x,fw)
        except EOFError:#executed when readable file reaches the end
            fr.close()
        fw.close()
        os.remove(Path+"ID.dat")
        os.rename(Path+"temp.dat",Path+"ID.dat")
        
        
            
#class containing basic features available to any general user who visits the portal
class Homepage:
    def info(self):
        ReadAll("AboutUs.txt")

    def news(self):
        print "Notice Board".center(100)
        ReadRev("News.txt")
        
    def achievements(self):#latest achievements are added in end but must be read first 
        ReadRev("Achievements.txt")
         
    def courses(self):
       ReadAll("Courses.txt")
        
    def fee(self):
        print "Press corresponding key for the desired course"
        fr=open(Path+"Courses.txt","r")
        no=1
        for i in fr.readlines():
            print no,'\t',i,
            no+=1
        print
        #checking fee for each section
        x=Inp("Enter your choice:",range(1,7))
        if x==5:
            x=4
        if x in range(1,5):     # i<>6
            f=[80000*(5-x),20000*(5-x),10000*(5-x)]
            print "Tution Fee: Rs",f[0]
            print "Infrastructure Fee: Rs",f[1]
            print "Book Fee: Rs",f[2]
            print "Total Fees : Rs",(f[0]+f[1]+f[2])
        elif x==6:
            print "Book Fee is  Rs 20000 per annum"
            

    def contactUs(self):
        ReadAll("ContactUs.txt")
        print "Do you wish to leave us a suggestion/complaint?"
        ch=Inp("Press Y for yes or N to continue:",['Y','N'],True)
        if ch=='Y':
            s=raw_input("Enter your suggestion/complaint:")
            fw=open(Path+"Feedback.txt",'a')
            fw.write(s+'\n')
            fw.close()
            print "Thank You for your feedback! We value your opinion greatly."
        
    
h1=Homepage()
a1=Admin()
#To be executed only once,i.e., to be executed by the programmer only while designing the program becoz admin is created only once and has all round control
"""a1.id="Admin987"
a1.pswrd="superuser.123"
a1.type=0
fw=open(Path+"ID.dat",'ab')
pickle.dump(a1,fw)
fw.close()"""



# class which is executed first -- directs control based upon user choice
class Execute:
    
    # this function takes input from user
    def accept(self):
        print "="*FormattingLength
        print "\t\tWelcome to BLUEBEAM EDUCATION HUB Portal"
        print "="*FormattingLength
        print "Press 1 to know more about us"
        print "Press 2 to know about the courses offered"
        print "Press 3 to see the past achievements"
        print "Press 4 to learn about the Fee Structure"
        print "Press 5 to contact us"
        print "Press 6 to login\n"
        x= Inp("Enter your choice:",range(1,7))
        return x

    #this function directs the control to respective jobs
    def check(self,x):
        if x==1:
            h1.info()
        elif x==2:
            h1.courses()
        elif x==3:
            h1.achievements()
        elif x==4:
            h1.fee()
        elif x==5:
            h1.contactUs()
        elif x==6:
            login()
        
#global part
while True:    
    e1=Execute()
    x=e1.accept()
    e1.check(x)
    print '\n'
    ch=Inp("Continue to main menu <Y/N>:",['Y','N'],True)
    if ch !='Y':#continues ONLY if first character entered is y or Y
        print "Quitting out of program"
        break

