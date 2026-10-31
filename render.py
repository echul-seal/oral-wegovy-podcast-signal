# Rebuild v1 (Python 3.13, Pillow, OpenCV)
from PIL import Image, ImageDraw, ImageFont
import cv2, numpy as np
W,H,F,N=480,854,12,84
vals=[7,3,3,3]; dates=["JAN 12","MAR 18","MAY 21","JUN 23"]
reg="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
bold="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def ft(n,b=False): return ImageFont.truetype(bold if b else reg,n)
out=cv2.VideoWriter("oral_wegovy_podcast_signal.mp4",cv2.VideoWriter_fourcc(*"mp4v"),F,(W,H))
for frame in range(N):
    t=frame/(N-1); im=Image.new("RGB",(W,H),(9,15,28)); d=ImageDraw.Draw(im)
    for y in range(H):
        c=int(18+20*y/H); d.line((0,y,W,y),fill=(9,c,35+int(25*y/H)))
    d.text((30,54),"PODCAST INDEX",font=ft(13,True),fill=(115,210,190))
    d.text((30,86),"Oral Wegovy",font=ft(40,True),fill=(242,246,247))
    d.text((31,133),"a sudden January signal, then a quieter tail",font=ft(15),fill=(157,177,192))
    L,R,Top,B=42,441,365,630
    d.line((L,B,R,B),fill=(62,95,110),width=2)
    reveal=(t-.23)/.55
    for i,v in enumerate(vals):
        x=L+43+i*96; q=min(1,max(0,(reveal-i*.18)/.22)); h=(B-Top)*v/8*q
        d.rounded_rectangle((x,B-h,x+56,B),10,fill=(89+int(55*i/3),218-int(35*i/3),183-int(25*i/3)))
        if q>.8:
            d.text((x+14,B-h-25),str(v),font=ft(18,True),fill=(230,246,240))
            d.text((x-3,B+14),dates[i],font=ft(10,True),fill=(158,184,191))
    d.text((30,805),"EXA-TRACKED PODCAST SURFACE  /  31 OCT 2026",font=ft(10,True),fill=(94,135,143))
    out.write(cv2.cvtColor(np.array(im),cv2.COLOR_RGB2BGR))
out.release()
