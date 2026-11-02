#!/usr/bin/env python3
"""analyze-certificate-inspector intro: rooftop observatory during a long exposure, scenery only, nothing readable."""
import random
from PIL import Image, ImageDraw, ImageFilter
random.seed(47)
W,H=1200,520
ALT=(24,34,72); APR=(244,176,110); CIR=(244,246,248); SIL=(193,199,209)
img=Image.new('RGB',(W,H),ALT); d=ImageDraw.Draw(img,'RGBA')
# night sky taking the upper half, altitude blue deepening upward
for y in range(0,270):
    t=y/270; d.line([(0,y),(W,y)],fill=(int(16+14*t),int(24+18*t),int(52+34*t)))
# thin cirrus bands in white
for bx,by in [(80,64),(420,110),(760,48)]:
    for i in range(4): d.line([(bx,by+i*7),(bx+340-i*30,by+i*7-8)],fill=(230,236,244,70),width=3)
# field of small steady stars, no words formed by them
for _ in range(150):
    x,y=random.uniform(0,W),random.uniform(0,240); r=random.choice([1,1,2])
    d.ellipse([x-r,y-r,x+r,y+r],fill=(235,240,248,220))
# the comet high at the right: bright silver head, vast apricot tail trailing off the edge
hx,hy=935,92
d.polygon([(hx,hy-14),(1200,hy-96),(1200,hy-30),(hx,hy+14)],fill=(244,176,110,110))
d.polygon([(hx,hy-7),(1200,hy-74),(1200,hy-48),(hx,hy+7)],fill=(246,196,138,110))
for i in range(12):
    t=i/12; d.line([(hx,hy),(hx+290*t,hy-58*t+16*t)],fill=(246,220,180,90),width=max(1,int(10*(1-t))))
d.ellipse([hx-17,hy-17,hx+17,hy+17],fill=(248,250,252))
d.ellipse([hx-9,hy-9,hx+9,hy+9],fill=(255,255,255))
# town below the parapet: rooftops, chimneys, a spire, scattered lit windows
d.polygon([(0,352),(0,306),(150,292),(330,312),(520,296),(700,314),(900,298),(1200,316),(1200,352)],fill=(14,18,38))
for x,y in [(90,318),(240,326),(430,320),(620,328),(820,322),(1020,330)]:
    d.rectangle([x,y-20,x+14,y],fill=(10,13,28))
d.polygon([(520,314),(534,262),(548,314)],fill=(10,13,28))  # church spire
for _ in range(38):
    x,y=random.uniform(20,1180),random.uniform(318,346)
    d.rectangle([x,y,x+9,y+12],fill=(250,196,110,230))
# flat roof in the midground, low parapet
d.rectangle([0,330,W,352],fill=(52,50,58))
d.rectangle([0,352,W,520],fill=(38,36,44))
# table with star charts held down by a stone: dots and faint ruled lines, no writing
d.rectangle([430,386,690,398],fill=(90,70,48))
d.rectangle([446,398,462,452],fill=(70,54,36)); d.rectangle([648,398,664,452],fill=(70,54,36))
d.rectangle([452,368,668,390],fill=(238,240,242))
for _ in range(26):
    x,y=random.uniform(460,660),random.uniform(371,387); d.point((x,y),fill=(40,48,90)); d.point((x+1,y),fill=(40,48,90))
for gx in range(478,668,30): d.line([(gx,369),(gx,389)],fill=(190,196,205),width=1)
d.ellipse([540,364,576,382],fill=(105,103,108))  # the stone
# closed plate box
d.rectangle([740,404,858,448],fill=(80,62,40)); d.rectangle([740,404,858,418],fill=(96,76,48))
# foreground: camera end of the telescope at close range, a diagonal brass tube on a heavy tripod
d.polygon([(96,388),(118,404),(268,238),(246,220)],fill=(150,116,58))  # brass tube, camera end low at left
d.polygon([(246,220),(268,238),(292,214),(272,198)],fill=(120,88,40))
d.rectangle([66,392,128,430],fill=(60,42,24))  # camera box at the near end
d.ellipse([84,402,112,422],fill=(196,158,84),outline=(120,90,40),width=2)
for lx in (120,182,238):
    d.line([(178,392),(lx,520)],fill=(70,54,32),width=10)
d.ellipse([150,306,166,322],fill=(196,158,84),outline=(120,90,40),width=2)  # brass fitting on the tube
# empty silver plate holder leaning against the tripod leg, glass catching apricot light on one edge
d.polygon([(286,520),(322,398),(388,408),(366,520)],fill=SIL,outline=(140,146,156),width=3)
d.polygon([(298,506),(328,416),(376,422),(360,506)],fill=(30,40,78))
d.line([(376,422),(360,506)],fill=APR,width=5)
# roof lantern at the frame edge, warm light
d.rectangle([1150,300,1184,344],outline=(20,20,24),width=3)
d.rectangle([1156,308,1178,336],fill=(252,204,116))
img=img.filter(ImageFilter.GaussianBlur(0.4))
img.save(__file__.rsplit('/',1)[0]+'/intro-banner.png')
print('saved intro')
