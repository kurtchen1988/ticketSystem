from django import forms

class NameForm(forms.Form):
    file = forms.FileField()
    name = forms.CharField(label='name', max_length=100)
    path = forms.CharField(label='path', max_length=100)
    updateid = forms.CharField(label='path', max_length=100)
    namesec = forms.CharField(label='path', max_length=100)
    namethird = forms.CharField(label='path', max_length=100)
    recordid = forms.CharField(label='path', max_length=100)


    '''
     <p>请上传文件：<input type="file" id="image"></p>
        <p>随意输入名字，请不要与之前输入的名字重复(任意输入值即可)：<input type="text" id="name"></p>
        <p>随意输入路径值，请不要与之前输入的路径重复(任意输入值即可)：<input type="text" id="path"></p>
        <p>请输入update_id(结算单上的备案号)：<input type="text" id="updateid"></p>
        <p>随意输入名字，请不要与之前输入的名字重复(任意输入值即可)：<input type="text" id="namesec"></p>
        <p>随意输入名字，请不要与之前输入的名字重复(任意输入值即可)：<input type="text" id="namethird"></p>
        <p>请输入record_id(同步号)：<input type="text" id="recordid"></p>
        <p><button type="submit">提交</button> <button type="reset">重新提交</button> </p>
    '''