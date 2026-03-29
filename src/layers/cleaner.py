import re

class CleanerLayer:
    def __init__(self):
        self.ai_patterns = [
            r"esta función (se encarga de|sirve para|realiza|hace)",
            r"el siguiente bloque de código",
            r"este método",
            r"se utiliza para",
            r"procedemos a",
            r"a continuación,",
            r"es un ejemplo de"
        ]

    def apply(self, text):
        processed = text.lower().strip()
        for pattern in self.ai_patterns:
            processed = re.sub(pattern, "", processed).strip()
        return processed