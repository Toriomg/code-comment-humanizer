class JargonLayer:
    def __init__(self):
        self.dictionary = {
            # --- GENERAL / CORE ---
            "funcion": "func",
            "funciones": "funcs",
            "parametros": "params",
            "argumentos": "args",
            "configuracion": "config",
            "informacion": "info",
            "identificador": "id",
            "variable": "var",
            "temporal": "tmp",
            "resultado": "res",
            "anterior": "prev",
            "siguiente": "next",
            "error": "err",
            "excepcion": "exc",
            "instancia": "inst",
            "objeto": "obj",
            "clase": "cls",
            "iterador": "iter",
            "generador": "gen",
            "contexto": "ctx",
            "ayudante": "helper",
            "utilidad": "util",
            "biblioteca": "lib",
            "paquete": "pkg",
            "dependencia": "dep",
            "archivo": "file",
            "directorio": "dir",
            "camino": "path",
            "sistema operativo": "SSOO",

            # --- INFRA & DB ---
            "base de datos": "db",
            "conexion": "conn",
            "consulta": "query",
            "registro": "log",
            "servidor": "srv",
            "cliente": "cli",
            "produccion": "prod",
            "desarrollo": "dev",
            "entorno": "env",
            "autenticacion": "auth",
            "autorizacion": "authz",
            "peticion": "req",
            "respuesta": "res",
            "cabecera": "hdr",
            "cuerpo": "body",
            "mensaje": "msg",

            # --- FRONTEND (React, JS, HTML/CSS) ---
            "componente": "comp",
            "propiedades": "props",
            "referencia": "ref",
            "estado": "state",
            "efecto": "effect",
            "gancho": "hook",
            "manejador": "handler",
            "evento": "evt",
            "navegación": "nav",
            "ventana": "win",
            "documento": "doc",
            "estilo": "style",
            "clase css": "class",
            "botón": "btn",
            "formulario": "form",
            "entrada": "input",

            # --- BACKEND & PYTHON (Django/Flask) ---
            "modelo": "mdl",
            "vista": "view",
            "controlador": "ctrl",
            "serializador": "ser",
            "plantilla": "tpl",
            "decorador": "dec",
            "conjunto datos": "ds",
            "entorno virtual": "venv",
            "comando": "cmd",
            "tarea": "task",
            "cola": "queue",

            # --- LOW LEVEL & C ---
            "puntero": "ptr",
            "direccion": "addr",
            "memoria": "mem",
            "asignacion": "alloc",
            "entero": "int",
            "cadena": "str",
            "caracter": "char",
            "arreglo": "arr",
            "matriz": "mtx",
            "bufer": "buf",
            "estructura": "struct",
            "fuente": "src",
            "destino": "dst",
            "valor": "val",
            "índice": "idx"
        }

        self.sorted_keys = sorted(self.dictionary.keys(), key=len, reverse=True)

    def apply(self, text):
        processed = text
        for key in self.sorted_keys:
            if key in processed:
                processed = processed.replace(key, self.dictionary[key])
        return processed