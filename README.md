

**L3xBOT: Empowering Vision Through Technology**

*L3xBOT* is an assistive technology tool designed to empower individuals who are blind or have low vision. Developed by Naomi McQuade, L3xBOT leverages computer vision, AI-driven guidance, and haptic feedback to make perception more accessible.

#### ✨ Features
- 🏷 **Object Recognition** — Real-time detection and identification using YOLOv3 and OpenCV.
​🔬 The Logic of Perception
​Edge-Aware Synthesis: Uses Canny filtering to resolve boundary-bleed for high myopia (-10.00 diopters).
​Motion-Parallax Depth: Since I am monocular, the system is being tuned to calculate depth-from-motion, mirroring how the human brain adapts to one-eye vision.
​Semantic Contrast: Leveraging CLAHE (Contrast Limited Adaptive Histogram Equalization) to reveal details in flat or high-glare lighting (like snow).
- 🔊 **Speech Output** — Converts visual information into audio using Google Text-to-Speech (gTTS).
- 📳 **Haptic Feedback** — Vibrates to signal nearby obstacles, assisting navigation through touch.
- 🌍 **Accessible UX** — Built with simplicity and inclusivity at its core, ensuring ease of use for all.

#### ⚙️ Tech Stack
- **Python** – AI logic and core functionality  
- **OpenCV** – Image capture and processing  
- **YOLOv3** – Deep learning-based object detection  
- **Google TTS** – Voice response generation  
- **Arduino / Raspberry Pi** – Hardware interface and haptics

#### 🚀 Getting Started
```bash
git clone https://github.com/NaomiMcQuade/L3xbot.git
cd L3xbot
``