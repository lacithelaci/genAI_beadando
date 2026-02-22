# AI Cinematic Short Film Generator

## Project Description

This project implements a multimodal generative AI pipeline that produces a cinematic short film using diffusion-based image generation, iterative frame transformation, automatic image captioning, and temporal semantic analysis.

The system combines generative modeling and analytical components into a unified workflow suitable for academic demonstration of multimodal AI systems.

---

## System Architecture

The pipeline consists of the following stages:

1. Text-to-Image generation using Stable Diffusion
2. Iterative Image-to-Image refinement for temporal continuity
3. Scene progression via structured prompt evolution
4. Video rendering using OpenCV
5. Frame-level caption generation using BLIP
6. Temporal semantic analysis using statistical methods

---

## Models Used

Stable Diffusion v1.5  
Source: runwayml/stable-diffusion-v1-5

BLIP Image Captioning (Base)  
Source: Salesforce/blip-image-captioning-base

Both models are accessed via the Hugging Face ecosystem.

---

## Functional Components

### 1. Image Generation
Initial frame creation using text-to-image diffusion.

### 2. Temporal Animation
Frame-to-frame transformation using image-to-image diffusion with controlled strength parameter.

### 3. Scene Structuring
Prompt evolution across frames:
- Intro
- Build-up
- Close-up
- Fade-out

### 4. Video Rendering
Frame stitching into a cinematic video using adjustable FPS.

### 5. Caption Generation
Automatic caption generation for each frame using BLIP.

### 6. Temporal Content Analysis
- Word frequency analysis
- Caption length tracking
- Keyword presence monitoring
- Semantic drift observation

---

## Installation

Clone the repository:


git clone https://github.com/lacithelaci/ai-cinematic-shortfilm.git

cd ai-cinematic-shortfilm


Install dependencies:


pip install -r requirements.txt


---

## Usage

Run the Jupyter Notebook locally or in Google Colab and execute the cells sequentially.

---

## Hardware Requirements

- NVIDIA GPU recommended
- CUDA-compatible environment
- Minimum 12GB VRAM recommended for extended video generation

---

## Academic Scope

This project demonstrates:

- Generative diffusion models
- Multimodal AI systems
- Temporal consistency modeling
- Automated semantic analysis
- AI-driven visual storytelling

---

## Notes

Generation time depends on frame count and GPU performance.
Public pretrained models from Hugging Face are used.
The system is intended for educational and research purposes.
