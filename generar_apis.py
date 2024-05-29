from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return 'Bienvenido a mi web'
    return render_template('index.html')

@app.route('/suma')
def suma():
    valor1 = 5
    valor2 = 6
    suma =  valor1 + valor2
    return {'suma': suma}

@app.route('/insert', methods=['POST'])
def insert():
    game_details = request.get_json()
    valor1 = game_details["valor1"]
    valor2 = game_details["valor2"]
    operacion = game_details["operacion"]
    if operacion == 'suma':
        resultado = valor1 + valor2
    elif operacion == 'resta':
        if valor1 < valor2:
            resultado = valor2 - valor1
        else:
            resultado = valor1 - valor2

    elif operacion == 'multiplicar':
        resultado = valor1 * valor2
    else: 
       resultado = 'no conozco la operacion'
    
    return str(resultado)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

