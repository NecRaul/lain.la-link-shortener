try:
    import importlib.metadata

    __version__ = importlib.metadata.version("lain_shorten")

except importlib.metadata.PackageNotFoundError:
    __version__ = "1.19"
