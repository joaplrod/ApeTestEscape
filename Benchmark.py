#! python3
# Benchmark.py - A Cura benchmark test

import Config2 as C2
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

#Chose which version must be tested
cura_version = "3.4.1"
#cura_version_str = str(cura_version[0]) + '.' + str(cura_version[1]) + '.' + str(cura_version[2])

C2.LoadVariables(cura_version)

print("Test for " + cura_version + " started...")

#Go to desktop (To clear the screen)
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


file_location = C2.findTarget(C2.Img_file2drag)
print('File location found: ', file_location[:-1])

# Actually drag and drop the file
pya.moveTo(file_location[0], file_location[1])
time.sleep(0.5)
pya.dragTo(width*3//5, height//2, button='left',duration=1)
pya.click()

file_loaded = C2.findTarget(C2.imgPreparebtn, C2.Q4)
# Store Prepare btn locat
prepare_btn = (file_loaded[0], file_loaded[1])
print("The time that took to load the .STL file was: " + str(file_loaded[2]))

# Maximize Cura
#pya.click()
C2.MaxScreen()



#       #####################
#       #### Slice file #####
#       #####################

print(prepare_btn)
pya.click(prepare_btn) # Press Prepare (To Slice)
pya.moveTo(width//2,height//2)  # Move cursor out of prepare btn (The img changes if the cursor is in it)

model_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice the .STL file was: " + str(model_sliced[2]))




#       #####################
#       #### Layer View #####
#       #####################

layerview = C2.findTarget(C2.imgViewLabel, C2.Q1)
pya.click(layerview[0], layerview[1])
time.sleep(1)

for i in range(0,3,1):
    pya.hotkey('down')
    time.sleep(0.5)
pya.hotkey('enter')

layerviewloaded = C2.findTarget(C2.ImgLayerView, C2.Q7)
print("The time that took to show the Layer View was: " + str(layerviewloaded[2]))

# Layer View OFF
pya.click(layerview[0], layerview[1])
time.sleep(1)
pya.hotkey('down')
pya.hotkey('enter')



#       #######################
#       #### Send Printjob ####
#       #######################

pya.click(prepare_btn) # Press Prepare (Also Print btn locat)
printjobesent = C2.findTarget(C2.ImgPrintjobsent, C2.Q3)
print("The time that took to send the print job was: " + str(printjobesent[2]))

#Clean buildplate
C2.cleanBP()



#       ###########################
#       #### Open project file ####
#       ###########################

C2.OpenFile('TEST.3mf')
project_loaded = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print("The time that took to slice the .3mf file was: " + str(project_loaded[2]))



#       ##############################
#       #### Slice file #####
#       ##############################

print(prepare_btn)
pya.click(prepare_btn) # Press Prepare (To Slice)
pya.moveTo(width//2,height//2)  # Move cursor out of prepare btn (The img changes if the cursor is in it)

project_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice the .3mf file was: " + str(project_sliced[2]))



#       #####################
#       #### Layer View #####
#       #####################

pya.click(layerview[0], layerview[1])
time.sleep(1)
for i in range(0,3,1):
    pya.hotkey('down')
    time.sleep(0.5)
pya.hotkey('enter')

layerviewloaded3mf = C2.findTarget(C2.ImgLayerView, C2.Q7)
print("The time that took to show the Layer View of the .3mf was: " + str(layerviewloaded3mf[2]))

#       #######################
#       #### Send Printjob ####
#       #######################

pya.click(prepare_btn) # Press Prepare (Also Print btn locat)
projectsent = C2.findTarget(C2.ImgPrintjobsent, C2.Q3)
print("The time that took to send the project file was: " + str(projectsent[2]))




#Clean buildplate
C2.cleanBP()

#       ####################
#       #### Open Gcode ####
#       ####################

C2.OpenFile('TEST.gcode')
gcode_loaded = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to load the .gcode file was: " + str(gcode_loaded[2]))



#       #######################
#       #### Send Printjob ####
#       #######################

pya.click(prepare_btn) # Press Prepare (Also Print btn locat)
gcodesent = C2.findTarget(C2.ImgPrintjobsent, C2.Q3)
print("The time that took to send the gcode was: " + str(gcodesent[2]))



#Load info in excel file
f = open(r'C:\Users\System-Testing\PycharmProjects\CuraBenchmark\ResultsCuraBenchmark.txt','a')

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
f.write("---> Time to send print over network is: "+ str(printjobesent[2]))
f.write('\n')
f.write("---> Time to load the project file is: "+ str(project_loaded[2]))
f.write('\n')
f.write("---> Time to slice the project file is: "+ str(project_sliced[2]))
f.write('\n')
f.write("---> Time to send the project file printjob is: "+ str(projectsent[2]))
f.write('\n')
f.write("---> Time to load the gcode is: "+ str(gcode_loaded[2]))
f.write('\n')
f.write("---> Time to send the gcode printjob is: "+ str(gcodesent[2]))
f.write('\n')
f.write('\n')

f.close()

pya.alert("Test is finished...")
