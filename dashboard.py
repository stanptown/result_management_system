from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk  #pip install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
import sqlite3
import os
class RMS:
	def add_course(self):
		self.new_win=Toplevel(self.root)
		self.new_obj=CourseClass(self.new_win)
	def add_student(self):
		self.new_win=Toplevel(self.root)
		self.new_obj=studentClass(self.new_win)
	def add_result(self):
		self.new_win=Toplevel(self.root)
		self.new_obj=resultClass(self.new_win)
	def add_report(self):
		self.new_win=Toplevel(self.root)
		self.new_obj=reportClass(self.new_win)
	def exit(self):
		op=messagebox.askyesno("Confirm","Do you really want to exit?",parent=self.root)
		if op==True:
			self.root.destroy()
	def __init__(self,root):
		self.root=root;
		self.root.title("Student Result Management System")
		# 1350x700 is the window and +0+0 is the coordinates
		self.root.geometry("1350x700+0+0")
		self.root.config(bg="white")
		#====icons=====
		self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")

		#====title=====
		title=Label(self.root,text="Student Result Managment System",image=self.logo_dash,padx=10,compound=LEFT,font=("goudy old style",20,"bold"),bg='#033054',fg="white").place(x=0,y=0,relwidth=1,height=50)

		# Menu
		M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
		M_Frame.place(x=10,y=70,width=1340,height=80)

		btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg='#0b5337',fg="black",cursor="hand2",highlightbackground="#3E4149",command=self.add_course).place(x=20,y=5,width=230,height=40)
		btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg='#0b5337',fg="black",cursor="hand2",highlightbackground="#3E4149",command=self.add_student).place(x=290,y=5,width=230,height=40)
		btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg='#0b5337',fg="black",cursor="hand2",highlightbackground="#3E4149",command=self.add_result).place(x=560,y=5,width=230,height=40)
		btn_view=Button(M_Frame,text="View Student Results",font=("goudy old style",15,"bold"),bg='#0b5337',fg="black",cursor="hand2",highlightbackground="#3E4149",command=self.add_report).place(x=830,y=5,width=230,height=40)
		# btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg='#0b5337',fg="black",cursor="hand2",highlightbackground="#3E4149").place(x=900,y=5,width=200,height=40)
		btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg='#0b5337',fg="black",cursor="hand2",highlightbackground="#3E4149",command=self.exit).place(x=1100,y=5,width=230,height=40)


		#====content window====
		self.bg_img=Image.open("images/bg.png")
		self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
		self.bg_img=ImageTk.PhotoImage(self.bg_img)

		self.lbl_bg=Label(self.root,image=self.bg_img).place(x=200,y=180,width=920,height=350)

		#====update details=====
		self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
		self.lbl_course.place(x=200,y=530,width=300,height=100)

		self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
		self.lbl_student.place(x=510,y=530,width=300,height=100)

		self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
		self.lbl_result.place(x=820,y=530,width=300,height=100)
 

		#====footer=====
		footer=Label(self.root,text="SRMS-Student Result Managment System\nDeveloped by Satvik Tiwari",font=("goudy old style",12),bg='#262626',fg="white").pack(side=BOTTOM,fill=X)
		self.details()
	def details(self):
		con=sqlite3.connect(database="rms.db")
		cur=con.cursor()

		try:
			cur.execute("select * from course")
			cr=cur.fetchall()
			self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
			cur.execute("select * from student")
			cr=cur.fetchall()
			self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
			cur.execute("select * from result")
			cr=cur.fetchall()
			self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
			self.lbl_course.after(200,self.details)
			# self.lbl_student.after(200,self.details)
			# self.lbl_result.after(200,self.details)
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to {str(ex)}")

    



if __name__=="__main__":
	root=Tk()
	obj=RMS(root)
	# to make sure the screen stay with us
	root.mainloop()  

