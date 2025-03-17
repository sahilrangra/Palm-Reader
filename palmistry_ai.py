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

image_path = "hand1.jpeg"
horoscope = generate_horoscope(image_path)

print("\nGenerated Horoscope:\n", horoscope)
