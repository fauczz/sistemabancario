# 🏦 Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em **Python** com foco em operações básicas de conta corrente: **depósitos, saques e extrato**.  
O projeto foi construído com base em regras de negócio comuns em sistemas bancários.

---

## 📌 Funcionalidades

- **Depositar** valores (não é permitido valor `0` ou negativo).
- **Sacar** valores com as seguintes regras:
  - Máximo **R$ 500,00 por saque**.
  - Até **3 saques por dia**.
  - Não é permitido sacar valores maiores que o saldo disponível.
- **Extrato**: exibe todas as movimentações realizadas (depósitos e saques) e o saldo atual formatado em reais.

---

## ⚙️ Requisitos

- Python 3.8 ou superior instalado na máquina.
- Nenhuma biblioteca externa é necessária (apenas bibliotecas nativas do Python).
