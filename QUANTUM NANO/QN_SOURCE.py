import math,random,sys
try:
 from direct.showbase.ShowBase import *
 from panda3d.core import *
except ImportError:
 print("ERROR:'pip install panda3d' required")
 sys.exit()
class QN(ShowBase):
 def __init__(s):
  print("LOADING")
  ShowBase.__init__(s)
  s.disableMouse()
  props=WindowProperties()
  props.setCursorHidden(True)
  s.win.requestProperties(props)
  s.keymap={}
  for k in "wsadeq":
   s.accept(k,s.set_key,[k,1])
   s.accept(f"{k}-up",s.set_key,[k,0])
   s.accept("escape",sys.exit)
   s.spd=5
   s.cam.setPos(8,8,17)
   s.win.movePointer(0,s.win.getXSize()//2,s.win.getYSize()//2)
   s.accept("mouse1",s.center_mouse)
   c=s.loader.loadModel("models/box")
   s.cursor = s.aspect2d.attachNewNode(TextNode("cursor"))
   s.cursor.node().setText("Q")
   s.cursor.node().setTextColor(1,1,1,1)
   s.cursor.setScale(0.15)
   s.taskMgr.add(s.update_cursor,"update_cursor")
  if c:
   T=[[[[a%256,b%256,a^b%256,255]for b in range(256)]for a in range(256)],[[[a%256,b%256,(a+b)%256,255]for b in range(256)]for a in range(256)],[[[a%256,b%256,a*b%256,255]for b in range(256)]for a in range(256)],[[[255,0,0,255]for b in range(256)]for a in range(256)],[[[0,255,255,255]for b in range(256)]for a in range(256)],[[[255,0,255,255]for b in range(256)]for a in range(256)],[[[255,255,255,255]for b in range(256)]for a in range(256)],[[[0,0,0,255]for b in range(256)]for a in range(256)]]
   for x in range(16):
    for y in range(16):
     for z in range(16):
      if random.randint(1,2) == 1:
       N=NodePath("N")
       c.copyTo(N)
       N.reparentTo(s.render)
       N.setPos(x,y,z)
       t=Texture()
       t.setup2dTexture(256,256,Texture.TUnsignedByte,Texture.FRgba8)
       t.setRamImage(bytes([c for a in random.choice(T) for b in a for c in b]))
       ts=TextureStage("ts")
       N.setTexture(ts,t)
  print("RUNNING")
  s.taskMgr.add(s.update,"update")
  s.taskMgr.add(s.mouse_control,"mouse_control")
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
