import os
from shell import *
sh=pyshell()
import json
import hashlib
try:
 from cryptography.fernet import Fernet
except ModuleNotFoundError :
 os.system(" pip3 install cryptography --break-system-packages ")
sh.clear()
class UYT:
  def key(self):
   if(os.path.exists("key.txt")):
    with open("key.txt","rb") as f:
     key=f.read()
    return Fernet(key)
   else:
    key=Fernet.generate_key()
    with open("key.txt","wb") as f:
     f.write(key)
    return Fernet(key)


  def encrypt(self,text):
   chiper=self.key()
   return chiper.encrypt(text.encode()).decode()

  def decrypt(self,en):
   chiper=self.key()
   return chiper.decrypt(en.encode()).decode()

  def hash(self,text):
   return hashlib.md5(text.encode()).hexdigest()

  def database(self):
   if(os.path.exists("database.json")):
    with open("database.json","r") as f:
     database=json.load(f)
    return database
   else:
    database={"admin":{
               "name":"",
               "password":""},
              "passwords":{},
              "impo_file":[]}
    return database

  def save_data(self,data):
   with open("database.json","w") as f:
    json.dump(data,f,indent=4)

  #crud password
  #c
  def save_password(self,work,password):
   database=self.database()
   if(work not in database["passwords"]):
    database["passwords"][work]={
              "password":self.encrypt(password)}
    self.save_data(database)
    print("save it sucessfuly")
   else:
    print("thsi password exists ")
  #r
  def see_password(self):
   database=self.database()
   for i,password in enumerate(database["passwords"],start=1):
    print(i,password,"==",self.decrypt(database["passwords"][password]["password"]))
  #u
  def update_password(self,work,password):
    database = self.database()
    if work in database["passwords"]:
        database["passwords"][work]["password"] = self.encrypt(password)
        self.save_data(database)
        print("save update")
    else:
        print("this name not exists")
  #d
  def delet_password(self,work):
   database=self.database()
   if(work in database["passwords"]):
    del database["passwords"][work]
    self.save_data(database)
    print("delet sucsessfuly")
   else:
    print("thsi name not exists")
  #c
  def save_file(self,name):
   database=self.database()
   ok=[]
   for i in database["impo_file"]:
    ok.append(self.decrypt(i))
   if(name not in ok):
    database["impo_file"].append(self.encrypt(name))
    self.save_data(database)
   else:
    print("this file is exists")
  #r
  def see_file(self):
   database=self.database()
   for i,files in enumerate(database["impo_file"],start=1):
    print(i,self.decrypt(files))
  #d
  def delet_file(self,name):
   database=self.database()
   d=[]
   e=[]
   for i in database["impo_file"]:
    d.append(self.decrypt(i))
   if(name  in d):
    d.remove(name)
    for i in d:
     e.append(self.encrypt(i))
    database["impo_file"]=e
    self.save_data(database)
   else:
    print("this file not exists")

  def change_admin(name,pas):
   database=self.database()
   database["admin"]["name"]=name
   database["admin"]["password"]=hash(pas)

  def see_admin(self):
   database=self.database()
   print("name:" , database["admin"]["name"])
   print("password:" , (database["admin"]["password"]))

  def admin(self):
   T_l=0
   database=self.database()
   if(database["admin"]["name"].strip() =="" or database["admin"]["password"].strip() ==""):
    name=input("set a username :")
    password=input("set a password :")
    database["admin"]["name"]=name.strip()
    database["admin"]["password"]=self.hash(password.strip())
    self.save_data(database)
    self.main()
   else:
    while True:
     name=input("enter user name : ")
     password=input("enter password : ")
     if(name ==database["admin"]["name"] and self.hash(password)==database["admin"]["password"]):
      self.main()
      break
     elif(T_l==2):
      print("3 time try")
      break
     else:
      print("wrong password", T_l+1)
      T_l+=1

  def distroy(self):
   pass
  def main(self):
    while True:
     print("1.add password")
     print("2.see password list")
     print("3.change password ")
     print("4.delet password")
     print("5.add impo file")
     print("6.see impo files")
     print("7.delet impo file ")
     print("8.see admin cradintion")
     print("9.change admin imformation")
     print("10.distroy")
     print("11.exit")
     x=input("(taltur/SSS): ")
     if(x=="11"):
      break
     elif(x=="1"):
      work=input("enter work :")
      password=input("set  password :")
      self.save_password(work,password)
     elif(x=="2"):
      self.see_password()
     elif(x=="3"):
      work=input("what work password you whant change  :")
      new_password=input("set a new password :")
      self.update_password(work,new_password)
     elif(x=="4"):
      work=input("enter work :")
      self.delet_password(work)
     elif(x=="5"):
      file=input("entet file name :")
      self.save_file(file)
     elif(x=="6"):
      self.see_file()
     elif(x=="7"):
      file=input("enter file name :")
      self.delet_file(file)
     elif(x=="8"):
      database=self.database()
      pas=input("enter admin password :")
      if(self.hash(pas)==database["admin"]["password"]):
       self.see_admin()
      else:
       print("wrong password")
     elif(x=="9"):
      database=self.database()
      password=input("enter admin  password :")
      if(self.hash(password)==database["admin"]["password"]):
       name=input("set a new name :")
       pas=input("set a new name :")
       self.change_admin(name,pas)
      else:
       print("wrong password")
     elif(x=="10"):
      self.distroy()
     else:
      sh.main(x)
if __name__=="__main__":
 om=UYT()
 #key=om.key()
 #print(key)
 #database=om.database()
 #database["admin"]["name"]="om"
 #database["admin"]["password"]="2912"
 #om.save_data(database)
 #om.save_password("oojeheeje","sehwufjfjekowk000sk")
 #om.update_password("oojeheeje","opriieehej")
 #om.see_password()
 #om.delet_password("oojeheeje")
 #om.save_file("omehjwhreheh")
 #om.see_file()
 #om.delet_file("omehjwhreheh")
 om.admin()
