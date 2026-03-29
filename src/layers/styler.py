import random

class StylerLayer:
    def apply(self, text):
        if not text: return text
        
        # 80% probabilidad de quitar punto final
        if text.endswith('.') and random.random() < 0.8:
            text = text[:-1]

        # 15% probabilidad de añadir un prefijo de dev (TODO, FIXME)
        """
        if random.random() < 0.15:
            tags = ["TODO:", "fixme:", "nota:", "ojo:"]
            text = f"{random.choice(tags)} {text}"
        """

        # 90% probabilidad de empezar en minúscula (muy humano en código)
        if random.random() < 0.9:
            text = text[0].lower() + text[1:]
        else:
            text = text[0].upper() + text[1:]

        return text