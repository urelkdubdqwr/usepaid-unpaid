#!/usr/bin/env python3
"""PAID signature beat — 100 BPM, Am-F-C-G, pure stdlib synthesis (zero samples). Run: python3 beat.py -> beat_final.wav"""
import wave, math, struct
SR=22050; BPM=100; beat=60/BPM; secs=26.0
N=int(SR*secs); buf=[0.0]*N
def add(t0,d,f,g,decay=0.0):
    i0=int(t0*SR); n=int(d*SR)
    for k in range(n):
        if i0+k>=N: break
        t=k/SR
        e=math.exp(-decay*t) if decay else (1.0 if t<d*0.8 else max(0.0,(d-t)/(d*0.2)))
        buf[i0+k]+=g*e*math.sin(2*math.pi*f*t)
def kick(t0):
    i0=int(t0*SR); n=int(0.14*SR); ph=0.0
    for k in range(n):
        if i0+k>=N: break
        t=k/SR; ph+=2*math.pi*(110*math.exp(-20*t)+45)/SR
        buf[i0+k]+=0.85*math.exp(-18*t)*math.sin(ph)
prog=[220.0,174.61,261.63,196.0]
arp=[[440,523.25,659.25,523.25],[349.23,440,523.25,440],[523.25,659.25,783.99,659.25],[392,493.88,587.33,493.88]]
for s in range(0,int(secs//beat)+1):
    t=s*beat
    if s%2==0: kick(t)
    bar=int(t//(4*beat))%4
    add(t,beat*0.92,prog[bar]/2,0.30,decay=3.0)
    add(t,beat*0.92,prog[bar],0.16,decay=3.0)
for s in range(0,int(secs/(beat/2))+1):
    t=s*beat/2; bar=int(t//(4*beat))%4
    add(t,beat*0.4,arp[bar][s%4],0.12,decay=6.0)
    if s%2: add(t,0.03,6000+(s%3)*300,0.025,decay=30)
for f,i in [(783.99,0),(659.25,1),(523.25,2),(587.33,3),(659.25,4),(523.25,6),(493.88,7)]:
    add(16.0+i*beat,beat*0.9,f,0.20,decay=2.5)
mx=max(abs(x) for x in buf); sc=0.88/mx
with wave.open('beat_final.wav','wb') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b''.join(struct.pack('<h',int(max(-1,min(1,x*sc))*32767)) for x in buf))
print('beat_final.wav', N/SR, 's')
