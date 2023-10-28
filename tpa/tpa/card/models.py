from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=200)
    text_content = models.TextField(blank=True, null=True) # 텍스트 내용
    url = models.TextField(blank=True, null=True) # url 내용
    image = models.ImageField(upload_to='cards/images/', blank=True, null=True) # 이미지
    isPreparing = models.BooleanField(default=True)
    isGoods = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    def __str__(self):
        return self.title