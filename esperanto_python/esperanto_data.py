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
    "inversa": 'reversed',
    "nombri": "enumerate",
    "mapi": "map",

    # std
    "presi": "print",
    "enigo": "input",

    # errors
    "ImportadoEraro": "ImportError",
    "NomoEraro": "NameError",
    "PermesoEraro": "PermissionError",
    "Escepto":"Exception",
    "DosieroNeTrovitaEraro":"FileNotFoundError",
    

    # strings
    'repr': 'repr',  # TODO is this the best translation?
    "ekzek": "exec",
    "malfermi": "open"
}

# keywords:
esperanto_keywords = {
    "בנוי":  # "built"/"designed"
    "esperanto_python",  # TODO : I want to create another module for this.

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
    "צא": "break",
    "dum": "while",
    "daŭrigu": "continue",

    # types:
    "listo": "list",
    "entjero": "int",  # nur "ent"?
    "glitkomo": "float",  # nur "glit"?
    "Nul": "None",
    "bulea": "bool",  # aŭ buleo?
    "teksto": "str",  # signoĉeno
    "aro": "set()",  # TODO forigu parentezojn?
    'object': 'objekto',  # TODO interŝanĝi?

    # imports
    "el": "from",
    "importu": "import",
    "kiel": "as",

    # classes and functions
    "redonu": "return",
    "מחלקה": "class",
    "malloka": "global",
    "dif": "def",
    "עבור": "pass",
    "צור": "yield",

    # errors
    "נסה": "try",
    "ודא": "assert",
    "זרוק": "raise",
    "תפוס": "except",
    "fine": "finally",
    
    # list
    "עגל": "round()",
    "פרוסה": "slice()",
    "מיין": "sorted()",
    "סכום": "sum()",
    "סוג": "type()",

    #
    'kun': "with",
    "forigu": "del",
    "lambda": "lambda",
    "lokaj": "locals()",
}
