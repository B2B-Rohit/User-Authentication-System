import socket
from tkinter import *
root=Tk()
s=socket.socket()
host=str(socket.gethostbyname(socket.gethostname()))
port=1112
s.connect((host,port))
#print(s.recv(1024).decode("utf-8"))
class enc:
	dict1={}
	dict2={}
	def producedict(self):
		x='abcdefghijklmnopqrstuvwxyz'
		z=0
		for i in x:
		    enc.dict1[i]=z
		    enc.dict2[z]=i
		    z+=1
	def encrypt(self,x,n):
		y=''
		for i in x:
		    if i in "abcdefghijklmnopqrstuvwxyz":
			    m=enc.dict1[i]
			    m=m+n
			    m=m%26
			    y+=enc.dict2[m]
		    else:
		    	   y+=i
		return y
	def decrypt(self,x,n):
		y=''
		for i in x:
		    if i in "abcdefghijklmnopqrstuvwxyz":
			    m=enc.dict1[i]
			    m=m-n
			    m=m%26
			    y+=enc.dict2[m]
		    else:
		    	y+=i
		return y
ob=enc()
ob.producedict()
def login():
	string='1'+','+username.get()+','+password.get()
	string=ob.encrypt(string,3) #encrypt
	s.send(bytes(string,"utf-8"))
	string=s.recv(1024).decode("utf-8")
	if string=="login error":
		print("don't try to do sql injection")
		return
	log=Tk()
	#first name
	first=Label(log,text="first name").grid(row=0,column=0)
	first=Entry(log,)
	first.grid(row=0,column=1)
	#middle name
	middle=Label(log,text="middle name").grid(row=2,column=0)
	middle=Entry(log,)
	middle.grid(row=2,column=1)
	#last name
	last=Label(log,text="last name").grid(row=3,column=0)
	last=Entry(log,)
	last.grid(row=3,column=1)
	#mother name
	mother=Label(log,text="mother name").grid(row=4,column=0)
	mother=Entry(log,)
	mother.grid(row=4,column=1)
	#qualification
	highest=Label(log,text="highest_qualification").grid(row=5,column=0)
	highest=Entry(log,)
	highest.grid(row=5,column=1)
	#dob
	do=Label(log,text="dob").grid(row=6,column=0)
	do=Entry(log,)
	do.grid(row=6,column=1)
	#email
	mail=Label(log,text="email ").grid(row=7,column=0)
	mail=Entry(log,)
	mail.grid(row=7,column=1)
	#phone no
	phone=Label(log,text="mob no").grid(row=8,column=0)
	phone=Entry(log,)
	phone.grid(row=8,column=1)
	
	
	string=ob.decrypt(string,3).split(",") #decrypt
	
	#assigning values
	first_name=string[0]
	middle_name=string[1]
	last_name=string[2]
	mother_name=string[3]
	highest_qualification=string[4]
	dob=string[5]
	email=string[6]
	mob_no=string[7]
	
	#insert in tabs
	first.insert(0,first_name)
	middle.insert(0,middle_name)
	last.insert(0,last_name)
	mother.insert(0,mother_name)
	highest.insert(0,highest_qualification)
	do.insert(0,dob)
	mail.insert(0,email)
	phone.insert(0,mob_no)
	
	def update():
            return
	update=Button(log,text="update",command=update)
	update.grid(row=9,column=1)
	return
def register():
    reg=Tk()
    #submit form
    def submit():
    	string='2'+","+first_name.get()+","+middle_name.get()+","+last_name.get()+","+mother_name.get()+","+highest_qualification.get()+","+dob.get()+","+email.get()+","+mob_no.get()+","+username.get()+","+password.get()
    	string=ob.encrypt(string,3) #encrypt
    	s.send(bytes(string,"utf-8"))
    	first_name.delete(0,END)
    	middle_name.delete(0,END)
    	last_name.delete(0,END)
    	mother_name.delete(0,END)
    	highest_qualification.delete(0,END)
    	dob.delete(0,END)
    	email.delete(0,END)
    	mob_no.delete(0,END)
    	username.delete(0,END)
    	password.delete(0,END)
    	return
    #clear entry key
    def clear():
        first_name.delete(0,END)
        middle_name.delete(0,END)
        last_name.delete(0,END)
        mother_name.delete(0,END)
        highest_qualification.delete(0,END)
        dob.delete(0,END)
        email.delete(0,END)
        mob_no.delete(0,END)
        username.delete(0,END)
        password.delete(0,END)
        return
    #label of registration entry key
    first_name=Label(reg,text="first name").grid(row=0,column=0)
    middle_name=Label(reg,text="middle name").grid(row=1,column=0)
    last_name=Label(reg,text="last name").grid(row=2,column=0)
    mother_name=Label(reg,text="mother name").grid(row=3,column=0)
    highest_qualification=Label(reg,text="highest qualification").grid(row=4,column=0)
    dob=Label(reg,text="date of birth").grid(row=5,column=0)
    email=Label(reg,text="email id").grid(row=6,column=0)
    mob_no=Label(reg,text="mob no").grid(row=7,column=0)
    username=Label(reg,text="username").grid(row=8,column=0)
    password=Label(reg,text="password").grid(row=9,column=0)
    #entry point in registration
    first_name=Entry(reg,)
    middle_name=Entry(reg,)
    last_name=Entry(reg,)
    mother_name=Entry(reg,)
    highest_qualification=Entry(reg,)
    dob=Entry(reg,)
    email=Entry(reg,)
    mob_no=Entry(reg,)
    username=Entry(reg,)
    password=Entry(reg, show='*')
    #grid of entry
    first_name.grid(row=0,column=1)
    middle_name.grid(row=1,column=1)
    last_name.grid(row=2,column=1)
    mother_name.grid(row=3,column=1)
    highest_qualification.grid(row=4,column=1)
    dob.grid(row=5,column=1)
    email.grid(row=6,column=1)
    mob_no.grid(row=7,column=1)
    username.grid(row=8,column=1)
    password.grid(row=9,column=1)
    #submit and clear bottons
    submit=Button(reg,text="submit",command=submit)
    submit.grid(row=10,column=1)
    clear=Button(reg,text="clear",command=clear)
    clear.grid(row=11,column=1)
    
    return
    return
    return
def forgetuser():
    use=Tk()
    mob=Label(use,text="mob no").grid(row=0,column=0)
    moname=Label(use,text="dob").grid(row=1,column=0)
    mo=Entry(use,)
    mo.grid(row=0,column=1)
    mname=Entry(use,)
    mname.grid(row=1,column=1)
    def user():
    	#print("inuser")
    	string="4"+","+mo.get()+","+mname.get()
    	string=ob.encrypt(string,3) #encrypt
    	s.send(bytes(string,"utf-8"))
    	op=s.recv(1024).decode("utf-8")
    	print(ob.decrypt(op,3))
    	return
    but=Button(use,text="show user",command=user).grid(row=3,column=1)
    
    return
def forgetpass():
    pas=Tk()
    user=Label(pas,text="username").grid(row=0,column=0)
    a=Entry(pas,)
    a.grid(row=0,column=1)
    def passw():
    	use=Label(pas,text="new password").grid(row=2,column=0)
    	us=Label(pas,text="dob").grid(row=3,column=0)
    	c=Entry(pas,)
    	b=Entry(pas,show='*')
    	b.grid(row=2,column=1)
    	c.grid(row=3,column=1)
    	def chpass():
    		string="5"+","+a.get()+","+b.get()+","+c.get()
    		string=ob.encrypt(string,3) #encrypt
    		s.send(bytes(string,"utf-8"))
    		return
    	bu=Button(pas,text="update password",command=chpass).grid(row=4,column=1)
    	return
    bt=Button(pas,text="next",command=passw).grid(row=1,column=1)
def show():
    s.send(bytes("3,","utf-8"))
    
    
def main():
 user=Label(root,text="username").grid(row=0,column=0)
passw=Label(root,text="password").grid(row=1,column=0)
username=Entry(root,)
password=Entry(root, show='*')
username.grid(row=0,column=1)
password.grid(row=1,column=1)
login=Button(root,text="Login",command=login).grid(row=2,column=1)
register=Button(root,text="Register",command=register).grid(row=2,column=2)
forgetuser=Button(root,text="forget username",command=forgetuser).grid(row=12,column=1)
forgetpass=Button(root,text="forget password",command=forgetpass).grid(row=13,column=1)
show=Button(root,text="show",command=show).grid(row=14,column=1) 
main()
root.mainloop()
