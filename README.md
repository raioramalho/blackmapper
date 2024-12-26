# Blackmapper [![](https://img.shields.io/github/last-commit/raioramalho/blackmapper.svg)](https://github.com/raioramalho/blackmapper/releases/) [![](https://img.shields.io/github/release-date/raioramalho/blackmapper.svg?style=popout)](https://github.com/raioramalho/blackmapper) [![](https://img.shields.io/github/release/raioramalho/blackmapper.svg?style=popout)](https://github.com/raioramalho/blackmapper/releases) [![Twitter Follow](https://img.shields.io/twitter/follow/raioramalho.svg?style=social&label=Follow)](https://twitter.com/raioramalho)

```
# Blackmapper

O **Blackmapper** é um framework desenvolvido para a injeção física de códigos utilizando placas como Arduino, PIC e Teensy. Este projeto permite que dispositivos de hardware emulem entradas de teclado e mouse para automatizar tarefas ou executar scripts pré-definidos.

## Principais Funções e Classes

- **Função `main`**: Ponto de entrada do programa, responsável por interpretar os argumentos da linha de comando e iniciar o processo de injeção de código.

- **Classe `Device`**: Representa o dispositivo de hardware conectado (por exemplo, Arduino ou Teensy) e contém métodos para estabelecer comunicação e enviar comandos.

- **Função `inject_code`**: Gerencia o processo de envio do código especificado para o dispositivo selecionado, garantindo que a injeção ocorra conforme o esperado.

## Arquitetura do Projeto

O projeto está organizado da seguinte forma:

- **Diretório `payloads/`**: Contém scripts pré-definidos que podem ser injetados nos dispositivos.

- **Arquivo `blackmapper`**: Script principal que coordena a operação do framework.

- **Arquivo `README.md`**: Fornece informações sobre o projeto, incluindo instruções de uso e configuração.

- **Arquivo `LICENSE`**: Detalha a licença sob a qual o projeto é distribuído.

## Normas de Codificação

O código do projeto segue as seguintes convenções:

- **Nomes de Funções e Variáveis**: Utilizam o padrão `snake_case`, onde palavras são separadas por underscores.

  *Exemplo:*

  ```python
  def inject_code(device, payload):
      # Implementação da função
  ```

- **Nomes de Classes**: Adotam o padrão `PascalCase`, onde cada palavra começa com letra maiúscula e não há separadores.

  *Exemplo:*

  ```python
  class Device:
      # Implementação da classe
  ```

## Créditos e Autores

O projeto foi desenvolvido por:

- **Alan Ramalho** (@raioramalho): [Perfil no GitLab](https://gitlab.com/raioramalho)

- **Acr4n1us**

- **RamalhoSec**

- **DuckyBR** (@TradeCrafter): [Perfil no GitHub](https://github.com/tradecrafter)

Para mais detalhes e acesso ao código-fonte, visite o repositório oficial: [https://github.com/raioramalho/blackmapper](https://github.com/raioramalho/blackmapper)


Usage: blackmapper -h or --help

Global Options:
	--help <>: Show this screen.
	-h <>: Show this screen too.

Compatible boards:
    Arduino Leonardo: (Need a reset button!)
    Arduino Leonardo Micro: (Need a reset button!)
    Arduino Pro Micro: (Need a reset button!)
    Arduino CJMCU Beetle: (Need a reset button!)
    Arduino Tiny USB ATMEGA32U4: (Need a reset button!)

    Teensy: 2.0, 2.0++, 3.0, 3.1++

Setup IDE:
    IDE from adafruit with TeeOnArdu LIB: (https://www.dropbox.com/s/aibtwz1xr5a8tx9/arduino-1.6.4.rar?dl=0)
    Board: TeeOnArdu.
    USBType: Keyboard+Mouse+Joystick.
    Keyboard Layout: Layout from your city.
    Port: Com port of your board.

Credits:
    Alan Ramalho @raioramalho (www.gitlab.com/raioramalho)
    Acr4n1us
    RamalhoSec
    DuckyBR @TradeCrafter (www.github.com/tradecrafter)
