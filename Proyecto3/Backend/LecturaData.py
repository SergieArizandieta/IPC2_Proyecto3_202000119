import xml.etree.ElementTree as ET
import re
from Autorizaciones import Autorizasiones,DTE_individual
import collections
import xml.etree.cElementTree as ETS
from tabla import tablas
import webbrowser

Ob_Autorizaciones = []

def LecturaData():
    try:
        global Ob_Autorizaciones

        ruta = 'data.xml' 
        gestion = ET.parse(ruta)
        root = gestion.getroot()
        
       
        for Solicitud in root:
            for dte in Solicitud.iter('DTE'):
                
                Errores = []

                for time in dte.iter('TIEMPO'):
                    timepo = (time.text) #guardarfecha
                    fecha = Lecturafecha(timepo)
                    if fecha != 'NoSeEncontro':
                        print (fecha)
                        CrearData(fecha)
                    else:
                        Errores.append('error')
                       
                        print("errrsdkjasdk")
                    #print(timepo)  

                for reference in dte.iter('REFERENCIA'):
                    referencia = (reference.text).replace(" ","")
                    if validarReferencia(referencia):
                        refRepetida(referencia,fecha)
                        if refRepetida(referencia,fecha):
                            Errores.append('referencia')
                    else:
                        Errores.append('error')
                       
                    #print(referencia)  

                for emit in dte.iter('NIT_EMISOR'):
                    emisor = (emit.text).replace(" ","") #error
                    if ValidarNit(emisor):
                        pass
                    else: 
                        Errores.append('nit_emisor')
                       
                    #ValidarNit(emisor)
                    #print(emisor)

                for recept in dte.iter('NIT_RECEPTOR'):
                    receptor = (recept.text).replace(" ","") #error
                    if ValidarNit(receptor):
                        pass
                    else:
                        Errores.append('nit_receptor')
                      
                    #print(receptor)

                for values in dte.iter('VALOR'):
                    valor = (values.text)
                    if validarNum(valor):
                        valor = float(valor)
                    else:
                        Errores.append('error')
                      
                
                    #print(valor)

                for impues in dte.iter('IVA'):
                    impuesto = (impues.text) #error
                    if validarNum(impuesto):
                        impuesto = float(impuesto)
                        iva = round(valor * 0.12, 2)
                        
                        if impuesto == iva:
                            print("IVA comprobado", iva)
                        else:
                            Errores.append('iva')
                          
                            print("iva malo")
                        #print(impuesto)

                    else: 
                        Errores.append('error')
                        

                for tot in dte.iter('TOTAL'):
                    total = (tot.text) #error 
                    
                    if validarNum(total):
                        total = float(total)
                        TotalValidar = iva + valor

                        if TotalValidar == total:
                           print("total comprobado", total)
                        else:
                            Errores.append('total')
                         
                            print("total malo")
                        #print(total)
                    else:
                        Errores.append('error')
                   
                
                AgregarData(fecha,Errores,referencia,emisor,receptor,valor,impuesto,total)
            
            """if Reconocer:
                
                    print("save DTE")
                else:
                    print("rechazar DTE")"""
                 
        print("\nArchivo Cargado con Exito\n")
    except:
        print("Error")
from lxml import etree


def GenrarSalidaPDF(data):
    global Ob_Autorizaciones
    dataNew = data.split("\n")
    
    arreglo = []
    
    for i in dataNew:
        temp = []
        temp.append(i)
        #print(temp)
        arreglo.append(temp)
    
    tablas(arreglo,'ResumenPorRangos.pdf')
    path = 'ResumenPorRangos.pdf'
    webbrowser.open_new(path)
    

#Genrar archivo salida
def GenrarSalida():
    global Ob_Autorizaciones
    #root = ET.Element("LISTAAUTORIZACIONES")
    #ET.SubElement(root, "AUTORIZACION")
    root = ET.Element("LISTAAUTORIZACIONES")
    
    for i in Ob_Autorizaciones:
        Autorizacion = ET.SubElement(root, "AUTORIZACION")
        print("\n")
        print("Autorizacion")
        print(i.fecha)
        ET.SubElement(Autorizacion, "FECHA").text = str(i.fecha)
        print(i.fact_recibidas)
        ET.SubElement(Autorizacion, "FACTURAS_RECIBIDAS").text = str(i.fact_recibidas)
        print("Errores")
        Errores = ET.SubElement(Autorizacion, "ERRORES")
        print(i.nit_Emisor)
        ET.SubElement(Errores, "NIT_EMISOR").text = str(i.nit_Emisor)
        print(i.nit_Receptor)
        ET.SubElement(Errores, "NIT_RECEPTOR").text = str(i.nit_Receptor)
        print(i.iva)
        ET.SubElement(Errores, "IVA").text = str(i.iva)
        print(i.total)
        ET.SubElement(Errores, "TOTAL").text = str(i.total)
        print(i.ref_duplicada)
        ET.SubElement(Errores, "REFERENCIA_DUPLICADA").text = str(i.ref_duplicada)
        print("Correctas")
        ET.SubElement(Autorizacion, "FACTURAS_CORRECTAS").text = str(i.fact_correctas)
        print(i.fact_correctas)

        
        Emisores = []
        Receptores = []
        for x in i.listado_autorizaiones:
            Emisores.append(x.emisor)
            Receptores.append(x.receptor)
            
            emisions = collections.Counter(Emisores)
            receptions = collections.Counter(Receptores)

        ET.SubElement(Autorizacion, "CANTIDAD_EMISORES").text = str(len(emisions))
        ET.SubElement(Autorizacion, "CANTIDAD_RECEPTORES").text = str(len(receptions))
        print(len(emisions))
        print(len(receptions))
        ListAutorazcion = ET.SubElement(Autorizacion, "LISTADO_AUTORIZACIONES")

        for x in i.listado_autorizaiones:
            aprobacion = ET.SubElement(ListAutorazcion, "APROBACION")
            ET.SubElement(aprobacion, "NIT_EMISOR",ref=x.referencia).text = str(x.emisor)
            ET.SubElement(aprobacion, "CODIGO_APROBACION").text = str(x.Noaprobacion)

    def Bonito(elemento, identificador='  '):
        validar = [(0, elemento)]  

        while validar:
            level, elemento = validar.pop(0)
            children = [(level + 1, child) for child in list(elemento)]
            if children:
                elemento.text = '\n' + identificador * (level+1)  
            if validar:
                elemento.tail = '\n' + identificador * validar[0][0]  
            else:
                elemento.tail = '\n' + identificador * (level-1)  
            validar[0:0] = children 

        
    Bonito(root)
    archio = ET.ElementTree(root) 
    archio.write("./Autorizaciones.xml", encoding='UTF-8')
    xml_str = ElementTree.tostring(root).decode()
    return xml_str
from xml.etree import ElementTree

#agregar dara a fecha
def AgregarData(fecha,Errores,referencia,emisor,receptor,valor,impuesto,total):
    
    global Ob_Autorizaciones
    print(Errores )
    for i in Ob_Autorizaciones:

            if i.fecha == fecha:
                
                if Errores != []:
                    for e in Errores:
                        if e == 'error':
                            pass
                        elif e == 'referencia':
                            i.ref_duplicada += 1
                        elif e == 'nit_emisor':
                            i.nit_Emisor += 1
                        elif e == 'nit_receptor':
                            i.nit_Receptor += 1
                        elif e == 'iva':
                            i.iva += 1
                        elif e == 'total':
                            i.total += 1
                else:
                    print("\n")
                    noAprobacion = str(noAutorizacion(fecha,i.listado_autorizaiones))
                    DTE_unica = DTE_individual(referencia,noAprobacion,emisor,receptor,valor,impuesto,total)
                    i.fact_correctas += 1 
                    i.listado_autorizaiones.append(DTE_unica)  
                break

#Revisar Ref repetida
def refRepetida(ref,fecha):
    global Ob_Autorizaciones
    for i in Ob_Autorizaciones:
            if i.fecha == fecha:
                if i.listado_autorizaiones != []:
                    for x in i.listado_autorizaiones:
                        if ref == x.referencia:
                            return True
                return False

#Formarno Autorizacion
def noAutorizacion(fecha,arreglo):
    try:
   
        cantidadceros = "00000000"
        cantidad  = str(len(arreglo) +1)

        dia  = re.search(r'\d{2}(\/)',fecha).group()
        mes  = re.search(r'(\/)\d{2}(\/)',fecha).group()
        year = re.search(r'(\/)\d{4}',fecha).group()

        dia = dia.replace("/","")
        mes = mes.replace("/","")
        year = year.replace("/","")

        NoAutorizacion = year + mes + dia

        #print("lingitud",len(cantidadceros) - len(cantidad) )

        for i in range (0,len(cantidadceros) - len(cantidad) ):
            NoAutorizacion += "0"
            
        NoAutorizacion += cantidad
        print(NoAutorizacion)

        return NoAutorizacion
        
    except:
        return 'NoSeEncontro'

#llenar autorizacion
def CrearData(fecha):
    encontrado = False
    global Ob_Autorizaciones

    if Ob_Autorizaciones == [] :
        Ob_Autorizaciones.append(Autorizasiones(fecha,1,0,0,0,0,0,0,0,0,[]))
    
        print("Se creo fecha \n" , Ob_Autorizaciones)
    else:
        for i in Ob_Autorizaciones:
            if i.fecha == fecha:
                encontrado = True
                break
        if encontrado:
            i.fact_recibidas += 1
            print("Fecha existe \n", Ob_Autorizaciones)
        else:
            Ob_Autorizaciones.append(Autorizasiones(fecha,1,0,0,0,0,0,0,0,0,[]))
            print("Se creo fecha, No Vacio \n" , Ob_Autorizaciones)

#validar longitud nit
def ValidarNit(nit):
    if len(nit)<=20:
        if validarNum(nit):

            if ValidarNoNit(nit):
                return True
            else:
                return False
        else:
            return False
        #print(len(nit))
        #print(nit)
        
    else:
        return False 

#validar nit
def ValidarNoNit(nit):
    try:
        base = 1 
        sum = 0

        Num_validar  = nit[-1]
        nums_nit = list(nit[0:-1])
        nums_nit.reverse()
        #print(Num_validar)
        #print(nums_nit)
        #print("Nit ", nit)

        for i in nums_nit:
            base += 1
            sum += int(i) * base

        result = sum % 11
        comprobante = 11 - result

        if sum >= 11:
            result = sum % 11
            comprobante = 11 - result

        if comprobante == 10:
            if Num_validar.upper() == 'K':
                print("Nit comprobado")
                return True

        elif comprobante == int(Num_validar):
            print("Nit comprobado",nit )
            return True

        else:
            print("Nit rechazado",nit)
            return False

    except:
        print("Nit rechazado")
        return False

#validar referencia
def validarReferencia(referencia):

    if len(referencia)<=40:
        #print(len(referencia))
        return True
    else:
        return False

#validar sea numero
def validarNum(num):
    try: 
        float(num)
        return True
    except ValueError:
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
   