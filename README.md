# projeto-engenharia-de-software

1. Objetivo do Laboratório
Compreender o domínio do problema, definir o escopo inicial do projeto e estruturar o trabalho em grupo, estabelecendo a base conceitual para a evolução do sistema ao longo da disciplina.
2. Definição do Domínio do Sistema
Descrever, em poucas linhas:
•	Qual é o domínio do sistema?
  o	O sistema está inserido no domínio de comércio eletrônico, com foco na venda integrada de ingressos para shows e produtos de vestuário temáticos relacionados aos eventos disponíveis na plataforma.
•	Qual problema real ele resolve?
  o	O problema real que o sistema resolve é a fragmentação da experiência de compra, na qual usuários precisam utilizar plataformas distintas para adquirir ingressos e produtos relacionados aos shows. A proposta do sistema é centralizar essas operações em um único ambiente, proporcionando uma experiência de compra unificada, mais prática e eficiente.
•	Quem são os principais usuários?
  o	Os principais usuários do sistema são os clientes, que realizam a compra de ingressos e vestuário, e os administradores da plataforma, responsáveis pelo cadastro de shows, ingressos, produtos de vestuário e pela gestão básica das vendas.

3.  Visão Geral do Sistema
Preencher os itens abaixo:
•	Nome do sistema: Show&Wear.
•	Usuários principais: Clientes e Administradores.
•	Principais funcionalidades (alto nível)
  o	Comprar ingressos de shows e peças de vestuário do respectivo tema.
  o	Controle de pagamento online.
  o	Carrinho de compras.
  o	Login e cadastro do usuário.
  o	Edição das informações site apenas (pelo administrador).
  o	Barra de busca de produtos.

4. Identificação dos Processos de Negócio
Identificar de 2 a 4 processos principais do domínio.
Para cada processo, descrever:
•	Nome do processo
•	Entrada
•	Saída
•	Atores envolvidos

Processo 1: Compra de Ingressos
•	Nome do processo: Compra de ingressos para shows
•	Entrada: Seleção do show, quantidade de ingressos e dados do cliente
•	Saída: Ingressos adicionados ao pedido e registro da compra no sistema
•	Atores envolvidos: Cliente, sistema de ecommerce, API de pagamento

Processo 2: Compra de Vestuário Temático
•	Nome do processo: Compra de produtos de vestuário temáticos
•	Entrada: Seleção de produtos de vestuário, escolha de tamanho e quantidade
•	Saída: Produtos adicionados ao pedido e atualização do estoque após a confirmação da compra
•	Atores envolvidos: Cliente, sistema de ecommerce

Processo 3: Processamento de Pagamento
•	Nome do processo: Processamento de pagamento do pedido
•	Entrada: Dados do pedido e informações de pagamento do cliente
•	Saída: Confirmação ou recusa do pagamento e atualização do status do pedido
•	Atores envolvidos: Cliente, sistema de ecommerce, API de pagamento

Processo 4: Gestão de Shows e Produtos
•	Nome do processo: Cadastro e gestão de shows e produtos de vestuário
•	Entrada: Dados de shows, ingressos e produtos de vestuário fornecidos pelo administrador
•	Saída: Shows e produtos disponíveis para venda no sistema
•	Atores envolvidos: Administrador, sistema de ecommerce

5. Diagrama Simplificado de Processo
Representar os processos identificados usando fluxograma simples
<img width="900" height="288" alt="image" src="https://github.com/user-attachments/assets/5e645b81-c657-4fbb-ac0d-66e5bd3b4b4c" />

6. Preparação do Ambiente
•	Criar repositório do projeto (Git)
o	https://github.com/Ryu2525/projeto-engenharia-de-software
•	Definir linguagem e framework
o	Python e FastAPI
•	Registrar essas decisões no README  
