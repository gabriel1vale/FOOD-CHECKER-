# 🛒 FOOD CHECKER - WEBCRAWLER

Este é um projeto desenvolvido como parte do curso de **Big Data no Agronegócio** na **FATEC Shunji Nishimura**. Desenvolvido para a disciplina de Projeto Integrador, o FOOD CHECKER envolveu a criação de um webcrawler para coletar informações de produtos básicos de mercados da região de Marília/SP, e um site responsivo para exibir os resultados.

---

## 📋 Sobre o Projeto

O Food Checker é um sistema de comparação de preços que:

- **Coleta dados** de produtos básicos de dois supermercados: **Tauste** e **Amigão**
- **Categorias rastreadas:** Arroz, Feijão, Açúcar, Óleo e Farinha
- **Exporta** os dados coletados para arquivos CSV
- **Exibe** os resultados em um site responsivo com tabelas comparativas

---

## 📁 Estrutura do Projeto

```
FOOD-CHECKER-/
├── README.md                      # Documentação do projeto
├── FOODCHECKER - MVP.pdf          # Apresentação do projeto (MVP)
├── códigos_food_checker.py        # Script do webcrawler (Python)
└── Site/
    ├── index.html                 # Página principal do site
    └── img/
        └── logocolorida.png       # Logo do projeto
```

---

## 🚀 Pré-requisitos

- [Python 3](https://www.python.org/downloads/)
- Bibliotecas Python:
  - `requests`
  - `beautifulsoup4`

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/gabriel1vale/FOOD-CHECKER-.git
   cd FOOD-CHECKER-
   ```

2. Instale as dependências:
   ```bash
   pip install requests beautifulsoup4
   ```

## ▶️ Como Usar

1. **Executar o webcrawler** para coletar os dados:
   ```bash
   python códigos_food_checker.py
   ```
   Os dados serão salvos em arquivos CSV (ex: `arroz_tauste.csv`, `feijao-amigao.csv`).

2. **Visualizar os resultados** abrindo o site:
   ```
   Site/index.html
   ```
   Abra o arquivo diretamente no navegador para visualizar as tabelas de preços.

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia |
|-----------|-----------|
| **Web Scraping** | Python, BeautifulSoup, Requests |
| **Frontend** | HTML5, CSS3 |
| **Framework CSS** | [W3.CSS](https://www.w3schools.com/w3css/) |
| **Dados** | CSV |
| **Metodologia** | SCRUM e MVP |
| **Ferramentas Externas** | Adobe Illustrator (logo), PowerPoint (slides), Excel + conversor CSV para tabelas HTML |

---

## 🔗 Acesso ao Projeto

- **GitHub:** https://github.com/gabriel1vale/FOOD-CHECKER-
- **GitLab:** https://gitlab.com/BDAg/food-checker
