from flask import Flask, request
from prompt import generate_prompt

app = Flask(__name__)


@app.route('/prompt', methods=['GET'])
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
    return_value = generate_prompt(
        prompt, location, time_year, size_farm, available_tools, willing_pay, extra_info)
    return return_value


if __name__ == "__main__":
    app.run()
