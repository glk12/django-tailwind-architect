# Plano de Finalizacao do Site

Este plano foi feito para voce implementar e entender cada decisao tecnica, sem precisar pedir tudo pronto.

## Objetivo
- Finalizar o site institucional com qualidade de producao.
- Resolver primeiro o problema de imagem no mobile (full width).
- Em seguida, criar a secao de contato abaixo dos projetos, com as mesmas animacoes de scroll ja existentes.
- Fechar com polimento, testes e deploy.

## Ordem de Execucao (sem pular)
1. Baseline e diagnostico rapido
2. Corrigir imagem no mobile (full width)
3. Criar secao de contato (layout + animacao)
4. Tornar contato funcional (backend Django)
5. Polimento final (acessibilidade, SEO, performance)
6. Checklist de entrega

---

## 1) Baseline e Diagnostico Rapido

### O que fazer
- Rodar o projeto local e abrir o modo responsivo no navegador.
- Validar visualmente as secoes: Hero, Sobre, Servicos, Projetos.
- Confirmar qual imagem esta com problema no mobile (provavel: bloco de projetos).

### Onde olhar no codigo
- `djangoseed/home/templates/home/home.html`
- `djangoseed/projects/templates/projects/projects.html`
- `djangoseed/home/templates/includes/about.html`
- `djangoseed/templates/base.html`

### O que aprender aqui
- Como a hierarquia de templates Django monta a pagina.
- Como classes utilitarias do Tailwind influenciam largura/espacamento no mobile.

### Criterio de pronto
- Voce consegue apontar com seguranca qual container limita a imagem no mobile.

---

## 2) Corrigir Imagem no Mobile (prioridade 1)

## Hipotese mais provavel
No mobile, a imagem de projetos nao fica full width por causa de container com `max-w-*` + `px-4` e por layout pensado para desktop.

### Onde alterar primeiro
- `djangoseed/projects/templates/projects/projects.html`

### Estrategia recomendada
- No mobile (`< lg`), fazer o bloco visual de imagem "full bleed" (ocupando toda a largura da viewport).
- No desktop (`lg+`), manter o layout atual com offsets e composicao.

### Ajustes tecnicos (conceito)
- Criar wrapper especifico para mobile com largura da viewport (`w-screen`) e compensacao do padding do container (ex.: `relative left-1/2 right-1/2 -ml-[50vw] -mr-[50vw]` ou `-mx-4` se suficiente).
- Garantir que a imagem continue com proporcao consistente (`aspect-*`) e sem distorcao (`object-cover` ou `object-contain` conforme objetivo visual).
- Revisar se o texto "Deslize para ver mais fotos" ainda fica bem posicionado.

### O que testar
- 360px, 390px, 412px de largura.
- 2-3 projetos com quantidade diferente de imagens.
- Scroll horizontal da galeria.

### O que aprender aqui
- Padrao full-bleed dentro de container centralizado.
- Diferenca entre `object-cover` e `object-contain` em UX mobile.

### Criterio de pronto
- A imagem ocupa visualmente 100% da largura do device no mobile.
- Sem overflow quebrado, sem corte estranho de conteudo importante.

---

## 3) Secao de Contato Abaixo de Projetos (prioridade 2)

### Onde criar
- Novo include: `djangoseed/home/templates/includes/contact.html`
- Inserir no fluxo: `djangoseed/home/templates/home/home.html` (depois de `render_projects_list`)

### Requisito de animacao
- Aplicar as classes ja existentes de scroll:
  - `fade-in-section` no container da secao
  - `stagger-fade` nos elementos internos (campos/cards/botoes)
- Nao precisa alterar JS se usar essas classes, porque `scroll_animation.js` ja observa ambas.

### Estrutura sugerida da secao
- Titulo + subtitulo
- Bloco esquerdo: informacoes de contato (WhatsApp, email, endereco)
- Bloco direito: formulario (nome, email, telefone, mensagem)
- CTA claro: "Solicitar Orcamento"

### O que aprender aqui
- Como reutilizar padrao de animacao sem duplicar logica JS.
- Como manter consistencia visual com as outras secoes.

### Criterio de pronto
- Secao aparece abaixo de projetos.
- Animacoes disparam ao entrar em viewport exatamente como as demais secoes.

---

## 4) Tornar Contato Funcional no Django (prioridade 3)

### Abordagem didatica recomendada
Implementar em 2 etapas:

1. Etapa A (rapida): formulario visual com `action="#"` para validar UI/UX.
2. Etapa B (real): enviar para backend com `forms.py` + `views.py`.

### Backend minimo recomendado
- Criar `ContactForm` (campos: nome, email, telefone opcional, mensagem).
- Criar view para receber POST, validar e:
  - salvar em banco (modelo `ContactLead`) **ou**
  - enviar email (SMTP).
- Retornar mensagem de sucesso com `django.contrib.messages`.

### Onde alterar
- `djangoseed/home/forms.py` (novo)
- `djangoseed/home/models.py` (opcional, se salvar lead)
- `djangoseed/home/views.py`
- `djangoseed/home/urls.py`
- `djangoseed/home/templates/includes/contact.html`

### O que aprender aqui
- Ciclo completo de formulario no Django: template -> POST -> validacao -> feedback.

### Criterio de pronto
- Submit sem erro.
- Usuario recebe feedback de sucesso/erro.
- Dados chegam no destino definido (banco ou email).

---

## 5) Polimento Final

### Acessibilidade
- `label for` em todos os campos.
- `alt` coerente nas imagens.
- Contraste suficiente em botoes e textos.

### SEO basico
- Ajustar `title` e `meta description` por pagina principal.
- Hierarquia correta de headings (`h1` unico, depois `h2`).

### Performance
- Revisar peso de imagens.
- Confirmar `loading="lazy"` onde aplicavel.
- Build final de CSS (`npm run build:css`).

### Criterio de pronto
- Lighthouse mobile sem alertas graves de acessibilidade/performance.

---

## 6) Checklist de Entrega

- [ ] Mobile image full width corrigida
- [ ] Secao de contato criada abaixo de projetos
- [ ] Animacoes de scroll funcionando na secao de contato
- [ ] Contato funcional (backend)
- [ ] Teste manual em mobile e desktop
- [ ] CSS buildado para producao
- [ ] Deploy validado

---

## Vue.js: usar agora ou nao?

## Recomendacao direta
Nao aplicar Vue no site inteiro agora.

### Por que
- Projeto atual e Django + templates server-side, ideal para site institucional.
- Seu ganho imediato esta em UX, conteudo, formulario e performance.
- Introduzir Vue global agora aumenta complexidade (bundle, build, manutencao) sem retorno proporcional.

### Onde Vue faria sentido (pontual)
- Filtro dinamico de projetos sem reload.
- Carrossel mais rico com estados complexos.
- Simulador de orcamento em tempo real.

Se quiser experimentar Vue, comece por um componente isolado dentro da secao de projetos, sem migrar a arquitetura inteira.

---

## Sugestao de ritmo (3 dias)

### Dia 1
- Baseline + correcao da imagem mobile full width.

### Dia 2
- Criar secao de contato com animacoes e revisar responsividade.

### Dia 3
- Backend do formulario + polimento + checklist final.
