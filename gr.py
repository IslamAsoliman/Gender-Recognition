from tkinter import *
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def gender():
	
	txt1.delete('1.0',END)
	txt2.delete('1.0',END)
	try:
		name=txt.get('1.0',END).strip()
		url = 'https://api.genderize.io/?name=' + str(name)
		html = urllib.request.urlopen(url, context = ctx).read()
		soup = BeautifulSoup(html, 'html.parser')
		data = soup.get_text()
		dect = json.loads(data)
		gender=dect['gender']
		prob=dect['probability']
		#txt1.config(state='normal')
		#txt2.config(state='normal')
		txt1.insert('1.0',gender)
		txt2.insert('1.0',prob)
		#txt1.config(state='DISABLED')
		#txt2.config(state='DISABLED')
	except:
		txt1.delete('1.0',END)
		txt2.delete('1.0',END)
		txt1.insert('1.0',"Unavailable name")
		txt2.insert('1.0',"Unavailable name")
w=Tk()

txt=Text(w ,height=1, width=30)
txt1=Text(w, height=1, width=30)
txt2=Text(w, height=1, width=30)
btn_ok=Button(w,text="Get gender",height=2, width=30,command=gender).grid(row=2,column=1)

txt.grid(row=0,column=1)
txt1.grid(row=4,column=1)
txt2.grid(row=5,column=1)


lbl=Label(w, text="Enter a name").grid(row=0,column=0)
lbl1=Label(w, text="Gender      :").grid(row=4,column=0)
lbl2=Label(w, text="Probability :").grid(row=5,column=0)

w.mainloop()