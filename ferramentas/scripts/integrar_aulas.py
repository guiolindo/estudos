#!/usr/bin/env python3
"""
Integra aulas geradas por IA externa (DeepSeek etc) no HTML principal.

Uso:
    python3 integrar_aulas.py <arquivo_aulas.json> <disciplina>

Espera JSON com formato:
    { "aulas": [ { "topico": "...", "disciplina": "...", "intro": "...", ... } ] }

Substitui TODAS as aulas da disciplina informada no HTML pelas do arquivo.
Preserva aulas de outras disciplinas.
"""
import json
import re
import sys
from pathlib import Path

HTML_PATH = Path(__file__).resolve().parent.parent.parent / "plano-estudos-contagem-2026.html"


def repair_deepseek_json(s: str) -> str:
    """Correções comuns em JSON devolvido por DeepSeek."""
    # Envolve "resumo": "..." seguido de ] extraviado (não fecha array)
    s = re.sub(r'("resumo"\s*:\s*"(?:[^"\\]|\\.)*")\s*\]', r'\1', s)
    return s


def find_conteudo_bounds(html: str) -> tuple[int, int]:
    m = re.search(r"const CONTEUDO_INTEGRADO\s*=\s*", html)
    if not m:
        raise SystemExit("CONTEUDO_INTEGRADO não encontrado no HTML")
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
    raise SystemExit("Não achei o final do objeto CONTEUDO_INTEGRADO")


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    fonte = Path(sys.argv[1])
    disciplina = sys.argv[2]

    raw = fonte.read_text(encoding="utf-8")
    novos = json.loads(repair_deepseek_json(raw))
    novas_aulas = novos.get("aulas", [])
    for a in novas_aulas:
        a["disciplina"] = disciplina
    print(f"[+] Novas aulas de {disciplina}: {len(novas_aulas)}")

    html = HTML_PATH.read_text(encoding="utf-8")
    i, end = find_conteudo_bounds(html)
    obj = json.loads(html[i:end])
    antigas = obj.get("aulas", [])

    mantidas = [a for a in antigas if a.get("disciplina") != disciplina]
    obj["aulas"] = mantidas + novas_aulas
    print(f"[+] Mantidas de outras disciplinas: {len(mantidas)}")
    print(f"[+] Total após integração: {len(obj['aulas'])}")

    novo_html = html[:i] + json.dumps(obj, ensure_ascii=False) + html[end:]
    HTML_PATH.write_text(novo_html, encoding="utf-8")
    print(f"[✓] HTML atualizado ({len(novo_html):,} bytes)")


if __name__ == "__main__":
    main()
