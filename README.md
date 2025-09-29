# Meu Projeto

![Build Status](https://github.com/011295mmatos/lab-pipeline/workflows/Build%20Docker%20Image/badge.svg)

# Pipeline CI/CD com AWS

Aplicação Flask que faz deploy automático na AWS quando você dá push no GitHub.

## 🛠️ Tecnologias

- Python/Flask
- Docker
- GitHub Actions
- AWS ECR
- AWS ECS Fargate

## 🚀 Como funciona

1. Faz `git push`
2. GitHub Actions builda a imagem Docker
3. Envia pro AWS ECR
4. Deploy automático no Fargate

## 💻 Rodar local
```bash
pip install -r requirements.txt
python app.py
