import mysql.connector
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


connection=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tiger",
    database="system13")


def museum():
    m=Tk()
    m.configure(background="white")
    m.title("DMRC Metro Museum")
    m.geometry("699x570")
    a=Label(m,text="METRO MUSEUM",fg="red",bg="white",font=("courier new",26,"bold")).place(x=220,y=20)
    b=Label(m,text="Timings:-",bg="white",fg="maroon",font=("courier new",20,"bold")).place(x=275,y=65)
    c=Label(m,text="9:15AM-4:45PM (all days except Monday and Holidays)",fg="salmon3",bg="white",font=("courier new",16,"bold")).place(x=25,y=105)
    d=Label(m,text="Souvenier Shop:-",fg="maroon",bg="white",font=("courier new",20,"bold")).place(x=250,y=145)
    e=Label(m,text="9:15AM-4:45PM (all days except Monday and Holidays)\nPh:91-11-2417910-12\nExtn:12362\nAdmission By\nBy Smart Cards/tokens(only valid for 45 min)\n Entry Fee: Rs.10",bg="white",font=("courier new",16)).place(x=25,y=185)
    f=Label(m,text="Interesting Facts About Metro Museum",fg="maroon",bg="white",font=("courier new",20,"bold")).place(x=90,y=345)
    g=Label(m,text="1.Metro Museum at Patel Chowk is the only museum ",bg="white",font=("courier new",16)).place(x=20,y=375)
    h=Label(m,text="about Metro Railway in the entire South Asian region.",bg="white",font=("courier new",16)).place(x=20,y=400)
    i=Label(m,text="2.It is possibly the only museum in the world in an ",bg="white",font=("courier new",16)).place(x=20,y=425)
    j=Label(m,text="operational Metro station.",bg="white",font=("courier new",16)).place(x=25,y=450)
    k=Label(m,text="3.The Museum has working models of trains, tunnel",bg="white",font=("courier new",16)).place(x=20,y=475)
    l=Label(m,text="boring machines along with a giant LED Screen that",bg="white",font=("courier new",16)).place(x=25,y=500)
    m1=Label(m,text="shows informative films on the Delhi Metro.",bg="white",font=("courier new",16)).place(x=25,y=525)
    m.mainloop()

def lost():
    m=Tk()
    m.configure(background="white")
    m.title("DMRC Lost and Found")
    m.geometry("720x540")
    a=Label(m,text="LOST AND FOUND",fg="red",bg="white",font=("courier new",24,"bold")).place(x=230,y=20)
    b=Label(m,text="\"Lost and Found office\" is setup at Kashmere Gate Metro\n Station, at the below address, for proper storage of \nLost & Found articles, disposal and keeping records.",bg="white",font=("courier new",16,"bold")).place(x=0,y=65)
    c=Label(m,text="KASHMERE GATE STATION ADDRESS",fg="salmon3",bg="white",font=("courier new",16,"bold")).place(x=175,y=150)
    d=Label(m,text="Kashmere Gate Metro Station",bg="white",font=("courier new",16,"bold")).place(x=185,y=175)
    e=Label(m,text="Ph: 011-23860837",bg="white",font=("courier new",16,"bold")).place(x=255,y=200)
    f=Label(m,text="This office works from 10AM to 5PM. It will be closed",bg="white",font=("courier new",16)).place(x=0,y=250)
    g=Label(m,text="on Sunday.",bg="white",font=("courier new",16)).place(x=0,y=275)
    h=Label(m,text="The passengers who lost their articles anywhere in",bg="white",font=("courier new",16)).place(x=0,y=300)
    i=Label(m,text="Delhi Metro premises or trains, should approach cutomer care",bg="white",font=("courier new",16)).place(x=0,y=325)
    j=Label(m,text="of the given station within 48hrs.",bg="white",font=("courier new",16)).place(x=0,y=350)
    k=Label(m,text="If the lost articles are not claimed within one month,",bg="white",font=("courier new",16)).place(x=00,y=375)
    l=Label(m,text="deposited lost article at lost and found office will",bg="white",font=("courier new",16)).place(x=00,y=400)
    n=Label(m,text="be desposed off.",bg="white",font=("courier new",16)).place(x=00,y=425)
    m.mainloop()


def others():
    m=Tk()
    m.configure(background="white")
    m.title("DMRC Other Information")
    m.geometry("680x540")
    a=Label(m,text="            DMRC Helpline",fg="red",bg="white",font=("courier new",24,"bold")).place(x=0,y=20)
    b=Label(m,text="    For any Complaints/queries\n    /suggestion, contact DMRC(24hrs)\n  Helpline Number :155370\n  Email :helpline@dmrc.org",bg="white",font=("courier new",16,"bold")).place(x=85,y=65)
    c=Label(m,text="Railway Stations",bg="white",fg="maroon",font=("courier new",18,"bold")).place(x=250,y=170)
    d=Label(m,text="     Raliways Station          Metro Station ",fg="salmon3",bg="white",font=("courier new",16,"bold")).place(x=50,y=200)
    e=Label(m,text="1.New Delhi Railway Sation       New Delhi ",bg="white",font=("courier new",16)).place(x=55,y=250)
    f=Label(m,text="2.Old Delhi Railway Sation     Chandni Chowk ",bg="white",font=("courier new",16)).place(x=55,y=275)
    g=Label(m,text="3.Shahdara Railway Sation        Shahdara ",bg="white",font=("courier new",16)).place(x=55,y=300)
    h=Label(m,text="4.Anand Vihar Railway Sation    Anand Vihar ",bg="white",font=("courier new",16)).place(x=55,y=325)
    i=Label(m,text="Facilities for Differently Abled Commuter",fg="maroon",bg="white",font=("courier new",18,"bold")).place(x=55,y=375)
    j=Label(m,text="1. Wheel Chair for Commuters ",bg="white",font=("courier new",16)).place(x=55,y=405)
    k=Label(m,text="2. Facilities for Vissually Impaired Commuters ",bg="white",font=("courier new",16)).place(x=55,y=430)
    l=Label(m,text="3. Facilities for Hearing  Impaired  Commuters ",bg="white",font=("courier new",16)).place(x=55,y=455)
    m.mainloop()                                                     

    
def menu():
    xmenu=135
    ymenu=400
    route.place(x=xmenu,y=ymenu)
    mueseum.place(x=xmenu+225,y=ymenu)
    OInfo.place(x=xmenu,y=ymenu+75)
    TGuide.place(x=xmenu,y=ymenu+150)
    LnF.place(x=xmenu+225,y=ymenu+150)
    l2.place(x=124,y=105)

    route_invisible()
    


def creation():
    
    if (start ==""):
        messagebox.showinfo("Information","Pl select starting station " )
        return()
    if (end ==""):
        messagebox.showinfo("Information","Pl select end station " )
        return()
    cursor1=connection.cursor()
    
    ## for choosing line of start station
    cursor1.execute("select * from all_line where sname='"+start+"' ;")
    k1=cursor1.fetchone()
    line1=k1[2]
    
    ## for choosing line of end station
    cursor1.execute("select * from all_line where sname='"+end+"' ;")
    k2=cursor1.fetchone()
    line2=k2[2]

    ## for checking number of interchange stations
    cursor1.execute("select * from interchange2 where line1='"+line1+"' and line2='"+line2+"';")
    kc=cursor1.fetchone()

    if kc[1]==None:           ## number of interchange  -> single/double/triple line 
        via=kc[4]
        if via!=None:         ## Double Interchange or three lines travel
            ## station name of first intechange station
            cursor1.execute("select  * from interchange2 where line1='"+line1+"' and line2='"+via+"';")
            cl1=cursor1.fetchone()
            st=cl1[1]

            ## station name of second intechange station
            cursor1.execute("select  * from interchange2 where line1='"+line2+"' and line2='"+via+"';")
            cl2=cursor1.fetchone()  
            en=cl2[1]

            ## calculation of number of station in intermediate line
            cursor1.execute("select Nxt_Id from "+via+" where sname='"+st+"';")
            kc1=cursor1.fetchall()  
            cursor1.execute("select Nxt_Id from "+via+" where sname='"+en+"';")
            kc2=cursor1.fetchall()
            c=math.fabs(kc1[0][0]- kc2[0][0])      # number of stations in intermediate line
  
            stname2=""
            bs2change=False

            ist = kc1[0][0]
            ien = kc2[0][0]
            ## for displaying station in intermediate line by their direction
            if (ist >= ien) :
                cursor1.execute("select sname from "+via+" where Nxt_Id >= "+str(ien) +" and  Nxt_Id <"+str(ist+1) +";")
                bs2change=True
                stname2= cursor1.fetchall()    
            else:
                cursor1.execute("select sname from "+kc[4]+" where Nxt_Id >= "+ str(ist) +" and Nxt_Id < "+ str(ien+1) +";")
                stname2= cursor1.fetchall()
                bs2change=False

            ## calculation of number of station in first line           
            cursor1.execute("select Nxt_Id from "+line1+" where sname= '"+start+"';") 
            k_i1=cursor1.fetchone()  
            cursor1.execute("select Nxt_Id from "+line1+" where sname= '"+st+"';")
            k_i2=cursor1.fetchone()
            a=math.fabs(k_i1[0]-k_i2[0])  # number of stations in first line
          
             
            stname1=""
            bs1change=False
            
            j1=int(k_i1[0])
            j2 =int(k_i2[0])

            ## for displaying station in first line by their direction
            if ( j1 >= j2 ) :
                cursor1.execute("select sname from "+line1+" where Nxt_Id >= "+str(j2)+" and Nxt_Id < "+str(j1+1)+";")
                stname1= cursor1.fetchall()
                bs1change=False
               
            else:
                cursor1.execute("select sname from "+line1+" where Nxt_Id >= "+str(j1)+" and Nxt_Id < "+str(j2+1)+";")
                stname1= cursor1.fetchall()
                bs1change=True

            
            ## calculation of number of station in second line  
            cursor1.execute("select Nxt_Id from "+line2+" where sname= '"+end+"';")
            k_i3=cursor1.fetchone()
            cursor1.execute("select Nxt_Id from "+line2+" where sname= '"+en+"';")
            k_i4=cursor1.fetchone()
            b=math.fabs(k_i3[0]-k_i4[0])

            ## Total Number of Stations
            total=a+b+c
            ic=2
            
            stname3=""
            bs3change=False
            
            jj1=k_i3[0]
            jj2=k_i4[0]
            
            ## for displaying station in second line by their direction
            if ( jj1 >= jj2) :
                cursor1.execute("select sname from "+line2+" where Nxt_Id >= "+str(jj2)+" and Nxt_Id < "+str(jj1+1)+";")
                stname3= cursor1.fetchall()
                bs3change=False
                                        
            else:
                cursor1.execute("select sname from "+line2+" where Nxt_Id >= "+str(jj1)+" and Nxt_Id < "+ str(jj2+1)+";")
                stname3= cursor1.fetchall()
                bs3change=True

            ## display of details 
            dis=""
            if bs1change == True :
                il=len(stname1)
                for i in range(il):
                    
                    dis= dis+  stname1[i][0] + "->"
                    if ((i+1)%5 ==0):
                        dis= dis + " \n "
                    
            else:
                
                il=len(stname1)
                for i in range(il):   
                    
                    dis= dis+  stname1[il-1 -i][0] + "->"
                    if ((i+1)%5 ==0):
                        dis= dis + " \n "

            dis= dis + " \n "
            
            if (bs2change==True) :
                
                il=len(stname2)
                for i in range(il):
                    
                    dis= dis+  stname2[il-1 -i][0] + "->"
                    if ((i+1)%5 ==0):
                        dis= dis + " \n "
            else:
                
                for i in range(len(stname2)):
                    
                    dis= dis+  stname2[i][0] + "->"
                    if ((i+1)%5 ==0):
                        dis= dis + " \n "
            dis= dis + " \n "
            if bs3change :
 
                il=len(stname3)
                for i in range(il):
                    
                    dis= dis+  stname3[il-1 -i][0] + "->"
                    if ((i+1)%5 ==0):
                        dis= dis + " \n "
            else:
                
                for i in range(len(stname3)):
                    
                    dis= dis+  stname3[i][0] + "->"
                    if ((i+1)%5 ==0):
                        dis= dis + " \n "
            
            


    else:
        if line1==line2:
            ## for choosing id of start station
            cursor1.execute("select Nxt_Id from "+line1+" where sname='"+start+"';")
            ks1a=cursor1.fetchone()
            ## for choosing id of start station
            cursor1.execute("select Nxt_Id from "+line2+" where sname='"+end+"';")
            ks2a=cursor1.fetchone()
            ## calculation of number of station
            c=math.fabs(int(ks1a[0])-int(ks2a[0]))
            total =c
            ic=0
            
            ## for displayind all stations
            jj1= ks1a[0]
            jj2= ks2a[0]
            if ( jj1 >= jj2) :
                cursor1.execute("select sname from "+line2+" where Nxt_Id >= "+str(jj2)+" and Nxt_Id < "+str(jj1+1)+";")
                stnamesame= cursor1.fetchall()
                bschangesame=True                        
            else:
                cursor1.execute("select sname from "+line2+" where Nxt_Id >= "+str(jj1)+" and Nxt_Id < "+ str(jj2+1)+";")
                stnamesame= cursor1.fetchall()
                bschangesame=False
            ## displaying details
            dis =""
            if (bschangesame==True) :
                il=len(stnamesame)
                for i in range(il):
                    dis= dis+  stnamesame[il-1 -i][0] + "->"
                    if ((i+1)%5 ==0):
                        dis= dis + " \n "
            else:
                for i in range(len(stnamesame)):
                    dis= dis + stnamesame[i][0] + "->"
                    if ((i+1)%5 ==0):
                        dis= dis + " \n "
                    
          

        
        else:
            ## for choosing interchange station between lines
            cursor1.execute("select sname from interchange2 where line1='"+line1+"' and line2='"+line2+"';")
            kc=cursor1.fetchone()
            ## for choosing id of station b/w start station and interchange

            ## id of start station
            cursor1.execute("select Nxt_Id from "+line1+" where sname='"+start+"';")
            ks1=cursor1.fetchone()
            ## id of end statin
            cursor1.execute("select Nxt_Id from "+line2+" where sname='"+end+"';")
            ks2=cursor1.fetchone()
            ## id of interchange station from both lines
            cursor1.execute("select Nxt_Id from "+line1+" where sname='"+kc[0]+"';")
            ki1=cursor1.fetchone()
            cursor1.execute("select Nxt_Id from "+line2+" where sname='"+kc[0]+"';")
            ki2=cursor1.fetchone()
            a=math.fabs(int(ki1[0])-int(ks1[0]))
            b=math.fabs(int(ki2[0])-int(ks2[0]))
            ## calcuation of total number of station
            total = a+b 
            ic=1

            ## displaying details
            jj1=ki1[0]
            jj2=ks1[0]
            if ( jj1 >= jj2) :
                cursor1.execute("select sname from "+line1+" where Nxt_Id >= "+str(jj2)+" and Nxt_Id < "+str(jj1+1)+";")
                stname1c1= cursor1.fetchall()
                bschange1c1=False                       
            else:
                cursor1.execute("select sname from "+line1+" where Nxt_Id >= "+str(jj1)+" and Nxt_Id < "+ str(jj2+1)+";")
                stname1c1= cursor1.fetchall()
                bschange1c1=True
                

            dis=""   
            if (bschange1c1==True) :
                il=len(stname1c1)
                for i in range(il):
                    dis= dis+ stname1c1 [il-1 -i][0] + "->"
                    if ((i+1)%5 ==0):
                        dis= dis + " \n "
        
            else:
                for i in range(len(stname1c1)):
                    dis= dis+  stname1c1[i][0] + "->"
                    if ((i+1)%5 ==0):
                        dis= dis + " \n "

            ## for displaying all statioins
            jj1=ki2[0]
            jj2=int(ks2[0])
            if ( jj1 >= jj2) :
                cursor1.execute("select sname from "+line2+" where Nxt_Id >= "+str(jj2)+" and Nxt_Id < "+str(jj1+1)+";")
                stname3= cursor1.fetchall()             
                bschange1c2=True                     
            else:
                cursor1.execute ("select sname from "+line2+" where Nxt_Id >= "+str(jj1)+" and Nxt_Id < "+ str(jj2+1)+";")
                stname3= cursor1.fetchall()
                bschange1c2=False

            dis= dis + " \n "

            if (bschange1c2==True) :
                il=len(stname3)
                for i in range(il):
                    dis= dis +  stname3[il-1 -i][0] + "->"
                    if ((i+1)%5 ==0):
                        dis= dis + " \n "
        
                    
            else:
                for i in range(len(stname3)):
                    dis= dis +  stname3[i][0] + "->"
                    if ((i+1)%5 ==0):
                        dis= dis + " \n "
        

               
    yval=400
    xval=10
    ldis.place(x=xval+20,y=yval)
    ldis.config(text=dis)

    ## for calculation of cost accoding to station
    dis=total*1.5
    if total<2:
        cost=6
    elif total<4:
        cost=12
    elif total<7:
        cost=18
    elif total<9:
        cost=26
    elif total<11:
        cost=34
    elif total<15:
        cost=42
    else :
        cost=60
    
    
    time=total*2
    ich=ic
    yval=250 
    xval=195

    ## displaying of all  details in a label
    total=int(total)
    sresult = " No. of Stations : " + str(total)     
    lresult.place(x=xval,y=yval)
    lresult.config(text=sresult)

    sresult = " Cost : Rs " + str(cost) 
    yval1=yval+30
    lresult1.place(x=xval,y=yval1)
    lresult1.config(text=sresult)
    
    sresult = " Time : " + str(time) + " min" 
    yval2=yval1+30
    lresult2.place(x=xval,y=yval2)
    lresult2.config(text=sresult)
    
    sresult =  " No. of Interchange Station : " + str(ich)
    yval3=yval2+30
    lresult3.place(x=xval,y=yval3)
    lresult3.config(text=sresult)
    


end=""
start=""
root = Tk()
root.geometry("700x640")
root.configure(background="white")



yval=500
xval=55
m=Label(root, text='From Station',bd=3,width=11,font=("Courier New,",12,"bold"),bg="LemonChiffon2",fg="gray16",relief="ridge")
m.place(x=xval,y=yval)
mv=Label(root, text='',bd=3,font=("Courier New,",12,"bold"),width=11,bg="LemonChiffon2",fg="gray16",relief="ridge")
yval1= yval+30 
mv.place(x=xval,y=yval1)
box = Listbox(root,bg="floral white",fg="grey26")
yval2= yval1+30 
box.place(x=xval,y=yval2)
box2 = Listbox(root,bg="floral white",fg="grey26")
cursor1=connection.cursor()
cursor1.execute("select sname from all_line order by sname;")
k1=cursor1.fetchall()


for item in k1:
   box.insert(END, item[0])
   box2.insert(END, item[0])
  
   
xval=485
mt=Label(root, text='To Station',width=11,font=("Courier New,",12,"bold"),bg="LemonChiffon2",bd=3,fg="gray16",relief="ridge")
mt.place(x=xval,y=yval)

mvto=Label(root, text='',bd=3,width=11,font=("Courier New,",12,"bold"),bg="LemonChiffon2",fg="gray16",relief="ridge")
mvto.place(x=xval,y=yval1)
box2.place(x=xval,y=yval2)

btjouy = Button(root, text = 'Journey Planner',font=("Courier New,",18,"bold"),relief="ridge",bg="floral white",activebackground="gray86",width=15, fg='firebrick3',command=creation)
btjouy.place(x=100,y=250)
btend = Button(root, text = 'Back',font=("Courier New,",18,"bold"),relief="ridge",bg="floral white",activebackground="gray86",width=15, fg='firebrick3',command=menu)
btend.place(x=100,y=350)



sresult=""
lresult=Label(root, text=sresult,bd=3,width=25,font=("Courier New,",12,"bold"),bg="LemonChiffon2",fg="gray16",relief="ridge")
yval=400
lresult.place(x=190,y=yval)
lresult.config(text=sresult)


       
lresult1=Label(root, text=sresult,bd=3,width=25,font=("Courier New,",12,"bold"),bg="LemonChiffon2",fg="gray16",relief="ridge")
yval1=yval+30
lresult1.place(x=190,y=yval1)
lresult1.config(text=sresult)
    
     
lresult2=Label(root, text=sresult,bd=3,width=25,font=("Courier New,",12,"bold"),bg="LemonChiffon2",fg="gray16",relief="ridge")
yval2=yval1+30
lresult2.place(x=190,y=yval2)
lresult2.config(text=sresult)
    
lresult3=Label(root, text=sresult,bd=3,width=25,font=("Courier New,",12,"bold"),bg="LemonChiffon2",fg="gray16",relief="ridge")
yval3=yval2+30
lresult3.place(x=190,y=yval3)
lresult3.config(text=sresult)

ldis=Label(root, text=sresult,bd=3,font=("Courier New,",12,"bold"),bg="LemonChiffon2",fg="gray16",relief="ridge")
yval3=yval2+30
ldis.place(x=190,y=yval3)

    
    
def route_invisible():
    m.place_forget()
    mv.place_forget()
    box.place_forget()
    
    mvto.place_forget()
    mt.place_forget()
    box2.place_forget()

    btjouy.place_forget()
    btend.place_forget()
    
    lresult.place_forget()
    lresult1.place_forget()
    lresult2.place_forget()
    lresult3.place_forget()
    
    ldis.place_forget()

    
    
def route_visible():
    yval=125 
    xval=55
    m.place(x=xval,y=yval)
    yval1= yval+30 
    mv.place(x=xval,y=yval1)
    yval2= yval1+30 
    box.place(x=xval,y=yval2)
    btjouy.place(x=xval+160,y=yval)
    btend.place(x=xval+160,y=yval+60)
    
    xval=485
    mt.place(x=xval,y=yval)
    mvto.place(x=xval,y=yval1)
    box2.place(x=xval,y=yval2)
    
    l2.place_forget()

    mueseum.place_forget()
    route.place_forget()
    OInfo.place_forget()
    TGuide.place_forget()
    LnF.place_forget()

    
    



def on_first_box(idx, val):
    global start
    start = val
    mv.config(text=val)


def on_second_box(idx, val):
    global end
    end=val
    mvto.config(text=val)


def onselect(event, listbox):
    w = event.widget
    try:
        idx = int(w.curselection()[0])
    except IndexError:
        return
    if listbox is box:
        return on_first_box(idx, w.get(idx))
    if listbox is box2:
        return on_second_box(idx, w.get(idx))



def tour():
    root=Tk()       
    label = Label(root, text="Tourist Places Nearest To Delhi Metro Station",fg="red",bg="floral white", font=("Arial",30)).grid(row=0, columnspan=4)
    cols = ('SNo', 'Tourist Place', 'Metro', 'Distance')
    listBox = ttk.Treeview(root, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)    
    listBox.grid(row=1, column=0, columnspan=2)
    
    cursor1=connection.cursor()
    cursor1.execute("select * from tour ;")
    k=cursor1.fetchall()
    for i in range(len(k)):
        listBox.insert("", "end", values=(k[i][0],k[i][1],k[i][2],k[i][3]))




box.bind('<<ListboxSelect>>', lambda e: onselect(e, box))
box2.bind('<<ListboxSelect>>', lambda e: onselect(e, box2))


i="metro_logo.png"
img=PhotoImage(file=i)
l1=Label(root,image=img,bg="white")
l1.place(x=0,y=0,width=725)
i2="metro12.png"
img1=PhotoImage(file=i2)
l2=Label(root,image=img1)
l2.place(x=156,y=125)

mueseum=Button(root,text="Metro\nMuseum",fg="red",bg="floral white",command=lambda:museum(),width=15,font=("courier new",18),activebackground="grey86")
route=Button(root,text="Route Between\nStations",fg="red",command=lambda:route_visible(),bg="floral white",width=15,font=("courier new",18),activebackground="grey82")
OInfo=Button(root,text="Other\nInfo",fg="red",command=lambda:others(),bg="floral white",width=31,font=("courier new",18),activebackground="grey86")
TGuide=Button(root,text="Tour\nGuide",fg="red",command=lambda:tour(),bg="floral white",width=15,font=("courier new",18),activebackground="grey82")
LnF=Button(root,text="Lost And\nFound",fg="red",command=lambda:lost(),bg="floral white",width=15,font=("courier new",18),activebackground="grey82")

xmenu=135
ymenu=400
route.place(x=xmenu,y=ymenu)
mueseum.place(x=xmenu+225,y=ymenu)
OInfo.place(x=xmenu,y=ymenu+75)
TGuide.place(x=xmenu,y=ymenu+150)
LnF.place(x=xmenu+225,y=ymenu+150)

route_invisible()
root.title("DMRC")
root.mainloop()
