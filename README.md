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
