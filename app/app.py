#https://codigofacilito.com/videos/primera-pagina-web-y-hola-mundo

from flask import Flask, render_template, request

app = Flask(__name__)


@app.before_request
def beforeRequest():
    print("Antes de la petición")

@app.after_request # necesita devolver una respuesta
def afterRequest(response):
    print("Despues de la petición")
    return response

@app.route("/")#llama a la funcion en el elemento raiz
def index():
    print("Estamos accediendo a la vista para realizar las peticiones")
    # return "Esta pagina esta vacia"
    #return render_template("index.html", titulo="Pagina principal") #Abrimos el documento html y enviamos un valor Index con la etiqueta titulo
    data={
        "titulo" : "Index",
        "encabezado" : "Bienvenido"
    }
    return render_template("index.html", data=data)

@app.route("/contacto")
def contacto():
    data={
        "titulo" : "Contacto",
        "encabezado" : "Bienvenido"
    }
    return render_template("contacto.html",data=data)

#indicamos que va a recibir un nombre y la funcion tiene que recibir el mismo con el mosmo nombre
@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"hola {nombre}"

@app.route("/suma/<int:valor1>/<int:valor2>")
def suma(valor1, valor2):
    #Siempre hay que devolver un string
    return f"La suma es {valor1 + valor2}"


@app.route("/perfil/<nombre>/<int:edad>")
def perfil(nombre,edad):
    return f"tu nombre es {nombre} y tu edad es {edad}"

def holaMundo():
    return "Hola mundo"


@app.route("/lenguajes")
def lenguajes():
    data = {
        "hayLenguajes" : False,
        "lenguajes" : ["PHP", "Python", "Kotlin", "Java", "C#", "javaScript"]
    }
    return render_template("lenguajes.html",data=data)

#HTTP: HyperText Transfer Protocol
#GET, POST, PUT, DELETE

@app.route("/datos")
def datos ():
    #http://127.0.0.1:5000/datos?valor1=python&valor2=28
    #Muestra los valores que se les pasa
    #print(request.args)
    valor1 = request.args.get("valor1")
    valor2 = request.args.get("valor2")
    return f"estos son los datos llega el : {valor1} y ademas {valor2}"


if __name__ == '__main__':
    app.add_url_rule("/holamundo", view_func=holaMundo) #Llamar la función hola mundo como vista
    app.run(debug=True, port=5000)#definimos puesto y en debus se actualiza los cambios sin tener que parar y arrancar el servidor
