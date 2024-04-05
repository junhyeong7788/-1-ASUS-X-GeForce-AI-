import openai
import urllib

API_KEY = "API-KEY"
client = openai.OpenAI(api_key=API_KEY)

response = client.images.generate( # 생성 
    model = "dall-e-3", 
    prompt = """Image prompt 
Title: "ASUS ROG Zephyrus" is a laptop and should emphasize a slim, rounded design.
Image Style: Make the aurora smooth through the connection between warm and cold colors, and use a wide background to show product details. On the floor, Vertical Line and Horizontal Line are intersected to express a sense of distance. 
Laptop Image: The top and bottom ends of the laptop are rounded. Emphasize the slim design with lighting focused on the product side. The rear side of the laptop product should be visible, and the laptop should express the texture of high-quality aluminum. The logo of the ROG laptop should be displayed on the back of the laptop. The laptop design should be emphasized by drawing a silver diagonal line from the bottom left to the right of the top. Open the laptop slightly and place it in the center. Emphasize product realism using the Eclipse Gray from "ASUS ROG Zephyrus".
Priority: 1. The aurora in the background should have a vast and mysterious sensibility, and the image should be projected clearer through the screen of the laptop. 2. At the bottom of the laptop, the text "NVIDIA-GEFORCE" should be written clearly and accurately with ASUS Zephyrus text and advertised phrases. 3. The rear side of the product should be visible.""",
    quality = "hd",
    n=1, 
)

image_url = response.data[0].url
urllib.request.urlretrieve(image_url, "image.jpg") 
print(image_url)
 