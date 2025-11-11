# 🏙️ ComfyUI-QwenEdit-Urbanism-by-UGA
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A collection of **ComfyUI workflows and custom nodes** designed for **urbanism**, **architecture**, and **geospatial visualization**, developed by **Urban Geo Analytics (UGA)**.  
This repository focuses on fully **local and offline** pipelines powered by **Qwen Image Edit (GGUF)** and complementary custom nodes for practical urban applications.

---

## 🧠 Qwen Image Edit for Urbanism

This module integrates **Qwen-Image-Edit (GGUF format)** into ComfyUI for fully **local** and **offline** visual editing.  
It performs **semantic image modifications** using natural-language prompts, ideal for **urban design**, **streetscape transformation**, and **architectural visualization**.

The workflow adapts automatically to the input image ratio and includes adjustable parameters such as **CFG**, **denoise**, and **steps**, providing precise control and reproducible results even on **mid-range GPUs (6–8 GB VRAM)**.

Example prompts:
- “Add trees and benches along the sidewalk”  
- “Change the building to have shops on the ground floor”  
- “Turn this street into a pedestrian plaza”  

---

## 🎲 Random Image Selector Node

Includes a lightweight custom node — **RandomImageSelector** — that randomly selects one image from multiple inputs.  
Useful for dataset exploration, visual sampling, or random input selection in multi-image workflows.

---

## ⚙️ Installation

1. Go to your ComfyUI `custom_nodes` directory:
