# TradeBinBot - A simple Python live trading robot

  Simule aplicações de trade baseadas em indicador!

  ![alt text](images/RUNNING-BOT.png)

  Essa aplicação foi desenvolvida como um escopo de estudo para robôs de trade. 

  Desenvolvida inicialmente para ser futuramente integrado ao Django, possibilitando a interação com o usuário por meio de um front-end

## Instalação

  É recomendado que a instalação seja feita em um ambiente isolado, recomendamos o `python virtual-env`, você pode encontrar informações nesse  [link](https://docs.python.org/3/library/venv.html).

  To install the pip requirements go to the app folder and activate your virtual env:
  ```
  (tradebot-venv) user@pc:~/root/tradebinbot/ $ pip install -r requirements.txt .
  ```

### Módulos 

`BinWebSocket` - Módulo responsável por interagir com a binance utilizando websockets

`binalytics` - Módulo responsável por armazenar e tratar os preços da vela, de forma a calcular os indicadores

`binOrderSim` - Módulo utilizado pra simular a carteira, registrando ordens

`logManager` - Módulo responsavel por tratar mensagens e mostrar imagens na tela

`orderManager` - Módulo utilizado para realizar ordens e compras na binance ( NÃO UTILIZADO )


### Resultados

  Balanço final positivo em operação de demonstração com baixos valores para RSI e contratos

![alt text](images/SUCCESS%20TEST%201.png)

  Orders registered by the simulated wallet 

![alt text](images/LIVE_ORDER_REGISTER.png)