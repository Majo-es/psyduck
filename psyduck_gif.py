from PIL import Image

image_path_list = ['psyduck1.jpeg', 'psyduck2.jpeg', 'psyduck3.jpeg']

image_list = [Image.open(file) for file in image_path_list]

image_list[0].save(
            #'animation.gif',
            #save_all=True,
           # append_images=image_list[1:], 
           # duration=800, 
           # loop=4)
