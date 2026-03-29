import os
from PyPDF2 import PdfReader
from gtts import gTTS


def generate_story_audio(
        pdf_path="content/stories/tale.pdf",
        output_folder="content/voice",
        output_filename="tale.mp3",
        language='en'
):
    output_path = os.path.join(output_folder, output_filename)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        reader = PdfReader(pdf_path)
        full_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text + " "

        if not full_text.strip():
            return False, "Empty PDF"

        tts = gTTS(text=full_text, lang=language)
        tts.save(output_path)

        return True, output_path

    except Exception as e:
        return False, str(e)
