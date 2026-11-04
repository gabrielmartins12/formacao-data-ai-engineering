# Ementa detalhada — 48 semanas / 480 horas

**Carga:** 10h por semana; progressão por competências. **Objetivo:** Engenharia de Dados Júnior com Engenharia de Software, BI e IA. Este documento é a especificação curricular; apostilas, datasets e soluções devem ser desenvolvidos e validados separadamente.

**Formato por semana:** aula 1 (2h, fundamentos), aula 2 (3h, laboratório guiado), aula 3 (3h, desafio independente), aula 4 (2h, revisão, testes e avaliação). Critérios gerais: explicação técnica, artefato reproduzível, testes adequados, segurança, documentação e revisão por PR. Avançar somente com domínio demonstrado; referência 70/100 sem falhas críticas.

## Módulo 1 — Fundamentos de programação

### Semana 01 — Linux e terminal

- **Aula 1 — teoria (2h):** filesystem, permissões, processos, pipes, grep/find, bash e ambientes.
- **Aula 2 — laboratório (3h):** automatizar validação de arquivos CSV com shell.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** script executável, erros tratados e comandos explicados.

### Semana 02 — Git e GitHub

- **Aula 1 — teoria (2h):** commits, branches, merge, conflitos, PR, .gitignore e revisão.
- **Aula 2 — laboratório (3h):** criar branch, abrir PR e resolver conflito simulado.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** histórico limpo e revisão reproduzível.

### Semana 03 — Python essencial

- **Aula 1 — teoria (2h):** tipos, controle de fluxo, funções, escopo, mutabilidade e tipagem.
- **Aula 2 — laboratório (3h):** classificar receitas e despesas com funções.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** testes de casos válidos e inválidos.

### Semana 04 — Algoritmos e estruturas

- **Aula 1 — teoria (2h):** listas, dicionários, sets, pilhas, filas, busca, ordenação e Big O.
- **Aula 2 — laboratório (3h):** deduplicar transações e comparar estruturas.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** medição e justificativa de complexidade.

### Semana 05 — Arquivos, Pandas e logs

- **Aula 1 — teoria (2h):** CSV, JSON, pathlib, encoding, exceptions, Pandas e logging.
- **Aula 2 — laboratório (3h):** normalizar extratos sintéticos heterogêneos.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** linhas reconciliadas e logs úteis.

## Módulo 2 — Engenharia de Software

### Semana 06 — Orientação a objetos

- **Aula 1 — teoria (2h):** classes, composição, herança, encapsulamento, dataclasses e protocolos.
- **Aula 2 — laboratório (3h):** modelar Conta, Transação e importadores.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** substituir implementação sem mudar regras.

### Semana 07 — SOLID e refatoração

- **Aula 1 — teoria (2h):** SRP, OCP, LSP, ISP, DIP, coesão, acoplamento e code smells.
- **Aula 2 — laboratório (3h):** refatorar importador monolítico.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** testes preservados e responsabilidades claras.

### Semana 08 — Arquitetura de aplicações

- **Aula 1 — teoria (2h):** domínio, aplicação, infraestrutura, serviços, repositórios, DTOs e DI.
- **Aula 2 — laboratório (3h):** separar regras financeiras da persistência.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** troca de adaptador sem afetar domínio.

### Semana 09 — Testes automatizados

- **Aula 1 — teoria (2h):** pytest, fixtures, mocks, parametrização, cobertura e integração.
- **Aula 2 — laboratório (3h):** testar regras, erros e importação.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** regressões identificadas por testes.

### Semana 10 — PostgreSQL inicial

- **Aula 1 — teoria (2h):** DDL/DML, PK/FK, constraints, NULL, transações, psycopg.
- **Aula 2 — laboratório (3h):** persistir transações e executar rollback.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** integridade e idempotência demonstradas.

## Módulo 3 — SQL e Backend

### Semana 11 — SQL relacional

- **Aula 1 — teoria (2h):** SELECT, WHERE, JOIN, GROUP BY, HAVING e subqueries.
- **Aula 2 — laboratório (3h):** relatórios de receitas e despesas por categoria.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** consultas corretas sem duplicação por JOIN.

### Semana 12 — SQL analítico

- **Aula 1 — teoria (2h):** CTE, window functions, índices, EXPLAIN ANALYZE e tuning.
- **Aula 2 — laboratório (3h):** saldo acumulado e ranking de categorias.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** comparação fundamentada de planos.

### Semana 13 — HTTP e REST

- **Aula 1 — teoria (2h):** métodos, headers, JSON, status, contratos, OpenAPI, paginação.
- **Aula 2 — laboratório (3h):** especificar API de transações.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** contratos e erros documentados.

### Semana 14 — FastAPI

- **Aula 1 — teoria (2h):** Pydantic, rotas, dependências, serviços, validação e testes.
- **Aula 2 — laboratório (3h):** CRUD de transações com PostgreSQL.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** testes de integração e paginação.

### Semana 15 — Segurança de API

- **Aula 1 — teoria (2h):** authn/authz, hashing, JWT conceitos, OWASP, CORS e secrets.
- **Aula 2 — laboratório (3h):** restringir endpoints por papéis.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** acesso cruzado bloqueado em testes.

## Módulo 4 — Scraping, Crawling e ETL

### Semana 16 — HTTP e parsing

- **Aula 1 — teoria (2h):** requests/httpx, DOM, CSS selectors, Beautiful Soup e encoding.
- **Aula 2 — laboratório (3h):** extrair tabelas de HTML autorizado.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** parsing testado com fixtures.

### Semana 17 — Scraping resiliente

- **Aula 1 — teoria (2h):** paginação, sessões, timeout, retries, 429, rate limit e caching.
- **Aula 2 — laboratório (3h):** coletar catálogo paginado autorizado.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** falhas e duplicatas tratadas.

### Semana 18 — Arquitetura de crawling

- **Aula 1 — teoria (2h):** URL frontier, BFS/DFS, canonicalização, deduplicação, profundidade e robots.txt.
- **Aula 2 — laboratório (3h):** crawler local com fila e checkpoint.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** retomada sem duplicação e limites respeitados.

### Semana 19 — Scrapy

- **Aula 1 — teoria (2h):** spiders, items, pipelines, middleware, AutoThrottle e exports.
- **Aula 2 — laboratório (3h):** migrar crawler para Scrapy.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** execução configurável e métricas.

### Semana 20 — ETL/ELT

- **Aula 1 — teoria (2h):** batch, watermark, upsert, incremental, idempotência, checkpoint e Parquet.
- **Aula 2 — laboratório (3h):** carregar dados coletados no PostgreSQL.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** reprocessamento seguro.

### Semana 21 — Qualidade de dados

- **Aula 1 — teoria (2h):** schema, nulos, duplicatas, freshness, testes, quarentena e lineage.
- **Aula 2 — laboratório (3h):** validar datasets e gerar relatório.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** anomalias detectadas e isoladas.

## Módulo 5 — Modelagem, dbt e Airflow

### Semana 22 — Modelagem dimensional

- **Aula 1 — teoria (2h):** OLTP/OLAP, grão, fatos, dimensões, star schema e surrogate keys.
- **Aula 2 — laboratório (3h):** modelar mart financeiro.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** grão e medidas coerentes.

### Semana 23 — Warehouse e histórico

- **Aula 1 — teoria (2h):** SCD1/SCD2, Bronze/Silver/Gold, particionamento e histórico.
- **Aula 2 — laboratório (3h):** historizar dimensões.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** consultas temporais corretas.

### Semana 24 — dbt

- **Aula 1 — teoria (2h):** sources, refs, staging, marts, testes, macros, snapshots e docs.
- **Aula 2 — laboratório (3h):** criar projeto dbt analítico.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** dbt build e testes reproduzíveis.

### Semana 25 — Airflow fundamentos

- **Aula 1 — teoria (2h):** DAG, tasks, schedule, data interval, operators, conexões e retries.
- **Aula 2 — laboratório (3h):** orquestrar extração, validação e carga.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** falha simulada recuperada.

### Semana 26 — Airflow operação

- **Aula 1 — teoria (2h):** backfill, catchup, sensors, pools, XCom, Docker e alertas.
- **Aula 2 — laboratório (3h):** executar pipeline conteinerizado.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** backfill idempotente e runbook.

## Módulo 6 — Cloud, Spark e Databricks

### Semana 27 — AWS fundamentos

- **Aula 1 — teoria (2h):** IAM, least privilege, regiões, rede básica, billing e budgets.
- **Aula 2 — laboratório (3h):** desenhar permissões mínimas para S3.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** políticas seguras e custo controlado.

### Semana 28 — AWS dados

- **Aula 1 — teoria (2h):** S3, RDS, Glue, Athena, Parquet, partições e lifecycle.
- **Aula 2 — laboratório (3h):** consultar dados sintéticos via Athena.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** leitura eficiente e permissões verificadas.

### Semana 29 — Spark fundamentos

- **Aula 1 — teoria (2h):** driver, executors, lazy evaluation, DataFrames, shuffle e jobs.
- **Aula 2 — laboratório (3h):** transformar dados em PySpark.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** plano físico interpretado.

### Semana 30 — PySpark otimização

- **Aula 1 — teoria (2h):** joins, broadcast, skew, partition, cache e window.
- **Aula 2 — laboratório (3h):** comparar estratégias de join.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** benchmark e justificativa.

### Semana 31 — Databricks

- **Aula 1 — teoria (2h):** workspace, notebooks, compute, Jobs, Workflows e parâmetros.
- **Aula 2 — laboratório (3h):** pipeline parametrizado em Jobs.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** execução monitorável.

### Semana 32 — Delta Lake

- **Aula 1 — teoria (2h):** ACID, MERGE, schema evolution, time travel e Medallion.
- **Aula 2 — laboratório (3h):** ingestão incremental Delta.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** MERGE idempotente.

### Semana 33 — Governança Lakehouse

- **Aula 1 — teoria (2h):** Unity Catalog, lineage, privilégios, otimização e custo.
- **Aula 2 — laboratório (3h):** documentar controle de acesso e performance.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** acessos e trade-offs demonstrados.

## Módulo 7 — Power BI e DAX

### Semana 34 — Power Query

- **Aula 1 — teoria (2h):** M, query folding, conectores, parâmetros, tipos e limpeza.
- **Aula 2 — laboratório (3h):** combinar fontes financeiras.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** transformações e tipagem verificadas.

### Semana 35 — Modelo tabular

- **Aula 1 — teoria (2h):** star schema, relacionamentos, cardinalidade, filtros e calendário.
- **Aula 2 — laboratório (3h):** montar modelo financeiro.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** ausência de ambiguidade.

### Semana 36 — DAX essencial

- **Aula 1 — teoria (2h):** medidas, contexto de linha/filtro, CALCULATE, SUMX, VAR.
- **Aula 2 — laboratório (3h):** KPIs receita, despesa, saldo e participação.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** validação contra SQL.

### Semana 37 — DAX avançado

- **Aula 1 — teoria (2h):** time intelligence, ALL, ALLSELECTED, tabelas virtuais e performance.
- **Aula 2 — laboratório (3h):** comparativos MoM/YoY e acumulados.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** totais e filtros corretos.

### Semana 38 — BI Service e storytelling

- **Aula 1 — teoria (2h):** refresh, gateway, RLS, permissões, UX, acessibilidade e narrativa.
- **Aula 2 — laboratório (3h):** dashboard executivo publicado.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** RLS e narrativa validados.

## Módulo 8 — DataOps e Streaming

### Semana 39 — Docker

- **Aula 1 — teoria (2h):** Dockerfile, Compose, imagens, volumes, redes e configuração.
- **Aula 2 — laboratório (3h):** conteinerizar API e banco.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** ambiente reproduzível.

### Semana 40 — CI/CD

- **Aula 1 — teoria (2h):** GitHub Actions, lint, type checks, testes, build e deploy.
- **Aula 2 — laboratório (3h):** pipeline de testes e qualidade.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** regressão bloqueia merge.

### Semana 41 — Kafka

- **Aula 1 — teoria (2h):** topics, partitions, producers, consumers, groups e offsets.
- **Aula 2 — laboratório (3h):** emitir eventos sintéticos.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** duplicatas tratadas.

### Semana 42 — Observabilidade streaming

- **Aula 1 — teoria (2h):** windows, DLQ, métricas, logs, alertas, SLO e incidentes.
- **Aula 2 — laboratório (3h):** monitorar consumidor e simular falha.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** runbook e recuperação.

## Módulo 9 — Engenharia de IA

### Semana 43 — LLMs

- **Aula 1 — teoria (2h):** tokens, contexto, embeddings, prompting, APIs, custo e privacidade.
- **Aula 2 — laboratório (3h):** classificar descrições sintéticas.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** saída validada e custo registrado.

### Semana 44 — RAG

- **Aula 1 — teoria (2h):** chunking, embeddings, vector/hybrid search, reranking e citações.
- **Aula 2 — laboratório (3h):** indexar documentação do projeto.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** respostas rastreáveis.

### Semana 45 — Agentes

- **Aula 1 — teoria (2h):** tool calling, workflows, estado, limites e autorização.
- **Aula 2 — laboratório (3h):** consultas financeiras somente leitura.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** chamadas fora do escopo bloqueadas.

### Semana 46 — LLMOps

- **Aula 1 — teoria (2h):** evals, testes, observabilidade, prompt injection e FastAPI.
- **Aula 2 — laboratório (3h):** integrar assistente e suíte de avaliação.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** testes de regressão e segurança.

## Módulo 10 — Produto e carreira

### Semana 47 — FinData AI ponta a ponta

- **Aula 1 — teoria (2h):** arquitetura, ingestão, PostgreSQL, Airflow, Lakehouse, BI, API e IA.
- **Aula 2 — laboratório (3h):** integrar componentes com dados sintéticos.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** pipeline e demonstração ponta a ponta.

### Semana 48 — Portfólio e entrevistas

- **Aula 1 — teoria (2h):** ADRs, documentação, demo, SQL/Python, arquitetura e storytelling.
- **Aula 2 — laboratório (3h):** publicar documentação e apresentar projeto.
- **Aula 3 — desafio (3h):** ampliar o laboratório com um caso extremo, um requisito adicional e verificações independentes, sem receber solução pronta.
- **Aula 4 — avaliação (2h):** revisar código, executar testes, defender decisões e explicar limites da solução.
- **Critério específico:** entrevista simulada e revisão técnica.

## Projetos integradores

1. CLI de extratos sintéticos e aplicação modular.
2. API financeira em FastAPI e PostgreSQL.
3. Web Intelligence Crawler responsável e ETL incremental.
4. Pipeline dbt/Airflow e Lakehouse em Spark/Databricks.
5. Dashboard executivo Power BI com DAX e RLS.
6. FinData AI com RAG e agentes seguros.

**Ambientes:** Python/Linux local; Power BI Desktop requer Windows; AWS/Databricks somente com controle de custos. Respeitar robots.txt, termos e limites de acesso. Não versionar credenciais ou dados reais.
