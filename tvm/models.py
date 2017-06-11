from django.db import models

# Create your models here.
class TVM(models.Model):
    PeriodTime1 = u'100000-110000'
    PeriodTime2 = u'130000-140000'
    PeriodTime3 = u'093000-100000'
    PeriodTime4 = u'140000-150000'
    dict_Name = {0:'360自行车',1:'VR',2:'全息音效'}
    Name_Level = (
         (u'360',u'360自行车'),
         (u'VR',u'VR'),
         (u'FULLSOUND',u'全息音效'),
    )
    Period_Level = (
         (PeriodTime1, PeriodTime1),
         (PeriodTime2, PeriodTime2),
         (PeriodTime3, PeriodTime3),
         (PeriodTime4, PeriodTime4),
    )
    name = models.CharField(choices = Name_Level,verbose_name = '项目名称',null = False,max_length=20) # 名称
    datetime = models.DateField(max_length = 10) #日期
    date = models.CharField(max_length = 20,default = '20101010')
    SellTimePeriod = models.CharField(choices = Period_Level,verbose_name = '开放时间',null= False,max_length = 30) # 时间段
    TicketNum = models.IntegerField() # 余票数量

    #python2使用__unicode__,python3使用__str__
    def __str__(self):
	#if (name == 0)
        return self.name
        #return self.dict_Name[int(self.name)]
        #if (name == 1)
        # return self.
    class Meta:
        ordering = ['-name']
