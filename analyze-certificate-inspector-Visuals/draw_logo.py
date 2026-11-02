#!/usr/bin/env python3
"""analyze-certificate-inspector logo: one glass comet photograph plate in its silver holder, name in Athiti below."""
import random
from PIL import Image, ImageDraw, ImageFont
random.seed(7)
HERE=__file__.rsplit('/',1)[0]
W,H=960,700
ALT=(24,34,72); APR=(244,176,110); CIR=(244,246,248); SIL=(193,199,209)
img=Image.new('RGB',(W,H),CIR); d=ImageDraw.Draw(img,'RGBA')
# plate tilted slightly toward the viewer: holder drawn as a shallow trapezoid
plate=[(268,66),(700,44),(716,442),(252,466)]
glass=[(292,92),(678,72),(690,418),(278,440)]
d.polygon(plate,fill=SIL,outline=(138,144,154),width=3)
d.polygon(glass,fill=(18,26,58))
# silver clips gripping the top edge
for x in (330,610): d.rectangle([x,34,x+44,86],fill=(214,220,228),outline=(140,146,156),width=2)
# wooden base edge, worn and dark
d.polygon([(252,466),(716,442),(716,478),(252,502)],fill=(74,54,34))
d.line([(270,482),(700,458)],fill=(96,74,46),width=3)
# scatter of small silver stars fixed in the emulsion
def inside(x,y): return 300<x<680 and 84<y<430
pts=[]
while len(pts)<44:
    x,y=random.uniform(300,678),random.uniform(84,428)
    if inside(x,y): pts.append((x,y))
for x,y in pts: d.ellipse([x-2,y-2,x+2,y+2],fill=(226,232,240))
# the comet burned into the plate: bright head low at left, tail streaming up and right
hx,hy=352,368
for i in range(30):
    t=i/30; x=hx+t*310; y=hy-t*262
    d.line([(x,y),(x+22,y-15)],fill=(244,176,110,int(190*(1-t)+30)),width=max(1,int(30*(1-t)+2)))
for i in range(10):
    t=i/10; d.line([(hx,hy),(hx+296*t,hy-250*t+22*t)],fill=(246,222,186,110),width=max(1,int(8*(1-t))))
d.ellipse([hx-19,hy-19,hx+19,hy+19],fill=(246,248,250))
d.ellipse([hx-10,hy-10,hx+10,hy+10],fill=(255,255,255))
# name below the plate, Athiti in altitude blue on cirrus white, silver dots between the words
f=ImageFont.truetype(HERE+'/fonts/Athiti.ttf',43)
parts=['analyze','certificate','inspector']
dotw=18
widths=[d.textlength(p+'-',font=f) for p in parts[:2]]+[d.textlength(parts[2],font=f)]
total=sum(widths)+dotw*2; x=(W-total)/2
for i,p in enumerate(parts):
    seg=p+('-' if i<2 else '')
    d.text((x,556),seg,font=f,fill=ALT); x+=widths[i]
    if i<2:
        d.ellipse([x+3,582,x+13,592],fill=SIL); x+=dotw
img.save(HERE+'/logo.png')
img.resize((64,47)).save(HERE+'/scratch/logo64-ship.png')
print('saved logo')
