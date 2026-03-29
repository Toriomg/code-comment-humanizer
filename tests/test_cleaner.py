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