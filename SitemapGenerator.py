from tkinter import *
import os
import urllib
import re
from urllib.request import Request, urlopen
from urllib.error import URLError

def getUrls():
    path = e1.get()
    inputPath =[1]
    if ',' in path:
        tempPath=path.split(",")
        inputPath=tempPath
    else: 
        inputPath[0]=path
    #urlList =['https://www.afrin.com/sitemap.xml','https://www.aleve.com/sitemap.xml','https://www.alkaseltzer.com/sitemap.xml','https://www.bayeraspirin.com/','https://www.buyberocca.com/sitemap.xml','','','','','','','','','','','https://www.claritin.com/sitemap.xml']
    #<loc>(https:\/\/.+)<\/loc>
    #qbfile = open(path, 'r')
    output_path="'"+e2.get()+"'"
    if e2.get()=='':
        output_path= 'C:/Temp/urlList.txt'
    urlPath = open(output_path,'w+')
    print(inputPath[0])
    #print(inputPath[1])
    for i in range(len(inputPath)):
        x=0
        req = Request(inputPath[i])
        try:
            u2 = urllib.request.urlopen(inputPath[i])
            print (u2)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('Request failed to reach the server.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
        else:
            print('Url reached')
            
        ent = Text(frame, width=50, bg='white', relief='flat')
        pageText = u2.readlines()
        for line in pageText:
            x+=1
            if (b'xmlns') in line:
                continue
            if (b'xsi') in line: 
                continue
            if (b'xsd') in line: 
                continue
            elif (b'https') in line:
                
                newString = line.decode('utf-8')
                #print(newString)

                #searchStr = '(?P<url>https?://[^\s]+)<\/loc>'
                #try:
                newString = newString.replace('\n','')
                newString = newString.replace('\t','')
                newString = newString.replace('      ','') 
                #print(newString)
                try:
                    sitemapUrl = re.search('(?P<url>https?://[^\s]+)<\/loc>', newString).group('url')
                except:
                    sitemapUrl = newString
                #except:
                    #sitemapUrl = re.search(searchStr, line.deco).group()
                
                #''.join(sitemapUrl.strip())
                sitemapUrl.lstrip()
                urlPath.write(sitemapUrl)
                urlPath.write('\n')
                #Label(frame,text=sitemapUrl,anchor="w").grid(stick="W",row=x,column=0)
                
                ent.insert(END, sitemapUrl+'\n')
                ent.config(state='normal')
                ent.pack()
            elif (b'http') in line:
                
                newString = line.decode('utf-8')
                #print(newString)

                #searchStr = '(?P<url>https?://[^\s]+)<\/loc>'
                #try:
                newString = newString.replace('\n','')
                newString = newString.replace('\t','')
                newString = newString.replace('      ','') 
                #print(newString)
                try:
                    sitemapUrl = re.search('(?P<url>http?://[^\s]+)<\/loc>', newString).group('url')
                except:
                    sitemapUrl = newString
                #except:
                    #sitemapUrl = re.search(searchStr, line.deco).group()
                
                #''.join(sitemapUrl.strip())
                sitemapUrl.lstrip()
                urlPath.write(sitemapUrl)
                urlPath.write('\n')
                #print(sitemapUrl)
                #Label(frame,text=sitemapUrl,anchor="w").grid(stick="W",row=x,column=0)
                
                ent.insert(END, sitemapUrl +'\n')
                ent.config(state='normal')
                ent.pack()
        pass
def myfunction(event):
    canvas.configure(scrollregion=(canvas.bbox("all")),width=400,height=290)

root=Tk()
sizex = 500
sizey = 500
posx  = 100
posy  = 100
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
root.title('Sitemap Extractor')
myframe=Frame(root,relief=GROOVE,width=100,height=400,bd=1)
myframe.place(x=20,y=120)

canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="both", expand=False)
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0,0),window=frame,anchor='w')
frame.bind("<Configure>",myfunction)

e1 = Entry(root, width=45)
e2 = Entry(root, width=45)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Label(root, text="Sitemap Url").grid(row=0) 
Label(root, text="Output Path").grid(row=1)
Label(root, text="'Default = C:Temp/SitemapOutput'").grid(row=2)
Label(root, text="Output:").place(x=20,y=90)
Button(root, text='Quit', command=root.quit, bg="#0a77c1",width=10).place(x=20,y=430)
Button(root, text='Get Urls', command=getUrls,bg="#13aa1e", width=10).place(x=120,y=430)
root.mainloop()