# 🛠️ Editor de Modelos de Motocicleta JSON

Aplicación desarrollada para el área de **Canal Digital** con el fin de facilitar la edición de archivos `.json` que contienen la base de conocimiento del modelo de inteligencia artificial que responde preguntas sobre motocicletas Yamaha.

---

## 🎯 Propósito

Esta herramienta permite actualizar de forma sencilla:

- Precios sugeridos
- Especificaciones técnicas
- Disponibilidad de modelos
- Mensajes comerciales y técnicos

Así se garantiza que el sistema de IA brinde información precisa y vigente.

---

## 📂 Estructura esperada del JSON

El archivo JSON debe tener una estructura tipo diccionario con claves numéricas y valores tipo objeto:

```json
{
  "0": {
    "Categoria": "Scooter",
    "Nombre o modelo": "XMAX",
    "Año modelo": "2024",
    "Precio": "...",
    "Mensaje comercial": "...",
    "Mensaje Tecnico": "...",
    "Mensaje de disponibilidad ": "..."
  },
  "1": {
    // Otro modelo
  }
}

🚀 Cómo ejecutar la aplicación
Asegúrate de tener Python 3.8 o superior instalado en tu equipo.

Clona el repositorio o descarga el archivo .py:

git clone https://github.com/tu-org/editor-modelos-motos-json.git
cd editor-modelos-motos-json

Ejecuta el archivo:
python editor_informacion_modelos_motos.py

Selecciona el archivo JSON que deseas editar desde la interfaz.

🖥️ Funcionalidades destacadas
✅ Interfaz gráfica amigable (Tkinter)

✅ Carga de archivos .json con soporte para utf-8 y utf-8-sig

✅ Vista tipo tabla con buscador

✅ Edición con doble clic en cada registro

✅ Creación de nuevos modelos desde la app

✅ Guardado automático de los cambios

✅ Redimensionable y responsiva

✅ Pie de página institucional:
Desarrollado por Nuevas Tecnologías División TI

🧠 Impacto
Los archivos editados por esta herramienta son consumidos por el motor de IA para responder preguntas como:

¿Cuánto cuesta la MT03?

¿Qué motor tiene la XTZ125?

¿La Aerox tiene freno ABS?

¿Está disponible la FZ25?

Mantener este contenido actualizado asegura respuestas confiables en canales digitales y asistentes virtuales.

🤝 Créditos
Desarrollado por el equipo de Nuevas Tecnologías - División TI, para uso exclusivo del área Canal Digital.

📧 Contacto: afgiraldo@incolmotos-yamaha.com.co
