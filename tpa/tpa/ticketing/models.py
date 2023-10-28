from django.db import models

# Create your models here.

class Point(models.Model):
    x = models.FloatField()
    y = models.FloatField()

class Grade(models.Model):
    gradeId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=20)  # 예: "rgb(209, 80, 80)"
    price = models.IntegerField()

    def __str__(self):
        return str(self.gradeId) + "/" + self.name
    
class Block(models.Model):
    blockId = models.IntegerField()
    blockName = models.CharField(max_length=255)
    cornerPoints = models.ManyToManyField(Point, related_name='blocks_with_corner')
    linkedPoint = models.OneToOneField(Point, on_delete=models.CASCADE, related_name='block_with_linked', null=True)
    vectorPoint = models.OneToOneField(Point, on_delete=models.CASCADE, related_name='block_with_vector', null=True)
    grade = models.ManyToManyField(Grade, related_name='blocks_with_grade')
    def __str__(self):
        return self.blockName


class Seat(models.Model):
    logicalSeatId = models.IntegerField()
    gradeId = models.IntegerField()
    cornerPoints = models.JSONField()
    position = models.JSONField()
    rowIdx = models.IntegerField()
    colIdx = models.IntegerField()
    mapInfo = models.CharField(max_length=255)
    seatCount = models.IntegerField()
    linkedId = models.IntegerField()
    blockId = models.IntegerField()
    sortMapInfo = models.CharField(max_length=255)
    area = models.JSONField()
    sectionId = models.IntegerField()
    def __str__(self):
        return str(self.blockId)
    
class grid(models.Model):
    key = models.CharField(max_length=255)
    seat = models.ManyToManyField(Seat, related_name='grids_with_seat')

class Baseball(models.Model):
    name = models.CharField(max_length=255)
    eng = models.CharField(max_length=255,null=True)
    blocks = models.ManyToManyField(Block, related_name='baseball_with_blocks', null=True)
    grade = models.ManyToManyField(Grade, related_name='baseball_with_grade', null=True)
    imageUrlThumnail = models.ImageField(upload_to='ticketing/baseball/images/', blank=True, null=True) 

class Football(models.Model):
    name = models.CharField(max_length=255)
    eng = models.CharField(max_length=255,null=True)
    blocks = models.ManyToManyField(Block, related_name='football_with_blocks', null=True)
    grade = models.ManyToManyField(Grade, related_name='football_with_grade', null=True)
    imageUrlThumnail = models.ImageField(upload_to='ticketing/football/images/', blank=True, null=True) 


class ItSeatTypes(models.Model):
    typeName = models.CharField(max_length=255)
    color = models.CharField(max_length=20)  # 예: "rgb(209, 80, 80)"

class ItFigure(models.Model):
    shape = models.CharField(max_length=255)
    coords = models.CharField(max_length=255)

class ItSeatDetail(models.Model):
    seatNumber = models.CharField(max_length=255)
    left = models.IntegerField()
    top = models.IntegerField()
    rb = models.BooleanField(default=False)
    seatInfo = models.CharField(max_length=255, null=True)
    seatType = models.OneToOneField(ItSeatTypes, on_delete=models.CASCADE, related_name='seatdetail_with_seattype', null=True)

class ItSeatRanges(models.Model):
    seatNumber = models.CharField(max_length=255)
    figure = models.OneToOneField(ItFigure, on_delete=models.CASCADE, related_name='seatrange_with_figure', null=True)
    seatDetail = models.ManyToManyField(ItSeatDetail, related_name='seatrange_with_seatdetail', null=True)

class ItEvent(models.Model):
    eventName = models.CharField(max_length=255)
    venueName = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    placeName = models.CharField(max_length=255)
    seatRange = models.ManyToManyField(ItSeatRanges, related_name='event_with_seatrange', null=True)
    seatType = models.ManyToManyField(ItSeatTypes, related_name='event_with_seattype', null=True)

