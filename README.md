# 🏙️ ComfyUI-QwenEdit-Urbanism-by-UGA
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A collection of **ComfyUI workflows and custom nodes** designed for **urbanism** and **architecture**, developed by **Urban Geo Analytics (UGA)**.  
This repository focuses on pipelines powered by **Qwen Image Edit (GGUF)** and complementary custom nodes for practical urban applications.

---

## 🧠 Qwen Image Edit for Urbanism

v1.0 
This first version of Qwen Image Edit for Urbanism uses the base Qwen-Image-Edit-2509 model in GGUF format, designed for fully local and offline visual editing. It operates on a single input image, with output size automatically adapted to the original image ratio. The workflow is lightweight and stable, ideal for quick urban or architectural edits on mid-range GPUs.

v1.1
This version introduces advanced sampling and multi-image editing capabilities.
[v1.1 tutorial on Urban Geo Analytics](https://urbangeoanalytics.com/local-ai-image-editing-for-urbanism-v1-1/)


---

## 🎲 Random Image Selector Node

Includes a lightweight custom node — **RandomImageSelector** — that randomly selects one image from multiple inputs.  
Useful for dataset exploration, visual sampling, or random input selection in multi-image workflows.

---

## ⚙️ Installation

1. Go to your ComfyUI `custom_nodes` directory:
