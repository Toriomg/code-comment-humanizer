class JargonLayer:
    def __init__(self):
        self.dictionary = {
            "función": "func",
            "parámetros": "params",
            "configuración": "config",
            "información": "info",
            "base de datos": "db",
            "identificador": "id",
            "anterior": "prev",
            "siguiente": "next",
            "resultado": "res",
            "temporal": "tmp",
            "error": "err",
            "usuario": "user",
            "archivo": "file",
            "autenticación": "auth",
            "biblioteca": "lib"
        }

    def apply(self, text):
        words = text.split()
        new_words = [self.dictionary.get(w, w) for w in words]
        return " ".join(new_words)