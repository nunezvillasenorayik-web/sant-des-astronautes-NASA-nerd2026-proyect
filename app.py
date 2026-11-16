import math
import random

# --- CONSTANTES DEL MODELO ---
FUERZA_PARTICULA = (
    8.35e-22  # Newtons (F = m * a para una partícula de regolito)
)


def simular_impactos_esfera(num_particulas):
  fuerza_total = 0.0
  for _ in range(num_particulas):
    # Ángulos aleatorios en coordenadas esféricas
    theta = random.uniform(0, math.pi)  # De Polo Norte a Sur
    phi = random.uniform(0, 2 * math.pi)  # Vuelta completa horizontal

    # Factor direccional usando el jacobiano sen ( theta)
    componente_area = math.sin(theta)

    # Acumular fuerza de impacto direccional
    fuerza_total += FUERZA_PARTICULA * componente_area

  return fuerza_total


def evaluar_riesgo_vascular(fuerza_acumulada):
  presion_vascular = fuerza_acumulada * 1e15
  if presion_vascular > 5.0:
    return "[ALERTA] Alto riesgo de estrés endotelial y vasoconstricción."
  else:
    return "Estado vascular estable."


# --- INICIO DE TELEMETRÍA ---
print("=================================================")
print("   [SYSTEM INITIALIZED]  welcome  of Santé des Espace - NASA  ")
print("=================================================\n")

nombre = input("What is your name? / Cual es tu nombre?: ")
edad = input("What is your age? / Cual es tu edad?: ")

# Altura y validación con estándares NASA
altura = float(input("What is your height (m)? / Cual es tu altura (m)?: "))
if 1.57 <= altura <= 1.90:
  print(
      "[ÓPTIMO] Estatura dentro del rango antropométrico estándar de la NASA"
      " (1.57m - 1.90m)."
  )
else:
  print(
      "[ADVERTENCIA] Estatura fuera del rango estándar. Revisa ergonomía de"
      " cabina."
  )

# Peso y validación
peso = float(input("Enter your weight (kg) / Ingresa tu peso en kg: "))
if 50 <= peso <= 95:
  print(
      "[ÓPTIMO] Peso corporal dentro de los límites seguros para tolerancia"
      " ortostática."
  )
else:
  print(
      "[ADVERTENCIA] Desviación de peso detectada. Mayor riesgo cardiovascular"
      " al reingreso."
  )

# --- SIMULACIÓN DE IMPACTO ---
print("\n-------------------------------------------------")
print("[SIMULACIÓN] Ejecutando modelo de Monte Carlo con regolito...")
num_particulas = 1000
fuerza_acumulada = simular_impactos_esfera(num_particulas)
print(f"Fuerza base acumulada calculada: {fuerza_acumulada:.2e} N")

# Evaluación vascular y luz verde visual
presion_vascular = fuerza_acumulada * 1e15
if presion_vascular <= 5.0 and 50 <= peso <= 95:
  print("[ 🟢 STATUS: GREEN LIGHT / LUZ VERDE ] - Parámetros óptimos.")
else:
  print("[ 🔴 STATUS: RED ALERT / ALERTA ] - Parámetros fuera de rango.")

# --- DURACIÓN DE LA MISIÓN ---
numero_de_dias = int(
    input(
        "\nHow long is the mission in days? / Cuales la duracion en dias"
        " de la mision?: "
    )
)

if numero_de_dias <= 180:
  print(
      "[PERFIL] La duración estándar (hasta 180 días) equilibra la"
      " investigación y la seguridad."
  )
else:
  print(
      "[ALERTA DE EXPOSICIÓN] La misión supera los 6 meses. Se requiere"
      " vigilancia estricta."
  )

# Cálculo acumulado total por días de misión
impacto_total_mision = fuerza_acumulada * numero_de_dias

# --- GUARDAR REPORTE DE TELEMETRÍA ---
with open("reporte_mision_nasa.txt", "w", encoding="utf-8") as archivo:
  archivo.write("=== REPORTE OFICIAL DE TELEMETRÍA - SANTÉ DES ESPACE ===\n")
  archivo.write(f"Astronauta: {nombre}\n")
  archivo.write(f"Edad: {edad}\n")
  archivo.write(f"Duración de Misión: {numero_de_dias} días\n")
  archivo.write(f"Impacto Acumulado Total: {impacto_total_mision:.2e} N\n")
  archivo.write("Estado: Verificado por Sistema de Monitoreo Orbital.\n")

print(
    "\n[LOG SUCCESS] Archivo 'reporte_mision_nasa.txt' generado y guardado"
)
