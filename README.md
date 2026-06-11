## Detecção de Code Smells com IA no GitHub


### Objetivo

- Utilizar GitHub Actions e IA para automatizar a detecção de code smells em um projeto.


### Instruções

1. Sigam com o mesmo grupo e o mesmo repositório da atividade de cobertura de testes em Python.
2. Adicione a Action AI Inference ao repositório (Marketplace -> Actions ->AI Inference).
3. Crie um workflow em `.github/workflows/`.
4. Crie um prompt capaz de detectar pelo menos 2 code smells (ex.: Long Method, Duplicated Code, Large Class, Feature Envy, Data Clumps etc.).
5. Configure o workflow para executar a análise utilizando IA.
6. Crie duas branches e mantenha os dois PRs abertos: Um contendo a versão com os code smells, e o outro contendo a versão após a refatoração.


### Entrega

- Link do repositório GitHub, contendo os dois PRs abertos

### Avaliação

- Workflow funcionando;
- Prompt detectando pelo menos 2 code smells;
- Execução da análise via GitHub Actions;
- Dois PRs criados corretamente.
