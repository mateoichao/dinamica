import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# Configuración de la página
st.set_page_config(
    page_title="Calculadora de Movimiento de Proyectiles",
    page_icon="🎯",
    layout="wide"
)

# Título principal
st.title("🎯 Calculadora de Movimiento de Proyectiles")
st.markdown("---")

# Descripción del problema
st.markdown("""
### Descripción del Problema
El movimiento de proyectiles es un ejemplo clásico de movimiento en dos dimensiones bajo la acción de la gravedad.
Un proyectil se lanza con una velocidad inicial v₀ y un ángulo θ, describiendo una trayectoria parabólica.
""")

# Sidebar para parámetros
st.sidebar.header("⚙️ Parámetros de Entrada")

# Parámetros de entrada
v0 = st.sidebar.slider("Velocidad inicial (m/s)", 1.0, 100.0, 20.0, 0.1)
angle_deg = st.sidebar.slider("Ángulo de lanzamiento (°)", 0.0, 90.0, 45.0, 0.1)
height = st.sidebar.slider("Altura inicial (m)", 0.0, 50.0, 0.0, 0.1)
g = st.sidebar.number_input("Aceleración gravitacional (m/s²)", value=9.81, min_value=0.1, max_value=20.0)

# Convertir ángulo a radianes
angle_rad = math.radians(angle_deg)

# Componentes de velocidad inicial
v0x = v0 * math.cos(angle_rad)
v0y = v0 * math.sin(angle_rad)

# Cálculos principales
def calculate_projectile_motion(v0, angle_rad, height, g):
    """Calcula los parámetros del movimiento de proyectiles"""
    
    # Componentes de velocidad inicial
    v0x = v0 * math.cos(angle_rad)
    v0y = v0 * math.sin(angle_rad)
    
    # Tiempo de vuelo
    discriminant = v0y**2 + 2*g*height
    if discriminant < 0:
        t_flight = 0
    else:
        t_flight = (v0y + math.sqrt(discriminant)) / g
    
    # Altura máxima
    h_max = height + (v0y**2) / (2*g)
    
    # Tiempo para alcanzar altura máxima
    t_max = v0y / g
    
    # Alcance horizontal
    x_max = v0x * t_flight
    
    # Velocidad final
    vf_x = v0x  # No cambia
    vf_y = v0y - g * t_flight
    vf_magnitude = math.sqrt(vf_x**2 + vf_y**2)
    
    return {
        'v0x': v0x,
        'v0y': v0y,
        't_flight': t_flight,
        'h_max': h_max,
        't_max': t_max,
        'x_max': x_max,
        'vf_x': vf_x,
        'vf_y': vf_y,
        'vf_magnitude': vf_magnitude
    }

# Realizar cálculos
results = calculate_projectile_motion(v0, angle_rad, height, g)

# Mostrar resultados
col1, col2 = st.columns(2)

with col1:
    st.header("📊 Resultados del Cálculo")
    
    st.subheader("Velocidad Inicial")
    st.write(f"• Componente horizontal (v₀ₓ): **{results['v0x']:.2f} m/s**")
    st.write(f"• Componente vertical (v₀ᵧ): **{results['v0y']:.2f} m/s**")
    
    st.subheader("Parámetros de Vuelo")
    st.write(f"• Tiempo de vuelo: **{results['t_flight']:.2f} s**")
    st.write(f"• Altura máxima: **{results['h_max']:.2f} m**")
    st.write(f"• Tiempo hasta altura máxima: **{results['t_max']:.2f} s**")
    st.write(f"• Alcance horizontal: **{results['x_max']:.2f} m**")
    
    st.subheader("Velocidad Final")
    st.write(f"• Componente horizontal (vfₓ): **{results['vf_x']:.2f} m/s**")
    st.write(f"• Componente vertical (vfᵧ): **{results['vf_y']:.2f} m/s**")
    st.write(f"• Magnitud: **{results['vf_magnitude']:.2f} m/s**")

with col2:
    st.header("📈 Gráfico de Trayectoria")
    
    # Generar puntos para la trayectoria
    if results['t_flight'] > 0:
        t = np.linspace(0, results['t_flight'], 100)
        x = results['v0x'] * t
        y = height + results['v0y'] * t - 0.5 * g * t**2
        
        # Crear el gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Trayectoria
        ax.plot(x, y, 'b-', linewidth=2, label='Trayectoria')
        
        # Punto de lanzamiento
        ax.plot(0, height, 'go', markersize=8, label='Punto de lanzamiento')
        
        # Punto de impacto
        ax.plot(results['x_max'], 0, 'ro', markersize=8, label='Punto de impacto')
        
        # Altura máxima
        ax.plot(results['v0x'] * results['t_max'], results['h_max'], 'yo', markersize=8, label='Altura máxima')
        
        # Configurar el gráfico
        ax.set_xlabel('Distancia horizontal (m)')
        ax.set_ylabel('Altura (m)')
        ax.set_title('Trayectoria del Proyectil')
        ax.grid(True, alpha=0.3)
        ax.legend()
        ax.set_ylim(bottom=0)
        ax.set_xlim(left=0)
        
        # Mostrar el gráfico
        st.pyplot(fig)
    else:
        st.error("No se puede calcular la trayectoria con los parámetros dados.")

# Ecuaciones utilizadas
st.markdown("---")
st.header("📚 Ecuaciones Utilizadas")

st.markdown("""
### Ecuaciones del Movimiento de Proyectiles

**Componentes de velocidad inicial:**
- vₐₓ = v₀ × cos(θ)
- vₐᵧ = v₀ × sin(θ)

**Posición en función del tiempo:**
- x(t) = vₐₓ × t
- y(t) = h₀ + vₐᵧ × t - ½ × g × t²

**Tiempo de vuelo:**
- t = (vₐᵧ + √(vₐᵧ² + 2gh₀)) / g

**Altura máxima:**
- hₘₐₓ = h₀ + vₐᵧ² / (2g)

**Alcance horizontal:**
- xₘₐₓ = vₐₓ × t

**Velocidad final:**
- vfₓ = vₐₓ (constante)
- vfᵧ = vₐᵧ - g × t
- |vf| = √(vfₓ² + vfᵧ²)
""")

# Análisis adicional
st.markdown("---")
st.header("🔍 Análisis Adicional")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Ángulo Óptimo")
    # Para el ángulo óptimo (45° para h₀ = 0)
    optimal_angle = 45 if height == 0 else math.degrees(math.atan(v0 / math.sqrt(v0**2 + 2*g*height)))
    st.write(f"Para máximo alcance desde h₀ = {height} m:")
    st.write(f"**Ángulo óptimo: {optimal_angle:.1f}°**")
    
    # Calcular alcance con ángulo óptimo
    optimal_results = calculate_projectile_motion(v0, math.radians(optimal_angle), height, g)
    st.write(f"**Alcance óptimo: {optimal_results['x_max']:.2f} m**")

with col4:
    st.subheader("Energía del Sistema")
    # Energía cinética inicial
    ke_initial = 0.5 * 1 * v0**2  # asumiendo masa = 1 kg
    
    # Energía potencial inicial
    pe_initial = 1 * g * height  # asumiendo masa = 1 kg
    
    # Energía total
    e_total = ke_initial + pe_initial
    
    st.write("(Asumiendo masa = 1 kg)")
    st.write(f"• Energía cinética inicial: **{ke_initial:.2f} J**")
    st.write(f"• Energía potencial inicial: **{pe_initial:.2f} J**")
    st.write(f"• Energía total: **{e_total:.2f} J**")

# Información adicional
st.markdown("---")
st.info("""
💡 **Consejos para el uso:**
- Experimenta con diferentes ángulos para ver cómo afecta el alcance
- Observa cómo la altura inicial influye en el tiempo de vuelo
- El ángulo de 45° maximiza el alcance solo cuando se lanza desde el suelo
- La componente horizontal de la velocidad permanece constante durante todo el vuelo
""")