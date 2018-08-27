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
#cura_version = "3.4.99"
cura_version = "3.0.4"

C2.LoadExpertVariables(cura_version)
print("Test for " + cura_version + " started...")

time.sleep(5)


# Go to desktop (To clear the screen)
pya.hotkey('win','d')
pya.click(width//2, height //2)


#       ###################
#       #### Open Cura ####
#       ###################
C2.OpenCura(cura_version)
Cura_opened = C2.findTarget(C2.imgIsCuraOpened, C2.Q2)
print("The time that took to open Cura was: " + str(Cura_opened[2]))
# Maximize Cura
C2.MaxScreen()



#       #####################
#       #### Drag n Drop ####
#       #####################

# Resize Cura window to right side (Drag n Drop file is on the left side of the desktop)
pya.hotkey('win','right')
time.sleep(0.5)
pya.hotkey('esc')

time.sleep(1.5)
pya.click(width // 3, height // 3)

file_location = C2.findTarget(C2.imgexptest, C2.Q3)
print('File location found: ', file_location[:-1])

# Actually drag and drop the file
pya.moveTo(file_location[0], file_location[1])
time.sleep(0.5)
pya.dragTo(width*3//5, height//2, button='left',duration=1)
pya.click()

file_loaded = C2.findTarget(C2.imgPreparebtn, C2.Q4)
# Store Prepare btn locat
prepare_btn = (file_loaded[0], file_loaded[1])
print("The time that took to load the complex .STL file was: " + str(file_loaded[2]))

# Maximize Cura
C2.MaxScreen()

#       #####################
#       #### Slice file #####
#       #####################


prepare_btn = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print(prepare_btn)


pya.click(prepare_btn[0], prepare_btn[1]) # Press Prepare (To Slice)
pya.moveTo(width//2,height//2)  # Move cursor out of prepare btn (The img changes if the cursor is in it)

model_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice the complex .STL file was: " + str(model_sliced[2]))

#       #####################
#       #### Layer View #####
#       #####################

C2.layerviewOnOff('on')

layerviewloaded = C2.findTarget(C2.imgLayerView, C2.Q7)
print("The time that took to show the Layer View was: " + str(layerviewloaded[2]))

C2.layerviewOnOff('off')


#       ##########################
#       #### Custom Settings #####
#       ##########################


# prepare_btn = (1302, 697)

C2.ResetExtraset()

# custombtn = C2.findTarget(C2.imgcustombtn)
# pya.click(custombtn[0], custombtn[1])

textbxbtn = C2.findTarget(C2.imgtextbx, C2.Q7)
time.sleep(1)

C2.TypeTextinTextBox('build plate adhesion type', textbxbtn)
for i in range (0,3,1):
    pya.hotkey('tab')
    time.sleep(1.5)
pya.hotkey('s')
pya.hotkey('enter')


C2.ClearTextBox(textbxbtn)
C2.TypeTextinTextBox('wall line count', textbxbtn)

for i in range (0,4,1):
    pya.hotkey('tab')
    time.sleep(1)
pya.typewrite('5')
pya.hotkey('enter')



C2.ClearTextBox(textbxbtn)
C2.TypeTextinTextBox('infill pattern', textbxbtn)

for i in range (0,3,1):
    pya.hotkey('tab')
    time.sleep(2)
pya.hotkey('g')
pya.hotkey('enter')

C2.ClearTextBox(textbxbtn)
C2.TypeTextinTextBox('fuzzy skin', textbxbtn)

fzyskbtn = C2.findTarget(C2.imgfuzsk, C2.Q4)
pya.click(fzyskbtn[0], fzyskbtn[1])


pya.click(prepare_btn[0], prepare_btn[1]) # Press Prepare (To Slice)
pya.moveTo(width//2,height//2)  # Move cursor out of prepare btn (The img changes if the cursor is in it)

modif_model_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice the complex .STL file with modifications was: " + str(modif_model_sliced[2]))

#pya.alert("Done...")

#Load info in excel file
f = open(r'C:\Users\System-Testing\PycharmProjects\CuraBenchmark\ResultsExpCuraBenchmark.txt','a')

f.write('Test for Cura' + str(cura_version) + ' started...')
f.write('\n')
f.write("---> Time to open Cura is: " +  str(Cura_opened[2]))
f.write('\n')
f.write("---> Time to Drag n Drop is: "+ str(file_loaded[2]))
f.write('\n')
f.write("---> Time to slice the '.stl' is: " + str(model_sliced[2]))
f.write('\n')
f.write("---> Time to show Layer view is of the .stl is: " + str(layerviewloaded[2]))
f.write('\n')
f.write("---> Time to load modified .stl file is: "+ str(modif_model_sliced[2]))
f.write('\n')
f.write("---> Time to run the script was: " + str(time.time() - start_scp))
f.write('\n')
f.write('\n')
f.close()

#pya.alert("Test is finished...")