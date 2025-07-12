import requests

def get_raw_food_nutrition(query="banana"):
    api_key = "6J42vMz257ndOAi5waghwfo81uyyWIzQm1k0HOCk"
    url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    params = {
        "query": query,
        "dataType": "Foundation", # "Survey (FNDDS)",  # Can also try "Foundation"
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        items = response.json().get("foods", [])
        if items:
            return items[0]  # Return first matched raw food
    return None

def extract_nutrients(nutrients, nutrient_ids=[1003, 1008]):
    desired_nutrients = []
    for n in nutrients:
        if n["nutrientId"] in nutrient_ids:
            desired_nutrients.append({
                "name": n["nutrientName"],
                "value": n["value"],
                "unit": n["unitName"]
            })
    return desired_nutrients