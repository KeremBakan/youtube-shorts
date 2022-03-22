import PIL.Image
import pilgram

img = PIL.Image.open('../images/baloon.jpg')

pilgram.lofi(img).save('../images/baloon-filtered.jpg')
pilgram.toaster(img).save('../images/baloon-filtered2.jpg')
pilgram.moon(img).save('../images/ballon-filtered3.jpg')