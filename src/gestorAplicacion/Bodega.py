class Bodega:
    def ___init__(self, nombre, barrio, supermercado, productos, promos):
        self.nombre = nombre
        self.barrio = barrio
        self.supermercado = supermercado
        self.productos = productos
        self.promos = promos

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getBarrio(self):
        return self.barrio

    def setBarrio(self, barrio):
        self.barrio = barrio

    def getSupermercado(self):
        return self.supermercado

    def setSupermercado(self, supermercado):
        self.supermercado = supermercado
    
    def getProductos(self):
        return self.productos

    def setProductos(self, productos):
        self.productos = productos

    def agregarProducto(self,producto):
        self.productos.add(producto)

    def quitarProducto(self,producto):
        self.productos.remove(producto)

    def getPromos(self):
        return self.promos
    
    def setPromos(self, promos):
        self.promos = promos

    def agregarPromo(self, promo):
        self.promos.add(promo)

    def quitarPromo(self, promo):
        self.promos.remove(promo)