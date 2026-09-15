# 🏧 Simulador de Controle de Fluxo (Caixa Eletrônico)

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Licença](https://img.shields.io/badge/uso-acad%C3%AAmico-lightgrey)

Simulador em linha de comando, desenvolvido em Python, que reproduz o funcionamento básico de um caixa eletrônico (ATM): controle de estoque de notas, abastecimento e saques utilizando o **menor número de notas possível**.

> 📚 Projeto desenvolvido como exercício da disciplina de Programação (Python) na UNICSUL (Universidade Cruzeiro do Sul).

---

## 📋 Sumário

- [Sobre o projeto](#-sobre-o-projeto)
- [Demonstração](#-demonstração)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#️-tecnologias)
- [Como executar](#️-como-executar)
- [Como usar](#-como-usar)
- [Decisões técnicas](#-decisões-técnicas)
- [Desafios e soluções](#-desafios-e-soluções)
- [Aprendizados](#-aprendizados)
- [Melhorias futuras](#-melhorias-futuras)
- [Observações](#-observações)
- [Autor](#-autor)
- [Licença](#-licença)

---

## 🎯 Sobre o projeto

**Problema resolvido:** caixas eletrônicos precisam calcular, a cada saque, a combinação de notas que atende ao valor solicitado usando o mínimo de cédulas — e isso considerando um estoque limitado, que pode não ter todas as denominações disponíveis.

Este projeto simula esse comportamento em um programa de terminal, permitindo:

- Consultar o estoque de notas disponível;
- Abastecer o ATM com novas notas;
- Sacar valores, com o sistema calculando automaticamente a menor quantidade de cédulas necessária.

O objetivo acadêmico foi praticar lógica de programação, estruturas de repetição/condicional, controle de estado (estoque) e formatação de saída para o usuário.

## 🖥️ Demonstração

> 💡 *Sugestão: adicione aqui um print ou GIF do terminal em execução (menu + um saque realizado). Isso deixa o repositório muito mais atrativo para quem visita seu portfólio.*

```
UNICSUL - SIMULADOR DE CONTROLE DE FLUXO - VERSÃO 2026 31/08/2026
    0 - VER ESTOQUE
    1 - ABASTECER
    2 - SACAR
    9 - SAIR
```

## 📋 Funcionalidades

| Opção | Ação | Descrição |
|---|---|---|
| `0` | **Ver Estoque** | Exibe a quantidade atual de notas de R$100, R$50, R$20 e R$10 disponíveis. |
| `1` | **Abastecer** | Adiciona notas de cada denominação ao estoque (pode deixar em branco para não adicionar). |
| `2` | **Sacar** | Valida, calcula e dispensa notas para o valor solicitado. |
| `9` | **Sair** | Encerra o programa. |

Detalhes da operação de saque:

- Valida se o valor é **positivo** e **múltiplo de R$10,00**.
- Calcula a combinação de notas (da maior para a menor denominação) usando apenas o que está disponível em estoque.
- **Nega o saque** caso não exista combinação possível com o estoque atual.
- Atualiza o estoque após a operação e exibe a quantidade de notas dispensadas por denominação, com data e hora do saque.

## 🛠️ Tecnologias

- **Python 3**
- Módulo `datetime` (biblioteca padrão) — registro de data/hora das operações

## ▶️ Como executar

1. Certifique-se de ter o Python 3 instalado:

   ```bash
   python3 --version
   ```

2. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

3. Execute o script:

   ```bash
   python3 ATM.py
   ```

4. Siga as instruções exibidas no menu do terminal.

## 💻 Como usar

Ao rodar o programa, o menu abaixo é exibido:

```
UNICSUL - SIMULADOR DE CONTROLE DE FLUXO - VERSÃO 2026 31/08/2026
    0 - VER ESTOQUE
    1 - ABASTECER
    2 - SACAR
    9 - SAIR
```

- Digite `0` para consultar o estoque atual de notas.
- Digite `1` para abastecer o ATM, informando a quantidade de notas de cada denominação.
- Digite `2` para realizar um saque, informando o valor desejado.
- Digite `9` para encerrar o programa.

**Exemplo de saída (saque de R$180,00):**

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

## 🧠 Decisões técnicas

- **Algoritmo guloso (greedy):** o cálculo das notas percorre as denominações da maior para a menor, dispensando o máximo possível de cada uma antes de passar à próxima. É simples de implementar e eficiente para o escopo do exercício.
- **Estoque em memória:** optei por manter o estoque em variáveis/estruturas em memória (sem arquivo ou banco de dados), já que o foco do projeto é a lógica de cálculo de troco, não persistência de dados.
- **Validação antes do processamento:** valores inválidos (negativos ou não múltiplos de R$10) são barrados antes de qualquer tentativa de cálculo, evitando estados inconsistentes de estoque.

## 🧩 Desafios e soluções

- **Desafio:** o algoritmo guloso pode falhar em encontrar uma combinação mesmo havendo saldo suficiente somado em denominações menores (ex.: sobra de R$20 sem notas de R$10 para fechar um valor específico).
  **Solução adotada:** o saque é negado nesse cenário, com uma mensagem clara ao usuário, em vez de dispensar um valor incorreto.
- **Desafio:** garantir que o estoque não fosse alterado em saques que não pudessem ser completados.
  **Solução adotada:** o cálculo é feito antes de qualquer atualização de estoque; o estoque só é debitado se a combinação for validada com sucesso.

## 📈 Aprendizados

- Prática de estruturas de repetição e condicionais aplicadas a um problema real (troco/dispensação de notas).
- Manipulação de estado (estoque) ao longo da execução do programa.
- Formatação de saída amigável para o usuário no terminal, incluindo data/hora com o módulo `datetime`.
- Percepção prática das limitações de algoritmos gulosos frente a abordagens mais robustas (como programação dinâmica).

## 🚀 Melhorias futuras

- [ ] Persistir o estoque em arquivo (JSON/CSV) ou banco de dados, mantendo o estado entre execuções.
- [ ] Implementar um algoritmo alternativo (ex.: programação dinâmica) para cobrir casos em que a estratégia gulosa falha.
- [ ] Adicionar testes automatizados (`unittest`/`pytest`) para as funções de cálculo de notas e validação de saque.
- [ ] Registrar um histórico de operações (extrato).

## 📌 Observações

- O estoque de notas é iniciado zerado — é necessário abastecer o ATM antes de realizar saques.
- O cálculo das notas segue a estratégia "gulosa" (da maior para a menor denominação), o que pode não encontrar uma combinação mesmo havendo saldo suficiente em outras denominações menores.
- O estoque não é persistido em arquivo ou banco de dados; é reiniciado a cada execução do programa.

## 👤 Autor

Desenvolvido por **[seu nome]** — estudante de [seu curso] na UNICSUL.

[![GitHub](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white)](https://github.com/seu-usuario)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://linkedin.com/in/seu-usuario)

## 📄 Licença

Este projeto é de uso educacional/acadêmico.
