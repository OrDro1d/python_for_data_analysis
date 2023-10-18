import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

url = "https://upload.wikimedia.org/wikipedia/ru/thumb/2/24/Lenna.png/330px-Lenna.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img = img.resize((128, 128))
plt.imshow(img)
plt.show()
