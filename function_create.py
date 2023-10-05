import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt


def draw_side(x_, y_):
    plt.plot(x_, y_, 'b-')
    # plt.fill_between(x_, y_, color='pink')
    #plt.pause(0.001)
    #plt.show(block=False)



num_sides_ = 12
radius_ = 2
angle_offset_ = np.pi / num_sides_
plt.figure(figsize=(6, 6))
lim1_ = -10
lim2_ = 10
plt.xlim(lim1_, lim2_)
plt.ylim(lim1_, lim2_)


def back(num_sides, radius, angle_offset, center, lim1, lim2):
    angle = np.linspace(0, 2 * np.pi, num_sides + 1)
    while lim1 <= (center - center / 2):
        x = radius * np.cos(angle - angle_offset) - lim2
        size1_ = abs(x[1] - x[2] - (x[11] - x[10]))
        size2_ = abs(lim1 - x[0])
        size3_ = abs((x[3] - x[4]) / 2)

        return size1_, size2_, size3_, x[5]


def return_r(num_sides, radius, angle_offset, center, lim1, lim2):
    angle = np.linspace(0, 2 * np.pi, num_sides + 1)
    while lim1 <= (center - center / 2):
        x = radius * np.cos(angle - angle_offset) - lim2
        r_ = sqrt(radius * radius - (x[3] - x[4]) / 2 * (x[3] - x[4]) / 2)
        return r_


def create_lateral_side(num_sides, radius, angle_offset, center, lim1, lim2):
    angle = np.linspace(0, 2 * np.pi, num_sides + 1)
    while lim1 <= (center - center / 2):
        x = radius * np.cos(angle - angle_offset) - lim2
        y = radius * np.sin(angle - angle_offset) + center
        for i in range(num_sides):
            draw_side([x[i], x[i + 1]], [y[i], y[i + 1]])
            # print(str(i) + " x1, y1 =" + str([x[i], y[i]]) + " x2, y2 =" + str([x[i + 1], y[i + 1]]))
        draw_side([x[3], x[3]], [y[3], y[3] + (x[3] - x[4])])
        draw_side([x[4], x[4]], [y[3], y[3] + (x[3] - x[4])])
        draw_side([x[4], x[3]], [y[3] + (x[3] - x[4]), y[3] + (x[3] - x[4])])

        draw_side([x[9], x[9]], [y[9], y[9] - (x[3] - x[4])])
        draw_side([x[10], x[10]], [y[9], y[9] - (x[3] - x[4])])
        draw_side([x[9], x[10]], [y[9] - (x[3] - x[4]), y[9] - (x[3] - x[4])])

        draw_side([x[1], x[1] + (x[11] - x[10])], [y[1], y[1] + (y[11] - y[10])])
        draw_side([x[2], x[2] + (x[11] - x[10])], [y[2], y[2] + (y[11] - y[10])])
        draw_side([x[1] + (x[11] - x[10]), x[2] + (x[11] - x[10])], [y[1] + (y[11] - y[10]), y[2] + (y[11] - y[10])])

        draw_side([x[5], x[5] - (x[9] - x[8])], [y[5], y[5] - (y[9] - y[8])])
        draw_side([x[6], x[6] - (x[9] - x[8])], [y[6], y[6] - (y[9] - y[8])])
        draw_side([x[5] - (x[9] - x[8]), x[6] - (x[9] - x[8])], [y[5] - (y[9] - y[8]), y[6] - (y[9] - y[8])])

        draw_side([x[7], x[7] - (x[11] - x[10])], [y[7], y[7] - (y[11] - y[10])])
        draw_side([x[8], x[8] - (x[11] - x[10])], [y[8], y[8] - (y[11] - y[10])])
        draw_side([x[7] - (x[11] - x[10]), x[8] - (x[11] - x[10])], [y[7] - (y[11] - y[10]), y[8] - (y[11] - y[10])])

        draw_side([x[0], x[0] + (x[9] - x[8])], [y[0], y[0] + (y[9] - y[8])])
        draw_side([x[11], x[11] + (x[9] - x[8])], [y[11], y[11] + (y[9] - y[8])])
        draw_side([x[0] + (x[9] - x[8]), x[11] + (x[9] - x[8])], [y[0] + (y[9] - y[8]), y[11] + (y[9] - y[8])])
        center += - sqrt(radius_ * radius_ - (x[3] - x[4]) / 2 * (x[3] - x[4]) / 2) - (x[3] - x[4]) - sqrt(
            radius_ * radius_ - (x[3] - x[4]) / 2 * (x[3] - x[4]) / 2)


def create_the_main_chain(num_sides, radius, angle_offset, center, lim1, lim2):
    center += size3
    angle = np.linspace(0, 2 * np.pi, num_sides + 1)
    while lim1 <= (center - center / 2):
        x = radius * np.cos(angle - angle_offset) - lim2
        y = radius * np.sin(angle - angle_offset) + center
        for i in range(num_sides):
            draw_side([x[i], x[i + 1]], [y[i], y[i + 1]])
            # print(str(i) + " x1, y1 =" + str([x[i], y[i]]) + " x2, y2 =" + str([x[i + 1], y[i + 1]]))
        draw_side([x[3], x[3]], [y[3], y[3] + (x[3] - x[4])])
        draw_side([x[4], x[4]], [y[3], y[3] + (x[3] - x[4])])
        draw_side([x[4], x[3]], [y[3] + (x[3] - x[4]), y[3] + (x[3] - x[4])])

        #draw_side([x[9], x[9]], [y[9], y[9] - (x[3] - x[4])])
        #draw_side([x[10], x[10]], [y[9], y[9] - (x[3] - x[4])])
        #draw_side([x[9], x[10]], [y[9] - (x[3] - x[4]), y[9] - (x[3] - x[4])])

        draw_side([x[1], x[1] + (x[11] - x[10])], [y[1], y[1] + (y[11] - y[10])])
        draw_side([x[2], x[2] + (x[11] - x[10])], [y[2], y[2] + (y[11] - y[10])])
        draw_side([x[1] + (x[11] - x[10]), x[2] + (x[11] - x[10])], [y[1] + (y[11] - y[10]), y[2] + (y[11] - y[10])])

        draw_side([x[0], x[0] + (x[9] - x[8])], [y[0], y[0] + (y[9] - y[8])])
        draw_side([x[11], x[11] + (x[9] - x[8])], [y[11], y[11] + (y[9] - y[8])])
        draw_side([x[0] + (x[9] - x[8]), x[11] + (x[9] - x[8])], [y[0] + (y[9] - y[8]), y[11] + (y[9] - y[8])])
        center += - sqrt(radius_ * radius_ - (x[3] - x[4]) / 2 * (x[3] - x[4]) / 2) - (x[3] - x[4]) - sqrt(
            radius_ * radius_ - (x[3] - x[4]) / 2 * (x[3] - x[4]) / 2)


size1, size2, size3, edge = back(num_sides_, radius_, angle_offset_,
                                 lim2_ - return_r(num_sides_, radius_, angle_offset_, lim2_, lim1_, lim2_), lim1_,
                                 lim2_)
_ = 0
cal = 0
edge = abs(edge)
while edge >= lim1_:
    if _ == 0:
        create_lateral_side(num_sides_, radius_, angle_offset_,
                            lim2_ - return_r(num_sides_, radius_, angle_offset_, lim2_, lim1_, lim2_), lim1_, lim2_)
        _ += 1
        edge = lim2_
        # print(edge)
    elif _ % 2 == 1:
        cal = cal - size1 - return_r(num_sides_, radius_, angle_offset_, lim2_, lim1_, lim2_) - return_r(num_sides_,
                                                                                                         radius_,
                                                                                                         angle_offset_,
                                                                                                         lim2_, lim1_,
                                                                                                         lim2_)
        create_the_main_chain(num_sides_, radius_, angle_offset_, lim2_, lim1_, lim2_ + cal)
        edge = lim2_ + cal
        # print(edge)
        _ += 1
    else:
        cal = cal - size1 - return_r(num_sides_, radius_, angle_offset_, lim2_, lim1_, lim2_) - return_r(num_sides_,
                                                                                                         radius_,
                                                                                                         angle_offset_,
                                                                                                         lim2_, lim1_,
                                                                                                         lim2_)
        create_the_main_chain(num_sides_, radius_, angle_offset_,
                              lim2_ - size3 - return_r(num_sides_, radius_, angle_offset_, lim2_, lim1_, lim2_), lim1_,
                              lim2_ + cal)
        edge = lim2_ + cal
        # print(edge)
        _ += 1

plt.show()
