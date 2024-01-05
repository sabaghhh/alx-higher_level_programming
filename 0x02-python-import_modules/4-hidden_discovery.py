#!/usr/bin/python3
if __name__ == "__main__":
    import importlib
    import inspect
    if __name__ == "__main__":
        hidden_4 = importlib.import_module('hidden_4')
        names = dir(hidden_4)
        names = [name for name in names if not name.startswith('__')]
        names.sort()
        for name in names:
            print(name)
