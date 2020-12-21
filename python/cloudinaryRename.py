import re
import cloudinary
import cloudinary.uploader

cloudinary.config(
  cloud_name = "ddghc4l09",
  api_key = "567915225657993",
  api_secret = "RtYLkOIc-Yn-RzjLSOJcnZEWZhM"
)
   
class Cloudinary_Result:
    extractionLimit = 500
    #Get url1 and 2 are "http://res.cloudinary.com/cloud_name/url1/url2/.../"
    def __init__(self, fldPth, getkey, url1='image', url2='upload'):
        self.num         = 0
        self.fldPth      = fldPth
        self.getkey      = getkey
        self.url1        = url1
        self.url2        = url2
        self.next_val    = ''
        self.limitBreak  = ''
        self.res = '' 
        self._result()
        self.ids = []

    def _result(self):
        self.res = cloudinary.api.resources(
                resource_type = self.url1,
                type          = self.url2,
                prefix        = self.fldPth,
                max_results   = self.extractionLimit,
                next_cursor   = self.limitBreak
              )
        self.limitBreak  = self.res.get("next_cursor")

    def reqestAssets(self):
        while True:
             for img in self.res["resources"]:
                 #self.num += 1
                 #print('{: <4}'.format(self.num)+':', img.get(self.getkey))
                 self.ids.append(img.get(self.getkey))
             
             if self.res.get("next_cursor"):
                 self.res = self._result()
             else:
                 break   

names = [
         '2018/2018102919133600-C616B031331154665D639EF16DA76BC0',
         '2018/2018102919144000-C616B031331154665D639EF16DA76BC0',
         '2018/2018102919370900-C616B031331154665D639EF16DA76BC0'
]

num = 2
for name in names:
    rename = '2018/1029fig' + str(num)
    cloudinary.uploader.rename(name, rename)
    num = num + 1


#c = Cloudinary_Result("2018/", "public_id", 'image')
#c.reqestAssets() 
#for name in c.ids:
#    if re.search('_', name) and not re.search('canva-photo-editor', name):
#        rename = name[:(name.rfind('_'))]
        #rename = rename.replace("old2018/", '')
        #cloudinary.uploader.rename(name, rename, resource_type=c.url1)
#        print("before : %s \n"
#              "after  : %s \n\n" 
#              % (name, rename) 
#            )
#    else:
#        continue
