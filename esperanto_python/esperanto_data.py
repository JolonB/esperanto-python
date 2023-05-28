# functions:
esperanto_builtins = {
    # numbers
    "abs": "abs",
    "ĉio": "all",
    "io": "any",
    # list
    "longo": "len",
    "min": "min",
    "maks": "max",
    "inversa": "reversed",
    "nombri": "enumerate",
    "mapi": "map",
    # std
    "presi": "print",
    "enigo": "input",
    # strings
    "repr": "repr",
    "ekzek": "exec",
    # files
    "malfermi": "open",
    # others
    "__nomo__": "__name__",
    "lokaj": "locals",

    # types:
    "listo": "list",
    "entjero": "int",  # nur "ent"?
    "glitkomo": "float",  # nur "glit"?
    "bulea": "bool",  # aŭ buleo?
    "teksto": "str",  # signoĉeno
    "aro": "set",
    "objekto": "object",
    "intervalo": "range",  # atingopovo?
    # classes and functions
    "tipo": "type",
    "estasklaso": "isinstance",
    # math
    "rondigi": "round",
    "sumo": "sum",
    # lists
    "tranĉaĵo": "slice",
    "ordigita": "sorted",

    # errors
    "ImportadoEraro": "ImportError",
    "NomoEraro": "NameError",
    "PermesoEraro": "PermissionError",
    "Escepto": "Exception",
    "DosieroNeTrovitaEraro": "FileNotFoundError",
    "RultempoEraro": "RuntimeError",
    # TODO add more errors
}

# All builtins (including aiter and anext)
# `import builtins; print(dir(builtins))`
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

# keywords:
esperanto_keywords = {
    # "pitono": "esperanto_python",
    # if and booleans:
    "Malvera": "False",
    "Nul": "None",
    "Vera": "True",
    "kaj": "and",
    "kiel": "as",
    "aserti": "assert",
    "nesink": "async",
    "atendi": "await",
    "interrompi": "break",
    "klaso": "class",
    "daŭrigi": "continue",
    "dif": "def",
    "forigi": "del",
    "alse": "elif",
    "alie": "else",
    "trakti": "except",  # aŭ krom?
    "fine": "finally",
    "por": "for",
    "el": "from",
    "malloka": "global",
    "se": "if",
    "importi": "import",
    "en": "in",
    "estas": "is",
    "lambda": "lambda",
    "neloka": "nonlocal",
    "ne": "not",
    "aŭ": "or",
    "pasi": "pass",
    "altigi": "raise",  # aŭ levi?
    "redoni": "return",
    "provi": "try",
    "dum": "while",
    "kun": "with",
    "doni": "yield",
}
