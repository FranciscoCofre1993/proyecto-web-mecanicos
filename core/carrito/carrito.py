class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, servicio):
        if str(servicio.id) not in self.carrito.keys():
            self.carrito[str(servicio.id)] = {
                "id": servicio.id,
                "nombre": servicio.nombre,
                "cantidad": 1,
                "precio": str(servicio.precio)
            }
        else:
            for key, value in self.carrito.items():
                if key == str(servicio.id):
                    value["cantidad"] += 1
                    break
        self.guardar()

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, servicio):
        id = str(servicio.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar()

    def restar(self, servicio):
        for key, value in self.carrito.items():
            if key == str(servicio.id):
                value["cantidad"] -= 1
                if value["cantidad"] < 1:
                    self.eliminar(servicio)
                else:
                    self.guardar()
                break

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    @property
    def servicio(self):
        # Obtener la lista de productos en el carrito
        servicio_carrito = []
        for item in self.carrito.values():
            servicio_carrito.append({
                "id": item["id"],
                "nombre": item["nombre"],
                "precio": item["precio"],
                "cantidad": item["cantidad"]
            })
        return servicio_carrito

    @property
    def total(self):
        # Calcular el total del carrito
        total = 0
        for item in self.carrito.values():
            precio = float(item["precio"])
            cantidad = item["cantidad"]
            total += precio * cantidad
        return total
