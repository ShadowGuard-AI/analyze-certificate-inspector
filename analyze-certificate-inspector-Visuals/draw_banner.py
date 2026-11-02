#!/usr/bin/env python3
"""analyze-certificate-inspector wordmark banner: rooftop observatory on a May night in 1910, name on the wall sign."""
import random
from PIL import Image, ImageDraw, ImageFont
random.seed(63)
HERE=__file__.rsplit('/',1)[0]
W,H=1400,560
ALT=(24,34,72); APR=(244,176,110); CIR=(244,246,248); SIL=(193,199,209)
img=Image.new('RGB',(W,H),ALT); d=ImageDraw.Draw(img,'RGBA')
for y in range(0,320):
    t=y/320; d.line([(0,y),(W,y)],fill=(int(14+16*t),int(22+20*t),int(48+38*t)))
for _ in range(170):
    x,y=random.uniform(0,W),random.uniform(0,300); d.ellipse([x-1.5,y-1.5,x+1.5,y+1.5],fill=(235,240,248,210))
for bx,by in [(180,70),(820,120)]:
    for i in range(3): d.line([(bx,by+i*7),(bx+300,by+i*7-8)],fill=(230,236,244,60),width=3)
# comet fills the upper sky, tail sweeping across and leaving the frame
hx,hy=1060,84
d.polygon([(hx,hy-20),(240,hy+96),(240,hy+150),(hx,hy+22)],fill=(244,176,110,96))
d.polygon([(hx,hy-10),(240,hy+112),(240,hy+136),(hx,hy+11)],fill=(246,196,138,110))
for i in range(5):
    yy=hy-6+i*11; d.line([(hx-40,yy),(hx-330-i*60,yy+44+i*8)],fill=(246,214,170,70),width=3)
d.ellipse([hx-24,hy-24,hx+24,hy+24],fill=(248,250,252)); d.ellipse([hx-13,hy-13,hx+13,hy+13],fill=(255,255,255))
# sleeping town below the roofline: silhouettes, lit windows, seller cart with bottles in rows, spire
d.rectangle([0,468,W,560],fill=(12,16,34))
d.polygon([(880,468),(896,388),(912,468)],fill=(9,12,26))
for x,w,h in [(60,150,54),(260,120,44),(430,170,60),(640,130,48),(980,160,56),(1200,150,50)]:
    d.rectangle([x,468-h,x+w,468],fill=(16,21,42))
    d.polygon([(x-6,468-h),(x+w/2,468-h-22),(x+w+6,468-h)],fill=(20,26,50))
for _ in range(34):
    x,y=random.uniform(30,1370),random.uniform(428,520); d.rectangle([x,y,x+8,y+11],fill=(250,196,110,230))
# street seller's cart, small bottles set out in rows, nobody looking down
d.rectangle([1120,486,1250,500],fill=(70,50,30)); d.ellipse([1136,498,1162,524],fill=(40,32,22)); d.ellipse([1206,498,1232,524],fill=(40,32,22))
for r in range(2):
    for i in range(6):
        bx=1132+i*19; by=470+r*13; d.rectangle([bx,by,bx+8,by+12],fill=(170,200,180)); d.rectangle([bx+2,by-4,bx+6,by],fill=(150,150,140))
# observatory building and roof, left and center
d.rectangle([0,330,760,560],fill=(40,42,56))
d.rectangle([0,318,820,336],fill=(56,54,64))
# painted wall sign above the door: the one lettered thing in the scene
d.rectangle([36,368,560,428],fill=ALT,outline=SIL,width=3)
f=ImageFont.truetype(HERE+'/fonts/Athiti.ttf',31)
txt='analyze-certificate-inspector'
tw=d.textlength(txt,font=f); d.text(((298-tw/2),382),txt,font=f,fill=CIR)
d.rectangle([610,436,690,560],fill=(22,24,36))  # the door under the sign
# brass telescope on a heavy tripod pointing up at the comet
d.polygon([(330,322),(352,322),(404,196),(384,188)],fill=(150,116,58))
d.polygon([(384,188),(404,196),(428,168),(412,158)],fill=(120,88,40))
for lx in (306,352,398):
    d.line([(342,318),(lx,362)],fill=(70,54,32),width=9)
d.rectangle([404,150,452,182],fill=(60,42,24))  # camera box at the eye end
d.rectangle([412,158,444,174],fill=SIL)
# astronomer holding a fresh plate up toward the comet light
d.ellipse([492,238,522,268],fill=(226,196,164))
d.polygon([(478,268),(538,268),(546,360),(470,360)],fill=(26,28,38))  # dark coat
d.line([(532,282),(584,238)],fill=(26,28,38),width=10)
d.polygon([(578,196),(640,186),(646,240),(584,250)],fill=SIL,outline=(140,146,156),width=2)
d.polygon([(586,204),(632,196),(636,232),(590,240)],fill=(20,28,62))
d.ellipse([606,214,620,228],fill=APR)
# second figure bent over the camera box
d.ellipse([452,206,478,232],fill=(226,196,164))
d.polygon([(440,232),(492,226),(500,286),(446,292)],fill=(30,30,42))
d.line([(486,240),(446,196)],fill=(30,30,42),width=9)
# table between them: star charts weighted with a stone, plate box lid ajar, envelopes
d.rectangle([560,352,760,364],fill=(90,70,48))
d.rectangle([576,364,590,420],fill=(70,54,36)); d.rectangle([724,364,738,420],fill=(70,54,36))
d.rectangle([574,336,690,354],fill=(238,240,242))
for _ in range(22):
    x,y=random.uniform(580,684),random.uniform(339,351); d.point((x,y),fill=(40,48,90))
d.ellipse([616,330,646,346],fill=(105,103,108))
d.rectangle([700,330,758,352],fill=(80,62,40)); d.polygon([(700,330),(758,330),(770,318),(712,318)],fill=(96,76,48))
for i in range(3): d.rectangle([574+i*16,318,586+i*16,336],fill=(232,228,214),outline=(170,170,160))
img.save(HERE+'/banner.png')
print('saved banner')
