# Formação em Engenharia de Dados

Trilha prática para desenvolver competências de **Engenharia de Dados Júnior**, incluindo coleta, processamento, orquestração, Lakehouse e entrega analítica.

**Dedicação:** 10 horas/semana. **Referência:** 36 semanas, com avanço por competência.

## Escopo

O eixo central é Engenharia de Dados. Web scraping, BI e Databricks/PySpark são componentes integrados da formação, não trilhas paralelas. IA/LLMs, RAG, desenvolvimento web, Kafka e cloud avançada ficam para uma fase futura.

## Roadmap

| Etapa | Semanas de referência | Conteúdos | Entrega |
|---|---|---|---|
| 1. Linux e Git | 1–3 | Terminal, permissões, Bash, Git/GitHub | Script de validação CSV |
| 2. Python | 4–8 | Lógica, funções, CSV/JSON, exceções, testes, NumPy: arrays, indexação e vetorização | Processador de arquivos |
| 3. SQL e PostgreSQL | 9–12 | JOIN, GROUP BY, CTE, janelas, modelagem relacional | Banco consultável |
| 4. Coleta de dados | 13–16 | APIs, HTTP, Scrapy, Selenium, Playwright, paginação e coleta responsável | Coletor robusto |
| 5. ETL/ELT | 17–20 | NumPy aplicado, Pandas, validação, cargas incrementais, modelagem dimensional | Pipeline Python → PostgreSQL |
| 6. Orquestração | 21–24 | Docker, Compose, Airflow, DAGs, logs e retries | Pipeline agendado |
| 7. Spark e Databricks | 25–28 | Spark, PySpark DataFrames, joins, agregações, Databricks notebooks/jobs, Delta Lake, MERGE, arquitetura Medallion (Bronze/Silver/Gold) e otimização introdutória | Pipeline Lakehouse |
| 8. BI | 29–32 | Power BI, Power Query, DAX essencial, KPIs e dashboards | Dashboard analítico |
| 9. Projeto integrador | 33–36 | Coleta → ETL → PostgreSQL/Delta Lake → Airflow → BI; testes e documentação | Projeto ponta a ponta |

## Método

Teoria, laboratório guiado, desafio independente, revisão, testes e avaliação (referência >=70/100 sem falhas críticas). Avançar por domínio, não apenas por semanas.

## Retomada

Linux/Bash já iniciado, com avaliações teóricas anteriores. Próximo passo: laboratório de validação CSV com Shell. Não reiniciar nem descartar o histórico.

## Documentação

- [Progresso](PROGRESSO.md)
- [Orientações ao mentor](AGENTS.md)
- [Metodologia](docs/METODOLOGIA.md)

> Documentos anteriores em `curso/` e `docs/` podem conter planos legados de 36–48 semanas. O roadmap acima é a referência vigente; preservar e adaptar materiais gradualmente.

Usar dados sintéticos, respeitar termos de uso e robots.txt, não publicar credenciais e verificar custos/limites antes de utilizar recursos Databricks.
