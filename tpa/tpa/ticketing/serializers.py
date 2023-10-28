from rest_framework import serializers
from django.db import models, IntegrityError
from .models import Point, Block, Baseball, Grade, Seat, Football


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class BlockSerializer(serializers.ModelSerializer):
    cornerPoints = PointSerializer(many=True)
    linkedPoint = PointSerializer()
    vectorPoint = PointSerializer()
    grade = GradeSerializer(many=True)
    class Meta:
        model = Block
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'
    def create(self, validated_data):
        # validated_data를 사용하여 모델 인스턴스를 생성하고 저장
        return Seat.objects.create(**validated_data)

    def find_next_available_id(self):
        # Assume the id field is an IntegerField.
        # Find the maximum id value and add 1 to it.
        last_id = Seat.objects.all().order_by('-id').first()
        if last_id:
            return last_id.id + 1
        else:
            return 1  # Assume first id is 1 when no instances exist

    def save_instance(self,data):
        serializer = SeatSerializer(data=data)
        
        if serializer.is_valid():
            next_id = self.find_next_available_id()
            instance_data = serializer.validated_data
            instance_data['id'] = next_id

            try:
                serializer.save(id=next_id)
            except IntegrityError:
                # Handle case where id has been taken while this function was processing.
                # This may include recalling the function to try again, logging an error, etc.
                pass 
        else:
            # Handle validation error
            pass

class GradeDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class BaseballSerializer(serializers.ModelSerializer):
    blocks = BlockSerializer(many=True)
    grade = serializers.SerializerMethodField()
    class Meta:
        model = Baseball
        fields = '__all__'
    
    def get_grade(self, obj):
        # Grade 객체를 딕셔너리 형태로 직렬화
        grade_objects = obj.grade.all()
        grade_data = GradeDictSerializer(grade_objects, many=True).data

        # gradeId를 key로 사용하여 딕셔너리로 변환
        grade_dict = {}
        for grade in grade_data:
            grade_dict[str(grade['gradeId'])] = grade

        return grade_dict

class FootballSerializer(serializers.ModelSerializer):
    blocks = BlockSerializer(many=True)
    grade = serializers.SerializerMethodField()
    class Meta:
        model = Football
        fields = '__all__'
    
    def get_grade(self, obj):
        # Grade 객체를 딕셔너리 형태로 직렬화
        grade_objects = obj.grade.all()
        grade_data = GradeDictSerializer(grade_objects, many=True).data

        # gradeId를 key로 사용하여 딕셔너리로 변환
        grade_dict = {}
        for grade in grade_data:
            grade_dict[str(grade['gradeId'])] = grade

        return grade_dict


from rest_framework import serializers
import random

# ... [Your previous code]

class RandomTLBaseballSerializer(serializers.ModelSerializer):
    random_seat = serializers.SerializerMethodField()
    
    class Meta:
        model = Baseball
        fields = ['name','random_seat'] # Specify any other fields you want here
    
    def get_random_seat(self, obj):
        # Get all blocks
        blocks = obj.blocks.all()
        flag = True
        # Randomly select a block
        while flag:
            random_block = random.choice(blocks)
            block_data = BlockSerializer(random_block).data
            # Get all seats from the random block
            all_seats = Seat.objects.filter(blockId=random_block.blockId)
            
            # Check if there are any seats
            if all_seats:
                # Determine the number of random seats to select
                num_random_seats = min(len(all_seats), random.randint(1, 5))
                
                # Randomly select 1-5 seats
                random_seats = random.sample(list(all_seats), num_random_seats)
                flag = False
                return {"eng" : obj.eng, "img" : obj.imageUrlThumnail.url,  "block": block_data, "seat" : SeatSerializer(random_seats, many=True).data}


class RandomTLFootballSerializer(serializers.ModelSerializer):
    random_seat = serializers.SerializerMethodField()
    
    class Meta:
        model = Football
        fields = ['name','random_seat'] # Specify any other fields you want here
    
    def get_random_seat(self, obj):
        # Get all blocks
        blocks = obj.blocks.all()
        flag = True
        # Randomly select a block
        while flag:
            random_block = random.choice(blocks)
            block_data = BlockSerializer(random_block).data
            # Get all seats from the random block
            all_seats = Seat.objects.filter(blockId=random_block.blockId)
            
            # Check if there are any seats
            if all_seats:
                # Determine the number of random seats to select
                num_random_seats = min(len(all_seats), random.randint(1, 5))
                
                # Randomly select 1-5 seats
                random_seats = random.sample(list(all_seats), num_random_seats)
                flag = False
                return {"eng" : obj.eng, "img" : obj.imageUrlThumnail.url, "block": block_data, "seat" : SeatSerializer(random_seats, many=True).data}
