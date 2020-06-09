# -*- mode: python ; coding: utf-8 -*-

from kivy_deps import sdl2, glew

from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal, get_deps_all, hookspath, runtime_hooks

block_cipher = None


a = Analysis(['main.py'],
             pathex=['Z:\\General Documents\\Inch to MM App'],
             
             datas=[],
             
             hookspath=[],
             runtime_hooks=[],
             
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False,
             **get_deps_minimal(video=None, audio=None))
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Inch to MM Converter',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='inmmconv.ico')
coll = COLLECT(exe, Tree('\\General Documents\\Inch to MM App\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Inch to MM Converter')
