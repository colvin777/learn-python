'''
Created on 

@author: haoweizh
'''
import urllib.request                                                                                                                     
import urllib.parse                                                                                                                       
import re                                                                                                                                 
import urllib.request,urllib.parse,http.cookiejar       



                                                                                                                                          
def getHtml(url):                                                                                                                         
    cj=http.cookiejar.CookieJar()                                                                                                         
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))      
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),('Cookie','4564564564564564565646540')]                                                           
                                                                                                                                          
    urllib.request.install_opener(opener)                                                                                                 
                                                                                                                                          
    html_bytes = urllib.request.urlopen( url ).read()                                                                                     
    html_string = html_bytes.decode( 'utf-8' )                                                                                            
    return html_string                                                                                                                    
                                                                                                                                          
#url = http://zst.aicai.com/ssq/openInfo/                                                                                                 
                                                                    
html = getHtml("http://1.hd.mi.com/detail?pid=88058798008989&product_id=2170800024")                                                                                      
#<table class="fzTab nbt"> </table>                                                                                                       
                                                                                                                                          
table = html[html.find('<table class="fzTab nbt">') : html.find('</table>')]                                                              
#print (table)                                                                                                                            
#<tr onmouseout="this.style.background=''" onmouseover="this.style.background='#fff7d8'">                                                 
#<tr \r\n\t\t                  onmouseout=                                                                                                
tmp = table.split('<tr \r\n\t\t                  onmouseout=',1)                                                                          
#print(tmp)                                                                                                                               
#print(len(tmp))                                                                                                                          
trs = tmp[1]                                                                                                                              
tr = trs[: trs.find('</tr>')]                                                                                                             
#print(tr)                                                                                                                                
number = tr.split('<td   >')[1].split('</td>')[0]                                                                                         
print(number + 'Number:',end='')                                                                                                     
redtmp = tr.split('<td  class="redColor sz12" >')                                                                                         
reds = redtmp[1:len(redtmp)-1]#                                                                      
#print(reds)                                                                                                                              
for redstr in reds:                                                                                                                       
    print(redstr.split('</td>')[0] + ",",end='')                                                                                          
print('basketball:',end='')                                                                                                                    
blue = tr.split('<td  class="blueColor sz12" >')[1].split('</td>')[0]                                                                     
print(blue)                                                                                                                               
