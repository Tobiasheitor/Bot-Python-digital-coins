# Bot-Python-digital-coins

Um Chatterbot para tirar dúvidas sobre moedas digitais

Este Chatterbot faz parte do trabalho de Inteligência Artificial do curso de
Ciência da Computação da Universidade Regional Integrada (URI) Campus Erechim.

Autor: Tobias Heitor Goettert

Orientador: Prof Marcos A. Lucas

## Download do projeto

Olhe para o canto superior direito, aparecerá um botão para Download, você pode escolher entre:

### Donwload usando o git

Caso você tenha o git instalado basta digitar o seguinte comando:
```
git clone https://github.com/Tobiasheitor/Bot-Python-digital-coins.git
```
### Download .zip
Basta baixar o arquivo e extrair ele no seu computador

## Instalar Python versão 3.6.*

Para poder rodar o chatterbot você deve primeiro verificar se já possui o Python instalado. Para isso, digite no seu terminal o seguinte comando:
```
python -V
```

Caso a resposta seja positiva, você pode passar para o próximo tópico.

Caso contrário vá até o seguinte endereço https://www.python.org/downloads/ e busque pelo python versão 3.6.* compatível com o seu sistema operacional.

Para instalar e configurar o python você pode seguir um dos diversos tutoriais na internet.

Um bom tutorial para linux Ubuntu pode ser encontrado em https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04.

## Instalar pacotes do projeto

O projeto vem um arquivo .py e diversos diretórios contendo arquivos usados pelo algorítmo.
Para iniciar o aplicativo devemos executar o arquivo digital_coins.py, para isso algumas dependências devem ser instaladas.
Primeiramente instale o microframework Flask, para isso verifique a documentação no site http://flask.pocoo.org/
Com o Flask instalado baixe a biblioteca Chatterbot com o seguinte comando.
```
pip install chatterbot
```

## Configurando o Chatbot

Se estiver usando linux Ubuntu acesse a pasta com os arquivos baixados via terminal, entre na pasta e digite o código abaixo.
```
export FLASK_APP=digital_coins.py
```

## Para executar o Chatbot digite o comando:
```
python3 -m flask
```

Algumas mensagens aparecerão no terminal e se tudo tiver dado certo acesse o endereço mostrado.
O endereço abrirá no navegador web em um porta pre definida, após aberto já será possível conversar com o Chatbot.

## Algumas sentenças mapeadas

- O que é Bitcoin
- O que é altcoin
- O que é mineração
- O que e Ether
- Ethereum Virtual Machine (EVM)

OBS: Nesta lista não conta todas as sentenças mapeadas, mas sim as principais.

## Referências

1. Turing, A.M. (1950). Computing machinery and intelligence. Mind, vol. LIX, No. 236.
2. LIMA, Luciano Alves. Estudo de implementação de um robô de conversação em curso de língua estrangeira em ambiente virtual: um caso de estabilização do Sistema Adaptativo Complexo. 2014. 130 f. Tese (Doutorado) – Faculdade de Letras, Universidade Federal de Minas Gerais, Belo Horizonte, 2014. Disponível em: http://www.bibliotecadigital.ufmg.br/dspace/bitstream/handle/1843/MGSS-9R3MHD/1360d.pdf. Acesso em: 2 jul. 2018.
3. Micro-framework Flask, disponível em: “http://flask.pocoo.org”.