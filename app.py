import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Radiografía Legislativa",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# ESTILOS
# ---------------------------------------------------

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0F172A;
    color: #F8FAFC;
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: white;
}

.subtitle {
    font-size: 20px;
    color: #CBD5E1;
    margin-bottom: 30px;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 15px;
    color: white;
}

.card {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 14px;
    border-left: 6px solid #2563EB;
    margin-bottom: 15px;
}

.critical {
    border-left: 6px solid #C62828;
}

.medium {
    border-left: 6px solid #F9A825;
}

.good {
    border-left: 6px solid #2E7D32;
}

.metric-card {
    background-color: #1E293B;
    padding: 18px;
    border-radius: 14px;
    text-align: center;
}

.footer {
    margin-top: 50px;
    text-align: center;
    color: #94A3B8;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

menu = st.sidebar.radio(
    "Navegación",
    [
        "Inicio",
        "Radiografía del Articulado",
        "Ley 819 de 2003",
        "Vulnerabilidades",
        "Fichas de Proposición",
        "Presión Negociadora",
        "Secuencia de Debate",
        "Conclusión Estratégica"
    ]
)

# ---------------------------------------------------
# DATA
# ---------------------------------------------------

articulado = pd.DataFrame({
    "Artículo": [
        "Art.1", "Art.2", "Art.4", "Art.5",
        "Art.6", "Art.7", "Art.8", "Art.9", "Art.10"
    ],
    "Materia": [
        "Objeto",
        "Objetivo General",
        "Campo de Aplicación",
        "Fases",
        "Responsables",
        "Presupuesto",
        "MFMP",
        "Reglamentación",
        "Informe"
    ],
    "Responsable": [
        "Gestión Social",
        "Gestión Social",
        "Alcaldía",
        "Múltiples actores",
        "Consejo Política Social",
        "Hacienda",
        "Hacienda",
        "Alcaldía",
        "Administración Distrital"
    ],
    "Riesgo": [
        "Medio",
        "Alto",
        "Alto",
        "Alto",
        "Crítico",
        "Crítico",
        "Crítico",
        "Medio",
        "Medio"
    ]
})

# ---------------------------------------------------
# INICIO
# ---------------------------------------------------

if menu == "Inicio":

    st.markdown('<div class="main-title">RADIOGRAFÍA LEGISLATIVA</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="subtitle">Proyecto de Acuerdo — Parques Neuroinclusivos y Neurodesarrollo</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Artículos", "10")

    with col2:
        st.metric("Riesgos críticos", "4")

    with col3:
        st.metric("Cumplimiento Ley 819", "20%")

    with col4:
        st.metric("Proposiciones clave", "4")

    st.markdown("---")

    st.markdown('<div class="section-title">Índice de Riesgo Legislativo</div>', unsafe_allow_html=True)

    categories = ['Fiscal', 'Jurídico', 'Operativo', 'Administrativo', 'Político']

    values = [95, 85, 80, 78, 45]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Riesgo'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        template="plotly_dark",
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# ARTICULADO
# ---------------------------------------------------

elif menu == "Radiografía del Articulado":

    st.markdown('<div class="section-title">Radiografía del Articulado</div>', unsafe_allow_html=True)

    st.dataframe(
        articulado,
        use_container_width=True,
        height=500
    )

# ---------------------------------------------------
# LEY 819
# ---------------------------------------------------

elif menu == "Ley 819 de 2003":

    st.markdown('<div class="section-title">Semáforo de Cumplimiento — Ley 819 de 2003</div>', unsafe_allow_html=True)

    st.progress(20)

    st.error("❌ No existe cuantificación del impacto fiscal")

    st.error("❌ No existe fuente de financiación identificada")

    st.warning("⚠️ Compatibilidad parcial con MFMP")

    st.error("❌ No existe concepto previo de Hacienda")

    st.error("❌ No existe incorporación expresa al POAI")

# ---------------------------------------------------
# VULNERABILIDADES
# ---------------------------------------------------

elif menu == "Vulnerabilidades":

    st.markdown('<div class="section-title">Mapa de Vulnerabilidades</div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["🔴 Críticas", "🟡 Medias", "🟢 Oportunidades"])

    # ---------------------------------------------------
    # CRÍTICAS
    # ---------------------------------------------------

    with tab1:

        with st.expander("1. Ausencia real de estudio de impacto fiscal"):

            st.markdown("""
### Problema

El acuerdo ordena:

- adecuación de parques
- mobiliario especializado
- rutas de transporte
- circuitos sensoriales

Sin cuantificar:

- costo unitario
- costo anual
- impacto plurianual

### Riesgo Jurídico

Vulneración directa del Art. 7 de la Ley 819 de 2003.

### Nivel de Riesgo

ALTO
""")

        with st.expander("2. Responsabilidad institucional difusa"):

            st.markdown("""
### Problema

No existe un ejecutor operativo único.

### Consecuencia

Nadie queda jurídicamente obligado a ejecutar metas.
""")

        with st.expander("3. Obligaciones abiertas e indeterminadas"):

            st.markdown("""
### Problema

No existen metas territoriales ni cronograma.

### Consecuencia

La Alcaldía podría cumplir simbólicamente.
""")

    # ---------------------------------------------------
    # MEDIAS
    # ---------------------------------------------------

    with tab2:

        with st.expander("5. Verbos rectores débiles"):

            st.markdown("""
- promover
- facilitar
- desarrollar

Generan discrecionalidad administrativa.
""")

        with st.expander("6. Informe vacío al Concejo"):

            st.markdown("""
No existe contenido mínimo obligatorio.
""")

    # ---------------------------------------------------
    # OPORTUNIDADES
    # ---------------------------------------------------

    with tab3:

        st.success("✅ Priorizar parques piloto por localidad")

        st.success("✅ Crear indicadores SMART")

        st.success("✅ Incorporar mantenimiento anual")

        st.success("✅ Crear mapa georreferenciado")

# ---------------------------------------------------
# FICHAS
# ---------------------------------------------------

elif menu == "Fichas de Proposición":

    st.markdown('<div class="section-title">Fichas de Proposición</div>', unsafe_allow_html=True)

    # ---------------------------------------------------

    st.subheader("FICHA 1 — Artículo Fiscal")

    col1, col2 = st.columns(2)

    with col1:
        st.error("""
### Texto Actual

“Incorpórese en el presupuesto las apropiaciones necesarias…”
""")

    with col2:
        st.success("""
### Texto Propuesto

“La Secretaría Distrital de Recreación y Deportes,
en coordinación con Hacienda,
incorporará las acciones derivadas del Acuerdo
en el POAI.”
""")

    st.info("""
PALANCA DE CURUL:

“¿Cuál es el costo unitario por parque neuroinclusivo?”
""")

    st.markdown("---")

    st.subheader("FICHA 2 — Indicadores SMART")

    col3, col4 = st.columns(2)

    with col3:
        st.error("""
### Texto Actual

No existe artículo.
""")

    with col4:
        st.success("""
### Texto Propuesto

- Número de parques
- Cobertura territorial
- Beneficiarios
- Ejecución presupuestal
""")

# ---------------------------------------------------
# PRESIÓN NEGOCIADORA
# ---------------------------------------------------

elif menu == "Presión Negociadora":

    st.markdown('<div class="section-title">Mapa de Presión Negociadora</div>', unsafe_allow_html=True)

    df = pd.DataFrame({
        "Vulnerabilidad": [
            "Impacto fiscal",
            "Responsabilidad difusa",
            "Sin indicadores",
            "Informe vacío",
            "Cobertura abierta"
        ],
        "Impacto": [10, 9, 8, 6, 7],
        "Viabilidad Política": [9, 8, 10, 9, 7]
    })

    fig = px.scatter(
        df,
        x="Impacto",
        y="Viabilidad Política",
        size="Impacto",
        color="Impacto",
        hover_name="Vulnerabilidad",
        template="plotly_dark",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# SECUENCIA DE DEBATE
# ---------------------------------------------------

elif menu == "Secuencia de Debate":

    st.markdown('<div class="section-title">Secuencia Estratégica de Debate</div>', unsafe_allow_html=True)

    st.markdown("""
## ETAPA 1 — PRIMER DEBATE

### Objetivo
Fortalecer técnicamente el proyecto.

### Prioridades
- Artículo fiscal
- Responsable único
- Indicadores SMART
- Informe obligatorio
""")

    st.markdown("---")

    st.markdown("""
## ETAPA 2 — ENTRE DEBATES

### Solicitar:
- Concepto de Hacienda
- Estimación de costos
- Inventario de parques
- Viabilidad técnica
""")

    st.markdown("---")

    st.markdown("""
## ETAPA 3 — SEGUNDO DEBATE

### Condicionar apoyo político a:
- metas verificables
- apropiación presupuestal
- cronograma
""")

# ---------------------------------------------------
# CONCLUSIÓN
# ---------------------------------------------------

elif menu == "Conclusión Estratégica":

    st.markdown('<div class="section-title">Conclusión Estratégica</div>', unsafe_allow_html=True)

    st.error("""
# CONCLUSIÓN

El proyecto posee legitimidad social alta,
pero presenta debilidad estructural en:

- sostenibilidad fiscal
- trazabilidad administrativa
- exigibilidad normativa
- control político

El escenario óptimo es utilizar
proposiciones de fortalecimiento técnico
sin confrontar el objeto social del acuerdo.
""")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
Radiografía Legislativa — Concejo Distrital de Barranquilla
</div>
""", unsafe_allow_html=True)
