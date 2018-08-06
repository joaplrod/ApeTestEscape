import pyautogui as pya

def matmaker(W,H,fW,fH,sW,sH):
  #width, height = pya.size()
  k = 0
  if W == fW:
    fW = W+1
    sW = 1
  if H == fH:
    fH = H+1
    sH = 1
  colormat = []
  for i in range(W, fW, sW):
    for j in range(H, fH, sH):
      colormat.append(pya.pixel(i, j))
      k += 1
  return colormat