

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, obra):
        if obra.idObra not in self.carrito.keys():
            self.carrito[obra.idObra]={
                "obra_id":obra.idObra, 
                "autor": obra.autor,
                "titulo": obra.titulo,
                "precio": str (obra.precio),
                "cantidad": 1,
                "total": obra.precio,

            }
        else:
            for key, value in self.carrito.items():
                if key==obra.idObra:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = obra.precio
                    value["total"]= value["total"] + obra.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True


    def eliminar(self, obra):
        id = obra.idObra
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,obra):
        for key, value in self.carrito.items():
            if key == obra.idObra:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- obra.precio
                if value["cantidad"] < 1:   
                    self.eliminar(obra)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 
