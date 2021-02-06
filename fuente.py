import psutil as psu
import platform

#Obtengo la lista de todos los procesos que actualmente están corriendo.
process_names = [proc.name() for proc in psu.process_iter()]

#Obtengo el nombre de los usuarios que actualmente estan conectados
users = psu.users()

#Obtengo el nombre del procesador
procesador = platform.processor()

#Obtengo el nombre del sistema operativo
nombreSO = platform.system()

#Obtengo la versión del SO
versionSO = platform.version()