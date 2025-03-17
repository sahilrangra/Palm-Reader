# 📌 Ollama LLaVA-based Palmistry AI

This project uses **Ollama's LLaVA (Large Language and Vision Assistant)** model to analyze palm images based on **Hindu palmistry** and generate horoscopes. 🖐🔮

## 📜 Features
- 🖼 **Image-based analysis** using Hindu palmistry principles
- 🔍 **LLaVA model** for vision-language understanding
- 📝 **Generates horoscopes** based on uploaded hand images
- 🚀 **Easy to use** with Python and Ollama

---
## 🛠 Installation & Setup

### 1️⃣ Install Ollama
First, install Ollama from the official site:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2️⃣ Install Required Python Libraries
Ensure you have Python installed, then install dependencies:
```bash
pip install ollama
```

### 3️⃣ Pull the LLaVA Model
Download the LLaVA model for image-based AI processing:
```bash
ollama pull llava
```

---
## 🚀 Usage

### Run the Script
Save your hand image as **`hand.jpeg`** and execute the script:
```bash
python palmistry_ai.py
```

### 🖥 Python Script (`palmistry_ai.py`)
```python
import base64
import ollama

def encode_image(image_path):
    """ Convert image to base64 format for AI processing """
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def generate_horoscope(image_path):
    """ Send encoded image to Ollama for palmistry-based horoscope """
    image_base64 = encode_image(image_path)

    response = ollama.chat(
        model="llava",
        messages=[
            {"role": "user", "content": "Analyze the following hand image based on Hindu palmistry and provide a horoscope."},
            {"role": "user", "images": [image_base64]}
        ],
    )
    
    return response['message']['content']

image_path = "hand.jpeg"
horoscope = generate_horoscope(image_path)

print("\nGenerated Horoscope:\n", horoscope)
```

---
## 🔥 Example Output
```bash
Generated Horoscope:
You have a strong and well-defined fate line, which suggests a determined and ambitious personality. Your heart line indicates deep emotional connections...
```

---
## 🛠 Troubleshooting
- **Error: Model not found?** → Run `ollama pull llava` to download the model.
- **Invalid Image Format?** → Ensure the image is **JPEG** or **PNG**.
- **API Issues?** → Check if the **Ollama service is running** (`ollama serve`).

---
## 📜 License
This project is licensed under the **MIT License**.

---
## 🤝 Contributing
Pull requests and suggestions are welcome! Fork the repo and contribute. 😊

---
## 🔗 References
- [Ollama Official Documentation](https://ollama.com)
- [LLaVA Model Overview](https://github.com/haotian-liu/LLaVA)

