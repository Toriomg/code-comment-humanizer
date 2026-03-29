import re
import random

class CodeHumanizer:
    def __init__(self):
        # Diccionario de jerga y abreviaturas comunes de devs
        self.jargon_map = {
            "función": "func",
            "funciones": "funcs",
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
            "contexto": "ctx",
            "usuario": "user",
            "archivo": "file"
        }

        # Frases típicas de IA que hay que eliminar o simplificar
        self.ai_redundancies = [
            r"esta función (se encarga de|sirve para|realiza)",
            r"el siguiente bloque de código",
            r"este método",
            r"se utiliza para",
            r"procedemos a",
            r"a continuación,"
        ]

    def transform_text(self, text):
        # 1. Limpieza de redundancias de IA
        processed = text.lower().strip()
        for pattern in self.ai_redundancies:
            processed = re.sub(pattern, "", processed).strip()

        # 2. Aplicar Jerga de programador
        words = processed.split()
        new_words = [self.jargon_map.get(w, w) for w in words]
        processed = " ".join(new_words)

        # 3. Estilo "Humano" (Aleatoriedad)
        # Quitar punto final el 80% de las veces
        if processed.endswith('.') and random.random() < 0.8:
            processed = processed[:-1]

        # Añadir etiquetas de contexto aleatorias (10% de probabilidad)
        if random.random() < 0.1:
            tags = ["TODO:", "fixme:", "nota:", "ojo:"]
            processed = f"{random.choice(tags)} {processed}"

        # Capitalización aleatoria del inicio (más humano que sea minúscula)
        if len(processed) > 0 and random.random() < 0.7:
            processed = processed[0].lower() + processed[1:]
        elif len(processed) > 0:
            processed = processed[0].upper() + processed[1:]

        return processed

    def process_file(self, input_file, output_file):
        # Detecta comentarios de tipo # (Python/JS) o // (JS/C++/Java)
        # Mantiene la indentación original
        comment_pattern = re.compile(r'^(\s*)(#|//)\s*(.*)$')
        
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            match = comment_pattern.match(line)
            if match:
                indent = match.group(1)
                symbol = match.group(2)
                content = match.group(3)
                
                # Solo procesar si el comentario no está vacío y es largo (estilo IA)
                if len(content.split()) > 2:
                    humanized_content = self.transform_text(content)
                    new_lines.append(f"{indent}{symbol} {humanized_content}\n")
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        print(f"✅ Archivo procesado y guardado en: {output_file}")

# --- MODO DE USO ---
if __name__ == "__main__":
    humanizer = CodeHumanizer()
    
    # Ejemplo: cambia 'codigo_ia.py' por el nombre de tu archivo
    # humanizer.process_file("codigo_ia.py", "codigo_humano.py")
    
    # Demostración rápida con un string
    test_comment = "Esta función se encarga de realizar la configuración de la base de datos."
    print(f"IA: {test_comment}")
    print(f"Humano: {humanizer.transform_text(test_comment)}")