# 🚀 Meu Repositório de Estudos em Python

![Python CI](https://github.com/igorpompeo/Python/actions/workflows/python-test.yml/badge.svg)
![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen)
[![Coverage](https://img.shields.io/codecov/c/github/igorpompeo/Python)](https://codecov.io/gh/igorpompeo/Python)

---

## 🐍 Exercícios de Python - Curso em Vídeo (Gustavo Guanabara)

Este repositório contém minha prática dos exercícios do **Curso de Python 3 - Mundo 01** do [Curso em Vídeo](https://www.cursoemvideo.com/curso/python-3-mundo-1/), com scripts organizados e um menu interativo para facilitar a execução.

---

## 📁 Estrutura do Projeto

```text
.
├── .github/
│   └── workflows/
│       ├── python-test.yml        # CI para testes e verificação do código
│       └── python-ci.yml          # CI alternativo
├── Mundo01/
│   ├── Exercicios/                # Exercícios corrigidos e validados
│   └── Desafios/                  # Versões experimentais ou alternativas
├── menu.py                        # Menu interativo para rodar exercícios
├── test_all.py                    # Executa todos os exercícios
├── requirements.txt               # Dependências do projeto
├── setup.cfg                      # Configurações do Flake8 e outros linters
├── .pre-commit-config.yaml        # Configurações do pre-commit
└── README.md                      # Este arquivo
```

---

## ▶️ Como Executar

### 🔹 Requisitos:
- Python 3 instalado

### 🔹 Passos:

```bash
git clone https://github.com/igorpompeo/Python.git
cd Python
python menu.py
```

Digite o número do exercício desejado (sem o prefixo `ex`):

```
Digite o número do exercício (ex: 001), ou 'sair': 004
```

---

## ✅ Testar Todos os Exercícios

Para rodar todos os exercícios automaticamente:

```bash
python test_all.py
```

---

## ⚙️ DevOps com GitHub Actions

Este projeto conta com CI configurado:

- ✅ Lint com **flake8**
- ✅ Formatação com **black**
- ✅ Ordenação de imports com **isort**
- ✅ Pre-commit hooks
- ✅ Execução automática de todos os scripts com `test_all.py`

O workflow é executado em todos os `push`, `pull_request` e pode ser executado manualmente.

---

## 🧼 Pre-commit Hooks

O repositório usa [pre-commit](https://pre-commit.com) para garantir qualidade no código.

### Para instalar os hooks localmente:

```bash
pip install pre-commit
pre-commit install
```

### Para rodar manualmente:

```bash
pre-commit run --all-files
```

---

## 🚧 Em andamento

Este repositório está sendo atualizado conforme avanço no curso. Fique à vontade para acompanhar ou contribuir!

---

## 📚 Créditos

Curso ministrado por [Gustavo Guanabara](https://github.com/gustavoguanabara) no portal [Curso em Vídeo](https://www.cursoemvideo.com/).

---

## 📄 Licença

Este projeto está licenciado sob os termos da licença [MIT](LICENSE).
