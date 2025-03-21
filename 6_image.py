"""
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
"""
import urllib.request
from PIL import Image 
import urllib
from fractions import Fraction

def get_ratio(url):

    try: 
        response = urllib.request.urlopen(url)
        img_r = Image.open(response)
        w, h = img_r.size

        f_ratio = str(Fraction(w, h))

        list_ratio = f_ratio.split("/")

        print(f"El ratio de la imagen es: '{list_ratio[0]}:{list_ratio[1]}'")
    except Exception:
        print("The provided URL is invalid!")

if __name__ == "__main__":

    img = "https://wallpapers.com/images/hd/blue-aesthetic-moon-df8850p673zj275y.jpg"
    get_ratio(img)

    




