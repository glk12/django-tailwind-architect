## Projeto

Este repositório é um site profissional para arquitetos desenvolvido em Django, com interface responsiva estilizada por Tailwind CSS e daisyUI. Ele reúne a estrutura de aplicações e templates necessários para um website institucional moderno, com páginas, componentes e assets organizados para produção e evolução contínua.

---

## 🛠️ Requisitos

Certifique-se de ter as ferramentas a seguir instaladas em sua máquina:

- **Python** (>= 3.12)
- **Node.js** (>= versão 16.x)
- Gerenciador de pacotes como `npm` ou `yarn`

---

## 📦 Instalação

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/glk12/django-tailwind-architect.git
cd django-tailwind-architect
cd djangoseed
```

### 2️⃣ Crie e ative um ambiente virtual Python
```bash
python3 -m venv venv
source venv/bin/activate # No Windows: venv\Scripts\activate
```

### 3️⃣ Instale as dependências Python
```bash
pip install -r requirements.txt
```

### 4️⃣ Instale as dependências JavaScript
```bash
npm install
```

---

## 🔧 Configuração

1. **Migrações do Django**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. **Criação de um superusuário**
    ```bash
    python manage.py createsuperuser
    ```

3. **Build do CSS (Tailwind)**
    ```bash
    npm run build:css
    ```

4. **Configure as variáveis ambiente (`.env` local ou env vars do deploy)**.

---

## ▶️ Execução

Após a configuração, execute o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

Abra seu navegador e acesse: `http://localhost:8000`

---

## 📚 Tecnologias Usadas

- **Django**: Framework back-end Python
- **Tailwind CSS**: Framework de estilização CSS
- **DaisyUI**: Biblioteca de componentes para Tailwind CSS
- **Node.js** e **NPM**: Ferramentas para gerenciar dependências front-end
