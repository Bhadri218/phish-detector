def convertion(url,prediction):
    name = []
    if(prediction==1):
        return [url,"Safe","Continue","1"]
    else:
        return [url,"Not Safe","Still want to Continue"]