#https://codigofacilito.com/videos/primera-pagina-web-y-hola-mundo

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")#llama a la funcion en el elemento raiz
def index():
    # return "Esta pagina esta vacia"
    #return render_template("index.html", titulo="Pagina principal") #Abrimos el documento html y enviamos un valor Index con la etiqueta titulo
    data={
        "titulo" : "Index",
        "encabezado" : "Bienvenido"
    }
    return render_template("index.html", data=data)

def holaMundo():
    return "Hola mundo"

if __name__ == '__main__':
    app.add_url_rule("/holamundo", view_func=holaMundo) #Llamar la función hola mundo como vista
    app.run(debug=True, port=5000)#definimos puesto y en debus se actualiza los cambios sin tener que parar y arrancar el servidor
