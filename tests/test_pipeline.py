from main import CommentHumanizer

def test_full_transformation():
    humanizer = CommentHumanizer()
    ai_comment = "Esta función se encarga de configurar la base de datos 🚀."
    
    output = humanizer.humanize_text(ai_comment)
    
    # El resultado final debería:
    # 1. No tener la frase de IA
    # 2. No tener emojis
    # 3. Tener abreviaturas (db, config)
    # 4. Probablemente no tener punto final o estar en minúsculas
    
    assert "esta función" not in output
    assert "🚀" not in output
    assert "db" in output or "config" in output
    print(f"\n[Test Integración] Entrada: {ai_comment} -> Salida: {output}")
    ai_comment = "1. me gustan los macarrones."
    output = humanizer.humanize_text(ai_comment)
    print(f"\n[Test Integración] Entrada: {ai_comment} -> Salida: {output}")


