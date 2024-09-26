# Traductor de Audio con IA 🤖✨

Este proyecto es una aplicación web que utiliza inteligencia artificial para transcribir y traducir audios a varios idiomas. La aplicación transcribe el audio, detecta automáticamente el idioma original, traduce el texto transcrito a los idiomas seleccionados por el usuario y genera archivos de audio con la traducción correspondiente.

He de agradecer a  [MoureDev](https://youtu.be/oxLvf2nDCvQ?si=8fC2fkEkYl_FwSfc) por compartir sus conocimientos y por ser esa eterna fuente de inspiración.

## Características 🛠️

- **Transcripción de Audio**: Utiliza el modelo [Whisper](https://github.com/openai/whisper) para transcribir audios desde el archivo cargado o desde el propio micrófono del usuario.

- **Traducción**: Traduce el texto transcrito a varios idiomas usando la librería [Translate](https://github.com/terryyin/translate-python).

- **Síntesis de Voz**: Genera archivos de audio para cada idioma traducido utilizando la API de [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/docs/libraries?hl=es-419#client-libraries-install-python).

- **Interfaz Gráfica**: Proporciona una interfaz de usuario para cargar audios, seleccionar idiomas para la traducción, y reproducir los audios traducidos usando [Gradio](https://www.gradio.app/).

## Capturas del proyecto 💻

Interfaz: 

![https://github.com/Monxiidev](Traductor-de-audio-con-IA/Images/Interfaz/Interfaz-inicial.png)


Transcripciones

Inglés:

![https://github.com/Monxiidev](Traductor-de-audio-con-IA/Images/Transcriptions/English-Transcription.png)

Frances:

![https://github.com/Monxiidev](Traductor-de-audio-con-IA/Images/Transcriptions/French-Transcription.png)

Italiano:

![https://github.com/Monxiidev](Traductor-de-audio-con-IA/Images/Transcriptions/Italian-Transcription.png)

Español:

![https://github.com/Monxiidev](Traductor-de-audio-con-IA/Images/Transcriptions/Espanish-Transcription.png)

Interfaz completa:

![https://github.com/Monxiidev](Traductor-de-audio-con-IA/Images/Interfaz/Interfaz-completa.png)



## Instalación ⚙️

1. Clona el repositorio:

   git clone https://github.com/Monxiidev/Traductor-de-audio-con-IA.git
   cd Traductor-de-audio-con-IA

2. Crea y activa un entorno virtual (opcional pero se trata de buenas prácticas así que lo recomiendo encarecidamente):

   python3 -m venv .venv
   source .venv/bin/activate  

# En Windows se usa `.venv\Scripts\activate`

3. Instala las dependencias:

   pip install -r requirements.txt

4. Configura las credenciales de Google Cloud Text-to-Speech. Asegúrate de tener configurada la variable de entorno `GOOGLE_APPLICATION_CREDENTIALS` con el path a tu archivo de credenciales JSON descargado desde Google Cloud Console.

   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials.json"


## Uso

1. Ejecuta la aplicación:

   python traductor_de_audio.py
sh
2. Abre tu navegador web e ingresa a la dirección proporcionada por Gradio.

Imagen del running

3. Carga un archivo de audio o graba tu voz usando tu micrófono, selecciona los idiomas a los que deseas traducir y haz clic en "Traducir".

## Estructura del Código

- `main.py`: Es el Script principal que define el flujo de la interfaz gráfica y las funciones de transcripción, traducción y síntesis de voz.

- `requirements.txt`: Es la lista de dependencias necesarias a instalar para ejecutar el proyecto.

## Tecnologías Utilizadas

- [Python](https://www.python.org): Como lenguaje de programación
- [Gradio](https://www.gradio.app/): Para la interfaz gráfica del usuario.
- [Whisper](https://github.com/openai/whisper): Para la transcripción de audio.
- [Translate](https://github.com/terryyin/translate-python): Para la traducción de texto.
- [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/docs/libraries?hl=es-419#client-libraries-install-python): Para la generación de audio traducido.
- [Langdetect](https://pypi.org/project/langdetect/): Para la detección del idioma del texto.

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de hacer un fork del proyecto, crear una rama, agregar tus cambios y enviar un pull request.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Ver el archivo LICENSE para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, siéntete libre de abrir un issue o contactarme directamente.

¡Gracias por usar el Traductor de Audio con IA! 🚀🎉
