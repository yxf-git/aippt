import random

img_list = ['test_img/图3.jpg', 'test_img/图4.jpg', 'test_img/图5.jpg', 'test_img/图1.png', 'test_img/图2.png', 'test_img/图3.png']

# 使用random.sample函数随机抽样三个元素
sampled_images = random.sample(img_list, 3)

print(sampled_images)