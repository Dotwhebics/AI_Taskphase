import kociemba as kb
import cv2 as cv

# getting the cube faces and determination of top left and bottom right corner coordinates
# to be completed

# convert the face images to hsv
up_hsv = cv.cvtColor(up_face_img, cv.COLOR_BGR2HSV)
right_hsv = cv.cvtColor(right_face_img, cv.COLOR_BGR2HSV)
front_hsv = cv.cvtColor(front_face_img, cv.COLOR_BGR2HSV)
down_hsv = cv.cvtColor(down_face_img, cv.COLOR_BGR2HSV)
left_hsv = cv.cvtColor(left_face_img, cv.COLOR_BGR2HSV)
back_hsv = cv.cvtColor(back_face_img, cv.COLOR_BGR2HSV)

# extract HSV values of the center of each face
# up face
x_cord = (x_top_up + x_bottom_up)/2 
y_cord =  (y_top_up + y_bottom_up)/2
U_hue = up_hsv[x_cord, y_cord, 0]
U_saturation = up_hsv[x_cord, y_cord, 1]
U_value = up_hsv[x_cord, y_cord, 2]
# right face
x_cord = (x_top_right + x_bottom_right)/2 
y_cord =  (y_top_right + y_bottom_right)/2
R_hue = up_hsv[x_cord, y_cord, 0]
R_saturation = up_hsv[x_cord, y_cord, 1]
R_value = up_hsv[x_cord, y_cord, 2]
# front face
x_cord = (x_top_front + x_bottom_front)/2 
y_cord =  (y_top_front + y_bottom_front)/2
F_hue = up_hsv[x_cord, y_cord, 0]
F_saturation = up_hsv[x_cord, y_cord, 1]
F_value = up_hsv[x_cord, y_cord, 2]
# down face
x_cord = (x_top_down + x_bottom_down)/2 
y_cord =  (y_top_down + y_bottom_down)/2
D_hue = up_hsv[x_cord, y_cord, 0]
D_saturation = up_hsv[x_cord, y_cord, 1]
D_value = up_hsv[x_cord, y_cord, 2]
# left face
x_cord = (x_top_left + x_bottom_left)/2 
y_cord =  (y_top_left + y_bottom_left)/2
L_hue = up_hsv[x_cord, y_cord, 0]
L_saturation = up_hsv[x_cord, y_cord, 1]
L_value = up_hsv[x_cord, y_cord, 2]
# back face
x_cord = (x_top_back + x_bottom_back)/2 
y_cord =  (y_top_back + y_bottom_back)/2
B_hue = up_hsv[x_cord, y_cord, 0]
B_saturation = up_hsv[x_cord, y_cord, 1]
B_value = up_hsv[x_cord, y_cord, 2]

# assign colours to each face squares
# function to assign colours
def assign(hsv, face_list):     # while assigning range within + or - 30 of recrded is checked
    if hsv[0] > U_hue - 30 and hsv [0] < U_hue + 30:
        if hsv[1] >  U_saturation - 30 and hsv[1] < U_saturation + 30:
            if hsv[2] > U_value - 30 and hsv[2] < U_value + 30:
                face_list.append('U')
    if hsv[0] > R_hue - 30 and hsv [0] < R_hue + 30:
        if hsv[1] >  R_saturation - 30 and hsv[1] < R_saturation + 30:
            if hsv[2] > R_value - 30 and hsv[2] < R_value + 30:
                face_list.append('R')
    if hsv[0] > F_hue - 30 and hsv [0] < F_hue + 30:
        if hsv[1] >  F_saturation - 30 and hsv[1] < F_saturation + 30:
            if hsv[2] > F_value - 30 and hsv[2] < F_value + 30:
                face_list.append('F')
    if hsv[0] > D_hue - 30 and hsv [0] < D_hue + 30:
        if hsv[1] >  D_saturation - 30 and hsv[1] < D_saturation + 30:
            if hsv[2] > D_value - 30 and hsv[2] < D_value + 30:
                face_list.append('D')
    if hsv[0] > L_hue - 30 and hsv [0] < L_hue + 30:
        if hsv[1] >  L_saturation - 30 and hsv[1] < L_saturation + 30:
            if hsv[2] > L_value - 30 and hsv[2] < L_value + 30:
                face_list.append('L')
    else:
        face_list.append('B')

# up face
up_list = []
x_cord = (x_bottom_up - x_top_up)/6 + x_top_up  # top left 
y_cord = (y_bottom_up - y_top_up)/6 + y_top_up
hue = up_hsv[x_cord, y_cord, 0]
saturation = up_hsv[x_cord, y_cord, 1]
value = up_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], up_list)
x_cord = (x_bottom_up - x_top_up)/6 * 3 + x_top_up  # top middle 
y_cord = (y_bottom_up - y_top_up)/6 + y_top_up
hue = up_hsv[x_cord, y_cord, 0]
saturation = up_hsv[x_cord, y_cord, 1]
value = up_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], up_list)
x_cord = (x_bottom_up - x_top_up)/6 * 5 + x_top_up  # top right
y_cord = (y_bottom_up - y_top_up)/6 + y_top_up
hue = up_hsv[x_cord, y_cord, 0]
saturation = up_hsv[x_cord, y_cord, 1]
value = up_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], up_list)
x_cord = (x_bottom_up - x_top_up)/6 + x_top_up  # middle left
y_cord = (y_bottom_up - y_top_up)/6 * 3 + y_top_up 
hue = up_hsv[x_cord, y_cord, 0]
saturation = up_hsv[x_cord, y_cord, 1]
value = up_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], up_list)
x_cord = (x_bottom_up - x_top_up)/6 * 3 + x_top_up  # center
y_cord = (y_bottom_up - y_top_up)/6 * 3 + y_top_up
hue = up_hsv[x_cord, y_cord, 0]
saturation = up_hsv[x_cord, y_cord, 1]
value = up_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], up_list)
x_cord = (x_bottom_up - x_top_up)/6 * 5 + x_top_up  # middle right
y_cord = (y_bottom_up - y_top_up)/6 * 3 + y_top_up
hue = up_hsv[x_cord, y_cord, 0]
saturation = up_hsv[x_cord, y_cord, 1]
value = up_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], up_list)
x_cord = (x_bottom_up - x_top_up)/6 + x_top_up  # bottom left
y_cord = (y_bottom_up - y_top_up)/6 * 5 + y_top_up
hue = up_hsv[x_cord, y_cord, 0]
saturation = up_hsv[x_cord, y_cord, 1]
value = up_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], up_list)
x_cord = (x_bottom_up - x_top_up)/6 * 3 + x_top_up  # bottom middle
y_cord = (y_bottom_up - y_top_up)/6 * 5 + y_top_up
hue = up_hsv[x_cord, y_cord, 0]
saturation = up_hsv[x_cord, y_cord, 1]
value = up_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], up_list)
x_cord = (x_bottom_up - x_top_up)/6 * 5 + x_top_up  # bottom right
y_cord = (y_bottom_up - y_top_up)/6 * 5 + y_top_up
hue = up_hsv[x_cord, y_cord, 0]
saturation = up_hsv[x_cord, y_cord, 1]
value = up_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], up_list)

# right face
right_list = []
x_cord = (x_bottom_right - x_top_right)/6 + x_top_right  # top left 
y_cord = (y_bottom_right - y_top_right)/6 + y_top_right
hue = right_hsv[x_cord, y_cord, 0]
saturation = right_hsv[x_cord, y_cord, 1]
value = right_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], right_list)
x_cord = (x_bottom_right - x_top_right)/6 * 3 + x_top_right  # top middle 
y_cord = (y_bottom_right - y_top_right)/6 + y_top_right
hue = right_hsv[x_cord, y_cord, 0]
saturation = right_hsv[x_cord, y_cord, 1]
value = right_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], right_list)
x_cord = (x_bottom_right - x_top_right)/6 * 5 + x_top_right  # top right
y_cord = (y_bottom_right - y_top_right)/6 + y_top_right
hue = right_hsv[x_cord, y_cord, 0]
saturation = right_hsv[x_cord, y_cord, 1]
value = right_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], right_list)
x_cord = (x_bottom_right - x_top_right)/6 + x_top_right  # middle left
y_cord = (y_bottom_right - y_top_right)/6 * 3 + y_top_right 
hue = right_hsv[x_cord, y_cord, 0]
saturation = right_hsv[x_cord, y_cord, 1]
value = right_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], right_list)
x_cord = (x_bottom_right - x_top_right)/6 * 3 + x_top_right  # center
y_cord = (y_bottom_right - y_top_right)/6 * 3 + y_top_right
hue = right_hsv[x_cord, y_cord, 0]
saturation = right_hsv[x_cord, y_cord, 1]
value = right_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], right_list)
x_cord = (x_bottom_right - x_top_right)/6 * 5 + x_top_right  # middle right
y_cord = (y_bottom_right - y_top_right)/6 * 3 + y_top_right
hue = right_hsv[x_cord, y_cord, 0]
saturation = right_hsv[x_cord, y_cord, 1]
value = right_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], right_list)
x_cord = (x_bottom_right - x_top_right)/6 + x_top_right  # bottom left
y_cord = (y_bottom_right - y_top_right)/6 * 5 + y_top_right
hue = right_hsv[x_cord, y_cord, 0]
saturation = right_hsv[x_cord, y_cord, 1]
value = right_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], right_list)
x_cord = (x_bottom_right - x_top_right)/6 * 3 + x_top_right  # bottom middle
y_cord = (y_bottom_right - y_top_right)/6 * 5 + y_top_right
hue = right_hsv[x_cord, y_cord, 0]
saturation = right_hsv[x_cord, y_cord, 1]
value = right_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], right_list)
x_cord = (x_bottom_right - x_top_right)/6 * 5 + x_top_right  # bottom right
y_cord = (y_bottom_right - y_top_right)/6 * 5 + y_top_right
hue = right_hsv[x_cord, y_cord, 0]
saturation = right_hsv[x_cord, y_cord, 1]
value = right_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], right_list)

# front face
front_list = []
x_cord = (x_bottom_front - x_top_front)/6 + x_top_front  # top left 
y_cord = (y_bottom_front - y_top_front)/6 + y_top_front
hue = front_hsv[x_cord, y_cord, 0]
saturation = front_hsv[x_cord, y_cord, 1]
value = front_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], front_list)
x_cord = (x_bottom_front - x_top_front)/6 * 3 + x_top_front  # top middle 
y_cord = (y_bottom_front - y_top_front)/6 + y_top_front
hue = front_hsv[x_cord, y_cord, 0]
saturation = front_hsv[x_cord, y_cord, 1]
value = front_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], front_list)
x_cord = (x_bottom_front - x_top_front)/6 * 5 + x_top_front  # top right
y_cord = (y_bottom_front - y_top_front)/6 + y_top_front
hue = front_hsv[x_cord, y_cord, 0]
saturation = front_hsv[x_cord, y_cord, 1]
value = front_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], front_list)
x_cord = (x_bottom_front - x_top_front)/6 + x_top_front  # middle left
y_cord = (y_bottom_front - y_top_front)/6 * 3 + y_top_front 
hue = front_hsv[x_cord, y_cord, 0]
saturation = front_hsv[x_cord, y_cord, 1]
value = front_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], front_list)
x_cord = (x_bottom_front - x_top_front)/6 * 3 + x_top_front  # center
y_cord = (y_bottom_front - y_top_front)/6 * 3 + y_top_front
hue = front_hsv[x_cord, y_cord, 0]
saturation = front_hsv[x_cord, y_cord, 1]
value = front_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], front_list)
x_cord = (x_bottom_front - x_top_front)/6 * 5 + x_top_front  # middle right
y_cord = (y_bottom_front - y_top_front)/6 * 3 + y_top_front
hue = front_hsv[x_cord, y_cord, 0]
saturation = front_hsv[x_cord, y_cord, 1]
value = front_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], front_list)
x_cord = (x_bottom_front - x_top_front)/6 + x_top_front  # bottom left
y_cord = (y_bottom_front - y_top_front)/6 * 5 + y_top_front
hue = front_hsv[x_cord, y_cord, 0]
saturation = front_hsv[x_cord, y_cord, 1]
value = front_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], front_list)
x_cord = (x_bottom_front - x_top_front)/6 * 3 + x_top_front  # bottom middle
y_cord = (y_bottom_front - y_top_front)/6 * 5 + y_top_front
hue = front_hsv[x_cord, y_cord, 0]
saturation = front_hsv[x_cord, y_cord, 1]
value = front_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], front_list)
x_cord = (x_bottom_front - x_top_front)/6 * 5 + x_top_front  # bottom right
y_cord = (y_bottom_front - y_top_front)/6 * 5 + y_top_front
hue = front_hsv[x_cord, y_cord, 0]
saturation = front_hsv[x_cord, y_cord, 1]
value = front_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], front_list)

# down face
down_list = []
x_cord = (x_bottom_down - x_top_down)/6 + x_top_down  # top left 
y_cord = (y_bottom_down - y_top_down)/6 + y_top_down
hue = down_hsv[x_cord, y_cord, 0]
saturation = down_hsv[x_cord, y_cord, 1]
value = down_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], down_list)
x_cord = (x_bottom_down - x_top_down)/6 * 3 + x_top_down  # top middle 
y_cord = (y_bottom_down - y_top_down)/6 + y_top_down
hue = down_hsv[x_cord, y_cord, 0]
saturation = down_hsv[x_cord, y_cord, 1]
value = down_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], down_list)
x_cord = (x_bottom_down - x_top_down)/6 * 5 + x_top_down  # top right
y_cord = (y_bottom_down - y_top_down)/6 + y_top_down
hue = down_hsv[x_cord, y_cord, 0]
saturation = down_hsv[x_cord, y_cord, 1]
value = down_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], down_list)
x_cord = (x_bottom_down - x_top_down)/6 + x_top_down  # middle left
y_cord = (y_bottom_down - y_top_down)/6 * 3 + y_top_down 
hue = down_hsv[x_cord, y_cord, 0]
saturation = down_hsv[x_cord, y_cord, 1]
value = down_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], down_list)
x_cord = (x_bottom_down - x_top_down)/6 * 3 + x_top_down  # center
y_cord = (y_bottom_down - y_top_down)/6 * 3 + y_top_down
hue = down_hsv[x_cord, y_cord, 0]
saturation = down_hsv[x_cord, y_cord, 1]
value = down_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], down_list)
x_cord = (x_bottom_down - x_top_down)/6 * 5 + x_top_down  # middle right
y_cord = (y_bottom_down - y_top_down)/6 * 3 + y_top_down
hue = down_hsv[x_cord, y_cord, 0]
saturation = down_hsv[x_cord, y_cord, 1]
value = down_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], down_list)
x_cord = (x_bottom_down - x_top_down)/6 + x_top_down  # bottom left
y_cord = (y_bottom_down - y_top_down)/6 * 5 + y_top_down
hue = down_hsv[x_cord, y_cord, 0]
saturation = down_hsv[x_cord, y_cord, 1]
value = down_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], down_list)
x_cord = (x_bottom_down - x_top_down)/6 * 3 + x_top_down  # bottom middle
y_cord = (y_bottom_down - y_top_down)/6 * 5 + y_top_down
hue = down_hsv[x_cord, y_cord, 0]
saturation = down_hsv[x_cord, y_cord, 1]
value = down_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], down_list)
x_cord = (x_bottom_down - x_top_down)/6 * 5 + x_top_down  # bottom right
y_cord = (y_bottom_down - y_top_down)/6 * 5 + y_top_down
hue = down_hsv[x_cord, y_cord, 0]
saturation = down_hsv[x_cord, y_cord, 1]
value = down_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], down_list)

# left face
left_list = []
x_cord = (x_bottom_left - x_top_left)/6 + x_top_left  # top left 
y_cord = (y_bottom_left - y_top_left)/6 + y_top_left
hue = left_hsv[x_cord, y_cord, 0]
saturation = left_hsv[x_cord, y_cord, 1]
value = left_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], left_list)
x_cord = (x_bottom_left - x_top_left)/6 * 3 + x_top_left  # top middle 
y_cord = (y_bottom_left - y_top_left)/6 + y_top_left
hue = left_hsv[x_cord, y_cord, 0]
saturation = left_hsv[x_cord, y_cord, 1]
value = left_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], left_list)
x_cord = (x_bottom_left - x_top_left)/6 * 5 + x_top_left  # top right
y_cord = (y_bottom_left - y_top_left)/6 + y_top_left
hue = left_hsv[x_cord, y_cord, 0]
saturation = left_hsv[x_cord, y_cord, 1]
value = left_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], left_list)
x_cord = (x_bottom_left - x_top_left)/6 + x_top_left  # middle left
y_cord = (y_bottom_left - y_top_left)/6 * 3 + y_top_left
hue = left_hsv[x_cord, y_cord, 0]
saturation = left_hsv[x_cord, y_cord, 1]
value = left_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], left_list)
x_cord = (x_bottom_left - x_top_left)/6 * 3 + x_top_left  # center
y_cord = (y_bottom_left - y_top_left)/6 * 3 + y_top_left
hue = left_hsv[x_cord, y_cord, 0]
saturation = left_hsv[x_cord, y_cord, 1]
value = left_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], left_list)
x_cord = (x_bottom_left - x_top_left)/6 * 5 + x_top_left  # middle right
y_cord = (y_bottom_left - y_top_left)/6 * 3 + y_top_left
hue = left_hsv[x_cord, y_cord, 0]
saturation = left_hsv[x_cord, y_cord, 1]
value = left_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], left_list)
x_cord = (x_bottom_left - x_top_left)/6 + x_top_left  # bottom left
y_cord = (y_bottom_left - y_top_left)/6 * 5 + y_top_left
hue = left_hsv[x_cord, y_cord, 0]
saturation = left_hsv[x_cord, y_cord, 1]
value = left_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], left_list)
x_cord = (x_bottom_left - x_top_left)/6 * 3 + x_top_left  # bottom middle
y_cord = (y_bottom_left - y_top_left)/6 * 5 + y_top_left
hue = left_hsv[x_cord, y_cord, 0]
saturation = left_hsv[x_cord, y_cord, 1]
value = left_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], left_list)
x_cord = (x_bottom_left - x_top_left)/6 * 5 + x_top_left  # bottom right
y_cord = (y_bottom_left - y_top_left)/6 * 5 + y_top_left
hue = left_hsv[x_cord, y_cord, 0]
saturation = left_hsv[x_cord, y_cord, 1]
value = left_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], left_list)

# bottom face
back_list = []
x_cord = (x_bottom_back - x_top_back)/6 + x_top_back  # top left 
y_cord = (y_bottom_back - y_top_back)/6 + y_top_back
hue = back_hsv[x_cord, y_cord, 0]
saturation = back_hsv[x_cord, y_cord, 1]
value = back_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], back_list)
x_cord = (x_bottom_back - x_top_back)/6 * 3 + x_top_back  # top middle 
y_cord = (y_bottom_back - y_top_back)/6 + y_top_back
hue = back_hsv[x_cord, y_cord, 0]
saturation = back_hsv[x_cord, y_cord, 1]
value = back_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], back_list)
x_cord = (x_bottom_back - x_top_back)/6 * 5 + x_top_back  # top right
y_cord = (y_bottom_back - y_top_back)/6 + y_top_back
hue = back_hsv[x_cord, y_cord, 0]
saturation = back_hsv[x_cord, y_cord, 1]
value = back_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], back_list)
x_cord = (x_bottom_back - x_top_back)/6 + x_top_back  # middle left
y_cord = (y_bottom_back - y_top_back)/6 * 3 + y_top_back
hue = back_hsv[x_cord, y_cord, 0]
saturation = back_hsv[x_cord, y_cord, 1]
value = back_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], back_list)
x_cord = (x_bottom_back - x_top_back)/6 * 3 + x_top_back  # center
y_cord = (y_bottom_back - y_top_back)/6 * 3 + y_top_back
hue = back_hsv[x_cord, y_cord, 0]
saturation = back_hsv[x_cord, y_cord, 1]
value = back_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], back_list)
x_cord = (x_bottom_back - x_top_back)/6 * 5 + x_top_back  # middle right
y_cord = (y_bottom_back - y_top_back)/6 * 3 + y_top_back
hue = back_hsv[x_cord, y_cord, 0]
saturation = back_hsv[x_cord, y_cord, 1]
value = back_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], back_list)
x_cord = (x_bottom_back - x_top_back)/6 + x_top_back  # bottom left
y_cord = (y_bottom_back - y_top_back)/6 * 5 + y_top_back
hue = back_hsv[x_cord, y_cord, 0]
saturation = back_hsv[x_cord, y_cord, 1]
value = back_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], back_list)
x_cord = (x_bottom_back - x_top_back)/6 * 3 + x_top_back  # bottom middle
y_cord = (y_bottom_back - y_top_back)/6 * 5 + y_top_back
hue = back_hsv[x_cord, y_cord, 0]
saturation = back_hsv[x_cord, y_cord, 1]
value = back_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], back_list)
x_cord = (x_bottom_back - x_top_back)/6 * 5 + x_top_back  # bottom right
y_cord = (y_bottom_back - y_top_back)/6 * 5 + y_top_back
hue = back_hsv[x_cord, y_cord, 0]
saturation = back_hsv[x_cord, y_cord, 1]
value = back_hsv[x_cord, y_cord, 2]
assign([hue, saturation, value], back_list)

cube_list = []

def cube_list_append(l):
    for c in l:
        cube_list.append(c)

cube_list_append(up_list) 
cube_list_append(right_list)
cube_list_append(front_list)
cube_list_append(down_list)
cube_list_append(left_list)
cube_list_append(back_list)
cube_string = ''.join(cube_list)

print("The cube string is:", cube_string)
print("The solving rotations are:", kb.solve(cube_string))   # solving using the cube details
