#! python3
# Benchmark_advanced.py - An advanced Cura benchmark test

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

#Chose which version must be tested
cura_version = "3.4.99"

C2.LoadVariables(cura_version)
C2.LoadAdvanceVariables(cura_version)
print("Test for " + cura_version + " started...")

#time.sleep(4)

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



#       ###########################
#       #### Open project file ####
#       ###########################

C2.OpenFile('AdvTEST.stl')
preparebtn = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print("The time that took to load the .stl model was: " + str(preparebtn[2]))

pya.click(preparebtn[0],preparebtn[1])
pya.moveTo(width//2,height//2)

onemodel_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice one model was: " + str(onemodel_sliced[2]))

object_pos = C2.findTarget(C2.imgobjectpos, C2.Q6)


C2.MultiModel(20)       # Multiply by 20

multiply_finished = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print("The time that took to load the 20 .stl model was: " + str(multiply_finished[2]))
pya.click(preparebtn[0],preparebtn[1])
pya.moveTo(width//2,height//2)

twenmodel_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice twenty models was: " + str(twenmodel_sliced[2]))


C2.Chose6Models(object_pos)

rotatebtn = C2.findTarget(C2.imgrotatebtn,C2.Q2)    # Find rotate btn locat
pya.click(rotatebtn[0], rotatebtn[1])
rotate_line = C2.findTarget(C2.imgrotateline)

# movebtn = C2.findTarget(C2.imgmovebtn, C2.Q2)       # Find move btn
# rotate_line = C2.findTarget(C2.imgrotateline)
# lockbtn = C2.findTarget(C2.imglockbtn, C2.Q2)       # Find lock btn
# pya.click(lockbtn[0], lockbtn[1])                   # Lock models position
#
# pya.click(rotatebtn[0], rotatebtn[1])
pya.moveTo(rotate_line[0], rotate_line[1])
pya.dragRel(200,0,1.5)

rotate_finished = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print("The time that took to rotate the 6 .stl model was: " + str(rotate_finished[2]))

pya.click(preparebtn[0],preparebtn[1])
pya.moveTo(width//2,height//2)

rot_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice after rotating the models was: " + str(rot_sliced[2]))

# rotatereset = C2.findTarget(C2.imgrotatereset)
# pya.click(rotatereset[0], rotatereset[1])

#   Mirroring step
mirrorbtn = C2.findTarget(C2.imgmirrorbtn, C2.Q2)     #Mirror set
pya.click(mirrorbtn[0],mirrorbtn[1])        #Click mirror setting

mirror_line = C2.findTarget(C2.imgmirrorline)
pya.click(mirror_line[0],mirror_line[1])


mirror_finished = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print("The time that took to mirror the 6 .stl model was: " + str(mirror_finished[2]))

pya.click(preparebtn[0],preparebtn[1])
pya.moveTo(width//2,height//2)

mir_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice after mirroring the models was: " + str(mir_sliced[2]))


move_set = C2.findTarget(C2.imgmovebtn)
pya.click(move_set[0],move_set[1])
pya.moveTo(width // 2, height // 2)

move_line = C2.findTarget(C2.imgmoveline, C2.Q2)
pya.click((move_line[0] + 50),move_line[1])
pya.hotkey('ctrl','a')
time.sleep(1)
pya.typewrite('20')
pya.hotkey('enter')

move_finished = C2.findTarget(C2.imgPreparebtn, C2.Q4)
print("The time that took to move the 6 .stl model was: " + str(move_finished[2]))

pya.click(preparebtn[0],preparebtn[1])
pya.moveTo(width//2,height//2)

mov_sliced = C2.findTarget(C2.imgReady2print, C2.Q4)
print("The time that took to slice after noving the models was: " + str(mov_sliced[2]))


pya.alert("Done. " + str(time.time() - start_scp))