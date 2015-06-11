door-strut-simulator
====================

Door simulator for Home Shell system (baseado em: https://github.com/alisonbnt/lamp-strut-simulator)

### Descrição ###
*Este é um projeto complementar ao [Home Shell](http://github.com/alisonbento/home-shell). Verifique antes de qualquer coisa!*

Simulador de portas feito em Python 2.7 que se integra ao sistema Home Shell.

### Requisitos ###

Para executar este simulador, você vai precisar de:
* Python 2.7 contendo os seguintes módulos (últimas versões disponíveis recomendadas):
  * Flask
  * Pygame

### Executando ###

```
python app.py
```

Este comando abrirá uma janela contendo uma porta. Você pode acessá-la pelo endereço

```
http://localhost:5001
```

### Comandos ###

* / - Porta como um todo
* /services - Serviços da porta
* /services/nome_servico - executa o serviço "nome_servico"
* /status - Lista os status da porta
