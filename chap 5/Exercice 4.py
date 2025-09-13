def trouve(text,ch):
    index=0
    for c in text:
        if c==ch:
            return index
        index+=1
    else:
       return -1 
        
