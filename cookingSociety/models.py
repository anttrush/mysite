from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=20)
    req1 = models.IntegerField(default=0)
    req2 = models.IntegerField(default=0)
    req3 = models.IntegerField(default=0)
    req4 = models.IntegerField(default=0)
    req5 = models.IntegerField(default=0)
    req6 = models.IntegerField(default=0)
    req = [req1, req2, req3, req4, req5, req6] # [炒,烤,煮,蒸,炸,切]

    def __str__(self):
        res = self.name + ' :' + ' 炒-'+str(self.req1) + ' 烤-'+str(self.req2) + ' 煮-'+str(self.req3) + ' 蒸-'+str(self.req4) + ' 炸-'+str(self.req5) + ' 切-'+str(self.req6)
        '''reqnames = ['炒','烤','煮','蒸','炸','切']
        for i in range(6):
            if self.req[i] > 0:
                res += " " + reqnames[i] + ":" + str(self.req[i])'''
        return res

    def getREQ(self):
        return self.req

class Cooker(models.Model):
    name = models.CharField(max_length=20)
    skill1 = models.IntegerField(default=0)
    skill2 = models.IntegerField(default=0)
    skill3 = models.IntegerField(default=0)
    skill4 = models.IntegerField(default=0)
    skill5 = models.IntegerField(default=0)
    skill6 = models.IntegerField(default=0)
    skill = [skill1, skill2, skill3, skill4, skill5, skill6] # [炒,烤,煮,蒸,炸,切]

    def __str__(self):
        res = self.name + ' :' + ' 炒-'+str(self.skill1) + ' 烤-'+str(self.skill2) + ' 煮-'+str(self.skill3) + ' 蒸-'+str(self.skill4) + ' 炸-'+str(self.skill5) + ' 切-'+str(self.skill6)
        '''reqnames = ['炒','烤','煮','蒸','炸','切']
        for i in range(6):
            res += " " + str(reqnames[i]) + ":" + str(self.skill[i])'''
        return res

    def ableCookSupper(self, dish):
        for index in range(6):
            self.skill[index] += 100
            flag = True
            for i in range(6):
                if dish.req[i] * 4 > self.skill[i]:
                    flag = False
            self.skill[index] -= 100
            if flag:
                return True
        return False