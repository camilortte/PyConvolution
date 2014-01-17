import sys
from cx_Freeze import setup, Executable, install_exe


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "PyConvolution",
        version = "0.1.35",
        description = u"PyConvolution is a small project about a Spatial convolution applied to Images with filters. This was created with Technology Qt4, Python2.7 and Pyside",
        options ={'build_exe': {'init_script':'Console','icon':'C:\\Users\\x00fest\\Desktop\\PyConvolution-master\\resources\\src\\python.ico'}, 'install':{'install_exe':'install'},'bdist_msi':{'add_to_path':'install2'}},
        executables = [Executable("main.py", base=base)])