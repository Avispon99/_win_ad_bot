import exe_bot
import random, re, time




def rand(item):
	if type(item) is list: 
		x=random.randint(0, len(item)-1)
		#print('rand-> len')
	else:
		x=random.randint(0, item)
		#	print('rand-> int')
	return x


def modifi_t(titulo): # receiv tit_var as titulo
	ti_mo =titulo #En necesario actualizar el textro durante cada pasao del proceso para que regex lo añada correctamente  
	#print('\ntimo before\n')#<<
	#print(ti_mo)#<<
	#concatenar posible caracter aleatorio al final
	spc = ' ' if rand(1) == 1 else '' # spe puede ser un espacio o un nulo dependiendo de rand(1) 
	ti_mo = ti_mo + spc + char[rand(char)] #<<
	#print('\n\ntimo char:\n')#<< 
	#print(ti_mo)#<<

	
	#First Mayus o First Minus
	first_mayus=rand(2)
	#print('\nFirst Mayus\n', first_mayus)#<<

	if first_mayus == 1 or first_mayus == 2: #Posible remplazo a mayus o minus
		ti_mo=re.sub('^'+ti_mo[0], ti_mo[0].upper(), ti_mo)
		#print('\n\ntimo UPPER:\n')#<<
		#print(ti_mo)#<< 
	else:
		
		ti_mo=re.sub('^'+ti_mo[0], ti_mo[0].lower(), ti_mo)	
		#print('\n\ntimo-LOWER\n')<<
		#print(ti_mo)#<<

	#Alternar Mayus o Minus
	f = re.findall(r'(?<=\s)[a-zA-Z]',ti_mo) # retorna lista con los match de letras antecedidas por un espacio

	for i in range(len(f)): # recorre numero de letras halladas antecedidas por un epacio para sustituirlas una por una
		alt_mayus = rand(1) # retorna numero aleatorio entre 0-1
		if alt_mayus == 1: # si alt_mayus es igual a 1 entonces se sustituira la letra por su version en mayuscula
			ti_mo = re.sub(r'(?<=\s)['+f[i]+']', f[i].upper(), ti_mo) # sustituir letra f[i] antecedida por un espacio,  por ella misma pero en mayuscula 
			#print('\n\nPASO:\n')
			#print(ti_mo)
	
	#All Mayus o All Minus 		
	all_mayus = rand(5)
	#print('all:', all_mayus)#<<		
	if all_mayus == 1 : #posiblemente todo en mayus o todo en munus
		print('\nUPPER COMPLETO\n')#<<
		ti_mo = ti_mo.upper()
	elif all_mayus == 0: 
		ti_mo = ti_mo.lower()
		print('\nLOWER completo\n')
	
	#print('\n\nlisto pa entrgar:\n'+ti_mo)
	return ti_mo


def modifi_d(descripcion): #receiv descript_box as description
	pa_mo=descripcion

	#Concatenar si o si aleatorio caracter al principio y al final
	spc = ' ' if rand(1) == 1 else '' # spe puede ser un espacio o un nulo dependiendo de rand(1) 	
	#print('r-',r)#<<
	#print('char-',char[r])#<<
	pa_mo = char[rand(char)] + spc + pa_mo + spc + char[rand(char)]	
	
	#First Mayus o First Minus
	if re.search(r'^[a-zA-Z]', pa_mo):
		print('\n[a-zA-Z]\n')
		mayus=rand(1)
		if mayus==1: #Posible remplazo a mayus o minus  #NOTA SI HAY SIMBOLO AL INICIO ARROJA ERROR!
			pa_mo=re.sub('^'+pa_mo[0], pa_mo[0].upper(), pa_mo)
		else:
			pa_mo=re.sub('^'+pa_mo[0], pa_mo[0].lower(), pa_mo)
	else: print('No inicia letra')
	
	#Posible repeticion de concatenacion de caracter aleatorio pero solo al final
	doble=rand(1)
	
	if doble == 1: 
		pa_mo=pa_mo+char[rand(char)]
		print('Doble')

	return pa_mo





#compprobar que "ti" es distinto a todos loe de la lista "save_t"
def dif_t():
	print('dif_t:  ESTO SE EJCUTO ALGUNA VEZ========')
	ret_t =True 
	if save_t is []: # si lista esta vacia significa que es el original y puede pasar.
		pass
	else:   # De lo contrario comprar "ti" con los elementos almacenados en la lista 
		for i in save_t:
			if i == ti:
				print('\n                                    ti No es original.. NO PASARA\n')
				ret_t = False
	return ret_t

#compprobar que de es distinto a todos loe de la lista save_d
def dif_d():
	ret_d =True 
	if save_d is []:
		pass
	else:
		for i in save_d:
			if i == de:
				ret_d = False
				print('\n                                    de No es original.. NO PASARA\n')
				print('\n'+de)
	return ret_d




"""

log_mail='testmaster1255aa@gmail.com'
log_psw='master1255aa'

url= 'https://www.milanuncios.com/publicar-anuncios-gratis/formulario?c=323'

#titulo ='Elaboracion del tfg /tfm y Tesis Doctoral'
titulo ='Elaboracionn de tesis tfg /tfm'
descripcion='''Te ayudamos Con los problemas academicos que tengas sobre el proyecto final de grado podemos asesorarte con clases particulares
para la elaboracion del guion final del tfg o tfm y tesis doctoral en todas las ramas y todas las universidades tales como:
Ade, Marketinng, Derecho, Economia, Planes de viabilidad o de empresa/negocio, analisis del TIR y BAN, analisis estadistico SPSS,
psicologia, educacion, administracion, ingieneria, informatica entre otros, SPSS, psicologia, educacion, administracion, ingieneria,
informatica entre otros. no dudes de contactar atraves de mesjaes privado correo o WhatsApp sin compromiso'''
nombre='javier martines'
telefono= '692875247'
email='jhonatan.trabajo99@gmail.com'

dic={0:['212.115.44.178',58542,'tdt1RvAi59','VtSlkEIrJt'], 1:['212.115.44.178',58542,'tdt1RvAi59','VtSlkEIrJt'],2:['212.115.44.178',58542,'tdt1RvAi59','VtSlkEIrJt']}
"""
print('SE ASIGNARAN LAS VARIABLES????????????????')
#Global vars
char=['',' ','-','.','..','>','+','.','¨','*','`','``','<','|','°','~','¬','_','','^','#','','','¨',':',',','','',' ',' ','!']
save_t=[]
save_d=[]
ti=''
de=''
print('SE ASIGNARAN LAS VARIABLES????????????????',save_t)


def rout(ck_l,
		var_dic,
		user_var,
		psw_var,
		tit_var,
		name_var,
		descript_box,
		price_var,
		phone_var,
		phone2_var,
		mail_var,
		inter_var,
		rota_var,
		url_var,
		f_url_var,
		loop_var,
		img_var,
		varian_var):
	
	print('ASEGURAR VARIACIONES °--->',varian_var, ' - Typo:',type(varian_var))
	
	#url = 'https://www.myip.com/'
	#path = 'D:\\c_driver\\chromedriver.exe'

	#init var
	path=url_var
	log_url='https://www.milanuncios.com/mis-anuncios'
	print('RUTA BASE:',path)

	#run vars
	dic=var_dic

	#log vars
	log_mail=user_var
	log_psw=psw_var	
	
	#automate vars
	global ti, de, save_t, save_d
	ti=tit_var
	de=descript_box
	precio=price_var
	nombre=name_var
	telefono=phone_var
	telefono2=phone2_var
	email=mail_var
	form_url=f_url_var
	im=img_var
	print('+++----°',save_t)

	if telefono2 == '' or None:
		telefono2=False

	if im == '' or None:
		im=False


	
	save_d=[]
	t=False
	d=False
	add_c=0
	restart=False
	count_ro=0
	c=0
	t=inter_var

	"""
	ti=titulo
	de=descripcion
	save_t=[]
	save_d=[]
	t=False
	d=False
	add_c=0
	restart=False
	count_ro=0
	c=0
	t=0
	"""


	log=ck_l
	ruti=loop_var
	rotation=rota_var

	#Start program
	"""
	log=input('LOGIN? ---> ')
	ruti=input('CICLOS ---> ')
	rotation=input('Rotaciones por ciclo--> ')
	"""
	while 1:
		print('PLAY........................................++++++++..', c,'--->',ruti)
		if c >= int(ruti):
			print("<- C U T ->")
			break


		for ro in dic.keys():

			if c >= int(ruti): break # verify that not exceed the amount of "ciclos" (ruti) in case that the "dic.keys" is greater than "ruti"

			print('Conect with-prox: ', ro)

			PROXY_HOST = dic[ro][0]  # rotating proxy
			PROXY_PORT = dic[ro][1]
			PROXY_USER = dic[ro][2]
			PROXY_PASS = dic[ro][3]

			print(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

			#instance of Driver Bot
			bot = exe_bot.DriverBot(path)

			#Run conection and set proxy
			bot.run(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS, use_proxy=True)

			if log == 1:
				while 1:
					print('try log from routine file..') 
					res=bot.log(log_mail, log_psw, url=log_url)
					if res == True:
						print('succes log from routine***')
						break
					else:
						print('restart log')
						bot.close_bot()
								

			for i in range(int(ruti)):
				print('|-°-|')
				if c > int(ruti): break

				print('AQUI ESTA save_t    <:> ',save_t,'')
				time.sleep(t) # Time of interval
				print('Start loop->')
				
				#Garantizar no repeticion de titulo por comparacion de "save_t" con "ti"
				while 1:
					if save_t == [] or dif_t():
						if restart == True: #Si fueron reiniciadas las listas entonces igual se titulo original se procesa
							print('WHAT DA HELL IS GOING ON!!!!!!')
							ti = modifi_t(tit_var)
							restart=False  #Se reincia nuevamente a "False" para que no intefiera posteriormente
							print('restart---> modifi  ')  
						t=True
						break
					else: 
						ti = modifi_t(tit_var) #Mejor procesar siempre sobre el original para no crar variaciones muy extrañas
						print('else: Modifi')
				

				#Garantizar no repeticion de descripcion por comparacion de "save_d" con "de" 	
				while 1:
					if save_d == [] or dif_d():
						if restart == True: #Si fueron reiniciadas las listas entonces igual se titulo original se procesa
							de = modifi_d(descript_box)
							restart=False # esta linea talvez no sea necesario hacerla nuevamente pero por si acaso	
							print('restart---> modifi_d') 		
						t=True
						break
					else: 
						de = modifi_d(descript_box)
						print('restart---> modifi_d') 
				
				# Asegurarse que "ti" y "de" sean distintos al obtener positivos en sus respectivos ciclos de compraración
				if t or d: #<< NOTA: NO OLVIDAR CAMBIAR POR "and" al finalizar los test. 	
					print('\n<Antes> rastreando deformacion de ((ti)):',ti) 
					bot.automate(ti, de, precio, nombre, telefono, email, im, telefono2 , form_url)
					print('\n<Despues> rastreando deformacion de ((ti)):',ti)
					print('\nLista Save_d:\n', save_t,'\n' )
					print('\n-----<>.. ti actual o Mofificado ..<>-----\n'+ ti+'\n')
					print('\nLista Save_d:\n', save_d,'\n\n  Len: '+str(len(save_d))+'\n\n' )
					print('\n ---< de actual o Mofificado >---\n\n'+ de+'\n')

				save_t.append(ti)
				save_d.append(de)

				if add_c == varian_var: #<< 3 debe replazarse por una variable electiva en su version final
					add_c=0
					save_t=[]
					save_d=[]
					restart=True
					print('Restart <<')
				print('------------------------ -------------------------------->', add_c)	

				add_c+=1
				count_ro+=1
				c+=1
				
				#Restart conection with anoter proxy in case that is complain amount of loops before to neext rotation
				if count_ro == int(rotation):
					count_ro=0
					time.sleep(2)
					bot.close_bot()
					print('xxxxxxxxx change rotation')
					break

				print('FINISH CLICLO')
				print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Total',c,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')	



