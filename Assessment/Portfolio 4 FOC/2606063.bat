@echo off
title Dynamic Directory Structure Creator
color 0A

:MENU
cls
echo ==========================================
echo        DIRECTORY STRUCTURE CREATOR
echo ==========================================
echo 1. Create new directory structure
echo 2. Rename an existing directory
echo 3. Exit
echo ==========================================
set /p choice=Enter your choice (1-3): 

if "%choice%"=="1" goto CREATE
if "%choice%"=="2" goto RENAME
if "%choice%"=="3" exit
echo Invalid choice!
pause
goto MENU

:CREATE
cls
set /p ROOT=Enter root directory name: 

:: Error checking for empty input
if "%ROOT%"=="" (
    echo Root directory name cannot be empty!
    pause
    goto CREATE
)

mkdir "%ROOT%" 2>nul
if errorlevel 1 (
    echo Directory already exists or invalid name!
    pause
    goto MENU
)

cd "%ROOT%"

set /p D1=Enter first subdirectory name: 
if "%D1%"=="" goto SKIP1
mkdir "%D1%"

:SKIP1
set /p D2=Enter second subdirectory name: 
if "%D2%"=="" goto SKIP2
mkdir "%D2%"

:SKIP2
set /p FILE1=Enter file name to create (with extension): 
if "%FILE1%"=="" goto DONE
echo This is a sample file > "%FILE1%"

:DONE
echo.
echo Directory structure created successfully!
cd ..
pause
goto MENU

:RENAME
cls
set /p OLD=Enter existing directory name: 
if not exist "%OLD%" (
    echo Directory does not exist!
    pause
    goto MENU
)

set /p NEW=Enter new directory name: 
if "%NEW%"=="" (
    echo New name cannot be empty!
    pause
    goto MENU
)

ren "%OLD%" "%NEW%"
echo Directory renamed successfully!
pause
goto MENU