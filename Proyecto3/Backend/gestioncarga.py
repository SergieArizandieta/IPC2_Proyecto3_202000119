import xml.etree.ElementTree as ET

def actualizar(data):
    data =  "combinacino"
    return data

def cargarListasSimulacino():
    try:
        ruta = 'data.xml' 
        gestion = ET.parse(ruta)
        root = gestion.getroot()
        
        for Solicitud in root:
            for dte in Solicitud.iter('DTE'):
                for time in dte.iter('TIEMPO'):
                    timepo = (time.text) #guardarfecha
                for reference in dte.iter('REFERENCIA'):
                    referencia = (reference.text)
                for emit in dte.iter('NIT_EMISOR'):
                    emisor = (emit.text) #error
                for recept in dte.iter('NIT_RECEPTOR'):
                    receptor = (recept.text) #error
                for values in dte.iter('VALOR'):
                    valor = (values.text)
                for impues in dte.iter('IVA'):
                    impuesto = (impues.text) #error
                for tot in dte.iter('TOTAL'):
                    total = (tot.text) #error         
        print("\nArchivo Cargado con Exito\n")
    except:
        print("Error")

def cargsads():
        name = ""
        ruta = 'simulacion.xml' 
        gestion = ET.parse(ruta)
        root = gestion.getroot()
        
        for Simulacion in root:

            for NombreSimulacion in Simulacion.iter('Nombre'):
                name = (NombreSimulacion.text)
                #print(name)
                
            for ListadoP in Simulacion.iter('ListadoProductos'): 
                for Producto in ListadoP.iter('Producto'): 
                    producto = (Producto.text)

        print("\nArchivo Cargado con Exito\n")