import pytest
from layers.cleaner import CleanerLayer

def test_ai_phrase_removal():
    layer = CleanerLayer()
    input_text = "Esta función se encarga de calcular el total"
    output = layer.apply(input_text)
    assert "esta función se encarga de" not in output
    assert output == "calcular el total"

def test_emoji_removal():
    layer = CleanerLayer()
    input_text = "Procesando datos 🚀 ✅"
    output = layer.apply(input_text)
    assert "🚀" not in output
    assert "✅" not in output
    assert output == "procesando datos"

def test_emoticon_removal():
    layer = CleanerLayer()
    input_text = "Listo para deploy :D XD"
    output = layer.apply(input_text)
    assert ":D" not in output
    assert "xd" not in output
    assert output == "listo para deploy"

def test_numbered_list_removal():
    layer = CleanerLayer()
    
    # Caso simple
    assert layer.apply("1. Configurar el servidor") == "configurar el servidor"
    
    # Caso con número de dos cifras
    assert layer.apply("10. Retornar el resultado") == "retornar el resultado"
    
    # Caso donde el número está en medio (NO debe quitarlo)
    # Solo queremos quitarlo si es un formato de lista al inicio
    assert layer.apply("el puerto 80.80 es el default") == "el puerto 80.80 es el default"

def test_camelcase_and_accents():
    layer = CleanerLayer()
    # Debería quitar acento de 'función' y 'autenticación'
    # Debería mantener 'UserManager' y 'API'
    input_txt = "Esta función llama al UserManager de la API para la autenticación."
    output = layer.apply(input_txt)
    
    assert "funcion" in output # Sin acento
    assert "UserManager" in output # CamelCase preservado
    assert "API" in output # Acrónimo preservado
    assert "autenticacion" in output # Sin acento