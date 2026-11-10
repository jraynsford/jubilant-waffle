"""Extract readable text from Apple Pages/Keynote .iwa files.

Usage: unzip file.pages -d <dir>, then
  python3 -I scripts/extract_pages_text.py <dir>/Index/*.iwa <dir>/Index/Tables/*.iwa
"""
import sys,glob,re
def unsnappy(b):
    i=0;l=0;s=0
    while True:
        c=b[i];i+=1;l|=(c&0x7f)<<s;s+=7
        if c<0x80:break
    out=bytearray()
    while i<len(b):
        t=b[i];i+=1;k=t&3
        if k==0:
            n=t>>2
            if n>=60:
                nb=n-59;n=int.from_bytes(b[i:i+nb],'little');i+=nb
            n+=1;out+=b[i:i+n];i+=n
        else:
            if k==1:
                n=((t>>2)&7)+4;o=((t>>5)<<8)|b[i];i+=1
            elif k==2:
                n=(t>>2)+1;o=int.from_bytes(b[i:i+2],'little');i+=2
            else:
                n=(t>>2)+1;o=int.from_bytes(b[i:i+4],'little');i+=4
            for _ in range(n):out.append(out[-o])
    return bytes(out)
def iwa(data):
    i=0;out=b''
    while i<len(data):
        ln=int.from_bytes(data[i+1:i+4],'little');i+=4
        out+=unsnappy(data[i:i+ln]);i+=ln
    return out
for f in sys.argv[1:]:
    raw=iwa(open(f,'rb').read())
    for m in re.finditer(rb'[\x09\x0a\x20-\x7e\xc2-\xf4][\x09\x0a\x20-\x7e\x80-\xbf\xc2-\xf4]{25,}',raw):
        t=m.group().decode('utf8','ignore')
        print('---',t)
