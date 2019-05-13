#coding=utf-8
from django.db import models

# Create your models here.

class Casetask(models.Model):
    cid = models.AutoField(primary_key=True)
    title=models.CharField(max_length=150,verbose_name="标题",default="")
    creater=models.CharField(max_length=20,verbose_name="创建人",default="")
    email = models.EmailField(verbose_name="邮箱",default="")
    run_time=models.CharField(max_length=20,verbose_name="运行时间",default="")
    case_path=models.CharField(max_length=100,verbose_name="路径",default="")
    desc=models.TextField(verbose_name="描述",default="")
    timestamp=models.DateTimeField(default="")
    class Meta:
        ordering = ('-timestamp',)

class Runlog(models.Model):
    id = models.AutoField(primary_key=True)
    cid=models.CharField(max_length=20,verbose_name="任务id",default="")
    report_title=models.CharField(max_length=150,verbose_name="报告名称",default="")
    report_path=models.CharField(max_length=150,verbose_name="报告路径",default="")
    desc=models.TextField(verbose_name="报告描述",default="")
    timestamp=models.DateTimeField(default="")