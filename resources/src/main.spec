# -*- mode: python -*-
a = Analysis(['main.pyw'],
             pathex=['C:\\Users\\x00fest\\Desktop\\PyConvolution-master\\resources\\src'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main.exe',
          debug=True,
          strip=None,
          upx=True,
          console=True , icon='C:\\Users\\x00fest\\Desktop\\PyConvolution-master\\resources\\img\\icon\\python.png')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='main')
