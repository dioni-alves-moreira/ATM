# 🏧 Simulador de Controle de Fluxo (Caixa Eletrônico)

Simulador em linha de comando desenvolvido em Python que reproduz o funcionamento básico de um caixa eletrônico (ATM), com controle de estoque de notas, abastecimento e saques utilizando o menor número de notas possível.

Projeto desenvolvido como exercício passado pelo professor da disciplina de Programação (Python) na UNICSUL (Universidade Cruzeiro do Sul).

## 📋 Funcionalidades

- **Ver Estoque**: exibe a quantidade atual de notas de R$100, R$50, R$20 e R$10 disponíveis no ATM.
- **Abastecer**: permite adicionar notas de cada denominação ao estoque do ATM.
- **Sacar**: 
  - Valida se o valor do saque é positivo e múltiplo de R$10,00.
  - Calcula a combinação de notas (da maior para a menor denominação) necessária para completar o saque, usando apenas o que está disponível em estoque.
  - Nega o saque caso não exista combinação de notas possível com o estoque atual.
  - Atualiza o estoque após o saque e exibe a quantidade de notas dispensadas por denominação, além de data e hora da operação.
- Menu interativo no terminal para escolha da operação.

## 🛠️ Tecnologias

- **Python 3**
- Módulo `datetime` (biblioteca padrão) para registro de data/hora

## ▶️ Como executar

1. Certifique-se de ter o Python 3 instalado:
   ```bash
   python3 --version
   ```

2. Clone ou baixe este repositório.

3. Execute o script:
   ```bash
   python3 ATM.py
   ```

4. Siga as instruções no menu exibido no terminal.

## 💻 Como usar

Ao rodar o programa, um menu será exibido com as opções:

```
UNICSUL - SIMULADOR DE CONTROLE DE FLUXO - VERSÃO 2026 31/08/2026
    0 - VER ESTOQUE
    1 - ABASTECER
    2 - SACAR
    9 - SAIR
```

- Digite `0` para consultar o estoque atual de notas.
- Digite `1` para abastecer o ATM, informando a quantidade de notas de cada denominação (pode deixar em branco para não adicionar).
- Digite `2` para realizar um saque, informando o valor desejado.
- Digite `9` para encerrar o programa.

### Exemplo de saída (Saque)

```
SAQUE REALIZADO COM SUCESSO!
VALOR: R$180,00

NOTAS DISPENSADAS: 
NOTAS R$100,00: 1
NOTAS R$50,00: 1
NOTAS R$20,00: 1
NOTAS R$10,00: 1

DATA/HORA: 31/08/2026 14:32:10
```

## 📌 Observações

- O estoque de notas é iniciado zerado — é necessário abastecer o ATM antes de realizar saques.
- O cálculo das notas segue a estratégia "gulosa" (da maior para a menor denominação), o que pode não encontrar uma combinação mesmo havendo saldo suficiente em outras denominações menores.
- O estoque não é persistido em arquivo ou banco de dados; é reiniciado a cada execução do programa.

## 📄 Licença

Este projeto é de uso educacional/acadêmico.
