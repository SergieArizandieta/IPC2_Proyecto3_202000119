import xml.etree.ElementTree as ET
import re

def LecturaData():
    try:

        ruta = 'data.xml' 
        gestion = ET.parse(ruta)
        root = gestion.getroot()
        
        for Solicitud in root:
            for dte in Solicitud.iter('DTE'):

                for time in dte.iter('TIEMPO'):

                    timepo = (time.text) #guardarfecha
                    fecha = Lecturafecha(timepo)
                    if fecha != 'NoSeEncontro':
                        print (fecha)
                    else:
                        print("errrsdkjasdk")
                    #print(timepo)  

                for reference in dte.iter('REFERENCIA'):
                    referencia = (reference.text).replace(" ","")
                    validarReferencia(referencia)
                    #print(referencia)  

                for emit in dte.iter('NIT_EMISOR'):
                    emisor = (emit.text).replace(" ","") #error
                    #ValidarNit(emisor)
                    #print(emisor)

                for recept in dte.iter('NIT_RECEPTOR'):
                    receptor = (recept.text).replace(" ","") #error
                    ValidarNit(receptor)
                    #print(receptor)

                for values in dte.iter('VALOR'):
                    valor = (values.text)
                    #print(valor)

                for impues in dte.iter('IVA'):
                    impuesto = (impues.text) #error
                    #print(impuesto)

                for tot in dte.iter('TOTAL'):
                    total = (tot.text) #error 
                    #print(total)
              
        print("\nArchivo Cargado con Exito\n")
    except:
        print("Error")


#validar nit
def ValidarNit(nit):
    if len(nit)<=20:
        ValidarNoNit(nit)
        #print(len(nit))
        #print(nit)
        return True
    else:
        return False 

def ValidarNoNit(nit):
    pass
#validar referencia
def validarReferencia(referencia):

    if len(referencia)<=40:
        #print(len(referencia))
        return True
    else:
        return False

#lecttura fecha 
def Lecturafecha(fecha):
    try:
        #fecha = "123"
        fecha  = re.search(r'\d{2}(\/)\d{2}(\/)\d{4}',fecha)
        #print(fecha.group())
        return fecha.group()
        
    except:
        return 'NoSeEncontro'
   