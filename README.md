# Show&Wear

## Construção de Serviços

O **Show&Wear** é uma plataforma que integra a compra de ingressos para shows e a compra de roupas/vestuário relacionadas aos eventos em um único fluxo de compra.

Nesta etapa do projeto, foram implementados dois serviços principais relacionados ao processo de finalização da compra:

- **Carrinho Service**
- **Pagamento Service**

O objetivo da implementação é demonstrar a construção de serviços em uma arquitetura orientada a serviços, utilizando coordenação por orquestração e validação por testes unitários e de integração.

---

## Serviços Implementados

### Carrinho Service

O **Carrinho Service** é responsável por gerenciar os itens selecionados pelo usuário durante o processo de compra.

Principais responsabilidades:

- Consultar os itens adicionados ao carrinho.
- Exibir o resumo da compra.
- Calcular o valor total dos itens.
- Criar ou identificar o pedido.
- Acionar o serviço de pagamento durante a finalização da compra.

Arquivo principal relacionado:

```text
carrinho.py
```

---

### Pagamento Service

O **Pagamento Service** é responsável por processar a tentativa de pagamento do pedido.

Principais responsabilidades:

- Receber os dados do pedido e do pagamento.
- Validar os dados recebidos.
- Processar o pagamento.
- Retornar se o pagamento foi aprovado ou recusado.
- Atualizar o status do pedido.

Arquivo principal relacionado:

```text
servicoPagamento.py
```

---

## Arquitetura Adotada

A arquitetura adotada segue o conceito de **orientação a serviços**, separando responsabilidades em serviços específicos.

O estilo de coordenação utilizado foi a **orquestração**.

A escolha pela orquestração ocorreu porque o fluxo de finalização da compra possui uma sequência bem definida:

1. O usuário acessa o carrinho.
2. O Carrinho Service consulta os itens.
3. O Carrinho Service calcula o valor total.
4. O Carrinho Service cria ou identifica o pedido.
5. O Carrinho Service envia os dados ao Pagamento Service.
6. O Pagamento Service processa o pagamento.
7. O resultado é retornado ao usuário.

Nesse fluxo, o **Carrinho Service** coordena a sequência principal da compra e aciona o **Pagamento Service** no momento adequado.

O **Supabase** é utilizado como camada de persistência, responsável por armazenar e consultar dados do sistema, como usuários, carrinho, pedidos e pagamentos. Ele não é considerado um serviço de negócio nesta entrega, mas sim um componente de apoio.

---

## Operações / Endpoints Lógicos

Como o projeto foi desenvolvido com **Streamlit**, os serviços não foram expostos como endpoints REST tradicionais. As operações são representadas por funções e métodos internos do sistema.

### Carrinho Service

Operações principais:

```text
consultar carrinho
adicionar item ao carrinho
gerar resumo do carrinho
finalizar compra
```

Entrada principal:

```text
idUsuario
idItem
tipoItem
quantidade
```

Saída principal:

```text
itens do carrinho
valor total
resumo da compra
status da finalização
```

---

### Pagamento Service

Operação principal:

```text
processar pagamento
```

Entrada principal:

```text
idPedido
dadosPagamento
```

Saída principal:

```text
pagamentoAprovado
statusPagamento
comprovante
mensagem
```

---

## Fluxo de Integração entre Serviços

O fluxo principal de integração ocorre na finalização da compra:

```text
Usuário
  ↓
Carrinho Service
  ↓
Pagamento Service
  ↓
Carrinho Service
  ↓
Usuário
```

Descrição do fluxo:

1. O usuário acessa o carrinho.
2. O Carrinho Service exibe os itens selecionados.
3. O usuário solicita a finalização da compra.
4. O Carrinho Service prepara os dados do pedido.
5. O Carrinho Service chama o Pagamento Service.
6. O Pagamento Service processa o pagamento.
7. O Pagamento Service retorna o resultado.
8. O sistema exibe o status final da compra ao usuário.

---

## Tecnologias Utilizadas

- Python
- Streamlit
- Supabase
- unittest

---

## Como Executar o Projeto

Acesse a pasta do projeto:

```bash
cd Show-Wear/carrinho
```

Crie o ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install streamlit supabase pandas
```

Execute o sistema:

```bash
python3 -m streamlit run usuario.py
```

Após executar o comando, acesse no navegador o endereço exibido no terminal, por exemplo:

```text
http://localhost:8502
```

---

## Como Executar os Testes

### Teste Unitário do Pagamento Service

Para executar o teste unitário do serviço de pagamento:

```bash
python3 -m unittest testePagamento.py -v
```

Esse teste valida a lógica interna do **Pagamento Service**, verificando cenários como pagamento aprovado e pagamento recusado.

---

### Teste de Integração

O teste de integração é validado pelo fluxo completo da aplicação:

1. Iniciar o sistema.
2. Realizar login ou cadastro.
3. Acessar o catálogo.
4. Adicionar um item ao carrinho.
5. Acessar o carrinho.
6. Finalizar a compra.
7. Verificar o retorno do pagamento.

Esse fluxo comprova a comunicação entre o **Carrinho Service** e o **Pagamento Service**.

Caso exista arquivo de teste automatizado para o carrinho, ele pode ser executado com:

```bash
python3 -m unittest testeCarrinho.py -v
```

---

## Evidências de Teste

As evidências dos testes devem conter:

- Print da aplicação rodando no terminal.
- Print do teste unitário do Pagamento Service executado com sucesso.
- Print do usuário logado no sistema.
- Print do catálogo com itens disponíveis.
- Print do item adicionado ao carrinho.
- Print do carrinho com item e valor total.
- Print da finalização da compra com resultado do pagamento.
- Print opcional do Supabase com o pedido atualizado.

---


### Quem somos nós?
Um show não é apenas música, é sobre pertencimento. Você já sentiu aquela insegurança de chegar ao estádio e sentir que seu visual está 'fora de sintonia' com a energia da galera? Com <b>Show&Wear</b> sua única preocupação vai ser cantar todas as músicas. O ingresso e o figurino ficam com a gente. Pagamento facilitado, site blindado e zero fila virtual. O processo é tão fluido quanto a sua música favorita.

### Quais são nossas tecnologias?
Utilizamos um ecossistema robusto baseado em Python: FastAPI para uma comunicação de dados ágil e Streamlit para interfaces dinâmicas. Toda a nossa gestão de dados é centralizada no Supabase via infraestrutura SQL, garantindo escalabilidade e integração segura com APIs de pagamento.

### Diagrama simplificado de Processo
<img width="900" height="288" alt="image" src="https://github.com/user-attachments/assets/17a38959-f767-4955-bc0d-56acc5003fb9" />



### Quem fez o projeto possível?
Matheus do Valle Dourado - 22.224.023-6<br>
João Pedro Peterutto - 22.125.066-5<br>
João Pedro Sabino - 22.224.032-7<br>
Julian Ryu Takeda - 22.224.030-1<br>
Vinícius de Castro Duarte - 22.224.020-2<br>

Para rodar o codigo precisar digitar no terminal: streamlit run usuario.py
