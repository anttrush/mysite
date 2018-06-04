from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=20)
    req = [models.IntegerField()]*6 # [炒,烤,煮,蒸,炸,切]

    def __str__(self):
        res = self.name
        reqnames = ['炒','烤','煮','蒸','炸','切']
        for i in range(6):
            if self.req[i] > 0:
                res += " " + reqnames[i] + ":" + str(self.req[i])
        return res

    def getREQ(self):
        return self.req

class Cooker(models.Model):
    name = models.CharField(max_length=20)
    skill = [models.IntegerField()]*6 # [炒,烤,煮,蒸,炸,切]

    def __str__(self):
        res = self.name
        reqnames = ['炒','烤','煮','蒸','炸','切']
        for i in range(6):
            res += " " + reqnames[i] + ":" + str(self.skill[i])
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