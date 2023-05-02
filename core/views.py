from django.shortcuts import render, HttpResponse, redirect
from .models import clientes, venta
from django.contrib.auth.decorators import login_required # el login required, oculta las vistas y solo permite iniciar luego del login 
from django.contrib.auth import logout # para el cerrar sesión
from datetime import date
from django.core.exceptions import ObjectDoesNotExist

@login_required
def home(request): #Funcion la cual se encarga de obtener datos la ultimas compras realizada por los clientes
    lista_venta = [] #Lista la cual es la úlitma compra de cada Cliente
    Clientes = clientes.objects.all() #Llama a todos los clientes que se encuentra en models
    #Esta lista se utiliza para la funcion en la cual te trae la ultima fecha de venta registrada del cliente
    Clientes_list = clientes.objects.all() #Esto es para cargar los datos de los clientes a la venta 
    today = date.today()
    message = [] #Variable que almacena los mensajes de atraso de un cliente
    #Ej "Han pasado",delta.days ," Días desde que el cliente", Clientes.nombre,"no a realizado una compra")) 
    #Este for itera por cada cliente
    for Clientes in Clientes:
        if venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first() is None:
            print("Cliente no posee Compras")
        else:
            ultima_fecha = venta.objects.filter(cliente = Clientes).order_by('-fecha_compra').first()
            lista_venta.append(ultima_fecha)#Append inserta un dato en un arreglo, esto inserta la ultima compra realizada por el cliente
            fecha_rgistrada = ultima_fecha.fecha_compra #Almacena solo la ultima fecha del cliente que se este recorriendo
            delta = today - fecha_rgistrada
            if delta.days >= 14:
                message.append(("Han pasado",delta.days ," Días desde que el cliente", Clientes.nombre,"no a realizado una compra"))
            else:
                print("No han pasado 2 semanas") 
    return render(request, 'core/home.html', {"venta_list": lista_venta ,"clientes_lista": Clientes_list,'message': message})

@login_required
def salir(request): # cerrar sesion
    logout(request)
    return redirect('/')

@login_required#Eliminar en futuro
def historial_Compra(request):
    return render(request, 'core/historial_Compra.html')

@login_required
def menu_Historial(request):#Carga el historial general de las ventas
    venta_historial = venta.objects.all()
    Clientes_list = clientes.objects.all() # esto es para cargar los datos de los clientes a la venta 
    return render(request, 'core/menu_Historial.html', {"clientes_lista": Clientes_list, "venta_historial": venta_historial})

@login_required
def registrar_Cliente(request):
    Clientes_lists = clientes.objects.all() # esto es para listar mediante orm
    Clientes_list = clientes.objects.all() # esto es para cargar los datos de los clientes a la venta
    return render(request, 'core/registrar_Cliente.html', {"clientes_list": Clientes_lists, "clientes_lista": Clientes_list})

@login_required
def registrarCliente(request):
    rut = request.POST['txtRut']
    nombre = request.POST['txtNombre']
    direccion = request.POST['txtDireccion']
    email = request.POST['txtEmail']

    try: #Obtiene los clientes registrados y los compara con el rut ingresado si este es igual no lo almacena.
        cliente = clientes.objects.get(rut=rut)
    except ObjectDoesNotExist:
        # Si no existe el cliente, lo crea.
        cliente = clientes.objects.create(rut=rut, nombre=nombre, direccion=direccion, email=email)

    return redirect("/registrar_Cliente")

@login_required
def eliminardatosclientes(request, rut): # Eliminar cliente
    Cliente = clientes.objects.get(rut=rut)  #valida el rut y obtiene los datos 
    Cliente.delete() #se encarga de borrarlos
    return redirect('/registrar_Cliente')

@login_required
def editarcliente(request, rut): # redirecciona enviando el rut a la ventana cliente
    cliente = clientes.objects.get(rut=rut)
    Clientes_list = clientes.objects.all() # esto es para cargar los datos de los clientes a la venta
    return render(request, "core/editar_Cliente.html", {'client':cliente, "clientes_lista": Clientes_list}) 

@login_required
def guardarEdicion(request): # Guardar los datos del cliente
    rut = request.POST['txtRut']
    nombre = request.POST['txtNombre']
    direccion = request.POST['txtDireccion']
    email = request.POST['txtEmail']

    cliente = clientes.objects.get(rut=rut)
    cliente.nombre = nombre
    cliente.direccion = direccion
    cliente.email = email
    cliente.save()

    return redirect('/registrar_Cliente')

@login_required
def prosesar_formulario_venta(request):
    codigo_venta = request.POST['txtCodigo'] #obtiene los datos de los labels
    cliente_nombre = request.POST['txtCliente']
    cliente = clientes.objects.get(nombre = cliente_nombre)
    fecha_compra = request.POST['datefecha']
    productos = request.POST['txtProductos'] # traer el archivo de la imagen
    try:
        vent = venta.objects.get(codigo_venta=codigo_venta)
    except ObjectDoesNotExist:
        vent = venta.objects.create(codigo_venta=codigo_venta, cliente=cliente, fecha_compra=fecha_compra, productos= productos) #se encarga de crear guardar los datos obtenidos
    return redirect('/')

@login_required
def search_results(request): # esto lo saco de chatgpt xD 
    query = request.POST['query']
    cliente = clientes.objects.filter(nombre__icontains=query)
    return render(request, "core/registrar_Cliente.html", {'clientes_list': cliente})

@login_required
def regsitrar_Venta(request):
    return render(request, 'core/regsitrar_Venta.html')

@login_required
def ultima_Compra(request):
    return render(request, 'core/ultima_Compra.html')

@login_required
def Alerta(request):
    return render(request, 'core/Alertas.html')


