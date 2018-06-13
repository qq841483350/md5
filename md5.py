#coding:utf8
__author__="liyatao"
#字符串加密，32位小，参考：http://tool.chinaz.com/tools/md5.aspx
import hashlib,time,types
def md5(str_text):
    m= hashlib.md5()  # 创建md5对象
    m.update(str_text)
    result=m.hexdigest()
    print('MD5加密前为 ：' + str_text)
    print('MD5加密后为 ：' +result)

if __name__=="__main__":
    #待加密信息
    sign="123456支付宝"
    md5(sign)
