print("**** Ejercicio 1 ****")

# Definición de la clase Mascota
class Mascota:
    # Método constructor de la clase Mascota, se inicializan los atributos de la mascota y se define el tamaño según su peso
    def __init__(self, apodo, tipo_raza, años, masa_corporal, Caracteristica, responsable, contacto_responsable):
        self.apodo = apodo                  
        self.tipo_raza = tipo_raza             
        self.años = años                       
        self.masa_corporal = masa_corporal     
        self.Caracteristica = Caracteristica           
        self.responsable = responsable         
        self.contacto_responsable = contacto_responsable  
        self.estado_atencion = "NO ATENDIDO"   
        self.categoria_tamaño = self.determinar_tamaño()  

    # Método para definir el tamaño de la mascota en función de su masa corporal
    def determinar_tamaño(self):
        if self.masa_corporal < 10:
            return "Mascota Pequeña"  
        else:
            return "Mascota Grande"   

    # Método para registrar la atención de la mascota, cambiando su estado a "ATENDIDO"
    def registrar_atencion(self):
        self.estado_atencion = "ATENDIDO"

    # Método para mostrar la información de la mascota
    def mostrar_informacion(self):
        print(f"Apodo: {self.apodo}")                            
        print(f"Raza: {self.tipo_raza}")                        
        print(f"Edad: {self.años} años")                         
        print(f"Masa Corporal: {self.masa_corporal} kg")         
        print(f"Caracteristica: {self.Caracteristica}")                     
        print(f"Responsable: {self.responsable}")                
        print(f"Contacto del Responsable: {self.contacto_responsable}")  
        print(f"Estado de Atención: {self.estado_atencion}")      
        print(f"Tamaño: {self.categoria_tamaño}")                 


# Se solicitan los datos de la mascota al usuario
apodo = input("Ingrese el apodo de la mascota: ")
tipo_raza = input("Ingrese la raza de la mascota: ")
años = int(input("Ingrese la edad de la mascota: "))
masa_corporal = float(input("Ingrese la masa corporal de la mascota (en kg): "))
tonalidad = input("Ingrese una caracteristica unica: ")
responsable = input("Ingrese el nombre del responsable: ")
contacto_responsable = input("Ingrese el contacto del responsable: ")

# Se crea una instancia de la clase Mascota con los datos ingresados
mascota = Mascota(apodo, tipo_raza, años, masa_corporal, tonalidad, responsable, contacto_responsable)

mascota.registrar_atencion()

mascota.mostrar_informacion()

print("*****************************************************************************")

print ("**** Ejercicio 2 ****")

# Definición de la clase Producto
class Producto:
    # Método constructor que inicializa el precio de compra y calcula el precio de venta
    def __init__(self, costo_inicial):
        self.costo_inicial = costo_inicial      
        self.precio_final = self.calcular_precio_final()  

    # Método para calcular el precio de venta con un margen de ganancia del 30%
    def calcular_precio_final(self):
        return self.costo_inicial * 1.30

    # Método para mostrar información del producto (será sobrescrito en las subclases)
    def mostrar_informacion(self):
        pass  

class Libreta(Producto):
    def __init__(self, costo_inicial, numero_hojas):
        super().__init__(costo_inicial)     
        self.numero_hojas = numero_hojas      
        self.marca_libreta = "NORMA"         

    def mostrar_informacion(self):
        print(f"Producto: Libreta")
        print(f"Marca: {self.marca_libreta}")
        print(f"Número de hojas: {self.numero_hojas}")
        print(f"Costo inicial: ${self.costo_inicial:.2f}")
        print(f"Precio final: ${self.precio_final:.2f}")



class Pluma(Producto):
    # Constructor que inicializa el costo inicial, el tipo de pluma y la marca
    def __init__(self, costo_inicial, tipo_pluma):
        super().__init__(costo_inicial)       
        self.tipo_pluma = tipo_pluma            
        self.marca_pluma = "Prisma Colors"             

    # Método para mostrar la información de la pluma
    def mostrar_informacion(self):
        print(f"Producto: Pluma")
        print(f"Marca: {self.marca_pluma}")
        print(f"Tipo: {self.tipo_pluma}")
        print(f"Costo inicial: ${self.costo_inicial:.2f}")
        print(f"Precio final: ${self.precio_final:.2f}")



libreta1 = Libreta(costo_inicial=1.50, numero_hojas=50)
libreta2 = Libreta(costo_inicial=2.80, numero_hojas=100)


pluma1 = Pluma(costo_inicial=0.30, tipo_pluma="Grafito")
pluma2 = Pluma(costo_inicial=0.50, tipo_pluma="Colores")

libreta1.mostrar_informacion()
print()
libreta2.mostrar_informacion()
print()
pluma1.mostrar_informacion()
print()
pluma2.mostrar_informacion()

print("*****************************************************************************")

print("**** Ejercicio 3 ****")

# Definición de la clase Vehiculo
class Vehiculo:
    # Método constructor que inicializa los atributos del vehículo
    def __init__(self, fabricante, modelo, año_fabricacion, tonalidad, categoria, motorizacion, energia, transmision, costo_adquisicion, procedencia):
        self.fabricante = fabricante            
        self.modelo = modelo                    
        self.año_fabricacion = año_fabricacion  
        self.tonalidad = tonalidad             
        self.categoria = categoria              
        self.motorizacion = motorizacion        
        self.energia = energia                 
        self.transmision = transmision          
        self.costo_adquisicion = costo_adquisicion  
        self.procedencia = procedencia          
        self.numero_ruedas = 4                 
        self.capacidad_occupantes = 5           
        self.precio_final = self.calcular_precio_final()  

    # Método para calcular el precio de venta con un margen de ganancia del 40%
    def calcular_precio_final(self):
        return self.costo_adquisicion * 1.4

    # Método para mostrar la información del vehículo
    def mostrar_informacion(self):
        print(f"Fabricante: {self.fabricante}")
        print(f"Modelo: {self.modelo}")
        print(f"Año de fabricación: {self.año_fabricacion}")
        print(f"Tonalidad: {self.tonalidad}")
        print(f"Categoría: {self.categoria}")
        print(f"Motorización: {self.motorizacion}")
        print(f"Energía: {self.energia}")
        print(f"Transmisión: {self.transmision}")
        print(f"Procedencia: {self.procedencia}")
        print(f"Número de ruedas: {self.numero_ruedas}")
        print(f"Capacidad de ocupantes: {self.capacidad_occupantes}")
        print(f"Costo de adquisición: ${self.costo_adquisicion:.2f}")
        print(f"Precio de venta: ${self.precio_final:.2f}")

# Crear instancia de la clase Vehiculo con datos específicos
vehiculo1 = Vehiculo(
    fabricante="Toyota",
    modelo="Corolla",
    año_fabricacion=2023,
    tonalidad="Blanco",
    categoria="Sedán",
    motorizacion="1.8L",
    energia="Gasolina",
    transmision="Tracción delantera",
    costo_adquisicion=20000,
    procedencia="Nacional"
)

# Crear otra instancia de la clase Vehiculo con diferentes datos
vehiculo2 = Vehiculo(
    fabricante="BMW",
    modelo="X5",
    año_fabricacion=2024,
    tonalidad="Negro",
    categoria="SUV",
    motorizacion="3.0L",
    energia="Diesel",
    transmision="4x4",
    costo_adquisicion=50000,
    procedencia="Importado"
)

vehiculo1.mostrar_informacion()
print()
vehiculo2.mostrar_informacion()

print("*****************************************************************************")

print("**** Ejercicio 4 ****")

# Definición de la clase Gadget
class Gadget:
    # Método constructor que inicializa los atributos del dispositivo electrónico
    def __init__(self, categoria, modelo, capacidad_almacenamiento, memoria_ram, chip_procesador, dimension_pantalla, costo_adquisicion):
        self.fabricante = "Samsung"                
        self.categoria = categoria              
        self.modelo = modelo                     
        self.capacidad_almacenamiento = capacidad_almacenamiento 
        self.memoria_ram = memoria_ram        
        self.chip_procesador = chip_procesador     
        self.dimension_pantalla = dimension_pantalla  
        self.costo_adquisicion = costo_adquisicion   
        self.precio_final = self.calcular_precio_final()  
        self.origen_producto = "Importado"          

    # Método para calcular el precio de venta con un margen de ganancia del 70%
    def calcular_precio_final(self):
        return self.costo_adquisicion * 1.7

    # Método para mostrar la información del gadget
    def mostrar_informacion(self):
        print(f"Categoría: {self.categoria}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Modelo: {self.modelo}")
        print(f"Capacidad de almacenamiento: {self.capacidad_almacenamiento}")
        print(f"Memoria RAM: {self.memoria_ram}")
        print(f"Chip procesador: {self.chip_procesador}")
        print(f"Tamaño de pantalla: {self.dimension_pantalla} pulgadas")
        print(f"Origen del producto: {self.origen_producto}")
        print(f"Costo de adquisición: ${self.costo_adquisicion:.2f}")
        print(f"Precio de venta: ${self.precio_final:.2f}")

# Solicitar al usuario que ingrese los datos para el primer gadget
categoria1 = input("Ingrese la categoría del gadget (Ejemplo: Celular, Portátil): ")
modelo1 = input("Ingrese el modelo del gadget: ")
capacidad_almacenamiento1 = input("Ingrese la capacidad de almacenamiento (Ejemplo: 128GB, 512GB): ")
memoria_ram1 = input("Ingrese la memoria RAM (Ejemplo: 8GB, 16GB): ")
chip_procesador1 = input("Ingrese el procesador (Ejemplo: Snapdragon 888, Intel i7): ")
dimension_pantalla1 = float(input("Ingrese el tamaño de la pantalla en pulgadas: "))
costo_adquisicion1 = float(input("Ingrese el costo de adquisición en dólares: "))

# Crear instancia de la clase Gadget con los datos ingresados
gadget1 = Gadget(
    categoria=categoria1,
    modelo=modelo1,
    capacidad_almacenamiento=capacidad_almacenamiento1,
    memoria_ram=memoria_ram1,
    chip_procesador=chip_procesador1,
    dimension_pantalla=dimension_pantalla1,
    costo_adquisicion=costo_adquisicion1
)

# Solicitar al usuario que ingrese los datos para el segundo gadget
categoria2 = input("Ingrese la categoría del gadget (Ejemplo: Celular, Portátil): ")
modelo2 = input("Ingrese el modelo del gadget: ")
capacidad_almacenamiento2 = input("Ingrese la capacidad de almacenamiento (Ejemplo: 128GB, 512GB): ")
memoria_ram2 = input("Ingrese la memoria RAM (Ejemplo: 8GB, 16GB): ")
chip_procesador2 = input("Ingrese el procesador (Ejemplo: Snapdragon 888, Intel i7): ")
dimension_pantalla2 = float(input("Ingrese el tamaño de la pantalla en pulgadas: "))
costo_adquisicion2 = float(input("Ingrese el costo de adquisición en dólares: "))

# Crear otra instancia de la clase Gadget con los datos ingresados
gadget2 = Gadget(
    categoria=categoria2,
    modelo=modelo2,
    capacidad_almacenamiento=capacidad_almacenamiento2,
    memoria_ram=memoria_ram2,
    chip_procesador=chip_procesador2,
    dimension_pantalla=dimension_pantalla2,
    costo_adquisicion=costo_adquisicion2
)
print("---------------------------------------------")
print("Los datos del Gadget son:")
gadget1.mostrar_informacion()
print()
gadget2.mostrar_informacion()

print("---------------------------------------------")
print("**** Ejercicio 5 ****")
# Definición de la clase ClienteFinanciero
class ClienteFinanciero:
    def __init__(self, nombre_cliente, numero_dui, acciones_comprar, tipo_servicio, monto_dolares):
        self.nombre_cliente = nombre_cliente          
        self.numero_dui = numero_dui                  
        self.acciones_comprar = acciones_comprar     
        self.tipo_servicio = tipo_servicio          
        self.monto_dolares = monto_dolares            

    # Método para evaluar si la solicitud está aprobada o rechazada
    def evaluar_solicitud(self):
        if self.monto_dolares >= 1000:  # Aprobado si el monto es mayor o igual a $1000
            return "APROBADO"
        else:
            return "RECHAZADO"

    # Método para mostrar la información del cliente
    def mostrar_informacion(self):
        print(f"Nombre del Cliente: {self.nombre_cliente}")
        print(f"Número de DUI: {self.numero_dui}")
        print(f"Acciones a Comprar: {self.acciones_comprar}")
        print(f"Tipo de Servicio: {self.tipo_servicio}")
        print(f"Monto en Dólares: ${self.monto_dolares:.2f}")
        print(f"Estado de la Solicitud: {self.evaluar_solicitud()}")

# Solicitar al usuario que ingrese los datos
nombre_cliente = input("Ingrese su nombre: ")
numero_dui = input("Ingrese su número de DUI: ")
acciones_comprar = int(input("Ingrese la cantidad de acciones que desea comprar: "))
tipo_servicio = input("Ingrese el tipo de servicio que desea: ")
monto_dolares = float(input("Ingrese el monto en dólares que planea invertir: "))

# Crear una instancia de ClienteFinanciero con los datos ingresados
cliente = ClienteFinanciero(
    nombre_cliente=nombre_cliente,
    numero_dui=numero_dui,
    acciones_comprar=acciones_comprar,
    tipo_servicio=tipo_servicio,
    monto_dolares=monto_dolares
)
cliente.mostrar_informacion()
