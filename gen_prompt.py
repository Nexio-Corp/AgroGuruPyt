def generate_prompt(prompt: str, location: str, time_year: str, size_farm: str | None = None, available_tools: str | None = None, willing_pay: str | None = None, extra_info: str | None = None) -> str:
    extras = []  # Lista de informações opcionais
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


def input_valid_year() -> str:
    year = input("Digite o ano: ")
    while True:
        if year.isnumeric() and len(year) == 4:
            return year
        year = input("Digite um ano valido: ")


def input_valid_name() -> str:
    name = input("Digite seu nome: ")
    while not name.isalpha() or len(name) < 3:
        name = input("Digite um nome valido: ")
    return name


def input_valid_password() -> str:
    password = input("Digite sua senha: ")
    confirm_password = input("Confirme sua senha: ")
    while password != confirm_password:
        print("As senhas não coincidem, tente novamente")
        password = input("Digite sua senha: ")
        confirm_password = input("Confirme sua senha: ")
    return password


def create_account():
    name = input_valid_name()
    password = input_valid_password()
    year_birth = input_valid_year()
    if int(year_birth) > 2005:
        print("Você não tem idade para criar uma conta")
        return
    return [name, password, year_birth]


def create_prompt():
    print("Vamos criar o seu prompt!")
    prompt = input("Primeiro digite o que você quer fazer: ")
    location = input(
        "Agora digite onde você está localizado (quanto mais preciso melhor): ")
    time_year = input(
        "Agora digite a época do ano que você irá realizar isso: ")
    print("Agora vamos adicionar algumas informações opcionais (caso não queira deixe em branco)")
    size_farm = input("Digite o tamanho da sua fazenda: ") or None
    available_tools = input(
        "Digite as ferramentas que você tem disponível: ") or None
    willing_pay = input("Digite quanto você está disposto a pagar: ") or None
    extra_info = input("Digite alguma informação adicional: ") or None
    return generate_prompt(prompt, location, time_year, size_farm, available_tools, willing_pay, extra_info)


def main():
    print("Bem vindo ao AgroGuru, o assistente virtual para pequenos produtores")
    print("Para começar, crie uma conta")
    account = create_account()
    if not account:
        print("Menor de idade, não pode criar uma conta")
        return
    prompts = []
    print("Conta criada com sucesso")
    while True:
        choice = input(
            "1 - Criar um prompt\n2 - Ver prompts criados\n3 - Sair\n")
        while choice not in ["1", "2", "3"]:
            choice = input("Digite uma opção valida")
        if choice == "1":
            prompts.append(create_prompt())
            print("Prompt criado com sucesso\n")
            print(prompts[-1])
        elif choice == "2":
            for i in range(len(prompts)):
                print(f"Prompt {i+1}:\n{prompts[i]}")
        elif choice == "3":
            break
    print("Obrigado por usar o AgroGuru, até a próxima")


if __name__ == "__main__":
    main()
