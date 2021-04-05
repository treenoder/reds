__all__ = 'VERSION', 'version_info'

VERSION = '0.1.6'


def version_info():
    import platform
    import sys
    from pathlib import Path

    info = {
        'reds version': VERSION,
        'install path': Path(__file__).resolve().parent,
        'python version': sys.version,
        'platform': platform.platform(),
    }
    return '\n'.join('{:>30} {}'.format(k + ':', str(v).replace('\n', ' ')) for k, v in info.items())
