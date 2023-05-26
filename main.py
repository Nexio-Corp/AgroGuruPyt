def generate_prompt(prompt: str, location: str, time_year: str, size_farm: str | None = None, available_tools: str | None = None, willing_pay: str | None = None, extra_info: str | None = None) -> str:
    extras = []
    if size_farm:
        extras.append(f"tamanho da fazenda: {size_farm}")
    if available_tools:
        extras.append(f"ferramentas disponíveis: {available_tools}")
    if willing_pay:
        extras.append(f"quanto está disposto a pagar: {willing_pay}")
    if extra_info:
        extras.append(f"informações adicionais: {extra_info}")
    return_value = f"Agora você é o FarmGpt, sua missão é ajudar os pequenos produtores a venderem e cultivarem seus produtos." +\
        "lembre-se de responder com uma linguagem simples, sua missão é ajudar e prover uma passo a passo para qualquer instrução passada pelo agricultor" +\
        f" e tendo em mente as seguintes informações: \nLocalização: {location}\nÉpoca do ano: {time_year}\n"
    for extra in extras:
        return_value += "\n" + extra
    return_value += (
        f"\nE com base nisso sua primeira instrução é :'{prompt}'")
    return return_value


print(generate_prompt("vender 10kg de tomate por 5 reais", "são paulo",
      "verão", "pequena", "enxada", "10 reais", "tomate maduro"))
generate_prompt("vender 10kg de tomate por 5 reais",
                "são paulo", "verão", extra_info="Sou pobre")
