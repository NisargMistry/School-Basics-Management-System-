import mysql.connector as a
con=a.connect(host="localhost",user="root",passwd='1234',database="school")
c=con.cursor()
              
def ast():
    n=input("Student Name:")
    c=input("Class Name:")
    r=input("Roll No:")
    a=input("Address:")
    p=input("Phone:")
    data=(n,c,r,a,p)
    sql='insert into student values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">---------------------------------------------------------------------------------------------------------------------------------------<")
    main()

def rst():
    c=input("Class Name:")
    r=input("Roll No:")
    data=(c,r)
    sql='delete from student where CLASS=%s and ROLL_No=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Update")
    print(">------------------------------------------------------------------------------------------------------------------------------------<")
    main()


def update_s():
    x=input("Name of student:")
    c=input("Old class number:")
    s=input("Roll No:")
    r=input("Enter updated class number")
    sql='update student set Class=%s where Class=%s'
    data=(r,c)
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Update successfully")
    print(">---------------------------------------------------------------------------------------------------------------------------------------<")
    main()

def addt():
    n=input("Teacher:")
    p=input("Post:")
    s=input("Salary:")
    a=input("Address:")
    ph=input("Phone:")
    ac=input("Account:")
    data=(n,p,s,a,ph,ac)
    sql='insert into teacher values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">-------------------------------------------------------------------------------------------------------------------------------------<")
    main()
    
def update_t():
    x=input("Enter the phone number which details you want to update:")
    c=input(" New Post:")
    u=input("enter updated post")
    sql='update teacher set post=%s  where post=%s'
    data=(u,c)
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Searched successfully")
    print(">---------------------------------------------------------------------------------------------------------------------------------------<")
    main()
 


def remt():
    n=input("Teacher Name:")
    ac=input("Account No:")
    data=(n,ac)
    sql='delete from teacher where name=%s and Ac_no=%s'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Updated")
    print(">-------------------------------------------------------------------------------------------------------------------------------------<")
    main()


def abclass():
    d=input("Date:")
    cl=input("Class:")
    ab=input("Names of Absent Students:")
    data=(d,cl,ab)
    sql="insert into cattendence values(%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    data="select * from cattendence"
    c.execute(data)
    d=c.fetchall()
    for i in d:
        print(i)
    
    con.commit()
    print("Data Updated")
    print(">-------------------------------------------------------------------------------------------------------------------------------------<")
    main()

def abteacher():
    d=input("Data:")
    ab=input("Names of Absent Teacher:")
    data=(d,ab)
    sql="insert into tattendence values(%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    data="select * from tattendence"
    c.execute(data)
    d=c.fetchall()
    for i in d:
        print(i)
    con.commit()
    print("Data Updated")
    print(">-------------------------------------------------------------------------------------------------------------------------------------<")
    main()

def submitf():
    n=input("Name:")
    m=input("Class:")
    p=input("Roll_no:")
    h=input("Up to how many month fees is paid:")
    e=input("How much amount is paid?:")
    i=input("Date of payement:")
    sql='insert into fees values(%s,%s,%s,%s,%s,%s)'
    data=(n,m,p,h,e,i)
    c=con.cursor()
    c.execute(sql,data)
    data="select * from fees"
    c.execute(data)
    d=c.fetchall()
    for i in d:
        print(i)
    con.commit()
    print("Data Entered Successfully")
    print(">-------------------------------------------------------------------------------------------------------------------------------------<")
    main()
    

def pays():
    n=input("Teacher Name:")
    m=input("Month:")
    p=input("Yes/No:")
    data=(n,m,p)
    sql='insert into salary values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    data="select * from salary"
    c.execute(data)
    d=c.fetchall()
    for i in d:
        print(i)
    con.commit()
    print("Data Entered Successfully")
    print(">-------------------------------------------------------------------------------------------------------------------------------------<")
    main()

def dclass():
    sql="Select*from student"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print("NAME:",i[0])
        print("CLASS:",i[1])
        print("ROLL NO:",i[2])
        print("ADDRESS:",i[3])
        print("PHONE:",i[4])
        print(">--------------------------------<")
    print(">------------------------------------------------------------------------------------------------------------------------------------<")
    main()

def dteacher():
    sql="select*from teacher"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print("NAME:",i[0])
        print("POST:",i[1])
        print("SALARY",i[2])
        print("ADDRESS:",i[3])
        print("PHONE:",i[4])
        print("ACNO:",i[5])
        print(">--------------------------------<")
    print(">------------------------------------------------------------------------------------------------------------------------------------<")
    main()

def search(Roll_No):
    c.execute("select*from student where Roll_No={}".format(Roll_No))
    data=c.fetchall()
    count=c.rowcount

    if count==1:
        flag=1
        for row in data:
            for i in row:
                print(i,end='  ',sep=" \t ")
    else:
        flag=0
        print("Not found")
    return flag
    main()

def search_t(Phone):
    c.execute("select*from teacher where Phone={}".format(Phone))
    data=c.fetchall()
    count=c.rowcount

    if count==1:
        flag=1
        for row in data:
            for i in row:
                print(i,end='  ',sep=" \t ")
    else:
        flag=0
        print("Not found")
    return flag
    main()


    

def main():
    print("""                                   CHANDERBALA MODI ACADEMY
                               1.STUDENT
                               2.TEACHER
                               3.ADMIN
""")
    choice=input("Enter Task No:")
    print(">----------------------<")
    if(choice=='1'):
        
        print("STUDENT")
        print("1.New admission:")
        print("2.Attendence:")
        print("3.Remove Student")
        print("4.Search")
        print("5.Display")
        print("6.Update")
        print("7.back")
        ch=int(input("Enter your choice"))
        if ch==1:
            ast()
        elif ch==2:
            abclass()
        elif ch==3:
            rst()
        elif ch==4:
            searrno=int(input("Enter the roll no which you want to search:"))
            search(searrno)
        elif ch==5:
           dclass()
        elif ch==6:
            update_s()
        elif ch==7:
            main()
        else:
            print("Choice is incorrect")
            
    elif(choice=='2'):

        print("TEACHER")
        print("1.Entry for new Teacher:")
        print("2.Teacher Attendence:")
        print("3.Remove Teacher")
        print("4.Search Information")
        print("5.Display Information")
        print("6.Update")
        print("7:back")
        ch=int(input("Enter your choice"))
        if ch==1:
            addt()
        elif ch==2:
            abteacher()
        elif ch==3:
            remt()
        elif ch==4:
            searrno_1=int(input("Enter the Phone number which you want to search:"))
            search_t(searrno_1)
        elif ch==5:
           dteacher()
        elif ch==6:
            update_t()
        elif ch==7:
            main()
        else:
            print("Choice is incorrect")
                

    elif(choice=='3'):

         print("ADMIN")
         print("1.Salary Slip:")
         print("2.Fees:")
         print("3.back")
         ch=int(input("Enter your choice"))
         if ch==1:
             pays()
         elif ch==2:
             submitf()
         elif ch==3:
             main()
         else:
             print("choice is incorrect")
    else:
        print("Wrong choice OP")
        main()
def pswd():
    p=input("Password:")
    if p=='NSOP':
        main()
    else:
        print("Password is incorrect. Please enter it again")
        pswd()
pswd()