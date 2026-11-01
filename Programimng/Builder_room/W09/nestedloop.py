h = 0
ls = []
while h<24:
    m = 0
    while m<60:
        s = 0
        hr = str(h)
        mi = str(m)
        if h < 10:
            hr = "0"+hr
        if m < 10:
            mi = "0"+mi
        while s<60:
            ss = str(s)
            if s < 10:
                ss = "0"+ss
            print(f"{hr}:{mi}:{ss}")  
            s+=1
        m+=1
    h+=1

