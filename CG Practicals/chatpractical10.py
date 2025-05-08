import matplotlib.pyplot as plt

x_min = 50
y_min = 50
x_max = 250
y_max = 200

polygon = [(100, 100), (200, 300), (300, 150), (150, 50), (50, 150)]

def cohen_sutherland_clip(polygon, x_min, y_min, x_max, y_max):
    code_inside = 0
    code_left = 1
    code_right = 2
    code_bottom = 4
    code_top = 8

    def compute_outcode(x, y):
        code = code_inside

        if x < x_min:
            code |= code_left
        elif x > x_max:
            code |= code_right

        if y < y_min:
            code |= code_bottom
        elif y > y_max:
            code |= code_top

        return code

    clipped_polygon = []

    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]

        outcode1 = compute_outcode(x1, y1)
        outcode2 = compute_outcode(x2, y2)

        while True:
            if not (outcode1 | outcode2):
                clipped_polygon.append((x1, y1))
                clipped_polygon.append((x2, y2))
                break
            elif outcode1 & outcode2:
                break
            else:
                x = 0
                y = 0
                outcode = outcode1 or outcode2

                if outcode & code_top:
                    x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                    y = y_max
                elif outcode & code_bottom:
                    x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                    y = y_min
                elif outcode & code_right:
                    y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                    x = x_max
                elif outcode & code_left:
                    y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                    x = x_min

                if outcode == outcode1:
                    x1, y1 = x, y
                    outcode1 = compute_outcode(x1, y1)
                else:
                    x2, y2 = x, y
                    outcode2 = compute_outcode(x2, y2)

    return clipped_polygon

clipped_polygon = cohen_sutherland_clip(polygon, x_min, y_min, x_max, y_max)

x, y = zip(*polygon)
plt.plot(x, y, 'b-', label='Original Polygon')

x, y = zip(*clipped_polygon)
plt.plot(x, y, 'r-', label='Clipped Polygon')

plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], 'k--', label='Clipping Region')

plt.xlim(0, 350)
plt.ylim(0, 350)
plt.show()