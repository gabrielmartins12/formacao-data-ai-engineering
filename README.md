# Data & AI Engineering Roadmap

> Formação prática de 36 semanas para entrada no mercado como **Engenheiro de Dados Júnior** e evolução para **Data & AI Engineer**.

**Carga:** 8–10 horas por semana (288–360 horas estimadas). **Foco:** Engenharia de Dados (65%), Engenharia de Software (20%) e Engenharia de IA (15%).

## Como estudar

1. Abra a semana em `curso/` e leia o problema de negócio.
2. Estude os conceitos e referências sugeridas; registre suas próprias anotações.
3. Implemente o laboratório em uma branch `semana-NN`.
4. Resolva o desafio sem pedir a solução pronta ao Codex.
5. Execute os testes, documente decisões e abra um pull request para revisão.
6. Registre sua nota e evolução em `PROGRESSO.md`.

Cada semana tem um **plano de aula e uma atividade avaliativa**, a serem aprofundados durante a formação. Este repositório é o **esqueleto inicial do curso**, não 36 aulas teóricas completas já escritas.

## Trilha

| Fase | Semanas | Área |
|---|---|---|
| 1 | 01–04 | Linux, Git, Python e testes |
| 2 | 05–08 | SQL, PostgreSQL e integração |
| 3 | 09–12 | APIs, scraping, ETL e qualidade |
| 4 | 13–16 | Data Warehouse, dbt e Airflow |
| 5 | 17–22 | AWS, Spark, Databricks e Delta Lake |
| 6 | 23–28 | DataOps, Kafka, Power BI e APIs |
| 7 | 29–36 | Engenharia de IA, produto e carreira |

## Projetos de portfólio

- **FinData AI:** produto integrador de finanças pessoais (somente dados sintéticos até haver autorização e segurança adequadas).
- **Web Intelligence Crawler:** coleta responsável de dados públicos.
- **Lakehouse Analytics:** PySpark, Databricks e Delta Lake com dados sintéticos em escala.
- **AI Knowledge Assistant:** RAG com citações, controles e avaliação.

Veja `projetos/README.md`, `docs/METODOLOGIA.md` e `docs/ROADMAP-CARREIRA.md`.

## Princípios

- Priorize **Python + SQL + ETL + testes** antes de ferramentas distribuídas.
- Projetos devem ter README, testes, logs, dados de exemplo e instruções de execução.
- Não comite dados bancários reais, senhas, tokens ou arquivos `.env`.
- Respeite robots.txt, termos de uso e limites de requisição ao fazer scraping.
- Cloud e Databricks podem gerar custos; use laboratórios com orçamento e limites configurados.

## Licença

Material original de estudo sob licença MIT (ver `LICENSE`). Referências externas devem respeitar os direitos de seus autores.
