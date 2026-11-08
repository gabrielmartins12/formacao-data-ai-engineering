# FinData AI — laboratório autoral

## MVP inicial
Dados fictícios CSV → leitura e validação Python → PostgreSQL → consultas SQL → API FastAPI → testes e logs.

## Requisitos incrementais
1. Classificar transações.
2. Somar gastos por categoria.
3. Validar CSV (data, categoria, valor, duplicação).
4. Modelar tabelas transacoes e categorias.
5. Importar com SQL parametrizado e idempotência.
6. Expor GET /resumo com filtros de período/categoria.
7. Adicionar testes, logs e execução reproduzível.

## Critérios transversais
- Dados exclusivamente sintéticos.
- Nenhuma credencial no repositório.
- Valores financeiros com Decimal ou NUMERIC, não float para cálculos monetários definitivos.
- Tratar registros inválidos explicitamente.
- Documentar execução, testes e decisões.
- Cada entrega deve ser explicável pelo aluno.

**Não começar com Open Finance, scraping bancário, Airflow ou LLMs.**