from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import base64
import hashlib
import re

xml = '<?xml version="1.0" encoding="gbk"?><business comment="采购合同修改信息" id="BA_CONTRACT_UPDATE">      <group>   ' \
      '           <update_id>%s</update_id>              <rec_id>%s</rec_id>              <con_no>%s</con_no>              <gysmc>%s</gysmc>              ' \
      '<skyh>%s</skyh>              <yhzh>%s</yhzh>       </group>   ' \
      '    <business comment="附件信息" id="BA_CONTRACT_ACCESS">              <group>                     ' \
      '<access_id>%s</access_id>                     <access_name>%s</access_name>        ' \
      '<access_remark/>                      <access_type>%s</access_type>                      ' \
      '<access_data>%s</access_data>              </group>       </business></business>'

def index(request):
    return render(request,"index.html")

def contractChange(request):
    return render(request,"contractChange.html")

@csrf_exempt
def upload(request):
    myfile = request.FILES.get("myfile", None)
    if not myfile:
        return HttpRequest("没有上传文件信息")

@csrf_exempt
def process_form(request):

    try:
        file = request.FILES.get("file", None)
        filename = file.name
        filetype = re.findall(".*\.(.*)",filename)[0]
        # filetext = conBase64(file)
        name = request.POST["name"]
        path = request.POST["path"]
        updateid = request.POST["updateid"]
        recordid = request.POST["recordid"]
        contractno = request.POST["contractno"]
        supname = request.POST["supname"]
        bank = request.POST["bank"]
        account = request.POST["account"]
        #print(filename)
        #print(filetype)

        if not file:
            data = {'finaldata': '没有上传附件，请上传附件'}
            return render(request, 'contractChange.html', data)
        elif updateid == None or recordid== None or contractno == None or supname== None or bank== None or account==None or path==None or name==None or filename==None:
            data = {'finaldata': '有空的地方，请检查'}
            return render(request, 'contractChange.html', data)

        final = xml%(str.strip(updateid),str.strip(recordid), str.strip(contractno), str.strip(supname),str.strip(bank),str.strip(account),conMD5(path+name),conMD5(filename)+"."+filetype,str.strip(filetype),str.strip(conBase64(file).decode()) )

    except Exception as error:
        print(error)
        return render(request,'contractChange.html',{'finaldata':"出错了，先看看你有没有空的地方，如果木有，赶紧跟半土说:"+str(error)})
    data = {'finaldata':final}
    return render(request, 'contractChange.html', data)


def get_data(request):
    pass



def conMD5(data):

    return hashlib.md5(data.encode()).hexdigest()

def conBase64(file):

    with file.open("rb") as file_pro:
        return base64.b64encode(file_pro.read())
    #with open(filePath,"rb") as f:
    #    return base64.b64encode(f.read())