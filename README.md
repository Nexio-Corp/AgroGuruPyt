# AgroGuru - Gerador de Prompts

O AgroConnect é uma solução inovadora desenvolvida pela Nexio, que visa enfrentar os desafios da fome e da escassez de alimentos através da integração de tecnologia e sustentabilidade. Nosso objetivo principal é promover a distribuição e o acesso aos alimentos, conectando produtores agrícolas às comunidades em situação de vulnerabilidade alimentar.

No coração do AgroConnect está o AgroGuru, um algoritmo de engenharia de prompt para o ChatGpt, escrito em Python. Os agricultores cadastrados no nosso website, AgroConnect, podem gerar prompts personalizados que auxiliam nas suas atividades agrícolas. Para isso eles gastam os seus AgroCredits, os quais são ganhos após a interação com alguma comunidade.

Ao preencher um formulário detalhado com informações relevantes, como o que desejam saber, a localização da propriedade, a época do ano e outras informações opcionais, os agricultores podem gerar prompts adequados para a IA generativa. O AgroGuru processa esses prompts e fornece respostas mais precisas e personalizadas para as perguntas dos agricultores.

A simulação da API do AgroConnect oferece uma demonstração de interface de console do AgroGuru, mostrando o processo de cadastro, preenchimento do formulário e geração de prompts. Atualmente, as respostas são exibidas no console, mas no futuro, pretendemos integrar diretamente à API da OpenAI.

Com o AgroConnect, buscamos não apenas fornecer acesso a informações valiosas para os agricultores, mas também incentivar a prática do comércio sustentável. Ao conectar os produtores agrícolas às comunidades em situação de vulnerabilidade alimentar, estamos unindo esforços para combater a fome e a escassez de alimentos.

## Membros da equipe

Adrian Satiro Sivilha – RM: 97784

Cauã Alencar Rojas Romero – RM: 98638

Jaci Teixeira Santos – RM: 99627

Pedro Henrique Nobrega de Castro Paterno – RM: 99726

Sabrina Faustino do Prado - RM: 99570

## Como usar

1. Execute o script gen_prompt.py em um terminal Python.
2. Crie uma conta no AgroGuru (deve ser maior de idade para acessar).
3. Escolha uma das opções do menu:
    1. Criar um prompt
    2. Ver prompts criados
    3. Sair
4. Se você escolher "Criar um prompt", siga as instruções para criar um prompt personalizado.
5. Se você escolher "Ver prompts criados", o script exibirá uma lista de todos os prompts criados até agora.
6. Quando terminar, escolha "Sair" para encerrar o script.

## Fluxo do Código

O código do AgroGuru segue o seguinte fluxo:

1. O programa começa com uma mensagem de boas-vindas e instrui o usuário a criar uma conta.
2. A função create_account() é chamada para coletar informações do usuário, como nome, senha e ano de nascimento. Essas informações são validadas para garantir que sejam inseridas corretamente.
3. Se o ano de nascimento for posterior a 2005, indica que o usuário é menor de idade e o programa encerra.
4. Caso contrário, o programa continua, exibe uma mensagem de conta criada com sucesso e apresenta um menu de opções.
5. O usuário pode escolher entre as opções:
    1. Criar um prompt
    2. Ver prompts criados
    3. Sair
6. O usuário é solicitado a escolher uma opção digitando o número correspondente.
7. O programa valida a escolha do usuário e executa a ação apropriada:
    1. Se a opção for "1" (Criar um prompt), a função create_prompt() é chamada. O usuário é guiado por uma série de perguntas para preencher as informações necessárias para gerar o prompt. As informações solicitadas são as seguintes:
        * Primeiro, o usuário deve digitar o que deseja fazer, que é o objetivo ou ação para o qual precisa de assistência.
        * Em seguida, o usuário é solicitado a inserir sua localização atual, sendo encorajado a fornecer uma descrição precisa, pois isso ajuda a gerar uma resposta mais relevante.
        * Depois disso, o usuário deve digitar a época do ano em que pretende realizar a ação especificada no prompt.
        * Além das informações essenciais mencionadas acima, o programa oferece a possibilidade de adicionar informações opcionais:
            * Tamanho da fazenda: O usuário pode digitar o tamanho de sua fazenda ou área de cultivo.
            * Ferramentas disponíveis: O usuário pode mencionar as ferramentas agrícolas disponíveis para realizar a ação.
            * Quanto está disposto a pagar: O usuário pode indicar o montante que está disposto a investir financeiramente.
            * Informações adicionais: O usuário tem a opção de fornecer qualquer informação adicional relevante que possa ajudar a gerar um prompt mais preciso.
        * Com base nas respostas do usuário, o prompt é gerado usando a função generate_prompt(), que combina todas as informações fornecidas em uma mensagem coerente e instrutiva para o AgroGuru e o prompt gerado é adicionado a uma lista de prompts criados para referência futura, após isso programa exibe uma mensagem informando que o prompt foi criado com sucesso e o prompt também é exibido na tela.
    2. Se a opção for "2" (Ver prompts criados), o programa itera sobre a lista de prompts criados e os exibe na tela.
    3. Se a opção for "3" (Sair), o programa encerra.
8. Após executar a ação escolhida, o programa retorna ao menu de opções, onde o usuário pode fazer uma nova escolha.
9. O programa continuará repetindo esse fluxo até que o usuário escolha a opção "3" (Sair).
10. Quando o usuário sai do programa, uma mensagem de agradecimento é exibida.

Esse fluxo de código permite ao usuário criar prompts personalizados e visualizar os prompts criados.

## Requisitos

Python 3.x
