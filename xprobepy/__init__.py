version_info= (0,0, 1, "dev1")
__version__ = ".".join(map(str, version_info))

try:
    from xprobepy import xprober


except ImportError:
    import traceback
    traceback.print_exc()
