# projeto-engenharia-de-software

1. Objetivo do Laboratório<br>
Compreender o domínio do problema, definir o escopo inicial do projeto e estruturar o trabalho em grupo, estabelecendo a base conceitual para a evolução do sistema ao longo da disciplina.<br><br>
2. Definição do Domínio do Sistema<br>
Descrever, em poucas linhas:<br>
•	Qual é o domínio do sistema?<br>
  o	O sistema está inserido no domínio de comércio eletrônico, com foco na venda integrada de ingressos para shows e produtos de vestuário temáticos relacionados aos eventos disponíveis na plataforma.<br>
•	Qual problema real ele resolve?<br>
  o	O problema real que o sistema resolve é a fragmentação da experiência de compra, na qual usuários precisam utilizar plataformas distintas para adquirir ingressos e produtos relacionados aos shows. A proposta do sistema é centralizar essas operações em um único ambiente, proporcionando uma experiência de compra unificada, mais prática e eficiente.<br>
•	Quem são os principais usuários?<br>
  o	Os principais usuários do sistema são os clientes, que realizam a compra de ingressos e vestuário, e os administradores da plataforma, responsáveis pelo cadastro de shows, ingressos, produtos de vestuário e pela gestão básica das vendas.<br><br>

4.  Visão Geral do Sistema<br>
Preencher os itens abaixo:<br>
•	Nome do sistema: Show&Wear.<br>
•	Usuários principais: Clientes e Administradores.<br>
•	Principais funcionalidades (alto nível)<br>
  o	Comprar ingressos de shows e peças de vestuário do respectivo tema.<br>
  o	Controle de pagamento online.<br>
  o	Carrinho de compras.<br>
  o	Login e cadastro do usuário.<br>
  o	Edição das informações site apenas (pelo administrador).<br>
  o	Barra de busca de produtos.<br><br>

5. Identificação dos Processos de Negócio<br>
Identificar de 2 a 4 processos principais do domínio.<br>
Para cada processo, descrever:<br>
•	Nome do processo<br>
•	Entrada<br>
•	Saída<br>
•	Atores envolvidos<br><br>

Processo 1: Compra de Ingressos<br>
•	Nome do processo: Compra de ingressos para shows<br>
•	Entrada: Seleção do show, quantidade de ingressos e dados do cliente<br>
•	Saída: Ingressos adicionados ao pedido e registro da compra no sistema<br>
•	Atores envolvidos: Cliente, sistema de ecommerce, API de pagamento<br><br>

Processo 2: Compra de Vestuário Temático<br>
•	Nome do processo: Compra de produtos de vestuário temáticos<br>
•	Entrada: Seleção de produtos de vestuário, escolha de tamanho e quantidade<br>
•	Saída: Produtos adicionados ao pedido e atualização do estoque após a confirmação da compra<br>
•	Atores envolvidos: Cliente, sistema de ecommerce<br><br>

Processo 3: Processamento de Pagamento<br>
•	Nome do processo: Processamento de pagamento do pedido<br>
•	Entrada: Dados do pedido e informações de pagamento do cliente<br>
•	Saída: Confirmação ou recusa do pagamento e atualização do status do pedido<br>
•	Atores envolvidos: Cliente, sistema de ecommerce, API de pagamento<br><br>

Processo 4: Gestão de Shows e Produtos<br>
•	Nome do processo: Cadastro e gestão de shows e produtos de vestuário<br>
•	Entrada: Dados de shows, ingressos e produtos de vestuário fornecidos pelo administrador<br>
•	Saída: Shows e produtos disponíveis para venda no sistema<br>
•	Atores envolvidos: Administrador, sistema de ecommerce<br><br>

5. Diagrama Simplificado de Processo<br>
Representar os processos identificados usando fluxograma simples<br>
<img width="900" height="288" alt="image" src="https://github.com/user-attachments/assets/5e645b81-c657-4fbb-ac0d-66e5bd3b4b4c" /><br><br>

6. Preparação do Ambiente<br>
•	Criar repositório do projeto (Git)<br>
o	https://github.com/Ryu2525/projeto-engenharia-de-software<br>
•	Definir linguagem e framework<br>
o	Python e FastAPI<br>
•	Registrar essas decisões no README  <br>
