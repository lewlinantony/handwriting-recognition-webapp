from flask import Flask, render_template, request, jsonify
import base64
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import os

app = Flask(__name__)

# Load the model and processor
processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')  # Route for the About page
def about():
    return render_template('about.html')

def fill_transparent_with_white(img):
    # If the image has an alpha fhannel (transparency), fill transparent areas with white
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        # Create a new image filled with white
        new_img = Image.new('RGB', img.size, (255, 255, 255))

        # Composite the original image over the white image
        new_img.paste(img, mask=img.split()[3])  # Use the alpha channel as the mask
        return new_img
    else:
        # Image doesn't have transparency, no action needed
        print(f"No transparent areas found in path. No action performed.")

@app.route('/recognize', methods=['POST'])
def recognize():
    image_data = request.json['image']
    # Remove the data:image/png;base64, part
    header, encoded = image_data.split(",", 1)
    image_data = base64.b64decode(encoded)

    # Specify the directory where you want to save the image. Ensure this directory exists and is writable.
    save_directory = "/Users/lewlinantony/Desktop/Hand_Writing_WA/"

    # Save the decoded image to a file
    image_path = os.path.join(save_directory, "debug_image_1.jpg")
    with open(image_path, "wb") as img_file:
        img_file.write(image_data)

    # Open, potentially convert, and recognize the image
    image = Image.open(image_path)
    image = fill_transparent_with_white(image)
    
    # Save the modified image
    image_path = os.path.join(save_directory, "debug_image_2.jpg")
    with open(image_path, "wb") as img_file:
        image.save(img_file)

    # Ensure the image is in RGB format for processing
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Recognize text using TrOCR
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    generated_text = generated_text.split()[0] if generated_text.split()[0][-1]!='.' else generated_text.split()[0][:-1]
    print(generated_text)
    return jsonify({'text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
