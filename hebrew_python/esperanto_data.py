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
    "שגיאת_ייבוא": "ImportError",
    "שגיאת_שם": "NameError",
    "שגיאת_הרשאות": "PermissionError",
    "שגיאה":"Exception",
    "שגיאת_קובץ_לא_נמצא":"FileNotFoundError",
    

    # strings
    'repr': 'repr',  # TODO is this the best translation?
    "ekzek": "exec",
    "malfermi": "open"
}

# keywords:
esperanto_keywords = {
    "בנוי":
    "esperanto_python",  # TODO : I want to create another module for this.

    # if and booleans:
    "se": "if",
    "Vera": "True",
    "Malvera": "False",
    "kaj": "and",
    "ne": "not",
    "estas": "is",
    "אחרת": "else",
    "אחרת_אם": "elif",  # אחרתאם ?
    "aŭ": "or",

    # loops
    "לכל": "for",
    "en": "in",
    "intervalo": "range",  # atingopovo?
    "צא": "break",
    "dum": "while",
    "המשך": "continue",

    # types:
    "רשימה": "list",
    "entjero": "int",  # just "ent"?
    "glitkomo": "float",  # just "glit"?
    "כלום": "None",
    "בוליאני": "bool",
    "מחרוזת":"str",
    "סט": "set()",
    'object': 'אובייקט',

    # imports
    "מתוך": "from",
    "יבא": "import",
    "בתור": "as",

    # classes and functions
    "החזר": "return",
    "מחלקה": "class",
    "גלובלי": "global",
    "הגדר": "def",
    "עבור": "pass",
    "צור": "yield",

    # errors
    "נסה": "try",
    "ודא": "assert",
    "זרוק": "raise",
    "תפוס": "except",
    "לבסוף": "finally",
    
    # list
    "עגל": "round()",
    "פרוסה": "slice()",
    "מיין": "sorted()",
    "סכום": "sum()",
    "סוג": "type()",

    #
    'עם': "with",
    "מחק": "del",
    "למדה": "lambda",
}
