#!/usr/bin/env python3
"""Injeta a data/hora do ultimo commit no index.html.

Grava ISO 8601 em BUILD_FALLBACK para o rodape nunca ficar vazio,
mesmo se a API do GitHub falhar (rate limit / offline / file://).

Uso:  python3 build.py
"""
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
ALVO = RAIZ / "index.html"
MARCA = "__BUILD__"


def data_commit() -> str:
    """Data ISO do HEAD. Cai para 'agora' se nao houver git."""
    try:
        saida = subprocess.run(
            ["git", "log", "-1", "--format=%cI"],
            cwd=RAIZ, capture_output=True, text=True, timeout=15,
        )
        iso = saida.stdout.strip()
        if iso:
            return iso
    except Exception:
        pass
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def main() -> int:
    if not ALVO.exists():
        print(f"ERRO: {ALVO} nao existe", file=sys.stderr)
        return 1

    html = ALVO.read_text(encoding="utf-8")
    iso = data_commit()

    # aceita tanto a marca crua quanto uma data ja injetada antes
    padrao = re.compile(r"const BUILD_FALLBACK = '[^']*';")
    novo = f"const BUILD_FALLBACK = '{iso}';"

    if not padrao.search(html):
        print("ERRO: BUILD_FALLBACK nao encontrado no index.html", file=sys.stderr)
        return 1

    html = padrao.sub(novo, html, count=1)
    ALVO.write_text(html, encoding="utf-8")

    print(f"OK: BUILD_FALLBACK = {iso}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())