@echo off
setlocal

call "C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\Tools\VsDevCmd.bat" -arch=x64
if errorlevel 1 exit /b %errorlevel%

cd /d "%~dp0"
nvcc -std=c++17 -Xcudafe --diag_suppress=177 --shared bitnet_kernels.cu -gencode=arch=compute_89,code=sm_89 -o libbitnet.dll
