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
        self.emoji_regex = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)

        # 3. Lista de emoticonos de texto comunes
        # Se escapan los caracteres especiales para que Regex no falle
        self.text_emoticons = [
            r":\)", r":D", r":\(", r";\)", r":-P", r":P", r"XD", r"xd", r"<3"
        ]

    def apply(self, text):
        # Primero quitamos los emojis Unicode
        processed = self.emoji_regex.sub(r'', text)
        
        # Luego quitamos los emoticonos de texto
        for emoticon in self.text_emoticons:
            processed = re.sub(emoticon, "", processed)

        # Convertimos a minúsculas y limpiamos espacios
        processed = processed.lower().strip()

        # Finalmente, eliminamos las frases redundantes de IA
        for pattern in self.ai_patterns:
            processed = re.sub(pattern, "", processed).strip()
            
        # Limpiar espacios dobles que hayan podido quedar tras borrar palabras
        processed = re.sub(r'\s+', ' ', processed)
        
        return processed