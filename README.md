# frases03

Um botão. Uma frase de TI. Um estouro de confete.

Página única, sem framework, sem build, sem dependência. Abre no navegador e funciona.

## O que é

Cada clique sorteia uma frase de TI — mas não só o texto muda: **o humor muda junto**, e com ele a cor do fundo, o brilho, o selo e as partículas do confete.

São quatro humores:

| tom | cor | o que traduz |
|---|---|---|
| **alegria** | âmbar → laranja | quando o deploy passa e ninguém acredita |
| **tristeza** | azul → índigo | o ajuste rápido que virou domingo |
| **cinismo** | ardósia → cinza | dívida técnica organizada em camadas |
| **mojo** | rosa → lilás | quando o regex funciona de primeira |

34 frases, distribuídas entre os quatro.

## Como usar

Abra o `index.html`. Ou:

```bash
python3 -m http.server 3210
# http://localhost:3210
```

**Clique** no botão, ou aperte **Espaço** / **Enter**.

## Detalhes técnicos

- **Zero dependências.** Nenhum npm, nenhum CDN de JS. Só Google Fonts (Inter + JetBrains Mono).
- **Confete em canvas puro**, escrito à mão: ~110 partículas por estouro, com gravidade, arrasto, rotação e achatamento no eixo Y (dá a sensação de girar no ar).
- **Cada tom tem sua física.** Alegria sobe mais e cai devagar; tristeza cai pesado; cinismo quase não sai do chão; mojo explode mais forte.
- **Jackpot a cada 7 cliques** — 220 partículas em leque 360°.
- **Acessibilidade:** `prefers-reduced-motion` desliga todas as animações, `:focus-visible` no botão, `aria-hidden` nas setas decorativas.
- **Sem repetição imediata** — o sorteio nunca devolve a frase atual.
- O `<title>` muda com a frase, então o histórico do navegador tem um registro do que passou.

## Estrutura

```
index.html    # tudo: HTML, CSS e JS em um arquivo
```

## Licença

MIT.