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
    # errors
    "ImportadoEraro": "ImportError",
    "NomoEraro": "NameError",
    "PermesoEraro": "PermissionError",
    "Escepto": "Exception",
    "DosieroNeTrovitaEraro": "FileNotFoundError",
    # strings
    "repr": "repr",  # TODO is this the best translation?
    "ekzek": "exec",
    "malfermi": "open",
}

# keywords:
esperanto_keywords = {
    "pitono": "esperanto_python",
    # if and booleans:
    "se": "if",
    "Vera": "True",
    "Malvera": "False",
    "kaj": "and",
    "ne": "not",
    "estas": "is",
    "alie": "else",
    "alse": "elif",  # אחרתאם ?
    "aŭ": "or",
    # loops
    "por": "for",
    "en": "in",
    "intervalo": "range",  # atingopovo?
    "interrompi": "break",
    "dum": "while",
    "daŭrigi": "continue",
    # types:
    "listo": "list",
    "entjero": "int",  # nur "ent"?
    "glitkomo": "float",  # nur "glit"?
    "Nul": "None",
    "bulea": "bool",  # aŭ buleo?
    "teksto": "str",  # signoĉeno
    "aro": "set()",  # TODO forigu parentezojn?
    "object": "objekto",  # TODO interŝanĝi?
    # imports
    "el": "from",
    "importi": "import",
    "kiel": "as",
    # classes and functions
    "redoni": "return",
    "klaso": "class",
    "malloka": "global",
    "dif": "def",
    "pasi": "pass",
    "doni": "yield",
    # errors
    "provi": "try",
    "aserti": "assert",
    "altigi": "raise",  # aŭ levi?
    "trakti": "except",  # aŭ krom?
    "fine": "finally",
    # list
    "rondigi": "round()",
    "tranĉaĵo": "slice()",
    "ordigita": "sorted()",
    "sumo": "sum()",
    "tipo": "type()",
    #
    "kun": "with",
    "forigi": "del",
    "lambda": "lambda",
    "lokaj": "locals()",
}
