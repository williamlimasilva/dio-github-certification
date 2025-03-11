# Explorando Colaboração e Markdown

## Introdução ao Git e GitHub

Git é um sistema de controle de versão distribuído amplamente utilizado para rastrear mudanças em arquivos e coordenar trabalho entre múltiplas pessoas. GitHub é uma plataforma baseada em nuvem que hospeda repositórios Git e facilita a colaboração.

## Instalação do Git

### Windows

1. Baixe o instalador em: [git-scm.com](https://git-scm.com/downloads)
2. Execute o instalador e siga as instruções
3. Verifique a instalação com:
   ```sh
   git --version
   ```

### Linux (Debian/Ubuntu)

```sh
sudo apt update
sudo apt install git -y
```

### macOS

```sh
brew install git
```

## Configuração Inicial do Git

```sh
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@example.com"
```

## Criando um Repositório

```sh
git init meu-repositorio
cd meu-repositorio
```

## Clonando um Repositório

```sh
git clone https://github.com/usuario/repositorio.git
```

## Principais Comandos do Git

### Verificando o Status

```sh
git status
```

### Adicionando Arquivos

```sh
git add arquivo.txt # Adiciona um único arquivo
git add .           # Adiciona todos os arquivos
```

### Criando um Commit

```sh
git commit -m "Mensagem do commit"
```

### Enviando para o GitHub

```sh
git push origin main
```

## Trabalhando com Branches

### Criar uma Nova Branch

```sh
git branch nova-branch
```

### Trocar de Branch

```sh
git checkout nova-branch
```

### Criar e Mudar para a Branch Simultaneamente

```sh
git checkout -b nova-branch
```

### Mesclar uma Branch

```sh
git checkout main
git merge nova-branch
```

## Resolvendo Conflitos

Caso ocorra um conflito, edite os arquivos manualmente e finalize com:

```sh
git add .
git commit -m "Resolvendo conflito"
```

## Trabalhando com GitHub

### Criar um Repositório no GitHub

1. Acesse [GitHub](https://github.com/) e crie uma conta.
2. Clique em **New Repository**.
3. Escolha um nome e clique em **Create Repository**.
4. Para conectar ao repositório remoto:
   ```sh
   git remote add origin https://github.com/usuario/repositorio.git
   git branch -M main
   git push -u origin main
   ```

### Clonar, Modificar e Enviar Alterações

```sh
git clone https://github.com/usuario/repositorio.git
cd repositorio
# Fazer modificações
# Adicionar, commit e push
```

## Pull Requests

1. Faça alterações em uma branch separada.
2. Suba as alterações para o GitHub.
3. Abra um **Pull Request** no GitHub.
4. Após aprovação, faça o **merge** da branch.

## Conclusão

Git e GitHub são essenciais para o desenvolvimento colaborativo. Dominar esses conceitos ajudará a gerenciar projetos de forma eficiente e profissional.
