#!/usr/bin/env python3
import os
import sys
import re
import json
import argparse
from pathlib import Path

from layers.cleaner import CleanerLayer
from layers.jargon import JargonLayer
from layers.styler import StylerLayer

class CommentHumanizer:
    def __init__(self):
        self.pipeline = [CleanerLayer(), JargonLayer(), StylerLayer()]
        # Lista de extensiones de código soportadas
        self.valid_extensions = {
            '.py', '.c', '.cpp', '.h', '.hpp', '.js', '.jsx', 
            '.ts', '.tsx', '.java', '.go', '.rs', '.php', '.rb', '.ipynb'
        }
        # Regex para Python (usado en Notebooks y .py)
        self.py_comment_re = re.compile(r'^(\s*)(#)\s*(.*)$')
        # Regex genérico para C-style
        self.c_comment_re = re.compile(r'^(\s*)(//|#)\s*(.*)$')

    def humanize_text(self, text):
        for layer in self.pipeline:
            text = layer.apply(text)
        return text

    def _process_line(self, line, comment_re):
        """Procesa una sola línea si es un comentario."""
        match = comment_re.match(line)
        if match:
            indent, symbol, content = match.groups()
            # Si el comentario tiene contenido sustancial, lo humanizamos
            if len(content.split()) > 2:
                humanized = self.humanize_text(content)
                # Conservamos el salto de línea original si existía
                newline = "\n" if line.endswith("\n") else ""
                return f"{indent}{symbol} {humanized}{newline}"
        return line

    def process_jupyter(self, file_path):
        """Maneja la estructura JSON de los archivos .ipynb"""
        print(f"📓 Procesando Notebook: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                nb_data = json.load(f)

            for cell in nb_data.get('cells', []):
                if cell.get('cell_type') == 'code':
                    source = cell.get('source', [])
                    # Las líneas en 'source' pueden ser una lista de strings
                    new_source = []
                    for line in source:
                        new_source.append(self._process_line(line, self.py_comment_re))
                    cell['source'] = new_source

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(nb_data, f, indent=1, ensure_ascii=False)
                
        except Exception as e:
            print(f"❌ Error procesando Notebook {file_path}: {e}")

    def process_standard_file(self, file_path):
        """Maneja archivos de texto plano (.c, .py, etc.)"""
        print(f"📄 Procesando: {file_path}")
        suffix = file_path.suffix
        comment_re = self.py_comment_re if suffix == '.py' else self.c_comment_re
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            processed_lines = [self._process_line(line, comment_re) for line in lines]

            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(processed_lines)
        except Exception as e:
            print(f"❌ Error en {file_path}: {e}")

    def run(self, target_path):
        path = Path(target_path)
        if path.is_file():
            if path.suffix == '.ipynb':
                self.process_jupyter(path)
            elif path.suffix in self.valid_extensions:
                self.process_standard_file(path)
        elif path.is_dir():
            for root, _, files in os.walk(path):
                for file in files:
                    file_path = Path(root) / file
                    if file_path.suffix == '.ipynb':
                        self.process_jupyter(file_path)
                    elif file_path.suffix in self.valid_extensions:
                        self.process_standard_file(file_path)
        else:
            print(f"⚠️ El camino {target_path} no existe.")

def main():
    parser = argparse.ArgumentParser(description="Humaniza comentarios de IA en archivos de código.")
    parser.add_argument("path", help="Fichero o directorio a procesar")
    args = parser.parse_args()

    humanizer = CommentHumanizer()
    humanizer.run(args.path)

if __name__ == "__main__":
    main()