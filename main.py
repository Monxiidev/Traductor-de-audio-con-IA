import gradio as gr
import whisper
from translate import Translator
from langdetect import detect
from google.cloud import texttospeech
from concurrent.futures import ThreadPoolExecutor

LANGUAGE_MAP = {
    "Inglés": "en",
    "Italiano": "it",
    "Francés": "fr",
    "Portugués": "pt",
    "Alemán": "de",
    "Árabe": "ar",
    "Catalán": "ca",
    "Coreano": "ko",
    "Ruso": "ru",
    "Español": "es"
}

def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"Error en {func.__name__}: {str(e)}")
        return None

def translator(audio_file, selected_languages):
    transcription, detected_language = safe_execute(transcribe_audio, audio_file)
    if not transcription:
        raise gr.Error("Error al transcribir el audio.")
    
    selected_language_codes = [LANGUAGE_MAP[lang] for lang in selected_languages]
    translations = safe_execute(translate_text_async, transcription, detected_language, selected_language_codes)
    if not translations:
        raise gr.Error("Error al traducir el texto.")
    
    audio_files = safe_execute(generate_translated_audio, translations)
    if not audio_files:
        raise gr.Error("Error al generar audios traducidos.")
    
    audio_outputs = []
    for lang, audio_path in zip(selected_languages, audio_files):
        audio_outputs.append(gr.update(visible=True, value=audio_path, label=lang))
    
    audio_outputs += [gr.update(visible=False)] * (10 - len(audio_outputs))
    
    return audio_outputs

def transcribe_audio(audio_file):
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_file, language=None, fp16=False)
        transcription = result["text"]
        detected_language = detect(transcription)
        print(f"Texto original: {transcription} (Idioma detectado: {detected_language})")
        return transcription, detected_language
    except Exception as e:
        raise gr.Error(f"Error al transcribir el audio: {str(e)}")

def translate_text_async(transcription, detected_language, selected_language_codes):
    translations = {}

    def translate(lang_code):
        try:
            translator = Translator(from_lang=detected_language, to_lang=lang_code)
            return lang_code, translator.translate(transcription)
        except Exception as e:
            print(f"Error al traducir a {lang_code}: {str(e)}")
            return lang_code, None

    with ThreadPoolExecutor() as executor:
        results = executor.map(translate, selected_language_codes)

    for lang_code, translation in results:
        if translation:
            translations[lang_code] = translation
            print(f"Texto traducido a {lang_code}: {translation}")

    return translations

def generate_translated_audio(translations):
    audio_paths = []
    try:
        for lang_code, text in translations.items():
            audio_path = text_to_speech(text, lang_code)
            audio_paths.append(audio_path)
        return audio_paths
    except Exception as e:
        raise gr.Error(f"Error al generar audios traducidos: {str(e)}")

def text_to_speech(text: str, language: str) -> str:
    try:
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code=language,
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )
        response = client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )
        save_file_path = f"audios/{language}.mp3"
        
        with open(save_file_path, "wb") as f:
            f.write(response.audio_content)

        return save_file_path
    except Exception as e:
        raise gr.Error(f"Error al guardar audio traducido: {str(e)}")


with gr.Blocks() as web:
    with gr.Row():
        gr.Markdown("""
            <h1 style='text-align: center;'>Traductor de voz con IA 💞</h1>
            <p style='text-align: center;'>Sube o graba un audio con tu voz y... ¡Voilà, harás magia! 🪄✨</p>
        """)

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(sources=["microphone", "upload"], type="filepath", label="Sube un archivo de audio o usa el micrófono")
        with gr.Column():
            select_languages = gr.CheckboxGroup(
                choices=[
                    "Inglés", "Italiano", "Francés", "Portugués", "Alemán", "Árabe", "Catalán", "Coreano", "Ruso", "Español"
                ],
                label="Elige uno o varios idiomas a los que traducir 🥰"
            )

    with gr.Row():
        with gr.Column():
            translate_button = gr.Button("Traducir")

    with gr.Row():
        audio_outputs = [
            gr.Audio(visible=False),
            gr.Audio(visible=False),
            gr.Audio(visible=False),
            gr.Audio(visible=False),
            gr.Audio(visible=False),
            gr.Audio(visible=False),
            gr.Audio(visible=False),
            gr.Audio(visible=False),
            gr.Audio(visible=False),
            gr.Audio(visible=False)
        ]

    translate_button.click(
        fn=translator,
        inputs=[audio_input, select_languages],
        outputs=audio_outputs
    )

    with gr.Row():
        feedback = gr.Textbox(label="¿Quieres mandarnos tu Feedback? 🤩", placeholder="Escríbelo aquí...")
        submit_button = gr.Button("Enviar")
        feedback_response = gr.Textbox(label="Respuesta", visible=False)

        def handle_feedback(feedback_text):
            with open("feedback.txt", "a") as f:
                f.write(feedback_text + "\n")
            return gr.update(value="¡Muchas gracias por tu feedback! 🔥😎", visible=True)

        submit_button.click(fn=handle_feedback, inputs=[feedback], outputs=[feedback_response])

    web.launch()