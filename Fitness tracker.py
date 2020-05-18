from tkinter import*
import time
import datetime

root=Tk()
root.geometry("1600x8000")
root.title("Health Manager")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)


localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arial',50,'bold'),text="Fitness Tracker",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)




#********************************************************************************************

def bmr():
    g = str(gender.get())
    h = int(height.get())
    w = int(weight.get())
    a = int(age.get())

    H = h * 6.25
    W = w * 9.99
    A = a * 4.92
    if g == 'm' or g == 'M':
        bmr = H + W - A + 5
        
    elif g == 'f' or g == 'F':
        bmr = H + W - A - 161

    tdee = aLevel(bmr,g)
    return tdee;

def aLevel(bmr,g): 


    aLevel = int(level.get())
    if g == 'm' or g == 'M' :
        if aLevel == 1:
            tdee = 1.2 * bmr
        elif aLevel == 2:
            tdee = 1.375 * bmr
        elif aLevel == 3:
            tdee = 1.55 * bmr
        elif aLevel == 4:
            tdee = 1.725 * bmr

            
    if g == 'f' or g == 'F':
        if aLevel == 1:
            tdee = 1.1 * bmr
        elif aLevel == 2:
            tdee = 1.275 * bmr
        elif aLevel == 3:
            tdee = 1.35 * bmr
        elif aLevel == 4:
            tdee = 1.525 * bmr

    return(int(tdee))

def Ref():
    cal = bmr()
    Total.set(cal)

def Reset():
    gender.set("") 
    height.set("")
    weight.set("")
    age.set("")
    level.set("")
    Total.set("")

    
def qExit():
    root.destroy()



    
#====================================Restaraunt Info 1===========================================================
gender = StringVar()
height=StringVar()
weight=StringVar()
age=StringVar()
level=StringVar()
Total=StringVar()




lblgender= Label(f1, font=('arial', 16, 'bold'),text="Male(M)/Female(F)",bd=16,anchor="w")
lblgender.grid(row=0, column=0)
txtgender=Entry(f1, font=('arial',16,'bold'),textvariable=gender,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtgender.grid(row=0,column=1)

lblheight= Label(f1, font=('arial', 16, 'bold'),text="Height(in Cm)",bd=16,anchor="w")
lblheight.grid(row=1, column=0)
txtheight=Entry(f1, font=('arial',16,'bold'),textvariable=height,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtheight.grid(row=1,column=1)


lblweight= Label(f1, font=('arial', 16, 'bold'),text="Weight (in Kg)",bd=16,anchor="w")
lblweight.grid(row=2, column=0)
txtweight=Entry(f1, font=('arial',16,'bold'),textvariable=weight,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtweight.grid(row=2,column=1)


lblage= Label(f1, font=('arial', 16, 'bold'),text="Age",bd=16,anchor="w")
lblage.grid(row=3, column=0)
txtage=Entry(f1, font=('arial',16,'bold'),textvariable=age,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtage.grid(row=3,column=1)

lbl8= Label(f1, font=('arial', 16, 'bold'),text="",bd=16,anchor="w")
lbl8.grid(row=4, column=0)


lbl9= Label(f1, font=('arial', 16, 'bold'),text="",bd=16,anchor="w")
lbl9.grid(row=5, column=0)


#============================================================================================================
#                                RESTAURANT INFO 2
#========================================================================================

lbl= Label(f1, font=('arial', 16, 'bold'),text="ACTIVITY LEVEL(S.No)",bd=16,anchor="w")
lbl.grid(row=0, column=2)
txtlevel=Entry(f1, font=('arial',16,'bold'),textvariable=level,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtlevel.grid(row=0,column=3)


lbl1= Label(f1, font=('arial', 16, 'bold'),text="1. Couch Potato",bd=16,anchor="w")
lbl1.grid(row=1, column=2)



lbl2= Label(f1, font=('arial', 16, 'bold'),text="2. Going to Work is my cardio",bd=16,anchor="w")
lbl2.grid(row=2, column=2)



lbl3= Label(f1, font=('arial', 16, 'bold'),text="3. Getting them pecs",bd=16,anchor="w")
lbl3.grid(row=3, column=2)


lbl4= Label(f1, font=('arial', 16, 'bold'),text="4. B.U.F.F",bd=16,anchor="w")
lbl4.grid(row=4, column=2)


lblTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Calorie needed",bd=16,anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTotalCost.grid(row=5,column=3)

#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Check",bg="powder blue",command=Ref).grid(row=8,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=8,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=8,column=3)


root.mainloop()


