import numpy as np
import base64
import json
def mask_union(data):
       json_from_post = data
       base = json_from_post.get("data")
       mask=json_from_post.get("mask")
       img=np.frombuffer(base64.b64decode(base),np.uint8)
       img=np.resize(img,mask)
#        img=np.reshape(img, (256, 256))
       united64 = str(base64.b64encode(img))
       united64=united64.split("base64")[1]
       return united64

