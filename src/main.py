import re
from layers.cleaner import CleanerLayer
from layers.jargon import JargonLayer
from layers.styler import StylerLayer

class CommentHumanizer:
    def __init__(self):
        # Registramos las capas en orden de ejecución
        self.pipeline = [
            CleanerLayer(),
            JargonLayer(),
            StylerLayer()
        ]

    def humanize_text(self, text):
        for layer in self.pipeline:
            text = layer.apply(text)
        return text

    def process_file(self, input_path, output_path):
        # Soporta comentarios de tipo # (Python, Shell) y // (JS, C, Java)
        comment_re = re.compile(r'^(\s*)(#|//)\s*(.*)$')
        
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        processed_lines = []
        for line in lines:
            match = comment_re.match(line)
            if match:
                indent, symbol, content = match.groups()
                # Solo procesamos si el comentario tiene más de 3 palabras (estilo IA)
                if len(content.split()) > 3:
                    humanized = self.humanize_text(content)
                    processed_lines.append(f"{indent}{symbol} {humanized}\n")
                else:
                    processed_lines.append(line)
            else:
                processed_lines.append(line)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(processed_lines)
        print(f"--- Proceso completado: {output_path} ---")

if __name__ == "__main__":
    humanizer = CommentHumanizer()
    
    # Ejemplo de uso:
    # humanizer.process_file("tu_codigo_ia.py", "tu_codigo_humano.py")
    
    # Test rápido de consola
    test = "Esta función se encarga de realizar la autenticación del usuario en la base de datos."
    print(f"Original: {test}")
    print(f"Humanizado: {humanizer.humanize_text(test)}")