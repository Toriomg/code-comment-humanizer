import pytest
from layers.styler import StylerLayer

def test_styler_random_behavior():
    layer = StylerLayer()
    text = "Mensaje de prueba."
    
    # Ejecutamos varias veces para ver si la aleatoriedad funciona
    results = [layer.apply(text) for _ in range(150)]
    
    # Verificar que al menos algunas veces empieza con minúscula
    assert any(r[0].islower() for r in results)
    
    # Verificar que al menos algunas veces no tiene punto final
    assert any(not r.endswith('.') for r in results)
    