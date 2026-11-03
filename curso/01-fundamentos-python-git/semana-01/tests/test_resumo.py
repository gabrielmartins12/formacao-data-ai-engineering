from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from resumo import resumir


def test_resumo_exemplo():
    assert resumir() == {"receitas": 5250.0, "despesas": 769.3, "saldo": 4480.7}
