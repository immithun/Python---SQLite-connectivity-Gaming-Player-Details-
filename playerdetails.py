import sys;
import sqlite3;  
import re
conn=sqlite3.connect("freefire.db")
cur=conn.cursor()


class freefire:


    def __init__(self,version,lastupdated,noofusers,gamesize,ftype):
        self.__version=version
        self.__lastupdated=lastupdated
        self.__noofusers=noofusers
        self.__gamesize=gamesize
        self.__type=ftype
    def getversion(self):
        return self.__version
       
    def getlastupdated(self):
        return self.__lastupdated


    def getnoofusers(self):
        return self.__noofusers


    def getgamesize(self):
        return self.__gamesize
   
    def gettype(self):
        return self.__type
   
    def setversion(self, value):
        self.__version = value
   


    def setlastupdated(self, value):
        self.__lastupdated = value


    def setnoofusers(self, value):
        self.__noofusers = value


    def setgamesize(self, value):
        self.__gamesize = value


    def settype(self, value):
        self.__ftype = value
       
    def checkgamesize(self):
        if(int(self.__gamesize)<2):
            return True
        else:    
            print("GAME SIZE EXCEEDED")
            return False


class player(freefire):
           
           
    def __init__(self,version,lastupdated,noofusers,gamesize,ftype,pname,pid,age,level):
        self.__pname=pname
        self.__pid=pid
        self.__age=age
        self.__level=level
        super(player, self).__init__(version,lastupdated,noofusers,gamesize,ftype)


         
    def getpname(self):
        return self.__pname


    def getpid(self):
        return self.__pid


    def getage(self):
        return self.__age


    def getlevel(self):
        return self.__level






    def setpname(self, value):
        self.__pname = value


    def setpid(self, value):
        self.__pid = value


    def setage(self, value):
        self.__age = value


    def setlevel(self, value):
        self.__level = value
       
    def checkage(self):
        if(int(self.__age)>18):
            return True
        else:    
            print("NOT ELIGIBLE")
            return False












class maintenance(freefire):
           
           
    def __init__(self,version,lastupdated,noofusers,gamesize,ftype,mid,mname,time,salary):
        self.__mid=mid
        self.__mname=mname
        self.__time=time
        self.__salary=salary
       
        super(maintenance, self).__init__(version,lastupdated,noofusers,gamesize,ftype) # calling base class constructor


         
    def getmid(self):
        return self.__mid


    def getmname(self):
        return self.__mname


    def gettime(self):
        return self.__time


    def getsalary(self):
        return self.__salary


    def setmid(self, value):
        self.__mid = value


    def setmname(self, value):
        self.__mname = value


    def settime(self, value):
        self.__time = value


    def setsalary(self, value):
        self.__salary = value


             
    def incrementsalary(self):
        if(int(self.__time)<60):
            self.__salary=self.__salary+25000
   
    def displayincrementsalary(self):
        print('Salary:',self.__salary)




class gamedetails(player):
           
           
    def __init__(self,version,lastupdated,noofusers,gamesize,ftype,pname,pid,age,level,gid,noofkills,noofdeaths,noofvictory,noofloses):
        self.__gid=gid
        self.__noofkills=noofkills
        self.__noofdeaths=noofdeaths
        self.__noofvictory=noofvictory
        self.__noofloses=noofloses
        super(gamedetails, self).__init__(version,lastupdated,noofusers,gamesize,ftype,pname,pid,age,level)


    def getgid(self):
        return self.__gid
   
    def getnoofkills(self):
        return self.__noofkills


    def getnoofdeaths(self):
        return self.__noofdeaths


    def getnoofvictory(self):
        return self.__noofvictory


    def getnoofloses(self):
        return self.__noofloses




    def setgid(self, value):
        self.__gid = value
       
    def setnoofkills(self, value):
        self.__noofkills = value


    def setnoofdeaths(self, value):
        self.__noofdeaths = value


    def setnoofloses(self, value):
        self.__age = value


    def setnoofvictory(self, value):
        self.__noofvictory = value
       
    def calculatekbydratio(self):
        print('%.2f'%(int(self.__noofkills)/int(self.__noofdeaths)))
       


           


class hello:
    n=0
    ch='n'
    def options(self):
        print("******************************")
        print("GARENA GAMING DETAILS")
        print("******************************")
        print("1. Add New details")
        print("2. View Player Details")
        print("3. View Maintenance Details")
        print("4. View freefire Details")
        print("5. Exit")
        n=int(input("Select your choice"))
        if n==1:
            self.insertrecord()
        elif n==2:
            self.viewallplayer()
        elif n==3:
            self.viewallmaintenance()
        elif n==4:
            self.viewfreefiredetails()
        elif n==5:
            print("LET'S CHILL WITH GAMING EXPERIENCE")
            sys.exit
           
   
    def insertrecord(self):
        try:


            #conn.execute('''drop table freefire;''')
            #conn.execute('''drop table player;''')
            #conn.execute('''drop table maintenance;''')
            #conn.execute('''drop table gamedetails;''')
            #conn.execute('''CREATE TABLE player (PNAME  TEXT NOT NULL,PID INT NOT NULL,AGE INT NOT NULL,LEVEL INT NOT NULL);''')


            #conn.execute('''CREATE TABLE maintenance (MID INT NOT NULL,MNAME  TEXT NOT NULL,TIME INT NOT NULL,SALARY INT NOT NULL);''')
           


            #conn.execute('''CREATE TABLE freefire (VERSION INT NOT NULL,LASTUPDATED TEXT NOT NULL,NOOFUSERS INT NOT NULL,GAMESIZE INT NOT NULL,TYPE TEXT NOT NULL);''')


            #conn.execute('''CREATE TABLE gamedetails (GID INT NOT NULL,NOOFKILLS INT NOT NULL,NOOFDEATHS INT NOT NULL,NOOFVICTORY INT NOT NULL, NOOFLOSES INT NOT NULL);''')
           
            version=input("Enter version")
            lastupdated = input("Enter  lastupdated")
            noofusers=input("Enter noofusers")
            gamesize=input("Enter gamesize")
            ftype=input("Enter type (player/maintenance)")
            obj=freefire(version,lastupdated,noofusers,gamesize,ftype)
           
            conn.execute("""insert into freefire(version,lastupdated,noofusers,gamesize,type)
                    values (?,?,?,?,?)""",(obj.getversion(),obj.getlastupdated(),obj.getnoofusers(),obj.getgamesize(),obj.gettype()))
           
            #to check gamesize
            if(obj.checkgamesize()):
                print("GAME SIZE NOT EXCEEDED")
            else:
                print("GAME SIZE EXCEEDED")
                hello.options(self)
           
            if(obj.gettype() =="player"):
               
                pname=input("Enter name")
                pid=input("Enter pid")
                age=int(input("Enter age"))
                level=int(input("Enter level"))
                pobj=player(version,lastupdated,noofusers,gamesize,ftype,pname,pid,age,level)
               
                conn.execute("insert into player(pname,pid,age,level) values(?,?,?,?)",(pobj.getpname(),pobj.getpid(),pobj.getage(),pobj.getlevel()))
               
                if(pobj.checkage()):
                    print("ELIGIBLE")
                   
                    gid = input("Enter gameid")
                    noofkills = input("Enter noofkills")
                    noofdeaths = input("Enter noofdeaths")
                    noofvictory = input("Enter noofvictory")
                    noofloses = input("Enter noofloses")
                    gobj = gamedetails(version,lastupdated,noofusers,gamesize,ftype,pname,pid,age,level,gid,noofkills,noofdeaths,noofvictory,noofloses)
                   
                    conn.execute("""insert into gamedetails(gid,noofkills,noofdeaths,noofvictory,noofloses)
                    values (?,?,?,?,?)""",(gobj.getgid(),gobj.getnoofkills(),gobj.getnoofdeaths(),gobj.getnoofvictory(),gobj.getnoofloses()))
                   
                else:
                    print("NOT ELIGIBLE")
                    hello.options(self)


                choice = input("Do you want game details of player(y/n)")
                if(choice=='y'):
                    g = int(input("Enter game id"))
                    cur.execute("select * from gamedetails where gid=?",(g,))
                    for n in cur.fetchall():
                        print(n)
                    gobj.calculatekbydratio()
            elif(obj.gettype()=="maintenance"):
                    mid=input("Enter mid ")
                    mname=input("Enter mname")
                    time=(input("Enter time"))
                    salary=int(input("Enter salary"))
                   
                    mobj=maintenance(version,lastupdated,noofusers,gamesize,ftype,mid,mname,time,salary)
                   
                   
                   
                    conn.execute("""insert into maintenance(mid,mname,time,salary)
                    values (?,?,?,?)""",(mobj.getmid(),mobj.getmname(),mobj.gettime(),mobj.getsalary()))
                   
                    mobj.incrementsalary()
                    mobj.displayincrementsalary()
                    oobj.gooptions()
        except sqlite3.DatabaseError as e:
            print("Error details: ",e)
        finally:
            conn.commit()
                   
           


    def viewallplayer(self):
        cur.execute("select * from player")
        for n in cur.fetchall():
            print(n)
        oobj.gooptions()


    def viewallmaintenance(self):
        cur.execute("select * from maintenance")
        for n in cur.fetchall():
            print(n)
        oobj.gooptions()
           
    def viewfreefiredetails(self):
        cur.execute("select * from freefire")
        for n in cur.fetchall():
            print(n)
   
       
    def gooptions(self):
        ch=input("Do you wish to continue(y/n)")
        if(ch=='y' or ch=='Y'):
            hello.options(self)
       


           
oobj=hello()
oobj.options()
oobj.gooptions()
