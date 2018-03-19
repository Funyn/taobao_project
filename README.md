# taobao_project
淘宝爬虫项目

start taobao_login project
  
    from taobao import TaoBao
    tb = TaoBao(username='your_username_email_or_phone_or_nickname')
    tb.login()
    登陆成功后,你只需要在你想要访问的用户信息url中添加tb.cookies即可
    用requests模块为例,登陆成功后访问个人信息页
    request.get('https://i.taobao.com/my_taobao.htm',cookies=tb.cookies) 即可
