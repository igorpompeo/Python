# 🚀 Meu Repositório de Estudos em Python

![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen)
[![CI](https://github.com/igorpompeo/Python/actions/workflows/python-ci.yml/badge.svg)](https://github.com/igorpompeo/Python/actions/workflows/python-ci.yml)
[![Coverage](https://img.shields.io/codecov/c/github/igorpompeo/Python)](https://app.codecov.io/gh/igorpompeo/Python)
[![PyPI](https://img.shields.io/pypi/v/meu_pacote_python.svg)](https://pypi.org/project/meu_pacote_python/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🐍 Exercícios de Python - Curso em Vídeo (Gustavo Guanabara)

Este repositório contém minha prática dos exercícios do **Curso de Python 3 - Mundo 01** do [Curso em Vídeo](https://www.cursoemvideo.com/curso/python-3-mundo-1/), com scripts organizados e um menu interativo para facilitar a execução.

---

## 📦 Instalação
```bash
pip install meu_pacote_python
```

---

## 📁 Estrutura do Projeto

```text
.
├── .github/
│   ├── workflows/
│   │   ├── python-ci.yml          # CI/CD completo com testes e deploy
│   │   └── release-drafter.yml    # Geração automática de changelog
│   └── release-drafter.yml        # Configuração do Release Drafter
├── tests/
│   └── test_dummy.py              # Teste de placeholder
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


## 💻 Uso como Pacote
Após instalar, você pode importar os exercícios diretamente:
```python
from meu_pacote_python.Mundo01.Exercicios import ex001
ex001.ex001()  # Executa o exercício 1
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

## 🧪 Cobertura de Testes

Para verificar a cobertura dos exercícios:

```bash
pytest --cov=Mundo01 --cov-report=term-missing --cov-fail-under=80
```

---

## ⚙️ DevOps com GitHub Actions

Este projeto conta com CI configurado:

- ✅ Testes com **pytest**
- ✅ Análise de segurança com **bandit**
- ✅ Cobertura de testes com **codecov**
- ✅ Publicação automática no **PyPI**
- ✅ Geração de changelog com **Release Drafter**
- ✅ Pre-commit hooks com formatação e lint

O workflow é executado em todos os `push`, `pull_request` e pode ser executado manualmente.

---

## 🤝 Como Contribuir
1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona novo exercício'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

## 🧼 Pre-commit Hooks

O repositório usa [pre-commit](https://pre-commit.com) para garantir qualidade no código.

### Para instalar os hooks localmente:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
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
