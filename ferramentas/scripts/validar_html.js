#!/usr/bin/env node
// Valida a sintaxe JS dos <script> inline do HTML principal.
// Uso: NODE_PATH=/opt/node22/lib/node_modules node validar_html.js
const fs = require("fs");
const path = require("path");

const HTML = path.resolve(__dirname, "..", "..", "plano-estudos-contagem-2026.html");
const html = fs.readFileSync(HTML, "utf-8");
const scripts = [...html.matchAll(/<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/g)];

let ok = true;
scripts.forEach((m, i) => {
  try {
    new Function(m[1]);
    console.log(`script ${i}: OK (${m[1].length.toLocaleString()} chars)`);
  } catch (e) {
    ok = false;
    console.error(`script ${i}: FAIL — ${e.message.slice(0, 200)}`);
  }
});
process.exit(ok ? 0 : 1);
