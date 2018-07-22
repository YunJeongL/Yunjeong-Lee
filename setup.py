import sys
from cx_Freeze import setup, Executable
import os

# 빌드 옵션
buildOptions = dict(
    packages = ['selenium'],  # run.py에서 사용한 써드파트 모듈
    excludes = [],  # 필요한 모듈 리스트
    include_files = ['chromedriver.exe']  # 파이썬 파일이 아닌 파일 리스트(dll, exe)
)
# 실행 관련 변수
base = None
base = 'Win32GUI' if sys.platform == 'win32' else None
executables = [
    Executable('run.py', base=base, icon='2Heart.ico')
]
# 셋업
setup(name='crawer',
version='1.0',
description='this...',
requires=[],
options=dict(build_exe=buildOptions),
executables=executables
)