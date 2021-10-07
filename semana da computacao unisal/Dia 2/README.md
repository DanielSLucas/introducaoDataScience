# ABRIR O VISUAL STUDIO CODE COMO ADMINISTRADOR.



## Executar este comando no vscode para criar a pasta do ambiente virtual:

```bash
  python -m venv bot-env
```

## Executar este comando para inicializar o ambiente virtual:

```bash
  .\bot-env\Scripts\activate.ps1
```

## Caso o comando acima apresente algum erro , executar no windows power shell o seguinte comando:

```bash
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
Digitar S e fechar o windows power shell.


## Executar novamente o comando que ativa o ambiente virtual:
```bash
  .\bot-env\Scripts\activate.ps1
```

## Criar arquivo de requirements

`**requirements.txt**`

```
  ChatterBot==1.0.8
  spacy==2.3.2
  SQLAlchemy==1.3.17
  ChatterBot-corpus
```


## Instalar o arquivo de requirements:

```bash
  pip install -r requirements.txt
```

## Baixar pacotes auxiliares

python -m spacy download en_core_web_lg
python -m spacy download en_core_web_sm
python -m spacy download en


## Para linux:
https://linoxide.com/how-to-create-python-virtual-environment-on-ubuntu-20-04/

```bash
  # install python3
  apt install python3

  # install pip for python3
  apt install python3-pip

  # install tkinter
  sudo apt-get install python3-tk 

  # install venv
  apt-get install python3-venv

  # create a virtual enviroment
  python3 -m venv my_env_project

  # activate virtual enviroment
  source my_env_project/bin/activate

  # to install packages into virtual enviroment 
  pip install -r ./requirements.txt # or pip instal packageName

  # To exit from virtual environment use exit or Ctrl+d command. 
  # To delete a virtual environment run the following command:
  deactivate
```

