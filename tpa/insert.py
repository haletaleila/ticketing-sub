import json
import os
import csv
from uuid import uuid4
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
import django
django.setup()
from django.core.files import File
from PIL import Image as ING
from tpa.ticketing.models import Block,Point
from django.core.files.temp import NamedTemporaryFile
from botocore.exceptions import NoCredentialsError
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from tpa.ticketing.models import Seat
from tpa.ticketing.serializers import SeatSerializer
json_data = [
    {
                        "blockId": 100695,
                        "blockName": "103블록",
                        "cornerPoints": [{
                            "x": 5894.0,
                            "y": 3588.0
                        }, {
                            "x": 5796.0,
                            "y": 3759.0
                        }, {
                            "x": 6232.0,
                            "y": 4010.0
                        }, {
                            "x": 6290.0,
                            "y": 3915.0
                        }, {
                            "x": 6068.0,
                            "y": 3786.0
                        }, {
                            "x": 6110.0,
                            "y": 3712.0
                        }],
                        "linkedPoint": {
                            "x": 6104.0,
                            "y": 3844.0
                        },
                        "vectorPoint": {
                            "x": -0.866,
                            "y": 0.5
                        },
                        "grades": [{
                            "gradeId": 79345,
                            "remainCnt": 162,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79350,
                            "remainCnt": 4,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100696,
                        "blockName": "104블록",
                        "cornerPoints": [{
                            "x": 5785.0,
                            "y": 3775.0
                        }, {
                            "x": 5687.0,
                            "y": 3949.0
                        }, {
                            "x": 6121.0,
                            "y": 4204.0
                        }, {
                            "x": 6221.0,
                            "y": 4028.0
                        }],
                        "linkedPoint": {
                            "x": 5954.0,
                            "y": 3989.5
                        },
                        "vectorPoint": {
                            "x": -0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79345,
                            "remainCnt": 420,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79350,
                            "remainCnt": 8,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100697,
                        "blockName": "105블록",
                        "cornerPoints": [{
                            "x": 5673.0,
                            "y": 3969.0
                        }, {
                            "x": 5571.0,
                            "y": 4143.0
                        }, {
                            "x": 6008.0,
                            "y": 4398.0
                        }, {
                            "x": 6113.0,
                            "y": 4223.0
                        }],
                        "linkedPoint": {
                            "x": 5842.0,
                            "y": 4183.5
                        },
                        "vectorPoint": {
                            "x": -0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79345,
                            "remainCnt": 448,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79350,
                            "remainCnt": 8,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100698,
                        "blockName": "106블록",
                        "cornerPoints": [{
                            "x": 5561.0,
                            "y": 4162.0
                        }, {
                            "x": 5463.0,
                            "y": 4335.0
                        }, {
                            "x": 5902.0,
                            "y": 4589.0
                        }, {
                            "x": 6001.0,
                            "y": 4415.0
                        }],
                        "linkedPoint": {
                            "x": 5732.0,
                            "y": 4375.5
                        },
                        "vectorPoint": {
                            "x": -0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79345,
                            "remainCnt": 417,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79350,
                            "remainCnt": 4,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100699,
                        "blockName": "107블록",
                        "cornerPoints": [{
                            "x": 5452.0,
                            "y": 4352.0
                        }, {
                            "x": 5348.0,
                            "y": 4531.0
                        }, {
                            "x": 5792.0,
                            "y": 4788.0
                        }, {
                            "x": 5896.0,
                            "y": 4605.0
                        }],
                        "linkedPoint": {
                            "x": 5622.0,
                            "y": 4570.0
                        },
                        "vectorPoint": {
                            "x": -0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79343,
                            "remainCnt": 386,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79350,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100700,
                        "blockName": "108블록",
                        "cornerPoints": [{
                            "x": 5340.0,
                            "y": 4547.0
                        }, {
                            "x": 5252.0,
                            "y": 4726.0
                        }, {
                            "x": 5688.0,
                            "y": 4971.0
                        }, {
                            "x": 5784.0,
                            "y": 4802.0
                        }],
                        "linkedPoint": {
                            "x": 5518.0,
                            "y": 4759.0
                        },
                        "vectorPoint": {
                            "x": -0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79343,
                            "remainCnt": 212,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79350,
                            "remainCnt": 2,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100701,
                        "blockName": "109블록",
                        "cornerPoints": [{
                            "x": 5241.0,
                            "y": 4739.0
                        }, {
                            "x": 5111.0,
                            "y": 4999.0
                        }, {
                            "x": 5482.0,
                            "y": 5342.0
                        }, {
                            "x": 5681.0,
                            "y": 4985.0
                        }],
                        "linkedPoint": {
                            "x": 5396.0,
                            "y": 5040.5
                        },
                        "vectorPoint": {
                            "x": -0.866,
                            "y": 0.5
                        },
                        "grades": [{
                            "gradeId": 79343,
                            "remainCnt": 341,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79350,
                            "remainCnt": 16,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100702,
                        "blockName": "110블록",
                        "cornerPoints": [{
                            "x": 5104.0,
                            "y": 5012.0
                        }, {
                            "x": 4999.0,
                            "y": 5149.0
                        }, {
                            "x": 5339.0,
                            "y": 5492.0
                        }, {
                            "x": 5478.0,
                            "y": 5353.0
                        }],
                        "linkedPoint": {
                            "x": 5238.5,
                            "y": 5252.0
                        },
                        "vectorPoint": {
                            "x": -0.7071,
                            "y": 0.7071
                        },
                        "grades": [{
                            "gradeId": 79343,
                            "remainCnt": 107,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79350,
                            "remainCnt": 8,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100703,
                        "blockName": "111블록",
                        "cornerPoints": [{
                            "x": 4983.0,
                            "y": 5162.0
                        }, {
                            "x": 4829.0,
                            "y": 5319.0
                        }, {
                            "x": 5171.0,
                            "y": 5655.0
                        }, {
                            "x": 5328.0,
                            "y": 5508.0
                        }],
                        "linkedPoint": {
                            "x": 5078.5,
                            "y": 5408.5
                        },
                        "vectorPoint": {
                            "x": -0.7071,
                            "y": 0.7071
                        },
                        "grades": [{
                            "gradeId": 79343,
                            "remainCnt": 7,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79350,
                            "remainCnt": 8,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100704,
                        "blockName": "112블록",
                        "cornerPoints": [{
                            "x": 4818.0,
                            "y": 5327.0
                        }, {
                            "x": 4683.0,
                            "y": 5470.0
                        }, {
                            "x": 5021.0,
                            "y": 5808.0
                        }, {
                            "x": 5163.0,
                            "y": 5669.0
                        }],
                        "linkedPoint": {
                            "x": 4923.0,
                            "y": 5567.5
                        },
                        "vectorPoint": {
                            "x": -0.7071,
                            "y": 0.7071
                        },
                        "grades": [{
                            "gradeId": 79341,
                            "remainCnt": 7,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79350,
                            "remainCnt": 8,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100705,
                        "blockName": "113블록",
                        "cornerPoints": [{
                            "x": 4673.0,
                            "y": 5485.0
                        }, {
                            "x": 4558.0,
                            "y": 5651.0
                        }, {
                            "x": 4868.0,
                            "y": 5960.0
                        }, {
                            "x": 5008.0,
                            "y": 5819.0
                        }],
                        "linkedPoint": {
                            "x": 4783.0,
                            "y": 5722.5
                        },
                        "vectorPoint": {
                            "x": -0.5,
                            "y": 0.866
                        },
                        "grades": [{
                            "gradeId": 79341,
                            "remainCnt": 5,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79350,
                            "remainCnt": 6,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100706,
                        "blockName": "S-301",
                        "cornerPoints": [{
                            "x": 5849.0,
                            "y": 4813.0
                        }, {
                            "x": 5796.0,
                            "y": 4916.0
                        }, {
                            "x": 5930.0,
                            "y": 4988.0
                        }, {
                            "x": 5986.0,
                            "y": 4881.0
                        }],
                        "linkedPoint": {
                            "x": 5891.0,
                            "y": 4900.5
                        },
                        "vectorPoint": {
                            "x": -0.8829,
                            "y": 0.4695
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100707,
                        "blockName": "1루 파티석",
                        "cornerPoints": [{
                            "x": 6089.0,
                            "y": 4345.0
                        }, {
                            "x": 6226.0,
                            "y": 4414.0
                        }, {
                            "x": 5994.0,
                            "y": 4868.0
                        }, {
                            "x": 5857.0,
                            "y": 4797.0
                        }],
                        "linkedPoint": {
                            "x": 6041.5,
                            "y": 4606.5
                        },
                        "vectorPoint": {
                            "x": -0.866,
                            "y": 0.5
                        },
                        "grades": [{
                            "gradeId": 79336,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100708,
                        "blockName": "S-302",
                        "cornerPoints": [{
                            "x": 5790.0,
                            "y": 4927.0
                        }, {
                            "x": 5926.0,
                            "y": 4995.0
                        }, {
                            "x": 5872.0,
                            "y": 5103.0
                        }, {
                            "x": 5736.0,
                            "y": 5033.0
                        }],
                        "linkedPoint": {
                            "x": 5831.0,
                            "y": 5015.0
                        },
                        "vectorPoint": {
                            "x": -0.8829,
                            "y": 0.4695
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100709,
                        "blockName": "S-303",
                        "cornerPoints": [{
                            "x": 5730.0,
                            "y": 5044.0
                        }, {
                            "x": 5676.0,
                            "y": 5148.0
                        }, {
                            "x": 5808.0,
                            "y": 5220.0
                        }, {
                            "x": 5866.0,
                            "y": 5113.0
                        }],
                        "linkedPoint": {
                            "x": 5771.0,
                            "y": 5132.0
                        },
                        "vectorPoint": {
                            "x": -0.8829,
                            "y": 0.4695
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100710,
                        "blockName": "S-304",
                        "cornerPoints": [{
                            "x": 5665.0,
                            "y": 5162.0
                        }, {
                            "x": 5611.0,
                            "y": 5265.0
                        }, {
                            "x": 5745.0,
                            "y": 5338.0
                        }, {
                            "x": 5801.0,
                            "y": 5232.0
                        }],
                        "linkedPoint": {
                            "x": 5706.0,
                            "y": 5250.0
                        },
                        "vectorPoint": {
                            "x": -0.882,
                            "y": 0.4713
                        },
                        "grades": [{
                            "gradeId": 79351,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100711,
                        "blockName": "S-305",
                        "cornerPoints": [{
                            "x": 5603.0,
                            "y": 5277.0
                        }, {
                            "x": 5529.0,
                            "y": 5370.0
                        }, {
                            "x": 5640.0,
                            "y": 5471.0
                        }, {
                            "x": 5736.0,
                            "y": 5354.0
                        }],
                        "linkedPoint": {
                            "x": 5632.5,
                            "y": 5374.0
                        },
                        "vectorPoint": {
                            "x": 0.0,
                            "y": 1.0
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100712,
                        "blockName": "S-306",
                        "cornerPoints": [{
                            "x": 5517.0,
                            "y": 5385.0
                        }, {
                            "x": 5435.0,
                            "y": 5469.0
                        }, {
                            "x": 5543.0,
                            "y": 5575.0
                        }, {
                            "x": 5627.0,
                            "y": 5489.0
                        }],
                        "linkedPoint": {
                            "x": 5531.0,
                            "y": 5480.0
                        },
                        "vectorPoint": {
                            "x": -0.7771,
                            "y": 0.6293
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100713,
                        "blockName": "S-307",
                        "cornerPoints": [{
                            "x": 5423.0,
                            "y": 5479.0
                        }, {
                            "x": 5340.0,
                            "y": 5562.0
                        }, {
                            "x": 5448.0,
                            "y": 5670.0
                        }, {
                            "x": 5532.0,
                            "y": 5584.0
                        }],
                        "linkedPoint": {
                            "x": 5436.0,
                            "y": 5574.5
                        },
                        "vectorPoint": {
                            "x": -0.7771,
                            "y": 0.6293
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100714,
                        "blockName": "S-308",
                        "cornerPoints": [{
                            "x": 5332.0,
                            "y": 5572.0
                        }, {
                            "x": 5248.0,
                            "y": 5654.0
                        }, {
                            "x": 5352.0,
                            "y": 5764.0
                        }, {
                            "x": 5439.0,
                            "y": 5680.0
                        }],
                        "linkedPoint": {
                            "x": 5343.5,
                            "y": 5668.0
                        },
                        "vectorPoint": {
                            "x": -0.6691,
                            "y": 0.7431
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100715,
                        "blockName": "S-309",
                        "cornerPoints": [{
                            "x": 5238.0,
                            "y": 5664.0
                        }, {
                            "x": 5153.0,
                            "y": 5747.0
                        }, {
                            "x": 5259.0,
                            "y": 5856.0
                        }, {
                            "x": 5345.0,
                            "y": 5772.0
                        }],
                        "linkedPoint": {
                            "x": 5249.0,
                            "y": 5760.0
                        },
                        "vectorPoint": {
                            "x": -0.6816,
                            "y": 0.7317
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100716,
                        "blockName": "S-310",
                        "cornerPoints": [{
                            "x": 5144.0,
                            "y": 5754.0
                        }, {
                            "x": 5059.0,
                            "y": 5837.0
                        }, {
                            "x": 5164.0,
                            "y": 5946.0
                        }, {
                            "x": 5251.0,
                            "y": 5862.0
                        }],
                        "linkedPoint": {
                            "x": 5155.0,
                            "y": 5850.0
                        },
                        "vectorPoint": {
                            "x": -0.6816,
                            "y": 0.7317
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100717,
                        "blockName": "S-311",
                        "cornerPoints": [{
                            "x": 5051.0,
                            "y": 5846.0
                        }, {
                            "x": 4966.0,
                            "y": 5928.0
                        }, {
                            "x": 5065.0,
                            "y": 6041.0
                        }, {
                            "x": 5158.0,
                            "y": 5953.0
                        }],
                        "linkedPoint": {
                            "x": 5062.0,
                            "y": 5943.5
                        },
                        "vectorPoint": {
                            "x": -0.6816,
                            "y": 0.7317
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100718,
                        "blockName": "S-312",
                        "cornerPoints": [{
                            "x": 4956.0,
                            "y": 5937.0
                        }, {
                            "x": 4866.0,
                            "y": 6011.0
                        }, {
                            "x": 4962.0,
                            "y": 6128.0
                        }, {
                            "x": 5054.0,
                            "y": 6052.0
                        }],
                        "linkedPoint": {
                            "x": 4960.0,
                            "y": 6032.5
                        },
                        "vectorPoint": {
                            "x": -0.6816,
                            "y": 0.7317
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100719,
                        "blockName": "S-313",
                        "cornerPoints": [{
                            "x": 4853.0,
                            "y": 6023.0
                        }, {
                            "x": 4762.0,
                            "y": 6097.0
                        }, {
                            "x": 4858.0,
                            "y": 6215.0
                        }, {
                            "x": 4952.0,
                            "y": 6138.0
                        }],
                        "linkedPoint": {
                            "x": 4857.0,
                            "y": 6119.0
                        },
                        "vectorPoint": {
                            "x": -0.6816,
                            "y": 0.7317
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100720,
                        "blockName": "S-314",
                        "cornerPoints": [{
                            "x": 4751.0,
                            "y": 6108.0
                        }, {
                            "x": 4664.0,
                            "y": 6181.0
                        }, {
                            "x": 4744.0,
                            "y": 6305.0
                        }, {
                            "x": 4847.0,
                            "y": 6224.0
                        }],
                        "linkedPoint": {
                            "x": 4755.5,
                            "y": 6206.5
                        },
                        "vectorPoint": {
                            "x": -0.6691,
                            "y": 0.7431
                        },
                        "grades": [{
                            "gradeId": 79353,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100721,
                        "blockName": "S-315",
                        "cornerPoints": [{
                            "x": 4537.0,
                            "y": 6247.0
                        }, {
                            "x": 4424.0,
                            "y": 6280.0
                        }, {
                            "x": 4453.0,
                            "y": 6428.0
                        }, {
                            "x": 4591.0,
                            "y": 6389.0
                        }],
                        "linkedPoint": {
                            "x": 4507.5,
                            "y": 6337.5
                        },
                        "vectorPoint": {
                            "x": -0.2419,
                            "y": 0.9703
                        },
                        "grades": [{
                            "gradeId": 79353,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100722,
                        "blockName": "S-316",
                        "cornerPoints": [{
                            "x": 4410.0,
                            "y": 6283.0
                        }, {
                            "x": 4294.0,
                            "y": 6304.0
                        }, {
                            "x": 4319.0,
                            "y": 6454.0
                        }, {
                            "x": 4437.0,
                            "y": 6433.0
                        }],
                        "linkedPoint": {
                            "x": 4365.5,
                            "y": 6368.5
                        },
                        "vectorPoint": {
                            "x": -0.2419,
                            "y": 0.9703
                        },
                        "grades": [{
                            "gradeId": 79353,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100723,
                        "blockName": "S-320",
                        "cornerPoints": [{
                            "x": 3781.0,
                            "y": 6284.0
                        }, {
                            "x": 3754.0,
                            "y": 6433.0
                        }, {
                            "x": 3872.0,
                            "y": 6454.0
                        }, {
                            "x": 3897.0,
                            "y": 6304.0
                        }],
                        "linkedPoint": {
                            "x": 3825.5,
                            "y": 6369.0
                        },
                        "vectorPoint": {
                            "x": 0.2079,
                            "y": 0.9781
                        },
                        "grades": [{
                            "gradeId": 79353,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100724,
                        "blockName": "S-321",
                        "cornerPoints": [{
                            "x": 3655.0,
                            "y": 6247.0
                        }, {
                            "x": 3601.0,
                            "y": 6388.0
                        }, {
                            "x": 3738.0,
                            "y": 6428.0
                        }, {
                            "x": 3768.0,
                            "y": 6281.0
                        }],
                        "linkedPoint": {
                            "x": 3684.5,
                            "y": 6337.5
                        },
                        "vectorPoint": {
                            "x": 0.2079,
                            "y": 0.9781
                        },
                        "grades": [{
                            "gradeId": 79353,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100725,
                        "blockName": "S-322",
                        "cornerPoints": [{
                            "x": 3440.0,
                            "y": 6107.0
                        }, {
                            "x": 3346.0,
                            "y": 6223.0
                        }, {
                            "x": 3448.0,
                            "y": 6305.0
                        }, {
                            "x": 3528.0,
                            "y": 6181.0
                        }],
                        "linkedPoint": {
                            "x": 3437.0,
                            "y": 6206.0
                        },
                        "vectorPoint": {
                            "x": 0.6018,
                            "y": 0.7986
                        },
                        "grades": [{
                            "gradeId": 79353,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100726,
                        "blockName": "S-323",
                        "cornerPoints": [{
                            "x": 3339.0,
                            "y": 6023.0
                        }, {
                            "x": 3241.0,
                            "y": 6137.0
                        }, {
                            "x": 3333.0,
                            "y": 6215.0
                        }, {
                            "x": 3430.0,
                            "y": 6097.0
                        }],
                        "linkedPoint": {
                            "x": 3335.5,
                            "y": 6119.0
                        },
                        "vectorPoint": {
                            "x": 0.5396,
                            "y": 0.8419
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100727,
                        "blockName": "S-324",
                        "cornerPoints": [{
                            "x": 3236.0,
                            "y": 5936.0
                        }, {
                            "x": 3138.0,
                            "y": 6052.0
                        }, {
                            "x": 3229.0,
                            "y": 6128.0
                        }, {
                            "x": 3326.0,
                            "y": 6012.0
                        }],
                        "linkedPoint": {
                            "x": 3232.0,
                            "y": 6032.0
                        },
                        "vectorPoint": {
                            "x": 0.5396,
                            "y": 0.8419
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100728,
                        "blockName": "S-325",
                        "cornerPoints": [{
                            "x": 3141.0,
                            "y": 5846.0
                        }, {
                            "x": 3034.0,
                            "y": 5952.0
                        }, {
                            "x": 3126.0,
                            "y": 6041.0
                        }, {
                            "x": 3226.0,
                            "y": 5928.0
                        }],
                        "linkedPoint": {
                            "x": 3130.0,
                            "y": 5943.5
                        },
                        "vectorPoint": {
                            "x": 0.5396,
                            "y": 0.8419
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100729,
                        "blockName": "S-326",
                        "cornerPoints": [{
                            "x": 3049.0,
                            "y": 5754.0
                        }, {
                            "x": 2941.0,
                            "y": 5862.0
                        }, {
                            "x": 3027.0,
                            "y": 5946.0
                        }, {
                            "x": 3133.0,
                            "y": 5836.0
                        }],
                        "linkedPoint": {
                            "x": 3037.0,
                            "y": 5850.0
                        },
                        "vectorPoint": {
                            "x": 0.7446,
                            "y": 0.6675
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100730,
                        "blockName": "S-327",
                        "cornerPoints": [{
                            "x": 2955.0,
                            "y": 5664.0
                        }, {
                            "x": 2848.0,
                            "y": 5772.0
                        }, {
                            "x": 2933.0,
                            "y": 5856.0
                        }, {
                            "x": 3038.0,
                            "y": 5747.0
                        }],
                        "linkedPoint": {
                            "x": 2943.0,
                            "y": 5760.0
                        },
                        "vectorPoint": {
                            "x": 0.7446,
                            "y": 0.6675
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100731,
                        "blockName": "S-328",
                        "cornerPoints": [{
                            "x": 2860.0,
                            "y": 5572.0
                        }, {
                            "x": 2753.0,
                            "y": 5680.0
                        }, {
                            "x": 2838.0,
                            "y": 5764.0
                        }, {
                            "x": 2945.0,
                            "y": 5655.0
                        }],
                        "linkedPoint": {
                            "x": 2849.0,
                            "y": 5668.0
                        },
                        "vectorPoint": {
                            "x": 0.7446,
                            "y": 0.6675
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100732,
                        "blockName": "S-329",
                        "cornerPoints": [{
                            "x": 2769.0,
                            "y": 5478.0
                        }, {
                            "x": 2660.0,
                            "y": 5584.0
                        }, {
                            "x": 2744.0,
                            "y": 5670.0
                        }, {
                            "x": 2853.0,
                            "y": 5562.0
                        }],
                        "linkedPoint": {
                            "x": 2756.5,
                            "y": 5574.0
                        },
                        "vectorPoint": {
                            "x": 0.7446,
                            "y": 0.6675
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100733,
                        "blockName": "S-330",
                        "cornerPoints": [{
                            "x": 2676.0,
                            "y": 5384.0
                        }, {
                            "x": 2566.0,
                            "y": 5488.0
                        }, {
                            "x": 2648.0,
                            "y": 5575.0
                        }, {
                            "x": 2758.0,
                            "y": 5469.0
                        }],
                        "linkedPoint": {
                            "x": 2662.0,
                            "y": 5479.5
                        },
                        "vectorPoint": {
                            "x": 0.7446,
                            "y": 0.6675
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100734,
                        "blockName": "S-331",
                        "cornerPoints": [{
                            "x": 2590.0,
                            "y": 5277.0
                        }, {
                            "x": 2455.0,
                            "y": 5354.0
                        }, {
                            "x": 2554.0,
                            "y": 5476.0
                        }, {
                            "x": 2665.0,
                            "y": 5374.0
                        }],
                        "linkedPoint": {
                            "x": 2560.0,
                            "y": 5376.5
                        },
                        "vectorPoint": {
                            "x": 0.7446,
                            "y": 0.6675
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100735,
                        "blockName": "S-332",
                        "cornerPoints": [{
                            "x": 2526.0,
                            "y": 5162.0
                        }, {
                            "x": 2391.0,
                            "y": 5232.0
                        }, {
                            "x": 2447.0,
                            "y": 5339.0
                        }, {
                            "x": 2581.0,
                            "y": 5266.0
                        }],
                        "linkedPoint": {
                            "x": 2486.0,
                            "y": 5250.5
                        },
                        "vectorPoint": {
                            "x": 0.8746,
                            "y": 0.4848
                        },
                        "grades": [{
                            "gradeId": 79351,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100736,
                        "blockName": "S-333",
                        "cornerPoints": [{
                            "x": 2462.0,
                            "y": 5043.0
                        }, {
                            "x": 2327.0,
                            "y": 5114.0
                        }, {
                            "x": 2383.0,
                            "y": 5220.0
                        }, {
                            "x": 2517.0,
                            "y": 5149.0
                        }],
                        "linkedPoint": {
                            "x": 2422.0,
                            "y": 5131.5
                        },
                        "vectorPoint": {
                            "x": 0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100737,
                        "blockName": "S-334",
                        "cornerPoints": [{
                            "x": 2402.0,
                            "y": 4927.0
                        }, {
                            "x": 2265.0,
                            "y": 4996.0
                        }, {
                            "x": 2320.0,
                            "y": 5102.0
                        }, {
                            "x": 2456.0,
                            "y": 5033.0
                        }],
                        "linkedPoint": {
                            "x": 2360.5,
                            "y": 5014.5
                        },
                        "vectorPoint": {
                            "x": 0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100738,
                        "blockName": "S-335",
                        "cornerPoints": [{
                            "x": 2342.0,
                            "y": 4813.0
                        }, {
                            "x": 2207.0,
                            "y": 4880.0
                        }, {
                            "x": 2261.0,
                            "y": 4987.0
                        }, {
                            "x": 2397.0,
                            "y": 4917.0
                        }],
                        "linkedPoint": {
                            "x": 2302.0,
                            "y": 4900.0
                        },
                        "vectorPoint": {
                            "x": 0.866,
                            "y": 0.5
                        },
                        "grades": [{
                            "gradeId": 79352,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100739,
                        "blockName": "3루 파티석",
                        "cornerPoints": [{
                            "x": 2108.0,
                            "y": 4347.0
                        }, {
                            "x": 1971.0,
                            "y": 4418.0
                        }, {
                            "x": 2202.0,
                            "y": 4870.0
                        }, {
                            "x": 2339.0,
                            "y": 4800.0
                        }],
                        "linkedPoint": {
                            "x": 2155.0,
                            "y": 4608.5
                        },
                        "vectorPoint": {
                            "x": 0.8572,
                            "y": 0.515
                        },
                        "grades": [{
                            "gradeId": 79335,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100740,
                        "blockName": "중앙테이블석",
                        "cornerPoints": [{
                            "x": 4550.0,
                            "y": 5665.0
                        }, {
                            "x": 4327.0,
                            "y": 5829.0
                        }, {
                            "x": 3869.0,
                            "y": 5829.0
                        }, {
                            "x": 3646.0,
                            "y": 5665.0
                        }, {
                            "x": 3342.0,
                            "y": 5973.0
                        }, {
                            "x": 3737.0,
                            "y": 6225.0
                        }, {
                            "x": 4459.0,
                            "y": 6225.0
                        }, {
                            "x": 4854.0,
                            "y": 5973.0
                        }],
                        "linkedPoint": {
                            "x": 4098.0,
                            "y": 5945.0
                        },
                        "vectorPoint": {
                            "x": -0.5,
                            "y": 0.866
                        },
                        "grades": [{
                            "gradeId": 79327,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }, {
                            "gradeId": 79328,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100741,
                        "blockName": "116블록",
                        "cornerPoints": [{
                            "x": 3523.0,
                            "y": 5483.0
                        }, {
                            "x": 3187.0,
                            "y": 5819.0
                        }, {
                            "x": 3328.0,
                            "y": 5962.0
                        }, {
                            "x": 3639.0,
                            "y": 5650.0
                        }],
                        "linkedPoint": {
                            "x": 3413.0,
                            "y": 5722.5
                        },
                        "vectorPoint": {
                            "x": 0.7033,
                            "y": 0.7109
                        },
                        "grades": [{
                            "gradeId": 79340,
                            "remainCnt": 2,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79349,
                            "remainCnt": 6,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100742,
                        "blockName": "챔피언석",
                        "cornerPoints": [{
                            "x": 4442.0,
                            "y": 5550.0
                        }, {
                            "x": 3751.0,
                            "y": 5550.0
                        }, {
                            "x": 3751.0,
                            "y": 5689.0
                        }, {
                            "x": 3874.0,
                            "y": 5780.0
                        }, {
                            "x": 4322.0,
                            "y": 5780.0
                        }, {
                            "x": 4442.0,
                            "y": 5689.0
                        }],
                        "linkedPoint": {
                            "x": 4096.5,
                            "y": 5665.0
                        },
                        "vectorPoint": {
                            "x": 0.0,
                            "y": 1.0
                        },
                        "grades": [{
                            "gradeId": 79326,
                            "remainCnt": 0,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100743,
                        "blockName": "117블록",
                        "cornerPoints": [{
                            "x": 3378.0,
                            "y": 5327.0
                        }, {
                            "x": 3032.0,
                            "y": 5669.0
                        }, {
                            "x": 3176.0,
                            "y": 5809.0
                        }, {
                            "x": 3514.0,
                            "y": 5471.0
                        }],
                        "linkedPoint": {
                            "x": 3273.0,
                            "y": 5568.0
                        },
                        "vectorPoint": {
                            "x": 0.7033,
                            "y": 0.7109
                        },
                        "grades": [{
                            "gradeId": 79340,
                            "remainCnt": 0,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79349,
                            "remainCnt": 8,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100744,
                        "blockName": "118블록",
                        "cornerPoints": [{
                            "x": 3213.0,
                            "y": 5162.0
                        }, {
                            "x": 2868.0,
                            "y": 5509.0
                        }, {
                            "x": 3024.0,
                            "y": 5655.0
                        }, {
                            "x": 3367.0,
                            "y": 5317.0
                        }],
                        "linkedPoint": {
                            "x": 3117.5,
                            "y": 5408.5
                        },
                        "vectorPoint": {
                            "x": 0.7033,
                            "y": 0.7109
                        },
                        "grades": [{
                            "gradeId": 79342,
                            "remainCnt": 0,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79349,
                            "remainCnt": 8,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100745,
                        "blockName": "119블록",
                        "cornerPoints": [{
                            "x": 3200.0,
                            "y": 5150.0
                        }, {
                            "x": 3093.0,
                            "y": 5011.0
                        }, {
                            "x": 2719.0,
                            "y": 5352.0
                        }, {
                            "x": 2857.0,
                            "y": 5493.0
                        }],
                        "linkedPoint": {
                            "x": 2959.5,
                            "y": 5252.0
                        },
                        "vectorPoint": {
                            "x": 0.7033,
                            "y": 0.7109
                        },
                        "grades": [{
                            "gradeId": 79342,
                            "remainCnt": 0,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79349,
                            "remainCnt": 8,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100746,
                        "blockName": "120블록",
                        "cornerPoints": [{
                            "x": 2954.0,
                            "y": 4740.0
                        }, {
                            "x": 2515.0,
                            "y": 4986.0
                        }, {
                            "x": 2713.0,
                            "y": 5341.0
                        }, {
                            "x": 3086.0,
                            "y": 5000.0
                        }],
                        "linkedPoint": {
                            "x": 2800.5,
                            "y": 5040.5
                        },
                        "vectorPoint": {
                            "x": 0.866,
                            "y": 0.5
                        },
                        "grades": [{
                            "gradeId": 79342,
                            "remainCnt": 2,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79349,
                            "remainCnt": 16,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100747,
                        "blockName": "121블록",
                        "cornerPoints": [{
                            "x": 2856.0,
                            "y": 4548.0
                        }, {
                            "x": 2945.0,
                            "y": 4727.0
                        }, {
                            "x": 2508.0,
                            "y": 4971.0
                        }, {
                            "x": 2413.0,
                            "y": 4801.0
                        }],
                        "linkedPoint": {
                            "x": 2679.0,
                            "y": 4759.5
                        },
                        "vectorPoint": {
                            "x": 0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79342,
                            "remainCnt": 0,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79349,
                            "remainCnt": 8,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100748,
                        "blockName": "122블록",
                        "cornerPoints": [{
                            "x": 2743.0,
                            "y": 4351.0
                        }, {
                            "x": 2301.0,
                            "y": 4605.0
                        }, {
                            "x": 2403.0,
                            "y": 4788.0
                        }, {
                            "x": 2849.0,
                            "y": 4532.0
                        }],
                        "linkedPoint": {
                            "x": 2575.0,
                            "y": 4569.5
                        },
                        "vectorPoint": {
                            "x": 0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79342,
                            "remainCnt": 0,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79349,
                            "remainCnt": 4,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100749,
                        "blockName": "123블록",
                        "cornerPoints": [{
                            "x": 2634.0,
                            "y": 4161.0
                        }, {
                            "x": 2196.0,
                            "y": 4414.0
                        }, {
                            "x": 2293.0,
                            "y": 4590.0
                        }, {
                            "x": 2732.0,
                            "y": 4336.0
                        }],
                        "linkedPoint": {
                            "x": 2464.0,
                            "y": 4375.5
                        },
                        "vectorPoint": {
                            "x": 0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79342,
                            "remainCnt": 0,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79349,
                            "remainCnt": 7,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100750,
                        "blockName": "124블록",
                        "cornerPoints": [{
                            "x": 2524.0,
                            "y": 3969.0
                        }, {
                            "x": 2082.0,
                            "y": 4222.0
                        }, {
                            "x": 2187.0,
                            "y": 4398.0
                        }, {
                            "x": 2625.0,
                            "y": 4144.0
                        }],
                        "linkedPoint": {
                            "x": 2353.5,
                            "y": 4183.5
                        },
                        "vectorPoint": {
                            "x": 0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79344,
                            "remainCnt": 2,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79349,
                            "remainCnt": 8,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100751,
                        "blockName": "125블록",
                        "cornerPoints": [{
                            "x": 2412.0,
                            "y": 3775.0
                        }, {
                            "x": 1975.0,
                            "y": 4027.0
                        }, {
                            "x": 2075.0,
                            "y": 4205.0
                        }, {
                            "x": 2510.0,
                            "y": 3950.0
                        }],
                        "linkedPoint": {
                            "x": 2242.5,
                            "y": 3990.0
                        },
                        "vectorPoint": {
                            "x": 0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79344,
                            "remainCnt": 13,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79349,
                            "remainCnt": 8,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100752,
                        "blockName": "126블록",
                        "cornerPoints": [{
                            "x": 2303.0,
                            "y": 3589.0
                        }, {
                            "x": 2086.0,
                            "y": 3712.0
                        }, {
                            "x": 2128.0,
                            "y": 3785.0
                        }, {
                            "x": 1906.0,
                            "y": 3914.0
                        }, {
                            "x": 1963.0,
                            "y": 4010.0
                        }, {
                            "x": 2401.0,
                            "y": 3759.0
                        }],
                        "linkedPoint": {
                            "x": 2090.0,
                            "y": 3852.0
                        },
                        "vectorPoint": {
                            "x": 0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79344,
                            "remainCnt": 15,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }, {
                            "gradeId": 79349,
                            "remainCnt": 2,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100753,
                        "blockName": "127블록",
                        "cornerPoints": [{
                            "x": 1922.0,
                            "y": 3410.0
                        }, {
                            "x": 2077.0,
                            "y": 3695.0
                        }, {
                            "x": 2291.0,
                            "y": 3573.0
                        }, {
                            "x": 2191.0,
                            "y": 3418.0
                        }],
                        "linkedPoint": {
                            "x": 2106.5,
                            "y": 3552.5
                        },
                        "vectorPoint": {
                            "x": 0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79344,
                            "remainCnt": 19,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100754,
                        "blockName": "3루 타이거즈 가족석(B3)",
                        "cornerPoints": [{
                            "x": 1905.0,
                            "y": 3409.0
                        }, {
                            "x": 1572.0,
                            "y": 3420.0
                        }, {
                            "x": 1840.0,
                            "y": 3935.0
                        }, {
                            "x": 2106.0,
                            "y": 3781.0
                        }],
                        "linkedPoint": {
                            "x": 1839.0,
                            "y": 3672.0
                        },
                        "vectorPoint": {
                            "x": 0.866,
                            "y": 0.5
                        },
                        "grades": [{
                            "gradeId": 79331,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }, {
                            "gradeId": 79333,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100755,
                        "blockName": "1루 서프라이즈존",
                        "cornerPoints": [{
                            "x": 5517.0,
                            "y": 3949.0
                        }, {
                            "x": 5291.0,
                            "y": 4342.0
                        }, {
                            "x": 5381.0,
                            "y": 4395.0
                        }, {
                            "x": 5607.0,
                            "y": 4001.0
                        }],
                        "linkedPoint": {
                            "x": 5449.0,
                            "y": 4172.0
                        },
                        "vectorPoint": {
                            "x": -0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79330,
                            "remainCnt": 2,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100756,
                        "blockName": "501블록",
                        "cornerPoints": [{
                            "x": 6677.0,
                            "y": 3760.0
                        }, {
                            "x": 6579.0,
                            "y": 3972.0
                        }, {
                            "x": 6804.0,
                            "y": 4075.0
                        }, {
                            "x": 6903.0,
                            "y": 3859.0
                        }],
                        "linkedPoint": {
                            "x": 6741.0,
                            "y": 3917.5
                        },
                        "vectorPoint": {
                            "x": -0.9063,
                            "y": 0.4226
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 162,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100757,
                        "blockName": "502블록",
                        "cornerPoints": [{
                            "x": 6572.0,
                            "y": 3991.0
                        }, {
                            "x": 6486.0,
                            "y": 4176.0
                        }, {
                            "x": 6712.0,
                            "y": 4279.0
                        }, {
                            "x": 6797.0,
                            "y": 4093.0
                        }],
                        "linkedPoint": {
                            "x": 6641.5,
                            "y": 4135.0
                        },
                        "vectorPoint": {
                            "x": -0.9063,
                            "y": 0.4226
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 151,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100758,
                        "blockName": "503블록",
                        "cornerPoints": [{
                            "x": 6478.0,
                            "y": 4192.0
                        }, {
                            "x": 6397.0,
                            "y": 4375.0
                        }, {
                            "x": 6618.0,
                            "y": 4481.0
                        }, {
                            "x": 6705.0,
                            "y": 4297.0
                        }],
                        "linkedPoint": {
                            "x": 6551.0,
                            "y": 4336.5
                        },
                        "vectorPoint": {
                            "x": -0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 202,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100759,
                        "blockName": "504블록",
                        "cornerPoints": [{
                            "x": 6388.0,
                            "y": 4393.0
                        }, {
                            "x": 6303.0,
                            "y": 4578.0
                        }, {
                            "x": 6527.0,
                            "y": 4682.0
                        }, {
                            "x": 6611.0,
                            "y": 4499.0
                        }],
                        "linkedPoint": {
                            "x": 6457.0,
                            "y": 4537.5
                        },
                        "vectorPoint": {
                            "x": -0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 185,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100760,
                        "blockName": "505블록",
                        "cornerPoints": [{
                            "x": 6296.0,
                            "y": 4595.0
                        }, {
                            "x": 6209.0,
                            "y": 4782.0
                        }, {
                            "x": 6429.0,
                            "y": 4889.0
                        }, {
                            "x": 6521.0,
                            "y": 4701.0
                        }],
                        "linkedPoint": {
                            "x": 6365.0,
                            "y": 4742.0
                        },
                        "vectorPoint": {
                            "x": -0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 224,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100761,
                        "blockName": "506블록",
                        "cornerPoints": [{
                            "x": 6201.0,
                            "y": 4796.0
                        }, {
                            "x": 6115.0,
                            "y": 4987.0
                        }, {
                            "x": 6339.0,
                            "y": 5094.0
                        }, {
                            "x": 6425.0,
                            "y": 4904.0
                        }],
                        "linkedPoint": {
                            "x": 6270.0,
                            "y": 4945.0
                        },
                        "vectorPoint": {
                            "x": -0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 194,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100762,
                        "blockName": "507블록",
                        "cornerPoints": [{
                            "x": 6106.0,
                            "y": 5004.0
                        }, {
                            "x": 6008.0,
                            "y": 5218.0
                        }, {
                            "x": 6234.0,
                            "y": 5329.0
                        }, {
                            "x": 6332.0,
                            "y": 5111.0
                        }],
                        "linkedPoint": {
                            "x": 6170.0,
                            "y": 5166.5
                        },
                        "vectorPoint": {
                            "x": -0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 233,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100763,
                        "blockName": "508블록",
                        "cornerPoints": [{
                            "x": 6000.0,
                            "y": 5232.0
                        }, {
                            "x": 5884.0,
                            "y": 5456.0
                        }, {
                            "x": 6073.0,
                            "y": 5645.0
                        }, {
                            "x": 6230.0,
                            "y": 5342.0
                        }],
                        "linkedPoint": {
                            "x": 6057.0,
                            "y": 5438.5
                        },
                        "vectorPoint": {
                            "x": -0.8912,
                            "y": 0.4536
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 206,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100764,
                        "blockName": "509블록",
                        "cornerPoints": [{
                            "x": 5871.0,
                            "y": 5468.0
                        }, {
                            "x": 5708.0,
                            "y": 5638.0
                        }, {
                            "x": 5898.0,
                            "y": 5830.0
                        }, {
                            "x": 6063.0,
                            "y": 5661.0
                        }],
                        "linkedPoint": {
                            "x": 5885.5,
                            "y": 5649.0
                        },
                        "vectorPoint": {
                            "x": -0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 210,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100765,
                        "blockName": "510블록",
                        "cornerPoints": [{
                            "x": 5695.0,
                            "y": 5650.0
                        }, {
                            "x": 5551.0,
                            "y": 5803.0
                        }, {
                            "x": 5741.0,
                            "y": 5994.0
                        }, {
                            "x": 5888.0,
                            "y": 5843.0
                        }],
                        "linkedPoint": {
                            "x": 5719.5,
                            "y": 5822.0
                        },
                        "vectorPoint": {
                            "x": -0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 167,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100766,
                        "blockName": "511블록",
                        "cornerPoints": [{
                            "x": 5539.0,
                            "y": 5813.0
                        }, {
                            "x": 5384.0,
                            "y": 5961.0
                        }, {
                            "x": 5575.0,
                            "y": 6154.0
                        }, {
                            "x": 5731.0,
                            "y": 6005.0
                        }],
                        "linkedPoint": {
                            "x": 5557.5,
                            "y": 5983.5
                        },
                        "vectorPoint": {
                            "x": -0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 197,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100767,
                        "blockName": "512블록",
                        "cornerPoints": [{
                            "x": 5371.0,
                            "y": 5974.0
                        }, {
                            "x": 5227.0,
                            "y": 6124.0
                        }, {
                            "x": 5418.0,
                            "y": 6315.0
                        }, {
                            "x": 5565.0,
                            "y": 6167.0
                        }],
                        "linkedPoint": {
                            "x": 5396.0,
                            "y": 6144.5
                        },
                        "vectorPoint": {
                            "x": -0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 184,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100768,
                        "blockName": "513블록",
                        "cornerPoints": [{
                            "x": 5215.0,
                            "y": 6139.0
                        }, {
                            "x": 5065.0,
                            "y": 6290.0
                        }, {
                            "x": 5249.0,
                            "y": 6482.0
                        }, {
                            "x": 5408.0,
                            "y": 6331.0
                        }],
                        "linkedPoint": {
                            "x": 5236.5,
                            "y": 6310.5
                        },
                        "vectorPoint": {
                            "x": -0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 197,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100769,
                        "blockName": "514블록",
                        "cornerPoints": [{
                            "x": 5055.0,
                            "y": 6299.0
                        }, {
                            "x": 4869.0,
                            "y": 6442.0
                        }, {
                            "x": 4997.0,
                            "y": 6664.0
                        }, {
                            "x": 5238.0,
                            "y": 6495.0
                        }],
                        "linkedPoint": {
                            "x": 5053.5,
                            "y": 6481.5
                        },
                        "vectorPoint": {
                            "x": -0.6442,
                            "y": 0.7648
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 169,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100770,
                        "blockName": "515블록",
                        "cornerPoints": [{
                            "x": 4856.0,
                            "y": 6448.0
                        }, {
                            "x": 4678.0,
                            "y": 6548.0
                        }, {
                            "x": 4803.0,
                            "y": 6773.0
                        }, {
                            "x": 4982.0,
                            "y": 6672.0
                        }],
                        "linkedPoint": {
                            "x": 4830.0,
                            "y": 6610.5
                        },
                        "vectorPoint": {
                            "x": -0.4969,
                            "y": 0.8678
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 201,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100771,
                        "blockName": "516블록",
                        "cornerPoints": [{
                            "x": 4663.0,
                            "y": 6558.0
                        }, {
                            "x": 4461.0,
                            "y": 6648.0
                        }, {
                            "x": 4462.0,
                            "y": 6929.0
                        }, {
                            "x": 4788.0,
                            "y": 6780.0
                        }],
                        "linkedPoint": {
                            "x": 4624.5,
                            "y": 6743.5
                        },
                        "vectorPoint": {
                            "x": -0.4078,
                            "y": 0.9131
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 174,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100772,
                        "blockName": "517블록",
                        "cornerPoints": [{
                            "x": 4220.0,
                            "y": 6649.0
                        }, {
                            "x": 4220.0,
                            "y": 6933.0
                        }, {
                            "x": 4444.0,
                            "y": 6933.0
                        }, {
                            "x": 4444.0,
                            "y": 6649.0
                        }],
                        "linkedPoint": {
                            "x": 4332.0,
                            "y": 6791.0
                        },
                        "vectorPoint": {
                            "x": 0.0,
                            "y": 1.0
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 172,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100773,
                        "blockName": "518블록",
                        "cornerPoints": [{
                            "x": 3985.0,
                            "y": 6649.0
                        }, {
                            "x": 3985.0,
                            "y": 6933.0
                        }, {
                            "x": 4194.0,
                            "y": 6933.0
                        }, {
                            "x": 4194.0,
                            "y": 6649.0
                        }],
                        "linkedPoint": {
                            "x": 4089.5,
                            "y": 6791.0
                        },
                        "vectorPoint": {
                            "x": 0.0,
                            "y": 1.0
                        },
                        "grades": [{
                            "gradeId": 79347,
                            "remainCnt": 53,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100774,
                        "blockName": "519블록",
                        "cornerPoints": [{
                            "x": 3738.0,
                            "y": 6649.0
                        }, {
                            "x": 3738.0,
                            "y": 6933.0
                        }, {
                            "x": 3962.0,
                            "y": 6933.0
                        }, {
                            "x": 3962.0,
                            "y": 6649.0
                        }],
                        "linkedPoint": {
                            "x": 3850.0,
                            "y": 6791.0
                        },
                        "vectorPoint": {
                            "x": 0.0,
                            "y": 1.0
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 80,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100775,
                        "blockName": "520블록",
                        "cornerPoints": [{
                            "x": 3519.0,
                            "y": 6557.0
                        }, {
                            "x": 3394.0,
                            "y": 6780.0
                        }, {
                            "x": 3720.0,
                            "y": 6929.0
                        }, {
                            "x": 3720.0,
                            "y": 6648.0
                        }],
                        "linkedPoint": {
                            "x": 3557.0,
                            "y": 6743.0
                        },
                        "vectorPoint": {
                            "x": 0.4078,
                            "y": 0.9131
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 110,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100776,
                        "blockName": "521블록",
                        "cornerPoints": [{
                            "x": 3327.0,
                            "y": 6448.0
                        }, {
                            "x": 3201.0,
                            "y": 6671.0
                        }, {
                            "x": 3379.0,
                            "y": 6772.0
                        }, {
                            "x": 3505.0,
                            "y": 6548.0
                        }],
                        "linkedPoint": {
                            "x": 3353.0,
                            "y": 6610.0
                        },
                        "vectorPoint": {
                            "x": 0.4969,
                            "y": 0.8678
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 136,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100777,
                        "blockName": "522블록",
                        "cornerPoints": [{
                            "x": 3129.0,
                            "y": 6299.0
                        }, {
                            "x": 2945.0,
                            "y": 6495.0
                        }, {
                            "x": 3184.0,
                            "y": 6664.0
                        }, {
                            "x": 3314.0,
                            "y": 6442.0
                        }],
                        "linkedPoint": {
                            "x": 3129.5,
                            "y": 6481.5
                        },
                        "vectorPoint": {
                            "x": 0.6131,
                            "y": 0.79
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 133,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100778,
                        "blockName": "523블록",
                        "cornerPoints": [{
                            "x": 2969.0,
                            "y": 6138.0
                        }, {
                            "x": 2777.0,
                            "y": 6329.0
                        }, {
                            "x": 2932.0,
                            "y": 6481.0
                        }, {
                            "x": 3119.0,
                            "y": 6290.0
                        }],
                        "linkedPoint": {
                            "x": 2948.0,
                            "y": 6309.5
                        },
                        "vectorPoint": {
                            "x": 0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 176,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100779,
                        "blockName": "524블록",
                        "cornerPoints": [{
                            "x": 2810.0,
                            "y": 5974.0
                        }, {
                            "x": 2618.0,
                            "y": 6167.0
                        }, {
                            "x": 2763.0,
                            "y": 6316.0
                        }, {
                            "x": 2955.0,
                            "y": 6125.0
                        }],
                        "linkedPoint": {
                            "x": 2786.5,
                            "y": 6145.0
                        },
                        "vectorPoint": {
                            "x": 0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 154,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100780,
                        "blockName": "525블록",
                        "cornerPoints": [{
                            "x": 2643.0,
                            "y": 5814.0
                        }, {
                            "x": 2451.0,
                            "y": 6005.0
                        }, {
                            "x": 2606.0,
                            "y": 6154.0
                        }, {
                            "x": 2800.0,
                            "y": 5962.0
                        }],
                        "linkedPoint": {
                            "x": 2625.5,
                            "y": 5984.0
                        },
                        "vectorPoint": {
                            "x": 0.7033,
                            "y": 0.7109
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 174,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100781,
                        "blockName": "526블록",
                        "cornerPoints": [{
                            "x": 2488.0,
                            "y": 5650.0
                        }, {
                            "x": 2295.0,
                            "y": 5842.0
                        }, {
                            "x": 2440.0,
                            "y": 5993.0
                        }, {
                            "x": 2631.0,
                            "y": 5803.0
                        }],
                        "linkedPoint": {
                            "x": 2463.0,
                            "y": 5821.5
                        },
                        "vectorPoint": {
                            "x": 0.7033,
                            "y": 0.7109
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 166,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100782,
                        "blockName": "527블록",
                        "cornerPoints": [{
                            "x": 2313.0,
                            "y": 5468.0
                        }, {
                            "x": 2120.0,
                            "y": 5660.0
                        }, {
                            "x": 2284.0,
                            "y": 5829.0
                        }, {
                            "x": 2474.0,
                            "y": 5639.0
                        }],
                        "linkedPoint": {
                            "x": 2297.0,
                            "y": 5648.5
                        },
                        "vectorPoint": {
                            "x": 0.7033,
                            "y": 0.7109
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 162,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100783,
                        "blockName": "528블록",
                        "cornerPoints": [{
                            "x": 2183.0,
                            "y": 5232.0
                        }, {
                            "x": 1955.0,
                            "y": 5342.0
                        }, {
                            "x": 2109.0,
                            "y": 5644.0
                        }, {
                            "x": 2299.0,
                            "y": 5457.0
                        }],
                        "linkedPoint": {
                            "x": 2127.0,
                            "y": 5438.0
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 110,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100784,
                        "blockName": "529블록",
                        "cornerPoints": [{
                            "x": 2077.0,
                            "y": 5005.0
                        }, {
                            "x": 1851.0,
                            "y": 5111.0
                        }, {
                            "x": 1949.0,
                            "y": 5328.0
                        }, {
                            "x": 2174.0,
                            "y": 5218.0
                        }],
                        "linkedPoint": {
                            "x": 2012.5,
                            "y": 5166.5
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 144,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100785,
                        "blockName": "530블록",
                        "cornerPoints": [{
                            "x": 1980.0,
                            "y": 4797.0
                        }, {
                            "x": 1759.0,
                            "y": 4903.0
                        }, {
                            "x": 1843.0,
                            "y": 5093.0
                        }, {
                            "x": 2066.0,
                            "y": 4988.0
                        }],
                        "linkedPoint": {
                            "x": 1912.5,
                            "y": 4945.0
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 138,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100786,
                        "blockName": "531블록",
                        "cornerPoints": [{
                            "x": 1886.0,
                            "y": 4597.0
                        }, {
                            "x": 1662.0,
                            "y": 4700.0
                        }, {
                            "x": 1752.0,
                            "y": 4887.0
                        }, {
                            "x": 1971.0,
                            "y": 4782.0
                        }],
                        "linkedPoint": {
                            "x": 1816.5,
                            "y": 4742.0
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 218,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100787,
                        "blockName": "532블록",
                        "cornerPoints": [{
                            "x": 1793.0,
                            "y": 4394.0
                        }, {
                            "x": 1572.0,
                            "y": 4499.0
                        }, {
                            "x": 1654.0,
                            "y": 4681.0
                        }, {
                            "x": 1877.0,
                            "y": 4579.0
                        }],
                        "linkedPoint": {
                            "x": 1724.5,
                            "y": 4537.5
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 186,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100788,
                        "blockName": "533블록",
                        "cornerPoints": [{
                            "x": 1705.0,
                            "y": 4192.0
                        }, {
                            "x": 1477.0,
                            "y": 4296.0
                        }, {
                            "x": 1564.0,
                            "y": 4481.0
                        }, {
                            "x": 1786.0,
                            "y": 4376.0
                        }],
                        "linkedPoint": {
                            "x": 1631.5,
                            "y": 4336.5
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 202,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100789,
                        "blockName": "534블록",
                        "cornerPoints": [{
                            "x": 1609.0,
                            "y": 3991.0
                        }, {
                            "x": 1386.0,
                            "y": 4093.0
                        }, {
                            "x": 1469.0,
                            "y": 4277.0
                        }, {
                            "x": 1696.0,
                            "y": 4176.0
                        }],
                        "linkedPoint": {
                            "x": 1541.0,
                            "y": 4134.0
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 150,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100790,
                        "blockName": "535블록",
                        "cornerPoints": [{
                            "x": 1505.0,
                            "y": 3760.0
                        }, {
                            "x": 1280.0,
                            "y": 3858.0
                        }, {
                            "x": 1378.0,
                            "y": 4074.0
                        }, {
                            "x": 1602.0,
                            "y": 3972.0
                        }],
                        "linkedPoint": {
                            "x": 1441.0,
                            "y": 3917.0
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79346,
                            "remainCnt": 164,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100791,
                        "blockName": "스카이피크닉 T1",
                        "cornerPoints": [{
                            "x": 6592.0,
                            "y": 3711.0
                        }, {
                            "x": 6566.0,
                            "y": 3765.0
                        }, {
                            "x": 6631.0,
                            "y": 3796.0
                        }, {
                            "x": 6657.0,
                            "y": 3742.0
                        }],
                        "linkedPoint": {
                            "x": 6611.5,
                            "y": 3753.5
                        },
                        "vectorPoint": {
                            "x": -0.8912,
                            "y": 0.4536
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100792,
                        "blockName": "스카이피크닉 T2",
                        "cornerPoints": [{
                            "x": 6566.0,
                            "y": 3769.0
                        }, {
                            "x": 6540.0,
                            "y": 3823.0
                        }, {
                            "x": 6606.0,
                            "y": 3854.0
                        }, {
                            "x": 6631.0,
                            "y": 3800.0
                        }],
                        "linkedPoint": {
                            "x": 6585.5,
                            "y": 3811.5
                        },
                        "vectorPoint": {
                            "x": -0.8912,
                            "y": 0.4536
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100793,
                        "blockName": "스카이피크닉 T3",
                        "cornerPoints": [{
                            "x": 6539.0,
                            "y": 3826.0
                        }, {
                            "x": 6514.0,
                            "y": 3880.0
                        }, {
                            "x": 6578.0,
                            "y": 3910.0
                        }, {
                            "x": 6603.0,
                            "y": 3857.0
                        }],
                        "linkedPoint": {
                            "x": 6558.5,
                            "y": 3868.0
                        },
                        "vectorPoint": {
                            "x": -0.8912,
                            "y": 0.4536
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100794,
                        "blockName": "스카이피크닉 T4",
                        "cornerPoints": [{
                            "x": 6413.0,
                            "y": 4085.0
                        }, {
                            "x": 6387.0,
                            "y": 4139.0
                        }, {
                            "x": 6452.0,
                            "y": 4169.0
                        }, {
                            "x": 6478.0,
                            "y": 4116.0
                        }],
                        "linkedPoint": {
                            "x": 6432.5,
                            "y": 4127.0
                        },
                        "vectorPoint": {
                            "x": -0.9044,
                            "y": 0.4267
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100795,
                        "blockName": "스카이피크닉 T5",
                        "cornerPoints": [{
                            "x": 6387.0,
                            "y": 4143.0
                        }, {
                            "x": 6361.0,
                            "y": 4197.0
                        }, {
                            "x": 6426.0,
                            "y": 4227.0
                        }, {
                            "x": 6452.0,
                            "y": 4174.0
                        }],
                        "linkedPoint": {
                            "x": 6406.5,
                            "y": 4185.0
                        },
                        "vectorPoint": {
                            "x": -0.9044,
                            "y": 0.4267
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100796,
                        "blockName": "스카이피크닉 T6",
                        "cornerPoints": [{
                            "x": 6359.0,
                            "y": 4200.0
                        }, {
                            "x": 6334.0,
                            "y": 4254.0
                        }, {
                            "x": 6400.0,
                            "y": 4285.0
                        }, {
                            "x": 6425.0,
                            "y": 4231.0
                        }],
                        "linkedPoint": {
                            "x": 6379.5,
                            "y": 4242.5
                        },
                        "vectorPoint": {
                            "x": -0.9044,
                            "y": 0.4267
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100797,
                        "blockName": "스카이피크닉 T7",
                        "cornerPoints": [{
                            "x": 6210.0,
                            "y": 4520.0
                        }, {
                            "x": 6185.0,
                            "y": 4574.0
                        }, {
                            "x": 6249.0,
                            "y": 4604.0
                        }, {
                            "x": 6275.0,
                            "y": 4550.0
                        }],
                        "linkedPoint": {
                            "x": 6230.0,
                            "y": 4562.0
                        },
                        "vectorPoint": {
                            "x": -0.9128,
                            "y": 0.4085
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100798,
                        "blockName": "스카이피크닉 T8",
                        "cornerPoints": [{
                            "x": 6184.0,
                            "y": 4578.0
                        }, {
                            "x": 6158.0,
                            "y": 4632.0
                        }, {
                            "x": 6224.0,
                            "y": 4663.0
                        }, {
                            "x": 6249.0,
                            "y": 4609.0
                        }],
                        "linkedPoint": {
                            "x": 6203.5,
                            "y": 4620.5
                        },
                        "vectorPoint": {
                            "x": -0.9128,
                            "y": 0.4085
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100799,
                        "blockName": "스카이피크닉 T9",
                        "cornerPoints": [{
                            "x": 6157.0,
                            "y": 4636.0
                        }, {
                            "x": 6132.0,
                            "y": 4689.0
                        }, {
                            "x": 6196.0,
                            "y": 4720.0
                        }, {
                            "x": 6222.0,
                            "y": 4666.0
                        }],
                        "linkedPoint": {
                            "x": 6177.0,
                            "y": 4678.0
                        },
                        "vectorPoint": {
                            "x": -0.9128,
                            "y": 0.4085
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100800,
                        "blockName": "스카이피크닉 T10",
                        "cornerPoints": [{
                            "x": 5994.0,
                            "y": 4957.0
                        }, {
                            "x": 5968.0,
                            "y": 5012.0
                        }, {
                            "x": 6033.0,
                            "y": 5042.0
                        }, {
                            "x": 6059.0,
                            "y": 4988.0
                        }],
                        "linkedPoint": {
                            "x": 6013.5,
                            "y": 4999.5
                        },
                        "vectorPoint": {
                            "x": -0.9128,
                            "y": 0.4085
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100801,
                        "blockName": "스카이피크닉 T11",
                        "cornerPoints": [{
                            "x": 5968.0,
                            "y": 5015.0
                        }, {
                            "x": 5943.0,
                            "y": 5069.0
                        }, {
                            "x": 6007.0,
                            "y": 5100.0
                        }, {
                            "x": 6033.0,
                            "y": 5046.0
                        }],
                        "linkedPoint": {
                            "x": 5988.0,
                            "y": 5057.5
                        },
                        "vectorPoint": {
                            "x": -0.9128,
                            "y": 0.4085
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100802,
                        "blockName": "스카이피크닉 T12",
                        "cornerPoints": [{
                            "x": 5474.0,
                            "y": 5707.0
                        }, {
                            "x": 5432.0,
                            "y": 5749.0
                        }, {
                            "x": 5483.0,
                            "y": 5800.0
                        }, {
                            "x": 5525.0,
                            "y": 5757.0
                        }],
                        "linkedPoint": {
                            "x": 5478.5,
                            "y": 5753.5
                        },
                        "vectorPoint": {
                            "x": -0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100803,
                        "blockName": "스카이피크닉 T13",
                        "cornerPoints": [{
                            "x": 5430.0,
                            "y": 5753.0
                        }, {
                            "x": 5388.0,
                            "y": 5795.0
                        }, {
                            "x": 5439.0,
                            "y": 5846.0
                        }, {
                            "x": 5481.0,
                            "y": 5803.0
                        }],
                        "linkedPoint": {
                            "x": 5434.5,
                            "y": 5799.5
                        },
                        "vectorPoint": {
                            "x": -0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100804,
                        "blockName": "스카이피크닉 T14",
                        "cornerPoints": [{
                            "x": 5385.0,
                            "y": 5797.0
                        }, {
                            "x": 5343.0,
                            "y": 5839.0
                        }, {
                            "x": 5394.0,
                            "y": 5890.0
                        }, {
                            "x": 5436.0,
                            "y": 5848.0
                        }],
                        "linkedPoint": {
                            "x": 5389.5,
                            "y": 5843.5
                        },
                        "vectorPoint": {
                            "x": -0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100805,
                        "blockName": "스카이피크닉 T15",
                        "cornerPoints": [{
                            "x": 5123.0,
                            "y": 6056.0
                        }, {
                            "x": 5081.0,
                            "y": 6098.0
                        }, {
                            "x": 5131.0,
                            "y": 6149.0
                        }, {
                            "x": 5174.0,
                            "y": 6107.0
                        }],
                        "linkedPoint": {
                            "x": 5127.5,
                            "y": 6102.5
                        },
                        "vectorPoint": {
                            "x": -0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100806,
                        "blockName": "스카이피크닉 T16",
                        "cornerPoints": [{
                            "x": 5079.0,
                            "y": 6101.0
                        }, {
                            "x": 5036.0,
                            "y": 6144.0
                        }, {
                            "x": 5087.0,
                            "y": 6195.0
                        }, {
                            "x": 5129.0,
                            "y": 6153.0
                        }],
                        "linkedPoint": {
                            "x": 5082.5,
                            "y": 6148.0
                        },
                        "vectorPoint": {
                            "x": -0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100807,
                        "blockName": "스카이피크닉 T17",
                        "cornerPoints": [{
                            "x": 4773.0,
                            "y": 6365.0
                        }, {
                            "x": 4721.0,
                            "y": 6395.0
                        }, {
                            "x": 4757.0,
                            "y": 6457.0
                        }, {
                            "x": 4809.0,
                            "y": 6427.0
                        }],
                        "linkedPoint": {
                            "x": 4765.0,
                            "y": 6411.0
                        },
                        "vectorPoint": {
                            "x": -0.4882,
                            "y": 0.8727
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100808,
                        "blockName": "스카이피크닉 T18",
                        "cornerPoints": [{
                            "x": 4754.0,
                            "y": 6460.0
                        }, {
                            "x": 4718.0,
                            "y": 6398.0
                        }, {
                            "x": 4666.0,
                            "y": 6428.0
                        }, {
                            "x": 4702.0,
                            "y": 6490.0
                        }],
                        "linkedPoint": {
                            "x": 4710.0,
                            "y": 6444.0
                        },
                        "vectorPoint": {
                            "x": -0.4882,
                            "y": 0.8727
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100809,
                        "blockName": "스카이피크닉 T19",
                        "cornerPoints": [{
                            "x": 4308.0,
                            "y": 6508.0
                        }, {
                            "x": 4308.0,
                            "y": 6609.0
                        }, {
                            "x": 4375.0,
                            "y": 6609.0
                        }, {
                            "x": 4375.0,
                            "y": 6508.0
                        }],
                        "linkedPoint": {
                            "x": 4341.5,
                            "y": 6558.5
                        },
                        "vectorPoint": {
                            "x": 0.0,
                            "y": 1.0
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100810,
                        "blockName": "스카이피크닉 T20",
                        "cornerPoints": [{
                            "x": 4236.0,
                            "y": 6508.0
                        }, {
                            "x": 4236.0,
                            "y": 6609.0
                        }, {
                            "x": 4303.0,
                            "y": 6609.0
                        }, {
                            "x": 4303.0,
                            "y": 6508.0
                        }],
                        "linkedPoint": {
                            "x": 4269.5,
                            "y": 6558.5
                        },
                        "vectorPoint": {
                            "x": 0.0,
                            "y": 1.0
                        },
                        "grades": [{
                            "gradeId": 79338,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100811,
                        "blockName": "스카이피크닉 T21",
                        "cornerPoints": [{
                            "x": 3460.0,
                            "y": 6392.0
                        }, {
                            "x": 3423.0,
                            "y": 6454.0
                        }, {
                            "x": 3474.0,
                            "y": 6484.0
                        }, {
                            "x": 3511.0,
                            "y": 6422.0
                        }],
                        "linkedPoint": {
                            "x": 3467.0,
                            "y": 6438.0
                        },
                        "vectorPoint": {
                            "x": 0.4969,
                            "y": 0.8678
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100812,
                        "blockName": "스카이피크닉 T22",
                        "cornerPoints": [{
                            "x": 3405.0,
                            "y": 6359.0
                        }, {
                            "x": 3369.0,
                            "y": 6421.0
                        }, {
                            "x": 3420.0,
                            "y": 6451.0
                        }, {
                            "x": 3456.0,
                            "y": 6390.0
                        }],
                        "linkedPoint": {
                            "x": 3412.5,
                            "y": 6405.0
                        },
                        "vectorPoint": {
                            "x": 0.4969,
                            "y": 0.8678
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100813,
                        "blockName": "스카이피크닉 T23",
                        "cornerPoints": [{
                            "x": 3127.0,
                            "y": 6133.0
                        }, {
                            "x": 3076.0,
                            "y": 6184.0
                        }, {
                            "x": 3119.0,
                            "y": 6226.0
                        }, {
                            "x": 3169.0,
                            "y": 6175.0
                        }],
                        "linkedPoint": {
                            "x": 3122.5,
                            "y": 6179.5
                        },
                        "vectorPoint": {
                            "x": 0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100814,
                        "blockName": "스카이피크닉 T24",
                        "cornerPoints": [{
                            "x": 3083.0,
                            "y": 6087.0
                        }, {
                            "x": 3032.0,
                            "y": 6138.0
                        }, {
                            "x": 3074.0,
                            "y": 6180.0
                        }, {
                            "x": 3125.0,
                            "y": 6130.0
                        }],
                        "linkedPoint": {
                            "x": 3078.5,
                            "y": 6133.5
                        },
                        "vectorPoint": {
                            "x": 0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100815,
                        "blockName": "스카이피크닉 T25",
                        "cornerPoints": [{
                            "x": 2825.0,
                            "y": 5825.0
                        }, {
                            "x": 2774.0,
                            "y": 5876.0
                        }, {
                            "x": 2816.0,
                            "y": 5918.0
                        }, {
                            "x": 2867.0,
                            "y": 5867.0
                        }],
                        "linkedPoint": {
                            "x": 2820.5,
                            "y": 5871.5
                        },
                        "vectorPoint": {
                            "x": 0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100816,
                        "blockName": "스카이피크닉 T26",
                        "cornerPoints": [{
                            "x": 2780.0,
                            "y": 5781.0
                        }, {
                            "x": 2729.0,
                            "y": 5832.0
                        }, {
                            "x": 2772.0,
                            "y": 5874.0
                        }, {
                            "x": 2822.0,
                            "y": 5823.0
                        }],
                        "linkedPoint": {
                            "x": 2775.5,
                            "y": 5827.5
                        },
                        "vectorPoint": {
                            "x": 0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100817,
                        "blockName": "스카이피크닉 T27",
                        "cornerPoints": [{
                            "x": 2736.0,
                            "y": 5736.0
                        }, {
                            "x": 2778.0,
                            "y": 5778.0
                        }, {
                            "x": 2727.0,
                            "y": 5828.0
                        }, {
                            "x": 2685.0,
                            "y": 5786.0
                        }],
                        "linkedPoint": {
                            "x": 2731.5,
                            "y": 5782.0
                        },
                        "vectorPoint": {
                            "x": 0.7104,
                            "y": 0.7038
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100818,
                        "blockName": "스카이피크닉 T28",
                        "cornerPoints": [{
                            "x": 2227.0,
                            "y": 5077.0
                        }, {
                            "x": 2161.0,
                            "y": 5108.0
                        }, {
                            "x": 2187.0,
                            "y": 5161.0
                        }, {
                            "x": 2252.0,
                            "y": 5130.0
                        }],
                        "linkedPoint": {
                            "x": 2206.5,
                            "y": 5119.0
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100819,
                        "blockName": "스카이피크닉 T29",
                        "cornerPoints": [{
                            "x": 2200.0,
                            "y": 5019.0
                        }, {
                            "x": 2136.0,
                            "y": 5049.0
                        }, {
                            "x": 2161.0,
                            "y": 5102.0
                        }, {
                            "x": 2225.0,
                            "y": 5073.0
                        }],
                        "linkedPoint": {
                            "x": 2180.5,
                            "y": 5060.5
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100820,
                        "blockName": "스카이피크닉 T30",
                        "cornerPoints": [{
                            "x": 1971.0,
                            "y": 4525.0
                        }, {
                            "x": 1906.0,
                            "y": 4555.0
                        }, {
                            "x": 1931.0,
                            "y": 4609.0
                        }, {
                            "x": 1997.0,
                            "y": 4579.0
                        }],
                        "linkedPoint": {
                            "x": 1951.5,
                            "y": 4567.0
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100821,
                        "blockName": "스카이피크닉 T31",
                        "cornerPoints": [{
                            "x": 1944.0,
                            "y": 4468.0
                        }, {
                            "x": 1880.0,
                            "y": 4498.0
                        }, {
                            "x": 1905.0,
                            "y": 4552.0
                        }, {
                            "x": 1969.0,
                            "y": 4522.0
                        }],
                        "linkedPoint": {
                            "x": 1924.5,
                            "y": 4510.0
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100822,
                        "blockName": "스카이피크닉 T32",
                        "cornerPoints": [{
                            "x": 1918.0,
                            "y": 4410.0
                        }, {
                            "x": 1854.0,
                            "y": 4440.0
                        }, {
                            "x": 1879.0,
                            "y": 4494.0
                        }, {
                            "x": 1943.0,
                            "y": 4464.0
                        }],
                        "linkedPoint": {
                            "x": 1898.5,
                            "y": 4452.0
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100823,
                        "blockName": "스카이피크닉 T33",
                        "cornerPoints": [{
                            "x": 1853.0,
                            "y": 4269.0
                        }, {
                            "x": 1789.0,
                            "y": 4299.0
                        }, {
                            "x": 1814.0,
                            "y": 4352.0
                        }, {
                            "x": 1878.0,
                            "y": 4323.0
                        }],
                        "linkedPoint": {
                            "x": 1833.5,
                            "y": 4310.5
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100824,
                        "blockName": "스카이피크닉 T34",
                        "cornerPoints": [{
                            "x": 1826.0,
                            "y": 4212.0
                        }, {
                            "x": 1762.0,
                            "y": 4242.0
                        }, {
                            "x": 1787.0,
                            "y": 4296.0
                        }, {
                            "x": 1851.0,
                            "y": 4266.0
                        }],
                        "linkedPoint": {
                            "x": 1806.5,
                            "y": 4254.0
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100825,
                        "blockName": "스카이피크닉 T35",
                        "cornerPoints": [{
                            "x": 1800.0,
                            "y": 4154.0
                        }, {
                            "x": 1736.0,
                            "y": 4184.0
                        }, {
                            "x": 1761.0,
                            "y": 4238.0
                        }, {
                            "x": 1825.0,
                            "y": 4208.0
                        }],
                        "linkedPoint": {
                            "x": 1780.5,
                            "y": 4196.0
                        },
                        "vectorPoint": {
                            "x": 0.9044,
                            "y": 0.4267
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100826,
                        "blockName": "스카이피크닉 T36",
                        "cornerPoints": [{
                            "x": 1695.0,
                            "y": 3900.0
                        }, {
                            "x": 1631.0,
                            "y": 3930.0
                        }, {
                            "x": 1656.0,
                            "y": 3984.0
                        }, {
                            "x": 1720.0,
                            "y": 3954.0
                        }],
                        "linkedPoint": {
                            "x": 1675.5,
                            "y": 3942.0
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100827,
                        "blockName": "스카이피크닉 T37",
                        "cornerPoints": [{
                            "x": 1668.0,
                            "y": 3843.0
                        }, {
                            "x": 1604.0,
                            "y": 3874.0
                        }, {
                            "x": 1629.0,
                            "y": 3927.0
                        }, {
                            "x": 1693.0,
                            "y": 3897.0
                        }],
                        "linkedPoint": {
                            "x": 1648.5,
                            "y": 3885.0
                        },
                        "vectorPoint": {
                            "x": 0.9086,
                            "y": 0.4176
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100828,
                        "blockName": "스카이피크닉 T38",
                        "cornerPoints": [{
                            "x": 1639.0,
                            "y": 3782.0
                        }, {
                            "x": 1574.0,
                            "y": 3813.0
                        }, {
                            "x": 1599.0,
                            "y": 3866.0
                        }, {
                            "x": 1664.0,
                            "y": 3836.0
                        }],
                        "linkedPoint": {
                            "x": 1619.0,
                            "y": 3824.0
                        },
                        "vectorPoint": {
                            "x": 0.9044,
                            "y": 0.4267
                        },
                        "grades": [{
                            "gradeId": 79337,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100829,
                        "blockName": "102블록",
                        "cornerPoints": [{
                            "x": 5904.0,
                            "y": 3571.0
                        }, {
                            "x": 6000.0,
                            "y": 3424.0
                        }, {
                            "x": 6205.0,
                            "y": 3536.0
                        }, {
                            "x": 6119.0,
                            "y": 3694.0
                        }],
                        "linkedPoint": {
                            "x": 6054.5,
                            "y": 3559.0
                        },
                        "vectorPoint": {
                            "x": -0.866,
                            "y": 0.5
                        },
                        "grades": [{
                            "gradeId": 79345,
                            "remainCnt": 55,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100830,
                        "blockName": "101블록",
                        "cornerPoints": [{
                            "x": 6001.0,
                            "y": 3418.0
                        }, {
                            "x": 6208.0,
                            "y": 3530.0
                        }, {
                            "x": 6273.0,
                            "y": 3410.0
                        }],
                        "linkedPoint": {
                            "x": 6137.0,
                            "y": 3470.0
                        },
                        "vectorPoint": {
                            "x": -0.8624,
                            "y": 0.5062
                        },
                        "grades": [{
                            "gradeId": 79345,
                            "remainCnt": 0,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100831,
                        "blockName": "1루 타이거즈가족석(B1)",
                        "cornerPoints": [{
                            "x": 6292.0,
                            "y": 3407.0
                        }, {
                            "x": 6693.0,
                            "y": 3415.0
                        }, {
                            "x": 6398.0,
                            "y": 3958.0
                        }, {
                            "x": 6090.0,
                            "y": 3781.0
                        }],
                        "linkedPoint": {
                            "x": 6391.5,
                            "y": 3682.5
                        },
                        "vectorPoint": {
                            "x": -0.866,
                            "y": 0.5
                        },
                        "grades": [{
                            "gradeId": 79332,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }, {
                            "gradeId": 79334,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100832,
                        "blockName": "에코다이나믹석(1루외야)",
                        "cornerPoints": [{
                            "x": 4778.0,
                            "y": 1364.0
                        }, {
                            "x": 4772.0,
                            "y": 1538.0
                        }, {
                            "x": 4799.0,
                            "y": 1542.0
                        }, {
                            "x": 4833.0,
                            "y": 1550.0
                        }, {
                            "x": 4873.0,
                            "y": 1559.0
                        }, {
                            "x": 4923.0,
                            "y": 1573.0
                        }, {
                            "x": 4973.0,
                            "y": 1588.0
                        }, {
                            "x": 5040.0,
                            "y": 1611.0
                        }, {
                            "x": 5110.0,
                            "y": 1638.0
                        }, {
                            "x": 5159.0,
                            "y": 1658.0
                        }, {
                            "x": 5204.0,
                            "y": 1678.0
                        }, {
                            "x": 5238.0,
                            "y": 1694.0
                        }, {
                            "x": 5277.0,
                            "y": 1713.0
                        }, {
                            "x": 5324.0,
                            "y": 1737.0
                        }, {
                            "x": 5367.0,
                            "y": 1760.0
                        }, {
                            "x": 5409.0,
                            "y": 1784.0
                        }, {
                            "x": 5439.0,
                            "y": 1801.0
                        }, {
                            "x": 5470.0,
                            "y": 1820.0
                        }, {
                            "x": 5519.0,
                            "y": 1850.0
                        }, {
                            "x": 5568.0,
                            "y": 1882.0
                        }, {
                            "x": 5614.0,
                            "y": 1913.0
                        }, {
                            "x": 5658.0,
                            "y": 1944.0
                        }, {
                            "x": 5694.0,
                            "y": 1970.0
                        }, {
                            "x": 5732.0,
                            "y": 1998.0
                        }, {
                            "x": 5776.0,
                            "y": 2031.0
                        }, {
                            "x": 5805.0,
                            "y": 2055.0
                        }, {
                            "x": 5840.0,
                            "y": 2082.0
                        }, {
                            "x": 5938.0,
                            "y": 2165.0
                        }, {
                            "x": 5997.0,
                            "y": 2219.0
                        }, {
                            "x": 6028.0,
                            "y": 2247.0
                        }, {
                            "x": 6056.0,
                            "y": 2274.0
                        }, {
                            "x": 6084.0,
                            "y": 2302.0
                        }, {
                            "x": 6109.0,
                            "y": 2326.0
                        }, {
                            "x": 6131.0,
                            "y": 2351.0
                        }, {
                            "x": 6289.0,
                            "y": 2243.0
                        }, {
                            "x": 6267.0,
                            "y": 2217.0
                        }, {
                            "x": 6248.0,
                            "y": 2195.0
                        }, {
                            "x": 6226.0,
                            "y": 2171.0
                        }, {
                            "x": 6195.0,
                            "y": 2138.0
                        }, {
                            "x": 6164.0,
                            "y": 2105.0
                        }, {
                            "x": 6130.0,
                            "y": 2071.0
                        }, {
                            "x": 6102.0,
                            "y": 2044.0
                        }, {
                            "x": 6070.0,
                            "y": 2014.0
                        }, {
                            "x": 6041.0,
                            "y": 1988.0
                        }, {
                            "x": 6007.0,
                            "y": 1958.0
                        }, {
                            "x": 5981.0,
                            "y": 1936.0
                        }, {
                            "x": 5954.0,
                            "y": 1913.0
                        }, {
                            "x": 5926.0,
                            "y": 1891.0
                        }, {
                            "x": 5897.0,
                            "y": 1868.0
                        }, {
                            "x": 5867.0,
                            "y": 1845.0
                        }, {
                            "x": 5831.0,
                            "y": 1819.0
                        }, {
                            "x": 5800.0,
                            "y": 1797.0
                        }, {
                            "x": 5777.0,
                            "y": 1781.0
                        }, {
                            "x": 5752.0,
                            "y": 1764.0
                        }, {
                            "x": 5719.0,
                            "y": 1742.0
                        }, {
                            "x": 5690.0,
                            "y": 1724.0
                        }, {
                            "x": 5658.0,
                            "y": 1704.0
                        }, {
                            "x": 5622.0,
                            "y": 1682.0
                        }, {
                            "x": 5585.0,
                            "y": 1661.0
                        }, {
                            "x": 5552.0,
                            "y": 1643.0
                        }, {
                            "x": 5525.0,
                            "y": 1628.0
                        }, {
                            "x": 5490.0,
                            "y": 1610.0
                        }, {
                            "x": 5473.0,
                            "y": 1601.0
                        }, {
                            "x": 5452.0,
                            "y": 1591.0
                        }, {
                            "x": 5423.0,
                            "y": 1576.0
                        }, {
                            "x": 5397.0,
                            "y": 1564.0
                        }, {
                            "x": 5351.0,
                            "y": 1543.0
                        }, {
                            "x": 5298.0,
                            "y": 1520.0
                        }, {
                            "x": 5237.0,
                            "y": 1495.0
                        }, {
                            "x": 5172.0,
                            "y": 1471.0
                        }, {
                            "x": 5091.0,
                            "y": 1443.0
                        }, {
                            "x": 5035.0,
                            "y": 1425.0
                        }, {
                            "x": 4986.0,
                            "y": 1411.0
                        }, {
                            "x": 4931.0,
                            "y": 1396.0
                        }, {
                            "x": 4875.0,
                            "y": 1383.0
                        }, {
                            "x": 4816.0,
                            "y": 1371.0
                        }],
                        "linkedPoint": {
                            "x": 5530.5,
                            "y": 1857.5
                        },
                        "vectorPoint": {
                            "x": -0.6681,
                            "y": -0.7441
                        },
                        "grades": [{
                            "gradeId": 79339,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100833,
                        "blockName": "에코다이나믹석(3루외야)",
                        "cornerPoints": [{
                            "x": 1933.0,
                            "y": 2243.0
                        }, {
                            "x": 2086.0,
                            "y": 2349.0
                        }, {
                            "x": 2136.0,
                            "y": 2304.0
                        }, {
                            "x": 2193.0,
                            "y": 2246.0
                        }, {
                            "x": 2260.0,
                            "y": 2184.0
                        }, {
                            "x": 2346.0,
                            "y": 2116.0
                        }, {
                            "x": 2407.0,
                            "y": 2062.0
                        }, {
                            "x": 2488.0,
                            "y": 1998.0
                        }, {
                            "x": 2557.0,
                            "y": 1946.0
                        }, {
                            "x": 2656.0,
                            "y": 1880.0
                        }, {
                            "x": 2736.0,
                            "y": 1828.0
                        }, {
                            "x": 2855.0,
                            "y": 1758.0
                        }, {
                            "x": 2985.0,
                            "y": 1693.0
                        }, {
                            "x": 3077.0,
                            "y": 1653.0
                        }, {
                            "x": 3160.0,
                            "y": 1618.0
                        }, {
                            "x": 3267.0,
                            "y": 1582.0
                        }, {
                            "x": 3377.0,
                            "y": 1551.0
                        }, {
                            "x": 3450.0,
                            "y": 1536.0
                        }, {
                            "x": 3440.0,
                            "y": 1365.0
                        }, {
                            "x": 3351.0,
                            "y": 1381.0
                        }, {
                            "x": 3230.0,
                            "y": 1412.0
                        }, {
                            "x": 3116.0,
                            "y": 1444.0
                        }, {
                            "x": 3013.0,
                            "y": 1484.0
                        }, {
                            "x": 2871.0,
                            "y": 1540.0
                        }, {
                            "x": 2745.0,
                            "y": 1600.0
                        }, {
                            "x": 2614.0,
                            "y": 1669.0
                        }, {
                            "x": 2511.0,
                            "y": 1735.0
                        }, {
                            "x": 2407.0,
                            "y": 1802.0
                        }, {
                            "x": 2304.0,
                            "y": 1880.0
                        }, {
                            "x": 2205.0,
                            "y": 1962.0
                        }, {
                            "x": 2120.0,
                            "y": 2037.0
                        }, {
                            "x": 2059.0,
                            "y": 2101.0
                        }, {
                            "x": 1991.0,
                            "y": 2173.0
                        }],
                        "linkedPoint": {
                            "x": 2691.5,
                            "y": 1857.0
                        },
                        "vectorPoint": {
                            "x": 0.7141,
                            "y": -0.7
                        },
                        "grades": [{
                            "gradeId": 79339,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100834,
                        "blockName": "3루 서프라이즈존",
                        "cornerPoints": [{
                            "x": 2652.0,
                            "y": 3966.0
                        }, {
                            "x": 2742.0,
                            "y": 3913.0
                        }, {
                            "x": 2965.0,
                            "y": 4299.0
                        }, {
                            "x": 2872.0,
                            "y": 4352.0
                        }],
                        "linkedPoint": {
                            "x": 2808.5,
                            "y": 4132.5
                        },
                        "vectorPoint": {
                            "x": 0.8674,
                            "y": 0.4976
                        },
                        "grades": [{
                            "gradeId": 79329,
                            "remainCnt": 0,
                            "deadSeatConditions": ["TWO", "ONE"]
                        }]
                    }, {
                        "blockId": 100835,
                        "blockName": "스카이박스",
                        "cornerPoints": [{
                            "x": 147.0,
                            "y": -505.0
                        }, {
                            "x": 147.0,
                            "y": -95.0
                        }, {
                            "x": 2079.0,
                            "y": -95.0
                        }, {
                            "x": 2079.0,
                            "y": -505.0
                        }],
                        "linkedPoint": {
                            "x": 1113.0,
                            "y": -300.0
                        },
                        "vectorPoint": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "grades": [{
                            "gradeId": 79398,
                            "gradeName": "스카이박스",
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100836,
                        "blockName": "외야자유석",
                        "cornerPoints": [{
                            "x": 1886.0,
                            "y": 3099.0
                        }, {
                            "x": 1942.0,
                            "y": 2910.0
                        }, {
                            "x": 2003.0,
                            "y": 2768.0
                        }, {
                            "x": 2077.0,
                            "y": 2631.0
                        }, {
                            "x": 2186.0,
                            "y": 2471.0
                        }, {
                            "x": 2300.0,
                            "y": 2338.0
                        }, {
                            "x": 2433.0,
                            "y": 2206.0
                        }, {
                            "x": 2613.0,
                            "y": 2064.0
                        }, {
                            "x": 2773.0,
                            "y": 1957.0
                        }, {
                            "x": 2939.0,
                            "y": 1868.0
                        }, {
                            "x": 3104.0,
                            "y": 1797.0
                        }, {
                            "x": 3312.0,
                            "y": 1726.0
                        }, {
                            "x": 3495.0,
                            "y": 1677.0
                        }, {
                            "x": 3696.0,
                            "y": 1639.0
                        }, {
                            "x": 3846.0,
                            "y": 1622.0
                        }, {
                            "x": 4077.0,
                            "y": 1611.0
                        }, {
                            "x": 4227.0,
                            "y": 1611.0
                        }, {
                            "x": 4413.0,
                            "y": 1629.0
                        }, {
                            "x": 4642.0,
                            "y": 1662.0
                        }, {
                            "x": 4797.0,
                            "y": 1695.0
                        }, {
                            "x": 4947.0,
                            "y": 1744.0
                        }, {
                            "x": 5170.0,
                            "y": 1830.0
                        }, {
                            "x": 5369.0,
                            "y": 1919.0
                        }, {
                            "x": 5534.0,
                            "y": 2018.0
                        }, {
                            "x": 5720.0,
                            "y": 2160.0
                        }, {
                            "x": 5864.0,
                            "y": 2295.0
                        }, {
                            "x": 6030.0,
                            "y": 2483.0
                        }, {
                            "x": 6134.0,
                            "y": 2638.0
                        }, {
                            "x": 6210.0,
                            "y": 2781.0
                        }, {
                            "x": 6258.0,
                            "y": 2890.0
                        }, {
                            "x": 5973.0,
                            "y": 3180.0
                        }, {
                            "x": 5894.0,
                            "y": 3049.0
                        }, {
                            "x": 5797.0,
                            "y": 2923.0
                        }, {
                            "x": 5688.0,
                            "y": 2803.0
                        }, {
                            "x": 5585.0,
                            "y": 2706.0
                        }, {
                            "x": 5459.0,
                            "y": 2601.0
                        }, {
                            "x": 5330.0,
                            "y": 2516.0
                        }, {
                            "x": 5193.0,
                            "y": 2433.0
                        }, {
                            "x": 4961.0,
                            "y": 2324.0
                        }, {
                            "x": 4764.0,
                            "y": 2259.0
                        }, {
                            "x": 4537.0,
                            "y": 2204.0
                        }, {
                            "x": 4327.0,
                            "y": 2175.0
                        }, {
                            "x": 4204.0,
                            "y": 2168.0
                        }, {
                            "x": 4029.0,
                            "y": 2167.0
                        }, {
                            "x": 3842.0,
                            "y": 2180.0
                        }, {
                            "x": 3624.0,
                            "y": 2212.0
                        }, {
                            "x": 3427.0,
                            "y": 2264.0
                        }, {
                            "x": 3252.0,
                            "y": 2325.0
                        }, {
                            "x": 3083.0,
                            "y": 2395.0
                        }, {
                            "x": 2945.0,
                            "y": 2471.0
                        }, {
                            "x": 2822.0,
                            "y": 2546.0
                        }, {
                            "x": 2705.0,
                            "y": 2632.0
                        }, {
                            "x": 2598.0,
                            "y": 2726.0
                        }, {
                            "x": 2493.0,
                            "y": 2829.0
                        }, {
                            "x": 2388.0,
                            "y": 2942.0
                        }, {
                            "x": 2309.0,
                            "y": 3060.0
                        }, {
                            "x": 2247.0,
                            "y": 3146.0
                        }, {
                            "x": 2183.0,
                            "y": 3265.0
                        }],
                        "linkedPoint": {
                            "x": 4072.0,
                            "y": 2438.0
                        },
                        "vectorPoint": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "grades": [{
                            "gradeId": 79348,
                            "gradeName": "외야석",
                            "remainCnt": 1530,
                            "deadSeatConditions": []
                        }]
                    }, {
                        "blockId": 100837,
                        "blockName": "S-317",
                        "cornerPoints": [{
                            "x": 4167.0,
                            "y": 6308.0
                        }, {
                            "x": 4275.0,
                            "y": 6307.0
                        }, {
                            "x": 4298.0,
                            "y": 6456.0
                        }, {
                            "x": 4166.0,
                            "y": 6460.0
                        }],
                        "linkedPoint": {
                            "x": 4232.0,
                            "y": 6383.5
                        },
                        "vectorPoint": {
                            "x": 0.0,
                            "y": 1.0
                        },
                        "grades": [{
                            "gradeId": 80312,
                            "remainCnt": 0,
                            "deadSeatConditions": []
                        }]
    }
]
idx = 0
for item in json_data:
    block = Block.objects.create(
        blockId=item['blockId'],
        blockName=item['blockName']
    )
    
    linked_point = Point.objects.create(
        x=item['linkedPoint']['x'],
        y=item['linkedPoint']['y']
    )
    block.linkedPoint = linked_point
    
    vector_point = Point.objects.create(
        x=item['vectorPoint']['x'],
        y=item['vectorPoint']['y']
    )
    block.vectorPoint = vector_point
    
    for corner_point_data in item['cornerPoints']:
        corner_point = Point.objects.create(
            x=corner_point_data['x'],
            y=corner_point_data['y']
        )
        block.cornerPoints.add(corner_point)
    
    print(idx)
    block.save()
    idx = idx + 1