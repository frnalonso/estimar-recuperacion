import streamlit as st
from components.body_map import draw_body_with_markers
from components.predictor import predecir_dias_baja

st.title("Ingresá tu jugador")

col_img, col_form = st.columns([1, 2])

# Imagen del cuerpo
with col_img:
    zona_actual = st.session_state.get("zona_actual", None)
    img = draw_body_with_markers(zonas=[zona_actual] if zona_actual else [])
    st.image(img, width=150)

# Formulario
with col_form:
    st.subheader("Datos del jugador")

    nombre = st.text_input("Nombre del jugador")
    edad_en_lesion = st.number_input("Edad en la lesión: ", min_value=10, max_value=100)
    edad = st.number_input("Edad actual del jugador: ", min_value=10, max_value=100)
    lesiones_previas = st.number_input("Cantidad de lesiones previas", min_value=1, max_value=100)
    gravedad_clinica = st.selectbox("Seleccione la gravedad clinica de su lesión", ["Leve", "Moderada", "Grave"])

    st.subheader("Datos de la lesión")

    zona = st.selectbox(
        "Zona lesionada",
        ['Abdominal Interna', 'Cabeza-Cara', 'Columna', 'Condición Física',
 'Enfermedad', 'Extremidad Inferior', 'Extremidad Superior', 'Inguinal-Pubis',
 'Ligamentaria', 'Muscular', 'Neurológico', 'Otras', 'Postoperatorio',
 'Tendinosa', 'Trauma', 'Tórax', 'Ósea'],
    )

    tipo = st.selectbox(
        "Tipo de lesión",
        ['Abdominoplastia', 'Absceso', 'Accidente de tráfico', 'Amigdalitis', 'Angina', 'Apendicectomía', 'Apendicitis', 'Artroscopia', 'Astillado de hueso', 'Becerro jalado', 'Bloqueo en la espalda', 'Bronquitis', 'Bursitis', 'Cansancio muscular', 'Cirugía', 'Cirugía de cálculos renales', 'Cirugía de nariz', 'Cirugía del ligamento cruzado', 'Cirugía del tendón de Aquiles', 'Cirugía del tobillo', 'Cirugía dental', 'Cirugía intestinal', 'Compresión espinal', 'Compresión ósea', 'Conmoción', 'Contractura', 'Contusión', 'Contusión de cadera', 'Contusión de rodilla', 'Contusión del tendón de Aquiles', 'Contusión muscular', 'Contusión púbica', 'Coronavirus', 'Costilla fracturada', 'Cráneo fracturado', 'Cuarentena', 'Cáncer', 'Cáncer de glándula linfática', 'Cáncer de testículo', 'Cóccix magullado', 'Daño cartilaginoso', 'Daño de menisco', 'Daño parcial al ligamento cruzado', 'Depresión/Burnout', 'Derrame cerebral', 'Descanso', 'Desgarro de banda interna', 'Desgarro del aductor', 'Desgarro del tendón', 'Desgarro fibrilar', 'Desgarro miofascial', 'Desgarro muscular', 'Desgarro muscular del gemelo', 'Desgarro parcial de la fascia plantar', 'Desgarro parcial del músculo', 'Desgarro parcial del tendón rotuliano', 'Disco herniado', 'Distensión de muslo', 'Distensión del ligamento cruzado', 'Distensión inguinal', 'Distorsión de banda interna', 'Distorsión de la banda lateral de la rodilla', 'Distorsión del tobillo', 'Doble rotura de ligamento', 'Dolor de dientes', 'Dolores musculares', 'Edema de rodilla', 'Edema óseo', 'Endurecimiento de terneros', 'Endurecimiento muscular', 'Enfermedad viral', 'Enfermo', 'Esguince', 'Esguince de la articulación del tobillo', 'Esguince de tobillo', 'Espolón calcáneo', 'Estiramiento de banda', 'Estiramiento de los músculos de los muslos y los glúteos', 'Estiramiento del ligamento cruzado', 'Extensión del ligamento interno de la rodilla', 'Falta de condición física', 'Fiebre', 'Fisura del peroné', 'Fisura fina en el peroné', 'Fisura fina en el pie', 'Fractura', 'Fractura de antebrazo', 'Fractura de clavícula', 'Fractura de cráneo basal', 'Fractura de dedo', 'Fractura de escafoides', 'Fractura de fémur', 'Fractura de hombro', 'Fractura de la mandíbula', 'Fractura de la pierna', 'Fractura de mano', 'Fractura de media cara', 'Fractura de muñeca', 'Fractura de ombligo', 'Fractura de peroné', 'Fractura de pómulo', 'Fractura de rótula', 'Fractura de tibia', 'Fractura de tibia y peroné', 'Fractura de tobillo', 'Fractura de vértebra lumbar', 'Fractura del arco del ojo', 'Fractura del brazo', 'Fractura del cúbito', 'Fractura del pie', 'Fractura del pulgar', 'Fractura del tabique nasal', 'Fractura delgada en el dedo medio', 'Fractura facial', 'Fractura lumbar', 'Fractura metacarpiana', 'Fractura metatarsiana', 'Fractura orbitaria', 'Fractura por fatiga', 'Fémur desgarrado', 'Gastroenteritis gripal', 'Golpe', 'Golpe de muslo', 'Gripe', 'Hematoma', 'Hematoma acromioclavicular', 'Hematoma de la articulación del tobillo', 'Hematoma de la tibia', 'Hematoma en el pie', 'Hematoma en el pómulo', 'Hematoma en el tobillo', 'Hematoma metatarsiano', 'Hematoma pulmonar', 'Hemorragia cerebral', 'Herida abierta', 'Herida inflamada', 'Herida lacerada', 'Herida menor', 'Herida superficial', 'Hernia inguinal', 'Iirritación púbica', 'Incineración', 'Infección', 'Infección gripal', 'Inflamación', 'Inflamación de la médula ósea', 'Inflamación de los ligamentos de la rodilla', 'Inflamación de rodilla', 'Inflamación del pie', 'Inflamación del tendón del bíceps en el muslo', 'Inflamación del tobillo', 'Inflamación en la cabeza del peroné', 'Irritación del menisco', 'Irritación del tendón', 'Irritación del tendón de Aquiles', 'Irritación del tendón rotuliano', 'Lesión de banda lateral', 'Lesión de cadera', 'Lesión de codo', 'Lesión de cuello', 'Lesión de cápsula', 'Lesión de espalda', 'Lesión de hombro', 'Lesión de ligamentos', 'Lesión de los músculos abdominales', 'Lesión de mano', 'Lesión de muñeca', 'Lesión de nariz', 'Lesión de pierna', 'Lesión de pulgar', 'Lesión de rodilla', 'Lesión de talón', 'Lesión de tobillo', 'Lesión del aductor', 'Lesión del brazo', 'Lesión del ligamento cruzado', 'Lesión del músculo flexor de la pierna', 'Lesión del tendón peroneo', 'Lesión desconocida', 'Lesión en el dedo de la mano', 'Lesión en el dedo del pie', 'Lesión en el gemelo', 'Lesión en el muslo', 'Lesión en el pie', 'Lesión en el tobillo', 'Lesión en el tórax', 'Lesión en la columna cervical', 'Lesión en la espinilla', 'Lesión facial', 'Lesión inguinal', 'Lesión meniscal', 'Lesión muscular', 'Lesión ocular', 'Lesión por latigazo', 'Lesión pélvica', 'Lesión vertebral', 'Ligamento roto', 'Ligamento roto Articulación del tobillo', 'Ligamento roto de rodilla', 'Ligamento roto en el tarso', 'Lumbalgia', 'Luxación', 'Luxación de la rótula', 'Magulladuras en las costillas', 'Malaria', 'Malestar abdominal', 'Menisco desgarrado', 'Molestias en los aductores', 'Molestias en los gemelos', 'Mononucleosis infecciosa', 'Moratón', 'Moratón en la espalda', 'Moratón en la espinilla', 'Moratón tibial', 'Nervio oprimido', 'Neumotórax', 'Operación con el pie', 'Operación de ingle', 'Operación de rodilla', 'Osteítis', 'Pancratitis', 'Picadura de insecto', 'Problemas cardíacos', 'Problemas de cadera', 'Problemas de ciática', 'Problemas de espalda', 'Problemas de las vértebras lumbares', 'Problemas de ligamentos', 'Problemas de rodilla', 'Problemas de talón', 'Problemas de tobillo', 'Problemas del talón de Aquiles', 'Problemas del tendón de Aquiles', 'Problemas del tendón rotuliano', 'Problemas en el arco del pie', 'Problemas en el flexor de la cadera', 'Problemas en el flexor derecho de la cadera', 'Problemas en el flexor izquierdo de la cadera', 'Problemas en los muslos', 'Problemas estomacales', 'Problemas inguinales', 'Problemas musculares', 'Problemas renales', 'Pubalgia', 'Pubis', 'Pulmonía', 'Quiste en la rodilla', 'Quiste en los pulmones', 'Reacción de estrés del hueso', 'Resfriado', 'Retirar los tornillos/clavos', 'Rotura de fibras', 'Rotura de fibras en el aductor', 'Rotura de la cápsula articular del tobillo', 'Rotura de ligamento colateral de la rodilla', 'Rotura de ligamentos', 'Rotura de ligamentos del tobillo', 'Rotura de menisco', 'Rotura de tendones', 'Rotura del ligamento colateral de la rodilla', 'Rotura del ligamento cruzado', 'Rotura del ligamento de la rodilla', 'Rotura del ligamento de la sindesmosis', 'Rotura del ligamento externo de la rodilla', 'Rotura del ligamento externo del tobillo', 'Rotura del ligamento interno de la rodilla', 'Rotura del ligamento interno del tobillo', 'Rotura del ligamento lateral externo', 'Rotura del ligamento lateral interno', 'Rotura del menisco externo', 'Rotura del tendón de Aquiles', 'Rotura del tendón rotuliano', 'Rotura del tímpano', 'Rotura testicular', 'Sobrecarga', 'Sobreestiramiento', 'Sobreestiramiento de la banda de sindesmosis', 'Síndrome de la punta del tendón rotuliano', 'Tajada', 'Tejuelas', 'Tendonitis', 'Tirón muscular', 'Traumatismo', 'Traumatismo craneal', 'Tuberculosis', 'Varicela', 'Virus intestinal', 'Voladura acromioclavicular']
    )

    if st.button("Agregar lesión"):
        st.session_state.zona_actual = zona
        st.success(f"Lesión agregada: {zona} - {tipo}")

    if st.button("Predecir recuperación"):
        dias = predecir_dias_baja(
            edad_en_lesion = edad_en_lesion,
            zona=zona,
            gravedad_clinica=gravedad_clinica,      # podés hacer un selectbox si querés
            lesion=tipo,
            lesiones_previas_totales=lesiones_previas,
            edad=edad,
            )

        st.success(f"Estimación: **{dias} días fuera**")
