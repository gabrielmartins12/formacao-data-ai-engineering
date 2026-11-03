# Laboratório inicial — Semana 01

## História de usuário

Como analista financeiro, quero importar transações sintéticas de bancos diferentes para obter um resumo de receitas e despesas.

## Preparação

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pytest
python src/resumo.py
```

## Atividade

1. Leia `data/exemplo/transacoes.csv`.
2. Verifique colunas, tipos, valores faltantes e duplicados.
3. Calcule receitas, despesas e saldo.
4. Acrescente um teste para entrada duplicada.
5. Registre no README o que aprendeu e os comandos usados.

**Desafio sem solução:** modifique a aplicação para rejeitar valores não numéricos com mensagem clara, sem interromper o processamento das demais linhas válidas.
