#coding:utf8
__author__="liyatao"
#python字符串md5加密，32位小，参考：http://tool.chinaz.com/tools/md5.aspx
import hashlib,time,types
def md5(str_text):
    m= hashlib.md5()  # 创建md5对象
    # Tips
    # 此处必须声明encode
    # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
    m.update(str_text.encode('utf8'))
    result=m.hexdigest()  #32位小
    print(u'MD5加密前为 ：' + str_text)
    print(u'MD5加密后为 ：' +result)

if __name__=="__main__":
    #待加密信息
    sign="123456"
    md5(sign)
