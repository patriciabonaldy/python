""" 
	Autor: Patricia Bonaldy
    
"""
import sys
import signal
import config.env
import common_logging as log


__author__ = "Patricia Bonaldy"
__copyright__ = "Copyright 2019, AFIP"
__credits__ = ["Patricia Bonaldy"]
__license__ = "Private"
__version__ = "0.0.1"
__status__ = "Deveploment"


log.root_logger = log.config_logging(config.env.LOG_PATH, config.env.LOG_FILE_NAME_1, config.env.LOG_LEVEL_INFO)


def getArchivo(rutaFile, permiso):
    archivo = open(rutaFile,permiso)
    return archivo

def leerArchivo(archivo):
    for linea in  archivo.readlines():
        print(linea)

def getLineas(archivo):
    lineas = list()
    archivo.seek(0)
    for linea in  archivo.readlines():
        lineas.append(linea)    
    return lineas

def escribirArchivo(archivo,texto):
    archivo.write(texto+'\n')
    return archivo  


log.root_logger.info('Inicia el proceso:LeerArchivo')

rutaFile = 'C:/repositorio/python/csv_data/ejemplo.csv'
arch = getArchivo(rutaFile,'r+')
leerArchivo(arch)

arch = escribirArchivo(arch,'2795444111,201912,rer35423')
leerArchivo(arch)

listLineas = getLineas(arch)
arch.close

print(listLineas)

log.root_logger.info('Fin del proceso: LeerArchivo')
