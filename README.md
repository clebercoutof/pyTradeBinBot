# TradeBinBot - A simple Python live trading robot

  Essa aplicação foi desenvolvida como um protótipo de um robô para realizar operações de trading utilizando a API da binance e a análise tecnica do mercado.

  ![alt text](images/RUNNING-BOT.png)

  O protótipo foi desenvolvido considerando uma futuram integração com o framework Django, possibilitando a interação com o usuário por meio de um front-end

## Instalação
 1 - instalar virtual environment, configurar virtual environment, instalar python 3.9 dev
 2 - instalar TA-LIB dependencies em C

```
$ tar -xzf ta-lib-0.4.0-src.tar.gz
$ cd ta-lib/
$ ./configure --prefix=/usr
$ make
$ sudo make install
```

 3 - instalar package dependencies com o txt do PIP

  É recomendado que a instalação seja feita em um ambiente isolado, recomendamos o `python virtual-env`, você pode encontrar informações nesse  [link](https://docs.python.org/3/library/venv.html).

git clone git@github.com:clebercoutof/pyTradeBinBot.git
chmod +x create_env_3.9.sh 
./create_env_3.9.sh 

```
user@pc:~/path/to/pyTradeBinBot$ ./create_env_3.9.sh 
Enter Your VIRTUAL ENV name: tradebin_env
Output Path: /home/usr/path/to/pyTradeBinBot/tradebin_env
```

 To install the pip requirements go to the app folder and activate your virtual env:
  ```
  (tradebot-venv) user@pc:~/root/tradebinbot/ $ pip install -r requirements.txt .
  ```


### Executando o robô
Você pode executar normalmente o robô como um módulo do seu pacote python
```
python -m src.mybot
```

### Principais Dependências
Esses são os principais pacotes utilizados

 - Binance API
 - TA lib para analise tecnica
 - python virtual environment 
 - C instalado


### Módulos Internos

`BinWebSocket` - Módulo responsável por interagir com a binance utilizando websockets

`binalytics` - Módulo responsável por armazenar e tratar os preços da vela, de forma a calcular os indicadores

`binOrderSim` - Módulo utilizado pra simular a carteira, registrando ordens

`logManager` - Módulo responsavel por tratar mensagens e mostrar imagens na tela

`orderManager` - Módulo que utiliza a API da binance para realizar as ordens de compra e venda diretamente na corretora.

### Resultados

  Balanço final positivo em operação de demonstração com baixos valores para RSI e contratos

![alt text](images/SUCCESS%20TEST%201.png)

  Orders registered by the simulated wallet 

![alt text](images/LIVE_ORDER_REGISTER.png)


### Possíveis erros e troubleshooting 

#### Erros de valores no Numpy
Pode haver uma incompantibilidade do numpy já estalado na máquina e a versão utilizada pelo código, caso a instalação pelos requirements apresente problemas, você pode tentar dar upgrade na biblioteca `numpy` manualmente.

#### Mensagem de erro
```
ValueError: numpy.ndarray size changed, may indicate binary incompatibility. Expected 96 from C header, got 80 from PyObject
```
#### Solução 
Fazer o upgrade da versão da biblioteca `numpy`
```
pip install --upgrade numpy
```
#### Falha na instalação da TA-Lib
A biblioteca TA-Lib utiliza um código em linguagem C em conjunto com a linguagem Python. Para a instalação ocorrer sem problemas, é necessário que o usuário tenha a biblioteca em C instalada e o setup feito corretamente no sua máquina.

#### Mensagem de erro
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
#### Solução 
Refazer a instalação da TA-LIB

#### Mal funcionamento da biblioteca websocket
A biblioteca pode apresentar mal funcionamento caso o usuário tenha outras versões da biblioteca `websocket` instalada ou caso tenha criado um arquivo com o nome `websocket.py`junto ao pacote.

#### Mensagem do erro
```self.ws = websocket.WebSocketApp(wsurl,on_open=self.on_open,on_message=self.on_message,on_close=self.on_close)
AttributeError: module 'websocket' has no attribute 'WebSocketApp'
```

#### Solução
Reinstalar a biblioteca websocket individualmente utilizando o comando `pip`.

Primeiro remover as duas bibliotecas
```
pip uninstall websocket-client
pip uninstall websocket
```
E então reinstalar.
```
pip install websocket-client
pip install websocket
```
##### Solução bônus
O usuário pode utilizar o comando `locate` para buscar por arquivos nos eu computador e e encontrar o conflito
```
locate websocket.py
```




