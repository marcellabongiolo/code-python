# 🐍 Code Python Lab

Repositório de estudos e exercícios em **Python**, com foco em lógica de programação, algoritmos e boas práticas de desenvolvimento.

O projeto atual implementa um validador educacional de números de cartão baseado no **Algoritmo de Luhn**, inspirado no exercício Credit do CS50.

> **Escopo:** a validação é apenas matemática e de formato. O projeto não consulta bancos, emissores ou redes de pagamento e não deve ser usado para validar cartões reais em produção.

## Objetivos

- Praticar lógica de programação com Python.
- Implementar e compreender o Algoritmo de Luhn.
- Trabalhar com funções, validação de entrada e expressões regulares.
- Escrever código legível e modular.
- Criar testes automatizados.
- Utilizar integração contínua com GitHub Actions.

## Funcionalidades

O validador:

- aceita números digitados com espaços ou hífens como separadores;
- rejeita caracteres não permitidos;
- aplica o Algoritmo de Luhn;
- identifica exemplos compatíveis com AMEX, Mastercard e Visa dentro das regras implementadas;
- informa quando o número passa no Luhn, mas não corresponde às bandeiras tratadas pelo exercício.

## Estrutura

```text
code-python/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   └── test_cs50_credit.py
├── .gitignore
├── LICENSE
├── README.md
└── cs50_credit.py
```

## Tecnologias

- Python 3.12+
- Biblioteca padrão do Python
- unittest
- GitHub Actions

## Como executar

Clone o repositório:

```bash
git clone https://github.com/marcellabongiolo/code-python.git
cd code-python
```

Execute o programa:

```bash
python cs50_credit.py
```

Execute os testes:

```bash
python -m unittest discover -s tests -v
```

## Conceitos praticados

- Algoritmo de Luhn
- Validação e normalização de entrada
- Expressões regulares
- Funções e type hints
- Estruturas de repetição
- Testes automatizados
- Integração contínua (CI)

## Próximos passos

O repositório pode receber novos exercícios e pequenos projetos de Python à medida que o laboratório evolui, mantendo cada exemplo acompanhado de documentação e testes quando fizer sentido.

## Licença

Este projeto está disponível sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE).
