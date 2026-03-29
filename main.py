#!/usr/bin/env python3
import os
import sys
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
            '.ts', '.tsx', '.java', '.go', '.rs', '.php', '.rb'
        }

    def humanize_text(self, text):
        for layer in self.pipeline:
            text = layer.apply(text)
        return text

    def process_file(self, file_path):
        file_path = Path(file_path)
        if file_path.suffix not in self.valid_extensions:
            return

        print(f"📄 Procesando: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # Regex para comentarios según extensión
            import re
            if file_path.suffix == '.py':
                comment_re = re.compile(r'^(\s*)(#)\s*(.*)$')
            else:
                comment_re = re.compile(r'^(\s*)(//|#)\s*(.*)$')

            processed_lines = []
            for line in lines:
                match = comment_re.match(line)
                if match:
                    indent, symbol, content = match.groups()
                    if len(content.split()) > 2:
                        humanized = self.humanize_text(content)
                        processed_lines.append(f"{indent}{symbol} {humanized}\n")
                    else:
                        processed_lines.append(line)
                else:
                    processed_lines.append(line)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(processed_lines)
        except Exception as e:
            print(f"❌ Error en {file_path}: {e}")

    def run(self, target_path):
        path = Path(target_path)
        if path.is_file():
            self.process_file(path)
        elif path.is_dir():
            for root, _, files in os.walk(path):
                for file in files:
                    self.process_file(Path(root) / file)
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