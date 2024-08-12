@echo off
REM Verifica se o Python 3.12.4 está instalado
python --version 2>nul | findstr /r "3\.12\.4"
IF ERRORLEVEL 1 (
    echo Python 3.12.4 não está instalado ou não está no PATH.
    exit /b 1
)

REM Cria o ambiente virtual
echo Criando ambiente virtual usando Python 3.12.4...
python -m venv venv

REM Verifica se o ambiente virtual foi criado com sucesso
IF NOT EXIST "venv\Scripts\activate.bat" (
    echo Falha ao criar o ambiente virtual.
    exit /b 1
)

REM Ativa o ambiente virtual
echo Ativando ambiente virtual...
call .\venv\Scripts\Activate.bat

REM Verifica e atualiza o pip se necessário
echo Verificando e atualizando pip...
python -m pip install --upgrade pip

REM Verifica se a atualização do pip foi bem-sucedida
pip --version
IF ERRORLEVEL 1 (
    echo Falha ao atualizar o pip.
    exit /b 1
)

REM Instala as dependências do projeto usando o setup.py
echo Instalando dependências do projeto com setup.py...
pip install -e .

REM Confirma a instalação e informa que o ambiente está pronto
echo Ambiente configurado com sucesso.
echo Para ativar o ambiente virtual novamente, use: venv\Scripts\activate.bat
pause
