# 🏙️ ComfyUI-QwenEdit-Urbanism-by-UGA
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ComfyUI](https://img.shields.io/badge/Compatible%20with-ComfyUI-blue)](https://github.com/comfyanonymous/ComfyUI)
[![Urban Geo Analytics](https://img.shields.io/badge/By-Urban%20Geo%20Analytics-orange)](https://urbangeoanalytics.com)

**Qwen Image Edit for Urbanism** brings localized, text-driven image editing to urban and architectural workflows using the open-source **Qwen-Image-Edit** model in **GGUF format**. All processing runs fully offline — no API, no cloud — making it ideal for architects, planners, and researchers who need privacy, reproducibility, and full visual control.

---

## 🧠 1. Qwen Image Edit for Urbanism : Comfy Pipelines  

| Version | Description | Tutorial |
|----------|--------------|-----------|
| **v1.0** | Basic Qwen Image Edit workflow for single-image editing. Adapts automatically to input ratio and size. | [v1.0 Tutorial →](https://urbangeoanalytics.com/local-ai-image-editing-urbanism-comfyui-qwen-gguf/) |
| **v1.1** | Adds multi-image editing and advanced sampling capabilities for complex scenes. | [v1.1 Tutorial →](https://urbangeoanalytics.com/local-ai-image-editing-for-urbanism-v1-1/) |

### Download 
Right-click any link above and choose **“Save link as…”** to download the workflow file. Then, open **ComfyUI → File → Load → Workflow**, and select the downloaded `.json` file to load it into your workspace.
| Version | Workflow File |
|---|---|
| v1.0 | [Download Qwen-Edit-UGA-v1.0.json](https://github.com/perezjoan/ComfyUI-QwenEdit-Urbanism-by-UGA/blob/main/Qwen-Edit-UGA-v1.0.json) |
| v1.1 | [Download Gwen-Edit-UGA-v1.1.json](https://github.com/perezjoan/ComfyUI-QwenEdit-Urbanism-by-UGA/blob/main/Qwen-Edit-UGA-v1.1.json) |

---

## ⚙️ 2. Custom Nodes 

Custom nodes developed for urban image processing and automation within ComfyUI.

| Node Name | Function | Description |
|------------|-----------|--------------|
| 🎲 **Random Image Selector** | Randomly selects one image among several inputs each run. | For stochastic rendering. |
| 🔁 **Sequential Image Loader** | Loads each connected image in order across executions. | For batch processing. |

## 🧩 Installation

### 🖥️ Option 1 — ComfyUI Manager (Recommended)
1. Open **ComfyUI → Manager → Custom Nodes → Install from Git URL.**
2. Paste the following: https://github.com/perezjoan/ComfyUI-QwenEdit-Urbanism-by-UGA
3. Click **Install.**
4. Restart **ComfyUI.**

### 🧰 Option 2 — Manual Install

1. Navigate to your ComfyUI directory:
ComfyUI/custom_nodes/
2. Clone or download this repository:
git clone https://github.com/perezjoan/ComfyUI-QwenEdit-Urbanism-by-UGA.git
3. Restart **ComfyUI.**

The nodes will appear under **image/sequence** and **image/random** categories.

---

## 🧩 Credits
Developed by **Urban Geo Analytics (UGA)**  
Based on open-source work by **QuantStack**, **ComfyUI**, and **Qwen Image Edit** contributors.

---

## 🪪 License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

