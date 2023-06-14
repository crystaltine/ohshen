from PIL import Image, ImageDraw
import uuid4
  
def draw_gif(images: list, save_path: str):
    images[0].save(
        f'{save_path}.gif',
        save_all = True, 
        append_images = images[1:], 
        optimize = True, 
    )