import os

# os.system(r'del /S /Q ".\build\lib\*"')
os.system(r'rmdir /S /Q ".\build\lib')
os.system("python setup.py sdist")
os.system("python setup.py bdist_wheel")
