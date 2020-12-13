from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image 
import routine


#Window base
root=Tk()
root.title('Milanuncios APP')
root.config( bg="white")

di_prox={}
path_i=None
c=0
pic= "bot_m.jpg"


def start():
	#print('descript:::\n ', descript_box.get('0.0',END).strip())
	
	#start process
	routine.rout(checklog.get(),
			di_prox,
			user_var.get().strip(),
			psw_var.get().strip(),
			tit_var.get().strip(),
			name_var.get().strip(),
			descript_box.get('0.0', END).strip(),
			price_var.get().strip(),
			phone_var.get().strip(),
			phone2_var.get().strip(),
			mail_var.get().strip(),
			inter_var.get(),
			rota_var.get(),
			url_var.get().strip(),
			f_url_var.get().strip(),
			loop_var.get(),
			img_var.get())
	

def img():
	global path_i
	path_o = filedialog.askopenfilename(title = "Open File")
	img_var.set(path_o)

def add_prox(host,port,px_us=None,px_pw=None):
	global c
	global di_prox
	li=[host,port, px_us, px_pw]
	di_prox[c]=li
	c+=1
	host_var.set('')
	port_var.set(0)
	px_us_var.set('')
	px_pw_var.set('')



def button_run():
	filt_l=True
	filt_p=True

	print(di_prox)
	
	#Filter of checkbox
	if checklog.get() == 1 and ( user_var.get() == '' or psw_var.get() == '' ):
		filt_l=False
		error_l=Toplevel()
		Label(error_l,text ='ERROR, FORMULARIO DE LOGIN SIN COMPLETAR', font=(16), pady=15).pack()
		error_l.mainloop()

		raise NameError('End of filt_l') #Overturn(anular) this window
		

		
	if checkpx.get() == 1 and  di_prox == {}:
		filt_p=False
		error_p=Toplevel()
		Label(error_p,text ='SELECCIONASTE PROXY PERO NO AGREGASTE NINGUNO', font=(16), pady=15).pack()
		error_l.mainloop()

		raise NameError('End of filt_p')
		
		

	# if rotation of proxyes is 0, then the value will be the same value of loops, in the same way if checklist of proxy is empty
	if rota_var.get() == 0 or checkpx.get()==0: 
		rota_var.set(loop_var.get())
	print('ROTA SET',rota_var.get())#<<

	# if outcomes of filters are True then continue to the final verify before to start()  
	if filt_l and filt_p: 
		#if loop (ciclos) is higher or equal to rotation(rotacion de proxy) then the process can start, else throw error window
		if loop_var.get() >= rota_var.get():
			start() 
		else:
			T=Toplevel()
			Label(T, text ='ERROR: La Rotacion No puede ser mayor al ciclo!', font=(16)).pack(padx=5, pady = 10)		
			T.mainloop()




#Login Vars
user_var=StringVar()
psw_var=StringVar()

#Proxy Vars
host_var=StringVar()
port_var=IntVar() 
px_us_var=StringVar()
px_pw_var=StringVar()

#Form Vars
tit_var=StringVar()
name_var=StringVar()
phone_var=StringVar()
phone2_var=StringVar()
mail_var=StringVar()
price_var=StringVar()

#var to rotation and interval
inter_var=IntVar()
rota_var=IntVar()

#var img
img_var=StringVar()

#url vars
url_var=StringVar()
url_var.set('D:\chromedriver.exe')
f_url_var=StringVar()

#Loop var
loop_var=IntVar()

#checkvars
checklog=IntVar()
checkpx=IntVar()



#TEMPORAL Test var SET #<<

user_var.set('testmaster1255aa@gmail.com')
psw_var.set('master1255aa')

#Proxy Vars
host_var.set('212.115.44.178')
port_var.set(58542)
px_us_var.set('tdt1RvAi59')
px_pw_var.set('VtSlkEIrJt')

#Form Vars
tit_var.set('Elaboracionn de tesis tfg /tfm')
name_var.set('javier martines')
phone_var.set('692875247')
phone2_var.set('')
mail_var.set('testmaster1255aa@gmail.com')
price_var.set('8')

#var to rotation and interval
inter_var.set(0)
rota_var.set(0)

#var img
img_var.set('')

#url_form vars
f_url_var.set('https://www.milanuncios.com/publicar-anuncios-gratis/formulario?c=323')

#Loop var
loop_var.set(2)




#Window Frames config
	#Frame Login
frame1 = Frame(root, bg="white")
frame1.grid(row = 0, column = 0, padx= 20, pady=20 )

	#Frame Proxy
frame2 = Frame(root, bg="white")
frame2.grid(row = 0, column = 1, padx= 20, pady= 5)

	#Frames Add Form
frame3 = Frame(root, bg="white")
frame3.grid(row = 1, column = 0, padx= 20, pady= 20)

frame4 = Frame(root, bg="white")
frame4.grid(row = 1, column = 1 , padx= 20, pady= 20)

frame5 = Frame(root, bg="white")
frame5.grid(row = 2, columnspan=2 , padx= 20, pady= 20)

	#Frame loops
frame6 = Frame(root, bg="white")
frame6.grid(row = 3, columnspan=2 , padx= 20, pady= 15)

frame6 = Frame(root, bg="white")
frame6.grid(row = 3, columnspan=2 , padx= 20, pady= 15)

frame7 = Frame(root, bg="white")
#frame7.grid(row = 4, column=0 , padx= 20, pady= 15)
frame7.place(x=177, y=585)

 #Frames Button	
frame8 = Frame(root, bg="white")
frame8.grid(row = 5,column=1 , padx= 20, pady= 5)

frame9 = Frame(root,bg='white')
frame9.grid(row = 4, column=1 , padx= 20)




#Login Form
title_log = Label(frame1, text ='LOGIN', font=(16), bg="white")
title_log.grid(row = 0, column = 0, padx= 10, pady= 3)

user_text = Label(frame1, text ='User', font=(16), bg="white")
user_text.grid(row = 1, column = 0, padx= 10, pady= 3)

user_box=Entry(frame1, textvariable=user_var)
user_box.grid(row = 1, column = 1, padx= 10, pady= 3)

psw_text = Label(frame1, text ='Password', font=(16), bg="white")
psw_text.grid(row = 2, column = 0, padx= 10, pady= 3)

psw_box=Entry(frame1, textvariable=psw_var)
psw_box.grid(row = 2, column = 1, padx= 10, pady= 3)


#Proxy Form
title_prox = Label(frame2, text ='ESTABLECER PROXY', font=(16), bg="white")
title_prox.grid(row = 0, column = 0, padx= 10, pady= 3)

title_prox = Button(frame2, text ='Add Proxy', font=(16), command=lambda:add_prox(host_var.get(), port_var.get(), px_us_var.get(), px_pw_var.get()))
title_prox.grid(row = 0, column = 3, padx= 10, pady= 3)

host_text = Label(frame2, text ='Host', font=(16), bg="white")
host_text.grid(row = 1, column = 0, padx= 10, pady= 3)

host_box=Entry(frame2, textvariable=host_var)
host_box.grid(row = 1, column = 1, padx= 10, pady= 3)

port_text = Label(frame2, text ='Port', font=(16), bg="white")
port_text.grid(row = 2, column = 0, padx= 10, pady= 3)

port_box=Entry(frame2, textvariable=port_var)
port_box.grid(row = 2, column = 1, padx= 10, pady= 3)

px_user_text = Label(frame2, text ='Proxy User', font=(16), bg="white")
px_user_text.grid(row = 1, column = 2, padx= 10, pady= 3)

px_user_box=Entry(frame2, textvariable=px_us_var)
px_user_box.grid(row = 1, column = 3 , padx= 10, pady= 3)

px_psw_text = Label(frame2, text ='Proxy Password', font=(16), bg="white")
px_psw_text.grid(row = 2, column = 2, padx= 10, pady= 3)

px_user_box=Entry(frame2, textvariable=px_pw_var)
px_user_box.grid(row = 2, column = 3, padx= 10, pady= 3)


#Form add data
title_add = Label(frame3, text= 'FORMULARIO', font=(16), bg="white")
title_add.grid(row= 0, column= 0, padx=10, pady=3)

tit_add_text = Label(frame3 , text ='Titulo', font=(16), bg="white")
tit_add_text.grid(row = 1, column = 0, padx= 10, pady= 3)

tit_box=Entry(frame3, textvariable=tit_var)
tit_box.grid(row = 1, column = 1, padx= 10, pady= 3)

name_text = Label(frame3 , text ='Nombre', font=(16), bg="white")
name_text.grid(row = 2, column = 0, padx= 10, pady= 3)

name_box=Entry(frame3, textvariable=name_var)
name_box.grid(row = 2, column = 1, padx= 10, pady= 3)

phone_text = Label(frame3 , text ='Telefono', font=(16), bg="white")
phone_text.grid(row = 3, column = 0, padx= 10, pady= 3)

phone_box=Entry(frame3, textvariable=phone_var)
phone_box.grid(row = 3, column = 1, padx= 10, pady= 3)

phone2_text = Label(frame3 , text ='Telefono 2', font=(16), bg="white")
phone2_text.grid(row = 4, column = 0, padx= 10, pady= 3)

phone2_box=Entry(frame3, textvariable=phone2_var)
phone2_box.grid(row = 4, column = 1, padx= 10, pady= 3)

mail_text = Label(frame3 , text ='e-mail', font=(16), bg="white")
mail_text.grid(row = 5, column = 0, padx= 10, pady= 3)

mail_text = Label(frame3 , text ='e-mail', font=(16), bg="white")
mail_text.grid(row = 5, column = 0, padx= 10, pady= 3)

mail_box=Entry(frame3, textvariable=mail_var)
mail_box.grid(row = 5, column = 1, padx= 10, pady= 3)



mail_text = Label(frame4 , text ='Descripción', font=(16), bg="white")
mail_text.grid(row = 0, column = 0, padx= 10, pady= 3)

descript_box= Text(frame4, height=7, width=70)
descript_box.grid(row=1, column=0, padx=10, pady=3)

scroll_1=Scrollbar(frame4,orient='vertical',command=descript_box.yview) #SCROLLS
scroll_1.place(x=498, y=32, height=111)
descript_box.config(yscrollcommand=scroll_1.set)


#Temporal var set #<<
descript_box.insert(END,'''Te ayudamos Con los problemas academicos que tengas sobre el proyecto final de grado podemos asesorarte con clases particulares
para la elaboracion del guion final del tfg o tfm y tesis doctoral en todas las ramas y todas las universidades tales como:
Ade, Marketinng, Derecho, Economia, Planes de viabilidad o de empresa/negocio, analisis del TIR y BAN, analisis estadistico SPSS,
psicologia, educacion, administracion, ingieneria, informatica entre otros, SPSS, psicologia, educacion, administracion, ingieneria,
informatica entre otros. no dudes de contactar atraves de mesjaes privado correo o WhatsApp sin compromiso''')



price_text = Label(frame4 , text ='Precio', font=(16), bg="white")
price_text.grid(row = 2, column = 0, padx= 10, pady= 3)

price_box= Entry(frame4, textvariable=price_var)
price_box.grid(row=3, column=0, padx=10, pady=3)


url_text = Label(frame5 , text ='Intervalo', font=(16), bg="white")
url_text.grid(row = 0, column = 0, padx= 10, pady= 3)

url_box=Entry(frame5, textvariable=inter_var, width=20)
url_box.grid(row = 0, column = 1, padx= 10, pady= 3)

url_text = Label(frame5 , text ='Rotación de proxy', font=(16), bg="white")
url_text.grid(row = 0, column = 2, padx= 10, pady= 3)

url_box=Entry(frame5, textvariable=rota_var, width=20)
url_box.grid(row = 0, column = 3, padx= 10, pady= 3)



#urls
url_text = Label(frame5 , text ='URL', font=(16), bg="white")
url_text.grid(row = 1, column = 0, padx= 10, pady= 3)

url_box=Entry(frame5, textvariable=url_var, width=40)
url_box.grid(row = 1, column = 1, padx= 7, pady= 3)

url_text = Label(frame5 , text ='URL de formulario', font=(16), bg="white")
url_text.grid(row = 1, column = 2, padx= 7, pady= 3)

url_box=Entry(frame5, textvariable=f_url_var, width=40)
url_box.grid(row = 1, column = 3, padx= 10, pady= 5)



#Loop
url_text = Label(frame6, text='Ciclos', font=(16), bg="white")
url_text.grid(row = 0, column = 0, padx= 7, pady= 3)

loop_box= Entry(frame6, textvariable=loop_var)
loop_box.grid(row= 0, column= 1, padx=10, pady=5)


# Load img


Entry(frame7, textvariable=img_var).grid(row=0, column=0, padx=10, pady=1)
Button(frame7, text='Cargar imagen ¬', command=img).grid(row=0, column=1, padx=10, pady=1)

run_button= Label(frame8, bg="white", text='INICIAR',  height=1)
run_button.grid(row= 0, column= 0, padx=10, pady=2)

open_img=Image.open(pic)
resized=open_img.resize((150, 100), Image.ANTIALIAS)
picture=ImageTk.PhotoImage(resized)

#img = ImageTk.PhotoImage(Image.open("jura.jpg"))
img_label=Button(frame9,image=picture, command=button_run).grid(row=0, column=2,padx=10, pady=1) 



checklog.set(1)
Checkbutton(root, text="Login", variable=checklog).place(x=840, y=585)

checkpx.set(1)
Checkbutton(root, text="Proxy", variable=checkpx).place(x=61, y=585)





root.mainloop()
