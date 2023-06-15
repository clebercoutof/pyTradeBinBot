### 1. Módulos Internos

`BinWebSocket` - Módulo responsável por interagir com a binance utilizando websockets

`binalytics` - Módulo responsável por armazenar e tratar os preços da vela, de forma a calcular os indicadores

`binOrderSim` - Módulo utilizado pra simular a carteira, registrando ordens

`logManager` - Módulo responsavel por tratar mensagens e mostrar imagens na tela

`orderManager` - Módulo que utiliza a API da binance para realizar as ordens de compra e venda diretamente na corretora.

## 2. Instalação Manual
 > Caso o usuário opte por não utilizar a imagem  docker, pode instalar o programa manualmente utilizando os seguintes passos.
 > É recomendado que a instalação seja feita em um ambiente isolado, recomendamos o `python venv`, você pode encontrar informações nesse  [link](https://docs.python.org/3/library/venv.html).

A instalação manual consiste em alguns passos:

1. Instalação do Python 3.9 e python dev

2. Criação do ambiente virtual; 

3. Instalação da biblioteca C da TA-Lib;

4. Instalação das dependências em python;

### 2.1. Instalação Python
Atualize a lsita de pacotes e instale os pré requisitos
```
$ sudo apt update
$ sudo apt install software-properties-common
```

Adicione o PPA da deadsnakes a lista de sources do sistema:
```
$ sudo add-apt-repository ppa:deadsnakes/ppa
```
Atualize novamente as fontes de seus pacotes e atualize o python
```
$ sudo apt update 
$ sudo apt install python3.9 
```
### 2.2. Ambiente Virtual
> O programa conta com um script para criação do ambiente virtual em python e a adição no comando dentro do arquivo `/home/usr/.bashrc` do usuário. Para efeitos de exemplo, iremos utilizar o nome do ambiente como `tradebin_env`.

Clone o repositório no seu computador
```
$ git clone git@github.com:clebercoutof/pyTradeBinBot.git
```

Torne o script executável
 ```
  $ chmod +x create_env_3.9.sh 
 ```
Execute o script e escolha o nome desejado para o ambiente virtual:
```
  user@pc:~/path/to/pyTradeBinBot$ ./create_env_3.9.sh 
  Enter Your VIRTUAL ENV name: tradebin_env
  Output Path: /home/usr/path/to/pyTradeBinBot/tradebin_env
```

### 2.3. Instalação da biblioteca C da TA-Lib;
> O usuário pode encontrar a biblioteca original dentro da pasta `/external/`, realizando a instalação como um pacote C comum.

  ```
$ tar -xzf ta-lib-0.4.0-src.tar.gz
$ cd ta-lib/
$ ./configure --prefix=/usr
$ make
$ sudo make install
```
### 2.4. Instalação das dependências em python;
 > As depêndencias em python podem ser instaladas por meio do comando `pip install`.

Para ativar o ambiente virtual, utilize o comando `activate_nomedoenv`, para efeitos de exemplo, utilizaremos `tradebin_env`:

 ```
 user@pc:~/path/to/pyTradeBinBot$ activate_tradebin_env
 ```

 Dentro do environment, o usuário pode instalar as dependências python normalmente utilizando a função `pip install`.

```
  (tradebin_env) user@pc:~/root/path/to/pyTradeBinBot $ pip install -r requirements.txt .
```

### Executando o script principal
Você pode executar normalmente o robô como um módulo do seu pacote python
```
python -m src.mybot
```
## Possíveis erros e troubleshooting 

### Erros de valores no Numpy
> Pode haver uma incompantibilidade do numpy instalado na máquina  do usuário e a versão utilizada pelo código, caso a instalação pelos os apresente problemas, você pode tentar dar upgrade na biblioteca `numpy` manualmente.

#### Mensagem de erro
```
ValueError: numpy.ndarray size changed, may indicate binary incompatibility. Expected 96 from C header, got 80 from PyObject
```
#### Solução 
> Fazer o upgrade da versão da biblioteca `numpy`. O usuário pode utilizar o seguinte comando:
```
pip install --upgrade numpy
```
### Falha na instalação da TA-Lib
> A biblioteca TA-Lib utiliza um código em linguagem C em conjunto com a linguagem Python. Para a instalação ocorrer sem problemas, é necessário que o usuário tenha a biblioteca em C instalada e o setup feito corretamente no sua máquina.

### Mensagem de erro
```
Building wheel for TA-Lib (setup.py) ... error
  error: subprocess-exited-with-error

error: command '/usr/bin/x86_64-linux-gnu-gcc' failed with exit code 1
      [end of output]
  ...


  ...
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for TA-Lib
  Running setup.py clean for TA-Lib
Failed to build TA-Lib
ERROR: Could not build wheels for TA-Lib, which is required to install pyproject.toml-based projects
```
### Solução 
> Refazer a instalação da TA-LIB


### Mal funcionamento da biblioteca websocket
A biblioteca pode apresentar mal funcionamento caso o usuário tenha outras versões da biblioteca `websocket` instalada ou caso tenha criado um arquivo com o nome `websocket.py`junto ao pacote.

#### Mensagem do erro
```self.ws = websocket.WebSocketApp(wsurl,on_open=self.on_open,on_message=self.on_message,on_close=self.on_close)
AttributeError: module 'websocket' has no attribute 'WebSocketApp'
```

### Solução
> Reinstalar a biblioteca websocket individualmente utilizando o comando `pip`. O usuário pode utilizar os seguintes comandos:

1. Para remover as duas bibliotecas
```
pip uninstall websocket-client
pip uninstall websocket
```
2. Para reinstalar.
```
pip install websocket-client
pip install websocket
```
##### Helper
> O usuário pode utilizar o comando `locate` para buscar por arquivos nos eu computador e e encontrar o conflito
```
locate websocket.py
```

