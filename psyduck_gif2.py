from PIL import Image
import glob

frames = []
imgs = glob.glob("*.jpeg")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

frames[0].save('psyduck.gif', format='GIF',
              append_images=frames[1:],
              save_all=True,
              duration=300, loop=0)
