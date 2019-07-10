# pip install pyfiglet
# source https://www.devdungeon.com/content/create-ascii-art-text-banners-python
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hello!!")
print(ascii_banner)
from pyfiglet import Figlet

custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Hello!!'))

