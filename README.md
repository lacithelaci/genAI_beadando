# AI Storytelling Suite

**AI Storytelling Suite** is a modular, end-to-end generative AI platform that converts images into immersive stories and produces accompanying media (PDFs and audio). Built with Python, Streamlit, and state-of-the-art AI models, this project demonstrates a seamless pipeline from image input to fully narrated stories.

---

## Features

- **Image-to-Caption:** Automatically generates descriptive captions from uploaded images using BLIP.
- **Caption-to-Story:** Expands captions into rich, narrative stories with Groq's LLaMA-based models.
- **PDF Export:** Save generated stories as PDF for offline reading or sharing.
- **Text-to-Speech:** Convert PDFs into audio using Google TTS for accessible, hands-free storytelling.
- **Image Generation:** Create AI-generated images from text prompts using Stable Diffusion.
- **Streamlit Interface:** Interactive, user-friendly web UI for all modules with session state management.

---

## Technology Stack

- Python 3.11+
- [Streamlit](https://streamlit.io/) for interactive UI
- [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) for image captioning
- [Groq LLaMA](https://www.groq.com/) for story generation
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF handling
- [gTTS](https://pypi.org/project/gTTS/) for text-to-speech
- [Diffusers / Stable Diffusion](https://huggingface.co/docs/diffusers/index) for text-to-image generation
- PIL / Pillow for image handling

---

## Project Structure


├── generators/ # Core AI pipelines
│ ├── image_to_caption.py
│ ├── capture_to_story.py
│ ├── images_generator.py
│ └── text_to_speech.py
├── content/ # Output storage
│ ├── pictures/
│ ├── stories/
│ └── voice/
├── streamlit_apps/ # Streamlit interfaces
│ ├── image_generator_app.py
│ ├── image_to_story_app.py
│ └── pdf_to_audio_app.py
└── README.md


---

## Usage

1. Clone the repo:

```bash
git clone https://github.com/yourusername/ai-storytelling-suite.git
cd ai-storytelling-suite
Install dependencies:
pip install -r requirements.txt
Run any Streamlit app:
streamlit run streamlit_apps/image_to_story_app.py
Upload an image or PDF and explore the pipeline!
Notes
GPU is recommended for image generation and story generation for performance.
All outputs (images, PDFs, audio) are stored in content/.
Environment variables like API keys for Groq must be set in .env.
