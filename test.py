rev = '1zazYBQ8F-MY1cX6s2ncEX-eoHVoFP0s5stbpChUM2H5-DSFj8i6JdwL4oZ44onkkaM_UlKlAAAABg'

print(rev[::-1])

# remove noise from ./hush/test_noise.wav using scipy
# from scipy.io import wavfile
# from scipy.signal import wiener
# rate, data = wavfile.read('./hush/test_noise.wav')
# data = wiener(data)
# wavfile.write('./hush/test_noise_clean.wav', rate, data)

# # change ./hush/flag.mp4a to ./hush/flag.wav using scipy
# from scipy.io import wavfile
# rate, data = wavfile.read('./hush/flag.m4a')
# wavfile.write('./hush/flag.wav', rate, data)
#
#
# # print a list of all values in the array that are not 0
# # import numpy as np
# # a = np.array([1,2,0,0,4,0])
#
# print(a[a != 0])

# write a function that takes image granny/timber_wolf.jpg and adds granny/granny_1.jpeg over it as a mask
import cv2
import numpy as np

# def add_masK(img, mask):
#     img = cv2.imread(img)
#     mask = cv2.imread(mask)
#     mask = cv2.resize(mask, (img.shape[1], img.shape[0]))
#     mask = mask[:, :, 1]
#     # mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
#     # mask = np.stack((mask,)*3, axis=-1)
#     # mask = mask / 255
#     img = cv2.bitwise_and(img,img, mask=mask)
#
#     cv2.imwrite('./granny/granny_1_masked.jpg', img)
#
#
# add_masK('./granny/timber_wolf.jpg', './granny/granny_1.jpeg')