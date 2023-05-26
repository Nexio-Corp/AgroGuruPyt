from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def prompt():
    prompt = request.args.get('prompt')
    location = request.args.get('location')
    time_year = request.args.get('time_year')
    size_farm = request.args.get('size_farm')
    available_tools = request.args.get('available_tools')
    willing_pay = request.args.get('willing_pay')
    extra_info = request.args.get('extra_info')
    if not prompt or not location or not time_year:
        return "Falta informações necessárias", 400
    extras = []
    if size_farm:
        extras.append(f"tamanho da fazenda: {size_farm}")
    if available_tools:
        extras.append(f"ferramentas disponíveis: {available_tools}")
    if willing_pay:
        extras.append(f"quanto está disposto a pagar: {willing_pay}")
    if extra_info:
        extras.append(f"informações adicionais: {extra_info}")
    return_value = f"Agora você é o AgroGuru, sua missão é ajudar os pequenos produtores a venderem e cultivarem seus produtos." +\
        "lembre-se de responder com uma linguagem simples, sua missão é ajudar e prover uma passo a passo para qualquer instrução passada pelo agricultor" +\
        f" e tendo em mente as seguintes informações: \nLocalização: {location}\nÉpoca do ano: {time_year}\n"
    for extra in extras:
        return_value += "\n" + extra
    return_value += (
        f"\nE com base nisso sua primeira instrução é :'{prompt}'")
    
    return return_value
