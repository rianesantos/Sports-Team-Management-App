# 🏅 Sports Team Management App

Aplicação completa para **gestão de equipes esportivas**, centralizando todas as principais necessidades de um time em um único sistema.

---

## 🚀 Funcionalidades Implementadas

Todas as funcionalidades principais foram concluídas com sucesso:

1. **Team Roster Management**  
   ➝ Gerenciamento do elenco do time (perfis de jogadores, posições e estatísticas).

2. **Match Scheduling**  
   ➝ Organização e agendamento de partidas e torneios.

3. **Performance Tracking**  
   ➝ Monitoramento e análise de métricas de desempenho individuais e coletivas.

4. **Injury and Health Monitoring**  
   ➝ Acompanhamento de relatórios de saúde e lesões dos jogadores.

5. **Training Schedule Management**  
   ➝ Planejamento e gerenciamento de sessões de treino.

6. **Equipment Inventory Management**  
   ➝ Controle de inventário e gestão de equipamentos esportivos.

7. **Player Recruitment**  
   ➝ Gerenciamento do processo de prospecção e recrutamento de novos jogadores.

8. **Fan Engagement Tools (parcial)**  
   ➝ Recursos para interação com fãs (ex.: enquetes).

9. **Financial Management**  
   ➝ Gestão financeira, incluindo orçamentos e despesas.

10. **Media and Public Relations**  
    ➝ Administração de comunicados de imprensa e atividades de relações públicas.

✅ Todas as funcionalidades acima estão **operacionais**.

---

## ⚠️ Funcionalidade não implementada

- **Integração com Redes Sociais**  
  - Parte do módulo **Fan Engagement Tools** que dependia de APIs externas (Twitter, Facebook, Instagram).  
  - Não foi incluída devido à complexidade de autenticação, permissões e fluxos de API dessas plataformas.  
  - O sistema foi desenvolvido de forma **modular**, portanto essa integração poderá ser adicionada futuramente sem impacto nas demais funcionalidades.

---

## 📦 Instalação e Execução

Clone este repositório:

```bash
git clone https://github.com/seu-usuario/sports-team-management-app.git
cd sports-team-management-app

# 🏆 Sports Team Management App

Este projeto é um sistema de gerenciamento de console para equipes esportivas, focado em demonstrar a aplicação de **Padrões de Projeto (Design Patterns)** para construir uma arquitetura de software modular, robusta e fácil de manter.

## ✨ Visão Geral da Arquitetura

O código original foi refatorado para desacoplar responsabilidades e garantir a integridade dos dados, utilizando 6 padrões de projeto (3 Criacionais e 3 Comportamentais).

### 🏭 Padrões Criacionais (Construction Patterns)

Estes padrões se concentram em como os objetos são criados, isolando a complexidade de instanciação do código que os utiliza.

| Padrão | Aplicação | Benefício |
| :--- | :--- | :--- |
| **Singleton** | Gerenciamento de Dados (`DataManager`) e Conta Financeira. | Garante que o sistema tenha **apenas uma instância** do repositório de dados e do saldo financeiro, mantendo a integridade e um ponto de acesso global. |
| **Factory Method** | Criação de Eventos (`Match` e `Training`). | Isola a lógica de criação de objetos relacionados (Fábricas) do módulo de serviços, permitindo fácil adição de novos tipos de eventos. |
| **Builder** | Criação de Jogadores (`Player`). | Organiza a construção de objetos complexos (Player + Stats) em **etapas passo a passo**, separando a coleta de dados da ordem de montagem. |

### 🧭 Padrões Comportamentais (Behavioral Patterns)

Estes padrões focam na comunicação eficiente e na atribuição de responsabilidades entre os objetos.

| Padrão | Aplicação | Benefício |
| :--- | :--- | :--- |
| **Observer** | Mídias Sociais (`Post` e `Poll`). | Cria um sistema de **notificação automática** e desacoplado. O Post/Poll notifica os observadores (como o console) sem saber como eles reagem. |
| **Command** | Interface de Menus (a ser finalizado). | Encapsula cada ação do menu (ex: "Adicionar Jogador") como um **objeto de comando**, removendo longos blocos condicionais (`if/elif`) da interface. |
| **Strategy** | Listagem de Eventos (Agenda). | Permite definir **algoritmos intercambiáveis** (ex: listar todos os eventos, listar apenas partidas). O cliente executa a estratégia sem se preocupar com os detalhes da implementação. |

## 📁 Estrutura do Projeto

O projeto segue uma arquitetura modular clara:
