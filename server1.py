import socket
import sqlite3
conn=sqlite3.connect("cet.db")
c=conn.cursor()
s=socket.socket()
host=str(socket.gethostbyname(socket.gethostname()))
port=1112
s.bind((host,port))
s.listen(3)
clt,adr=s.accept()
conn=sqlite3.connect("cet.db")
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS student(first_name text NOT NULL,middle_name text NOT NULL,last_name text NOT NULL,mother_name text NOT NULL,highest_qualification text NOT NULL,dob text NOT NULL,email text,mob_no text NOT NULL,username text NOT NULL,password text NOT NULL)")
def login(usernam,passwor):
    #c.execute("SELECT OID FROM student WHERE username=? AND password=?",(usernam,passwor,))
    #row=c.fetchone()
    #print(row)
    c.execute("SELECT first_name FROM student WHERE username=? AND password=?",(usernam,passwor,))
    first_name=str(c.fetchone())
    first_name=first_name[2:(len(first_name)-3)]
    
    c.execute("SELECT middle_name FROM student WHERE username=? AND password=?",(usernam,passwor,))
    middle_name=str(c.fetchone())
    middle_name=middle_name[2:(len(middle_name)-3)]
    
    c.execute("SELECT last_name FROM student WHERE username=? AND password=?",(usernam,passwor,))
    last_name=str(c.fetchone())
    last_name=last_name[2:(len(last_name)-3)]
    
    c.execute("SELECT mother_name FROM student WHERE username=? AND password=?",(usernam,passwor,))
    mother_name=str(c.fetchone())
    mother_name=mother_name[2:(len(mother_name)-3)]
    
    c.execute("SELECT highest_qualification FROM student WHERE username=? AND password=?",(usernam,passwor,))
    highest_qualification=str(c.fetchone())
    highest_qualification=highest_qualification[2:(len(highest_qualification)-3)]
    
    c.execute("SELECT dob FROM student WHERE username=? AND password=?",(usernam,passwor,))
    dob=str(c.fetchone())
    dob=dob[2:(len(dob)-3)]
    
    c.execute("SELECT email FROM student WHERE username=? AND password=?",(usernam,passwor,))
    email=str(c.fetchone())
    email=email[2:(len(email)-3)]
    
    c.execute("SELECT mob_no FROM student WHERE username=? AND password=?",(usernam,passwor,))
    mob_no=str(c.fetchone())
    mob_no=mob_no[2:(len(mob_no)-3)]
    
    string=first_name+","+middle_name+","+last_name+","+mother_name+","+highest_qualification+","+dob+","+email+","+mob_no
    
    clt.send(bytes(string,"utf-8"))
    return
def register(first_name,middle_name,last_name,mother_name,highest_qualification,dob,email,mob_no,username,password):
    c.execute("INSERT INTO student VALUES(:first_name,:middle_name,:last_name,:mother_name,:highest_qualification,:dob,:email,:mob_no,:username,:password)",

                    {
                        "first_name":first_name,
                        "middle_name":middle_name,
                        "last_name":last_name,
                        "mother_name":mother_name,
                        "highest_qualification":highest_qualification,
                        "dob":dob,
                        "email":email,
                        "mob_no":mob_no,
                        "username":username,
                        "password":password,
                        }

                  )
    conn.commit()
    
    return
def fuser(mob_n,dob):
	query="SELECT username FROM student WHERE mob_no=? AND dob=?"
	c.execute(query,(mob_n,dob,))
	clt.send(bytes(str(c.fetchone()),"utf-8"))
	conn.commit()
	return
def fpass(us,pa,dob):
    query="UPDATE student SET password=? WHERE username=? AND dob=?"
    c.execute(query,(pa,us,dob,))
    conn.commit()
    
    return

def main():
    while True:
        code=clt.recv(1024).decode("utf-8").split(",") #receiver
        if code[0]=='1':
        	if len(code[0])<12 and len(code[1])<12:
        		login(code[1],code[2])
        		continue
        	clt.send(bytes("login error","utf-8"))
        if code[0]=='2':
            register(code[1],code[2],code[3],code[4],code[5],code[6],code[7],code[8],code[9],code[10])
            
        if code[0]=='3':
             print("firstname   middlename   lastname   mothername   qualification  dob email mobno   username password")
             conn=sqlite3.connect("cet.db")
             c=conn.cursor()
             c.execute("select * from student")
             m=c.fetchall()
             print(m)
             
        if code[0]=='4':
            fuser(code[1],code[2])
            
        if code[0]=='5':
            fpass(code[1],code[2],code[3])
            
            
            
    return
main()
#first_name
#middle_name
#last_name
#mother_name
#highest_qualification
#email
#mob_no
#username
#password
