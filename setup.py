import subprocess
import sys

# List of required packages
packages = [
    "opencv-python",
    "numpy",
    "torch",
    "torchvision",
    "gTTS",
    "pyserial"
]

print("🔧 Installing packages for L3xBOT...")

for package in packages:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} installed.")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}")

print("🎉 Setup complete.")