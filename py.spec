# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['py.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\saik2\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\better_profanity\\alphabetic_unicode.json', 'better_profanity'), ('C:\\Users\\saik2\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\better_profanity\\profanity_wordlist.txt', 'better_profanity')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='py',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
