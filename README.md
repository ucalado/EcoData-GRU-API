# EcoData-GRU-API - API de Indicadores Econômicos

## Sobre o Projeto:
Este repositório contém o código-fonte da aplicação desenvolvida para o meu TCC de Pós-Graduação em Desenvolvimento Full Stack pela PUCRS. 
O objetivo principal é a criação de um **Pipeline de Dados Econômicos**, que realiza a leitura de bases SQL e disponibiliza endpoints de pesquisa para análise de dados municipais.
A título de desenvolvimento do TCC, organizei e utilizei alguns dos dados do município de Guarulhos, os quais tenho familiaridade e utilizo diáriamente dentro da Prefeitura.
## Objetivo
Desenvolver uma interface de programação de aplicações (API) baseada em arquitetura REST para a padronização e disponibilização de indicadores econômicos municipais, 
transformando dados estruturados em bancos SQL em formatos de intercâmbio JSON, visando otimizar a geração de relatórios e a análise de dados no setor público.
## Pontos importantes:
**Eficiência Operacional:** A automação via API elimina processos manuais de exportação de planilhas, reduzindo erros humanos e o tempo de resposta do analista.

**Interoperabilidade:** O uso do formato JSON permite que qualquer ferramenta moderna (Power BI, Python, dashboards web) consuma os dados de forma nativa e em tempo real.

**Transparência e Governança:** Ao centralizar o acesso aos dados econômicos em uma API, cria-se um único repositório como fonte de dados, garantindo que todos os relatórios do município utilizem a mesma base de informação.


## Tecnologias e Arquitetura:
A aplicação foi estruturada seguindo as melhores práticas de desenvolvimento web e arquitetura de software:
- **Linguagem:** Python
- **Framework:** FastAPI, SQLAlchemy
- **Banco de Dados:** SQLite

## Endpoints Principais:
| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/v1/caged/caged_setor` | Dados de saldo de empregos por setor(Caged). |
| `GET` | `/v1/caged/caged_ano` | Dados de saldo de empregos por ano(Caged). |
| `GET` | `/v1/eleitores/eleitores` | Consulta quantidade de eleitores por gênero e ano. |
| `GET` | `/v1/eleitores/eleitores_ano` | Consulta quantidade de eleitores por ano. |
| `GET` | `/v1/eleitores/eleitores_mes_ano` | Consulta quantidade de eleitores por mês e ano.  |
| `GET` | `/v1/comex/mensal` | Consulta valores mesais de importação/exportação. |
| `GET` | `/v1/comex/anual` | Consulta valores anuais de importação/exportação. |
| `GET` | `/v1/comex/produtos/{cod_sh6}` | Consulta a classificação de produtos cadastrados no Comexstat. |
| `GET` | `/v1/datasus/cep` | Consulta unidades de saúde do município por cep. |
| `GET` | `/v1/datasus/bairro` | Consulta unidades de saúde do município por bairro. |
| `GET` | `/v1/datasus/cnes` | Consulta unidades de saúde do município por CNES. |


## Como Executar o Projeto:
1. Clone o repositório: `git clone https://github.com/ucalado/EcoData-GRU-API.git`
2. Instale as dependências: pip install -r requirements.txt
3. Configure as variáveis de ambiente no arquivo ".env".
4. Rodar a aplicação: Depende da IDEs utilizada
   
Passos Adicionais Recomendados:
Criar ambiente virtual: python -m venv venv
Ativar ambiente (Windows): .\venv\Scripts\activate
Ativar ambiente (Linux/macOS): source venv/bin/activate


## Licença
Este projeto é acadêmico e segue as diretrizes de dados abertos. Os dados utilizados para testes são anonimizados ou provenientes de bases públicas.
