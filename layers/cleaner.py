import re
import unicodedata

class CleanerLayer:
    def __init__(self):
        self.ai_patterns = [
            r"esta funcion (se encarga de|sirve para|realiza|hace)",
            r"el siguiente bloque de codigo",
            r"este metodo",
            r"se utiliza para",
            r"procedemos a",
            r"a continuacion,",
            r"es un ejemplo de"
        ]
        self.emoji_regex = re.compile(r'[\u2000-\u3300\U00010000-\U0010ffff\uFE00-\uFE0F]')

        # 3. Lista de emoticonos de texto comunes
        # Se escapan los caracteres especiales para que Regex no falle
        self.text_emoticons = [
            r":\)", r":D", r":\(", r";\)", r":-P", r":P", r"XD", r"xd", r"<3"
        ]
        # 3. NUEVO: Regex para detectar listas numeradas (Ej: "1. ", "10. ")
        # ^\d+ -> Empieza por uno o más dígitos
        # \.   -> Seguido de un punto literal
        # \s+  -> Seguido de uno o más espacios
        self.list_pattern = re.compile(r"^\d+\.\s+")

    def _strip_accents(self, text):
        """Elimina acentos (á -> a, é -> e, etc.)"""
        return ''.join(c for c in unicodedata.normalize('NFD', text)
                       if unicodedata.category(c) != 'Mn')
    
    def _camelCase_lower(self, text):
        """Baja a minúsculas solo palabras comunes, respetando CamelCase y acrónimos."""
        words = text.split()
        processed_words = []
        for word in words:
            # Si la palabra tiene una mayúscula que no está al principio (CamelCase: getUser)
            # o si toda la palabra es mayúsculas y larga (ID, API, USER_DATA)
            # la dejamos como está.
            has_internal_upper = any(c.isupper() for c in word[1:])
            is_all_upper = word.isupper() and len(word) > 1
            
            if has_internal_upper or is_all_upper:
                processed_words.append(word)
            else:
                processed_words.append(word.lower())
        return " ".join(processed_words)

    def apply(self, text):
        # 1. Quitar emojis y acentos
        text = self.emoji_regex.sub('', text)
        text = self._strip_accents(text)
        
        # 2. Quitar emoticonos
        for emoticon in self.text_emoticons:
            text = re.sub(emoticon, "", text, flags=re.IGNORECASE)

        # 3. Quitar numeración de lista al inicio
        text = text.strip()
        text = self.list_pattern.sub("", text)

        # 4. Quitar frases de IA (usando ignore case para el match)
        for pattern in self.ai_patterns:
            text = re.sub(pattern, "", text, flags=re.IGNORECASE).strip()

        # 5. Minúsculas inteligentes (Preserva CamelCase)
        text = self._camelCase_lower(text)
            
        return re.sub(r'\s+', ' ', text).strip()