#!/usr/bin/env python3
"""
Integra questões IBGP-style geradas por IA externa no HTML.

Uso:
    python3 integrar_questoes.py <arquivo_questoes.json> <disciplina>

Espera JSON com formato:
    { "blocos": [ { "topico": "...", "questoes": [ {enunciado, alternativas,
      correta, dificuldade, explicacao, textoBase?} ] } ] }

Substitui apenas o array `questoes` das aulas com tópico correspondente,
preservando teoria (intro, seções, exemplos, dicas, resumo).
"""
import json
import re
import sys
from pathlib import Path

HTML_PATH = Path(__file__).resolve().parent.parent.parent / "plano-estudos-contagem-2026.html"


def find_conteudo_bounds(html: str) -> tuple[int, int]:
    m = re.search(r"const CONTEUDO_INTEGRADO\s*=\s*", html)
    if not m:
        raise SystemExit("CONTEUDO_INTEGRADO não encontrado")
    i = html.index("{", m.end())
    depth = 0
    in_str = False
    esc = False
    str_ch = None
    j = i
    while j < len(html):
        c = html[j]
        if esc:
            esc = False
        elif in_str:
            if c == "\\":
                esc = True
            elif c == str_ch:
                in_str = False
        else:
            if c in "\"'`":
                in_str = True
                str_ch = c
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    return i, j + 1
        j += 1
    raise SystemExit("Fim do objeto não encontrado")


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    fonte = Path(sys.argv[1])
    disciplina = sys.argv[2]

    novo = json.loads(fonte.read_text(encoding="utf-8"))
    por_topico = {b["topico"]: b["questoes"] for b in novo.get("blocos", [])}
    print(f"[+] Blocos de questões novos: {len(por_topico)}")

    html = HTML_PATH.read_text(encoding="utf-8")
    i, end = find_conteudo_bounds(html)
    obj = json.loads(html[i:end])

    trocados = 0
    for a in obj.get("aulas", []):
        if a.get("disciplina") == disciplina and a.get("topico") in por_topico:
            a["questoes"] = por_topico[a["topico"]]
            trocados += 1
            print(f"    ✓ {a['topico']}: {len(a['questoes'])} questões")

    print(f"[+] Aulas atualizadas: {trocados}/{len(por_topico)}")

    novo_html = html[:i] + json.dumps(obj, ensure_ascii=False) + html[end:]
    HTML_PATH.write_text(novo_html, encoding="utf-8")
    print(f"[✓] HTML atualizado ({len(novo_html):,} bytes)")


if __name__ == "__main__":
    main()
