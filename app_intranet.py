import streamlit as st
import pandas as pd
import os

# Configuración de la página
st.set_page_config(
    page_title="EXPORCARMIN S.A.S. - Intranet",
    page_icon="⚖️",
    layout="wide"
)

# --- 1. SISTEMA DE AUTENTICACIÓN (LOGIN) ---
def verificar_login():
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    if not st.session_state.autenticado:
        st.subheader("🔐 Acceso Restringido - EXPORCARMIN S.A.S.")
        usuario = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        
        if st.button("Ingresar"):
            # Credenciales de acceso corporativo (puedes ajustarlas)
            if usuario == "admin" and password == "exporcarmin2026":
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos")
        return False
    return True

# Ejecutar validación de login antes de mostrar el sistema
if verificar_login():
    
    # --- 2. INTERFAZ PRINCIPAL DE LA INTRANET ---
    st.sidebar.title("Administración")
    st.sidebar.write("Seleccione el Maestro:")
    
    menu = st.sidebar.radio(
        "",
        ["Productos", "Tipos", "Zonas", "Patios", "Pilas", "Destinos", "Puntos de Entrega"]
    )

    st.sidebar.markdown("---")
    st.sidebar.info("⚡ Sistema sincronizado con la báscula de EXPORCARMIN S.A.S.")

    # Panel Principal
    st.title(f"Gestión de {menu}")
    st.write(f"Panel de administración centralizado para el control de {menu.lower()} en la operación.")

    # Simulación de datos maestros
    data_ejemplo = {
        "Nombre": ["CARBON", "COQUE", "ESTERIL"],
        "Codigo": ["CARB", "COQ", "EST"],
        "Estado": ["Activo", "Activo", "Activo"]
    }
    df = pd.DataFrame(data_ejemplo)

    # Botón para crear nuevo registro
    if st.button("➕ Crear Nuevo"):
        st.success(f"Abriendo formulario para registrar nuevo elemento en {menu}...")

    st.markdown("### 📋 Registros Existentes")
    st.dataframe(df, use_container_width=True)

    # Acciones sobre registros
    st.markdown("---")
    st.markdown("### ⚡ Acciones sobre Registros Existentes")
    
    col1, col2 = st.columns(2)
    with col1:
        reg_estado = st.selectbox("Seleccione registro para cambiar Estado:", df["Nombre"])
        if st.button("Cambiar Estado (Activo / Inactivo)"):
            st.success(f"El estado de {reg_estado} ha sido actualizado.")
            
    with col2:
        reg_eliminar = st.selectbox("Seleccione registro para eliminar:", df["Nombre"], key="del")
        if st.button("Eliminar Registro Permanentemente", type="primary"):
            st.warning(f"Registro {reg_eliminar} eliminado correctamente.")

    # Botón de cierre de sesión
    st.sidebar.markdown("---")
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()