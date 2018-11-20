# -*- mode: python -*-

block_cipher = None


a = Analysis(['upload_api-v2.py'],
             pathex=['/data/data/com.termux/files/home/sharpai/src/embedding'],
             binaries=[],
             datas=[],
             hiddenimports=['django', 'celery', 'celery.loaders.app', 'celery.app.amqp', 'celery.fixups.django', 'celery.bin.celery', 'sklearn.neighbors.ball_tree', 'sklearn.neighbors.dist_metrics', 'sklearn.neighbors.kd_tree', 'sklearn.neighbors.quad_tree', 'sklearn.neighbors.typedefs', 'kombu.transport.redis', 'celery.backends', 'celery.apps', 'celery.apps.worker', 'celery.events', 'celery.worker', 'celery.bin', 'celery.concurrency', 'celery.contrib', 'celery.fixups', 'celery.security', 'celery.task', 'celery.utils', 'celery.backends.redis', 'celery.app.events', 'celery.app.base.log_cls', 'celery.app.control', 'celery.app.log', 'celery.app.control', 'celery.app.task', 'celery.concurrency.prefork', 'celery.concurrency.eventlet', 'celery.concurrency.gevent', 'celery.concurrency.solo', 'celery.worker.components', 'celery.worker.autoscale', 'celery.worker.consumer', 'celery.worker.state', 'celery.worker.state.task_reserved', 'celery.worker.state.maybe_shutdown', 'celery.worker.state.reserved_requests', 'celery.worker.control', 'celery.worker.loops', 'celery.worker.request', 'celery.worker.strategy', 'celery.worker.heartbeat', 'celery.worker.pidbox', 'celery.events.state'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='embedding',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )