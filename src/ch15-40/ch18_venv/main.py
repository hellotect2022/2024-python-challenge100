import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('hirst_painting.jpg', 10)
color_list = []
for color in colors:
    color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
print(color_list)