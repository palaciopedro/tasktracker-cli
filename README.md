# TASKTRACKER CLI

**Projeto em Desenvolvimento**

# 📌 Task Tracker CLI

Um **Task Tracker em linha de comando (CLI)** desenvolvido em Python para gerenciar tarefas do dia a dia.  
O projeto permite criar, atualizar, remover e listar tarefas, persistindo os dados em um arquivo JSON local.

Este projeto foi desenvolvido com o objetivo de **praticar lógica de programação, manipulação de arquivos, argumentos de linha de comando e organização de código**, sem o uso de bibliotecas externas.
##
## 🚀 Funcionalidades

- Adicionar novas tarefas
- Atualizar descrição de tarefas
- Remover tarefas
- Marcar tarefas como:
  - 🕒 Em progresso
  - ✅ Concluídas
- Listar:
  - Todas as tarefas
  - Apenas tarefas concluídas
  - Apenas tarefas pendentes
  - Apenas tarefas em progresso
- Persistência de dados em arquivo `tasks.json`

## 📘 Comandos Disponíveis
### ➕ Adicionar tarefa
```
python tt.py add "Descrição da tarefa"
```
### 📄 Listar tarefas
```
python tasktracker.py list
python tasktracker.py list done
python tasktracker.py list todo
python tasktracker.py list in-progress
```
### ✏️ Atualizar tarefa
```
python tasktracker.py update ID "Nova descrição"
```
### ❌ Deletar tarefa
```
python tasktracker.py delete ID
```
### 🔄 Alterar status
```
python tasktracker.py mark-in-progress ID
python tasktracker.py mark-done ID
```
## 📜 Licença 
Esse projeto é licenciado de acordo com a MIT License. Você é livre para usar, modificar e distribuir o TaskTracker CLI.
