# -*- coding: utf-8 -*-


import requests
import re

class TaoBao:

    def __init__(self,username):
        # 淘宝登录的URL
        self.login_url = "https://login.taobao.com/member/login.jhtml"
        # 登陆前的验证,以获取cookie用于后续的登陆操作
        self.st_url = 'https://login.taobao.com/member/vst.htm?st={st}'
        # 淘宝登陆用户名
        self.username = username
        #header信息  (设置几个基本就可以的了，没必要设置这么多)
        self.loginHeaders = {
            'Host':'login.taobao.com',
            'Connection':'keep-alive',
            'Content-Length':'3357',
            'Cache-Control':'max-age=0',
            'Origin':'https://login.taobao.com',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Content-Type':'application/x-www-form-urlencoded',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer':'https://login.taobao.com/member/login.jhtml?style=mini&newMini2=true&from=alimama&redirectURL=http%3A%2F%2Flogin.taobao.com%2Fmember%2Ftaobaoke%2Flogin.htm%3Fis_login%3d1&full_redirect=true&disableQuickLogin=true',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
        }
        #可重复使用的ua,可以使用抓包软件在实现一次登陆之后获得
        self.ua = '107#ssPxCsS9stStAsNzPuRrXzT1lnIygOHxkKFXvIZd0ssV7XG9lu8dDXqX6r1LpV8VrXhXGIZd8syxxXGh/eEtXKZA6n1y9uG9V8qXPfZZgPdvVvJZ6ajfsYvxQy/y6/RQntw+iHCXetHNrmSSviPRN/iyhtOE4GrTCV6+Ws5xmWwXo9Lqr+pNk304Nedrewo+NLnOXIvuAZC/sbR1NSCXXQJWbLcmQKXlE8TOlXlkXFFQPcWEfJXlllEXIL1N1XFX+4EPl0fuXEnoVEp7yyrx86JWhDAAQTuzeegJG/gI8Kl8+B/LyyVA3TI3cBfddLl9FaQgC3idCJ+Lg9VG7BQbZyI3cBfddmrQtuDr8AnyudqK2lWB7yEmoxxoE0B8DmhBqWTht/Kco03n7EHj7EEgtfZ8fJahDvQjbeydhej13mXKBQMD7T+2hvIex2kX0vpyt3nErCi/uiyOgTVkJ2eitgdXv7Br8deewC/H3oCHIfub2BCWmDHnt01ql58jbgyVqnQtZY3jwZub25Cnkvy6ZckGFJGRIZQyhCOFbn9186eWgKQH6y/7hZRvcvAZl6giaunwe+9186eWgKQzyii/8xNIvJ7f1dqHCVCEuWnEukW27lOV2EC/32sC1kPwEvh+qqiowwpnd9OnsXHBByQnC5d8Zi0YvmgYtCHGqqjx3yEy7jMBsxhkucwSZZIuffQja/nIGnFq86yy7jMBsXuf8BNaQJxGI1+2wNj/G/pu819HRggOBDedGf0CdBURIvpjeeghlalF9BQLmEuJs1Hk8Q1+bKcRQFD7IIm3rN/DPKJMP74dI/3XXlx+bLZ='
        #将你输入的密码经过算法计算后提交,暂时不知道如何从js中获取,只能用笨方法从正确登陆后的表单中提取了
        self.TPL_password2 = '7b322a0a66a49034d3b063f091d68b77212e8d23e1e78ec2d6a40193ef7f778e8429207d0310c278c529bd91a09be0323b9c49edfca1d3641c01de3a3abaccb994b992435092e7039d866e3d339fd2209377886b6ab9fecf8e30ef5547a52197729484c6c13b410c3c60991db493c8371aeb56a6c9d9d47078254fbd20aaa791'
        #POST提交页面时所提交的表单数据
        self.post = {
            'TPL_username':self.username,
            'TPL_password': '',
            'ncoSig': '',
            'ncoSessionid': '',
            'ncoToken': '35afb8c178caecc65d4db8d0cdcf55cb63316049',
            'slideCodeShow': 'false',
            'useMobile': 'false',
            'lang': 'zh_CN',
            'newlogin': '0',
            'loginsite': '0',
            'TPL_redirect_url': "https://i.taobao.com/my_taobao.htm?",
            'from': 'tb',
            'fc': 'default',
            'style': 'default',
            'css_style': '',
            'keyLogin': 'false',
            'qrLogin': 'true',
            'newMini': 'false',
            'newMini2': 'false',
            'tid': '',
            'loginType': '3',
            'minititle': '',
            'minipara': '',
            'pstrong': '',
            'sign': '',
            'need_sign': '',
            'isIgnore': '',
            'full_redirect': '',
            'sub_jump': '',
            'popid': '',
            'callback': '',
            'guf': '',
            'not_duplite_str ': '',
            'need_user_id': '',
            'poy': self.TPL_password2,
            'gvfdcname': '10',
            'gvfdcre':'68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D61317A30392E322E3735343839343433372E372E3333633532653864725951795A5926663D746F70266F75743D7472756526726564697265637455524C3D6874747073253341253246253246627579657274726164652E74616F62616F2E636F6D25324674726164652532466974656D6C6973742532466C6973745F626F756768745F6974656D732E68746D253346',
            'from_encoding': '',
            'sub': '',
            'TPL_password_2':self.TPL_password2,
            'loginASR':'1',
            'loginASRSuc':'1',
            'allp': '',
            'oslanguage': 'zh-CN',
            'sr': '1920*1080',
            'osVer': 'windows|6.1',
            'naviVer': 'chrome|64.03282186',
            'osACN': 'Mozilla',
            'osAV': '5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'osPF': 'Win32',
            'appkey': '00000000',
            'nickLoginLink': '',
            'mobileLoginLink': 'https://login.taobao.com/member/login.jhtml?redirectURL=https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm?&useMobile=true',
            'showAssistantLink': '',
            'um_token': 'HV01PAAZ0b8705a865692b795aaf7d1b0022d8c0',
            'ua': self.ua
        }
        #设置cookie
        self.cookies = {}
        #请求登录
        print('-------请求登陆-------')

    def _get_st_token_url(self):
        response = requests.post(self.login_url, self.post, self.loginHeaders,cookies=self.cookies)
        content = response.content.decode('gbk')
        st_token_url_re = re.compile(r'<script src=\"(.*)\"><\/script>')
        match_url = st_token_url_re.findall(content)
        if match_url:
            st_token_url = match_url[0]
            return st_token_url
        else:
            print('请检查是否匹配成功')

    def _get_st_token(self):
        st_token_url = self._get_st_token_url()
        st_response = requests.get(st_token_url)
        st_response_content = st_response.content.decode('gbk')
        st_token_re = re.compile(r'"data":{"st":"(.+)"}')
        match_st_token_list = st_token_re.findall(st_response_content)
        if match_st_token_list:
            st = match_st_token_list[0]
            return st
        else:
            print('请检查是否匹配成功')


    def login_by_st(self,):
        st = self._get_st_token()
        st_url =self.st_url.format(st=st)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Host': 'login.taobao.com',
            'Connection': 'Keep-Alive'
        }
        response = requests.get(st_url, headers=headers)
        content = response.content.decode('gbk')
        self.cookies = response.cookies   #这一步是必须要做的
        # 检测结果，看是否登录成功
        pattern = re.compile('top.location.href = "(.*?)"', re.S)
        match = re.search(pattern, content)
        if match:
            print(u'登录网址成功')
            return match
        else:
            print(u'登录失败')
            return False

    def login(self):
        try:
            verified_url = self.login_by_st()
            # 此时的response将会是你的个人信息的页面,后续要访问的关于用户的url就携带self.cookies就可以正确访问了,在登陆的时候有时候会出现验证码,验证码部分我准备使用phantomJS解决
            response = requests.get(verified_url,cookies=self.cookies)

            # ——————————————————————————
            # response1 = requests.get('https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm')
            # response2 = requests.get('https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm',cookies=self.cookies)
            # print(response1.content.decode('gbk')) #不携带self.cookie的访问将会引导至登录页面
            # print('--------------------------')
            # print(response2.content.decode('gbk')) #携带self.cookie的访问将会引导至对应的页面
            # ———————————————————————————
        except TimeoutError as e:
            print('链接超时')



# t = TaoBao(username='13538022816')
# t.main()
