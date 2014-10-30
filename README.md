lamp-strut-simulator
====================

Lamp simulator for Home Shell system

### Descrição ###
*Este é um projeto complementar ao [Home Shell](http://github.com/alisonbento/home-shell). Verifique antes de qualquer coisa!*

Simulador de lâmpadas feito em Python 2.7 que se integra ao sistema Home Shell.

### Requisitos ###

Para executar este simulador, você vai precisar de:
* Python 2.7 contendo os seguintes módulos (últimas versões disponíveis recomendadas):
  * Flask
  * Pygame

### Executando ###

```
python app.py
```

Este comando abrirá uma janela contendo uma lâmpada. Você pode acessá-la pelo endereço

```
http://localhost:5000
```

### Comandos ###

* / - Lâmpada como um todo
* /services - Serviços da lâmpada
* /services/nome_servico - executa o serviço "nome_servico"
* /status - Lista os status da lâmpada
