from transformers import pipeline
from PIL import Image
import io
from src.app.services.get_raw_food_nutrition import extract_nutrients, get_raw_food_nutrition

classifier = pipeline("image-classification", model="google/vit-base-patch32-384")

async def classify_image(upload_file):
    contents = await upload_file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    results = classifier(image)
    data = get_raw_food_nutrition(results[0]['label'])
    nutrient = extract_nutrients(data['foodNutrients'])
    return nutrient  # You can format it more if needed