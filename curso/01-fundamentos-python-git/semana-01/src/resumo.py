"""Exemplo inicial: resumo de transações sintéticas."""
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "exemplo" / "transacoes.csv"


def resumir(path: Path = DATA) -> dict[str, float]:
    df = pd.read_csv(path)
    if "valor" not in df.columns:
        raise ValueError("Coluna obrigatória ausente: valor")
    valores = pd.to_numeric(df["valor"], errors="raise")
    receitas = round(float(valores[valores > 0].sum()), 2)
    despesas = round(float(-valores[valores < 0].sum()), 2)
    return {"receitas": receitas, "despesas": despesas, "saldo": round(receitas - despesas, 2)}


if __name__ == "__main__":
    print(resumir())
