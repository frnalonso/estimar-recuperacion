def predict_days_out(zona, tipo_lesion, edad, altura):
    """
    Esta función es de ejemplo.
    Después la reemplazás por tu modelo real.
    """
    base = 20

    if tipo_lesion == "Fractura":
        base += 40
    elif tipo_lesion == "Esguince":
        base += 10

    if zona == "Rodilla":
        base += 15

    if edad > 30:
        base += 5

    return base
