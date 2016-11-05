# -*- coding: utf-8 -*-
#------------------------------------------------------------
# PalcoTV Parser de TuMarcador.xyz by DarioMO
# Version 0.0.1 (10-09-2016)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info)
# Gracias a las librerías resolvers y media_analyzer de JuarroX (Grupo PalcoTV http://arena.pe.hu/forums/index.php y http://palcotv.blogspot.com.es/)

import os
import xbmcplugin
import xbmc, xbmcgui
import urllib

import sys
import urllib
import urllib2
import re

import xbmcaddon

import plugintools
import requests

from resources.tools.resolvers import *
from resources.tools.media_analyzer import *

playlists = xbmc.translatePath(os.path.join('special://userdata/playlists', ''))
temp = xbmc.translatePath(os.path.join('special://userdata/playlists/tmp', ''))

addonName           = xbmcaddon.Addon().getAddonInfo("name")
addonVersion        = xbmcaddon.Addon().getAddonInfo("version")
addonId             = xbmcaddon.Addon().getAddonInfo("id")
addonPath           = xbmcaddon.Addon().getAddonInfo("path")



parser="[COLOR skyblue][B]TuMarcador  [COLOR orange]Alegre  [COLOR skyblue]v0.0.8[/B][/COLOR]"
autor="[COLOR yellow][B][I]      **** by DarioMO ****[/I][/B][/COLOR]"
url_ref = "http://tumarcador.xyz/"
#url_montada = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=MI_CANAL%26referer='+url_ref
url_montada = 'plugin://plugin.video.live.streamspro/?url=%24doregex%5Bget-m3u8%5D&mode=17&regexs=%7Bu%27get-m3u8%27%3A%20%7B%27expres%27%3A%20u%27%23%24pyFunction%5Cndef%20GetLSProData%28page_data%2CCookie_Jar%2Cm%29%3A%5Cn%5Cn%20import%20requests%5Cn%20import%20re%5Cn%5Cn%20headers%20%3D%20%7B%5C%27User-Agent%5C%27%3A%20%5C%27Mozilla/5.0%20%28X11%3B%20Linux%20i686%3B%20rv%3A44.0%29%20Gecko/20100101%20Firefox/44.0%20Iceweasel/44.0%5C%27%2C%20%5C%27Referer%5C%27%3A%20%5C%27%5C%27%7D%5Cn%5Cn%20source%20%3D%20requests.get%28%5C%27MI_CANAL%5C%27%2C%20headers%3Dheaders%29%5Cn%20streamfn%20%3D%20re.findall%28%5C%27source%3A%20%28.%2A%3F%29%5C%5C%28%5C%27%2C%20source.text%29%5B0%5D%5Cn%20formula1%20%3D%20re.search%28r%5C%27function%20%5C%27%20%2B%20streamfn%20%2B%20%5C%27.%2A%5C%5Cn.%2A%5C%5C%5B%28.%2A%3F%29%5C%5C%5D.join.%2A%3F%5C%5C%2B%20%28.%2A%3F%29.join.%2A%3FById%5C%5C%28%22%28.%2A%3F%29%22%5C%27%2C%20source.text%29%5Cn%20par1%20%3D%20formula1.group%281%29.replace%28%5C%27%5C%5C%22%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%2C%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%5C%5C%5C%5C/%5C%27%2C%20%5C%27/%5C%27%29%5Cn%20prepar2%20%3D%20re.findall%28%5C%27var%20%5C%27%20%2B%20formula1.group%282%29%20%2B%20%5C%27.%2A%3F%5C%5C%5B%28%22.%2A%3F%29%5C%5C%5D%5C%27%2C%20source.text%29%5B0%5D%5Cn%20par2%20%3D%20prepar2.replace%28%5C%27%5C%5C%22%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%2C%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%5C%5C%5C%5C/%5C%27%2C%20%5C%27/%5C%27%29%5Cn%20par3%20%3D%20re.findall%28%5C%27id%3D%5C%27%20%2B%20formula1.group%283%29%20%2B%20%5C%27%3E%28.%2A%3F%29%3C%5C%27%2C%20source.text%29%5B0%5D%5Cn%5Cn%20finalm3u8%3D%20par1%20%2B%20par2%20%2Bpar3%5Cn%20return%20finalm3u8%5Cn%5Cn%27%2C%20%27name%27%3A%20u%27get-m3u8%27%2C%20%27page%27%3A%20None%7D%7D'
#url_montada = 'plugin://plugin.video.live.streamspro/?url=%24doregex%5Bget-m3u8%5D&amp;mode=17&amp;regexs=%7Bu%27get-m3u8%27%3A%20%7B%27expres%27%3A%20u%27%23%24pyFunction%5Cndef%20GetLSProData%28page_data%2CCookie_Jar%2Cm%29%3A%5Cn%5Cn%20import%20requests%5Cn%20import%20re%5Cn%5Cn%20headers%20%3D%20%7B%5C%27User-Agent%5C%27%3A%20%5C%27Mozilla/5.0%20%28X11%3B%20Linux%20i686%3B%20rv%3A44.0%29%20Gecko/20100101%20Firefox/44.0%20Iceweasel/44.0%5C%27%2C%20%5C%27Referer%5C%27%3A%20%5C%27%5C%27%7D%5Cn%5Cn%20source%20%3D%20requests.get%28%5C%27MI_CANAL%5C%27%2C%20headers%3Dheaders%29%5Cn%20streamfn%20%3D%20re.findall%28%5C%27source%3A%20%28.%2A%3F%29%5C%5C%28%5C%27%2C%20source.text%29%5B0%5D%5Cn%20formula1%20%3D%20re.search%28r%5C%27function%20%5C%27%20%2B%20streamfn%20%2B%20%5C%27.%2A%5C%5Cn.%2A%5C%5C%5B%28.%2A%3F%29%5C%5C%5D.join.%2A%3F%5C%5C%2B%20%28.%2A%3F%29.join.%2A%3FById%5C%5C%28%22%28.%2A%3F%29%22%5C%27%2C%20source.text%29%5Cn%20par1%20%3D%20formula1.group%281%29.replace%28%5C%27%5C%5C%22%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%2C%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%5C%5C%5C%5C/%5C%27%2C%20%5C%27/%5C%27%29%5Cn%20prepar2%20%3D%20re.findall%28%5C%27var%20%5C%27%20%2B%20formula1.group%282%29%20%2B%20%5C%27.%2A%3F%5C%5C%5B%28%22.%2A%3F%29%5C%5C%5D%5C%27%2C%20source.text%29%5B0%5D%5Cn%20par2%20%3D%20prepar2.replace%28%5C%27%5C%5C%22%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%2C%5C%27%2C%20%5C%27%5C%27%29.replace%28%5C%27%5C%5C%5C%5C/%5C%27%2C%20%5C%27/%5C%27%29%5Cn%20par3%20%3D%20re.findall%28%5C%27id%3D%5C%27%20%2B%20formula1.group%283%29%20%2B%20%5C%27%3E%28.%2A%3F%29%3C%5C%27%2C%20source.text%29%5B0%5D%5Cn%5Cn%20finalm3u8%3D%20par1%20%2B%20par2%20%2Bpar3%5Cn%20return%20finalm3u8%5Cn%5Cn%27%2C%20%27name%27%3A%20u%27get-m3u8%27%2C%20%27page%27%3A%20None%7D%7D'
                     

url = "http://tumarcador.xyz"

guia = "https://www.cubbyusercontent.com/pl/Guia_Marcador.txt/_4eb6780a4edc43c7879f6140c019b236"

fich_hora = xbmc.translatePath(os.path.join('special://userdata/addon_data/plugin.video.palcotv/horario_tumarcador.txt'))
def tumarcador0(params):
	###################################################################### DMO ######################################################################
	mi_version = ["2016","10","31"]  # OJO!! Cambiar la Version, por supuesto... AQUI Y EN EL FICHERO DE LA NUBE

	r = requests.get("http://pastebin.com/raw/2baqp6N8")

	data = r.content

	fecha = plugintools.find_single_match(data,'tumarcador>(.*?)<')
	ult_version = fecha.split(".")

	hay_nueva = False
	if mi_version[0] <> ult_version[0]:
		hay_nueva = True
	else:
		if mi_version[1] < ult_version[1]:
			hay_nueva = True
		else:
			if mi_version[2] < ult_version[2]:
				hay_nueva = True
				
	if hay_nueva == True:
		titu = "¡¡¡ATENCION!!!!"
		lin1 = "      Versión [COLOR red]OBSOLETA de TuMarcador[/COLOR] updated by DarioMO"
		lin2 = " Ya tienes disponible la Ultima Versión para poder actualizarlo"
		lin3 = "         [COLOR yellow]Descarga:[/COLOR] [COLOR red][B]http://adf.ly/7448402/nuevo-tumarcador[/COLOR][/B]"
		xbmcgui.Dialog().ok(titu, lin1, lin2, lin3)
	###################################################################### DMO ######################################################################

	ruta_pro = xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.live.streamspro', ''))
	#headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0', "Referer": url}
	r=requests.get(guia)
	data = r.content

	if not os.path.exists(ruta_pro):
		os.makedirs(ruta_pro)  # Si no existe el directorio, LSP nos va a dar error... así q lo creo
	
	logo = "https://pbs.twimg.com/profile_images/1851363673/logo.jpg"
	fondo = "http://www.sportyou.es/blog/wp-content/uploads/2016/09/Neymar-Benzema-Cristiano.jpg"
	
	plugintools.add_item(action="",url="",title="               "+parser+autor,thumbnail="http://imgur.com/l8fKJMB.png",fanart=fondo,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo, fanart=fondo, folder=False, isPlayable=False)
	
	plugintools.add_item(action="zap_marcador",url="",title="[COLOR white][B]- Zapping de Canales -[/COLOR][/B]",thumbnail="http://lafava.com/wp-content/uploads/2015/06/zapping1.jpg",fanart=fondo,folder=True,isPlayable=False)
	plugintools.add_item(action="muestra_guia",url="",title="[COLOR red][B]- Mostrar Guía en Imagenes -[/COLOR][/B]",thumbnail="http://i.imgur.com/BNQwcS6.png",fanart=fondo,folder=True,isPlayable=False)
	plugintools.add_item(action="cambia_hora_marcador",url="",title="[COLOR skyblue][B]- Cambiar Diferencia Horaria -[/COLOR][/B]",thumbnail="http://image.slidesharecdn.com/1esopresentaciontema1-110109052848-phpapp02/95/tema-1-la-tierra-1-eso-28-728.jpg?cb=1294550960",fanart=fondo,folder=True,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo, fanart=fondo, folder=False, isPlayable=False)

	#***********  Control de Diferencias Horarias DarioMO 15-10-16  *******************
	if not os.path.exists(fich_hora):
		diferencia = "00:00"
		file_hora=open(fich_hora, "w+")
		file_hora.write("00:00")
		file_hora.close()
	else:
		file_hora=open(fich_hora, "r")
		diferencia = file_hora.read()
		file_hora.close()
	#***********  Control de Diferencias Horarias DarioMO 15-10-16  *******************

	diferencia = diferencia + ":00"
	dias = plugintools.find_multiple_matches(data,'<dia>(.*?)<fin dia>')

	from datetime import datetime, timedelta

	for item in dias:
		dia = "             [COLOR white]Día: " + plugintools.find_single_match(item,'(.*?)<')
		plugintools.add_item(action="",url="",title=dia,thumbnail=logo, fanart=fondo, folder=False, isPlayable=False)
		
		lineas = plugintools.find_multiple_matches(item,'<linea>(.*?)<fin')
		
		for item2 in lineas:
			linea = item2 + "<"
			hora = plugintools.find_single_match(linea,'<hora>(.*?)<')
			competicion = plugintools.find_single_match(linea,'<competi>(.*?)<')
			partido = plugintools.find_single_match(linea,'<partido>(.*?)<')
			canal = ">" +  plugintools.find_single_match(linea,'<canal>(.*?)<') + "<"
			
			logo_ext = plugintools.find_single_match(linea,'<logo>(.*?)<')

			if len(hora) > 0:
				#***********  Control de Diferencias Horarias DarioMO 15-10-16  *******************
				hora_esp = hora.replace("[COLOR lightblue]","").replace("h[/COLOR]","").strip()
				hora_esp = hora_esp + ":00"  # Añado los segundos
				hora_dif = diferencia + ":00"  # Añado los segundos
				lista_esp = hora_esp.split(":")
				lista_dif = diferencia.replace("-","").split(":")

				esp_hora=int(lista_esp[0])
				esp_minuto=int(lista_esp[1])
				esp_segundo=int(lista_esp[2])

				dif_hora=int(lista_dif[0])
				dif_minuto=int(lista_dif[1])
				dif_segundo=int(lista_dif[2])

				h1 = datetime(2012, 12, 12, esp_hora, esp_minuto, 0)
				
					
				dh = timedelta(hours=dif_hora) 
				dm = timedelta(minutes=dif_minuto)          
				ds = timedelta(seconds=dif_segundo)
				
				
				if "-" in diferencia:  # Hay que restar horas
					resultado1 =h1 - ds
					resultado2 = resultado1 - dm
					resultado = resultado2 - dh
				else:  # Hay que sumar Horas
					resultado1 =h1 + ds
					resultado2 = resultado1 + dm
					resultado = resultado2 + dh

				
				hora="[COLOR lightblue]" + resultado.strftime("%H:%M:%S") + "h[/COLOR]"
				hora = hora.replace(":00h","h")
				#***********  Control de Diferencias Horarias DarioMO 15-10-16  *******************
			
			#if len(canal) > 1:
			canal2 = canal.replace(">" , "").replace("<" , "").replace("-Acestream" , "a-Acestream")
			if len(canal) > 3:  # Hay mas de 1 canal y seguramente acestream 31-10-16
				letrero = "Canales: "
				completa = hora + "   [COLOR white](" + competicion + ") - [/COLOR]" + partido + "    [COLOR white][I][ "+letrero+canal2+" ] [/COLOR][/I]"
				if len(logo_ext) > 0:
					logo = logo_ext

				plugintools.add_item(action="tumarcador_canales",url=canal,title=completa,thumbnail=logo, fanart=fondo, folder=True, isPlayable=False)
				
			else:
				letrero = "Canal: "
			
				canal_regex = canal2

				el_canal = "http://tumarcador.xyz/canal" + canal_regex + ".php"
					
				completa = hora + "   [COLOR white](" + competicion + ") - [/COLOR]" + partido + "    [COLOR white][I][ "+letrero+canal2+" ] [/COLOR][/I]"
				lanzo_spd = url_montada.replace("MI_CANAL", el_canal)
				if len(logo_ext) > 0:
					logo = logo_ext

				plugintools.runAddon(action="runPlugin",url=lanzo_spd,title=completa,thumbnail=logo, fanart=fondo, folder=False, isPlayable=True)
		
				
	return
	



def tumarcador_canales(params):  # 31-10-16
	titulo = params.get("title")
	canal = params.get("url")
	fondo = params.get("fanart")
	logo = params.get("thumbnail")

	## >5 y [COLOR red]5-Acestream[/COLOR]<fin
	canal_normal = plugintools.find_single_match(canal,'>(.*?) y')
	canal_aces = plugintools.find_single_match(canal,'red](.*?)-')
	pagina_aces = "http://tumarcador.xyz/canal" +  canal_aces + "a.php"

	plugintools.add_item(action="",url="",title=titulo,thumbnail=logo,fanart=fondo,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo, fanart=fondo, folder=False, isPlayable=False)

	r=requests.get(pagina_aces)
	data = r.content
	
	#Busco los 2 enlaces aces... el m3u8 y el acestream
	m3u8 = plugintools.find_single_match(data,'file: "(.*?)"')
	aces = "acestream://" + plugintools.find_single_match(data,'acestream://(.*?)"')

	el_canal = "http://tumarcador.xyz/canal" + canal_normal + ".php"
	lanzo_spd = url_montada.replace("MI_CANAL", el_canal)
	
	url_montada2 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+m3u8+'%26referer=http://tumarcador.xyz/'
	url_montada3 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+aces+'%26referer=http://tumarcador.xyz/'
	
	plugintools.runAddon(action="runPlugin",url=lanzo_spd,title="[COLOR white]-Ver en Canal "+canal_normal+"[/COLOR]",thumbnail=logo, fanart=fondo, folder=False, isPlayable=True)
	plugintools.add_item(action="runPlugin",url=url_montada3,title="[COLOR red]-Ver en Canal "+canal_aces+"a   Formato Acestream[/COLOR]",thumbnail=logo,fanart=fanart,folder=False,isPlayable=True)
	plugintools.add_item(action="runPlugin",url=url_montada2,title="[COLOR blue]-Ver en Canal "+canal_aces+"a   Formato m3u8[/COLOR]",thumbnail=logo,fanart=fanart,folder=False,isPlayable=True)



	
	
	


	
	
def cambia_hora_marcador(params):

	if not os.path.exists(fich_hora):
		diferencia = "00:00"
		file_hora=open(fich_hora, "w+")
		file_hora.write("00:00")
		file_hora.close()
	else:
		file_hora=open(fich_hora, "r")
		diferencia = file_hora.read()
		file_hora.close()

	pide = plugintools.keyboard_input(diferencia, 'Introduzca Diferencia (con [COLOR red]Signo Menos[/COLOR] si son a Disminuir) [COLOR green]XX:XX[/COLOR]')
	
	if pide <> diferencia:
		file_hora=open(fich_hora, "w+")
		file_hora.write(pide)
		file_hora.close()
		xbmcgui.Dialog().ok( "- Tenga en Cuenta -" , "Para que el cambio tenga efecto en la Guía, tendrá que salir del Parser y volver a entrar." )

	return

	
		
def lanza_marca(params):
	canal = params.get("url")
	fanart = params.get("fanart")
	thumbnail = params.get("thumbnail")
	partido = params.get("extra")
	
	if upper(canal) == "X":
		canal = "1"
	if upper(canal) == "Y":
		canal = "2"
		
	if len(canal) > 1:
		canales = canal.split(", ")
		titu = partido + "  en canal "
		for i in range(len(canales)):
			linea = "- ver " + titu + canales[i-1]
			lanzo_spd = url_montada.replace("MI_CANAL", canales[i-1])
			plugintools.log("*************Canal: "+canales[i-1]+"**************")
			plugintools.runAddon(action="runPlugin",url=lanzo_spd,title=partido,thumbnail=logo, fanart=fondo, folder=False, isPlayable=True)
	else:
		linea = "- ver " + titu + canal
		lanzo_spd = url_montada.replace("MI_CANAL", canal)
		plugintools.log("*************Canal: "+canal+"**************")
		plugintools.runAddon(action="runPlugin",url=lanzo_spd,title=partido,thumbnail=logo, fanart=fondo, folder=False, isPlayable=True)
		
	


def zap_marcador(params):
	fondo = params.get("fanart")
	logo = params.get("thumbnail")
	r=requests.get(url)
	data = r.content

	plugintools.add_item(action="",url="",title="               [COLOR skyblue][B]Zapping de "+parser+autor,thumbnail=logo,fanart=fondo,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo, fanart=fondo, folder=False, isPlayable=False)
	

	canales = plugintools.find_single_match(data,'dropdown-menu">(.*?)</ul>')  # Cojo el bloque de canales
	cada_canal = plugintools.find_multiple_matches(canales,'href=(.*?)/a>')  # Separo todos los canales y los monto en su url
				
	#Los saco a pantalla
	for item in cada_canal:
		canal_url = plugintools.find_single_match(item,'"(.*?)"')
		nombre_canal = plugintools.find_single_match(item,'">(.*?)<')
		titulo = "[COLOR aqua]- Ver el " + nombre_canal + "[/COLOR]"

		el_canal = "http://tumarcador.xyz/" + canal_url
		lanzo_spd = url_montada.replace("MI_CANAL", el_canal)
		
		#Montamos la línea.
		plugintools.runAddon(action="runPlugin",url=lanzo_spd,title=titulo,thumbnail=logo,fanart=fondo,folder=False,isPlayable=True)

	canales = plugintools.find_single_match(data,'Canales AceStream(.*?)</ul>')  # Cojo el bloque de canales Acestream
	cada_canal = plugintools.find_multiple_matches(canales,'href=(.*?)/a>')  # Separo todos los canales y los monto en su url
				
	#Los saco a pantalla
	for item in cada_canal:
		canal_url = plugintools.find_single_match(item,'"(.*?)"')
		nombre_canal = plugintools.find_single_match(item,'">(.*?)<')
		titulo = "[COLOR aqua]- Ver el " + nombre_canal + "a  [COLOR red][I](Acestream)[/I][/COLOR]"

		el_canal = "http://tumarcador.xyz/" + canal_url
		#lanzo_spd = url_montada.replace("MI_CANAL", el_canal)
		
		#Montamos la línea.
		#plugintools.runAddon(action="runPlugin",url=lanzo_spd,title=titulo,thumbnail=logo,fanart=fondo,folder=False,isPlayable=True)
		plugintools.add_item(action="saca_acestream",url=el_canal,title=titulo,thumbnail=logo, fanart=fondo, folder=True, isPlayable=False)





def saca_acestream(params):		
	url = params.get("url")
	titulo = params.get("title")
	fondo = params.get("fanart")
	logo = params.get("thumbnail")
	
	

	r=requests.get(url)
	data = r.content

	plugintools.add_item(action="",url="",title="          "+titulo.replace("-",""),thumbnail=logo,fanart=fondo,folder=False,isPlayable=False)
	plugintools.add_item(action="",url="",title="",thumbnail=logo, fanart=fondo, folder=False, isPlayable=False)

	#Busco los 2 enlaces aces... el m3u8 y el acestream
	m3u8 = plugintools.find_single_match(data,'file: "(.*?)"')
	aces = "acestream://" + plugintools.find_single_match(data,'acestream://(.*?)"')

	url_montada2 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+m3u8+'%26referer=http://tumarcador.xyz/'
	url_montada3 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url='+aces+'%26referer=http://tumarcador.xyz/'
	
	plugintools.add_item(action="runPlugin",url=url_montada3,title="[COLOR red]-Ver en Formato Acestream[/COLOR]",thumbnail=logo,fanart=fanart,folder=False,isPlayable=True)
	plugintools.add_item(action="runPlugin",url=url_montada2,title="[COLOR blue]-Ver en Formato m3u8[/COLOR]",thumbnail=logo,fanart=fanart,folder=False,isPlayable=True)

	
		
		
		

def muestra_guia(params):
	fanart = params.get("fanart")
	logo = params.get("thumbnail")

	r=requests.get(url)
	data = r.content
	logo = "http://i.imgur.com/BNQwcS6.png"

	#cada_guia = plugintools.find_multiple_matches(data,'div class="col-(.*?)</div>')  # Hay días que pone mas de una Imagen para la guia
	cada_guia = plugintools.find_multiple_matches(data,'<img height="(.*?)/>')  # Hay días que pone mas de una Imagen para la guia

	i = 0
	for item in cada_guia:
		imagenes = plugintools.find_multiple_matches(item,'src="(.*?)"')
		for item2 in imagenes:
			if len(item2) > 0:
				i = i + 1
				plugintools.add_item(action="lanza_imagen",url=item2,title="-Ver Guía "+str(i),thumbnail=logo,fanart=fanart,folder=True,isPlayable=False)
				
	return

def lanza_imagen(params):
	imagen = params.get("url")
	
	ACTION_PREVIOUS_MENU = 10
	ACTION_SELECT_ITEM = 7
	ACTION_PARENT_DIR = 9
	class MyClass(xbmcgui.Window):
		def __init__(self):
			xbmcgui.Window.__init__(self)
			self.addControl(xbmcgui.ControlImage(0,0,1280,720, imagen))
			self.strActionInfo = xbmcgui.ControlLabel(100, 200, 200, 200, "", "font13", "0xFFFF00FF")
			self.addControl(self.strActionInfo)
			self.strActionInfo.setLabel("")

	mydisplay = MyClass()
	mydisplay.doModal()
	del mydisplay

	return

			
	

def lanza_marca(params):
	lanzame = 'PlayMedia(' + params.get("url") + ')'

	plugintools.log("********LANZO: "+lanzame+"**************")    

	xbmc.executebuiltin(lanzame)
	
	
	
	
