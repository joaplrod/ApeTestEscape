#! python3
# Benchmark_advanced.py - An Expert Cura benchmark scenario

import config2 as C2
import pyautogui as pya
import time

# ###### Coordinates in screen ######
#
# 0,0       X increases -->
# +---------------------------+
# |                           | Y increases
# |                           |     |
# |   1920 x 1080 screen      |     |
# |                           |     V
# |                           |
# |                           |
# +---------------------------+ 1919, 1079

# ##### Quadrant division of the screen ######
#
# ,--------------,      ,--------------,      ,--------------,
# |  Q2  |  Q1   |      |   | Q5  |    |      |......|.......|
# |......|.......|      |   |.....|    |      | Q8   |  Q7   |
# |  Q3  |  Q4   |      |   | Q6  |    |      |''''''|'''''''|
# '------|-------'      '--------------'      '--------------'

width, height = pya.size()
start_scp = time.time()

# Chose which version must be tested
cura_version = "3.4.99"

C2.LoadExpertVariables(cura_version)
print("Test for " + cura_version + " started...")

time.sleep(5)


# # Go to desktop (To clear the screen)
# pya.hotkey('win','d')
# pya.click(width//2, height //2)
#
#
# #       ###################
# #       #### Open Cura ####
# #       ###################
# C2.OpenCura(cura_version)
# Cura_opened = C2.findTarget(C2.imgIsCuraOpened, C2.Q2)
# print("The time that took to open Cura was: " + str(Cura_opened[2]))
# # Maximize Cura
# C2.MaxScreen()



# #       #####################
# #       #### Drag n Drop ####
# #       #####################
#
# # Resize Cura window to right side (Drag n Drop file is on the left side of the desktop)
# pya.hotkey('win','right')
# time.sleep(0.5)
# pya.hotkey('esc')
#
#
# file_location = C2.findTarget(C2.imgexptest, C2.Q3)
# print('File location found: ', file_location[:-1])
#
# # Actually drag and drop the file
# pya.moveTo(file_location[0], file_location[1])
# time.sleep(0.5)
# pya.dragTo(width*3//5, height//2, button='left',duration=1)
# pya.click()
#
# file_loaded = C2.findTarget(C2.imgPreparebtn, C2.Q4)
# # Store Prepare btn locat
# prepare_btn = (file_loaded[0], file_loaded[1])
# print("The time that took to load the complex .STL file was: " + str(file_loaded[2]))
#
# # Maximize Cura
# C2.MaxScreen()
#
# #       #####################
# #       #### Slice file #####
# #       #####################
#
# #print(prepare_btn)
# pya.click(prepare_btn) # Press Prepare (To Slice)
# pya.moveTo(width//2,height//2)  # Move cursor out of prepare btn (The img changes if the cursor is in it)
#
# model_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
# print("The time that took to slice the complex .STL file was: " + str(model_sliced[2]))
#
# #       #####################
# #       #### Layer View #####
# #       #####################
#
# C2.layerviewOnOff('on')
#
# layerviewloaded = C2.findTarget(C2.ImgLayerView, C2.Q7)
# print("The time that took to show the Layer View was: " + str(layerviewloaded[2]))
#
# C2.layerviewOnOff('off')


#       ##########################
#       #### Custom Settings #####
#       ##########################


prepare_btn = C2.findTarget(C2.imgPreparebtn, C2.Q4)


custombtn = C2.findTarget(C2.imgcustombtn)
pya.click(custombtn[0], custombtn[1])
#allsetbtn = C2.findTarget(C2.imgallsetbtn)
textbxbtn = C2.findTarget(C2.imgtextbx)
pya.click(textbxbtn[0],textbxbtn[1])
time.sleep(1.5)

pya.typewrite('build plate adhesion type', interval=0.8)

for i in range (0,3,1):
    pya.hotkey('tab')
    time.sleep(1.5)
pya.hotkey('s')
pya.hotkey('enter')

pya.click(textbxbtn[0],textbxbtn[1])
pya.hotkey('ctrl', 'a')

pya.typewrite('wall line count', interval=0.8)
for i in range (0,4,1):
    pya.hotkey('tab')
    time.sleep(2)
pya.typewrite('5')
pya.hotkey('enter')

pya.click(textbxbtn[0],textbxbtn[1])
pya.hotkey('ctrl', 'a')

pya.typewrite('infill pattern', interval=0.8)

for i in range (0,3,1):
    pya.hotkey('tab')
    time.sleep(2)
pya.hotkey('g')
pya.hotkey('enter')

pya.click(textbxbtn[0],textbxbtn[1])
pya.hotkey('ctrl', 'a')
pya.typewrite('fuzzy skin', interval=0.8)

fzyskbtn = C2.findTarget(C2.imgfuzsk, C2.Q4)
pya.click(fzyskbtn[0], fzyskbtn[1])


pya.click(prepare_btn) # Press Prepare (To Slice)
pya.moveTo(width//2,height//2)  # Move cursor out of prepare btn (The img changes if the cursor is in it)

pya.alert("continue")

model_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice the complex .STL file with modifications was: " + str(model_sliced[2]))