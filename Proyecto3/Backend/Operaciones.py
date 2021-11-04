import re
from LecturaData import validarNum
import LecturaData as LD
import pandas as pd
from tabla import tablas
import webbrowser

import matplotlib.pyplot as plt

def limpiar():
    LD.Ob_Autorizaciones[:] = []
    print(LD.Ob_Autorizaciones,"Arreglo")

def genrarGRAFPRango(fechaS,FechaF,op):
    try: 
        eje_x = []
        eje_y= []

        fechaInicio = LecturafechaEntrada(fechaS)
        fechaInicio = fechaInicio.replace(" ","")
        fechaFinal = LecturafechaEntrada(FechaF)
        fechaFinal = fechaFinal.replace(" ","")
        op = op.replace(" ","")

        diaIncio = int(fechaInicio[0: 2])
        mesInicio = int(fechaInicio[3: 5])
        yearInicio = int(fechaInicio[6: 10])
    
        diaFinal = int(fechaFinal[0: 2])
        mesFinal = int(fechaFinal[3: 5])
        yearFinal = int(fechaFinal[6: 10])
        data = []
        df = ""
        
        cadena = ""
        
        if op == "Total":
            cadena = "Resumen por fechas y Totales"
        elif op == "SinIva":
            cadena = "Resumen por fechas y Valor sin Iva"
        
        df += cadena + "\n"
    
        for i in LD.Ob_Autorizaciones:
            diaTemp = int(i.fecha[0: 2])
            mesTemp = int(i.fecha[3: 5])
            yearTemp = int(i.fecha[6: 10])

            if diaTemp >= diaIncio and diaTemp <= diaFinal:
                if mesTemp >= mesInicio and mesTemp <= mesFinal:
                    if yearTemp >= yearInicio and yearTemp <= yearFinal:
                        
                    
                        eje_x.append(i.fecha)
                        if i.listado_autorizaiones != []:
                            for x in i.listado_autorizaiones: 
                                if op == "Total":
                                
                                    eje_y.append(x.total)
                                elif op == "SinIva":
                            
                                    eje_y.append(x.valor)

                        else:
                        
                            eje_y.append(0)


        plt.bar(eje_x, eje_y)
        plt.ylabel('Cantidad de Pago')
        plt.xlabel('Fechas ')
        

        plt.title('Resumen de cuentas por rango de: ' + fechaInicio + " a " + fechaFinal + " opcion: " + op)
        plt.savefig('ResumenRango.png')
        plt.close()
        html = ""
        escribir = "<center><h6 class=\"titulos\" ><b> Reporte de resumen de cuentas </b></h6> <br> <img src='ResumenRango.png'>"
        html += htmlInicial + escribir + htmlFinal

   
        
        FileHTML=open("./ResumenRango.HTML","w") 
        FileHTML.write(html) 
        FileHTML.close() 
        path = 'ResumenRango.HTML'
        webbrowser.open_new(path)
        #webbrowser.open("C:/Users/sergi/3D Objects/GitHub/LFP_Proyecto1_202000119/Reportes")
      

    except:
        print("La creación del Reporte falló")
    else:
         print("Se ha creado el Reporte Token" )

def GenerarGrafo(fecha,nit):
    try: 
        global htmlInicial
        global htmlFinal

        html = ""
        fechaNew = LecturafechaEntrada(fecha)
        fechaNew = fechaNew.replace(" ","")
        nit = nit.replace(" ","")

        ivaEmitido= 0
        ivaRecibido= 0

        validacion = False
        
        for i in LD.Ob_Autorizaciones:
            if i.fecha == fechaNew:
                
                if i.listado_autorizaiones != []:
                        for x in i.listado_autorizaiones:
                            if nit == x.emisor:
                                ivaEmitido += x.impuesto
                                validacion = True
                            elif nit == x.receptor:
                                ivaRecibido += x.impuesto
                                validacion = True
                break
        
    
        eje_x = ['Iva Emitido:','Iva Recibido']
        eje_y = [ivaEmitido,ivaRecibido]
            

        plt.bar(eje_x, eje_y)
        

        plt.ylabel('Cantidad de Pago')
        
    
        plt.xlabel('Nit ' + str(nit))
        

        plt.title('Resumen de cuentas del: ' + fechaNew )
        plt.savefig('ResumenNItFecha.png')
        plt.close()
        escribir = "<center><h6 class=\"titulos\" ><b> Reporte de resumen de cuentas </b></h6> <br> <img src='ResumenNItFecha.png'>"
        html += htmlInicial + escribir + htmlFinal

    
        
        FileHTML=open("./ResumenNItFecha.HTML","w") 
        FileHTML.write(html) 
        FileHTML.close() 
        path = 'ResumenNItFecha.HTML'
        webbrowser.open_new(path)
        #webbrowser.open("C:/Users/sergi/3D Objects/GitHub/LFP_Proyecto1_202000119/Reportes")
      

    except:
        print("La creación del Reporte falló")
    else:
         print("Se ha creado el Reporte Token" )

def genrarPDFRango(fechaS,FechaF,op):
    fechaInicio = LecturafechaEntrada(fechaS)
    fechaInicio = fechaInicio.replace(" ","")
    fechaFinal = LecturafechaEntrada(FechaF)
    fechaFinal = fechaFinal.replace(" ","")
    op = op.replace(" ","")

    diaIncio = int(fechaInicio[0: 2])
    mesInicio = int(fechaInicio[3: 5])
    yearInicio = int(fechaInicio[6: 10])
   
    diaFinal = int(fechaFinal[0: 2])
    mesFinal = int(fechaFinal[3: 5])
    yearFinal = int(fechaFinal[6: 10])
    data = []
    df = ""
    
    cadena = ""
    
    if op == "Total":
        cadena = "Resumen por fechas y Totales"
    elif op == "SinIva":
        cadena = "Resumen por fechas y Valor sin Iva"
    
    df += cadena + "\n"
    Encabezados= []
    Data = []
    for i in LD.Ob_Autorizaciones:
        diaTemp = int(i.fecha[0: 2])
        mesTemp = int(i.fecha[3: 5])
        yearTemp = int(i.fecha[6: 10])

        if diaTemp >= diaIncio and diaTemp <= diaFinal:
            if mesTemp >= mesInicio and mesTemp <= mesFinal:
                if yearTemp >= yearInicio and yearTemp <= yearFinal:
                    
                    Encabezados.append(i.fecha )
                    
                    if i.listado_autorizaiones != []:
                        for x in i.listado_autorizaiones: 
                            if op == "Total":
                                Data.append(x.total)
                            
                            elif op == "SinIva":
                                Data.append(x.valor)

                    else:
                        Data.append(0)

    data.append(Encabezados)
    data.append(Data)
                      
    
    tablas(data,'ResumenPorRangos.pdf')
    path = 'ResumenPorRangos.pdf'
    webbrowser.open_new(path)
    
def ResumenPorRango(fechaS,FechaF,op):
    fechaInicio = LecturafechaEntrada(fechaS)
    fechaInicio = fechaInicio.replace(" ","")
    fechaFinal = LecturafechaEntrada(FechaF)
    fechaFinal = fechaFinal.replace(" ","")
    op = op.replace(" ","")
    validacion = False
    #print(fechaInicio)
    #print(fechaFinal)
    #print(op)

    diaIncio = int(fechaInicio[0: 2])
    mesInicio = int(fechaInicio[3: 5])
    yearInicio = int(fechaInicio[6: 10])
   
    diaFinal = int(fechaFinal[0: 2])
    mesFinal = int(fechaFinal[3: 5])
    yearFinal = int(fechaFinal[6: 10])
    
    df = ""
    
    cadena = ""
    
    if op == "Total":
        cadena = "Resumen por fechas y Totales"
    elif op == "SinIva":
        cadena = "Resumen por fechas y Valor sin Iva"
    
    df += cadena + "\n"

    for i in LD.Ob_Autorizaciones:
        diaTemp = int(i.fecha[0: 2])
        mesTemp = int(i.fecha[3: 5])
        yearTemp = int(i.fecha[6: 10])

        if diaTemp >= diaIncio and diaTemp <= diaFinal:
            if mesTemp >= mesInicio and mesTemp <= mesFinal:
                if yearTemp >= yearInicio and yearTemp <= yearFinal:
                    
                    
                    df += i.fecha + ":\t"
                    if i.listado_autorizaiones != []:
                        for x in i.listado_autorizaiones: 
                            if op == "Total":
                                df += str(x.total) + "\n"
                               
                            elif op == "SinIva":
                                df += str(x.valor) + "\n"
                              
                    else:
                        df += str(0) + "\n"
    

    return df

def genrarPDFechaNit(fecha,nit):
    fechaNew = LecturafechaEntrada(fecha)
    fechaNew = fechaNew.replace(" ","")
    nit = nit.replace(" ","")

    ivaEmitido= 0
    ivaRecibido= 0

    validacion = False
    
    for i in LD.Ob_Autorizaciones:
        if i.fecha == fechaNew:
            
            if i.listado_autorizaiones != []:
                    for x in i.listado_autorizaiones:
                        if nit == x.emisor:
                           ivaEmitido += x.impuesto
                           validacion = True
                        elif nit == x.receptor:
                            ivaRecibido += x.impuesto
                            validacion = True
            break
    data = []
    Fecha = []
    Nit = []
    valores = []
    if validacion:
        Fecha.append("Fecha: " + fechaNew)
        Nit.append("Nit: " + str(nit))
        valores.append("Iva Emitido: " + str(ivaEmitido))
        valores.append("Iva Recibido: " + str(ivaRecibido))
        
    else:
        valores.append("No se encontro Fecha o NIt indicado")
    
    data.append(Fecha)
    data.append(Nit)
    data.append(valores)
    tablas(data,'ResumenPorFecha_Nit.pdf')
    path = 'ResumenPorFecha_Nit.pdf'
    webbrowser.open_new(path)
   
def ResumenIVAfechaNIT(fecha,nit):
    fechaNew = LecturafechaEntrada(fecha)
    fechaNew = fechaNew.replace(" ","")
    nit = nit.replace(" ","")

    ivaEmitido= 0
    ivaRecibido= 0

    validacion = False
    
    for i in LD.Ob_Autorizaciones:
        if i.fecha == fechaNew:
            
            if i.listado_autorizaiones != []:
                    for x in i.listado_autorizaiones:
                        if nit == x.emisor:
                           ivaEmitido += x.impuesto
                           validacion = True
                        elif nit == x.receptor:
                            ivaRecibido += x.impuesto
                            validacion = True
            break
    
    if validacion:
        text = "Fecha: " + str(fechaNew) + "\nNit: " + str(nit) + "\nIva Emitido: " + str(ivaEmitido)+ "\nIva Recibido: " + str(ivaRecibido)
    else:
        text = "No se encontro Fecha o NIt indicado"
    
   
    return text

#LeerFecha enviada
def LecturafechaEntrada(fecha):

    try:
        fechas = ""
        arreglo = fecha.split("-")
        arreglo.reverse()
        for i in arreglo:
            fechas += i
            if len(i) == 4:
               pass
            else:
                fechas += "/"
        return fechas
        
    except:
        return 'NoSeEncontro'


htmlInicial = """<!DOCTYPE html>
<html>

<!--Encabezado-->
<head>
<meta charset="UTF-8">
<meta name="name" content="Reporte">
<meta name="description" content="name">
<meta name="keywods" content="python,dos,tres">
<meta name="robots" content="Index, Follow">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="css/styles.css"/>
<title>Reporte</title>
</head>
<!----Curerpo--->
<body>
   """

htmlFinal = """<br><footer style="background-color:white;">Creado por: Sergie Daniel Arizandieta Yol - 202000119</footer>
</center></body>
</html>"""