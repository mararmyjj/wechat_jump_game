# -*- mode: python -*-

block_cipher = None


a = Analysis(['wechat_jump_auto.py'],
             pathex=['X:\\Users\\Administrator\\Desktop\\wechat_jump_game'],
             binaries=[],
             datas=[('X:\\Users\\Administrator\\Desktop\\wechat_jump_game\\config', 'config')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='wechat_jump_auto',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='wechat_jump_auto')
