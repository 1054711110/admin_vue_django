# -*- coding: utf-8 -*-
from rest_framework import serializers
from app01.models import User,userlist


class APIViewUserInfo(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)       # 主键序列化
    # 第一：普通字段序列化
    # user = serializers.CharField(label='名称', max_length=20)
    # pwd = serializers.CharField(label='密码')
    # tel = serializers.IntegerField(label='电话', required=False)
    # address=serializers.CharField(label='家庭地址', max_length=64)
    # time = serializers.DateTimeField(label='时间', required=False)
    # money=serializers.FloatField(label='钱', required=False)
    # # 第二：一对多字段序列化
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # # 第三：自定义显示（显示多对多）
    # xxx = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User

    # 自定义显示 多对多 字段
class seruserlist(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)  # 主键序列化

    # 第一：普通字段序列化
    name = serializers.CharField(max_length=10)
    mobile = serializers.CharField(max_length=11)
    address = serializers.CharField(max_length=64)
    state=serializers.BooleanField()
    class Meta:
        model = userlist
        fields = ('field1', 'field2')
 # 定义创建语法：ser.save()执行，就会立刻调用create方法用来创建数据
    def create(self, validated_data):
        '''validated_data: 表单或者vue请求携带的json：{"username":"zhangsan","password":"123456"}'''
        return self.Meta.model.objects.create(**validated_data)




class sergetuserList(serializers.ModelSerializer):
    """图书序列化器类"""
    class Meta:
        model = userlist
        fields = '__all__'