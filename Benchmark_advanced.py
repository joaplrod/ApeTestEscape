#! python3
# Benchmark_advanced.py - An advanced Cura benchmark scenario

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
#cura_version = "3.5"
#cura_version = "3.1"
#cura_version = "3.0.4"
#cura_version = "3.4.1"
#cura_version = "3.2.1"
#cura_version = "3.2.0"
#cura_version = "3.2.1"
#cura_version = "3.3"
#cura_version = "3.3.1"
#cura_version = "3.4.0"
#cura_version = "3.4.1"



C2.LoadAdvanceVariables(cura_version)
print("Test for " + cura_version + " started...")
C2.BenchRes['version'] = str(cura_version)
C2.BenchRes['date'] = time.strftime('%a, %d %b %Y %H:%M:%S', time.gmtime())

# Go to desktop (To clear the screen)
pya.hotkey('win','d')
pya.click(width//2, height //2)


#       ###################
#       #### Open Cura ####
#       ###################
C2.OpenCura(cura_version)
Cura_opened = C2.findTarget(C2.imgIsCuraOpened, C2.Q2)
print("The time that took to open Cura was: " + str(Cura_opened[2]))
C2.BenchRes['Scenario']['Advanced']['Open Cura']['time'] = str(Cura_opened[-1])

# Maximize Cura
C2.MaxScreen()

#time.sleep(4)

#       ###########################
#       #### Open project file ####
#       ###########################

C2.OpenFile('AdvTEST.stl')
preparebtn = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print("The time that took to load the .stl model was: " + str(preparebtn[2]))
C2.BenchRes['Scenario']['Advanced']['Load Stl']['time'] = str(preparebtn[-1])


pya.click(preparebtn[:-1])
pya.moveTo(width//2,height//2)

onemodel_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice one model was: " + str(onemodel_sliced[2]))


object_pos = C2.findTarget(C2.imgobjectpos, C2.Q6)


C2.MultiModel(20)       # Multiply by 20

multiply_finished = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print("The time that took to load the 20 more .stl models was: " + str(multiply_finished[2]))

pya.click(preparebtn[:-1])
pya.moveTo(1,1, duration=1)

twenmodel_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice 21 models was: " + str(twenmodel_sliced[2]))
C2.BenchRes['Scenario']['Advanced']['Slice 20stl']['time'] = str(twenmodel_sliced[-1])


C2.Chose6Models(object_pos)

rotatebtn = C2.findTarget(C2.imgrotatebtn,C2.Q2)    # Find rotate btn locat
pya.click(rotatebtn[:-1])
rotate_line = C2.findTarget(C2.imgrotateline)

pya.moveTo(rotate_line[:-1])
pya.dragRel(200,0,1.5)

rotate_finished = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print("The time that took to rotate the 6 .stl model was: " + str(rotate_finished[2]))

pya.click(preparebtn[:-1])
pya.moveTo(width//2,height//2)

rot_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice after rotating the models was: " + str(rot_sliced[2]))
C2.BenchRes['Scenario']['Advanced']['RotatedSlice']['time'] = str(rot_sliced[-1])

# rotatereset = C2.findTarget(C2.imgrotatereset)
# pya.click(rotatereset[0], rotatereset[1])

#   Mirroring step
mirrorbtn = C2.findTarget(C2.imgmirrorbtn)     #Mirror set
pya.click(mirrorbtn[0],mirrorbtn[1])        #Click mirror setting

mirror_line = C2.findTarget(C2.imgmirrorline)
print(mirror_line)
pya.click(mirror_line[0],mirror_line[1])


mirror_finished = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print("The time that took to mirror the 6 .stl model was: " + str(mirror_finished[2]))

pya.click(preparebtn[0],preparebtn[1])
pya.moveTo(width//2,height//2)

mir_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice after mirroring the models was: " + str(mir_sliced[2]))
C2.BenchRes['Scenario']['Advanced']['MirrornSlice']['time'] = str(mir_sliced[-1])


move_set = C2.findTarget(C2.imgmovebtn)
pya.click(move_set[0],move_set[1])
pya.moveTo(width // 2, height // 2)

move_line = C2.findTarget(C2.imgmoveline, C2.Q2)
pya.click((move_line[0] + 100),move_line[1])
print(move_line)


pya.hotkey('ctrl','r')
C2.findTarget(C2.imgPreparebtn, C2.Q4)
pya.hotkey('ctrl','a')
time.sleep(1.5)
pya.typewrite('5')
time.sleep(1.5)
pya.hotkey('enter')


move_finished = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print("The time that took to move the 6 .stl model was: " + str(move_finished[2]))


time.sleep(5)
pya.moveTo(preparebtn[:-1])
time.sleep(2)
pya.click(preparebtn[:-1])

pya.moveTo(width//2,height//2)

mov_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice after moving the models was: " + str(mov_sliced[2]))
C2.BenchRes['Scenario']['Advanced']['MovenSlice']['time'] = str(mov_sliced[-1])



#Drag n Drop 3 files
#Resize Cura window to right side (Drag n Drop file is on the left side of the desktop)
pya.hotkey('win','right')
time.sleep(1.5)
pya.hotkey('esc')
time.sleep(1.5)
pya.hotkey('esc')

DnD3_pos = C2.findTarget(C2.imgDnD3)
pya.moveTo(1,1)
time.sleep(1)
pya.dragRel(width // 3, height // 2, duration=1)
time.sleep(1)


# Actually drag and drop the file
pya.moveTo(DnD3_pos[0], DnD3_pos[1])
time.sleep(1.5)
pya.dragTo(width*3//5, height*2//3, button='left', duration=1)
time.sleep(1.5)
pya.click()

DnD3_loaded = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print("The time that took to Drag n Drop the 3 files was: " + str(DnD3_loaded[2]))
C2.BenchRes['Scenario']['Advanced']['DnD']['time'] = str(DnD3_loaded[-1])

pya.hotkey('ctrl','r')
wait = C2.findTarget(C2.imgPreparebtn, C2.Q4)
time.sleep(1)
pya.click(preparebtn[:-1])
pya.moveTo(width//2,height//2)

DnD3_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice after moving the models was: " + str(DnD3_sliced[2]))
C2.BenchRes['Scenario']['Advanced']['Slice All']['time'] = str(DnD3_sliced[-1])
C2.BenchRes['Scenario']['Advanced']['Running time']['time'] = str(time.time() - start_scp)

print("Test finished")
#Load info in excel file - Future step
C2.writeFile('Advanced')
C2.CloseCura()
#pya.alert("Test is finished...")