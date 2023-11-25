# запустить из консоли python 99_py_2_exe.py build_exe

import cx_Freeze

executables = [cx_Freeze.Executable("app.py")] #название файла python

cx_Freeze.setup(
    name="appname",
    options={"build_exe": {"packages":["PyQt5"]}},
    executables = executables
)