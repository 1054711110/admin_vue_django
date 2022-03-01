from rest_framework.permissions import AllowAny

from .models import *
from .ser import seruserlist,sergetuserList
from django.contrib.auth.backends import ModelBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username,
        "code": 200,
        "state": True
    }


class RegisterView(APIView):
    """
    用户注册, 权限是: 匿名用户可访问
    """
    # 自定义权限类
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        接收邮箱和密码, 前端校验两遍一致性, 注册成功后返回成功, 然后用户自行登录获取token
        1. 随机用户名
        2. 生成用户
        3. 设置用户密码
        4. 保存用户
        :param request:
        :return:  {'code':0,'msg':'注册成功'}
        """
        email = request.data.get('email')
        passwrod = request.data.get('password')
        username = request.data.get('username')

        if all([email, passwrod]):
            pass
        else:
            return Response({'code': 9999, 'msg': '参数不全'})
        user = User(username=username, email=email)
        user.set_password(passwrod)  # 密码加密
        user.save()
        return Response({'code': 0, 'msg': '注册成功'})


# 用户添加
class adduserList(APIView):
    # 自定义权限类

    def post(self, request):
        ser=seruserlist(data=request.data)
        print(request.data.get('state'))
        if ser.is_valid():
            ser.save()
            return Response({"msg": '成功',"code":200})

        return Response(data=ser.errors,status=400)





# 分页（局部）：自定义分页器 局部
class PageNum(PageNumberPagination):
    # 查询字符串中代表每页返回数据数量的参数名, 默认值: None
    page_size_query_param = 'page_size'
    # 查询字符串中代表页码的参数名, 有默认值: page
    page_query_param = 'page'
    # 一页中最多的结果条数
    # max_page_size = 2
# 查询用户
class getuserlist(APIView):
    def get(self, request):
        queryset = userlist.objects.all()
        print(request)
        if request.GET.get('page'):
            print(queryset)
            # 分页
            pg = PageNum()
            page_objs = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            ser = sergetuserList(instance=page_objs, many=True)  # 关联数据多条
            return Response({"code": 200, "data": ser.data, "count": userlist.objects.all().count()})
        ser = sergetuserList(instance=queryset, many=True)  # 关联数据多条
        print(userlist.objects.all().count())
        return Response({"code":200,"data":ser.data,"count":userlist.objects.all().count()})
# 删除用户
class deluser(APIView):
    def post(self,request):
        print(request.data.get('id'))
        obj=userlist.objects.all().filter(id=request.data.get('id'))
        if obj:
            print(obj)
            userlist.objects.all().filter(id=request.data.get('id')).delete()
            return Response({"code":200,"msg":'删除成功'})
        print(obj)
        return Response({"code":400,"msg":'删除失败'})
# 设置用户状态
class userstate(APIView):
    def post(self,request):
        print(request.data.get('id'),request.data.get('state'))
        userlist.objects.all().filter(id=request.data.get('id')).update(state=request.data.get('state'))
        return Response({"code": 200, "msg": '设置成功'})
# 修改用户
class updateuser(APIView):
    def post(self,request):
        userlist.objects.all().filter(id=request.data.get('id')).update(
          **request.data
        )
        print(request.data.get('name'))
        return Response({"code": 200, "msg": '修改成功'})