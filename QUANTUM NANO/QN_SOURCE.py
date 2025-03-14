import math,random,sys
try:
 from direct.showbase.ShowBase import *
 from panda3d.core import *
except ImportError:
 print("ERROR:'pip install panda3d' required")
 sys.exit()
class QN(ShowBase):
 def __init__(s):
  ShowBase.__init__(s)
  s.setFrameRateMeter(True)
  s.disableMouse()
  props=WindowProperties()
  props.setCursorHidden(True)
  props.setSize(1600,900)
  s.keymap={}
  for k in "wsadeq":
   s.accept(k,s.set_key,[k,1])
   s.accept(f"{k}-up",s.set_key,[k,0])
   s.accept("escape",sys.exit)
  s.spd=5
  s.cam.setPos(8,8,18)
  s.win.movePointer(0,s.win.getXSize()//2,s.win.getYSize()//2)
  s.accept("mouse1",s.center_mouse)
  s.cursor = s.aspect2d.attachNewNode(TextNode("cursor"))
  s.cursor.node().setText("Q")
  s.cursor.node().setTextColor(1,1,1,1)
  s.cursor.setScale(0.15)
  s.taskMgr.add(s.update_cursor,"update_cursor")
  s.taskMgr.add(s.update,"update")
  s.taskMgr.add(s.mouse_control,"mouse_control")
  Cube=s.loader.loadModel("models/box")
  if Cube:
   diamond=bytes([c for a in [[[255,255,0,255]for b in range(1)]for a in range(1)] for b in a for c in b])
   gold=bytes([c for a in [[[0,255,255,255]for b in range(1)]for a in range(1)] for b in a for c in b])
   grass=bytes([c for a in [[[0,255,0,255]for b in range(1)]for a in range(1)] for b in a for c in b])
   lapis=bytes([c for a in [[[255,0,0,255]for b in range(1)]for a in range(1)] for b in a for c in b])
   redstone=bytes([c for a in [[[0,0,255,255]for b in range(1)]for a in range(1)] for b in a for c in b])
   diamond_c=0
   gold_c=0
   grass_c=0
   lapis_c=0
   redstone_c=0
   for x in range(16):
    for y in range(16):
     for z in range(16):
      if z>=14:
       nT=grass
       grass_c+=1
      elif z >= 12 and z < 14:
       rand=random.randint(1,3)
       if rand==1:
        nT=grass
        grass_c+=1
       elif rand==2 or rand==3:
        nT=lapis
        lapis_c+=1
      elif z>4 and z<12:
       rand=random.randint(1,4)
       if rand==1 or rand==2:
        nT=grass
        grass_c+=1
       elif rand==3:
        nT=gold
        gold_c+=1
       elif rand==4:
        nT=redstone
        redstone_c+=1
      elif z>=0 and z<=4:
       rand=random.randint(1,24)
       if rand>=1 and rand<=23:
        nT=grass
        grass_c+=1
       else:
        nT=diamond
        diamond_c+=1
      N=render.attachNewNode("instance")
      N.setPos(x,y,z)
      t=Texture()
      t.setup2dTexture(1,1,Texture.TUnsignedByte,Texture.FRgba8)
      t.setRamImage(nT)
      ts=TextureStage("ts")
      N.setTexture(ts,t)
      Cube.instanceTo(N)
   render.flattenStrong()
   props.setTitle(f"QUANTUM NANO | DIAMOND: {diamond_c}, GOLD: {gold_c}, GRASS: {grass_c}, LAPIS:{lapis_c}, REDSTONE: {redstone_c}")
   s.win.requestProperties(props)
  else:
      sys.exit()
 def set_key(s,key,value):
  s.keymap[key]=value
 def update(s,task):
  dt=globalClock.getDt()
  h,p=math.radians(s.cam.getH()),math.radians(s.cam.getP())
  fwd,strafe,vert=s.keymap.get("w",0)-s.keymap.get("s",0),s.keymap.get("d",0)-s.keymap.get("a",0),s.keymap.get("e",0)-s.keymap.get("q",0)
  dx,dy=(fwd*-math.sin(h)+strafe*math.cos(h))*s.spd*dt,(fwd*math.cos(h)+strafe*math.sin(h))*s.spd*dt
  dz=vert*s.spd*dt
  s.cam.setPos(s.cam.getX()+dx,s.cam.getY()+dy,s.cam.getZ()+dz)
  return task.cont
 def mouse_control(s,task):
  if s.mouseWatcherNode.hasMouse():
   mpos=s.mouseWatcherNode.getMouse()
   s.cam.setH(s.cam.getH()-mpos.getX()*100)
   s.cam.setP(s.cam.getP()+mpos.getY()*100)
   s.win.movePointer(0,s.win.getXSize()//2,s.win.getYSize()//2)
   return task.cont
 def update_cursor(s, task):
  s.cursor.setPos(0,0,0)
  return task.cont
 def center_mouse(s):
  s.win.movePointer(0,s.win.getXSize()//2,s.win.getYSize()//2)
QN().run()
