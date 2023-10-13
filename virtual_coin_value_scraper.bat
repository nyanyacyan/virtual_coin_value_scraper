@echo off

@REM バッチファイルで行われた後に変更をしてしまったものを無効化する
setlocal enabledelayedexpansion


@REM ディレクトリをデスクトップにセット
set DESKTOP_DIR=%USERPROFILE%\Desktop


@REM exeファイルの場所を探す。  見つかった場合、そのファイルのフルパスPYTHON_INSTALLERという変数に定義
for /R"%DESKTOP_DIR%"%%i in (python-3.10.8-amd64.exe)do(
    set PYTHON_INSTALLER=%%i
)


@REM requirements.txtの場所を探す  見つかった場合、そのファイルのフルパスをREQUIREMENTS_FILEという変数に定義
for /R"%DESKTOP_DIR%"%%i in (requirements.txt)do(
    set REQUIREMENTS_FILE=%%i
)


@REM パイソンのインストール wait!はｲﾝｽﾄｰﾙが終わるまで実行をｽﾄｯﾌﾟ。quietはｻｲﾚﾝﾄﾓｰﾄﾞ（GUIなし）で実行
@REM InstallAllUsers=1 と PrependPath=1 すべてのユーザーのためにPythonをインストールPythonをシステムのPATHに追加
if defined PYTHON_INSTALLER(
    start /wait!PYTHON_INSTALLER! /quiet InstallAllUser=1 PrependPath=1
)else(
    echo python-3.10.8-amd64.exe が見つかりません。.
    exit /b
)


@REM main.pyファイルの場所を探す。  見つかった場合、そのファイルのフルパスをMAIN_PY_PATHという変数に定義
for /R "%DESKTOP_DIR%" %%i in (main.py) do (
    set MAIN_PY_PATH=%%i
)


REM requirements.txtの依存関係をインストール（見つかった場合）
if defined REQUIREMENTS_FILE (
    python -m pip install -r !REQUIREMENTS_FILE!
) else (
    echo requirements.txt not found on Desktop.
    exit /b
)

REM タスクスケジューラにタスクを追加
REM 両方のファイルが見つかった場合、タスクスケジューラにタスクを追加
if defined PYTHON_PATH if defined MAIN_PY_PATH (
    schtasks /create /tn "RunMainPy" /tr "!PYTHON_PATH! !MAIN_PY_PATH!" /sc daily /st 06:00
) else (
    echo python.exe or main.py not found on Desktop.
    exit /b
)
