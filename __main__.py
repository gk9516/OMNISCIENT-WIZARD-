from tkinter import *
from tkcalendar import *
from tkinter import messagebox
from tkinter import simpledialog 
from tkinter import ttk
from tkscrolledframe import ScrolledFrame


from PIL import Image,ImageTk #Python Image library

from plyer import notification

import time
import webbrowser
import pickle

from datetime import datetime, time as time_mark, date as date_

#For COVID data retrieval
import requests
import bs4

from Matrices_Master_Module import Master_Matrix_Data

from Matrix_Tools import *
from Matrices_Master_Module import Matrix

import pyttsx3

# Initialize the converter 
converter = pyttsx3.init() 
converter.setProperty('rate', 180) 
converter.setProperty('volume', 0.7) 
converter.say("Hello master! I am a wizard at your service. Please say thine name to get started!") 
converter.runAndWait()


with open(r"C:\Users\ganes\AppData\Local\Programs\Python\Python38\Omniscient Wizard\Omniscient Wizard\Data\Save_Binary.txt","rb+") as data_handler:
	try:
		Save_Data = pickle.load(data_handler)
	except EOFError:
		Save_Data = {
			"Task" : "Enter your task here!",
			"raw_timetable": {
					'Monday' : ['Physics','Comp. Sci.','Mathematics','Chemistry','JEE_Chemistry'],
					'Tuesday': ['Physics','Comp. Sci.','Mathematics','English','JEE_Mathematics'],
					'Wednesday': ['Physics','Comp. Sci.','Mathematics','Chemistry','JEE_Physics'],
					'Thursday': ['Chemistry','Comp. Sci.','Physics','English','JEE_Chemistry'],
					'Friday': ['Mathematics','Comp. Sci.','Chemistry','English','JEE_Physics'],
					'Saturday': ['Physics','Mathematics','Chemistry','English','JEE_Mathematics']
					},
			"exam_data": [],
			"timing": [
						(time_mark(8,0,0),time_mark(8,45,0)),   #School First Session
						(time_mark(9,0,0),time_mark(9,45,0)),   #School Second Session
						(time_mark(10,0,0),time_mark(10,45,0)), #School Third Session
						(time_mark(11,0,0),time_mark(11,45,0)), #School Fourth Session
						(time_mark(17,0,0),time_mark(18,30,0)), #Conceptree Session
						(time_mark(23,59,59),)                   #Day - end
						] ,
			"user_preferences" : {

				"notifications" : {"sn_enabled" : False,
								"en_enabled" : False,
								"sn_timing": 5, #In Minutes
								"en_timing": 2}, #In Days

				"sessions" : {"List_Of_Subjects" : ['Physics','Chemistry','Comp. Sci.','English','Mathematics','JEE_Physics','JEE_Chemistry','JEE_Mathematics'],
							"Links":  {
										'Physics':     'https://meet.google.com/crp-srmr-hdo',
										'Chemistry':   'https://meet.google.com/feo-pahv-tou',
										'Comp. Sci.':  'https://meet.google.com/qxx-rxkh-igo',
										'English':     'https://meet.google.com/iks-ubon-frk',
										'Mathematics': 'https://meet.google.com/kie-stsh-rso',
										'JEE_Physics': 'https://us02web.zoom.us/j/81016169213?pwd=VVpKQmtWbytoK0FpanV5Yyt0TnZIdz09',
										'JEE_Chemistry': 'https://us02web.zoom.us/j/81016169213?pwd=VVpKQmtWbytoK0FpanV5Yyt0TnZIdz09',
										'JEE_Mathematics': 'https://us02web.zoom.us/j/81016169213?pwd=VVpKQmtWbytoK0FpanV5Yyt0TnZIdz09'
										} ,
							"Max_Sessions_Per_Day": 5
							},
				"theme": {
							'subject_colorcodes': 'Light',
							'Theme': 'Light'
							}
						}
			} #end save_data 


def window_closed():

	close = messagebox.askquestion("Sending the Wizard to rest","Are you sure your tasks are done with the wizard?")

	if close == 'yes':
		with open("Data/Save_Binary.txt","wb+") as data_handler:
			pickle.dump(Save_Data,data_handler)

		OW.quit()

		print("Data saved! Application closed.")
	else:
		pass

#User_Data


Username = "Ganesh"
Greeting = f"  Welcome back, Sorcerer {Username}!"
days_left = 48
QOTD = "If you wish to shine like the sun itself, then BURN \n like it"


Days_In_A_Week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']


Max_Sessions_Per_Day = Save_Data['user_preferences']['sessions']['Max_Sessions_Per_Day']
Links = Save_Data['user_preferences']['sessions']['Links']
List_Of_Subjects = Save_Data['user_preferences']['sessions']['List_Of_Subjects']


Options = {
	'subject_colorcodes': 'Light',
	'Theme': 'Light'
}



#Data-------------------------------------------------------------------------------------------------------------------

Theme = {
	'Light' : {"Background" : "#E6E6FA", "Text" : "#1F2523"} ,
	'Dark' : {"Background" : "#5D6A66", "Text" : 'white'}
}

subject_colorcodes = {

	'Light' : {
		'Physics': '#FFCD47',
		'Chemistry': '#1DD5A7',
		'Mathematics': '#47B9FF',
		'Comp. Sci.': '#FF3F73',
		'English' : '#F662FF',
		'JEE_Physics': '#FFCD47',
		'JEE_Chemistry': '#1DD5A7',
		'JEE_Mathematics': '#47B9FF'
	},

	'Dark' : {
		'Physics': '#F5BD00',
		'Chemistry': '#00D376',
		'Mathematics': '#00B3D3',
		'Comp. Sci.': '#D30086',
		'English' : '#C000D3',
		'JEE_Physics': '#F5BD00',
		'JEE_Chemistry': '#00D376',
		'JEE_Mathematics': '#00B3D3'
	},

	'Legacy' : {
		'Physics': '#FFCD00',
		'Chemistry': '#00FF64',
		'Mathematics': '#00A6FF',
		'Comp. Sci.': '#FF004D',
		'English' : '#7800FF',
		'JEE_Physics': '#FFCD00',
		'JEE_Chemistry': '#00FF64',
		'JEE_Mathematics': '#00A6FF'		
	},

	'Vivid' : {
		'Physics': '#FFCD00',
		'Chemistry': '#15D06A',
		'Mathematics': '#47B9FF',
		'Comp. Sci.': '#FF004D',
		'English' : '#7800FF',
		'JEE_Physics': '#FFCD00',
		'JEE_Chemistry': '#15D06A',
		'JEE_Mathematics': '#47B9FF'		
	}
}


#----------------------------------------{Master_Initialization}-------------------------------------------------------------


Background_Window_Color = Theme[Options['Theme']]['Background']
Text_Color = Theme[Options['Theme']]['Text']
Current_Task = Save_Data["Task"]
Ribbon_Color = "#3399ff"


#------------------------------------------{App Definitions}---------------------------------------------------------------

class Omniscient_Wizard(Tk):
	
	def __init__ (self,*args,**kwargs):
		Tk.__init__(self,*args,**kwargs)
		self.withdraw()
		base_frame = Frame(self,bg = Background_Window_Color)
		base_frame.pack(fill = "both",expand = 1)

		base_frame.grid_columnconfigure(0,weight = 1)
		base_frame.grid_columnconfigure(1,weight = 20)
		base_frame.grid_rowconfigure(0,weight = 1)

		Main_Ribbon = Frame(base_frame,bg = Ribbon_Color)
		Main_Ribbon.grid(column = 0,row = 0,sticky = 'nsew')

		raw_exit = Image.open('Resources/Icons/exit.png')
		self.exit = ImageTk.PhotoImage(raw_exit)

		raw_timetable = Image.open('Resources/Icons/timetable.png')
		self.timetable = ImageTk.PhotoImage(raw_timetable)

		raw_planning = Image.open('Resources/Icons/planning.png')
		self.planning = ImageTk.PhotoImage(raw_planning)
	
		raw_study = Image.open('Resources/Icons/study.png')
		self.study = ImageTk.PhotoImage(raw_study)

		raw_ow_icon = Image.open(r"C:\Users\ganes\AppData\Local\Programs\Python\Python38\Omniscient Wizard\Omniscient Wizard\Resources\Icons\ow_icon.png")
		self.ow_icon = ImageTk.PhotoImage(raw_ow_icon)

		raw_settings = Image.open('Resources/Icons/settings.png')
		self.settings = ImageTk.PhotoImage(raw_settings)

		self.frames = {}

		home_frame = Home(base_frame,self)
		home_frame.grid(column = 1, row = 0,sticky = 'nsew')

		study_frame = Study(base_frame,self)
		study_frame.grid(column = 1, row = 0, sticky = 'nsew')

		timetable_frame = Timetable(base_frame,self)
		timetable_frame.grid(column = 1, row = 0 , sticky = 'nsew')

		etimetable_frame = Edit_Timetable(base_frame,self)
		etimetable_frame.grid(column = 1, row = 0, sticky = 'nsew')



		math_frame = Mathematics(base_frame,self)
		math_frame.grid(column = 1, row = 0, sticky = 'nsew')

		n_settings_frame = Notification_Settings(base_frame,self)
		n_settings_frame.grid(column = 1, row  = 0, sticky = 'nsew')

		self.frames["notification_settings"] = n_settings_frame

		s_settings_frame = Session_Settings(base_frame,self)
		s_settings_frame.grid(column = 1, row = 0, sticky = 'nsew')

		self.frames["sessions_settings"] = s_settings_frame

		settings_frame = Settings(base_frame,self)
		settings_frame.grid(column = 1, row = 0, sticky = 'nsew')

		add_exam_frame = Add_Exam(base_frame,self)
		add_exam_frame.grid(column = 1, row = 0, sticky = 'nsew')

		edit_exam_frame = Edit_Exam(base_frame,self)
		edit_exam_frame.grid(column = 1, row = 0, sticky = 'nsew')





		self.frames["Home"] = home_frame
		self.frames["Study"] = study_frame
		self.frames["Timetable"] = timetable_frame

		self.frames["Math"] = math_frame
		self.frames["Edit_Timetable"] = etimetable_frame
		self.frames["Settings"] = settings_frame
		self.frames["Add_Exam"] = add_exam_frame
		self.frames["Edit_Exam"] = edit_exam_frame

		exams_frame = Exams(base_frame,self)
		exams_frame.grid(column = 1, row = 0, sticky = 'nsew')

		self.frames["Exams"] = exams_frame

		#-----{Subject Frames: Mathematics}-------

		#Matrices

		matrices_ile = Math_Matrices_ILE(base_frame,self)
		matrices_ile.grid(column = 1, row = 0, sticky = 'nsew')

		matrices_frame = Math_Matrices(base_frame,self)
		matrices_frame.grid(column = 1, row = 0, sticky = 'nsew')
		#--------
		self.frames["Math_Matrices"] = matrices_frame

		self.frames["MatricesILE"] = matrices_ile

		Main_Ribbon.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9),weight = 1)
		Main_Ribbon.grid_columnconfigure(0,weight = 1)

		ICON = Button(Main_Ribbon,image = self.ow_icon, bg = Ribbon_Color, activebackground = 'white', compound = 'left', command = lambda: self.show_frame("Home"), bd = 0, relief = 'flat')
		
		ICON.grid(row = 0, column = 0,columnspan = 1)

		STUDY = Button(Main_Ribbon,image = self.study, compound = 'left', bg = Ribbon_Color ,command = lambda: self.show_frame("Study"), bd = 0)

		STUDY.grid(row = 1, column = 0,columnspan = 1)

		TIMETABLE = Button(Main_Ribbon,image = self.timetable, compound = 'left', bg = Ribbon_Color, command = lambda: self.show_frame("Timetable"),bd = 0)

		TIMETABLE.grid(row = 2, column = 0,columnspan = 1)

		PLANNING = Button(Main_Ribbon,image = self.planning, compound = 'left', bg = Ribbon_Color, command = lambda: self.show_frame("Exams"),bd = 0)

		PLANNING.grid(row = 3, column = 0,columnspan = 1)

		EXIT = Button(Main_Ribbon,image = self.exit, compound = 'left', bg = Ribbon_Color , command = lambda: window_closed(),bd = 0)

		EXIT.grid(row = 9, column = 0,columnspan = 1)

		SETTINGS = Button(Main_Ribbon, image = self.settings,compound = 'left', bg = Ribbon_Color, command = lambda: self.show_frame("Settings"),bd = 0)
		SETTINGS.grid(row = 8, column = 0, columnspan = 1)



		self.show_frame("Home") #Initial Page

		
		Username = simpledialog.askstring(title = "Login",prompt = "Enter your full name here")
		converter.say("Please note that I am an alpha version Wizard. Any feature you use will be predefined. However you can change them anytime you wish") 
		converter.runAndWait()

		if Username:
			self.frames['Home'].greetings['text'] = f"Welcome back, Sorcerer {Username}!"
		else:
			self.frames['Home'].greetings['text'] = "Welcome back, Sorcerer!"
		self.deiconify()



	def show_frame(self,frame):
		f = self.frames[frame]
		f.tkraise()



#------------------------------------------{Window Definitions}---------------------------------------------------------------

class Home(Frame):

	notification_timing = Save_Data['user_preferences']['notifications']['sn_timing'] #Mmory point

	def __init__(self,parent,controller):
		Frame.__init__(self,parent)

		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure((0,2,4), weight = 10)
		self.grid_columnconfigure(1, weight = 10)
		self.grid_columnconfigure(3, weight = 60)
		self['bg'] = Background_Window_Color
		
		self.greetings = Label(self,text = Greeting, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
		self.greetings.grid(row = 0, column = 1,sticky = 'w')

		shortcut_frame = Frame(self,bg = Background_Window_Color)
		shortcut_frame.grid(row = 1, column = 1, sticky = 'nsew')

		shortcut_frame.grid_rowconfigure((0,2,4),weight = 23)
		shortcut_frame.grid_rowconfigure((1,3,5),weight = 4)
		shortcut_frame.grid_rowconfigure(6,weight = 3)
		shortcut_frame.grid_columnconfigure(0,weight = 1)

		rshortcut_frame = Frame(self,bg = Background_Window_Color)
		rshortcut_frame.grid(row = 1,column = 3,sticky = 'nsew')

		rshortcut_frame.grid_rowconfigure((0,2,4),weight = 15)
		rshortcut_frame.grid_rowconfigure((1,3,5),weight = 5)
		rshortcut_frame.grid_rowconfigure(6,weight = 6)
		rshortcut_frame.grid_columnconfigure(0,weight = 1)

		#COVID-19 (First Left)

		raw_virus = Image.open('Resources/Backgrounds/covid.png')
		self.virus = ImageTk.PhotoImage(raw_virus)


		label_frame = Frame(shortcut_frame,bg = 'grey')
		label_frame.grid(row = 0, column = 0, sticky = 'nsew')


		label_frame.grid_rowconfigure(0,weight = 2)
		label_frame.grid_rowconfigure(1,weight = 5)
		label_frame.grid_columnconfigure(0,weight = 1)


		top_frame = Frame(label_frame,bg = Text_Color)
		top_frame.grid(row = 0, column = 0,sticky = 'nsew')
		bottom_frame = Frame(label_frame,bg = 'white')
		bottom_frame.grid(row = 1, column = 0 , sticky = 'nsew')
		top_frame.grid_propagate(0)
		bottom_frame.grid_propagate(0)
		top_frame.grid_columnconfigure(0,weight = 1)
		top_frame.grid_rowconfigure(0,weight = 1)
		bottom_frame.grid_columnconfigure(0,weight = 1)
		bottom_frame.grid_rowconfigure(0,weight = 1)
	
		
		shortcut_covid = Button(bottom_frame,fg = 'white',bg = 'red',borderwidth = 0,font = ('Arial',20),text = "Testing",image = self.virus,compound = 'center')
		shortcut_covid.grid(row = 0, column = 0,sticky = 'nsew')
		
		covid_title = Label(top_frame,text = "Total No. of cases in India",bg = 'black',fg = 'white',font = ('Arial',20))
		covid_title.grid(row = 0,column = 0,sticky = 'nsew')
		


		#Sessions (Second Left)

		raw_session = Image.open('Resources/Backgrounds/session.png')
		raw_session = raw_session.resize((770,105),Image.ANTIALIAS)
		self.session = ImageTk.PhotoImage(raw_session)


		session_frame = Frame(shortcut_frame,bg = 'black')
		session_frame.grid(row = 2, column = 0, sticky = 'nsew')


		session_frame.grid_rowconfigure(0,weight = 1)
		session_frame.grid_rowconfigure(1,weight = 20)
		session_frame.grid_columnconfigure(0,weight = 1)
		session_frame.grid_propagate(0)

		
		shortcut_session = Button(session_frame,fg = 'white',bg = 'black',font = ('Arial',20),text = "Next Session: Computer Science at 9:00 A.M",image = self.session, compound  = 'center',bd = 0, activeforeground = 'white',relief = 'flat')
		shortcut_session.grid(row = 1, column = 0,sticky = 'nsew')
		
		session_title = Label(session_frame,text = "Sessions Manager", bg = 'black',fg = 'white',font = ('Aeriel',20))
		session_title.grid(row = 0,column = 0,sticky = 'nsew')
		

		

		#task (Exam) - (Third Left)

		raw_task = Image.open('Resources/Backgrounds/jee.png')
		self.task = ImageTk.PhotoImage(raw_task)

		task_frame = Frame(shortcut_frame,bg = 'grey')
		task_frame.grid(row = 4, column = 0, sticky = 'nsew')


		task_frame.grid_rowconfigure(0,weight = 1)
		task_frame.grid_rowconfigure(1,weight = 10)
		task_frame.grid_columnconfigure(0,weight = 1)

		task_frame.grid_propagate(0)
		
		self.shortcut_task = Button(task_frame,fg = 'white',bg = Text_Color,borderwidth = 0,font = ('Arial',20),image = self.task, compound  = 'center', command = lambda: controller.show_frame("Exams"))
		self.shortcut_task.grid(row = 1, column = 0,sticky = 'nsew')
		
		task_title = Label(task_frame,text = "Exams Manager", bg = 'black',fg = 'white',font = ('Aeriel',20))
		task_title.grid(row = 0,column = 0,sticky = 'nsew')
		

		#Daily Quote (Fourth Left)
		quote = Message(shortcut_frame,width = '1000',fg = Text_Color,bg = Background_Window_Color,borderwidth = 0,font = ('Helvetica',25,'italic'),text = f"~{QOTD}~")
		quote.grid(row = 6, column = 0,sticky = 'ew',columnspan = 2)

		#Jee
		jee_days_left = Frame(rshortcut_frame, bg = '#65706E')
		jee_days_left.grid(row = 0, column = 0,sticky = 'nsew')

		jee_days_left.grid_columnconfigure(0,weight = 1)
		jee_days_left.grid_columnconfigure(1,weight = 3)
		jee_days_left.grid_rowconfigure(0,weight = 1)

		days = Label(jee_days_left,text = f"{days_left}",fg = "white",bg = '#FF811F',font = ('Ariel',30))	
		jee_msg = Label(jee_days_left,text = "days left for JEE examination",fg = "white",bg = '#65706E',font = ('Ariel',20))

		jee_msg.grid(row = 0,column = 1,sticky = 'nsew')
		days.grid(row = 0,column = 0,sticky = 'nsew')

		#Date

		date_today = Frame(rshortcut_frame, bg = '#65706E')
		date_today.grid(row = 4, column = 0,sticky = 'nsew')

		date_today.grid_columnconfigure(0,weight = 1)
		date_today.grid_columnconfigure(1,weight = 4)
		date_today.grid_rowconfigure(0,weight = 1)

		date = Label(date_today,text = time.strftime("%dth %M %Y"),fg = "white",bg = '#65706E',font = ('Ariel',20))	
		date_title = Label(date_today,text = "Date",fg = "white",bg = '#1FFFCF',font = ('Ariel',30))

		date.grid(row = 0,column = 1,sticky = 'nsew')
		date_title.grid(row = 0,column = 0,sticky = 'nsew')

		#Task

		task_frame = Frame(rshortcut_frame, bg = '#65706E')
		task_frame.grid(row = 2, column = 0,sticky = 'nsew')

		task_frame.grid_columnconfigure(0,weight = 1)
		task_frame.grid_columnconfigure(1,weight = 4)
		task_frame.grid_rowconfigure(0,weight = 1)

		def update_task():
			new_task = simpledialog.askstring(title="Enter new task!",prompt = "Your task:",initialvalue = Save_Data['Task'])

			if new_task == None:
				pass
			else:
				Save_Data["Task"] = new_task
				task["text"] = new_task


		task = Button(task_frame,text = Current_Task,fg = "white",bg = '#65706E',font = ('Ariel',20),bd = 0,command = lambda: update_task())	
		task2_title = Label(task_frame,text = "Task",fg = "white",bg = '#7E1FFF',font = ('Ariel',30))




		task.grid(row = 0,column = 1,sticky = 'nsew')
		task2_title.grid(row = 0,column = 0,sticky = 'nsew')


		#Time

		time_frame = Frame(rshortcut_frame, bg = Background_Window_Color)
		time_frame.grid(row = 6, column = 0 , sticky = 'nsew')

		time_frame.grid_rowconfigure(0,weight = 1)
		time_frame.grid_columnconfigure(0,weight = 1)

		timelabel = Label(time_frame, text = time.strftime("%A %I:%M %p"),fg = Text_Color,bg = Background_Window_Color, font = ('Ariel',40))

		timelabel.grid(row = 0, column = 0, sticky = 'nsew')


		def datetime_update():
			date['text'] = time.strftime("%dth %B %Y")
			timelabel['text'] = time.strftime("%A %I:%M %p")
			days['text'] = (datetime(2021,2,22) - datetime.now()).days
			timelabel.after(1000,datetime_update)
		datetime_update()


		
		def pandemic_update():
			corona_count = (0,0)
			try:
				coronainfo_obj = requests.get("https://www.worldometers.info/coronavirus/country/india/")
				coronainfo = bs4.BeautifulSoup(coronainfo_obj.text,'html.parser')
				corona_actualinfo = coronainfo.title.getText().split(" ")

				corona_count = (corona_actualinfo[2],corona_actualinfo[5])
				shortcut_covid['text'] = f"Total: {corona_count[0]}    Deaths: {corona_count[1]}"
			except:
				shortcut_covid['text'] = f"You are not connected. Please check your connection"

			
			shortcut_covid.after(1000*60, pandemic_update) #Updates every minute, requests take time to load
		pandemic_update()
		
		def send_notification(header,msg):
			notification.notify(title = header,
				message = msg,
				app_name = 'Omniscient Wizard',
				app_icon = r'C:\Users\91729\Desktop\Omniscient Wizard\Resources\Icons\Omnis.ico')


		def update_current_period():
			msg = 'Calculating'
			current_link = 'Calculating'
			ongoing = 'Ongoing session {}, Join Immediately!'
			nxt = 'Next session {} @ {}'
			day = time.strftime("%A")
			currenttime = datetime.now()
			time_now = time_mark(int(time.strftime("%H")),int(time.strftime("%M")),0)
			#day = 'Monday'
			for i in range(len(Save_Data['timing'])-1):
				current_session = i
				next_session = i + 1

				current_start = Save_Data['timing'][current_session][0]
				current_end = Save_Data['timing'][current_session][1]
				next_start = Save_Data['timing'][next_session][0]
				if day == 'Sunday':
					pass
				else:
					if time_now < current_start:
						startdatetime = datetime.combine(date_.today(),current_start)
						#print((startdatetime - currenttime).seconds)
						subj = Save_Data["raw_timetable"][day][next_session]
						if (startdatetime - currenttime).seconds == int(self.notification_timing)*60 and Save_Data['user_preferences']['notifications']['sn_enabled']:
							send_notification(f"Session in {self.notification_timing} minutes!",f"You have a {subj} session in {self.notification_timing} minutes. Join the session immediately!")
						
						msg = nxt.format(subj,current_start.strftime("%I:%M %p"))
						current_link = Links[subj]
						break			
					if current_start <= time_now < current_end:
						subj = Save_Data["raw_timetable"][day][current_session]
						msg = ongoing.format(subj)
						current_link = Links[subj]
						break
					elif current_end < time_now < next_start:
						if next_session  > len(Save_Data['timing']) - 2:
							pass
						else:
							nextstartdatetime = datetime.combine(date_.today(),next_start)
							#print(currenttime,nextstartdatetime)
							#print((nextstartdatetime - currenttime).seconds)
							subj = Save_Data["raw_timetable"][day][next_session]
							if (nextstartdatetime - currenttime).seconds == int(self.notification_timing)*60 and Save_Data['user_preferences']['notifications']['sn_enabled']:
								send_notification(f"Session in {self.notification_timing} minutes!",f"You have a {subj} session in {self.notification_timing} minutes. Join the session immediately!")
							
							msg = nxt.format(subj,next_start.strftime("%I:%M %p"))
							current_link = Links[subj]
							break
			else:
				msg = "You are done with all sessions today!"
				current_link = 'DISABLED'

			shortcut_session['text'] = msg

			if current_link != 'DISABLED':
				shortcut_session['command'] = lambda: webbrowser.open(current_link)
			else:
				shortcut_session['command'] = lambda: messagebox.showinfo(title = 'No session to open', message = 'You are done with all sessions today')

			shortcut_session.after(1000,update_current_period)

		update_current_period()




class Study(Frame):

	def __init__(self,parent, controller):
		Frame.__init__(self,parent)
		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure(0,weight = 1)

		tab_message = "Please select subject to study"
		subs = Label(self,text = tab_message, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
		subs.grid(row = 0, column = 0, sticky = "nsew")
		sub_frame = Frame(self,bg = Background_Window_Color)
		sub_frame.grid(row = 1, column = 0, sticky = 'nsew')

		sub_frame.grid_rowconfigure((0,2,4), weight = 7)
		sub_frame.grid_rowconfigure((1,3,5),weight = 1)
		sub_frame.grid_columnconfigure((0,2), weight = 1)
		sub_frame.grid_columnconfigure(1, weight = 20)

		CHEMISTRY = Button(sub_frame,fg = 'white',bg = "#7EDA9E", text = '🔒 Chemistry (Coming Soon!)', font = ("Helvetica",35), bd = 0)
		CHEMISTRY.grid(row = 4, column = 1 , sticky = 'nsew')

		PHYSICS = Button(sub_frame,fg = 'white',bg = "#FFE346", text = 'Physics', font = ("Helvetica",35), bd = 0)
		PHYSICS.grid(row = 2, column = 1 , sticky = 'nsew')

		MATH = Button(sub_frame,fg = 'white',bg = "#54DBDD", text = 'Mathematics', font = ("Helvetica",35), command = lambda: controller.show_frame("Math"), bd = 0)
		MATH.grid(row = 0, column = 1 , sticky = 'nsew')


class Timetable(Frame):

	def __init__(self,parent, controller):
		Frame.__init__(self,parent)

		self.timetable_widgets = {}

		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure(0,weight = 1)

		tab_message = "Manage your timetable here"
		subs = Label(self,text = tab_message, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
		subs.grid(row = 0, column = 0, sticky = "nsew")
		sub_frame = Frame(self,bg = Background_Window_Color)
		sub_frame.grid(row = 1, column = 0, sticky = 'nsew')

		sub_frame.grid_columnconfigure((0,2),weight = 1)
		sub_frame.grid_columnconfigure(1,weight = 20)
		sub_frame.grid_rowconfigure((0,2),weight = 1)
		sub_frame.grid_rowconfigure(1,weight = 20)

		table_base = Frame(sub_frame,bg = Background_Window_Color)
		table_base.grid(row = 1, column = 1, sticky = 'nsew')

		table_base.grid_rowconfigure(tuple(range(len(Days_In_A_Week) + 1)),weight = 1)
		table_base.grid_columnconfigure(tuple(range(Max_Sessions_Per_Day + 1)),weight = 1)
		#table_base.grid_propagate(0)

		raw_edit = Image.open('Resources/Icons/edit.png')
		self.edit = ImageTk.PhotoImage(raw_edit)

		edit_button = Button(table_base,bd = 0 , image = self.edit, bg = Background_Window_Color, activebackground = Background_Window_Color, command = lambda: controller.show_frame("Edit_Timetable"))
		edit_button.grid(row = 0 , column = 0 ,sticky = 'nsew')

		#Fill the Days

		for i in range(len(Days_In_A_Week)):
			day = Label(table_base,text = Days_In_A_Week[i],font = ('Helvetica',16),bg = '#817489', fg = 'white',borderwidth = 1, relief = 'solid').grid(column = 0, row = i + 1, sticky = 'nsew',ipadx = 0, ipady = 0)
			Sessions = Save_Data["raw_timetable"][Days_In_A_Week[i]]

			for j in range(Max_Sessions_Per_Day):
				self.timetable_widgets[f"{i}{j}"] = Label(table_base, text = Sessions[j], font = ('Helvetica',16),bg = subject_colorcodes[Options['subject_colorcodes']][Sessions[j]], fg = 'white',borderwidth = 1, relief = 'solid')
				 
				self.timetable_widgets[f"{i}{j}"].grid(column = j + 1, row = i + 1 , sticky = 'nsew')

				
		#print(len(self.timetable_widgets))
		#Fill the Session headers

		for i in range(Max_Sessions_Per_Day):
			session = Label(table_base, text = "{} \n ({}-{})".format(f"Session {i + 1}",Save_Data['timing'][i][0].strftime("%I:%M %p"),Save_Data['timing'][i][1].strftime("%I:%M %p")), font = ('Helvetica',16), bg = '#748985', fg = 'white',borderwidth = 1, relief = 'solid')
			session.grid(row = 0, column = i + 1, sticky = 'nsew')
			self.timetable_widgets[f"H{i}"] = session




class Edit_Timetable(Frame):

	def __init__(self,parent, controller):
		Frame.__init__(self,parent)
		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure(0,weight = 1)

		etimetable_widgets = {}

		tab_message = "Touch the tiles which shall change"
		subs = Label(self,text = tab_message, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
		subs.grid(row = 0, column = 0, sticky = "nsew")
		sub_frame = Frame(self,bg = Background_Window_Color)
		sub_frame.grid(row = 1, column = 0, sticky = 'nsew')

		sub_frame.grid_columnconfigure((0,2),weight = 1)
		sub_frame.grid_columnconfigure(1,weight = 20)
		sub_frame.grid_rowconfigure((0,2),weight = 1)
		sub_frame.grid_rowconfigure(1,weight = 20)

		table_base = Frame(sub_frame,bg = Background_Window_Color)
		table_base.grid(row = 1, column = 1, sticky = 'nsew')

		table_base.grid_rowconfigure(tuple(range(len(Days_In_A_Week) + 1)),weight = 1)
		table_base.grid_columnconfigure(tuple(range(Max_Sessions_Per_Day + 1)),weight = 1)
		#table_base.grid_propagate(0)

		raw_ok = Image.open('Resources/Icons/ok.png')
		self.ok = ImageTk.PhotoImage(raw_ok)

		ok_button = Button(table_base,bd = 0 , image = self.ok, bg = Background_Window_Color, activebackground = Background_Window_Color, command = lambda: controller.show_frame("Timetable"))
		ok_button.grid(row = 0 , column = 0 ,sticky = 'nsew')


		def update_widget(widget_code):
			menu = Toplevel(self)
			menu.title("Select Subject")
			menu.geometry("200x200")
			menu.grab_set()
			options = List_Of_Subjects
			label = Label(menu, text = "Select one of the options below")
			label.grid(row = 0, column = 0)

			x = StringVar()

			def returning_duties(c):
				y = x.get()
				etimetable_widgets[widget_code]["text"] = y
				etimetable_widgets[widget_code]["bg"] = subject_colorcodes[Options['subject_colorcodes']][y]
				controller.frames["Timetable"].timetable_widgets[widget_code]["text"] = y
				controller.frames["Timetable"].timetable_widgets[widget_code]["bg"] = subject_colorcodes[Options['subject_colorcodes']][x.get()]
				Save_Data["raw_timetable"][Days_In_A_Week[int(widget_code[0])]][int(widget_code[1])] = x.get()
				menu.grab_release()
				menu.withdraw()

			options = OptionMenu(menu, x, *options,command = returning_duties)
			options.grid(row = 1,column = 0)

		def update_time(widget_code):
			obj = etimetable_widgets[widget_code]
			menu = Toplevel(self)
			menu.title("Select time for the session")
			menu.geometry("450x150")
			menu.grab_set()

			label = Label(menu, text = "Fix time for your session. This will affect your notification timing")
			label.grid(row = 0, column = 0,columnspan = 3)

			s_label = Label(menu, text = "Start time")
			s_label.grid(row = 1, column = 0)

			s_hour = Spinbox(menu, from_ = 1, to = 12, state = 'readonly')
			s_hour.grid(row = 2, column = 0)

			s_hour_label = Label(menu, text = "hr")
			s_hour_label.grid(row = 2, column = 1)

			s_min_label = Label(menu, text = "min")
			s_min_label.grid(row = 2, column = 3)
			

			s_minute = Spinbox(menu, from_ = 0, to = 59, state = 'readonly')
			s_minute.grid(row = 2, column = 2)

			s_meredian = Spinbox(menu, values = ("A.M","P.M"), state = 'readonly')
			s_meredian.grid(row = 2, column = 4)

			e_label = Label(menu, text = "End time")
			e_label.grid(row = 3, column = 0)

			e_hour_label = Label(menu, text = "hr")
			e_hour_label.grid(row = 4, column = 1)

			e_min_label = Label(menu, text = "min")
			e_min_label.grid(row = 4, column = 3)

			e_hour = Spinbox(menu, from_ = 1, to = 12, state = 'readonly')
			e_hour.grid(row = 4, column = 0)

			e_minute = Spinbox(menu, from_ = 0, to = 59, state = 'readonly')
			e_minute.grid(row = 4, column = 2)

			e_meredian = Spinbox(menu, values = ("A.M","P.M"), state = 'readonly')
			e_meredian.grid(row = 4, column = 4)

			def returning_duties(c = None):

				start_hour = int(s_hour.get())
				start_minute = int(s_minute.get())
				start_meredian = s_meredian.get()

				end_hour = int(e_hour.get())
				end_minute = int(e_minute.get())
				end_meredian = e_meredian.get()

				if start_meredian == "P.M":
					if start_hour == 12:
						pass
					else:
						start_hour += 12
				else:
					pass

				if end_meredian == "P.M":
					if end_hour == 12:
						pass
					else:
						end_hour += 12
				else:
					pass

				start = time_mark(start_hour,start_minute,0)
				end = time_mark(end_hour,end_minute,0)

				if end <= start:
					print("ERROR: End time lesser than Start time!")
				else:
					Save_Data['timing'][int(widget_code[1])] = (start,end)
					i = int(widget_code[1])
					new_text = "{} \n ({}-{})".format(f"Session {i + 1}",Save_Data['timing'][i][0].strftime("%I:%M %p"),Save_Data['timing'][i][1].strftime("%I:%M %p"))
					etimetable_widgets[widget_code]["text"] = new_text
					controller.frames["Timetable"].timetable_widgets[widget_code]["text"] = new_text
					#print(f"Start Time: {s_hour.get()} {s_minute.get()} {s_meredian.get()}, End Time: {e_hour.get()} {e_minute.get()} {e_meredian.get()}")

				menu.grab_release()
				menu.withdraw()

			confirm = Button(menu,text = "Confirm",command = returning_duties)
			confirm.grid(row = 5,column = 3)
			
		#Fill the Days

		for i in range(len(Days_In_A_Week)):
			day = Label(table_base,text = Days_In_A_Week[i],font = ('Helvetica',16),bg = '#817489', fg = 'white',borderwidth = 1, relief = 'solid').grid(column = 0, row = i + 1, sticky = 'nsew',ipadx = 0, ipady = 0)
			Sessions = Save_Data["raw_timetable"][Days_In_A_Week[i]]

			for j in range(Max_Sessions_Per_Day):
				key_pos = f"{i}{j}"
				session = Button(table_base, text = Sessions[j], font = ('Helvetica',16),bg = subject_colorcodes[Options['subject_colorcodes']][Sessions[j]], fg = 'white',borderwidth = 1, relief = 'solid',command = lambda key_pos = key_pos: update_widget(key_pos))
				etimetable_widgets[f"{i}{j}"] = session
				session.grid(column = j + 1, row = i + 1 , sticky = 'nsew')
				#print(f"{i}{j}")
				
		#print(etimetable_widgets)

		#Fill the Session headers

		for i in range(Max_Sessions_Per_Day):
			key_pos = f"H{i}"
			session = Button(table_base, text = "{} \n ({}-{})".format(f"Session {i + 1}",Save_Data['timing'][i][0].strftime("%I:%M %p"),Save_Data['timing'][i][1].strftime("%I:%M %p")), font = ('Helvetica',16), bg = '#748985', fg = 'white',borderwidth = 1, relief = 'solid', command = lambda key_pos = key_pos: update_time(key_pos))
			session.grid(row = 0, column = i + 1, sticky = 'nsew')
			etimetable_widgets[f"H{i}"] = session
		

subjc = {'Chemistry': "#7EDA9E",'Physics': "#FFE346", 'Mathematics': "#54DBDD", 'JEE': "#A23AFF"}
list_of_exams = ['Chemistry','Physics','Mathematics','English','Comp. Sci','JEE']

class Exam_Frame(Frame):
	def __init__(self,parent,date_str,subject,controller,pos,portions = False):
		
		Frame.__init__(self,parent,height = 250, width = 1270)
		self.grid_rowconfigure(0,weight = 1)
		self.grid_columnconfigure((0,1),weight = 1)
		self.grid_columnconfigure(2,weight = 10)
		self.grid_propagate(0)

		self.position = pos

		exam_date = Label(self,width = 10,text = date_str,bg = '#242829',fg = '#FFF580',font = ('Helvetica',20))
		exam_date.grid(row = 0, column = 0 , sticky = 'nsew')

		e_subject = Label(self,width = 10,text = subject,bg = subjc[subject],fg = 'white',font = ('Helvetica',20))
		e_subject.grid(row = 0, column = 1, sticky = 'nsew')

		e_subject.grid_rowconfigure(0, weight = 10)
		e_subject.grid_rowconfigure(1,weight = 1)
		e_subject.grid_columnconfigure(0,weight = 1)
		e_subject.grid_propagate(0)




		portions_ = Text(self,width = 10,bg = '#65706E',fg = 'white',font = ('Helvetica',20),padx = 20)
		portions_.insert(END,portions)
		portions_.configure(state = 'disabled')
		portions_.grid(row = 0, column = 2, sticky = 'nsew')

		x = Button(e_subject,text = "Edit",bg = "#2486F5", fg = 'white',bd = 0, command = lambda: controller.frames["Edit_Exam"].add_data(subject,portions,self,self.position) or controller.show_frame("Edit_Exam"))

		def add_edit(obj):
			x.grid(row = 1, column = 0, sticky = 'nsew')
		def remove_edit(obj):
			x.grid_forget()
			


		e_subject.bind("<Enter>",lambda e: add_edit(e.widget))
		e_subject.bind("<Leave>",lambda e: remove_edit(e.widget))



class Exams(Frame):

	examframes = Save_Data['exam_data']
	frameobjects = []
	frame_reference = {}

	def __init__(self,parent, controller):
		Frame.__init__(self,parent)
		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure(0,weight = 1)
		self.grid_propagate(0)

		self.controller = controller

		tab_message = "Manage your exam timetable here"
		subs = Label(self,text = tab_message, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
		subs.grid(row = 0, column = 0, sticky = "nsew")
		subs.grid_rowconfigure(0,weight = 1)
		subs.grid_columnconfigure(0,weight = 10)
		subs.grid_columnconfigure(1,weight = 1)

		#edit button

		edit = Button(subs, bd = 0, bg = 'black',command = lambda: controller.show_frame("Add_Exam"))
		edit.grid(row = 0, column = 1, sticky = 'nsew')

		sub_frame = ScrolledFrame(self,bg = 'black')
		sub_frame.grid(row = 1, column = 0,sticky = 'nsew')
		sub_frame.bind_arrow_keys(self)
		sub_frame.bind_scroll_wheel(self)


		self.sub_frame = sub_frame.display_widget(Frame)
		self.rearrange()

	def add_exam(self,date,type_,portions):

		date_elements = date.split("/")
		date_ = datetime(month= int(date_elements[0]),day = int(date_elements[1]),year = int(date_elements[2]))
		date_str = date_.strftime("%d %B")

		if len(self.examframes) == 0:
			self.examframes.append([date_,date_str,type_,portions])
		else:
			for i in range(len(self.examframes)):
				print(i)
				print(date_,self.examframes[i][0],self.examframes[i][0] >= date_)
				if self.examframes[i][0] >= date_:
					self.examframes.insert(i,[date_,date_str,type_,portions])
					break
			else:
				self.examframes.insert(i+1,[date_,date_str,type_,portions])

		self.rearrange()

	def rearrange(self):
		if len(self.examframes) == 0:
			self.controller.frames["Home"].shortcut_task['text'] = "No Upcoming exams as of now!"
			no_exams = Label(self.sub_frame,text = "There are no exams as of now! \n Click + to add an upcoming exam!" , bg = 'white', fg = 'grey', font = ("Helvetica",35))
			no_exams.pack(side = "right",fill = "both") 
			self.frameobjects.append(no_exams)
			pass
		else:
			for x in self.frameobjects:
				x.pack_forget()
				del x

			self.controller.frames["Home"].shortcut_task['text'] = f"Next Exam: {Save_Data['exam_data'][0][2]} @ {Save_Data['exam_data'][0][1]}"

			for i in range(len(self.examframes)):
				examf = Exam_Frame(self.sub_frame,date_str = self.examframes[i][1],subject = self.examframes[i][2],portions = self.examframes[i][3],controller = self.controller,pos = i)
				examf.pack(fill = "both", side = "top",expand = True)   
				self.frameobjects.append(examf)

	def remove_exam(self,pos):
		del self.examframes[pos]
		self.rearrange()					

class Add_Exam(Frame):

	def __init__(self,parent, controller, mode = "NEW_ENTRY"):
		Frame.__init__(self,parent)
		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure(0,weight = 1)

		if mode == "NEW_ENTRY":
			tab_message = "Sculpt your mastery's test date here!"
			subs = Label(self,text = tab_message, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
			subs.grid(row = 0, column = 0, sticky = "nsew")
			sub_frame = Frame(self,bg = Background_Window_Color)
			sub_frame.grid(row = 1, column = 0, sticky = 'nsew')
			sub_frame.grid_propagate(0)

			sub_frame.grid_rowconfigure((0,2,4), weight = 1)
			sub_frame.grid_rowconfigure(1,weight = 10)
			sub_frame.grid_rowconfigure(3,weight = 1)
			sub_frame.grid_rowconfigure(5,weight = 100)
			sub_frame.grid_rowconfigure(6,weight = 1)
			sub_frame.grid_columnconfigure((0,2), weight = 1)
			sub_frame.grid_columnconfigure(1, weight = 20)

			time_now = datetime.now()

			cal_title = Label(sub_frame, text = "Select Date of the exam", font = ("Helvetica",20), bg = Background_Window_Color, fg = 'black')
			cal_title.grid(row = 0, column = 1, sticky = 'nsew')

			cal = Calendar(sub_frame, selectmode = "day", year = int(time_now.strftime("%Y")) , month = int(time_now.strftime("%m")),day = int(time_now.strftime("%d")))
			cal.grid(row = 1,column = 1, sticky = 'nsew')

			x = StringVar()

			exam_type = OptionMenu(sub_frame, x , *list_of_exams)
			exam_type.grid(row = 3, column = 1 , sticky = 'nsew')

			type_title = Label(sub_frame, text = "Select type of the exam", font = ("Helvetica",20), bg = Background_Window_Color, fg = 'black')
			type_title.grid(row = 2, column = 1, sticky = 'nsew')

			portion_entry = Text(sub_frame)
			portion_entry.grid(row = 5, column = 1, sticky = 'nsew')

			portion_title = Label(sub_frame, text = "Type your exam portions here (Will be displayed as such)", font = ("Helvetica",20), bg = Background_Window_Color, fg = 'black')
			portion_title.grid(row = 4, column = 1, sticky = 'nsew')

			add = Button(sub_frame, text = "Add Exam", font = ("Helvetica",10), bg = Background_Window_Color, fg = 'black', command = lambda: controller.frames["Exams"].add_exam(cal.get_date(),x.get(),portion_entry.get("1.0",END)) or controller.show_frame("Exams"))
			add.grid(row = 6, column = 1, sticky = 'nsew')

class Edit_Exam(Frame):

	def __init__(self,parent, controller, mode = "EDIT_ENTRY"):
		Frame.__init__(self,parent)
		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure(0,weight = 1)

		if mode == "EDIT_ENTRY":

			tab_message = "Edit your test date here!"

			subs = Label(self,text = tab_message, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
			subs.grid(row = 0, column = 0, sticky = "nsew")

			subs.grid_columnconfigure(0,weight = 20)
			subs.grid_columnconfigure(1,weight = 1)
			subs.grid_rowconfigure(0, weight = 1)

			def remove_prompt():
				ans = messagebox.askquestion("Delete Exam","Do you wish to delete the exam you have selected?")

				if ans == "yes":
					self.to_remove.grid_forget()
					controller.frames["Exams"].remove_exam(self.to_remove_pos)
					controller.show_frame("Exams")
				else:
					pass



			remove_button = Button(subs,text = "X", font = ("Aerial",35,'bold'),bg = 'red',fg = 'white',command = lambda: remove_prompt())
			remove_button.grid(row = 0, column = 1, sticky = 'nsew')

			sub_frame = Frame(self,bg = Background_Window_Color)
			sub_frame.grid(row = 1, column = 0, sticky = 'nsew')
			sub_frame.grid_propagate(0)

			sub_frame.grid_rowconfigure((0,2,4), weight = 1)
			sub_frame.grid_rowconfigure(1,weight = 10)
			sub_frame.grid_rowconfigure(3,weight = 1)
			sub_frame.grid_rowconfigure(5,weight = 100)
			sub_frame.grid_rowconfigure(6,weight = 1)
			sub_frame.grid_columnconfigure((0,2), weight = 1)
			sub_frame.grid_columnconfigure(1, weight = 20)

			time_now = datetime.now()

			cal_title = Label(sub_frame, text = "Edit Date of the exam", font = ("Helvetica",20), bg = Background_Window_Color, fg = 'black')
			cal_title.grid(row = 0, column = 1, sticky = 'nsew')

			self.cal = Calendar(sub_frame, selectmode = "day", year = int(time_now.strftime("%Y")) , month = int(time_now.strftime("%m")),day = int(time_now.strftime("%d")))
			self.cal.grid(row = 1,column = 1, sticky = 'nsew')

			self.x = StringVar()

			exam_type = OptionMenu(sub_frame, self.x , *list_of_exams)
			exam_type.grid(row = 3, column = 1 , sticky = 'nsew')

			type_title = Label(sub_frame, text = "Edit type of the exam", font = ("Helvetica",20), bg = Background_Window_Color, fg = 'black')
			type_title.grid(row = 2, column = 1, sticky = 'nsew')

			self.portion_entry = Text(sub_frame)
			self.portion_entry.grid(row = 5, column = 1, sticky = 'nsew')

			portion_title = Label(sub_frame, text = "Edit your exam portions here (Will be displayed as such)", font = ("Helvetica",20), bg = Background_Window_Color, fg = 'black')
			portion_title.grid(row = 4, column = 1, sticky = 'nsew')

			def edit_changes():
				self.to_remove.grid_forget()
				controller.frames["Exams"].remove_exam(self.to_remove_pos)
				controller.frames["Exams"].add_exam(self.cal.get_date(),self.x.get(),self.portion_entry.get("1.0",END))
				controller.show_frame("Exams")

			add = Button(sub_frame, text = "Apply changes", font = ("Helvetica",10), bg = Background_Window_Color, fg = 'black', command = lambda: edit_changes())
			add.grid(row = 6, column = 1, sticky = 'nsew')



	def add_data(self,subject,portions,obj,pos):
		self.portion_entry.delete("1.0",END)
		self.portion_entry.insert(END,portions)
		self.x.set(subject)
		self.to_remove = obj
		self.to_remove_pos = pos


class Mathematics(Frame):

	def __init__(self,parent, controller):
		Frame.__init__(self,parent)
		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure(0,weight = 1)

		tab_message = "Please select topic to study in mathematics"
		subs = Label(self,text = tab_message, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
		subs.grid(row = 0, column = 0, sticky = "nsew")
		sub_frame = Frame(self,bg = Background_Window_Color)
		sub_frame.grid(row = 1, column = 0, sticky = 'nsew')

		sub_frame.grid_rowconfigure((0,2,4), weight = 7)
		sub_frame.grid_rowconfigure((1,3,5),weight = 1)
		sub_frame.grid_columnconfigure((0,2), weight = 1)
		sub_frame.grid_columnconfigure(1, weight = 20)

		#raw_trig = Image.open('Resources/Backgrounds/Trigonometry_bg.jpg')
		#self.trig = ImageTk.PhotoImage(raw_trig)

		Matrices = Button(sub_frame,fg = 'white',bg = "#7EDA9E", text = 'Matrices', font = ("Helvetica",35),bd = 0,command = lambda: controller.show_frame("Math_Matrices"))
		Matrices.grid(row = 0, column = 1 , sticky = 'nsew')

		Trigonometry = Label(sub_frame,fg = 'white',bg = "#FFE346", text = '🔒 Trigonometry', font = ("Helvetica",35), bd = 0, compound = "center")
		Trigonometry.grid(row = 4, column = 1 , sticky = 'nsew')

		Determinants = Label(sub_frame,fg = 'white',bg = "#54DBDD", text = '🔒 Determinants', font = ("Helvetica",35), bd = 0)
		Determinants.grid(row = 2, column = 1 , sticky = 'nsew')

class Math_Matrices(Frame):

	def __init__(self,parent, controller):
		Frame.__init__(self,parent)
		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure(0,weight = 1)

		tab_message = "Choose the mode of learning"
		subs = Label(self,text = tab_message, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
		subs.grid(row = 0, column = 0, sticky = "nsew")
		sub_frame = Frame(self,bg = Background_Window_Color)
		sub_frame.grid(row = 1, column = 0, sticky = 'nsew')

		sub_frame.grid_rowconfigure((0,2,4), weight = 7)
		sub_frame.grid_rowconfigure((1,3,5),weight = 1)
		sub_frame.grid_columnconfigure((0,2), weight = 1)
		sub_frame.grid_columnconfigure(1, weight = 20)

		ILE = Button(sub_frame,fg = 'white',bg = "#64676B", text = 'Matrices: Integrated Learning Environment', font = ("Helvetica",35),bd = 0,command = lambda: controller.show_frame("MatricesILE"))
		ILE.grid(row = 0, column = 1 , sticky = 'nsew')

		Tutor = Label(sub_frame,fg = 'white',bg = "#64676B", text = 'Matrices: Tutor', font = ("Helvetica",35), bd = 0, compound = "center")
		Tutor.grid(row = 2, column = 1 , sticky = 'nsew')

		Concepts = Label(sub_frame,fg = 'white',bg = "#64676B", text = '🔒 Matrices: Concepts to Master', font = ("Helvetica",35), bd = 0, compound = "center")
		Concepts.grid(row = 4, column = 1 , sticky = 'nsew')


class Math_Matrices_ILE(Frame): #OW Mains

	def __init__(self,parent, controller):
		Frame.__init__(self,parent)
		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure(0,weight = 1)

		tab_message = "Matrices Integrated Learning Environment"
		subs = Label(self,text = tab_message, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
		subs.grid(row = 0, column = 0, sticky = "nsew")
		sub_frame = Frame(self,bg = Background_Window_Color)
		sub_frame.grid(row = 1, column = 0, sticky = 'nsew')

		sub_frame.grid_rowconfigure(2, weight = 4)
		sub_frame.grid_rowconfigure(4,weight = 2)
		sub_frame.grid_rowconfigure((0,1,3,5),weight = 1)
		sub_frame.grid_columnconfigure((0,2), weight = 1)
		sub_frame.grid_columnconfigure(1, weight = 20)
		sub_frame.grid_propagate(0)

		def execute_command():
			Display['state'] = 'normal'
			Display.delete('1.0',END)
			cmd = Input.get()

			def execute_user_input(input_):
				try:
					_a = eval(input_)
					print(Explanation_Result['value'])
					return Explanation_Result['value']
				except:
					return "Invalid Syntax. Please Check your statement/ Matrix Name"

			result = execute_user_input(cmd)
			
			Display.insert(END,str(result))
			Display['state'] = 'disabled'

		def erase():
			Display['state'] = 'normal'
			Display.delete('1.0',END)
			Display['state'] = 'disabled'

		def addmatrix():
			result = simpledialog.askstring(title = "Order of Matrix",prompt = "Enter order of matrix in format rowsXcolumns:",initialvalue = "3X3")
			result_data = result.lower().split('x')

			if result_data[0].isdigit() and result_data[1].isdigit():
				Add_Matrix_Prompt((int(result_data[0]),int(result_data[1])))
			else:
				messagebox.showwarning(title = "Invalid matrix order",message = 'Please enter matrix order in specified format')
				addmatrix()



		Input = Entry(sub_frame,fg = 'white',bg = "#64676B", font = ("Helvetica",30),bd = 0)
		Input.grid(row = 0, column = 1 , sticky = 'nsew')

		Proceed = Button(Input,fg = 'white',bg = 'black', font = ("Helvetica",30,"bold"), text = '+',command = lambda: execute_command())
		Proceed.pack(side = 'right')

		Options = Frame(sub_frame,bg = Background_Window_Color, bd = 0)
		Options.grid(row = 4, column = 1 , sticky = 'nsew')

		Options.grid_rowconfigure(0,weight = 1)
		Options.grid_columnconfigure((0,2),weight = 3)
		Options.grid_columnconfigure(1,weight = 2)

		Clear = Button(Options,bg = 'grey',fg = 'white',text = 'Clear',font = ('Helvetica',20),bd = 0, command = erase)
		Clear.grid(row = 0, column = 2, sticky = 'nsew')

		Register = Button(Options,bg = 'grey',fg = 'white',text = '+ Matrix',font = ('Helvetica',20),bd = 0, command = addmatrix)
		Register.grid(row = 0, column = 0, sticky = 'nsew')

		Display = Text(sub_frame,fg = 'white',bg = "#64676B", font = ("Consolas",15), bd = 0,height = 20,state = 'disabled')
		Display.grid(row = 2, column = 1 , sticky = 'ew')



class Settings(Frame):

	def __init__(self,parent, controller):
		Frame.__init__(self,parent)
		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure(0,weight = 1)

		tab_message = "Cast the laws of working over here!"
		subs = Label(self,text = tab_message, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
		subs.grid(row = 0, column = 0, sticky = "nsew")
		sub_frame = Frame(self,bg = Background_Window_Color)
		sub_frame.grid(row = 1, column = 0, sticky = 'nsew')

		sub_frame.grid_rowconfigure((0,2,4,6,8), weight = 7)
		sub_frame.grid_rowconfigure((1,3,5,7,9),weight = 1)
		sub_frame.grid_columnconfigure((0,2), weight = 1)
		sub_frame.grid_columnconfigure(1, weight = 20)

		Sessions = Button(sub_frame,fg = 'white',bg = "#7EDA9E", text = 'Sessions Management', font = ("Helvetica",20), command = lambda: controller.show_frame("sessions_settings"),bd = 0)
		Sessions.grid(row = 0, column = 1 , sticky = 'nsew')

		Layout = Label(sub_frame,fg = 'white',bg = "#FFE346", text = 'Style and Themes', font = ("Helvetica",20))
		Layout.grid(row = 2, column = 1 , sticky = 'nsew')

		Notifications = Button(sub_frame,fg = 'white',bg = "#54DBDD", text = 'Notifications Management', font = ("Helvetica",20),command = lambda: controller.show_frame("notification_settings"), bd = 0)
		Notifications.grid(row = 4, column = 1 , sticky = 'nsew')

		Premium = Label(sub_frame,fg = 'white',bg = "#FC8B5A", text = 'Upgrade to Premium!', font = ("Helvetica",20,"bold"))
		Premium.grid(row = 6, column = 1 , sticky = 'nsew')

		Logout = Label(sub_frame,fg = 'white',bg = Ribbon_Color, text = 'Logout', font = ("Helvetica",20))
		Logout.grid(row = 8, column = 1 , sticky = 'nsew')


class Notification_Settings(Frame):

	def __init__(self,parent, controller):
		Frame.__init__(self,parent)
		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure(0,weight = 1)

		tab_message = "Cast the laws of working over here!"
		subs = Label(self,text = tab_message, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
		subs.grid(row = 0, column = 0, sticky = "nsew")
		sub_frame = Frame(self,bg = Background_Window_Color)
		sub_frame.grid(row = 1, column = 0, sticky = 'nsew')

		sub_frame.grid_rowconfigure((0,2,4), weight = 1)
		sub_frame.grid_rowconfigure((1,3),weight = 5)
		sub_frame.grid_columnconfigure((0,2,4), weight = 1)
		sub_frame.grid_columnconfigure((1,3), weight = 8)
		sub_frame.grid_propagate(0)

		off = "#FC8B5A"
		on = "#7EDA9E"

		self.sn_enabled = Save_Data['user_preferences']['notifications']['sn_enabled']
		self.en_enabled = Save_Data['user_preferences']['notifications']['en_enabled']

		def sn():
			if self.sn_enabled:
				Session_N['bg'] = off
				Session_N['text'] = 'Session Notifications: OFF'
				Session_N_time['state'] = 'disabled'
				Session_N_time['bg'] = 'grey'
				Save_Data['user_preferences']['notifications']['sn_enabled'] = False
			else:
				Session_N['bg'] = on
				Session_N['text'] = 'Session Notifications: ON'
				Session_N_time['state'] = 'normal'
				Session_N_time['bg'] = Ribbon_Color
				Save_Data['user_preferences']['notifications']['sn_enabled'] = True


		def en():
			if self.en_enabled:
				Exam_N['bg'] = off
				Exam_N['text'] = 'Exam Notifications: OFF'
				Exam_N_time['state'] = 'disabled'
				Exam_N_time['bg'] = 'grey'
				Save_Data['user_preferences']['notifications']['en_enabled'] = False

			else:
				Exam_N['bg'] = on
				Exam_N['text'] = 'Exam Notifications: ON'
				Exam_N_time['state'] = 'normal'
				Exam_N_time['bg'] = Ribbon_Color
				Save_Data['user_preferences']['notifications']['en_enabled'] = True


		def init_sn():
			if not self.sn_enabled:
				Session_N['bg'] = off
				Session_N['text'] = 'Session Notifications: OFF'
				Session_N_time['state'] = 'disabled'
				Session_N_time['bg'] = 'grey'
				Save_Data['user_preferences']['notifications']['sn_enabled'] = False
			else:
				Session_N['bg'] = on
				Session_N['text'] = 'Session Notifications: ON'
				Session_N_time['state'] = 'normal'
				Session_N_time['bg'] = Ribbon_Color
				Save_Data['user_preferences']['notifications']['sn_enabled'] = True


		def init_en():
			if not self.en_enabled:
				Exam_N['bg'] = off
				Exam_N['text'] = 'Exam Notifications: OFF'
				Exam_N_time['state'] = 'disabled'
				Exam_N_time['bg'] = 'grey'
				Save_Data['user_preferences']['notifications']['en_enabled'] = False

			else:
				Exam_N['bg'] = on
				Exam_N['text'] = 'Exam Notifications: ON'
				Exam_N_time['state'] = 'normal'
				Exam_N_time['bg'] = Ribbon_Color
				Save_Data['user_preferences']['notifications']['en_enabled'] = True


		self.sn_time = ("10 minutes","5 minutes","2 minutes","1 minute")
		self.en_time = ("2 days","1 day","On the day of exam")


		def update_duration(session_or_exam):
			menu = Toplevel(self)
			menu.title("Select Duration")
			menu.geometry("200x200")
			menu.grab_set()
			options = None

			if session_or_exam:
				options = self.sn_time
			else:
				options = self.en_time


			label = Label(menu, text = "Remind before: ")
			label.grid(row = 0, column = 0)

			x = StringVar()

			def returning_duties(c):
				y = x.get()
				if session_or_exam:
					Session_N_time['text'] = f'Remind Before: {y}'
					z = y.split(' ')
					Save_Data['user_preferences']['notifications']['sn_timing'] = z[0]
					controller.frames['Home'].notification_timing = z[0]
				else:
					z = y.split()
					if z[0].isdigit():
						Exam_N_time['text'] = f'Remind Before: {y}'
						Save_Data['user_preferences']['notifications']['sn_timing'] = z[0]
					else:
						Exam_N_time['text'] = f'Remind on the day of exam'
						Save_Data['user_preferences']['notifications']['sn_timing'] = False
				menu.grab_release()
				menu.withdraw()

			options = OptionMenu(menu, x, *options,command = returning_duties)
			options.grid(row = 1,column = 0)


		Session_N = Button(sub_frame,fg = 'white',bg = off, text = 'Session Notifications: OFF', font = ("Helvetica",20),bd = 0,command = lambda: sn())
		Session_N.grid(row = 1, column = 1 , sticky = 'nsew')

		Session_N_time = Button(sub_frame,fg = 'white',bg = 'grey', text = 'Remind Before: 5 mins', font = ("Helvetica",20),bd = 0, command = lambda: update_duration(True),state = 'normal')
		Session_N_time.grid(row = 1, column = 3 , sticky = 'nsew')

		Exam_N = Button(sub_frame,fg = 'white',bg = off, text = 'Exam Notifications: OFF', font = ("Helvetica",20), bd = 0,command = lambda: en())
		Exam_N.grid(row = 3, column = 1 , sticky = 'nsew')

		Exam_N_time = Button(sub_frame,fg = 'white',bg = "grey", text = 'Remind Before: 2 days', font = ("Helvetica",20), bd = 0, command = lambda: update_duration(False),state = 'normal')
		Exam_N_time.grid(row = 3, column = 3 , sticky = 'nsew')

		def initialize_timings():
			Session_N_time['text'] = f"Remind Before: {Save_Data['user_preferences']['notifications']['sn_timing']} mins"

			x = Save_Data['user_preferences']['notifications']['en_timing']

			if x:
				Exam_N_time['text'] = f"Remind Before: {Save_Data['user_preferences']['notifications']['en_timing']} days"
			else:
				Exam_N_time['text'] = "Remind on the day of exam"
		init_sn()
		init_en()
		initialize_timings()


class Add_Matrix_Prompt(Tk):

	cells = {}
	def __init__(self,dimensions):
		Tk.__init__(self)
		#dimensions given as tuple. 0 - row , 1 - column
		self.grab_set()

		rows = dimensions[0]
		col = dimensions[1]

		Label(self,text = 'ENTER MATRIX ELEMENTS').grid(row = 0, column = 0 , columnspan = 4)

		def add_matrix_to_environment():
			matrix = []
			for i in range(rows):
				ROW = []
				for j in range(col):
					ROW.append(int(self.cells[f"{i}{j}"].get()))
				matrix.append(ROW)
			name_var = name.get()
			if name_var.isalpha():
				Master_Matrix_Data[name.get()] = Matrix(matrix)
				globals().update(Master_Matrix_Data)
				self.grab_release()
				self.withdraw()
			else:
				messagebox.showwarning(title = "Invalid Matrix Name",message = "Please enter a valid matrix name (Must only contain alpha characters)")


		for i in range(rows):
			for j in range(col):
				self.cells[f"{i}{j}"] = Entry(self,width = 5,textvariable = IntVar())
				self.cells[f"{i}{j}"].grid(row = i+1, column = j)

		else:

			la = Label(self,text = "Matrix Name",width = 10)
			la.grid(row = i + 2,column = 0,columnspan = 3)

			name = Entry(self,text = "Name of Matrix",width = 10,textvariable = StringVar())
			name.grid(row = i + 2,column = 2, columnspan= 3)

			add = Button(self,text = "Add Matrix",width = 10, command = add_matrix_to_environment)
			add.grid(row = i + 3,column = 0,columnspan = 3)





class Session_Settings(Frame):

	def __init__(self,parent, controller):
		Frame.__init__(self,parent)
		self.grid_rowconfigure(0,weight = 1)
		self.grid_rowconfigure(1,weight = 15)
		self.grid_columnconfigure(0,weight = 1)

		tab_message = "Write the laws of your sessions over here!"
		subs = Label(self,text = tab_message, font = ("Aerial",35,'bold'), fg = Text_Color,bg = Background_Window_Color)
		subs.grid(row = 0, column = 0, sticky = "nsew")
		sub_frame = Frame(self,bg = Background_Window_Color)
		sub_frame.grid(row = 1, column = 0, sticky = 'nsew')

		sub_frame.grid_rowconfigure((0,2,4), weight = 1)
		sub_frame.grid_rowconfigure((1,3),weight = 5)
		sub_frame.grid_columnconfigure((0,2,4), weight = 1)
		sub_frame.grid_columnconfigure((1,3), weight = 8)
		sub_frame.grid_propagate(0)

		off = "#FC8B5A"
		on = "#7EDA9E"

		self.al_enabled = False

		def automatic_login():
			if self.al_enabled:
				AL['bg'] = off
				AL['text'] = 'Automatic Login: OFF'
				self.al_enabled = False
			else:
				AL['bg'] = on
				AL['text'] = 'Automatic Login: ON'
				self.al_enabled = True

		Session_No = Button(sub_frame,fg = 'white',bg = Ribbon_Color, text = 'Number of Sessions per day', font = ("Helvetica",20),bd = 0,command = lambda: sn())
		Session_No.grid(row = 1, column = 1 , sticky = 'nsew')

		Session_Type = Button(sub_frame,fg = 'white',bg = Ribbon_Color, text = 'Types of Sessions', font = ("Helvetica",20),bd = 0, command = lambda: update_duration(True),state = 'normal')
		Session_Type.grid(row = 1, column = 3 , sticky = 'nsew')

		Session_Links = Button(sub_frame,fg = 'white',bg = Ribbon_Color, text = 'Session Links', font = ("Helvetica",20), bd = 0,command = lambda: en())
		Session_Links.grid(row = 3, column = 1 , sticky = 'nsew')

		AL = Button(sub_frame,fg = 'white',bg = off, text = 'Automatic Login: OFF', font = ("Helvetica",20), bd = 0, command = automatic_login,state = 'normal')
		AL.grid(row = 3, column = 3 , sticky = 'nsew')




#------------------------------------------{App Driver}---------------------------------------------------------------



OW = Omniscient_Wizard()

OW.protocol("WM_DELETE_WINDOW", window_closed)

OW.state('zoomed')

OW.title("Omniscient Wizard v.5.0 (Alpha)")


#----------------------------------------------{Setup Window Definitions}----------------------------------------------------


OW.mainloop()
