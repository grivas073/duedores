
class Deudor():
    dni = 0
    apellido = ""
    nombre = ""
    dniCotitular = 0
    apellidoCotitular = ""
    nombreCotitular = ""
    montoAdeudado = 0
    anioDeuda = 0
    def __init__(self):
        self.dni = ""
        self.apellido = "" 
        self.nombre = ""
        self.dniCotitular = 0
        self.apellidoCotitular = "" 
        self.nombreCotitular = ""
        self.montoAdeudado = 0
        self.anioDeuda =  0
    def __init__(self, dni, apellido, nombre, dniCotitular, apellidoCotitular, nombreCotitular, montoAdeudado, anioDeuda):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.dniCotitular = dniCotitular
        self.apellidoCotitular = apellidoCotitular
        self.nombreCotitular = nombreCotitular
        self.montoAdeudado = montoAdeudado
        self.anioDeuda = anioDeuda
        # La deuda actual se calculará teniendo en cuenta el año de la deuda. Por cada año la deuda incrementará un 21%. Por ejemplo, si el monto es $10.000 y el año es 2020, la deuda actual será de $16.300
    def CalcularDeudaActual(self):
        anioActual = 2025
        anioDeudaWhile = self.anioDeuda
        montoOriginal = self.montoAdeudado
        MontoActual = self.montoAdeudado
        while anioActual > anioDeudaWhile:
            intereses = montoOriginal * 0.21
            MontoActual += intereses
            anioDeudaWhile += 1
        return MontoActual
    def RealizarPlanDePago(self,cuotas):
        deudaA = self.CalcularDeudaActual()
        if cuotas > 0 and cuotas <= 3:
            PlanDePago = deudaA / cuotas
            return PlanDePago
        elif cuotas >= 4 and cuotas <= 6:
            PlanDePago = (deudaA / cuotas) * 1.10
            return PlanDePago
        elif cuotas >= 7 and cuotas <= 12:
            PlanDePago = (deudaA / cuotas) * 1.19
            return PlanDePago
        else:
            return "No se puede realizar el plan de pago, el numero de cuotas tiene que ser entre 1 y 12"
    def CambiarCotitular(self, dniCotitular, apellidoCotitular, nombreCotitular):
        self.dniCotitular = dniCotitular
        self.apellidoCotitular = apellidoCotitular
        self.nombreCotitular = nombreCotitular
        self.montoAdeudado = self.montoAdeudado*1.05
        return f"Nuevo Cotitular: Nombre:{self.nombreCotitular}, Apellido: {self.apellidoCotitular}, DNI: {self.dniCotitular} {self.montoAdeudado}"
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}, Nombre del Cotitular: {self.nombreCotitular}, Apellido del Cotitular: {self.apellidoCotitular}, DNI Cotitular: {self.dniCotitular}, Monto Adeudado: {self.montoAdeudado}, Anio de Deuda: {self.anioDeuda}"
    def datosPersonalesDeudor(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}"
    def datosPersonalesCotitular(self):
        return f"Nombre del Cotitular: {self.nombreCotitular}, Apellido del Cotitular: {self.apellidoCotitular}, DNI Cotitular: {self.dniCotitular}"

dni = int(input("Ingrese el DNI del deudor: "))
apellido = input("Ingrese el apellido del deudor: ")
nombre = input("ingrese el nombre del deudor: ")
dniCotitular = int(input("Ingrese el DNI del cotitular: "))
apellidoCotitular = input("Ingrese el apellido del cotitular: ")
nombreCotitular = input("Ingrese el nombre del cotitular: ")
montoAdeudado = int(input("Ingrese el monto adeudado: "))
anioDeuda = int(input("Ingrese el año de la deuda: "))
objetoD = Deudor(dni, apellido, nombre, dniCotitular, apellidoCotitular, nombreCotitular, montoAdeudado, anioDeuda)

while True:
    print("1. Calcular deuda actual")
    print("2. Realizar plan de pago")
    print("3. Cambiar cotitular")
    print("4. Ver datos personales del deudor")
    print("5. Ver datos personales del cotitular")
    print("6. Ver todos los datos del deudor")
    print("7. Salir del programa")
    opcion = input("Ingrese la opcion deseada: ")
    match opcion:
        case "1":
            deudaActual = objetoD.CalcularDeudaActual()
            print(f"La deuda actual es: {deudaActual}")
        case "2":
            cuotas = int(input("Ingrese el numero de cuotas: "))
            planPago = objetoD.RealizarPlanDePago(cuotas)
            print(f"El plan de pago es: {planPago} en {cuotas} pago/s")
        case "3":
            dniCotitular = int(input("Ingrese el nuevo DNI del nuevo cotitular: "))
            apellidoCotitular = input("Ingrese el apellido del nuevo cotitular: ")
            nombreCotitular = input("Ingrese el nombre del nuevo cotitular: ")
            resultado = objetoD.CambiarCotitular(dniCotitular, apellidoCotitular, nombreCotitular)
            print("El nuevo cotitular tiene los siguientes datos:", resultado)
        case "4":
            datosPersonalesDeudor = objetoD.datosPersonalesDeudor()
            print("Datos personales del deudor:", datosPersonalesDeudor)
        case "5":
            datosPersonalesCotitular = objetoD.datosPersonalesCotitular()
            print("Datos personales del cotitular:", datosPersonalesCotitular)
        case "6":
            datosDeudor = objetoD.__str__()
            print("Todos los datos del deudor:", datosDeudor)
        case "7":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida, por favor escriba el número de la opción deseada.")


            