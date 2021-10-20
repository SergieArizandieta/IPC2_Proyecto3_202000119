class Autorizasiones (object):
    def __init__(self,fecha,fact_recibidas,nit_Emisor,nit_Receptor,iva,total,ref_duplicada,fact_correctas,cant_Errores,cant_receptores,listado_autorizaiones):
        self.fecha =fecha
        self.fact_recibidas =fact_recibidas
        self.nit_Emisor = nit_Emisor
        self.nit_Receptor = nit_Receptor
        self.iva = iva
        self.total = total
        self.ref_duplicada = ref_duplicada
        self.fact_correctas =fact_correctas
        self.cant_Errores = cant_Errores
        self.cant_receptores =cant_receptores
        self.listado_autorizaiones =listado_autorizaiones

class listado_autorizaiones (object):
    def __init__(self,referencia,aprobacion):
        self.referencia =referencia
        self.aprobacion =aprobacion
       