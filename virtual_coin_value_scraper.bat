@echo off

@REM �o�b�`�t�@�C���ōs��ꂽ��ɕύX�����Ă��܂������̂𖳌�������
setlocal enabledelayedexpansion


@REM �f�B���N�g�����f�X�N�g�b�v�ɃZ�b�g
set DESKTOP_DIR=%USERPROFILE%�_Desktop


@REM exe�t�@�C���̏ꏊ��T���B  ���������ꍇ�A���̃t�@�C���̃t���p�XPYTHON_INSTALLER�Ƃ����ϐ��ɒ�`
for /R"%DESKTOP_DIR%"%%i in (python-3.10.8-amd64.exe)do(
    set PYTHON_INSTALLER=%%i
)


@REM requirements.txt�̏ꏊ��T��  ���������ꍇ�A���̃t�@�C���̃t���p�X��REQUIREMENTS_FILE�Ƃ����ϐ��ɒ�`
for /R"%DESKTOP_DIR%"%%i in (requirements.txt)do(
    set REQUIREMENTS_FILE=%%i
)


@REM �p�C�\���̃C���X�g�[�� wait!�Ͳݽİق��I���܂Ŏ��s��į�߁Bquiet�ͻ����Ӱ�ށiGUI�Ȃ��j�Ŏ��s
@REM InstallAllUsers=1 �� PrependPath=1 ���ׂẴ��[�U�[�̂��߂�Python���C���X�g�[��Python���V�X�e����PATH�ɒǉ�
if defined PYTHON_INSTALLER (
    start /wait !PYTHON_INSTALLER! /quiet InstallAllUser=1 PrependPath=1
)else(
    echo python-3.10.8-amd64.exe ��������܂���B.
    exit /b
)


@REM main.py�t�@�C���̏ꏊ��T���B  ���������ꍇ�A���̃t�@�C���̃t���p�X��MAIN_PY_PATH�Ƃ����ϐ��ɒ�`
for /R "%DESKTOP_DIR%" %%i in (main.py) do (
    set MAIN_PY_PATH=%%i
)


REM requirements.txt�̈ˑ��֌W���C���X�g�[���i���������ꍇ�j
if defined REQUIREMENTS_FILE (
    python -m pip install -r !REQUIREMENTS_FILE!
) else (
    echo requirements.txt not found on Desktop.
    exit /b
)

REM �^�X�N�X�P�W���[���Ƀ^�X�N��ǉ�
REM �����̃t�@�C�������������ꍇ�A�^�X�N�X�P�W���[���Ƀ^�X�N��ǉ�
if defined PYTHON_INSTALLER if defined MAIN_PY_PATH (
    schtasks /create /tn "RunMainPy" /tr "!PYTHON_INSTALLER! !MAIN_PY_PATH!" /sc daily /st 06:00
) else (
    echo python.exe or main.py not found on Desktop.
    exit /b
)
