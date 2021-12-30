from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class resultClass:
	def __init__(self,root):
		self.root=root;
		self.root.title("Student Result Management System")
		# 1350x700 is the window and +0+0 is the coordinates
		self.root.geometry("1200x480+80+170")
		self.root.config(bg="white")
		self.root.focus_force()
		#=========title====
		title=Label(self.root,text="Add Student Results",font=("goudy old style",20,"bold"),bg='orange',fg="#262626").place(x=10,y=15,width=1180,height=50)
		#=======widgets=======
		#=======variables======
		self.var_roll=StringVar()
		self.var_name=StringVar()
		self.var_course=StringVar()
		self.var_marks=StringVar()
		self.var_full_marks=StringVar()
		self.roll_list=[]
		self.fetch_roll()

		lbl_select=Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
		lbl_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
		lbl_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=220)
		lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
		lbl_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)

		self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
		self.txt_student.place(x=280,width=200,y=100)
		self.txt_student.set("Select")
		btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg='#0b5337',fg="black",cursor="hand2",highlightbackground="#3E4149",command=self.search).place(x=500,y=100,width=100,height=30)

		txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,"bold"),bg='lightyellow',state='readonly').place(x=280,width=320,y=160)
		txt_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,"bold"),bg='lightyellow',state='readonly').place(x=280,width=320,y=220)
		txt_marks=Entry(self.root,textvariable=self.var_marks,font=("goudy old style",20,"bold"),bg='lightyellow').place(x=280,width=320,y=280)
		txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("goudy old style",20,"bold"),bg='lightyellow').place(x=280,width=320,y=340)
		#=======buttonn====

		btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg='#0b5337',fg="black",cursor="hand2",highlightbackground="#3E4149",command=self.add).place(x=300,y=420,width=120,height=35)
		btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg='#0b5337',fg="black",cursor="hand2",highlightbackground="#3E4149",command=self.clear).place(x=430,y=420,width=120,height=35)
		#=======image========
		self.bg_img=Image.open("images/result.jpg")
		self.bg_img=self.bg_img.resize((500,300),Image.ANTIALIAS)
		self.bg_img=ImageTk.PhotoImage(self.bg_img)

		self.lbl_bg=Label(self.root,image=self.bg_img).place(x=650,y=100)

#===========functions
	def fetch_roll(self):
		con=sqlite3.connect(database="rms.db")
		cur=con.cursor()
		try:
			cur.execute("select roll from student")
			row=cur.fetchall()
			v=[]
			if len(row)>0:
				for rows in row:
					self.roll_list.append(rows[0])
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to {str(ex)}")

	def search(self):
		con=sqlite3.connect(database="rms.db")
		cur=con.cursor()
		try:
			cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
			row=cur.fetchone()
			if row!=None:
				self.var_name.set(row[0])
				self.var_course.set(row[1])
			else:
				messagebox.showerror("Error","No record found",parent=self.root)
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to {str(ex)}")

	def add(self):
		con=sqlite3.connect(database="rms.db")
		cur=con.cursor()
		try:
			if self.var_name.get()=="":
				messagebox.showerror("Error","Please first search student record",parent=self.root)
			else:

				cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
				row=cur.fetchone()
				# print(24242422)
				# print("hi satvik")
				if row!=None:
					messagebox.showerror("Error","Result already present",parent=self.root)
				else:
					per=round((int(self.var_marks.get())*100)/int(self.var_full_marks.get()),3)

					# print(self.var_marks.get())
					cur.execute("insert into result (roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",(
						self.var_roll.get(),
						self.var_name.get(),
						self.var_course.get(),
						self.var_marks.get(),
						self.var_full_marks.get(),
						str(per)
					))
					con.commit()
					messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
					
		except Exception as ex:
			messagebox.showerror("Error",f"Error due to {str(ex)}")

	def clear(self):
		self.var_roll.set("Select"),
		self.var_name.set(""),
		self.var_course.set(""),
		self.var_marks.set(""),
		self.var_full_marks.set(""),
		



if __name__=="__main__":
	root=Tk()
	obj=resultClass(root)
	# to make sure the screen stay with us
	root.mainloop() 