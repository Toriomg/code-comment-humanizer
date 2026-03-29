from layers.jargon import JargonLayer

def test_jargon_translation_general():
    layer = JargonLayer()
    text = "la funcion utiliza la base de datos"
    output = layer.apply(text)
    assert "func" in output
    assert "db" in output

def test_jargon_frontend_react():
    layer = JargonLayer()
    text = "este componente recibe propiedades"
    output = layer.apply(text)
    assert "comp" in output
    assert "props" in output

def test_jargon_low_level_c():
    layer = JargonLayer()
    text = "el puntero apunta a la direccion de memoria"
    output = layer.apply(text)
    assert "ptr" in output
    assert "addr" in output
    assert "mem" in output

def test_punctuation_integrity():
    layer = JargonLayer()
    text = "revisa la configuracion," # Con coma
    output = layer.apply(text)
    assert output == "revisa la config,"