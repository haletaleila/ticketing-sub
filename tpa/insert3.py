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
json_data = {
            "20:17": [
                    {
                        "logicalSeatId": 1446098219,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5369.145,
                                "y": 4515.705
                            },
                            "se": {
                                "x": 5377.819,
                                "y": 4520.681
                            },
                            "sw": {
                                "x": 5374.121,
                                "y": 4507.031
                            },
                            "nw": {
                                "x": 5382.795,
                                "y": 4512.007
                            }
                        },
                        "position": {
                            "x": 5375.9697,
                            "y": 4513.856
                        },
                        "rowIdx": 0,
                        "colIdx": 1,
                        "mapInfo": "107블록 1열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 1,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00001열00013번",
                        "area": {
                            "virtualX": 20,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    }
                ],
                "21:18": [
                    {
                        "logicalSeatId": 1446098394,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5520.045,
                                "y": 4618.407
                            },
                            "se": {
                                "x": 5528.7188,
                                "y": 4623.383
                            },
                            "sw": {
                                "x": 5525.021,
                                "y": 4609.733
                            },
                            "nw": {
                                "x": 5533.6953,
                                "y": 4614.709
                            }
                        },
                        "position": {
                            "x": 5526.87,
                            "y": 4616.558
                        },
                        "rowIdx": 13,
                        "colIdx": 0,
                        "mapInfo": "107블록 14열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 176,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00014열00014번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098408,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5539.155,
                                "y": 4613.229
                            },
                            "se": {
                                "x": 5547.829,
                                "y": 4618.205
                            },
                            "sw": {
                                "x": 5544.131,
                                "y": 4604.555
                            },
                            "nw": {
                                "x": 5552.805,
                                "y": 4609.5312
                            }
                        },
                        "position": {
                            "x": 5545.98,
                            "y": 4611.38
                        },
                        "rowIdx": 14,
                        "colIdx": 1,
                        "mapInfo": "107블록 15열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 190,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00015열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098421,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5544.335,
                                "y": 4632.339
                            },
                            "se": {
                                "x": 5553.009,
                                "y": 4637.315
                            },
                            "sw": {
                                "x": 5549.311,
                                "y": 4623.665
                            },
                            "nw": {
                                "x": 5557.9854,
                                "y": 4628.641
                            }
                        },
                        "position": {
                            "x": 5551.16,
                            "y": 4630.49
                        },
                        "rowIdx": 15,
                        "colIdx": 0,
                        "mapInfo": "107블록 16열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 203,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00016열00014번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098422,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5551.295,
                                "y": 4620.195
                            },
                            "se": {
                                "x": 5559.9688,
                                "y": 4625.171
                            },
                            "sw": {
                                "x": 5556.271,
                                "y": 4611.521
                            },
                            "nw": {
                                "x": 5564.9453,
                                "y": 4616.497
                            }
                        },
                        "position": {
                            "x": 5558.12,
                            "y": 4618.346
                        },
                        "rowIdx": 15,
                        "colIdx": 1,
                        "mapInfo": "107블록 16열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 204,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00016열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098435,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5563.445,
                                "y": 4627.161
                            },
                            "se": {
                                "x": 5572.119,
                                "y": 4632.137
                            },
                            "sw": {
                                "x": 5568.421,
                                "y": 4618.487
                            },
                            "nw": {
                                "x": 5577.095,
                                "y": 4623.463
                            }
                        },
                        "position": {
                            "x": 5570.27,
                            "y": 4625.312
                        },
                        "rowIdx": 16,
                        "colIdx": 1,
                        "mapInfo": "107블록 17열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 217,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00017열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098436,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5570.405,
                                "y": 4615.017
                            },
                            "se": {
                                "x": 5579.079,
                                "y": 4619.993
                            },
                            "sw": {
                                "x": 5575.381,
                                "y": 4606.343
                            },
                            "nw": {
                                "x": 5584.055,
                                "y": 4611.319
                            }
                        },
                        "position": {
                            "x": 5577.23,
                            "y": 4613.168
                        },
                        "rowIdx": 16,
                        "colIdx": 2,
                        "mapInfo": "107블록 17열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 218,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00017열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098448,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5568.625,
                                "y": 4646.271
                            },
                            "se": {
                                "x": 5577.299,
                                "y": 4651.247
                            },
                            "sw": {
                                "x": 5573.601,
                                "y": 4637.597
                            },
                            "nw": {
                                "x": 5582.275,
                                "y": 4642.573
                            }
                        },
                        "position": {
                            "x": 5575.45,
                            "y": 4644.422
                        },
                        "rowIdx": 17,
                        "colIdx": 0,
                        "mapInfo": "107블록 18열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 230,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00018열00014번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098449,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5575.585,
                                "y": 4634.127
                            },
                            "se": {
                                "x": 5584.259,
                                "y": 4639.103
                            },
                            "sw": {
                                "x": 5580.561,
                                "y": 4625.453
                            },
                            "nw": {
                                "x": 5589.2354,
                                "y": 4630.429
                            }
                        },
                        "position": {
                            "x": 5582.41,
                            "y": 4632.278
                        },
                        "rowIdx": 17,
                        "colIdx": 1,
                        "mapInfo": "107블록 18열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 231,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00018열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098450,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5582.5547,
                                "y": 4621.983
                            },
                            "se": {
                                "x": 5591.229,
                                "y": 4626.959
                            },
                            "sw": {
                                "x": 5587.5312,
                                "y": 4613.309
                            },
                            "nw": {
                                "x": 5596.205,
                                "y": 4618.285
                            }
                        },
                        "position": {
                            "x": 5589.38,
                            "y": 4620.134
                        },
                        "rowIdx": 17,
                        "colIdx": 2,
                        "mapInfo": "107블록 18열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 232,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00018열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098462,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5587.735,
                                "y": 4641.093
                            },
                            "se": {
                                "x": 5596.409,
                                "y": 4646.069
                            },
                            "sw": {
                                "x": 5592.711,
                                "y": 4632.419
                            },
                            "nw": {
                                "x": 5601.3853,
                                "y": 4637.395
                            }
                        },
                        "position": {
                            "x": 5594.56,
                            "y": 4639.244
                        },
                        "rowIdx": 18,
                        "colIdx": 1,
                        "mapInfo": "107블록 19열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 244,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00019열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098463,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5594.695,
                                "y": 4628.949
                            },
                            "se": {
                                "x": 5603.369,
                                "y": 4633.925
                            },
                            "sw": {
                                "x": 5599.671,
                                "y": 4620.275
                            },
                            "nw": {
                                "x": 5608.345,
                                "y": 4625.251
                            }
                        },
                        "position": {
                            "x": 5601.52,
                            "y": 4627.1
                        },
                        "rowIdx": 18,
                        "colIdx": 2,
                        "mapInfo": "107블록 19열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 245,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00019열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098464,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5601.665,
                                "y": 4616.805
                            },
                            "se": {
                                "x": 5610.339,
                                "y": 4621.7812
                            },
                            "sw": {
                                "x": 5606.641,
                                "y": 4608.131
                            },
                            "nw": {
                                "x": 5615.315,
                                "y": 4613.107
                            }
                        },
                        "position": {
                            "x": 5608.49,
                            "y": 4614.956
                        },
                        "rowIdx": 18,
                        "colIdx": 3,
                        "mapInfo": "107블록 19열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 246,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00019열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098475,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5592.905,
                                "y": 4660.203
                            },
                            "se": {
                                "x": 5601.579,
                                "y": 4665.179
                            },
                            "sw": {
                                "x": 5597.881,
                                "y": 4651.529
                            },
                            "nw": {
                                "x": 5606.555,
                                "y": 4656.505
                            }
                        },
                        "position": {
                            "x": 5599.73,
                            "y": 4658.354
                        },
                        "rowIdx": 19,
                        "colIdx": 0,
                        "mapInfo": "107블록 20열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 257,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00020열00014번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098476,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5599.875,
                                "y": 4648.059
                            },
                            "se": {
                                "x": 5608.549,
                                "y": 4653.035
                            },
                            "sw": {
                                "x": 5604.851,
                                "y": 4639.385
                            },
                            "nw": {
                                "x": 5613.525,
                                "y": 4644.361
                            }
                        },
                        "position": {
                            "x": 5606.7,
                            "y": 4646.21
                        },
                        "rowIdx": 19,
                        "colIdx": 1,
                        "mapInfo": "107블록 20열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 258,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00020열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098477,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5606.8447,
                                "y": 4635.915
                            },
                            "se": {
                                "x": 5615.519,
                                "y": 4640.891
                            },
                            "sw": {
                                "x": 5611.8213,
                                "y": 4627.241
                            },
                            "nw": {
                                "x": 5620.495,
                                "y": 4632.217
                            }
                        },
                        "position": {
                            "x": 5613.67,
                            "y": 4634.066
                        },
                        "rowIdx": 19,
                        "colIdx": 2,
                        "mapInfo": "107블록 20열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 259,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00020열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098478,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5613.8047,
                                "y": 4623.771
                            },
                            "se": {
                                "x": 5622.479,
                                "y": 4628.747
                            },
                            "sw": {
                                "x": 5618.7812,
                                "y": 4615.097
                            },
                            "nw": {
                                "x": 5627.455,
                                "y": 4620.073
                            }
                        },
                        "position": {
                            "x": 5620.63,
                            "y": 4621.922
                        },
                        "rowIdx": 19,
                        "colIdx": 3,
                        "mapInfo": "107블록 20열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 260,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00020열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098479,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5620.775,
                                "y": 4611.627
                            },
                            "se": {
                                "x": 5629.449,
                                "y": 4616.603
                            },
                            "sw": {
                                "x": 5625.751,
                                "y": 4602.953
                            },
                            "nw": {
                                "x": 5634.425,
                                "y": 4607.929
                            }
                        },
                        "position": {
                            "x": 5627.6,
                            "y": 4609.778
                        },
                        "rowIdx": 19,
                        "colIdx": 4,
                        "mapInfo": "107블록 20열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 261,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00020열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098489,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5612.0146,
                                "y": 4655.025
                            },
                            "se": {
                                "x": 5620.689,
                                "y": 4660.001
                            },
                            "sw": {
                                "x": 5616.991,
                                "y": 4646.351
                            },
                            "nw": {
                                "x": 5625.665,
                                "y": 4651.327
                            }
                        },
                        "position": {
                            "x": 5618.84,
                            "y": 4653.176
                        },
                        "rowIdx": 20,
                        "colIdx": 1,
                        "mapInfo": "107블록 21열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 271,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00021열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098490,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5618.985,
                                "y": 4642.881
                            },
                            "se": {
                                "x": 5627.659,
                                "y": 4647.857
                            },
                            "sw": {
                                "x": 5623.961,
                                "y": 4634.207
                            },
                            "nw": {
                                "x": 5632.6353,
                                "y": 4639.183
                            }
                        },
                        "position": {
                            "x": 5625.81,
                            "y": 4641.032
                        },
                        "rowIdx": 20,
                        "colIdx": 2,
                        "mapInfo": "107블록 21열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 272,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00021열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098502,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5617.195,
                                "y": 4674.135
                            },
                            "se": {
                                "x": 5625.869,
                                "y": 4679.111
                            },
                            "sw": {
                                "x": 5622.171,
                                "y": 4665.461
                            },
                            "nw": {
                                "x": 5630.845,
                                "y": 4670.437
                            }
                        },
                        "position": {
                            "x": 5624.02,
                            "y": 4672.286
                        },
                        "rowIdx": 21,
                        "colIdx": 0,
                        "mapInfo": "107블록 22열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 284,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00022열00014번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098503,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5624.165,
                                "y": 4661.991
                            },
                            "se": {
                                "x": 5632.839,
                                "y": 4666.967
                            },
                            "sw": {
                                "x": 5629.141,
                                "y": 4653.317
                            },
                            "nw": {
                                "x": 5637.815,
                                "y": 4658.293
                            }
                        },
                        "position": {
                            "x": 5630.99,
                            "y": 4660.142
                        },
                        "rowIdx": 21,
                        "colIdx": 1,
                        "mapInfo": "107블록 22열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 285,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00022열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    }
                ],
                "21:17": [
                    {
                        "logicalSeatId": 1446098220,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5376.105,
                                "y": 4503.561
                            },
                            "se": {
                                "x": 5384.7793,
                                "y": 4508.537
                            },
                            "sw": {
                                "x": 5381.081,
                                "y": 4494.887
                            },
                            "nw": {
                                "x": 5389.755,
                                "y": 4499.863
                            }
                        },
                        "position": {
                            "x": 5382.93,
                            "y": 4501.712
                        },
                        "rowIdx": 0,
                        "colIdx": 2,
                        "mapInfo": "107블록 1열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 2,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00001열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098221,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5383.075,
                                "y": 4491.417
                            },
                            "se": {
                                "x": 5391.749,
                                "y": 4496.393
                            },
                            "sw": {
                                "x": 5388.051,
                                "y": 4482.743
                            },
                            "nw": {
                                "x": 5396.725,
                                "y": 4487.7188
                            }
                        },
                        "position": {
                            "x": 5389.9,
                            "y": 4489.568
                        },
                        "rowIdx": 0,
                        "colIdx": 3,
                        "mapInfo": "107블록 1열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 3,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00001열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098222,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5390.035,
                                "y": 4479.273
                            },
                            "se": {
                                "x": 5398.709,
                                "y": 4484.249
                            },
                            "sw": {
                                "x": 5395.0107,
                                "y": 4470.599
                            },
                            "nw": {
                                "x": 5403.685,
                                "y": 4475.575
                            }
                        },
                        "position": {
                            "x": 5396.86,
                            "y": 4477.424
                        },
                        "rowIdx": 0,
                        "colIdx": 4,
                        "mapInfo": "107블록 1열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 4,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00001열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098223,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5397.005,
                                "y": 4467.129
                            },
                            "se": {
                                "x": 5405.6787,
                                "y": 4472.105
                            },
                            "sw": {
                                "x": 5401.981,
                                "y": 4458.455
                            },
                            "nw": {
                                "x": 5410.6553,
                                "y": 4463.431
                            }
                        },
                        "position": {
                            "x": 5403.83,
                            "y": 4465.28
                        },
                        "rowIdx": 0,
                        "colIdx": 5,
                        "mapInfo": "107블록 1열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 5,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00001열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098224,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5403.975,
                                "y": 4454.986
                            },
                            "se": {
                                "x": 5412.649,
                                "y": 4459.962
                            },
                            "sw": {
                                "x": 5408.951,
                                "y": 4446.312
                            },
                            "nw": {
                                "x": 5417.625,
                                "y": 4451.288
                            }
                        },
                        "position": {
                            "x": 5410.8,
                            "y": 4453.137
                        },
                        "rowIdx": 0,
                        "colIdx": 6,
                        "mapInfo": "107블록 1열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 6,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00001열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098225,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5410.935,
                                "y": 4442.841
                            },
                            "se": {
                                "x": 5419.609,
                                "y": 4447.817
                            },
                            "sw": {
                                "x": 5415.911,
                                "y": 4434.167
                            },
                            "nw": {
                                "x": 5424.585,
                                "y": 4439.143
                            }
                        },
                        "position": {
                            "x": 5417.76,
                            "y": 4440.992
                        },
                        "rowIdx": 0,
                        "colIdx": 7,
                        "mapInfo": "107블록 1열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 7,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00001열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098226,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5417.905,
                                "y": 4430.698
                            },
                            "se": {
                                "x": 5426.579,
                                "y": 4435.674
                            },
                            "sw": {
                                "x": 5422.881,
                                "y": 4422.024
                            },
                            "nw": {
                                "x": 5431.555,
                                "y": 4427.0
                            }
                        },
                        "position": {
                            "x": 5424.73,
                            "y": 4428.849
                        },
                        "rowIdx": 0,
                        "colIdx": 8,
                        "mapInfo": "107블록 1열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 8,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00001열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098227,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5424.8647,
                                "y": 4418.554
                            },
                            "se": {
                                "x": 5433.539,
                                "y": 4423.53
                            },
                            "sw": {
                                "x": 5429.841,
                                "y": 4409.88
                            },
                            "nw": {
                                "x": 5438.515,
                                "y": 4414.856
                            }
                        },
                        "position": {
                            "x": 5431.69,
                            "y": 4416.705
                        },
                        "rowIdx": 0,
                        "colIdx": 9,
                        "mapInfo": "107블록 1열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 9,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00001열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098228,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5431.835,
                                "y": 4406.41
                            },
                            "se": {
                                "x": 5440.509,
                                "y": 4411.3857
                            },
                            "sw": {
                                "x": 5436.811,
                                "y": 4397.736
                            },
                            "nw": {
                                "x": 5445.4854,
                                "y": 4402.712
                            }
                        },
                        "position": {
                            "x": 5438.66,
                            "y": 4404.561
                        },
                        "rowIdx": 0,
                        "colIdx": 10,
                        "mapInfo": "107블록 1열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 10,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00001열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098229,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5438.8047,
                                "y": 4394.266
                            },
                            "se": {
                                "x": 5447.479,
                                "y": 4399.242
                            },
                            "sw": {
                                "x": 5443.7812,
                                "y": 4385.592
                            },
                            "nw": {
                                "x": 5452.455,
                                "y": 4390.568
                            }
                        },
                        "position": {
                            "x": 5445.63,
                            "y": 4392.417
                        },
                        "rowIdx": 0,
                        "colIdx": 11,
                        "mapInfo": "107블록 1열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 11,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00001열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098230,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5445.7646,
                                "y": 4382.122
                            },
                            "se": {
                                "x": 5454.439,
                                "y": 4387.098
                            },
                            "sw": {
                                "x": 5450.741,
                                "y": 4373.448
                            },
                            "nw": {
                                "x": 5459.415,
                                "y": 4378.424
                            }
                        },
                        "position": {
                            "x": 5452.59,
                            "y": 4380.273
                        },
                        "rowIdx": 0,
                        "colIdx": 12,
                        "mapInfo": "107블록 1열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 12,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00001열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098231,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5452.735,
                                "y": 4369.978
                            },
                            "se": {
                                "x": 5461.409,
                                "y": 4374.954
                            },
                            "sw": {
                                "x": 5457.711,
                                "y": 4361.304
                            },
                            "nw": {
                                "x": 5466.3853,
                                "y": 4366.28
                            }
                        },
                        "position": {
                            "x": 5459.56,
                            "y": 4368.129
                        },
                        "rowIdx": 0,
                        "colIdx": 13,
                        "mapInfo": "107블록 1열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950644,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 13,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "1열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00001열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098232,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5374.315,
                                "y": 4534.815
                            },
                            "se": {
                                "x": 5382.9893,
                                "y": 4539.791
                            },
                            "sw": {
                                "x": 5379.291,
                                "y": 4526.141
                            },
                            "nw": {
                                "x": 5387.965,
                                "y": 4531.117
                            }
                        },
                        "position": {
                            "x": 5381.14,
                            "y": 4532.966
                        },
                        "rowIdx": 1,
                        "colIdx": 0,
                        "mapInfo": "107블록 2열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 14,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00002열00014번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098233,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5381.285,
                                "y": 4522.671
                            },
                            "se": {
                                "x": 5389.959,
                                "y": 4527.647
                            },
                            "sw": {
                                "x": 5386.2607,
                                "y": 4513.997
                            },
                            "nw": {
                                "x": 5394.935,
                                "y": 4518.973
                            }
                        },
                        "position": {
                            "x": 5388.11,
                            "y": 4520.822
                        },
                        "rowIdx": 1,
                        "colIdx": 1,
                        "mapInfo": "107블록 2열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 15,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00002열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098234,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5388.255,
                                "y": 4510.527
                            },
                            "se": {
                                "x": 5396.9287,
                                "y": 4515.503
                            },
                            "sw": {
                                "x": 5393.231,
                                "y": 4501.853
                            },
                            "nw": {
                                "x": 5401.9053,
                                "y": 4506.829
                            }
                        },
                        "position": {
                            "x": 5395.08,
                            "y": 4508.678
                        },
                        "rowIdx": 1,
                        "colIdx": 2,
                        "mapInfo": "107블록 2열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 16,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00002열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098235,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5395.215,
                                "y": 4498.383
                            },
                            "se": {
                                "x": 5403.889,
                                "y": 4503.359
                            },
                            "sw": {
                                "x": 5400.191,
                                "y": 4489.709
                            },
                            "nw": {
                                "x": 5408.865,
                                "y": 4494.685
                            }
                        },
                        "position": {
                            "x": 5402.04,
                            "y": 4496.534
                        },
                        "rowIdx": 1,
                        "colIdx": 3,
                        "mapInfo": "107블록 2열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 17,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00002열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098236,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5402.185,
                                "y": 4486.2393
                            },
                            "se": {
                                "x": 5410.859,
                                "y": 4491.215
                            },
                            "sw": {
                                "x": 5407.161,
                                "y": 4477.565
                            },
                            "nw": {
                                "x": 5415.835,
                                "y": 4482.541
                            }
                        },
                        "position": {
                            "x": 5409.01,
                            "y": 4484.39
                        },
                        "rowIdx": 1,
                        "colIdx": 4,
                        "mapInfo": "107블록 2열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 18,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00002열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098237,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5409.145,
                                "y": 4474.095
                            },
                            "se": {
                                "x": 5417.819,
                                "y": 4479.071
                            },
                            "sw": {
                                "x": 5414.121,
                                "y": 4465.421
                            },
                            "nw": {
                                "x": 5422.795,
                                "y": 4470.397
                            }
                        },
                        "position": {
                            "x": 5415.9697,
                            "y": 4472.246
                        },
                        "rowIdx": 1,
                        "colIdx": 5,
                        "mapInfo": "107블록 2열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 19,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00002열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098238,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5416.1147,
                                "y": 4461.951
                            },
                            "se": {
                                "x": 5424.789,
                                "y": 4466.927
                            },
                            "sw": {
                                "x": 5421.091,
                                "y": 4453.277
                            },
                            "nw": {
                                "x": 5429.765,
                                "y": 4458.253
                            }
                        },
                        "position": {
                            "x": 5422.94,
                            "y": 4460.102
                        },
                        "rowIdx": 1,
                        "colIdx": 6,
                        "mapInfo": "107블록 2열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 20,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00002열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098239,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5423.085,
                                "y": 4449.807
                            },
                            "se": {
                                "x": 5431.759,
                                "y": 4454.783
                            },
                            "sw": {
                                "x": 5428.061,
                                "y": 4441.133
                            },
                            "nw": {
                                "x": 5436.7354,
                                "y": 4446.109
                            }
                        },
                        "position": {
                            "x": 5429.91,
                            "y": 4447.958
                        },
                        "rowIdx": 1,
                        "colIdx": 7,
                        "mapInfo": "107블록 2열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 21,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00002열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098240,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5430.045,
                                "y": 4437.664
                            },
                            "se": {
                                "x": 5438.7188,
                                "y": 4442.64
                            },
                            "sw": {
                                "x": 5435.021,
                                "y": 4428.99
                            },
                            "nw": {
                                "x": 5443.6953,
                                "y": 4433.966
                            }
                        },
                        "position": {
                            "x": 5436.87,
                            "y": 4435.815
                        },
                        "rowIdx": 1,
                        "colIdx": 8,
                        "mapInfo": "107블록 2열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 22,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00002열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098241,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5437.0146,
                                "y": 4425.52
                            },
                            "se": {
                                "x": 5445.689,
                                "y": 4430.496
                            },
                            "sw": {
                                "x": 5441.991,
                                "y": 4416.8457
                            },
                            "nw": {
                                "x": 5450.665,
                                "y": 4421.822
                            }
                        },
                        "position": {
                            "x": 5443.84,
                            "y": 4423.671
                        },
                        "rowIdx": 1,
                        "colIdx": 9,
                        "mapInfo": "107블록 2열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 23,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00002열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098242,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5443.975,
                                "y": 4413.376
                            },
                            "se": {
                                "x": 5452.649,
                                "y": 4418.352
                            },
                            "sw": {
                                "x": 5448.951,
                                "y": 4404.702
                            },
                            "nw": {
                                "x": 5457.625,
                                "y": 4409.678
                            }
                        },
                        "position": {
                            "x": 5450.8,
                            "y": 4411.527
                        },
                        "rowIdx": 1,
                        "colIdx": 10,
                        "mapInfo": "107블록 2열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 24,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00002열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098243,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5450.945,
                                "y": 4401.232
                            },
                            "se": {
                                "x": 5459.619,
                                "y": 4406.208
                            },
                            "sw": {
                                "x": 5455.921,
                                "y": 4392.558
                            },
                            "nw": {
                                "x": 5464.595,
                                "y": 4397.534
                            }
                        },
                        "position": {
                            "x": 5457.77,
                            "y": 4399.383
                        },
                        "rowIdx": 1,
                        "colIdx": 11,
                        "mapInfo": "107블록 2열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 25,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00002열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098244,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5457.915,
                                "y": 4389.088
                            },
                            "se": {
                                "x": 5466.589,
                                "y": 4394.064
                            },
                            "sw": {
                                "x": 5462.891,
                                "y": 4380.414
                            },
                            "nw": {
                                "x": 5471.565,
                                "y": 4385.39
                            }
                        },
                        "position": {
                            "x": 5464.74,
                            "y": 4387.2393
                        },
                        "rowIdx": 1,
                        "colIdx": 12,
                        "mapInfo": "107블록 2열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 26,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00002열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098245,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5464.875,
                                "y": 4376.944
                            },
                            "se": {
                                "x": 5473.549,
                                "y": 4381.92
                            },
                            "sw": {
                                "x": 5469.851,
                                "y": 4368.27
                            },
                            "nw": {
                                "x": 5478.525,
                                "y": 4373.246
                            }
                        },
                        "position": {
                            "x": 5471.7,
                            "y": 4375.095
                        },
                        "rowIdx": 1,
                        "colIdx": 13,
                        "mapInfo": "107블록 2열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950658,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 27,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "2열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00002열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098246,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5393.425,
                                "y": 4529.637
                            },
                            "se": {
                                "x": 5402.099,
                                "y": 4534.613
                            },
                            "sw": {
                                "x": 5398.401,
                                "y": 4520.963
                            },
                            "nw": {
                                "x": 5407.075,
                                "y": 4525.939
                            }
                        },
                        "position": {
                            "x": 5400.25,
                            "y": 4527.788
                        },
                        "rowIdx": 2,
                        "colIdx": 1,
                        "mapInfo": "107블록 3열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 28,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00003열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098247,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5400.395,
                                "y": 4517.493
                            },
                            "se": {
                                "x": 5409.069,
                                "y": 4522.469
                            },
                            "sw": {
                                "x": 5405.371,
                                "y": 4508.819
                            },
                            "nw": {
                                "x": 5414.045,
                                "y": 4513.795
                            }
                        },
                        "position": {
                            "x": 5407.2197,
                            "y": 4515.644
                        },
                        "rowIdx": 2,
                        "colIdx": 2,
                        "mapInfo": "107블록 3열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 29,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00003열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098248,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5407.3647,
                                "y": 4505.349
                            },
                            "se": {
                                "x": 5416.039,
                                "y": 4510.325
                            },
                            "sw": {
                                "x": 5412.341,
                                "y": 4496.675
                            },
                            "nw": {
                                "x": 5421.015,
                                "y": 4501.651
                            }
                        },
                        "position": {
                            "x": 5414.19,
                            "y": 4503.5
                        },
                        "rowIdx": 2,
                        "colIdx": 3,
                        "mapInfo": "107블록 3열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 30,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00003열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098249,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5414.325,
                                "y": 4493.205
                            },
                            "se": {
                                "x": 5422.999,
                                "y": 4498.181
                            },
                            "sw": {
                                "x": 5419.301,
                                "y": 4484.531
                            },
                            "nw": {
                                "x": 5427.975,
                                "y": 4489.507
                            }
                        },
                        "position": {
                            "x": 5421.15,
                            "y": 4491.356
                        },
                        "rowIdx": 2,
                        "colIdx": 4,
                        "mapInfo": "107블록 3열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 31,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00003열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098250,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5421.295,
                                "y": 4481.061
                            },
                            "se": {
                                "x": 5429.9688,
                                "y": 4486.037
                            },
                            "sw": {
                                "x": 5426.271,
                                "y": 4472.387
                            },
                            "nw": {
                                "x": 5434.9453,
                                "y": 4477.363
                            }
                        },
                        "position": {
                            "x": 5428.12,
                            "y": 4479.212
                        },
                        "rowIdx": 2,
                        "colIdx": 5,
                        "mapInfo": "107블록 3열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 32,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00003열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098251,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5428.255,
                                "y": 4468.918
                            },
                            "se": {
                                "x": 5436.9287,
                                "y": 4473.894
                            },
                            "sw": {
                                "x": 5433.231,
                                "y": 4460.244
                            },
                            "nw": {
                                "x": 5441.9053,
                                "y": 4465.22
                            }
                        },
                        "position": {
                            "x": 5435.08,
                            "y": 4467.069
                        },
                        "rowIdx": 2,
                        "colIdx": 6,
                        "mapInfo": "107블록 3열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 33,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00003열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098252,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5435.225,
                                "y": 4456.773
                            },
                            "se": {
                                "x": 5443.899,
                                "y": 4461.749
                            },
                            "sw": {
                                "x": 5440.201,
                                "y": 4448.099
                            },
                            "nw": {
                                "x": 5448.875,
                                "y": 4453.075
                            }
                        },
                        "position": {
                            "x": 5442.05,
                            "y": 4454.924
                        },
                        "rowIdx": 2,
                        "colIdx": 7,
                        "mapInfo": "107블록 3열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 34,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00003열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098253,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5442.195,
                                "y": 4444.63
                            },
                            "se": {
                                "x": 5450.869,
                                "y": 4449.606
                            },
                            "sw": {
                                "x": 5447.171,
                                "y": 4435.956
                            },
                            "nw": {
                                "x": 5455.845,
                                "y": 4440.932
                            }
                        },
                        "position": {
                            "x": 5449.02,
                            "y": 4442.7812
                        },
                        "rowIdx": 2,
                        "colIdx": 8,
                        "mapInfo": "107블록 3열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 35,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00003열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098254,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5449.155,
                                "y": 4432.486
                            },
                            "se": {
                                "x": 5457.829,
                                "y": 4437.462
                            },
                            "sw": {
                                "x": 5454.131,
                                "y": 4423.812
                            },
                            "nw": {
                                "x": 5462.805,
                                "y": 4428.788
                            }
                        },
                        "position": {
                            "x": 5455.98,
                            "y": 4430.637
                        },
                        "rowIdx": 2,
                        "colIdx": 9,
                        "mapInfo": "107블록 3열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 36,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00003열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098255,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5456.125,
                                "y": 4420.342
                            },
                            "se": {
                                "x": 5464.799,
                                "y": 4425.3184
                            },
                            "sw": {
                                "x": 5461.101,
                                "y": 4411.668
                            },
                            "nw": {
                                "x": 5469.775,
                                "y": 4416.644
                            }
                        },
                        "position": {
                            "x": 5462.95,
                            "y": 4418.493
                        },
                        "rowIdx": 2,
                        "colIdx": 10,
                        "mapInfo": "107블록 3열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 37,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00003열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098256,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5463.085,
                                "y": 4408.198
                            },
                            "se": {
                                "x": 5471.759,
                                "y": 4413.174
                            },
                            "sw": {
                                "x": 5468.061,
                                "y": 4399.524
                            },
                            "nw": {
                                "x": 5476.7354,
                                "y": 4404.5
                            }
                        },
                        "position": {
                            "x": 5469.91,
                            "y": 4406.349
                        },
                        "rowIdx": 2,
                        "colIdx": 11,
                        "mapInfo": "107블록 3열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 38,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00003열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098257,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5470.0547,
                                "y": 4396.054
                            },
                            "se": {
                                "x": 5478.729,
                                "y": 4401.03
                            },
                            "sw": {
                                "x": 5475.0312,
                                "y": 4387.38
                            },
                            "nw": {
                                "x": 5483.705,
                                "y": 4392.356
                            }
                        },
                        "position": {
                            "x": 5476.88,
                            "y": 4394.205
                        },
                        "rowIdx": 2,
                        "colIdx": 12,
                        "mapInfo": "107블록 3열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 39,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00003열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098258,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5477.025,
                                "y": 4383.91
                            },
                            "se": {
                                "x": 5485.699,
                                "y": 4388.8857
                            },
                            "sw": {
                                "x": 5482.001,
                                "y": 4375.236
                            },
                            "nw": {
                                "x": 5490.675,
                                "y": 4380.212
                            }
                        },
                        "position": {
                            "x": 5483.85,
                            "y": 4382.061
                        },
                        "rowIdx": 2,
                        "colIdx": 13,
                        "mapInfo": "107블록 3열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950671,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 40,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "3열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00003열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098259,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5398.605,
                                "y": 4548.747
                            },
                            "se": {
                                "x": 5407.2793,
                                "y": 4553.723
                            },
                            "sw": {
                                "x": 5403.581,
                                "y": 4540.073
                            },
                            "nw": {
                                "x": 5412.255,
                                "y": 4545.049
                            }
                        },
                        "position": {
                            "x": 5405.43,
                            "y": 4546.898
                        },
                        "rowIdx": 3,
                        "colIdx": 0,
                        "mapInfo": "107블록 4열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 41,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00004열00014번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098260,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5405.575,
                                "y": 4536.603
                            },
                            "se": {
                                "x": 5414.249,
                                "y": 4541.579
                            },
                            "sw": {
                                "x": 5410.551,
                                "y": 4527.929
                            },
                            "nw": {
                                "x": 5419.225,
                                "y": 4532.905
                            }
                        },
                        "position": {
                            "x": 5412.4,
                            "y": 4534.754
                        },
                        "rowIdx": 3,
                        "colIdx": 1,
                        "mapInfo": "107블록 4열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 42,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00004열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098261,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5412.535,
                                "y": 4524.459
                            },
                            "se": {
                                "x": 5421.209,
                                "y": 4529.435
                            },
                            "sw": {
                                "x": 5417.5107,
                                "y": 4515.785
                            },
                            "nw": {
                                "x": 5426.185,
                                "y": 4520.7607
                            }
                        },
                        "position": {
                            "x": 5419.36,
                            "y": 4522.61
                        },
                        "rowIdx": 3,
                        "colIdx": 2,
                        "mapInfo": "107블록 4열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 43,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00004열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098262,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5419.505,
                                "y": 4512.315
                            },
                            "se": {
                                "x": 5428.1787,
                                "y": 4517.291
                            },
                            "sw": {
                                "x": 5424.481,
                                "y": 4503.641
                            },
                            "nw": {
                                "x": 5433.1553,
                                "y": 4508.617
                            }
                        },
                        "position": {
                            "x": 5426.33,
                            "y": 4510.466
                        },
                        "rowIdx": 3,
                        "colIdx": 3,
                        "mapInfo": "107블록 4열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 44,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00004열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098263,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5426.475,
                                "y": 4500.171
                            },
                            "se": {
                                "x": 5435.149,
                                "y": 4505.147
                            },
                            "sw": {
                                "x": 5431.451,
                                "y": 4491.497
                            },
                            "nw": {
                                "x": 5440.125,
                                "y": 4496.473
                            }
                        },
                        "position": {
                            "x": 5433.3,
                            "y": 4498.322
                        },
                        "rowIdx": 3,
                        "colIdx": 4,
                        "mapInfo": "107블록 4열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 45,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00004열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098264,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5433.435,
                                "y": 4488.027
                            },
                            "se": {
                                "x": 5442.109,
                                "y": 4493.003
                            },
                            "sw": {
                                "x": 5438.411,
                                "y": 4479.353
                            },
                            "nw": {
                                "x": 5447.085,
                                "y": 4484.329
                            }
                        },
                        "position": {
                            "x": 5440.26,
                            "y": 4486.178
                        },
                        "rowIdx": 3,
                        "colIdx": 5,
                        "mapInfo": "107블록 4열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 46,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00004열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098265,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5440.405,
                                "y": 4475.883
                            },
                            "se": {
                                "x": 5449.079,
                                "y": 4480.859
                            },
                            "sw": {
                                "x": 5445.381,
                                "y": 4467.209
                            },
                            "nw": {
                                "x": 5454.055,
                                "y": 4472.185
                            }
                        },
                        "position": {
                            "x": 5447.23,
                            "y": 4474.034
                        },
                        "rowIdx": 3,
                        "colIdx": 6,
                        "mapInfo": "107블록 4열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 47,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00004열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098266,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5447.3647,
                                "y": 4463.74
                            },
                            "se": {
                                "x": 5456.039,
                                "y": 4468.716
                            },
                            "sw": {
                                "x": 5452.341,
                                "y": 4455.066
                            },
                            "nw": {
                                "x": 5461.015,
                                "y": 4460.042
                            }
                        },
                        "position": {
                            "x": 5454.19,
                            "y": 4461.891
                        },
                        "rowIdx": 3,
                        "colIdx": 7,
                        "mapInfo": "107블록 4열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 48,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00004열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098267,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5454.335,
                                "y": 4451.596
                            },
                            "se": {
                                "x": 5463.009,
                                "y": 4456.5723
                            },
                            "sw": {
                                "x": 5459.311,
                                "y": 4442.922
                            },
                            "nw": {
                                "x": 5467.9854,
                                "y": 4447.898
                            }
                        },
                        "position": {
                            "x": 5461.16,
                            "y": 4449.747
                        },
                        "rowIdx": 3,
                        "colIdx": 8,
                        "mapInfo": "107블록 4열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 49,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00004열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098268,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5461.3047,
                                "y": 4439.452
                            },
                            "se": {
                                "x": 5469.979,
                                "y": 4444.428
                            },
                            "sw": {
                                "x": 5466.2812,
                                "y": 4430.778
                            },
                            "nw": {
                                "x": 5474.955,
                                "y": 4435.754
                            }
                        },
                        "position": {
                            "x": 5468.13,
                            "y": 4437.603
                        },
                        "rowIdx": 3,
                        "colIdx": 9,
                        "mapInfo": "107블록 4열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 50,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00004열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098269,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5468.2646,
                                "y": 4427.308
                            },
                            "se": {
                                "x": 5476.939,
                                "y": 4432.284
                            },
                            "sw": {
                                "x": 5473.241,
                                "y": 4418.634
                            },
                            "nw": {
                                "x": 5481.915,
                                "y": 4423.61
                            }
                        },
                        "position": {
                            "x": 5475.09,
                            "y": 4425.459
                        },
                        "rowIdx": 3,
                        "colIdx": 10,
                        "mapInfo": "107블록 4열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 51,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00004열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098270,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5475.235,
                                "y": 4415.164
                            },
                            "se": {
                                "x": 5483.909,
                                "y": 4420.14
                            },
                            "sw": {
                                "x": 5480.211,
                                "y": 4406.49
                            },
                            "nw": {
                                "x": 5488.8853,
                                "y": 4411.466
                            }
                        },
                        "position": {
                            "x": 5482.06,
                            "y": 4413.315
                        },
                        "rowIdx": 3,
                        "colIdx": 11,
                        "mapInfo": "107블록 4열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 52,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00004열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098271,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5482.195,
                                "y": 4403.02
                            },
                            "se": {
                                "x": 5490.869,
                                "y": 4407.996
                            },
                            "sw": {
                                "x": 5487.171,
                                "y": 4394.3457
                            },
                            "nw": {
                                "x": 5495.845,
                                "y": 4399.322
                            }
                        },
                        "position": {
                            "x": 5489.02,
                            "y": 4401.171
                        },
                        "rowIdx": 3,
                        "colIdx": 12,
                        "mapInfo": "107블록 4열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 53,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00004열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098272,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5489.165,
                                "y": 4390.876
                            },
                            "se": {
                                "x": 5497.839,
                                "y": 4395.852
                            },
                            "sw": {
                                "x": 5494.141,
                                "y": 4382.202
                            },
                            "nw": {
                                "x": 5502.815,
                                "y": 4387.178
                            }
                        },
                        "position": {
                            "x": 5495.99,
                            "y": 4389.027
                        },
                        "rowIdx": 3,
                        "colIdx": 13,
                        "mapInfo": "107블록 4열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950685,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 54,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "4열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00004열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098273,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5417.715,
                                "y": 4543.569
                            },
                            "se": {
                                "x": 5426.389,
                                "y": 4548.545
                            },
                            "sw": {
                                "x": 5422.691,
                                "y": 4534.895
                            },
                            "nw": {
                                "x": 5431.365,
                                "y": 4539.871
                            }
                        },
                        "position": {
                            "x": 5424.54,
                            "y": 4541.72
                        },
                        "rowIdx": 4,
                        "colIdx": 1,
                        "mapInfo": "107블록 5열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 55,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00005열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098274,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5424.685,
                                "y": 4531.425
                            },
                            "se": {
                                "x": 5433.359,
                                "y": 4536.401
                            },
                            "sw": {
                                "x": 5429.661,
                                "y": 4522.751
                            },
                            "nw": {
                                "x": 5438.335,
                                "y": 4527.727
                            }
                        },
                        "position": {
                            "x": 5431.51,
                            "y": 4529.576
                        },
                        "rowIdx": 4,
                        "colIdx": 2,
                        "mapInfo": "107블록 5열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 56,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00005열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098275,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5431.645,
                                "y": 4519.2812
                            },
                            "se": {
                                "x": 5440.319,
                                "y": 4524.257
                            },
                            "sw": {
                                "x": 5436.621,
                                "y": 4510.607
                            },
                            "nw": {
                                "x": 5445.295,
                                "y": 4515.583
                            }
                        },
                        "position": {
                            "x": 5438.4697,
                            "y": 4517.432
                        },
                        "rowIdx": 4,
                        "colIdx": 3,
                        "mapInfo": "107블록 5열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 57,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00005열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098276,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5438.6147,
                                "y": 4507.137
                            },
                            "se": {
                                "x": 5447.289,
                                "y": 4512.113
                            },
                            "sw": {
                                "x": 5443.591,
                                "y": 4498.463
                            },
                            "nw": {
                                "x": 5452.265,
                                "y": 4503.439
                            }
                        },
                        "position": {
                            "x": 5445.44,
                            "y": 4505.288
                        },
                        "rowIdx": 4,
                        "colIdx": 4,
                        "mapInfo": "107블록 5열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 58,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00005열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098277,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5445.585,
                                "y": 4494.993
                            },
                            "se": {
                                "x": 5454.259,
                                "y": 4499.969
                            },
                            "sw": {
                                "x": 5450.561,
                                "y": 4486.319
                            },
                            "nw": {
                                "x": 5459.2354,
                                "y": 4491.295
                            }
                        },
                        "position": {
                            "x": 5452.41,
                            "y": 4493.144
                        },
                        "rowIdx": 4,
                        "colIdx": 5,
                        "mapInfo": "107블록 5열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 59,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00005열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098278,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5452.545,
                                "y": 4482.849
                            },
                            "se": {
                                "x": 5461.2188,
                                "y": 4487.825
                            },
                            "sw": {
                                "x": 5457.521,
                                "y": 4474.175
                            },
                            "nw": {
                                "x": 5466.1953,
                                "y": 4479.151
                            }
                        },
                        "position": {
                            "x": 5459.37,
                            "y": 4481.0
                        },
                        "rowIdx": 4,
                        "colIdx": 6,
                        "mapInfo": "107블록 5열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 60,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00005열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098279,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5459.5146,
                                "y": 4470.706
                            },
                            "se": {
                                "x": 5468.189,
                                "y": 4475.682
                            },
                            "sw": {
                                "x": 5464.491,
                                "y": 4462.032
                            },
                            "nw": {
                                "x": 5473.165,
                                "y": 4467.008
                            }
                        },
                        "position": {
                            "x": 5466.34,
                            "y": 4468.857
                        },
                        "rowIdx": 4,
                        "colIdx": 7,
                        "mapInfo": "107블록 5열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 61,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00005열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098280,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5466.475,
                                "y": 4458.562
                            },
                            "se": {
                                "x": 5475.149,
                                "y": 4463.538
                            },
                            "sw": {
                                "x": 5471.451,
                                "y": 4449.888
                            },
                            "nw": {
                                "x": 5480.125,
                                "y": 4454.8643
                            }
                        },
                        "position": {
                            "x": 5473.3,
                            "y": 4456.713
                        },
                        "rowIdx": 4,
                        "colIdx": 8,
                        "mapInfo": "107블록 5열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 62,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00005열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098281,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5473.445,
                                "y": 4446.418
                            },
                            "se": {
                                "x": 5482.119,
                                "y": 4451.394
                            },
                            "sw": {
                                "x": 5478.421,
                                "y": 4437.744
                            },
                            "nw": {
                                "x": 5487.095,
                                "y": 4442.72
                            }
                        },
                        "position": {
                            "x": 5480.27,
                            "y": 4444.569
                        },
                        "rowIdx": 4,
                        "colIdx": 9,
                        "mapInfo": "107블록 5열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 63,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00005열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098282,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5480.415,
                                "y": 4434.274
                            },
                            "se": {
                                "x": 5489.089,
                                "y": 4439.25
                            },
                            "sw": {
                                "x": 5485.391,
                                "y": 4425.6
                            },
                            "nw": {
                                "x": 5494.065,
                                "y": 4430.576
                            }
                        },
                        "position": {
                            "x": 5487.24,
                            "y": 4432.425
                        },
                        "rowIdx": 4,
                        "colIdx": 10,
                        "mapInfo": "107블록 5열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 64,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00005열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098283,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5487.375,
                                "y": 4422.13
                            },
                            "se": {
                                "x": 5496.049,
                                "y": 4427.106
                            },
                            "sw": {
                                "x": 5492.351,
                                "y": 4413.456
                            },
                            "nw": {
                                "x": 5501.025,
                                "y": 4418.432
                            }
                        },
                        "position": {
                            "x": 5494.2,
                            "y": 4420.2812
                        },
                        "rowIdx": 4,
                        "colIdx": 11,
                        "mapInfo": "107블록 5열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 65,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00005열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098284,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5494.3447,
                                "y": 4409.986
                            },
                            "se": {
                                "x": 5503.019,
                                "y": 4414.962
                            },
                            "sw": {
                                "x": 5499.3213,
                                "y": 4401.312
                            },
                            "nw": {
                                "x": 5507.995,
                                "y": 4406.288
                            }
                        },
                        "position": {
                            "x": 5501.17,
                            "y": 4408.137
                        },
                        "rowIdx": 4,
                        "colIdx": 12,
                        "mapInfo": "107블록 5열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 66,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00005열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098285,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5501.3047,
                                "y": 4397.842
                            },
                            "se": {
                                "x": 5509.979,
                                "y": 4402.8184
                            },
                            "sw": {
                                "x": 5506.2812,
                                "y": 4389.168
                            },
                            "nw": {
                                "x": 5514.955,
                                "y": 4394.144
                            }
                        },
                        "position": {
                            "x": 5508.13,
                            "y": 4395.993
                        },
                        "rowIdx": 4,
                        "colIdx": 13,
                        "mapInfo": "107블록 5열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950698,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 67,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "5열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00005열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098286,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5422.895,
                                "y": 4562.679
                            },
                            "se": {
                                "x": 5431.569,
                                "y": 4567.655
                            },
                            "sw": {
                                "x": 5427.871,
                                "y": 4554.005
                            },
                            "nw": {
                                "x": 5436.545,
                                "y": 4558.981
                            }
                        },
                        "position": {
                            "x": 5429.7197,
                            "y": 4560.83
                        },
                        "rowIdx": 5,
                        "colIdx": 0,
                        "mapInfo": "107블록 6열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 68,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00006열00014번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098287,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5429.8647,
                                "y": 4550.535
                            },
                            "se": {
                                "x": 5438.539,
                                "y": 4555.5107
                            },
                            "sw": {
                                "x": 5434.841,
                                "y": 4541.861
                            },
                            "nw": {
                                "x": 5443.515,
                                "y": 4546.837
                            }
                        },
                        "position": {
                            "x": 5436.69,
                            "y": 4548.686
                        },
                        "rowIdx": 5,
                        "colIdx": 1,
                        "mapInfo": "107블록 6열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 69,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00006열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098288,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5436.825,
                                "y": 4538.391
                            },
                            "se": {
                                "x": 5445.499,
                                "y": 4543.367
                            },
                            "sw": {
                                "x": 5441.801,
                                "y": 4529.717
                            },
                            "nw": {
                                "x": 5450.475,
                                "y": 4534.693
                            }
                        },
                        "position": {
                            "x": 5443.65,
                            "y": 4536.542
                        },
                        "rowIdx": 5,
                        "colIdx": 2,
                        "mapInfo": "107블록 6열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 70,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00006열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098289,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5443.795,
                                "y": 4526.247
                            },
                            "se": {
                                "x": 5452.4688,
                                "y": 4531.223
                            },
                            "sw": {
                                "x": 5448.771,
                                "y": 4517.573
                            },
                            "nw": {
                                "x": 5457.4453,
                                "y": 4522.549
                            }
                        },
                        "position": {
                            "x": 5450.62,
                            "y": 4524.398
                        },
                        "rowIdx": 5,
                        "colIdx": 3,
                        "mapInfo": "107블록 6열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 71,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00006열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098290,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5450.755,
                                "y": 4514.103
                            },
                            "se": {
                                "x": 5459.4287,
                                "y": 4519.079
                            },
                            "sw": {
                                "x": 5455.731,
                                "y": 4505.429
                            },
                            "nw": {
                                "x": 5464.4053,
                                "y": 4510.405
                            }
                        },
                        "position": {
                            "x": 5457.58,
                            "y": 4512.254
                        },
                        "rowIdx": 5,
                        "colIdx": 4,
                        "mapInfo": "107블록 6열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 72,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00006열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098291,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5457.725,
                                "y": 4501.959
                            },
                            "se": {
                                "x": 5466.399,
                                "y": 4506.935
                            },
                            "sw": {
                                "x": 5462.701,
                                "y": 4493.285
                            },
                            "nw": {
                                "x": 5471.375,
                                "y": 4498.2607
                            }
                        },
                        "position": {
                            "x": 5464.55,
                            "y": 4500.11
                        },
                        "rowIdx": 5,
                        "colIdx": 5,
                        "mapInfo": "107블록 6열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 73,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00006열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098292,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5464.695,
                                "y": 4489.815
                            },
                            "se": {
                                "x": 5473.369,
                                "y": 4494.791
                            },
                            "sw": {
                                "x": 5469.671,
                                "y": 4481.141
                            },
                            "nw": {
                                "x": 5478.345,
                                "y": 4486.117
                            }
                        },
                        "position": {
                            "x": 5471.52,
                            "y": 4487.966
                        },
                        "rowIdx": 5,
                        "colIdx": 6,
                        "mapInfo": "107블록 6열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 74,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00006열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098293,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5471.655,
                                "y": 4477.672
                            },
                            "se": {
                                "x": 5480.329,
                                "y": 4482.648
                            },
                            "sw": {
                                "x": 5476.631,
                                "y": 4468.998
                            },
                            "nw": {
                                "x": 5485.305,
                                "y": 4473.974
                            }
                        },
                        "position": {
                            "x": 5478.48,
                            "y": 4475.823
                        },
                        "rowIdx": 5,
                        "colIdx": 7,
                        "mapInfo": "107블록 6열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 75,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00006열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098294,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5478.625,
                                "y": 4465.528
                            },
                            "se": {
                                "x": 5487.299,
                                "y": 4470.504
                            },
                            "sw": {
                                "x": 5483.601,
                                "y": 4456.854
                            },
                            "nw": {
                                "x": 5492.275,
                                "y": 4461.83
                            }
                        },
                        "position": {
                            "x": 5485.45,
                            "y": 4463.679
                        },
                        "rowIdx": 5,
                        "colIdx": 8,
                        "mapInfo": "107블록 6열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 76,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00006열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098295,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5485.585,
                                "y": 4453.384
                            },
                            "se": {
                                "x": 5494.259,
                                "y": 4458.36
                            },
                            "sw": {
                                "x": 5490.561,
                                "y": 4444.71
                            },
                            "nw": {
                                "x": 5499.2354,
                                "y": 4449.686
                            }
                        },
                        "position": {
                            "x": 5492.41,
                            "y": 4451.535
                        },
                        "rowIdx": 5,
                        "colIdx": 9,
                        "mapInfo": "107블록 6열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 77,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00006열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098296,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5492.5547,
                                "y": 4441.24
                            },
                            "se": {
                                "x": 5501.229,
                                "y": 4446.216
                            },
                            "sw": {
                                "x": 5497.5312,
                                "y": 4432.566
                            },
                            "nw": {
                                "x": 5506.205,
                                "y": 4437.542
                            }
                        },
                        "position": {
                            "x": 5499.38,
                            "y": 4439.391
                        },
                        "rowIdx": 5,
                        "colIdx": 10,
                        "mapInfo": "107블록 6열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 78,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00006열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098297,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5499.525,
                                "y": 4429.096
                            },
                            "se": {
                                "x": 5508.199,
                                "y": 4434.0723
                            },
                            "sw": {
                                "x": 5504.501,
                                "y": 4420.422
                            },
                            "nw": {
                                "x": 5513.175,
                                "y": 4425.398
                            }
                        },
                        "position": {
                            "x": 5506.35,
                            "y": 4427.247
                        },
                        "rowIdx": 5,
                        "colIdx": 11,
                        "mapInfo": "107블록 6열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 79,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00006열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098298,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5506.485,
                                "y": 4416.952
                            },
                            "se": {
                                "x": 5515.159,
                                "y": 4421.928
                            },
                            "sw": {
                                "x": 5511.461,
                                "y": 4408.278
                            },
                            "nw": {
                                "x": 5520.1353,
                                "y": 4413.254
                            }
                        },
                        "position": {
                            "x": 5513.31,
                            "y": 4415.103
                        },
                        "rowIdx": 5,
                        "colIdx": 12,
                        "mapInfo": "107블록 6열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 80,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00006열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098299,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5513.455,
                                "y": 4404.808
                            },
                            "se": {
                                "x": 5522.129,
                                "y": 4409.784
                            },
                            "sw": {
                                "x": 5518.431,
                                "y": 4396.134
                            },
                            "nw": {
                                "x": 5527.105,
                                "y": 4401.11
                            }
                        },
                        "position": {
                            "x": 5520.2803,
                            "y": 4402.959
                        },
                        "rowIdx": 5,
                        "colIdx": 13,
                        "mapInfo": "107블록 6열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950712,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 81,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "6열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00006열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098300,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5442.005,
                                "y": 4557.501
                            },
                            "se": {
                                "x": 5450.6787,
                                "y": 4562.477
                            },
                            "sw": {
                                "x": 5446.981,
                                "y": 4548.827
                            },
                            "nw": {
                                "x": 5455.6553,
                                "y": 4553.803
                            }
                        },
                        "position": {
                            "x": 5448.83,
                            "y": 4555.652
                        },
                        "rowIdx": 6,
                        "colIdx": 1,
                        "mapInfo": "107블록 7열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 82,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00007열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098301,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5448.975,
                                "y": 4545.357
                            },
                            "se": {
                                "x": 5457.649,
                                "y": 4550.333
                            },
                            "sw": {
                                "x": 5453.951,
                                "y": 4536.683
                            },
                            "nw": {
                                "x": 5462.625,
                                "y": 4541.659
                            }
                        },
                        "position": {
                            "x": 5455.8,
                            "y": 4543.508
                        },
                        "rowIdx": 6,
                        "colIdx": 2,
                        "mapInfo": "107블록 7열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 83,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00007열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098302,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5455.935,
                                "y": 4533.213
                            },
                            "se": {
                                "x": 5464.609,
                                "y": 4538.189
                            },
                            "sw": {
                                "x": 5460.911,
                                "y": 4524.539
                            },
                            "nw": {
                                "x": 5469.585,
                                "y": 4529.515
                            }
                        },
                        "position": {
                            "x": 5462.76,
                            "y": 4531.3643
                        },
                        "rowIdx": 6,
                        "colIdx": 3,
                        "mapInfo": "107블록 7열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 84,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00007열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098303,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5462.905,
                                "y": 4521.069
                            },
                            "se": {
                                "x": 5471.579,
                                "y": 4526.045
                            },
                            "sw": {
                                "x": 5467.881,
                                "y": 4512.395
                            },
                            "nw": {
                                "x": 5476.555,
                                "y": 4517.371
                            }
                        },
                        "position": {
                            "x": 5469.73,
                            "y": 4519.22
                        },
                        "rowIdx": 6,
                        "colIdx": 4,
                        "mapInfo": "107블록 7열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 85,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00007열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098304,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5469.8647,
                                "y": 4508.925
                            },
                            "se": {
                                "x": 5478.539,
                                "y": 4513.901
                            },
                            "sw": {
                                "x": 5474.841,
                                "y": 4500.251
                            },
                            "nw": {
                                "x": 5483.515,
                                "y": 4505.227
                            }
                        },
                        "position": {
                            "x": 5476.69,
                            "y": 4507.076
                        },
                        "rowIdx": 6,
                        "colIdx": 5,
                        "mapInfo": "107블록 7열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 86,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00007열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098305,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5476.835,
                                "y": 4496.7812
                            },
                            "se": {
                                "x": 5485.509,
                                "y": 4501.757
                            },
                            "sw": {
                                "x": 5481.811,
                                "y": 4488.107
                            },
                            "nw": {
                                "x": 5490.4854,
                                "y": 4493.083
                            }
                        },
                        "position": {
                            "x": 5483.66,
                            "y": 4494.932
                        },
                        "rowIdx": 6,
                        "colIdx": 6,
                        "mapInfo": "107블록 7열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 87,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00007열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098306,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5483.8047,
                                "y": 4484.638
                            },
                            "se": {
                                "x": 5492.479,
                                "y": 4489.6143
                            },
                            "sw": {
                                "x": 5488.7812,
                                "y": 4475.964
                            },
                            "nw": {
                                "x": 5497.455,
                                "y": 4480.94
                            }
                        },
                        "position": {
                            "x": 5490.63,
                            "y": 4482.789
                        },
                        "rowIdx": 6,
                        "colIdx": 7,
                        "mapInfo": "107블록 7열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 88,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00007열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098307,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5490.7646,
                                "y": 4472.494
                            },
                            "se": {
                                "x": 5499.439,
                                "y": 4477.47
                            },
                            "sw": {
                                "x": 5495.741,
                                "y": 4463.82
                            },
                            "nw": {
                                "x": 5504.415,
                                "y": 4468.796
                            }
                        },
                        "position": {
                            "x": 5497.59,
                            "y": 4470.645
                        },
                        "rowIdx": 6,
                        "colIdx": 8,
                        "mapInfo": "107블록 7열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 89,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00007열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098308,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5497.735,
                                "y": 4460.35
                            },
                            "se": {
                                "x": 5506.409,
                                "y": 4465.326
                            },
                            "sw": {
                                "x": 5502.711,
                                "y": 4451.676
                            },
                            "nw": {
                                "x": 5511.3853,
                                "y": 4456.652
                            }
                        },
                        "position": {
                            "x": 5504.56,
                            "y": 4458.501
                        },
                        "rowIdx": 6,
                        "colIdx": 9,
                        "mapInfo": "107블록 7열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 90,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00007열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098309,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5504.695,
                                "y": 4448.206
                            },
                            "se": {
                                "x": 5513.369,
                                "y": 4453.182
                            },
                            "sw": {
                                "x": 5509.671,
                                "y": 4439.532
                            },
                            "nw": {
                                "x": 5518.345,
                                "y": 4444.508
                            }
                        },
                        "position": {
                            "x": 5511.52,
                            "y": 4446.357
                        },
                        "rowIdx": 6,
                        "colIdx": 10,
                        "mapInfo": "107블록 7열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 91,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00007열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098310,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5511.665,
                                "y": 4436.062
                            },
                            "se": {
                                "x": 5520.339,
                                "y": 4441.038
                            },
                            "sw": {
                                "x": 5516.641,
                                "y": 4427.388
                            },
                            "nw": {
                                "x": 5525.315,
                                "y": 4432.3643
                            }
                        },
                        "position": {
                            "x": 5518.49,
                            "y": 4434.213
                        },
                        "rowIdx": 6,
                        "colIdx": 11,
                        "mapInfo": "107블록 7열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 92,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00007열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098311,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5518.635,
                                "y": 4423.918
                            },
                            "se": {
                                "x": 5527.309,
                                "y": 4428.894
                            },
                            "sw": {
                                "x": 5523.611,
                                "y": 4415.244
                            },
                            "nw": {
                                "x": 5532.285,
                                "y": 4420.22
                            }
                        },
                        "position": {
                            "x": 5525.46,
                            "y": 4422.069
                        },
                        "rowIdx": 6,
                        "colIdx": 12,
                        "mapInfo": "107블록 7열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 93,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00007열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098312,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5525.5947,
                                "y": 4411.774
                            },
                            "se": {
                                "x": 5534.269,
                                "y": 4416.75
                            },
                            "sw": {
                                "x": 5530.5713,
                                "y": 4403.1
                            },
                            "nw": {
                                "x": 5539.245,
                                "y": 4408.076
                            }
                        },
                        "position": {
                            "x": 5532.42,
                            "y": 4409.925
                        },
                        "rowIdx": 6,
                        "colIdx": 13,
                        "mapInfo": "107블록 7열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950725,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 94,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "7열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00007열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098313,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5447.185,
                                "y": 4576.611
                            },
                            "se": {
                                "x": 5455.859,
                                "y": 4581.587
                            },
                            "sw": {
                                "x": 5452.161,
                                "y": 4567.937
                            },
                            "nw": {
                                "x": 5460.835,
                                "y": 4572.913
                            }
                        },
                        "position": {
                            "x": 5454.01,
                            "y": 4574.762
                        },
                        "rowIdx": 7,
                        "colIdx": 0,
                        "mapInfo": "107블록 8열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 95,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00008열00014번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098314,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5454.145,
                                "y": 4564.467
                            },
                            "se": {
                                "x": 5462.819,
                                "y": 4569.4434
                            },
                            "sw": {
                                "x": 5459.121,
                                "y": 4555.793
                            },
                            "nw": {
                                "x": 5467.795,
                                "y": 4560.769
                            }
                        },
                        "position": {
                            "x": 5460.9697,
                            "y": 4562.618
                        },
                        "rowIdx": 7,
                        "colIdx": 1,
                        "mapInfo": "107블록 8열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 96,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00008열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098315,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5461.1147,
                                "y": 4552.323
                            },
                            "se": {
                                "x": 5469.789,
                                "y": 4557.299
                            },
                            "sw": {
                                "x": 5466.091,
                                "y": 4543.649
                            },
                            "nw": {
                                "x": 5474.765,
                                "y": 4548.625
                            }
                        },
                        "position": {
                            "x": 5467.94,
                            "y": 4550.474
                        },
                        "rowIdx": 7,
                        "colIdx": 2,
                        "mapInfo": "107블록 8열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 97,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00008열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098316,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5468.085,
                                "y": 4540.179
                            },
                            "se": {
                                "x": 5476.759,
                                "y": 4545.155
                            },
                            "sw": {
                                "x": 5473.061,
                                "y": 4531.505
                            },
                            "nw": {
                                "x": 5481.7354,
                                "y": 4536.481
                            }
                        },
                        "position": {
                            "x": 5474.91,
                            "y": 4538.33
                        },
                        "rowIdx": 7,
                        "colIdx": 3,
                        "mapInfo": "107블록 8열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 98,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00008열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098317,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5475.045,
                                "y": 4528.035
                            },
                            "se": {
                                "x": 5483.7188,
                                "y": 4533.0107
                            },
                            "sw": {
                                "x": 5480.021,
                                "y": 4519.361
                            },
                            "nw": {
                                "x": 5488.6953,
                                "y": 4524.337
                            }
                        },
                        "position": {
                            "x": 5481.87,
                            "y": 4526.186
                        },
                        "rowIdx": 7,
                        "colIdx": 4,
                        "mapInfo": "107블록 8열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 99,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00008열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098318,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5482.0146,
                                "y": 4515.891
                            },
                            "se": {
                                "x": 5490.689,
                                "y": 4520.867
                            },
                            "sw": {
                                "x": 5486.991,
                                "y": 4507.217
                            },
                            "nw": {
                                "x": 5495.665,
                                "y": 4512.193
                            }
                        },
                        "position": {
                            "x": 5488.84,
                            "y": 4514.042
                        },
                        "rowIdx": 7,
                        "colIdx": 5,
                        "mapInfo": "107블록 8열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 100,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00008열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098319,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5488.975,
                                "y": 4503.747
                            },
                            "se": {
                                "x": 5497.649,
                                "y": 4508.723
                            },
                            "sw": {
                                "x": 5493.951,
                                "y": 4495.073
                            },
                            "nw": {
                                "x": 5502.625,
                                "y": 4500.049
                            }
                        },
                        "position": {
                            "x": 5495.8,
                            "y": 4501.898
                        },
                        "rowIdx": 7,
                        "colIdx": 6,
                        "mapInfo": "107블록 8열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 101,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00008열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098320,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5495.945,
                                "y": 4491.603
                            },
                            "se": {
                                "x": 5504.619,
                                "y": 4496.579
                            },
                            "sw": {
                                "x": 5500.921,
                                "y": 4482.929
                            },
                            "nw": {
                                "x": 5509.595,
                                "y": 4487.905
                            }
                        },
                        "position": {
                            "x": 5502.77,
                            "y": 4489.754
                        },
                        "rowIdx": 7,
                        "colIdx": 7,
                        "mapInfo": "107블록 8열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 102,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00008열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098321,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5502.915,
                                "y": 4479.46
                            },
                            "se": {
                                "x": 5511.589,
                                "y": 4484.436
                            },
                            "sw": {
                                "x": 5507.891,
                                "y": 4470.786
                            },
                            "nw": {
                                "x": 5516.565,
                                "y": 4475.762
                            }
                        },
                        "position": {
                            "x": 5509.74,
                            "y": 4477.611
                        },
                        "rowIdx": 7,
                        "colIdx": 8,
                        "mapInfo": "107블록 8열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 103,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00008열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098322,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5509.875,
                                "y": 4467.316
                            },
                            "se": {
                                "x": 5518.549,
                                "y": 4472.292
                            },
                            "sw": {
                                "x": 5514.851,
                                "y": 4458.642
                            },
                            "nw": {
                                "x": 5523.525,
                                "y": 4463.618
                            }
                        },
                        "position": {
                            "x": 5516.7,
                            "y": 4465.467
                        },
                        "rowIdx": 7,
                        "colIdx": 9,
                        "mapInfo": "107블록 8열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 104,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00008열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098323,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5516.8447,
                                "y": 4455.172
                            },
                            "se": {
                                "x": 5525.519,
                                "y": 4460.148
                            },
                            "sw": {
                                "x": 5521.8213,
                                "y": 4446.498
                            },
                            "nw": {
                                "x": 5530.495,
                                "y": 4451.474
                            }
                        },
                        "position": {
                            "x": 5523.67,
                            "y": 4453.323
                        },
                        "rowIdx": 7,
                        "colIdx": 10,
                        "mapInfo": "107블록 8열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 105,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00008열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098324,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5523.8047,
                                "y": 4443.028
                            },
                            "se": {
                                "x": 5532.479,
                                "y": 4448.004
                            },
                            "sw": {
                                "x": 5528.7812,
                                "y": 4434.354
                            },
                            "nw": {
                                "x": 5537.455,
                                "y": 4439.33
                            }
                        },
                        "position": {
                            "x": 5530.63,
                            "y": 4441.179
                        },
                        "rowIdx": 7,
                        "colIdx": 11,
                        "mapInfo": "107블록 8열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 106,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00008열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098325,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5530.775,
                                "y": 4430.884
                            },
                            "se": {
                                "x": 5539.449,
                                "y": 4435.86
                            },
                            "sw": {
                                "x": 5535.751,
                                "y": 4422.21
                            },
                            "nw": {
                                "x": 5544.425,
                                "y": 4427.186
                            }
                        },
                        "position": {
                            "x": 5537.6,
                            "y": 4429.035
                        },
                        "rowIdx": 7,
                        "colIdx": 12,
                        "mapInfo": "107블록 8열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 107,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00008열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098326,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5537.745,
                                "y": 4418.74
                            },
                            "se": {
                                "x": 5546.419,
                                "y": 4423.716
                            },
                            "sw": {
                                "x": 5542.7207,
                                "y": 4410.066
                            },
                            "nw": {
                                "x": 5551.395,
                                "y": 4415.042
                            }
                        },
                        "position": {
                            "x": 5544.57,
                            "y": 4416.891
                        },
                        "rowIdx": 7,
                        "colIdx": 13,
                        "mapInfo": "107블록 8열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950739,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 108,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "8열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00008열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098327,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5466.295,
                                "y": 4571.433
                            },
                            "se": {
                                "x": 5474.9688,
                                "y": 4576.409
                            },
                            "sw": {
                                "x": 5471.271,
                                "y": 4562.759
                            },
                            "nw": {
                                "x": 5479.9453,
                                "y": 4567.735
                            }
                        },
                        "position": {
                            "x": 5473.12,
                            "y": 4569.584
                        },
                        "rowIdx": 8,
                        "colIdx": 1,
                        "mapInfo": "107블록 9열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 109,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00009열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098328,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5473.255,
                                "y": 4559.289
                            },
                            "se": {
                                "x": 5481.9287,
                                "y": 4564.265
                            },
                            "sw": {
                                "x": 5478.231,
                                "y": 4550.615
                            },
                            "nw": {
                                "x": 5486.9053,
                                "y": 4555.591
                            }
                        },
                        "position": {
                            "x": 5480.08,
                            "y": 4557.44
                        },
                        "rowIdx": 8,
                        "colIdx": 2,
                        "mapInfo": "107블록 9열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 110,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00009열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098329,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5480.225,
                                "y": 4547.145
                            },
                            "se": {
                                "x": 5488.899,
                                "y": 4552.121
                            },
                            "sw": {
                                "x": 5485.201,
                                "y": 4538.4707
                            },
                            "nw": {
                                "x": 5493.875,
                                "y": 4543.447
                            }
                        },
                        "position": {
                            "x": 5487.05,
                            "y": 4545.296
                        },
                        "rowIdx": 8,
                        "colIdx": 3,
                        "mapInfo": "107블록 9열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 111,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00009열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098330,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5487.195,
                                "y": 4535.001
                            },
                            "se": {
                                "x": 5495.869,
                                "y": 4539.977
                            },
                            "sw": {
                                "x": 5492.171,
                                "y": 4526.327
                            },
                            "nw": {
                                "x": 5500.845,
                                "y": 4531.303
                            }
                        },
                        "position": {
                            "x": 5494.02,
                            "y": 4533.152
                        },
                        "rowIdx": 8,
                        "colIdx": 4,
                        "mapInfo": "107블록 9열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 112,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00009열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098331,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5494.155,
                                "y": 4522.857
                            },
                            "se": {
                                "x": 5502.829,
                                "y": 4527.833
                            },
                            "sw": {
                                "x": 5499.131,
                                "y": 4514.183
                            },
                            "nw": {
                                "x": 5507.805,
                                "y": 4519.159
                            }
                        },
                        "position": {
                            "x": 5500.98,
                            "y": 4521.008
                        },
                        "rowIdx": 8,
                        "colIdx": 5,
                        "mapInfo": "107블록 9열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 113,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00009열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098332,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5501.125,
                                "y": 4510.713
                            },
                            "se": {
                                "x": 5509.799,
                                "y": 4515.689
                            },
                            "sw": {
                                "x": 5506.101,
                                "y": 4502.039
                            },
                            "nw": {
                                "x": 5514.775,
                                "y": 4507.015
                            }
                        },
                        "position": {
                            "x": 5507.95,
                            "y": 4508.8643
                        },
                        "rowIdx": 8,
                        "colIdx": 6,
                        "mapInfo": "107블록 9열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 114,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00009열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098333,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5508.085,
                                "y": 4498.569
                            },
                            "se": {
                                "x": 5516.759,
                                "y": 4503.545
                            },
                            "sw": {
                                "x": 5513.061,
                                "y": 4489.895
                            },
                            "nw": {
                                "x": 5521.7354,
                                "y": 4494.871
                            }
                        },
                        "position": {
                            "x": 5514.91,
                            "y": 4496.72
                        },
                        "rowIdx": 8,
                        "colIdx": 7,
                        "mapInfo": "107블록 9열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 115,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00009열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098334,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5515.0547,
                                "y": 4486.426
                            },
                            "se": {
                                "x": 5523.729,
                                "y": 4491.402
                            },
                            "sw": {
                                "x": 5520.0312,
                                "y": 4477.752
                            },
                            "nw": {
                                "x": 5528.705,
                                "y": 4482.728
                            }
                        },
                        "position": {
                            "x": 5521.88,
                            "y": 4484.577
                        },
                        "rowIdx": 8,
                        "colIdx": 8,
                        "mapInfo": "107블록 9열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 116,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00009열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098335,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5522.025,
                                "y": 4474.282
                            },
                            "se": {
                                "x": 5530.699,
                                "y": 4479.2583
                            },
                            "sw": {
                                "x": 5527.001,
                                "y": 4465.608
                            },
                            "nw": {
                                "x": 5535.675,
                                "y": 4470.584
                            }
                        },
                        "position": {
                            "x": 5528.85,
                            "y": 4472.433
                        },
                        "rowIdx": 8,
                        "colIdx": 9,
                        "mapInfo": "107블록 9열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 117,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00009열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098336,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5528.985,
                                "y": 4462.138
                            },
                            "se": {
                                "x": 5537.659,
                                "y": 4467.1143
                            },
                            "sw": {
                                "x": 5533.961,
                                "y": 4453.464
                            },
                            "nw": {
                                "x": 5542.6353,
                                "y": 4458.44
                            }
                        },
                        "position": {
                            "x": 5535.81,
                            "y": 4460.289
                        },
                        "rowIdx": 8,
                        "colIdx": 10,
                        "mapInfo": "107블록 9열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 118,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00009열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098337,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5535.955,
                                "y": 4449.994
                            },
                            "se": {
                                "x": 5544.629,
                                "y": 4454.97
                            },
                            "sw": {
                                "x": 5540.931,
                                "y": 4441.32
                            },
                            "nw": {
                                "x": 5549.605,
                                "y": 4446.296
                            }
                        },
                        "position": {
                            "x": 5542.7803,
                            "y": 4448.145
                        },
                        "rowIdx": 8,
                        "colIdx": 11,
                        "mapInfo": "107블록 9열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 119,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00009열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098338,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5542.915,
                                "y": 4437.85
                            },
                            "se": {
                                "x": 5551.589,
                                "y": 4442.826
                            },
                            "sw": {
                                "x": 5547.891,
                                "y": 4429.176
                            },
                            "nw": {
                                "x": 5556.565,
                                "y": 4434.152
                            }
                        },
                        "position": {
                            "x": 5549.74,
                            "y": 4436.001
                        },
                        "rowIdx": 8,
                        "colIdx": 12,
                        "mapInfo": "107블록 9열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 120,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00009열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098339,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5549.885,
                                "y": 4425.706
                            },
                            "se": {
                                "x": 5558.559,
                                "y": 4430.682
                            },
                            "sw": {
                                "x": 5554.861,
                                "y": 4417.032
                            },
                            "nw": {
                                "x": 5563.535,
                                "y": 4422.008
                            }
                        },
                        "position": {
                            "x": 5556.71,
                            "y": 4423.857
                        },
                        "rowIdx": 8,
                        "colIdx": 13,
                        "mapInfo": "107블록 9열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950752,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 121,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "9열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00009열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098340,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5471.475,
                                "y": 4590.543
                            },
                            "se": {
                                "x": 5480.149,
                                "y": 4595.519
                            },
                            "sw": {
                                "x": 5476.451,
                                "y": 4581.869
                            },
                            "nw": {
                                "x": 5485.125,
                                "y": 4586.845
                            }
                        },
                        "position": {
                            "x": 5478.3,
                            "y": 4588.694
                        },
                        "rowIdx": 9,
                        "colIdx": 0,
                        "mapInfo": "107블록 10열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 122,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00010열00014번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098341,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5478.435,
                                "y": 4578.399
                            },
                            "se": {
                                "x": 5487.109,
                                "y": 4583.375
                            },
                            "sw": {
                                "x": 5483.411,
                                "y": 4569.725
                            },
                            "nw": {
                                "x": 5492.085,
                                "y": 4574.701
                            }
                        },
                        "position": {
                            "x": 5485.26,
                            "y": 4576.55
                        },
                        "rowIdx": 9,
                        "colIdx": 1,
                        "mapInfo": "107블록 10열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 123,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00010열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098342,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5485.405,
                                "y": 4566.255
                            },
                            "se": {
                                "x": 5494.079,
                                "y": 4571.231
                            },
                            "sw": {
                                "x": 5490.381,
                                "y": 4557.581
                            },
                            "nw": {
                                "x": 5499.055,
                                "y": 4562.557
                            }
                        },
                        "position": {
                            "x": 5492.23,
                            "y": 4564.4062
                        },
                        "rowIdx": 9,
                        "colIdx": 2,
                        "mapInfo": "107블록 10열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 124,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00010열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098343,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5492.3647,
                                "y": 4554.111
                            },
                            "se": {
                                "x": 5501.039,
                                "y": 4559.087
                            },
                            "sw": {
                                "x": 5497.341,
                                "y": 4545.437
                            },
                            "nw": {
                                "x": 5506.015,
                                "y": 4550.413
                            }
                        },
                        "position": {
                            "x": 5499.19,
                            "y": 4552.262
                        },
                        "rowIdx": 9,
                        "colIdx": 3,
                        "mapInfo": "107블록 10열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 125,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00010열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098344,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5499.335,
                                "y": 4541.967
                            },
                            "se": {
                                "x": 5508.009,
                                "y": 4546.9434
                            },
                            "sw": {
                                "x": 5504.311,
                                "y": 4533.293
                            },
                            "nw": {
                                "x": 5512.9854,
                                "y": 4538.269
                            }
                        },
                        "position": {
                            "x": 5506.16,
                            "y": 4540.118
                        },
                        "rowIdx": 9,
                        "colIdx": 4,
                        "mapInfo": "107블록 10열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 126,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00010열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098345,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5506.3047,
                                "y": 4529.823
                            },
                            "se": {
                                "x": 5514.979,
                                "y": 4534.799
                            },
                            "sw": {
                                "x": 5511.2812,
                                "y": 4521.149
                            },
                            "nw": {
                                "x": 5519.955,
                                "y": 4526.125
                            }
                        },
                        "position": {
                            "x": 5513.13,
                            "y": 4527.974
                        },
                        "rowIdx": 9,
                        "colIdx": 5,
                        "mapInfo": "107블록 10열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 127,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00010열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098346,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5513.2646,
                                "y": 4517.679
                            },
                            "se": {
                                "x": 5521.939,
                                "y": 4522.655
                            },
                            "sw": {
                                "x": 5518.241,
                                "y": 4509.005
                            },
                            "nw": {
                                "x": 5526.915,
                                "y": 4513.981
                            }
                        },
                        "position": {
                            "x": 5520.09,
                            "y": 4515.83
                        },
                        "rowIdx": 9,
                        "colIdx": 6,
                        "mapInfo": "107블록 10열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 128,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00010열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098347,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5520.235,
                                "y": 4505.535
                            },
                            "se": {
                                "x": 5528.909,
                                "y": 4510.5107
                            },
                            "sw": {
                                "x": 5525.211,
                                "y": 4496.861
                            },
                            "nw": {
                                "x": 5533.8853,
                                "y": 4501.837
                            }
                        },
                        "position": {
                            "x": 5527.06,
                            "y": 4503.686
                        },
                        "rowIdx": 9,
                        "colIdx": 7,
                        "mapInfo": "107블록 10열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 129,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00010열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098348,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5527.195,
                                "y": 4493.392
                            },
                            "se": {
                                "x": 5535.869,
                                "y": 4498.368
                            },
                            "sw": {
                                "x": 5532.171,
                                "y": 4484.718
                            },
                            "nw": {
                                "x": 5540.845,
                                "y": 4489.694
                            }
                        },
                        "position": {
                            "x": 5534.02,
                            "y": 4491.543
                        },
                        "rowIdx": 9,
                        "colIdx": 8,
                        "mapInfo": "107블록 10열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 130,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00010열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098349,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5534.165,
                                "y": 4481.248
                            },
                            "se": {
                                "x": 5542.839,
                                "y": 4486.224
                            },
                            "sw": {
                                "x": 5539.141,
                                "y": 4472.5737
                            },
                            "nw": {
                                "x": 5547.815,
                                "y": 4477.55
                            }
                        },
                        "position": {
                            "x": 5540.99,
                            "y": 4479.399
                        },
                        "rowIdx": 9,
                        "colIdx": 9,
                        "mapInfo": "107블록 10열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 131,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00010열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098350,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5541.135,
                                "y": 4469.104
                            },
                            "se": {
                                "x": 5549.809,
                                "y": 4474.08
                            },
                            "sw": {
                                "x": 5546.111,
                                "y": 4460.43
                            },
                            "nw": {
                                "x": 5554.785,
                                "y": 4465.4062
                            }
                        },
                        "position": {
                            "x": 5547.96,
                            "y": 4467.255
                        },
                        "rowIdx": 9,
                        "colIdx": 10,
                        "mapInfo": "107블록 10열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 132,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00010열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098351,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5548.0947,
                                "y": 4456.96
                            },
                            "se": {
                                "x": 5556.769,
                                "y": 4461.936
                            },
                            "sw": {
                                "x": 5553.0713,
                                "y": 4448.286
                            },
                            "nw": {
                                "x": 5561.745,
                                "y": 4453.262
                            }
                        },
                        "position": {
                            "x": 5554.92,
                            "y": 4455.111
                        },
                        "rowIdx": 9,
                        "colIdx": 11,
                        "mapInfo": "107블록 10열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 133,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00010열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098352,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5555.065,
                                "y": 4444.816
                            },
                            "se": {
                                "x": 5563.7393,
                                "y": 4449.792
                            },
                            "sw": {
                                "x": 5560.041,
                                "y": 4436.142
                            },
                            "nw": {
                                "x": 5568.715,
                                "y": 4441.118
                            }
                        },
                        "position": {
                            "x": 5561.89,
                            "y": 4442.967
                        },
                        "rowIdx": 9,
                        "colIdx": 12,
                        "mapInfo": "107블록 10열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 134,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00010열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098353,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5562.025,
                                "y": 4432.672
                            },
                            "se": {
                                "x": 5570.699,
                                "y": 4437.648
                            },
                            "sw": {
                                "x": 5567.001,
                                "y": 4423.998
                            },
                            "nw": {
                                "x": 5575.675,
                                "y": 4428.974
                            }
                        },
                        "position": {
                            "x": 5568.85,
                            "y": 4430.823
                        },
                        "rowIdx": 9,
                        "colIdx": 13,
                        "mapInfo": "107블록 10열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950766,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 135,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "10열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00010열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098354,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5490.585,
                                "y": 4585.365
                            },
                            "se": {
                                "x": 5499.259,
                                "y": 4590.341
                            },
                            "sw": {
                                "x": 5495.561,
                                "y": 4576.691
                            },
                            "nw": {
                                "x": 5504.2354,
                                "y": 4581.667
                            }
                        },
                        "position": {
                            "x": 5497.41,
                            "y": 4583.516
                        },
                        "rowIdx": 10,
                        "colIdx": 1,
                        "mapInfo": "107블록 11열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 136,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00011열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098355,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5497.545,
                                "y": 4573.221
                            },
                            "se": {
                                "x": 5506.2188,
                                "y": 4578.1973
                            },
                            "sw": {
                                "x": 5502.521,
                                "y": 4564.547
                            },
                            "nw": {
                                "x": 5511.1953,
                                "y": 4569.523
                            }
                        },
                        "position": {
                            "x": 5504.37,
                            "y": 4571.372
                        },
                        "rowIdx": 10,
                        "colIdx": 2,
                        "mapInfo": "107블록 11열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 137,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00011열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098356,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5504.5146,
                                "y": 4561.077
                            },
                            "se": {
                                "x": 5513.189,
                                "y": 4566.053
                            },
                            "sw": {
                                "x": 5509.491,
                                "y": 4552.403
                            },
                            "nw": {
                                "x": 5518.165,
                                "y": 4557.379
                            }
                        },
                        "position": {
                            "x": 5511.34,
                            "y": 4559.228
                        },
                        "rowIdx": 10,
                        "colIdx": 3,
                        "mapInfo": "107블록 11열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 138,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00011열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098357,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5511.475,
                                "y": 4548.933
                            },
                            "se": {
                                "x": 5520.149,
                                "y": 4553.909
                            },
                            "sw": {
                                "x": 5516.451,
                                "y": 4540.259
                            },
                            "nw": {
                                "x": 5525.125,
                                "y": 4545.235
                            }
                        },
                        "position": {
                            "x": 5518.3,
                            "y": 4547.084
                        },
                        "rowIdx": 10,
                        "colIdx": 4,
                        "mapInfo": "107블록 11열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 139,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00011열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098358,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5518.445,
                                "y": 4536.789
                            },
                            "se": {
                                "x": 5527.119,
                                "y": 4541.765
                            },
                            "sw": {
                                "x": 5523.421,
                                "y": 4528.115
                            },
                            "nw": {
                                "x": 5532.095,
                                "y": 4533.091
                            }
                        },
                        "position": {
                            "x": 5525.27,
                            "y": 4534.94
                        },
                        "rowIdx": 10,
                        "colIdx": 5,
                        "mapInfo": "107블록 11열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 140,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00011열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098359,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5525.415,
                                "y": 4524.645
                            },
                            "se": {
                                "x": 5534.089,
                                "y": 4529.621
                            },
                            "sw": {
                                "x": 5530.391,
                                "y": 4515.9707
                            },
                            "nw": {
                                "x": 5539.065,
                                "y": 4520.947
                            }
                        },
                        "position": {
                            "x": 5532.24,
                            "y": 4522.796
                        },
                        "rowIdx": 10,
                        "colIdx": 6,
                        "mapInfo": "107블록 11열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 141,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00011열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098360,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5532.375,
                                "y": 4512.501
                            },
                            "se": {
                                "x": 5541.049,
                                "y": 4517.477
                            },
                            "sw": {
                                "x": 5537.351,
                                "y": 4503.827
                            },
                            "nw": {
                                "x": 5546.025,
                                "y": 4508.803
                            }
                        },
                        "position": {
                            "x": 5539.2,
                            "y": 4510.652
                        },
                        "rowIdx": 10,
                        "colIdx": 7,
                        "mapInfo": "107블록 11열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 142,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00011열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098361,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5539.3447,
                                "y": 4500.358
                            },
                            "se": {
                                "x": 5548.019,
                                "y": 4505.334
                            },
                            "sw": {
                                "x": 5544.3213,
                                "y": 4491.684
                            },
                            "nw": {
                                "x": 5552.995,
                                "y": 4496.66
                            }
                        },
                        "position": {
                            "x": 5546.17,
                            "y": 4498.509
                        },
                        "rowIdx": 10,
                        "colIdx": 8,
                        "mapInfo": "107블록 11열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 143,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00011열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098362,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5546.3047,
                                "y": 4488.214
                            },
                            "se": {
                                "x": 5554.979,
                                "y": 4493.19
                            },
                            "sw": {
                                "x": 5551.2812,
                                "y": 4479.54
                            },
                            "nw": {
                                "x": 5559.955,
                                "y": 4484.516
                            }
                        },
                        "position": {
                            "x": 5553.13,
                            "y": 4486.365
                        },
                        "rowIdx": 10,
                        "colIdx": 9,
                        "mapInfo": "107블록 11열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 144,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00011열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098363,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5553.275,
                                "y": 4476.07
                            },
                            "se": {
                                "x": 5561.949,
                                "y": 4481.046
                            },
                            "sw": {
                                "x": 5558.251,
                                "y": 4467.396
                            },
                            "nw": {
                                "x": 5566.925,
                                "y": 4472.372
                            }
                        },
                        "position": {
                            "x": 5560.1,
                            "y": 4474.221
                        },
                        "rowIdx": 10,
                        "colIdx": 10,
                        "mapInfo": "107블록 11열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 145,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00011열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098364,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5560.245,
                                "y": 4463.926
                            },
                            "se": {
                                "x": 5568.919,
                                "y": 4468.902
                            },
                            "sw": {
                                "x": 5565.2207,
                                "y": 4455.252
                            },
                            "nw": {
                                "x": 5573.895,
                                "y": 4460.228
                            }
                        },
                        "position": {
                            "x": 5567.07,
                            "y": 4462.077
                        },
                        "rowIdx": 10,
                        "colIdx": 11,
                        "mapInfo": "107블록 11열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 146,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00011열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098365,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5567.205,
                                "y": 4451.782
                            },
                            "se": {
                                "x": 5575.879,
                                "y": 4456.7583
                            },
                            "sw": {
                                "x": 5572.181,
                                "y": 4443.108
                            },
                            "nw": {
                                "x": 5580.855,
                                "y": 4448.084
                            }
                        },
                        "position": {
                            "x": 5574.0303,
                            "y": 4449.933
                        },
                        "rowIdx": 10,
                        "colIdx": 12,
                        "mapInfo": "107블록 11열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 147,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00011열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098366,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5574.175,
                                "y": 4439.638
                            },
                            "se": {
                                "x": 5582.849,
                                "y": 4444.6143
                            },
                            "sw": {
                                "x": 5579.151,
                                "y": 4430.964
                            },
                            "nw": {
                                "x": 5587.825,
                                "y": 4435.94
                            }
                        },
                        "position": {
                            "x": 5581.0,
                            "y": 4437.789
                        },
                        "rowIdx": 10,
                        "colIdx": 13,
                        "mapInfo": "107블록 11열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950779,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 148,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "11열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00011열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098367,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5495.755,
                                "y": 4604.475
                            },
                            "se": {
                                "x": 5504.4287,
                                "y": 4609.451
                            },
                            "sw": {
                                "x": 5500.731,
                                "y": 4595.801
                            },
                            "nw": {
                                "x": 5509.4053,
                                "y": 4600.777
                            }
                        },
                        "position": {
                            "x": 5502.58,
                            "y": 4602.626
                        },
                        "rowIdx": 11,
                        "colIdx": 0,
                        "mapInfo": "107블록 12열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 149,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00012열00014번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098368,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5502.725,
                                "y": 4592.331
                            },
                            "se": {
                                "x": 5511.399,
                                "y": 4597.307
                            },
                            "sw": {
                                "x": 5507.701,
                                "y": 4583.657
                            },
                            "nw": {
                                "x": 5516.375,
                                "y": 4588.633
                            }
                        },
                        "position": {
                            "x": 5509.55,
                            "y": 4590.482
                        },
                        "rowIdx": 11,
                        "colIdx": 1,
                        "mapInfo": "107블록 12열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 150,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00012열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098369,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5509.695,
                                "y": 4580.187
                            },
                            "se": {
                                "x": 5518.369,
                                "y": 4585.163
                            },
                            "sw": {
                                "x": 5514.671,
                                "y": 4571.513
                            },
                            "nw": {
                                "x": 5523.345,
                                "y": 4576.4893
                            }
                        },
                        "position": {
                            "x": 5516.52,
                            "y": 4578.338
                        },
                        "rowIdx": 11,
                        "colIdx": 2,
                        "mapInfo": "107블록 12열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 151,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00012열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098370,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5516.655,
                                "y": 4568.043
                            },
                            "se": {
                                "x": 5525.329,
                                "y": 4573.019
                            },
                            "sw": {
                                "x": 5521.631,
                                "y": 4559.369
                            },
                            "nw": {
                                "x": 5530.305,
                                "y": 4564.345
                            }
                        },
                        "position": {
                            "x": 5523.48,
                            "y": 4566.194
                        },
                        "rowIdx": 11,
                        "colIdx": 3,
                        "mapInfo": "107블록 12열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 152,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00012열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098371,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5523.625,
                                "y": 4555.899
                            },
                            "se": {
                                "x": 5532.299,
                                "y": 4560.875
                            },
                            "sw": {
                                "x": 5528.601,
                                "y": 4547.225
                            },
                            "nw": {
                                "x": 5537.275,
                                "y": 4552.201
                            }
                        },
                        "position": {
                            "x": 5530.45,
                            "y": 4554.05
                        },
                        "rowIdx": 11,
                        "colIdx": 4,
                        "mapInfo": "107블록 12열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 153,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00012열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098372,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5530.585,
                                "y": 4543.755
                            },
                            "se": {
                                "x": 5539.259,
                                "y": 4548.731
                            },
                            "sw": {
                                "x": 5535.561,
                                "y": 4535.081
                            },
                            "nw": {
                                "x": 5544.2354,
                                "y": 4540.057
                            }
                        },
                        "position": {
                            "x": 5537.41,
                            "y": 4541.9062
                        },
                        "rowIdx": 11,
                        "colIdx": 5,
                        "mapInfo": "107블록 12열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 154,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00012열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098373,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5537.5547,
                                "y": 4531.611
                            },
                            "se": {
                                "x": 5546.229,
                                "y": 4536.587
                            },
                            "sw": {
                                "x": 5542.5312,
                                "y": 4522.937
                            },
                            "nw": {
                                "x": 5551.205,
                                "y": 4527.913
                            }
                        },
                        "position": {
                            "x": 5544.38,
                            "y": 4529.762
                        },
                        "rowIdx": 11,
                        "colIdx": 6,
                        "mapInfo": "107블록 12열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 155,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00012열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098374,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5544.525,
                                "y": 4519.467
                            },
                            "se": {
                                "x": 5553.199,
                                "y": 4524.4434
                            },
                            "sw": {
                                "x": 5549.501,
                                "y": 4510.793
                            },
                            "nw": {
                                "x": 5558.175,
                                "y": 4515.769
                            }
                        },
                        "position": {
                            "x": 5551.35,
                            "y": 4517.618
                        },
                        "rowIdx": 11,
                        "colIdx": 7,
                        "mapInfo": "107블록 12열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 156,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00012열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098375,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5551.485,
                                "y": 4507.323
                            },
                            "se": {
                                "x": 5560.159,
                                "y": 4512.299
                            },
                            "sw": {
                                "x": 5556.461,
                                "y": 4498.649
                            },
                            "nw": {
                                "x": 5565.1353,
                                "y": 4503.625
                            }
                        },
                        "position": {
                            "x": 5558.31,
                            "y": 4505.474
                        },
                        "rowIdx": 11,
                        "colIdx": 8,
                        "mapInfo": "107블록 12열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 157,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00012열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098376,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5558.455,
                                "y": 4495.18
                            },
                            "se": {
                                "x": 5567.129,
                                "y": 4500.1562
                            },
                            "sw": {
                                "x": 5563.431,
                                "y": 4486.506
                            },
                            "nw": {
                                "x": 5572.105,
                                "y": 4491.482
                            }
                        },
                        "position": {
                            "x": 5565.2803,
                            "y": 4493.331
                        },
                        "rowIdx": 11,
                        "colIdx": 9,
                        "mapInfo": "107블록 12열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 158,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00012열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098377,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5565.415,
                                "y": 4483.036
                            },
                            "se": {
                                "x": 5574.089,
                                "y": 4488.012
                            },
                            "sw": {
                                "x": 5570.391,
                                "y": 4474.362
                            },
                            "nw": {
                                "x": 5579.065,
                                "y": 4479.338
                            }
                        },
                        "position": {
                            "x": 5572.24,
                            "y": 4481.187
                        },
                        "rowIdx": 11,
                        "colIdx": 10,
                        "mapInfo": "107블록 12열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 159,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00012열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098378,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5572.385,
                                "y": 4470.892
                            },
                            "se": {
                                "x": 5581.059,
                                "y": 4475.868
                            },
                            "sw": {
                                "x": 5577.361,
                                "y": 4462.218
                            },
                            "nw": {
                                "x": 5586.035,
                                "y": 4467.194
                            }
                        },
                        "position": {
                            "x": 5579.21,
                            "y": 4469.043
                        },
                        "rowIdx": 11,
                        "colIdx": 11,
                        "mapInfo": "107블록 12열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 160,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00012열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098379,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5579.355,
                                "y": 4458.748
                            },
                            "se": {
                                "x": 5588.0293,
                                "y": 4463.724
                            },
                            "sw": {
                                "x": 5584.331,
                                "y": 4450.0737
                            },
                            "nw": {
                                "x": 5593.005,
                                "y": 4455.05
                            }
                        },
                        "position": {
                            "x": 5586.18,
                            "y": 4456.899
                        },
                        "rowIdx": 11,
                        "colIdx": 12,
                        "mapInfo": "107블록 12열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 161,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00012열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098380,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5586.315,
                                "y": 4446.604
                            },
                            "se": {
                                "x": 5594.9893,
                                "y": 4451.58
                            },
                            "sw": {
                                "x": 5591.291,
                                "y": 4437.93
                            },
                            "nw": {
                                "x": 5599.965,
                                "y": 4442.9062
                            }
                        },
                        "position": {
                            "x": 5593.14,
                            "y": 4444.755
                        },
                        "rowIdx": 11,
                        "colIdx": 13,
                        "mapInfo": "107블록 12열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950793,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 162,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "12열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00012열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098381,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5514.8647,
                                "y": 4599.297
                            },
                            "se": {
                                "x": 5523.539,
                                "y": 4604.273
                            },
                            "sw": {
                                "x": 5519.841,
                                "y": 4590.623
                            },
                            "nw": {
                                "x": 5528.515,
                                "y": 4595.599
                            }
                        },
                        "position": {
                            "x": 5521.69,
                            "y": 4597.448
                        },
                        "rowIdx": 12,
                        "colIdx": 1,
                        "mapInfo": "107블록 13열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 163,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00013열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098382,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5521.835,
                                "y": 4587.153
                            },
                            "se": {
                                "x": 5530.509,
                                "y": 4592.129
                            },
                            "sw": {
                                "x": 5526.811,
                                "y": 4578.479
                            },
                            "nw": {
                                "x": 5535.4854,
                                "y": 4583.455
                            }
                        },
                        "position": {
                            "x": 5528.66,
                            "y": 4585.304
                        },
                        "rowIdx": 12,
                        "colIdx": 2,
                        "mapInfo": "107블록 13열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 164,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00013열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098383,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5528.8047,
                                "y": 4575.009
                            },
                            "se": {
                                "x": 5537.479,
                                "y": 4579.985
                            },
                            "sw": {
                                "x": 5533.7812,
                                "y": 4566.335
                            },
                            "nw": {
                                "x": 5542.455,
                                "y": 4571.311
                            }
                        },
                        "position": {
                            "x": 5535.63,
                            "y": 4573.16
                        },
                        "rowIdx": 12,
                        "colIdx": 3,
                        "mapInfo": "107블록 13열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 165,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00013열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098384,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5535.7646,
                                "y": 4562.865
                            },
                            "se": {
                                "x": 5544.439,
                                "y": 4567.841
                            },
                            "sw": {
                                "x": 5540.741,
                                "y": 4554.191
                            },
                            "nw": {
                                "x": 5549.415,
                                "y": 4559.167
                            }
                        },
                        "position": {
                            "x": 5542.59,
                            "y": 4561.016
                        },
                        "rowIdx": 12,
                        "colIdx": 4,
                        "mapInfo": "107블록 13열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 166,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00013열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098385,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5542.735,
                                "y": 4550.721
                            },
                            "se": {
                                "x": 5551.409,
                                "y": 4555.6973
                            },
                            "sw": {
                                "x": 5547.711,
                                "y": 4542.047
                            },
                            "nw": {
                                "x": 5556.3853,
                                "y": 4547.023
                            }
                        },
                        "position": {
                            "x": 5549.56,
                            "y": 4548.872
                        },
                        "rowIdx": 12,
                        "colIdx": 5,
                        "mapInfo": "107블록 13열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 167,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00013열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098386,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5549.695,
                                "y": 4538.577
                            },
                            "se": {
                                "x": 5558.369,
                                "y": 4543.553
                            },
                            "sw": {
                                "x": 5554.671,
                                "y": 4529.903
                            },
                            "nw": {
                                "x": 5563.345,
                                "y": 4534.879
                            }
                        },
                        "position": {
                            "x": 5556.52,
                            "y": 4536.728
                        },
                        "rowIdx": 12,
                        "colIdx": 6,
                        "mapInfo": "107블록 13열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 168,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00013열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098387,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5556.665,
                                "y": 4526.434
                            },
                            "se": {
                                "x": 5565.339,
                                "y": 4531.41
                            },
                            "sw": {
                                "x": 5561.641,
                                "y": 4517.76
                            },
                            "nw": {
                                "x": 5570.315,
                                "y": 4522.736
                            }
                        },
                        "position": {
                            "x": 5563.49,
                            "y": 4524.585
                        },
                        "rowIdx": 12,
                        "colIdx": 7,
                        "mapInfo": "107블록 13열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 169,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00013열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098388,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5563.635,
                                "y": 4514.29
                            },
                            "se": {
                                "x": 5572.309,
                                "y": 4519.266
                            },
                            "sw": {
                                "x": 5568.611,
                                "y": 4505.616
                            },
                            "nw": {
                                "x": 5577.285,
                                "y": 4510.592
                            }
                        },
                        "position": {
                            "x": 5570.46,
                            "y": 4512.441
                        },
                        "rowIdx": 12,
                        "colIdx": 8,
                        "mapInfo": "107블록 13열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 170,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00013열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098389,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5570.5947,
                                "y": 4502.146
                            },
                            "se": {
                                "x": 5579.269,
                                "y": 4507.122
                            },
                            "sw": {
                                "x": 5575.5713,
                                "y": 4493.472
                            },
                            "nw": {
                                "x": 5584.245,
                                "y": 4498.448
                            }
                        },
                        "position": {
                            "x": 5577.42,
                            "y": 4500.297
                        },
                        "rowIdx": 12,
                        "colIdx": 9,
                        "mapInfo": "107블록 13열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 171,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00013열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098390,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5577.565,
                                "y": 4490.002
                            },
                            "se": {
                                "x": 5586.2393,
                                "y": 4494.978
                            },
                            "sw": {
                                "x": 5582.541,
                                "y": 4481.328
                            },
                            "nw": {
                                "x": 5591.215,
                                "y": 4486.304
                            }
                        },
                        "position": {
                            "x": 5584.39,
                            "y": 4488.153
                        },
                        "rowIdx": 12,
                        "colIdx": 10,
                        "mapInfo": "107블록 13열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 172,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00013열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098391,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5584.525,
                                "y": 4477.858
                            },
                            "se": {
                                "x": 5593.199,
                                "y": 4482.834
                            },
                            "sw": {
                                "x": 5589.501,
                                "y": 4469.184
                            },
                            "nw": {
                                "x": 5598.175,
                                "y": 4474.16
                            }
                        },
                        "position": {
                            "x": 5591.35,
                            "y": 4476.009
                        },
                        "rowIdx": 12,
                        "colIdx": 11,
                        "mapInfo": "107블록 13열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 173,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00013열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098392,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5591.495,
                                "y": 4465.714
                            },
                            "se": {
                                "x": 5600.169,
                                "y": 4470.69
                            },
                            "sw": {
                                "x": 5596.4707,
                                "y": 4457.04
                            },
                            "nw": {
                                "x": 5605.145,
                                "y": 4462.016
                            }
                        },
                        "position": {
                            "x": 5598.32,
                            "y": 4463.865
                        },
                        "rowIdx": 12,
                        "colIdx": 12,
                        "mapInfo": "107블록 13열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 174,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00013열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098393,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5598.465,
                                "y": 4453.57
                            },
                            "se": {
                                "x": 5607.139,
                                "y": 4458.546
                            },
                            "sw": {
                                "x": 5603.441,
                                "y": 4444.896
                            },
                            "nw": {
                                "x": 5612.115,
                                "y": 4449.872
                            }
                        },
                        "position": {
                            "x": 5605.29,
                            "y": 4451.721
                        },
                        "rowIdx": 12,
                        "colIdx": 13,
                        "mapInfo": "107블록 13열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950806,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 175,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "13열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00013열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098395,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5527.0146,
                                "y": 4606.263
                            },
                            "se": {
                                "x": 5535.689,
                                "y": 4611.2393
                            },
                            "sw": {
                                "x": 5531.991,
                                "y": 4597.589
                            },
                            "nw": {
                                "x": 5540.665,
                                "y": 4602.565
                            }
                        },
                        "position": {
                            "x": 5533.84,
                            "y": 4604.414
                        },
                        "rowIdx": 13,
                        "colIdx": 1,
                        "mapInfo": "107블록 14열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 177,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00014열00013번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098396,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5533.975,
                                "y": 4594.119
                            },
                            "se": {
                                "x": 5542.649,
                                "y": 4599.095
                            },
                            "sw": {
                                "x": 5538.951,
                                "y": 4585.445
                            },
                            "nw": {
                                "x": 5547.625,
                                "y": 4590.421
                            }
                        },
                        "position": {
                            "x": 5540.8,
                            "y": 4592.27
                        },
                        "rowIdx": 13,
                        "colIdx": 2,
                        "mapInfo": "107블록 14열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 178,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00014열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098397,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5540.945,
                                "y": 4581.975
                            },
                            "se": {
                                "x": 5549.619,
                                "y": 4586.951
                            },
                            "sw": {
                                "x": 5545.921,
                                "y": 4573.301
                            },
                            "nw": {
                                "x": 5554.595,
                                "y": 4578.277
                            }
                        },
                        "position": {
                            "x": 5547.77,
                            "y": 4580.126
                        },
                        "rowIdx": 13,
                        "colIdx": 3,
                        "mapInfo": "107블록 14열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 179,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00014열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098398,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5547.905,
                                "y": 4569.831
                            },
                            "se": {
                                "x": 5556.579,
                                "y": 4574.807
                            },
                            "sw": {
                                "x": 5552.881,
                                "y": 4561.157
                            },
                            "nw": {
                                "x": 5561.555,
                                "y": 4566.133
                            }
                        },
                        "position": {
                            "x": 5554.73,
                            "y": 4567.982
                        },
                        "rowIdx": 13,
                        "colIdx": 4,
                        "mapInfo": "107블록 14열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 180,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00014열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098399,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5554.875,
                                "y": 4557.687
                            },
                            "se": {
                                "x": 5563.549,
                                "y": 4562.663
                            },
                            "sw": {
                                "x": 5559.851,
                                "y": 4549.013
                            },
                            "nw": {
                                "x": 5568.525,
                                "y": 4553.9893
                            }
                        },
                        "position": {
                            "x": 5561.7,
                            "y": 4555.838
                        },
                        "rowIdx": 13,
                        "colIdx": 5,
                        "mapInfo": "107블록 14열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 181,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00014열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098400,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5561.8447,
                                "y": 4545.543
                            },
                            "se": {
                                "x": 5570.519,
                                "y": 4550.519
                            },
                            "sw": {
                                "x": 5566.8213,
                                "y": 4536.869
                            },
                            "nw": {
                                "x": 5575.495,
                                "y": 4541.845
                            }
                        },
                        "position": {
                            "x": 5568.67,
                            "y": 4543.694
                        },
                        "rowIdx": 13,
                        "colIdx": 6,
                        "mapInfo": "107블록 14열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 182,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00014열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098401,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5568.8047,
                                "y": 4533.4
                            },
                            "se": {
                                "x": 5577.479,
                                "y": 4538.376
                            },
                            "sw": {
                                "x": 5573.7812,
                                "y": 4524.726
                            },
                            "nw": {
                                "x": 5582.455,
                                "y": 4529.702
                            }
                        },
                        "position": {
                            "x": 5575.63,
                            "y": 4531.551
                        },
                        "rowIdx": 13,
                        "colIdx": 7,
                        "mapInfo": "107블록 14열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 183,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00014열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098402,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5575.775,
                                "y": 4521.256
                            },
                            "se": {
                                "x": 5584.449,
                                "y": 4526.232
                            },
                            "sw": {
                                "x": 5580.751,
                                "y": 4512.582
                            },
                            "nw": {
                                "x": 5589.425,
                                "y": 4517.558
                            }
                        },
                        "position": {
                            "x": 5582.6,
                            "y": 4519.407
                        },
                        "rowIdx": 13,
                        "colIdx": 8,
                        "mapInfo": "107블록 14열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 184,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00014열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098403,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5582.745,
                                "y": 4509.112
                            },
                            "se": {
                                "x": 5591.419,
                                "y": 4514.088
                            },
                            "sw": {
                                "x": 5587.7207,
                                "y": 4500.438
                            },
                            "nw": {
                                "x": 5596.395,
                                "y": 4505.414
                            }
                        },
                        "position": {
                            "x": 5589.57,
                            "y": 4507.263
                        },
                        "rowIdx": 13,
                        "colIdx": 9,
                        "mapInfo": "107블록 14열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 185,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00014열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098404,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5589.705,
                                "y": 4496.968
                            },
                            "se": {
                                "x": 5598.379,
                                "y": 4501.944
                            },
                            "sw": {
                                "x": 5594.681,
                                "y": 4488.294
                            },
                            "nw": {
                                "x": 5603.355,
                                "y": 4493.27
                            }
                        },
                        "position": {
                            "x": 5596.5303,
                            "y": 4495.119
                        },
                        "rowIdx": 13,
                        "colIdx": 10,
                        "mapInfo": "107블록 14열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 186,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00014열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098405,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5596.675,
                                "y": 4484.824
                            },
                            "se": {
                                "x": 5605.349,
                                "y": 4489.8
                            },
                            "sw": {
                                "x": 5601.651,
                                "y": 4476.15
                            },
                            "nw": {
                                "x": 5610.325,
                                "y": 4481.126
                            }
                        },
                        "position": {
                            "x": 5603.5,
                            "y": 4482.975
                        },
                        "rowIdx": 13,
                        "colIdx": 11,
                        "mapInfo": "107블록 14열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 187,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00014열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098406,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5603.635,
                                "y": 4472.68
                            },
                            "se": {
                                "x": 5612.309,
                                "y": 4477.6562
                            },
                            "sw": {
                                "x": 5608.611,
                                "y": 4464.006
                            },
                            "nw": {
                                "x": 5617.285,
                                "y": 4468.982
                            }
                        },
                        "position": {
                            "x": 5610.46,
                            "y": 4470.831
                        },
                        "rowIdx": 13,
                        "colIdx": 12,
                        "mapInfo": "107블록 14열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 188,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00014열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098407,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5610.605,
                                "y": 4460.536
                            },
                            "se": {
                                "x": 5619.2793,
                                "y": 4465.512
                            },
                            "sw": {
                                "x": 5615.581,
                                "y": 4451.862
                            },
                            "nw": {
                                "x": 5624.255,
                                "y": 4456.838
                            }
                        },
                        "position": {
                            "x": 5617.43,
                            "y": 4458.687
                        },
                        "rowIdx": 13,
                        "colIdx": 13,
                        "mapInfo": "107블록 14열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950820,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 189,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "14열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00014열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098409,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5546.125,
                                "y": 4601.085
                            },
                            "se": {
                                "x": 5554.799,
                                "y": 4606.061
                            },
                            "sw": {
                                "x": 5551.101,
                                "y": 4592.411
                            },
                            "nw": {
                                "x": 5559.775,
                                "y": 4597.387
                            }
                        },
                        "position": {
                            "x": 5552.95,
                            "y": 4599.236
                        },
                        "rowIdx": 14,
                        "colIdx": 2,
                        "mapInfo": "107블록 15열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 191,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00015열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098410,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5553.085,
                                "y": 4588.941
                            },
                            "se": {
                                "x": 5561.759,
                                "y": 4593.917
                            },
                            "sw": {
                                "x": 5558.061,
                                "y": 4580.267
                            },
                            "nw": {
                                "x": 5566.7354,
                                "y": 4585.243
                            }
                        },
                        "position": {
                            "x": 5559.91,
                            "y": 4587.092
                        },
                        "rowIdx": 14,
                        "colIdx": 3,
                        "mapInfo": "107블록 15열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 192,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00015열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098411,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5560.0547,
                                "y": 4576.797
                            },
                            "se": {
                                "x": 5568.729,
                                "y": 4581.773
                            },
                            "sw": {
                                "x": 5565.0312,
                                "y": 4568.123
                            },
                            "nw": {
                                "x": 5573.705,
                                "y": 4573.099
                            }
                        },
                        "position": {
                            "x": 5566.88,
                            "y": 4574.948
                        },
                        "rowIdx": 14,
                        "colIdx": 4,
                        "mapInfo": "107블록 15열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 193,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00015열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098412,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5567.0146,
                                "y": 4564.653
                            },
                            "se": {
                                "x": 5575.689,
                                "y": 4569.629
                            },
                            "sw": {
                                "x": 5571.991,
                                "y": 4555.979
                            },
                            "nw": {
                                "x": 5580.665,
                                "y": 4560.955
                            }
                        },
                        "position": {
                            "x": 5573.84,
                            "y": 4562.804
                        },
                        "rowIdx": 14,
                        "colIdx": 5,
                        "mapInfo": "107블록 15열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 194,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00015열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098413,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5573.985,
                                "y": 4552.509
                            },
                            "se": {
                                "x": 5582.659,
                                "y": 4557.485
                            },
                            "sw": {
                                "x": 5578.961,
                                "y": 4543.835
                            },
                            "nw": {
                                "x": 5587.6353,
                                "y": 4548.811
                            }
                        },
                        "position": {
                            "x": 5580.81,
                            "y": 4550.66
                        },
                        "rowIdx": 14,
                        "colIdx": 6,
                        "mapInfo": "107블록 15열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 195,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00015열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098414,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5580.955,
                                "y": 4540.365
                            },
                            "se": {
                                "x": 5589.629,
                                "y": 4545.341
                            },
                            "sw": {
                                "x": 5585.931,
                                "y": 4531.691
                            },
                            "nw": {
                                "x": 5594.605,
                                "y": 4536.667
                            }
                        },
                        "position": {
                            "x": 5587.7803,
                            "y": 4538.516
                        },
                        "rowIdx": 14,
                        "colIdx": 7,
                        "mapInfo": "107블록 15열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 196,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00015열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098415,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5587.915,
                                "y": 4528.221
                            },
                            "se": {
                                "x": 5596.589,
                                "y": 4533.1973
                            },
                            "sw": {
                                "x": 5592.891,
                                "y": 4519.547
                            },
                            "nw": {
                                "x": 5601.565,
                                "y": 4524.523
                            }
                        },
                        "position": {
                            "x": 5594.74,
                            "y": 4526.372
                        },
                        "rowIdx": 14,
                        "colIdx": 8,
                        "mapInfo": "107블록 15열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 197,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00015열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098416,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5594.885,
                                "y": 4516.078
                            },
                            "se": {
                                "x": 5603.559,
                                "y": 4521.054
                            },
                            "sw": {
                                "x": 5599.861,
                                "y": 4507.404
                            },
                            "nw": {
                                "x": 5608.535,
                                "y": 4512.38
                            }
                        },
                        "position": {
                            "x": 5601.71,
                            "y": 4514.229
                        },
                        "rowIdx": 14,
                        "colIdx": 9,
                        "mapInfo": "107블록 15열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 198,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00015열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098417,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5601.8447,
                                "y": 4503.934
                            },
                            "se": {
                                "x": 5610.519,
                                "y": 4508.91
                            },
                            "sw": {
                                "x": 5606.8213,
                                "y": 4495.26
                            },
                            "nw": {
                                "x": 5615.495,
                                "y": 4500.236
                            }
                        },
                        "position": {
                            "x": 5608.67,
                            "y": 4502.085
                        },
                        "rowIdx": 14,
                        "colIdx": 10,
                        "mapInfo": "107블록 15열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 199,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00015열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098418,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5608.815,
                                "y": 4491.79
                            },
                            "se": {
                                "x": 5617.4893,
                                "y": 4496.766
                            },
                            "sw": {
                                "x": 5613.791,
                                "y": 4483.116
                            },
                            "nw": {
                                "x": 5622.465,
                                "y": 4488.092
                            }
                        },
                        "position": {
                            "x": 5615.64,
                            "y": 4489.941
                        },
                        "rowIdx": 14,
                        "colIdx": 11,
                        "mapInfo": "107블록 15열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 200,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00015열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098419,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5615.785,
                                "y": 4479.646
                            },
                            "se": {
                                "x": 5624.459,
                                "y": 4484.622
                            },
                            "sw": {
                                "x": 5620.7607,
                                "y": 4470.972
                            },
                            "nw": {
                                "x": 5629.435,
                                "y": 4475.948
                            }
                        },
                        "position": {
                            "x": 5622.61,
                            "y": 4477.797
                        },
                        "rowIdx": 14,
                        "colIdx": 12,
                        "mapInfo": "107블록 15열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 201,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00015열00002번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098420,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5622.745,
                                "y": 4467.502
                            },
                            "se": {
                                "x": 5631.419,
                                "y": 4472.478
                            },
                            "sw": {
                                "x": 5627.7207,
                                "y": 4458.828
                            },
                            "nw": {
                                "x": 5636.395,
                                "y": 4463.804
                            }
                        },
                        "position": {
                            "x": 5629.57,
                            "y": 4465.653
                        },
                        "rowIdx": 14,
                        "colIdx": 13,
                        "mapInfo": "107블록 15열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950833,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 202,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "15열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00015열00001번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098423,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5558.2646,
                                "y": 4608.051
                            },
                            "se": {
                                "x": 5566.939,
                                "y": 4613.027
                            },
                            "sw": {
                                "x": 5563.241,
                                "y": 4599.377
                            },
                            "nw": {
                                "x": 5571.915,
                                "y": 4604.353
                            }
                        },
                        "position": {
                            "x": 5565.09,
                            "y": 4606.202
                        },
                        "rowIdx": 15,
                        "colIdx": 2,
                        "mapInfo": "107블록 16열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 205,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00016열00012번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098424,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5565.235,
                                "y": 4595.907
                            },
                            "se": {
                                "x": 5573.909,
                                "y": 4600.8833
                            },
                            "sw": {
                                "x": 5570.211,
                                "y": 4587.233
                            },
                            "nw": {
                                "x": 5578.8853,
                                "y": 4592.209
                            }
                        },
                        "position": {
                            "x": 5572.06,
                            "y": 4594.058
                        },
                        "rowIdx": 15,
                        "colIdx": 3,
                        "mapInfo": "107블록 16열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 206,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00016열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098425,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5572.195,
                                "y": 4583.763
                            },
                            "se": {
                                "x": 5580.869,
                                "y": 4588.7393
                            },
                            "sw": {
                                "x": 5577.171,
                                "y": 4575.089
                            },
                            "nw": {
                                "x": 5585.845,
                                "y": 4580.065
                            }
                        },
                        "position": {
                            "x": 5579.02,
                            "y": 4581.914
                        },
                        "rowIdx": 15,
                        "colIdx": 4,
                        "mapInfo": "107블록 16열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 207,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00016열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098426,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5579.165,
                                "y": 4571.619
                            },
                            "se": {
                                "x": 5587.839,
                                "y": 4576.595
                            },
                            "sw": {
                                "x": 5584.141,
                                "y": 4562.945
                            },
                            "nw": {
                                "x": 5592.815,
                                "y": 4567.921
                            }
                        },
                        "position": {
                            "x": 5585.99,
                            "y": 4569.77
                        },
                        "rowIdx": 15,
                        "colIdx": 5,
                        "mapInfo": "107블록 16열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 208,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00016열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098427,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5586.125,
                                "y": 4559.475
                            },
                            "se": {
                                "x": 5594.799,
                                "y": 4564.451
                            },
                            "sw": {
                                "x": 5591.101,
                                "y": 4550.801
                            },
                            "nw": {
                                "x": 5599.775,
                                "y": 4555.777
                            }
                        },
                        "position": {
                            "x": 5592.95,
                            "y": 4557.626
                        },
                        "rowIdx": 15,
                        "colIdx": 6,
                        "mapInfo": "107블록 16열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 209,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00016열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098428,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5593.0947,
                                "y": 4547.332
                            },
                            "se": {
                                "x": 5601.769,
                                "y": 4552.308
                            },
                            "sw": {
                                "x": 5598.0713,
                                "y": 4538.658
                            },
                            "nw": {
                                "x": 5606.745,
                                "y": 4543.634
                            }
                        },
                        "position": {
                            "x": 5599.92,
                            "y": 4545.483
                        },
                        "rowIdx": 15,
                        "colIdx": 7,
                        "mapInfo": "107블록 16열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 210,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00016열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098429,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5600.065,
                                "y": 4535.188
                            },
                            "se": {
                                "x": 5608.7393,
                                "y": 4540.164
                            },
                            "sw": {
                                "x": 5605.041,
                                "y": 4526.5137
                            },
                            "nw": {
                                "x": 5613.715,
                                "y": 4531.49
                            }
                        },
                        "position": {
                            "x": 5606.89,
                            "y": 4533.339
                        },
                        "rowIdx": 15,
                        "colIdx": 8,
                        "mapInfo": "107블록 16열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 211,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00016열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098430,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5607.025,
                                "y": 4523.044
                            },
                            "se": {
                                "x": 5615.699,
                                "y": 4528.02
                            },
                            "sw": {
                                "x": 5612.001,
                                "y": 4514.37
                            },
                            "nw": {
                                "x": 5620.675,
                                "y": 4519.346
                            }
                        },
                        "position": {
                            "x": 5613.85,
                            "y": 4521.195
                        },
                        "rowIdx": 15,
                        "colIdx": 9,
                        "mapInfo": "107블록 16열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 212,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00016열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098431,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5613.995,
                                "y": 4510.9
                            },
                            "se": {
                                "x": 5622.669,
                                "y": 4515.876
                            },
                            "sw": {
                                "x": 5618.9707,
                                "y": 4502.226
                            },
                            "nw": {
                                "x": 5627.645,
                                "y": 4507.202
                            }
                        },
                        "position": {
                            "x": 5620.82,
                            "y": 4509.051
                        },
                        "rowIdx": 15,
                        "colIdx": 10,
                        "mapInfo": "107블록 16열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 213,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00016열00004번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098432,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5620.955,
                                "y": 4498.756
                            },
                            "se": {
                                "x": 5629.629,
                                "y": 4503.732
                            },
                            "sw": {
                                "x": 5625.931,
                                "y": 4490.082
                            },
                            "nw": {
                                "x": 5634.605,
                                "y": 4495.058
                            }
                        },
                        "position": {
                            "x": 5627.7803,
                            "y": 4496.907
                        },
                        "rowIdx": 15,
                        "colIdx": 11,
                        "mapInfo": "107블록 16열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 214,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00016열00003번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098437,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5577.375,
                                "y": 4602.873
                            },
                            "se": {
                                "x": 5586.049,
                                "y": 4607.849
                            },
                            "sw": {
                                "x": 5582.351,
                                "y": 4594.1987
                            },
                            "nw": {
                                "x": 5591.025,
                                "y": 4599.175
                            }
                        },
                        "position": {
                            "x": 5584.2,
                            "y": 4601.024
                        },
                        "rowIdx": 16,
                        "colIdx": 3,
                        "mapInfo": "107블록 17열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 219,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00017열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098438,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5584.3447,
                                "y": 4590.729
                            },
                            "se": {
                                "x": 5593.019,
                                "y": 4595.705
                            },
                            "sw": {
                                "x": 5589.3213,
                                "y": 4582.055
                            },
                            "nw": {
                                "x": 5597.995,
                                "y": 4587.0312
                            }
                        },
                        "position": {
                            "x": 5591.17,
                            "y": 4588.88
                        },
                        "rowIdx": 16,
                        "colIdx": 4,
                        "mapInfo": "107블록 17열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 220,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00017열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098439,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5591.3047,
                                "y": 4578.585
                            },
                            "se": {
                                "x": 5599.979,
                                "y": 4583.561
                            },
                            "sw": {
                                "x": 5596.2812,
                                "y": 4569.911
                            },
                            "nw": {
                                "x": 5604.955,
                                "y": 4574.887
                            }
                        },
                        "position": {
                            "x": 5598.13,
                            "y": 4576.736
                        },
                        "rowIdx": 16,
                        "colIdx": 5,
                        "mapInfo": "107블록 17열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 221,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00017열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098440,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5598.275,
                                "y": 4566.441
                            },
                            "se": {
                                "x": 5606.949,
                                "y": 4571.417
                            },
                            "sw": {
                                "x": 5603.251,
                                "y": 4557.767
                            },
                            "nw": {
                                "x": 5611.925,
                                "y": 4562.743
                            }
                        },
                        "position": {
                            "x": 5605.1,
                            "y": 4564.592
                        },
                        "rowIdx": 16,
                        "colIdx": 6,
                        "mapInfo": "107블록 17열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 222,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00017열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098441,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5605.235,
                                "y": 4554.297
                            },
                            "se": {
                                "x": 5613.909,
                                "y": 4559.273
                            },
                            "sw": {
                                "x": 5610.211,
                                "y": 4545.623
                            },
                            "nw": {
                                "x": 5618.8853,
                                "y": 4550.599
                            }
                        },
                        "position": {
                            "x": 5612.06,
                            "y": 4552.448
                        },
                        "rowIdx": 16,
                        "colIdx": 7,
                        "mapInfo": "107블록 17열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 223,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00017열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098442,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5612.205,
                                "y": 4542.154
                            },
                            "se": {
                                "x": 5620.879,
                                "y": 4547.13
                            },
                            "sw": {
                                "x": 5617.181,
                                "y": 4533.48
                            },
                            "nw": {
                                "x": 5625.855,
                                "y": 4538.456
                            }
                        },
                        "position": {
                            "x": 5619.0303,
                            "y": 4540.305
                        },
                        "rowIdx": 16,
                        "colIdx": 8,
                        "mapInfo": "107블록 17열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 224,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00017열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098443,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5619.175,
                                "y": 4530.01
                            },
                            "se": {
                                "x": 5627.849,
                                "y": 4534.9863
                            },
                            "sw": {
                                "x": 5624.151,
                                "y": 4521.336
                            },
                            "nw": {
                                "x": 5632.825,
                                "y": 4526.312
                            }
                        },
                        "position": {
                            "x": 5626.0,
                            "y": 4528.161
                        },
                        "rowIdx": 16,
                        "colIdx": 9,
                        "mapInfo": "107블록 17열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 225,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00017열00005번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098451,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5589.5146,
                                "y": 4609.839
                            },
                            "se": {
                                "x": 5598.189,
                                "y": 4614.815
                            },
                            "sw": {
                                "x": 5594.491,
                                "y": 4601.165
                            },
                            "nw": {
                                "x": 5603.165,
                                "y": 4606.141
                            }
                        },
                        "position": {
                            "x": 5596.34,
                            "y": 4607.99
                        },
                        "rowIdx": 17,
                        "colIdx": 3,
                        "mapInfo": "107블록 18열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 233,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00018열00011번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098452,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5596.485,
                                "y": 4597.695
                            },
                            "se": {
                                "x": 5605.159,
                                "y": 4602.671
                            },
                            "sw": {
                                "x": 5601.461,
                                "y": 4589.021
                            },
                            "nw": {
                                "x": 5610.1353,
                                "y": 4593.997
                            }
                        },
                        "position": {
                            "x": 5603.31,
                            "y": 4595.846
                        },
                        "rowIdx": 17,
                        "colIdx": 4,
                        "mapInfo": "107블록 18열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 234,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00018열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098453,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5603.455,
                                "y": 4585.551
                            },
                            "se": {
                                "x": 5612.129,
                                "y": 4590.527
                            },
                            "sw": {
                                "x": 5608.431,
                                "y": 4576.877
                            },
                            "nw": {
                                "x": 5617.105,
                                "y": 4581.853
                            }
                        },
                        "position": {
                            "x": 5610.2803,
                            "y": 4583.702
                        },
                        "rowIdx": 17,
                        "colIdx": 5,
                        "mapInfo": "107블록 18열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 235,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00018열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098454,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5610.415,
                                "y": 4573.407
                            },
                            "se": {
                                "x": 5619.089,
                                "y": 4578.3833
                            },
                            "sw": {
                                "x": 5615.391,
                                "y": 4564.733
                            },
                            "nw": {
                                "x": 5624.065,
                                "y": 4569.709
                            }
                        },
                        "position": {
                            "x": 5617.24,
                            "y": 4571.558
                        },
                        "rowIdx": 17,
                        "colIdx": 6,
                        "mapInfo": "107블록 18열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 236,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00018열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098455,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5617.385,
                                "y": 4561.263
                            },
                            "se": {
                                "x": 5626.059,
                                "y": 4566.2393
                            },
                            "sw": {
                                "x": 5622.361,
                                "y": 4552.589
                            },
                            "nw": {
                                "x": 5631.035,
                                "y": 4557.565
                            }
                        },
                        "position": {
                            "x": 5624.21,
                            "y": 4559.414
                        },
                        "rowIdx": 17,
                        "colIdx": 7,
                        "mapInfo": "107블록 18열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 237,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00018열00007번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098456,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5624.3447,
                                "y": 4549.12
                            },
                            "se": {
                                "x": 5633.019,
                                "y": 4554.096
                            },
                            "sw": {
                                "x": 5629.3213,
                                "y": 4540.446
                            },
                            "nw": {
                                "x": 5637.995,
                                "y": 4545.422
                            }
                        },
                        "position": {
                            "x": 5631.17,
                            "y": 4547.271
                        },
                        "rowIdx": 17,
                        "colIdx": 8,
                        "mapInfo": "107블록 18열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 238,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00018열00006번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098465,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5608.625,
                                "y": 4604.661
                            },
                            "se": {
                                "x": 5617.299,
                                "y": 4609.637
                            },
                            "sw": {
                                "x": 5613.601,
                                "y": 4595.987
                            },
                            "nw": {
                                "x": 5622.275,
                                "y": 4600.963
                            }
                        },
                        "position": {
                            "x": 5615.45,
                            "y": 4602.812
                        },
                        "rowIdx": 18,
                        "colIdx": 4,
                        "mapInfo": "107블록 19열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 247,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00019열00010번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098466,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5615.5947,
                                "y": 4592.517
                            },
                            "se": {
                                "x": 5624.269,
                                "y": 4597.493
                            },
                            "sw": {
                                "x": 5620.5713,
                                "y": 4583.843
                            },
                            "nw": {
                                "x": 5629.245,
                                "y": 4588.819
                            }
                        },
                        "position": {
                            "x": 5622.42,
                            "y": 4590.668
                        },
                        "rowIdx": 18,
                        "colIdx": 5,
                        "mapInfo": "107블록 19열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 248,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00019열00009번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098467,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5622.565,
                                "y": 4580.373
                            },
                            "se": {
                                "x": 5631.2393,
                                "y": 4585.349
                            },
                            "sw": {
                                "x": 5627.541,
                                "y": 4571.6987
                            },
                            "nw": {
                                "x": 5636.215,
                                "y": 4576.675
                            }
                        },
                        "position": {
                            "x": 5629.39,
                            "y": 4578.524
                        },
                        "rowIdx": 18,
                        "colIdx": 6,
                        "mapInfo": "107블록 19열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 249,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00019열00008번",
                        "area": {
                            "virtualX": 21,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    }
                ],
                "22:17": [
                    {
                        "logicalSeatId": 1446098433,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5627.925,
                                "y": 4486.612
                            },
                            "se": {
                                "x": 5636.599,
                                "y": 4491.588
                            },
                            "sw": {
                                "x": 5632.901,
                                "y": 4477.938
                            },
                            "nw": {
                                "x": 5641.575,
                                "y": 4482.914
                            }
                        },
                        "position": {
                            "x": 5634.75,
                            "y": 4484.763
                        },
                        "rowIdx": 15,
                        "colIdx": 12,
                        "mapInfo": "107블록 16열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 215,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00016열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098434,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5634.895,
                                "y": 4474.468
                            },
                            "se": {
                                "x": 5643.569,
                                "y": 4479.444
                            },
                            "sw": {
                                "x": 5639.871,
                                "y": 4465.794
                            },
                            "nw": {
                                "x": 5648.545,
                                "y": 4470.77
                            }
                        },
                        "position": {
                            "x": 5641.7197,
                            "y": 4472.619
                        },
                        "rowIdx": 15,
                        "colIdx": 13,
                        "mapInfo": "107블록 16열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950847,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 216,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "16열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00016열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098444,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5626.135,
                                "y": 4517.866
                            },
                            "se": {
                                "x": 5634.809,
                                "y": 4522.842
                            },
                            "sw": {
                                "x": 5631.111,
                                "y": 4509.192
                            },
                            "nw": {
                                "x": 5639.785,
                                "y": 4514.168
                            }
                        },
                        "position": {
                            "x": 5632.96,
                            "y": 4516.017
                        },
                        "rowIdx": 16,
                        "colIdx": 10,
                        "mapInfo": "107블록 17열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 226,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00017열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098445,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5633.105,
                                "y": 4505.722
                            },
                            "se": {
                                "x": 5641.7793,
                                "y": 4510.698
                            },
                            "sw": {
                                "x": 5638.081,
                                "y": 4497.048
                            },
                            "nw": {
                                "x": 5646.755,
                                "y": 4502.024
                            }
                        },
                        "position": {
                            "x": 5639.93,
                            "y": 4503.873
                        },
                        "rowIdx": 16,
                        "colIdx": 11,
                        "mapInfo": "107블록 17열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 227,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00017열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098446,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5640.065,
                                "y": 4493.578
                            },
                            "se": {
                                "x": 5648.7393,
                                "y": 4498.554
                            },
                            "sw": {
                                "x": 5645.041,
                                "y": 4484.904
                            },
                            "nw": {
                                "x": 5653.715,
                                "y": 4489.88
                            }
                        },
                        "position": {
                            "x": 5646.89,
                            "y": 4491.729
                        },
                        "rowIdx": 16,
                        "colIdx": 12,
                        "mapInfo": "107블록 17열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 228,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00017열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098447,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5647.035,
                                "y": 4481.434
                            },
                            "se": {
                                "x": 5655.709,
                                "y": 4486.41
                            },
                            "sw": {
                                "x": 5652.0107,
                                "y": 4472.76
                            },
                            "nw": {
                                "x": 5660.685,
                                "y": 4477.736
                            }
                        },
                        "position": {
                            "x": 5653.86,
                            "y": 4479.585
                        },
                        "rowIdx": 16,
                        "colIdx": 13,
                        "mapInfo": "107블록 17열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950860,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 229,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "17열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00017열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098457,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5631.315,
                                "y": 4536.976
                            },
                            "se": {
                                "x": 5639.9893,
                                "y": 4541.952
                            },
                            "sw": {
                                "x": 5636.291,
                                "y": 4528.302
                            },
                            "nw": {
                                "x": 5644.965,
                                "y": 4533.278
                            }
                        },
                        "position": {
                            "x": 5638.14,
                            "y": 4535.127
                        },
                        "rowIdx": 17,
                        "colIdx": 9,
                        "mapInfo": "107블록 18열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 239,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00018열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098458,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5638.285,
                                "y": 4524.832
                            },
                            "se": {
                                "x": 5646.959,
                                "y": 4529.808
                            },
                            "sw": {
                                "x": 5643.2607,
                                "y": 4516.158
                            },
                            "nw": {
                                "x": 5651.935,
                                "y": 4521.134
                            }
                        },
                        "position": {
                            "x": 5645.11,
                            "y": 4522.983
                        },
                        "rowIdx": 17,
                        "colIdx": 10,
                        "mapInfo": "107블록 18열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 240,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00018열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098459,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5645.245,
                                "y": 4512.688
                            },
                            "se": {
                                "x": 5653.919,
                                "y": 4517.664
                            },
                            "sw": {
                                "x": 5650.2207,
                                "y": 4504.0137
                            },
                            "nw": {
                                "x": 5658.895,
                                "y": 4508.99
                            }
                        },
                        "position": {
                            "x": 5652.07,
                            "y": 4510.839
                        },
                        "rowIdx": 17,
                        "colIdx": 11,
                        "mapInfo": "107블록 18열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 241,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00018열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098460,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5652.215,
                                "y": 4500.544
                            },
                            "se": {
                                "x": 5660.889,
                                "y": 4505.52
                            },
                            "sw": {
                                "x": 5657.191,
                                "y": 4491.87
                            },
                            "nw": {
                                "x": 5665.865,
                                "y": 4496.846
                            }
                        },
                        "position": {
                            "x": 5659.04,
                            "y": 4498.695
                        },
                        "rowIdx": 17,
                        "colIdx": 12,
                        "mapInfo": "107블록 18열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 242,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00018열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098461,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5659.175,
                                "y": 4488.4
                            },
                            "se": {
                                "x": 5667.849,
                                "y": 4493.376
                            },
                            "sw": {
                                "x": 5664.151,
                                "y": 4479.726
                            },
                            "nw": {
                                "x": 5672.825,
                                "y": 4484.702
                            }
                        },
                        "position": {
                            "x": 5666.0,
                            "y": 4486.551
                        },
                        "rowIdx": 17,
                        "colIdx": 13,
                        "mapInfo": "107블록 18열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950874,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 243,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "18열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00018열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098468,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5629.525,
                                "y": 4568.229
                            },
                            "se": {
                                "x": 5638.199,
                                "y": 4573.205
                            },
                            "sw": {
                                "x": 5634.501,
                                "y": 4559.555
                            },
                            "nw": {
                                "x": 5643.175,
                                "y": 4564.5312
                            }
                        },
                        "position": {
                            "x": 5636.35,
                            "y": 4566.38
                        },
                        "rowIdx": 18,
                        "colIdx": 7,
                        "mapInfo": "107블록 19열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 250,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00019열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098469,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5636.495,
                                "y": 4556.086
                            },
                            "se": {
                                "x": 5645.169,
                                "y": 4561.062
                            },
                            "sw": {
                                "x": 5641.4707,
                                "y": 4547.412
                            },
                            "nw": {
                                "x": 5650.145,
                                "y": 4552.388
                            }
                        },
                        "position": {
                            "x": 5643.32,
                            "y": 4554.237
                        },
                        "rowIdx": 18,
                        "colIdx": 8,
                        "mapInfo": "107블록 19열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 251,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00019열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098470,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5643.455,
                                "y": 4543.942
                            },
                            "se": {
                                "x": 5652.129,
                                "y": 4548.918
                            },
                            "sw": {
                                "x": 5648.431,
                                "y": 4535.268
                            },
                            "nw": {
                                "x": 5657.105,
                                "y": 4540.244
                            }
                        },
                        "position": {
                            "x": 5650.2803,
                            "y": 4542.093
                        },
                        "rowIdx": 18,
                        "colIdx": 9,
                        "mapInfo": "107블록 19열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 252,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00019열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098471,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5650.425,
                                "y": 4531.798
                            },
                            "se": {
                                "x": 5659.099,
                                "y": 4536.774
                            },
                            "sw": {
                                "x": 5655.401,
                                "y": 4523.124
                            },
                            "nw": {
                                "x": 5664.075,
                                "y": 4528.1
                            }
                        },
                        "position": {
                            "x": 5657.25,
                            "y": 4529.949
                        },
                        "rowIdx": 18,
                        "colIdx": 10,
                        "mapInfo": "107블록 19열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 253,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00019열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098472,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5657.395,
                                "y": 4519.654
                            },
                            "se": {
                                "x": 5666.069,
                                "y": 4524.63
                            },
                            "sw": {
                                "x": 5662.371,
                                "y": 4510.98
                            },
                            "nw": {
                                "x": 5671.045,
                                "y": 4515.956
                            }
                        },
                        "position": {
                            "x": 5664.2197,
                            "y": 4517.805
                        },
                        "rowIdx": 18,
                        "colIdx": 11,
                        "mapInfo": "107블록 19열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 254,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00019열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098473,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5664.355,
                                "y": 4507.51
                            },
                            "se": {
                                "x": 5673.0293,
                                "y": 4512.4863
                            },
                            "sw": {
                                "x": 5669.331,
                                "y": 4498.836
                            },
                            "nw": {
                                "x": 5678.005,
                                "y": 4503.812
                            }
                        },
                        "position": {
                            "x": 5671.18,
                            "y": 4505.661
                        },
                        "rowIdx": 18,
                        "colIdx": 12,
                        "mapInfo": "107블록 19열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 255,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00019열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098474,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5671.325,
                                "y": 4495.366
                            },
                            "se": {
                                "x": 5679.999,
                                "y": 4500.342
                            },
                            "sw": {
                                "x": 5676.301,
                                "y": 4486.692
                            },
                            "nw": {
                                "x": 5684.975,
                                "y": 4491.668
                            }
                        },
                        "position": {
                            "x": 5678.15,
                            "y": 4493.517
                        },
                        "rowIdx": 18,
                        "colIdx": 13,
                        "mapInfo": "107블록 19열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950887,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 256,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "19열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00019열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098480,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5627.735,
                                "y": 4599.483
                            },
                            "se": {
                                "x": 5636.409,
                                "y": 4604.459
                            },
                            "sw": {
                                "x": 5632.711,
                                "y": 4590.809
                            },
                            "nw": {
                                "x": 5641.3853,
                                "y": 4595.785
                            }
                        },
                        "position": {
                            "x": 5634.56,
                            "y": 4597.634
                        },
                        "rowIdx": 19,
                        "colIdx": 5,
                        "mapInfo": "107블록 20열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 262,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00020열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098481,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5634.705,
                                "y": 4587.339
                            },
                            "se": {
                                "x": 5643.379,
                                "y": 4592.315
                            },
                            "sw": {
                                "x": 5639.681,
                                "y": 4578.665
                            },
                            "nw": {
                                "x": 5648.355,
                                "y": 4583.641
                            }
                        },
                        "position": {
                            "x": 5641.5303,
                            "y": 4585.49
                        },
                        "rowIdx": 19,
                        "colIdx": 6,
                        "mapInfo": "107블록 20열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 263,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00020열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098482,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5641.675,
                                "y": 4575.195
                            },
                            "se": {
                                "x": 5650.349,
                                "y": 4580.171
                            },
                            "sw": {
                                "x": 5646.651,
                                "y": 4566.521
                            },
                            "nw": {
                                "x": 5655.325,
                                "y": 4571.497
                            }
                        },
                        "position": {
                            "x": 5648.5,
                            "y": 4573.346
                        },
                        "rowIdx": 19,
                        "colIdx": 7,
                        "mapInfo": "107블록 20열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 264,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00020열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098483,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5648.635,
                                "y": 4563.052
                            },
                            "se": {
                                "x": 5657.309,
                                "y": 4568.028
                            },
                            "sw": {
                                "x": 5653.611,
                                "y": 4554.378
                            },
                            "nw": {
                                "x": 5662.285,
                                "y": 4559.354
                            }
                        },
                        "position": {
                            "x": 5655.46,
                            "y": 4561.203
                        },
                        "rowIdx": 19,
                        "colIdx": 8,
                        "mapInfo": "107블록 20열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 265,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00020열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098484,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5655.605,
                                "y": 4550.908
                            },
                            "se": {
                                "x": 5664.2793,
                                "y": 4555.884
                            },
                            "sw": {
                                "x": 5660.581,
                                "y": 4542.234
                            },
                            "nw": {
                                "x": 5669.255,
                                "y": 4547.21
                            }
                        },
                        "position": {
                            "x": 5662.43,
                            "y": 4549.059
                        },
                        "rowIdx": 19,
                        "colIdx": 9,
                        "mapInfo": "107블록 20열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 266,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00020열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098485,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5662.565,
                                "y": 4538.764
                            },
                            "se": {
                                "x": 5671.2393,
                                "y": 4543.74
                            },
                            "sw": {
                                "x": 5667.541,
                                "y": 4530.09
                            },
                            "nw": {
                                "x": 5676.215,
                                "y": 4535.066
                            }
                        },
                        "position": {
                            "x": 5669.39,
                            "y": 4536.915
                        },
                        "rowIdx": 19,
                        "colIdx": 10,
                        "mapInfo": "107블록 20열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 267,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00020열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098486,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5669.535,
                                "y": 4526.62
                            },
                            "se": {
                                "x": 5678.209,
                                "y": 4531.596
                            },
                            "sw": {
                                "x": 5674.5107,
                                "y": 4517.946
                            },
                            "nw": {
                                "x": 5683.185,
                                "y": 4522.922
                            }
                        },
                        "position": {
                            "x": 5676.36,
                            "y": 4524.771
                        },
                        "rowIdx": 19,
                        "colIdx": 11,
                        "mapInfo": "107블록 20열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 268,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00020열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098487,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5676.505,
                                "y": 4514.476
                            },
                            "se": {
                                "x": 5685.1787,
                                "y": 4519.452
                            },
                            "sw": {
                                "x": 5681.481,
                                "y": 4505.802
                            },
                            "nw": {
                                "x": 5690.1553,
                                "y": 4510.778
                            }
                        },
                        "position": {
                            "x": 5683.33,
                            "y": 4512.627
                        },
                        "rowIdx": 19,
                        "colIdx": 12,
                        "mapInfo": "107블록 20열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 269,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00020열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098488,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5683.465,
                                "y": 4502.332
                            },
                            "se": {
                                "x": 5692.139,
                                "y": 4507.308
                            },
                            "sw": {
                                "x": 5688.441,
                                "y": 4493.658
                            },
                            "nw": {
                                "x": 5697.115,
                                "y": 4498.634
                            }
                        },
                        "position": {
                            "x": 5690.29,
                            "y": 4500.483
                        },
                        "rowIdx": 19,
                        "colIdx": 13,
                        "mapInfo": "107블록 20열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950901,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 270,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "20열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00020열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098493,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5639.885,
                                "y": 4606.449
                            },
                            "se": {
                                "x": 5648.559,
                                "y": 4611.425
                            },
                            "sw": {
                                "x": 5644.861,
                                "y": 4597.775
                            },
                            "nw": {
                                "x": 5653.535,
                                "y": 4602.751
                            }
                        },
                        "position": {
                            "x": 5646.71,
                            "y": 4604.6
                        },
                        "rowIdx": 20,
                        "colIdx": 5,
                        "mapInfo": "107블록 21열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 275,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00021열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098494,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5646.8447,
                                "y": 4594.305
                            },
                            "se": {
                                "x": 5655.519,
                                "y": 4599.2812
                            },
                            "sw": {
                                "x": 5651.8213,
                                "y": 4585.631
                            },
                            "nw": {
                                "x": 5660.495,
                                "y": 4590.607
                            }
                        },
                        "position": {
                            "x": 5653.67,
                            "y": 4592.456
                        },
                        "rowIdx": 20,
                        "colIdx": 6,
                        "mapInfo": "107블록 21열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 276,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00021열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098495,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5653.815,
                                "y": 4582.161
                            },
                            "se": {
                                "x": 5662.4893,
                                "y": 4587.137
                            },
                            "sw": {
                                "x": 5658.791,
                                "y": 4573.487
                            },
                            "nw": {
                                "x": 5667.465,
                                "y": 4578.463
                            }
                        },
                        "position": {
                            "x": 5660.64,
                            "y": 4580.312
                        },
                        "rowIdx": 20,
                        "colIdx": 7,
                        "mapInfo": "107블록 21열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 277,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00021열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098496,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5660.785,
                                "y": 4570.017
                            },
                            "se": {
                                "x": 5669.459,
                                "y": 4574.993
                            },
                            "sw": {
                                "x": 5665.7607,
                                "y": 4561.343
                            },
                            "nw": {
                                "x": 5674.435,
                                "y": 4566.319
                            }
                        },
                        "position": {
                            "x": 5667.61,
                            "y": 4568.168
                        },
                        "rowIdx": 20,
                        "colIdx": 8,
                        "mapInfo": "107블록 21열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 278,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00021열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098497,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5667.745,
                                "y": 4557.874
                            },
                            "se": {
                                "x": 5676.419,
                                "y": 4562.85
                            },
                            "sw": {
                                "x": 5672.7207,
                                "y": 4549.2
                            },
                            "nw": {
                                "x": 5681.395,
                                "y": 4554.176
                            }
                        },
                        "position": {
                            "x": 5674.57,
                            "y": 4556.025
                        },
                        "rowIdx": 20,
                        "colIdx": 9,
                        "mapInfo": "107블록 21열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 279,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00021열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098498,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5674.715,
                                "y": 4545.73
                            },
                            "se": {
                                "x": 5683.389,
                                "y": 4550.706
                            },
                            "sw": {
                                "x": 5679.691,
                                "y": 4537.056
                            },
                            "nw": {
                                "x": 5688.365,
                                "y": 4542.032
                            }
                        },
                        "position": {
                            "x": 5681.54,
                            "y": 4543.881
                        },
                        "rowIdx": 20,
                        "colIdx": 10,
                        "mapInfo": "107블록 21열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 280,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00021열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098499,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5681.675,
                                "y": 4533.586
                            },
                            "se": {
                                "x": 5690.349,
                                "y": 4538.562
                            },
                            "sw": {
                                "x": 5686.651,
                                "y": 4524.912
                            },
                            "nw": {
                                "x": 5695.325,
                                "y": 4529.888
                            }
                        },
                        "position": {
                            "x": 5688.5,
                            "y": 4531.737
                        },
                        "rowIdx": 20,
                        "colIdx": 11,
                        "mapInfo": "107블록 21열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 281,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00021열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098500,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5688.645,
                                "y": 4521.442
                            },
                            "se": {
                                "x": 5697.319,
                                "y": 4526.418
                            },
                            "sw": {
                                "x": 5693.621,
                                "y": 4512.768
                            },
                            "nw": {
                                "x": 5702.295,
                                "y": 4517.744
                            }
                        },
                        "position": {
                            "x": 5695.4697,
                            "y": 4519.593
                        },
                        "rowIdx": 20,
                        "colIdx": 12,
                        "mapInfo": "107블록 21열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 282,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00021열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098501,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5695.6147,
                                "y": 4509.298
                            },
                            "se": {
                                "x": 5704.289,
                                "y": 4514.274
                            },
                            "sw": {
                                "x": 5700.591,
                                "y": 4500.624
                            },
                            "nw": {
                                "x": 5709.265,
                                "y": 4505.6
                            }
                        },
                        "position": {
                            "x": 5702.44,
                            "y": 4507.449
                        },
                        "rowIdx": 20,
                        "colIdx": 13,
                        "mapInfo": "107블록 21열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 283,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00021열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098508,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5658.995,
                                "y": 4601.271
                            },
                            "se": {
                                "x": 5667.669,
                                "y": 4606.247
                            },
                            "sw": {
                                "x": 5663.9707,
                                "y": 4592.597
                            },
                            "nw": {
                                "x": 5672.645,
                                "y": 4597.573
                            }
                        },
                        "position": {
                            "x": 5665.82,
                            "y": 4599.422
                        },
                        "rowIdx": 21,
                        "colIdx": 6,
                        "mapInfo": "107블록 22열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 290,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00022열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098509,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5665.955,
                                "y": 4589.127
                            },
                            "se": {
                                "x": 5674.629,
                                "y": 4594.103
                            },
                            "sw": {
                                "x": 5670.931,
                                "y": 4580.453
                            },
                            "nw": {
                                "x": 5679.605,
                                "y": 4585.429
                            }
                        },
                        "position": {
                            "x": 5672.7803,
                            "y": 4587.278
                        },
                        "rowIdx": 21,
                        "colIdx": 7,
                        "mapInfo": "107블록 22열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 291,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00022열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098510,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5672.925,
                                "y": 4576.983
                            },
                            "se": {
                                "x": 5681.599,
                                "y": 4581.959
                            },
                            "sw": {
                                "x": 5677.901,
                                "y": 4568.309
                            },
                            "nw": {
                                "x": 5686.575,
                                "y": 4573.285
                            }
                        },
                        "position": {
                            "x": 5679.75,
                            "y": 4575.134
                        },
                        "rowIdx": 21,
                        "colIdx": 8,
                        "mapInfo": "107블록 22열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 292,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00022열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098511,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5679.895,
                                "y": 4564.84
                            },
                            "se": {
                                "x": 5688.569,
                                "y": 4569.816
                            },
                            "sw": {
                                "x": 5684.871,
                                "y": 4556.166
                            },
                            "nw": {
                                "x": 5693.545,
                                "y": 4561.142
                            }
                        },
                        "position": {
                            "x": 5686.7197,
                            "y": 4562.991
                        },
                        "rowIdx": 21,
                        "colIdx": 9,
                        "mapInfo": "107블록 22열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 293,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00022열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098512,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5686.855,
                                "y": 4552.696
                            },
                            "se": {
                                "x": 5695.5293,
                                "y": 4557.672
                            },
                            "sw": {
                                "x": 5691.831,
                                "y": 4544.022
                            },
                            "nw": {
                                "x": 5700.505,
                                "y": 4548.998
                            }
                        },
                        "position": {
                            "x": 5693.68,
                            "y": 4550.847
                        },
                        "rowIdx": 21,
                        "colIdx": 10,
                        "mapInfo": "107블록 22열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 294,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00022열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098513,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5693.825,
                                "y": 4540.552
                            },
                            "se": {
                                "x": 5702.499,
                                "y": 4545.528
                            },
                            "sw": {
                                "x": 5698.801,
                                "y": 4531.878
                            },
                            "nw": {
                                "x": 5707.475,
                                "y": 4536.854
                            }
                        },
                        "position": {
                            "x": 5700.65,
                            "y": 4538.703
                        },
                        "rowIdx": 21,
                        "colIdx": 11,
                        "mapInfo": "107블록 22열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 295,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00022열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098514,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5700.785,
                                "y": 4528.408
                            },
                            "se": {
                                "x": 5709.459,
                                "y": 4533.384
                            },
                            "sw": {
                                "x": 5705.7607,
                                "y": 4519.734
                            },
                            "nw": {
                                "x": 5714.435,
                                "y": 4524.71
                            }
                        },
                        "position": {
                            "x": 5707.61,
                            "y": 4526.559
                        },
                        "rowIdx": 21,
                        "colIdx": 12,
                        "mapInfo": "107블록 22열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 296,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00022열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098515,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5707.755,
                                "y": 4516.264
                            },
                            "se": {
                                "x": 5716.4287,
                                "y": 4521.24
                            },
                            "sw": {
                                "x": 5712.731,
                                "y": 4507.59
                            },
                            "nw": {
                                "x": 5721.4053,
                                "y": 4512.566
                            }
                        },
                        "position": {
                            "x": 5714.58,
                            "y": 4514.415
                        },
                        "rowIdx": 21,
                        "colIdx": 13,
                        "mapInfo": "107블록 22열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 297,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00022열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098521,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5671.135,
                                "y": 4608.237
                            },
                            "se": {
                                "x": 5679.809,
                                "y": 4613.213
                            },
                            "sw": {
                                "x": 5676.111,
                                "y": 4599.563
                            },
                            "nw": {
                                "x": 5684.785,
                                "y": 4604.539
                            }
                        },
                        "position": {
                            "x": 5677.96,
                            "y": 4606.388
                        },
                        "rowIdx": 22,
                        "colIdx": 6,
                        "mapInfo": "107블록 23열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 303,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00023열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098522,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5678.105,
                                "y": 4596.093
                            },
                            "se": {
                                "x": 5686.7793,
                                "y": 4601.069
                            },
                            "sw": {
                                "x": 5683.081,
                                "y": 4587.419
                            },
                            "nw": {
                                "x": 5691.755,
                                "y": 4592.395
                            }
                        },
                        "position": {
                            "x": 5684.93,
                            "y": 4594.244
                        },
                        "rowIdx": 22,
                        "colIdx": 7,
                        "mapInfo": "107블록 23열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 304,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00023열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098523,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5685.065,
                                "y": 4583.949
                            },
                            "se": {
                                "x": 5693.7393,
                                "y": 4588.925
                            },
                            "sw": {
                                "x": 5690.041,
                                "y": 4575.275
                            },
                            "nw": {
                                "x": 5698.715,
                                "y": 4580.251
                            }
                        },
                        "position": {
                            "x": 5691.89,
                            "y": 4582.1
                        },
                        "rowIdx": 22,
                        "colIdx": 8,
                        "mapInfo": "107블록 23열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 305,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00023열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098524,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5692.035,
                                "y": 4571.806
                            },
                            "se": {
                                "x": 5700.709,
                                "y": 4576.782
                            },
                            "sw": {
                                "x": 5697.0107,
                                "y": 4563.132
                            },
                            "nw": {
                                "x": 5705.685,
                                "y": 4568.108
                            }
                        },
                        "position": {
                            "x": 5698.86,
                            "y": 4569.957
                        },
                        "rowIdx": 22,
                        "colIdx": 9,
                        "mapInfo": "107블록 23열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 306,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00023열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098525,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5699.005,
                                "y": 4559.662
                            },
                            "se": {
                                "x": 5707.6787,
                                "y": 4564.638
                            },
                            "sw": {
                                "x": 5703.981,
                                "y": 4550.988
                            },
                            "nw": {
                                "x": 5712.6553,
                                "y": 4555.964
                            }
                        },
                        "position": {
                            "x": 5705.83,
                            "y": 4557.813
                        },
                        "rowIdx": 22,
                        "colIdx": 10,
                        "mapInfo": "107블록 23열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 307,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00023열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098526,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5705.965,
                                "y": 4547.518
                            },
                            "se": {
                                "x": 5714.639,
                                "y": 4552.494
                            },
                            "sw": {
                                "x": 5710.941,
                                "y": 4538.8438
                            },
                            "nw": {
                                "x": 5719.615,
                                "y": 4543.82
                            }
                        },
                        "position": {
                            "x": 5712.79,
                            "y": 4545.669
                        },
                        "rowIdx": 22,
                        "colIdx": 11,
                        "mapInfo": "107블록 23열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 308,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00023열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098527,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5712.935,
                                "y": 4535.374
                            },
                            "se": {
                                "x": 5721.609,
                                "y": 4540.35
                            },
                            "sw": {
                                "x": 5717.911,
                                "y": 4526.7
                            },
                            "nw": {
                                "x": 5726.585,
                                "y": 4531.676
                            }
                        },
                        "position": {
                            "x": 5719.76,
                            "y": 4533.525
                        },
                        "rowIdx": 22,
                        "colIdx": 12,
                        "mapInfo": "107블록 23열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 309,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00023열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098528,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5719.895,
                                "y": 4523.23
                            },
                            "se": {
                                "x": 5728.569,
                                "y": 4528.206
                            },
                            "sw": {
                                "x": 5724.871,
                                "y": 4514.556
                            },
                            "nw": {
                                "x": 5733.545,
                                "y": 4519.532
                            }
                        },
                        "position": {
                            "x": 5726.7197,
                            "y": 4521.381
                        },
                        "rowIdx": 22,
                        "colIdx": 13,
                        "mapInfo": "107블록 23열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 310,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00023열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098536,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5690.245,
                                "y": 4603.059
                            },
                            "se": {
                                "x": 5698.919,
                                "y": 4608.035
                            },
                            "sw": {
                                "x": 5695.2207,
                                "y": 4594.385
                            },
                            "nw": {
                                "x": 5703.895,
                                "y": 4599.361
                            }
                        },
                        "position": {
                            "x": 5697.07,
                            "y": 4601.21
                        },
                        "rowIdx": 23,
                        "colIdx": 7,
                        "mapInfo": "107블록 24열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 318,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00024열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098537,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5697.215,
                                "y": 4590.915
                            },
                            "se": {
                                "x": 5705.889,
                                "y": 4595.891
                            },
                            "sw": {
                                "x": 5702.191,
                                "y": 4582.241
                            },
                            "nw": {
                                "x": 5710.865,
                                "y": 4587.217
                            }
                        },
                        "position": {
                            "x": 5704.04,
                            "y": 4589.066
                        },
                        "rowIdx": 23,
                        "colIdx": 8,
                        "mapInfo": "107블록 24열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 319,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00024열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098538,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5704.175,
                                "y": 4578.772
                            },
                            "se": {
                                "x": 5712.849,
                                "y": 4583.748
                            },
                            "sw": {
                                "x": 5709.151,
                                "y": 4570.098
                            },
                            "nw": {
                                "x": 5717.825,
                                "y": 4575.074
                            }
                        },
                        "position": {
                            "x": 5711.0,
                            "y": 4576.923
                        },
                        "rowIdx": 23,
                        "colIdx": 9,
                        "mapInfo": "107블록 24열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 320,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00024열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098539,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5711.145,
                                "y": 4566.628
                            },
                            "se": {
                                "x": 5719.819,
                                "y": 4571.604
                            },
                            "sw": {
                                "x": 5716.121,
                                "y": 4557.954
                            },
                            "nw": {
                                "x": 5724.795,
                                "y": 4562.93
                            }
                        },
                        "position": {
                            "x": 5717.9697,
                            "y": 4564.779
                        },
                        "rowIdx": 23,
                        "colIdx": 10,
                        "mapInfo": "107블록 24열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 321,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00024열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098540,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5718.1147,
                                "y": 4554.484
                            },
                            "se": {
                                "x": 5726.789,
                                "y": 4559.46
                            },
                            "sw": {
                                "x": 5723.091,
                                "y": 4545.81
                            },
                            "nw": {
                                "x": 5731.765,
                                "y": 4550.786
                            }
                        },
                        "position": {
                            "x": 5724.94,
                            "y": 4552.635
                        },
                        "rowIdx": 23,
                        "colIdx": 11,
                        "mapInfo": "107블록 24열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 322,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00024열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098541,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5725.075,
                                "y": 4542.34
                            },
                            "se": {
                                "x": 5733.749,
                                "y": 4547.316
                            },
                            "sw": {
                                "x": 5730.051,
                                "y": 4533.666
                            },
                            "nw": {
                                "x": 5738.725,
                                "y": 4538.642
                            }
                        },
                        "position": {
                            "x": 5731.9,
                            "y": 4540.491
                        },
                        "rowIdx": 23,
                        "colIdx": 12,
                        "mapInfo": "107블록 24열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 323,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00024열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098542,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5732.045,
                                "y": 4530.196
                            },
                            "se": {
                                "x": 5740.7188,
                                "y": 4535.172
                            },
                            "sw": {
                                "x": 5737.021,
                                "y": 4521.522
                            },
                            "nw": {
                                "x": 5745.6953,
                                "y": 4526.498
                            }
                        },
                        "position": {
                            "x": 5738.87,
                            "y": 4528.347
                        },
                        "rowIdx": 23,
                        "colIdx": 13,
                        "mapInfo": "107블록 24열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 324,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00024열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098550,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5709.355,
                                "y": 4597.882
                            },
                            "se": {
                                "x": 5718.0293,
                                "y": 4602.858
                            },
                            "sw": {
                                "x": 5714.331,
                                "y": 4589.208
                            },
                            "nw": {
                                "x": 5723.005,
                                "y": 4594.184
                            }
                        },
                        "position": {
                            "x": 5716.18,
                            "y": 4596.033
                        },
                        "rowIdx": 24,
                        "colIdx": 8,
                        "mapInfo": "107블록 25열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 332,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00025열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098551,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5716.325,
                                "y": 4585.737
                            },
                            "se": {
                                "x": 5724.999,
                                "y": 4590.713
                            },
                            "sw": {
                                "x": 5721.301,
                                "y": 4577.063
                            },
                            "nw": {
                                "x": 5729.975,
                                "y": 4582.039
                            }
                        },
                        "position": {
                            "x": 5723.15,
                            "y": 4583.888
                        },
                        "rowIdx": 24,
                        "colIdx": 9,
                        "mapInfo": "107블록 25열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 333,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00025열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098552,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5723.285,
                                "y": 4573.5938
                            },
                            "se": {
                                "x": 5731.959,
                                "y": 4578.57
                            },
                            "sw": {
                                "x": 5728.2607,
                                "y": 4564.92
                            },
                            "nw": {
                                "x": 5736.935,
                                "y": 4569.896
                            }
                        },
                        "position": {
                            "x": 5730.11,
                            "y": 4571.745
                        },
                        "rowIdx": 24,
                        "colIdx": 10,
                        "mapInfo": "107블록 25열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 334,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00025열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098553,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5730.255,
                                "y": 4561.45
                            },
                            "se": {
                                "x": 5738.9287,
                                "y": 4566.4263
                            },
                            "sw": {
                                "x": 5735.231,
                                "y": 4552.776
                            },
                            "nw": {
                                "x": 5743.9053,
                                "y": 4557.752
                            }
                        },
                        "position": {
                            "x": 5737.08,
                            "y": 4559.601
                        },
                        "rowIdx": 24,
                        "colIdx": 11,
                        "mapInfo": "107블록 25열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 335,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00025열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098554,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5737.225,
                                "y": 4549.306
                            },
                            "se": {
                                "x": 5745.899,
                                "y": 4554.282
                            },
                            "sw": {
                                "x": 5742.201,
                                "y": 4540.632
                            },
                            "nw": {
                                "x": 5750.875,
                                "y": 4545.608
                            }
                        },
                        "position": {
                            "x": 5744.05,
                            "y": 4547.457
                        },
                        "rowIdx": 24,
                        "colIdx": 12,
                        "mapInfo": "107블록 25열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 336,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00025열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098555,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5744.185,
                                "y": 4537.162
                            },
                            "se": {
                                "x": 5752.859,
                                "y": 4542.138
                            },
                            "sw": {
                                "x": 5749.161,
                                "y": 4528.488
                            },
                            "nw": {
                                "x": 5757.835,
                                "y": 4533.464
                            }
                        },
                        "position": {
                            "x": 5751.01,
                            "y": 4535.313
                        },
                        "rowIdx": 24,
                        "colIdx": 13,
                        "mapInfo": "107블록 25열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 337,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00025열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098564,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5721.505,
                                "y": 4604.848
                            },
                            "se": {
                                "x": 5730.1787,
                                "y": 4609.824
                            },
                            "sw": {
                                "x": 5726.481,
                                "y": 4596.174
                            },
                            "nw": {
                                "x": 5735.1553,
                                "y": 4601.15
                            }
                        },
                        "position": {
                            "x": 5728.33,
                            "y": 4602.999
                        },
                        "rowIdx": 25,
                        "colIdx": 8,
                        "mapInfo": "107블록 26열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 346,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00026열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098565,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5728.465,
                                "y": 4592.704
                            },
                            "se": {
                                "x": 5737.139,
                                "y": 4597.68
                            },
                            "sw": {
                                "x": 5733.441,
                                "y": 4584.03
                            },
                            "nw": {
                                "x": 5742.115,
                                "y": 4589.006
                            }
                        },
                        "position": {
                            "x": 5735.29,
                            "y": 4590.855
                        },
                        "rowIdx": 25,
                        "colIdx": 9,
                        "mapInfo": "107블록 26열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 347,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00026열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098566,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5735.435,
                                "y": 4580.56
                            },
                            "se": {
                                "x": 5744.109,
                                "y": 4585.536
                            },
                            "sw": {
                                "x": 5740.411,
                                "y": 4571.8857
                            },
                            "nw": {
                                "x": 5749.085,
                                "y": 4576.862
                            }
                        },
                        "position": {
                            "x": 5742.26,
                            "y": 4578.711
                        },
                        "rowIdx": 25,
                        "colIdx": 10,
                        "mapInfo": "107블록 26열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 348,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00026열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098567,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5742.395,
                                "y": 4568.416
                            },
                            "se": {
                                "x": 5751.069,
                                "y": 4573.392
                            },
                            "sw": {
                                "x": 5747.371,
                                "y": 4559.7417
                            },
                            "nw": {
                                "x": 5756.045,
                                "y": 4564.718
                            }
                        },
                        "position": {
                            "x": 5749.2197,
                            "y": 4566.567
                        },
                        "rowIdx": 25,
                        "colIdx": 11,
                        "mapInfo": "107블록 26열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 349,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00026열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098568,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5749.3647,
                                "y": 4556.272
                            },
                            "se": {
                                "x": 5758.039,
                                "y": 4561.248
                            },
                            "sw": {
                                "x": 5754.341,
                                "y": 4547.598
                            },
                            "nw": {
                                "x": 5763.015,
                                "y": 4552.574
                            }
                        },
                        "position": {
                            "x": 5756.19,
                            "y": 4554.423
                        },
                        "rowIdx": 25,
                        "colIdx": 12,
                        "mapInfo": "107블록 26열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 350,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00026열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098569,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5756.335,
                                "y": 4544.128
                            },
                            "se": {
                                "x": 5765.009,
                                "y": 4549.104
                            },
                            "sw": {
                                "x": 5761.311,
                                "y": 4535.454
                            },
                            "nw": {
                                "x": 5769.9854,
                                "y": 4540.43
                            }
                        },
                        "position": {
                            "x": 5763.16,
                            "y": 4542.279
                        },
                        "rowIdx": 25,
                        "colIdx": 13,
                        "mapInfo": "107블록 26열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 351,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00026열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098578,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5740.6147,
                                "y": 4599.67
                            },
                            "se": {
                                "x": 5749.289,
                                "y": 4604.646
                            },
                            "sw": {
                                "x": 5745.591,
                                "y": 4590.996
                            },
                            "nw": {
                                "x": 5754.265,
                                "y": 4595.972
                            }
                        },
                        "position": {
                            "x": 5747.44,
                            "y": 4597.821
                        },
                        "rowIdx": 26,
                        "colIdx": 9,
                        "mapInfo": "107블록 27열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 360,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00027열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098579,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5747.575,
                                "y": 4587.526
                            },
                            "se": {
                                "x": 5756.249,
                                "y": 4592.502
                            },
                            "sw": {
                                "x": 5752.551,
                                "y": 4578.852
                            },
                            "nw": {
                                "x": 5761.225,
                                "y": 4583.828
                            }
                        },
                        "position": {
                            "x": 5754.4,
                            "y": 4585.677
                        },
                        "rowIdx": 26,
                        "colIdx": 10,
                        "mapInfo": "107블록 27열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 361,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00027열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098580,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5754.545,
                                "y": 4575.382
                            },
                            "se": {
                                "x": 5763.2188,
                                "y": 4580.358
                            },
                            "sw": {
                                "x": 5759.521,
                                "y": 4566.708
                            },
                            "nw": {
                                "x": 5768.1953,
                                "y": 4571.684
                            }
                        },
                        "position": {
                            "x": 5761.37,
                            "y": 4573.533
                        },
                        "rowIdx": 26,
                        "colIdx": 11,
                        "mapInfo": "107블록 27열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 362,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00027열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098581,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5761.505,
                                "y": 4563.238
                            },
                            "se": {
                                "x": 5770.1787,
                                "y": 4568.214
                            },
                            "sw": {
                                "x": 5766.481,
                                "y": 4554.564
                            },
                            "nw": {
                                "x": 5775.1553,
                                "y": 4559.54
                            }
                        },
                        "position": {
                            "x": 5768.33,
                            "y": 4561.389
                        },
                        "rowIdx": 26,
                        "colIdx": 12,
                        "mapInfo": "107블록 27열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 363,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00027열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098582,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5768.475,
                                "y": 4551.0938
                            },
                            "se": {
                                "x": 5777.149,
                                "y": 4556.07
                            },
                            "sw": {
                                "x": 5773.451,
                                "y": 4542.42
                            },
                            "nw": {
                                "x": 5782.125,
                                "y": 4547.396
                            }
                        },
                        "position": {
                            "x": 5775.3,
                            "y": 4549.245
                        },
                        "rowIdx": 26,
                        "colIdx": 13,
                        "mapInfo": "107블록 27열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 364,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00027열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098592,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5752.755,
                                "y": 4606.635
                            },
                            "se": {
                                "x": 5761.4287,
                                "y": 4611.611
                            },
                            "sw": {
                                "x": 5757.731,
                                "y": 4597.961
                            },
                            "nw": {
                                "x": 5766.4053,
                                "y": 4602.937
                            }
                        },
                        "position": {
                            "x": 5759.58,
                            "y": 4604.786
                        },
                        "rowIdx": 27,
                        "colIdx": 9,
                        "mapInfo": "107블록 28열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 374,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00028열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098593,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5759.725,
                                "y": 4594.492
                            },
                            "se": {
                                "x": 5768.399,
                                "y": 4599.468
                            },
                            "sw": {
                                "x": 5764.701,
                                "y": 4585.818
                            },
                            "nw": {
                                "x": 5773.375,
                                "y": 4590.794
                            }
                        },
                        "position": {
                            "x": 5766.55,
                            "y": 4592.643
                        },
                        "rowIdx": 27,
                        "colIdx": 10,
                        "mapInfo": "107블록 28열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 375,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00028열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098594,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5766.685,
                                "y": 4582.348
                            },
                            "se": {
                                "x": 5775.359,
                                "y": 4587.324
                            },
                            "sw": {
                                "x": 5771.661,
                                "y": 4573.674
                            },
                            "nw": {
                                "x": 5780.335,
                                "y": 4578.65
                            }
                        },
                        "position": {
                            "x": 5773.51,
                            "y": 4580.499
                        },
                        "rowIdx": 27,
                        "colIdx": 11,
                        "mapInfo": "107블록 28열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 376,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00028열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098595,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5773.655,
                                "y": 4570.204
                            },
                            "se": {
                                "x": 5782.329,
                                "y": 4575.18
                            },
                            "sw": {
                                "x": 5778.631,
                                "y": 4561.53
                            },
                            "nw": {
                                "x": 5787.305,
                                "y": 4566.506
                            }
                        },
                        "position": {
                            "x": 5780.48,
                            "y": 4568.355
                        },
                        "rowIdx": 27,
                        "colIdx": 12,
                        "mapInfo": "107블록 28열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 377,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00028열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098596,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5780.6147,
                                "y": 4558.06
                            },
                            "se": {
                                "x": 5789.289,
                                "y": 4563.036
                            },
                            "sw": {
                                "x": 5785.591,
                                "y": 4549.3857
                            },
                            "nw": {
                                "x": 5794.265,
                                "y": 4554.362
                            }
                        },
                        "position": {
                            "x": 5787.44,
                            "y": 4556.211
                        },
                        "rowIdx": 27,
                        "colIdx": 13,
                        "mapInfo": "107블록 28열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 378,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00028열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098606,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5771.8647,
                                "y": 4601.458
                            },
                            "se": {
                                "x": 5780.539,
                                "y": 4606.434
                            },
                            "sw": {
                                "x": 5776.841,
                                "y": 4592.784
                            },
                            "nw": {
                                "x": 5785.515,
                                "y": 4597.76
                            }
                        },
                        "position": {
                            "x": 5778.69,
                            "y": 4599.609
                        },
                        "rowIdx": 28,
                        "colIdx": 10,
                        "mapInfo": "107블록 29열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 388,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00029열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098607,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5778.835,
                                "y": 4589.314
                            },
                            "se": {
                                "x": 5787.509,
                                "y": 4594.29
                            },
                            "sw": {
                                "x": 5783.811,
                                "y": 4580.64
                            },
                            "nw": {
                                "x": 5792.4854,
                                "y": 4585.616
                            }
                        },
                        "position": {
                            "x": 5785.66,
                            "y": 4587.465
                        },
                        "rowIdx": 28,
                        "colIdx": 11,
                        "mapInfo": "107블록 29열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 389,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00029열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098608,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5785.795,
                                "y": 4577.17
                            },
                            "se": {
                                "x": 5794.4688,
                                "y": 4582.146
                            },
                            "sw": {
                                "x": 5790.771,
                                "y": 4568.496
                            },
                            "nw": {
                                "x": 5799.4453,
                                "y": 4573.472
                            }
                        },
                        "position": {
                            "x": 5792.62,
                            "y": 4575.321
                        },
                        "rowIdx": 28,
                        "colIdx": 12,
                        "mapInfo": "107블록 29열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 390,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00029열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098609,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5792.7646,
                                "y": 4565.026
                            },
                            "se": {
                                "x": 5801.439,
                                "y": 4570.002
                            },
                            "sw": {
                                "x": 5797.741,
                                "y": 4556.352
                            },
                            "nw": {
                                "x": 5806.415,
                                "y": 4561.328
                            }
                        },
                        "position": {
                            "x": 5799.59,
                            "y": 4563.177
                        },
                        "rowIdx": 28,
                        "colIdx": 13,
                        "mapInfo": "107블록 29열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 391,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00029열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098620,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5784.005,
                                "y": 4608.424
                            },
                            "se": {
                                "x": 5792.6787,
                                "y": 4613.4
                            },
                            "sw": {
                                "x": 5788.981,
                                "y": 4599.75
                            },
                            "nw": {
                                "x": 5797.6553,
                                "y": 4604.726
                            }
                        },
                        "position": {
                            "x": 5790.83,
                            "y": 4606.575
                        },
                        "rowIdx": 29,
                        "colIdx": 10,
                        "mapInfo": "107블록 30열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 402,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00030열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098621,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5790.975,
                                "y": 4596.28
                            },
                            "se": {
                                "x": 5799.649,
                                "y": 4601.256
                            },
                            "sw": {
                                "x": 5795.951,
                                "y": 4587.606
                            },
                            "nw": {
                                "x": 5804.625,
                                "y": 4592.582
                            }
                        },
                        "position": {
                            "x": 5797.8,
                            "y": 4594.431
                        },
                        "rowIdx": 29,
                        "colIdx": 11,
                        "mapInfo": "107블록 30열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 403,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00030열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098622,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5797.945,
                                "y": 4584.1357
                            },
                            "se": {
                                "x": 5806.619,
                                "y": 4589.112
                            },
                            "sw": {
                                "x": 5802.921,
                                "y": 4575.462
                            },
                            "nw": {
                                "x": 5811.595,
                                "y": 4580.438
                            }
                        },
                        "position": {
                            "x": 5804.77,
                            "y": 4582.287
                        },
                        "rowIdx": 29,
                        "colIdx": 12,
                        "mapInfo": "107블록 30열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 404,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00030열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098623,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5804.905,
                                "y": 4571.992
                            },
                            "se": {
                                "x": 5813.579,
                                "y": 4576.968
                            },
                            "sw": {
                                "x": 5809.881,
                                "y": 4563.318
                            },
                            "nw": {
                                "x": 5818.555,
                                "y": 4568.294
                            }
                        },
                        "position": {
                            "x": 5811.73,
                            "y": 4570.143
                        },
                        "rowIdx": 29,
                        "colIdx": 13,
                        "mapInfo": "107블록 30열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 405,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00030열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098634,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5803.1147,
                                "y": 4603.246
                            },
                            "se": {
                                "x": 5811.789,
                                "y": 4608.222
                            },
                            "sw": {
                                "x": 5808.091,
                                "y": 4594.572
                            },
                            "nw": {
                                "x": 5816.765,
                                "y": 4599.548
                            }
                        },
                        "position": {
                            "x": 5809.94,
                            "y": 4601.397
                        },
                        "rowIdx": 30,
                        "colIdx": 11,
                        "mapInfo": "107블록 31열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 416,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00031열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098635,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5810.085,
                                "y": 4591.102
                            },
                            "se": {
                                "x": 5818.759,
                                "y": 4596.078
                            },
                            "sw": {
                                "x": 5815.061,
                                "y": 4582.4277
                            },
                            "nw": {
                                "x": 5823.7354,
                                "y": 4587.404
                            }
                        },
                        "position": {
                            "x": 5816.91,
                            "y": 4589.253
                        },
                        "rowIdx": 30,
                        "colIdx": 12,
                        "mapInfo": "107블록 31열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 417,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00031열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098636,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5817.0547,
                                "y": 4578.958
                            },
                            "se": {
                                "x": 5825.729,
                                "y": 4583.934
                            },
                            "sw": {
                                "x": 5822.0312,
                                "y": 4570.284
                            },
                            "nw": {
                                "x": 5830.705,
                                "y": 4575.26
                            }
                        },
                        "position": {
                            "x": 5823.88,
                            "y": 4577.109
                        },
                        "rowIdx": 30,
                        "colIdx": 13,
                        "mapInfo": "107블록 31열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 418,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00031열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098649,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5822.225,
                                "y": 4598.068
                            },
                            "se": {
                                "x": 5830.899,
                                "y": 4603.044
                            },
                            "sw": {
                                "x": 5827.201,
                                "y": 4589.394
                            },
                            "nw": {
                                "x": 5835.875,
                                "y": 4594.37
                            }
                        },
                        "position": {
                            "x": 5829.05,
                            "y": 4596.2188
                        },
                        "rowIdx": 31,
                        "colIdx": 12,
                        "mapInfo": "107블록 32열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 431,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00032열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098650,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5829.195,
                                "y": 4585.924
                            },
                            "se": {
                                "x": 5837.869,
                                "y": 4590.9
                            },
                            "sw": {
                                "x": 5834.171,
                                "y": 4577.25
                            },
                            "nw": {
                                "x": 5842.845,
                                "y": 4582.226
                            }
                        },
                        "position": {
                            "x": 5836.02,
                            "y": 4584.075
                        },
                        "rowIdx": 31,
                        "colIdx": 13,
                        "mapInfo": "107블록 32열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 432,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00032열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098662,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5834.375,
                                "y": 4605.034
                            },
                            "se": {
                                "x": 5843.049,
                                "y": 4610.01
                            },
                            "sw": {
                                "x": 5839.351,
                                "y": 4596.36
                            },
                            "nw": {
                                "x": 5848.025,
                                "y": 4601.336
                            }
                        },
                        "position": {
                            "x": 5841.2,
                            "y": 4603.185
                        },
                        "rowIdx": 32,
                        "colIdx": 12,
                        "mapInfo": "107블록 33열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 444,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00033열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098663,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5841.335,
                                "y": 4592.89
                            },
                            "se": {
                                "x": 5850.009,
                                "y": 4597.866
                            },
                            "sw": {
                                "x": 5846.311,
                                "y": 4584.216
                            },
                            "nw": {
                                "x": 5854.9854,
                                "y": 4589.192
                            }
                        },
                        "position": {
                            "x": 5848.16,
                            "y": 4591.041
                        },
                        "rowIdx": 32,
                        "colIdx": 13,
                        "mapInfo": "107블록 33열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 445,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00033열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098677,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5853.485,
                                "y": 4599.856
                            },
                            "se": {
                                "x": 5862.159,
                                "y": 4604.832
                            },
                            "sw": {
                                "x": 5858.461,
                                "y": 4591.1816
                            },
                            "nw": {
                                "x": 5867.1353,
                                "y": 4596.158
                            }
                        },
                        "position": {
                            "x": 5860.31,
                            "y": 4598.007
                        },
                        "rowIdx": 33,
                        "colIdx": 13,
                        "mapInfo": "107블록 34열 1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 459,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "1번"
                        ],
                        "sortMapInfo": "00107블록00034열00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 17
                        },
                         
                        "sectionId": 26536
                    }
                ],
                "22:18": [
                    {
                        "logicalSeatId": 1446098491,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5625.955,
                                "y": 4630.737
                            },
                            "se": {
                                "x": 5634.629,
                                "y": 4635.713
                            },
                            "sw": {
                                "x": 5630.931,
                                "y": 4622.063
                            },
                            "nw": {
                                "x": 5639.605,
                                "y": 4627.039
                            }
                        },
                        "position": {
                            "x": 5632.7803,
                            "y": 4628.888
                        },
                        "rowIdx": 20,
                        "colIdx": 3,
                        "mapInfo": "107블록 21열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 273,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00021열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098492,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5632.915,
                                "y": 4618.593
                            },
                            "se": {
                                "x": 5641.589,
                                "y": 4623.569
                            },
                            "sw": {
                                "x": 5637.891,
                                "y": 4609.919
                            },
                            "nw": {
                                "x": 5646.565,
                                "y": 4614.895
                            }
                        },
                        "position": {
                            "x": 5639.74,
                            "y": 4616.744
                        },
                        "rowIdx": 20,
                        "colIdx": 4,
                        "mapInfo": "107블록 21열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950914,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 274,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "21열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00021열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098504,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5631.125,
                                "y": 4649.847
                            },
                            "se": {
                                "x": 5639.799,
                                "y": 4654.823
                            },
                            "sw": {
                                "x": 5636.101,
                                "y": 4641.173
                            },
                            "nw": {
                                "x": 5644.775,
                                "y": 4646.149
                            }
                        },
                        "position": {
                            "x": 5637.95,
                            "y": 4647.998
                        },
                        "rowIdx": 21,
                        "colIdx": 2,
                        "mapInfo": "107블록 22열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 286,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00022열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098505,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5638.0947,
                                "y": 4637.703
                            },
                            "se": {
                                "x": 5646.769,
                                "y": 4642.679
                            },
                            "sw": {
                                "x": 5643.0713,
                                "y": 4629.029
                            },
                            "nw": {
                                "x": 5651.745,
                                "y": 4634.005
                            }
                        },
                        "position": {
                            "x": 5644.92,
                            "y": 4635.854
                        },
                        "rowIdx": 21,
                        "colIdx": 3,
                        "mapInfo": "107블록 22열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 287,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00022열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098506,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5645.065,
                                "y": 4625.559
                            },
                            "se": {
                                "x": 5653.7393,
                                "y": 4630.535
                            },
                            "sw": {
                                "x": 5650.041,
                                "y": 4616.885
                            },
                            "nw": {
                                "x": 5658.715,
                                "y": 4621.861
                            }
                        },
                        "position": {
                            "x": 5651.89,
                            "y": 4623.71
                        },
                        "rowIdx": 21,
                        "colIdx": 4,
                        "mapInfo": "107블록 22열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 288,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00022열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098507,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5652.025,
                                "y": 4613.415
                            },
                            "se": {
                                "x": 5660.699,
                                "y": 4618.391
                            },
                            "sw": {
                                "x": 5657.001,
                                "y": 4604.741
                            },
                            "nw": {
                                "x": 5665.675,
                                "y": 4609.717
                            }
                        },
                        "position": {
                            "x": 5658.85,
                            "y": 4611.566
                        },
                        "rowIdx": 21,
                        "colIdx": 5,
                        "mapInfo": "107블록 22열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950928,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 289,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "22열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00022열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098516,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5636.3047,
                                "y": 4668.957
                            },
                            "se": {
                                "x": 5644.979,
                                "y": 4673.933
                            },
                            "sw": {
                                "x": 5641.2812,
                                "y": 4660.283
                            },
                            "nw": {
                                "x": 5649.955,
                                "y": 4665.259
                            }
                        },
                        "position": {
                            "x": 5643.13,
                            "y": 4667.108
                        },
                        "rowIdx": 22,
                        "colIdx": 1,
                        "mapInfo": "107블록 23열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 298,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00023열00013번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098517,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5643.275,
                                "y": 4656.813
                            },
                            "se": {
                                "x": 5651.949,
                                "y": 4661.789
                            },
                            "sw": {
                                "x": 5648.251,
                                "y": 4648.139
                            },
                            "nw": {
                                "x": 5656.925,
                                "y": 4653.115
                            }
                        },
                        "position": {
                            "x": 5650.1,
                            "y": 4654.964
                        },
                        "rowIdx": 22,
                        "colIdx": 2,
                        "mapInfo": "107블록 23열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 299,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00023열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098518,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5650.235,
                                "y": 4644.669
                            },
                            "se": {
                                "x": 5658.909,
                                "y": 4649.645
                            },
                            "sw": {
                                "x": 5655.211,
                                "y": 4635.995
                            },
                            "nw": {
                                "x": 5663.8853,
                                "y": 4640.971
                            }
                        },
                        "position": {
                            "x": 5657.06,
                            "y": 4642.82
                        },
                        "rowIdx": 22,
                        "colIdx": 3,
                        "mapInfo": "107블록 23열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 300,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00023열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098519,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5657.205,
                                "y": 4632.525
                            },
                            "se": {
                                "x": 5665.879,
                                "y": 4637.501
                            },
                            "sw": {
                                "x": 5662.181,
                                "y": 4623.851
                            },
                            "nw": {
                                "x": 5670.855,
                                "y": 4628.827
                            }
                        },
                        "position": {
                            "x": 5664.0303,
                            "y": 4630.676
                        },
                        "rowIdx": 22,
                        "colIdx": 4,
                        "mapInfo": "107블록 23열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 301,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00023열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098520,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5664.175,
                                "y": 4620.381
                            },
                            "se": {
                                "x": 5672.849,
                                "y": 4625.357
                            },
                            "sw": {
                                "x": 5669.151,
                                "y": 4611.707
                            },
                            "nw": {
                                "x": 5677.825,
                                "y": 4616.683
                            }
                        },
                        "position": {
                            "x": 5671.0,
                            "y": 4618.532
                        },
                        "rowIdx": 22,
                        "colIdx": 5,
                        "mapInfo": "107블록 23열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950941,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 302,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "23열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00023열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098529,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5641.485,
                                "y": 4688.067
                            },
                            "se": {
                                "x": 5650.159,
                                "y": 4693.043
                            },
                            "sw": {
                                "x": 5646.461,
                                "y": 4679.393
                            },
                            "nw": {
                                "x": 5655.1353,
                                "y": 4684.369
                            }
                        },
                        "position": {
                            "x": 5648.31,
                            "y": 4686.218
                        },
                        "rowIdx": 23,
                        "colIdx": 0,
                        "mapInfo": "107블록 24열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 311,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00024열00014번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098530,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5648.455,
                                "y": 4675.923
                            },
                            "se": {
                                "x": 5657.129,
                                "y": 4680.899
                            },
                            "sw": {
                                "x": 5653.431,
                                "y": 4667.249
                            },
                            "nw": {
                                "x": 5662.105,
                                "y": 4672.225
                            }
                        },
                        "position": {
                            "x": 5655.2803,
                            "y": 4674.074
                        },
                        "rowIdx": 23,
                        "colIdx": 1,
                        "mapInfo": "107블록 24열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 312,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00024열00013번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098531,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5655.415,
                                "y": 4663.779
                            },
                            "se": {
                                "x": 5664.089,
                                "y": 4668.755
                            },
                            "sw": {
                                "x": 5660.391,
                                "y": 4655.105
                            },
                            "nw": {
                                "x": 5669.065,
                                "y": 4660.081
                            }
                        },
                        "position": {
                            "x": 5662.24,
                            "y": 4661.93
                        },
                        "rowIdx": 23,
                        "colIdx": 2,
                        "mapInfo": "107블록 24열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 313,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00024열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098532,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5662.385,
                                "y": 4651.635
                            },
                            "se": {
                                "x": 5671.059,
                                "y": 4656.611
                            },
                            "sw": {
                                "x": 5667.361,
                                "y": 4642.961
                            },
                            "nw": {
                                "x": 5676.035,
                                "y": 4647.937
                            }
                        },
                        "position": {
                            "x": 5669.21,
                            "y": 4649.786
                        },
                        "rowIdx": 23,
                        "colIdx": 3,
                        "mapInfo": "107블록 24열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 314,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00024열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098533,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5669.3447,
                                "y": 4639.491
                            },
                            "se": {
                                "x": 5678.019,
                                "y": 4644.467
                            },
                            "sw": {
                                "x": 5674.3213,
                                "y": 4630.817
                            },
                            "nw": {
                                "x": 5682.995,
                                "y": 4635.793
                            }
                        },
                        "position": {
                            "x": 5676.17,
                            "y": 4637.642
                        },
                        "rowIdx": 23,
                        "colIdx": 4,
                        "mapInfo": "107블록 24열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 315,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00024열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098534,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5676.315,
                                "y": 4627.347
                            },
                            "se": {
                                "x": 5684.9893,
                                "y": 4632.323
                            },
                            "sw": {
                                "x": 5681.291,
                                "y": 4618.673
                            },
                            "nw": {
                                "x": 5689.965,
                                "y": 4623.649
                            }
                        },
                        "position": {
                            "x": 5683.14,
                            "y": 4625.498
                        },
                        "rowIdx": 23,
                        "colIdx": 5,
                        "mapInfo": "107블록 24열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 316,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00024열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098535,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5683.285,
                                "y": 4615.203
                            },
                            "se": {
                                "x": 5691.959,
                                "y": 4620.179
                            },
                            "sw": {
                                "x": 5688.2607,
                                "y": 4606.529
                            },
                            "nw": {
                                "x": 5696.935,
                                "y": 4611.505
                            }
                        },
                        "position": {
                            "x": 5690.11,
                            "y": 4613.354
                        },
                        "rowIdx": 23,
                        "colIdx": 6,
                        "mapInfo": "107블록 24열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950955,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 317,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "24열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00024열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098543,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5660.5947,
                                "y": 4682.889
                            },
                            "se": {
                                "x": 5669.269,
                                "y": 4687.865
                            },
                            "sw": {
                                "x": 5665.5713,
                                "y": 4674.215
                            },
                            "nw": {
                                "x": 5674.245,
                                "y": 4679.191
                            }
                        },
                        "position": {
                            "x": 5667.42,
                            "y": 4681.04
                        },
                        "rowIdx": 24,
                        "colIdx": 1,
                        "mapInfo": "107블록 25열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 325,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00025열00013번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098544,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5667.565,
                                "y": 4670.745
                            },
                            "se": {
                                "x": 5676.2393,
                                "y": 4675.721
                            },
                            "sw": {
                                "x": 5672.541,
                                "y": 4662.071
                            },
                            "nw": {
                                "x": 5681.215,
                                "y": 4667.047
                            }
                        },
                        "position": {
                            "x": 5674.39,
                            "y": 4668.896
                        },
                        "rowIdx": 24,
                        "colIdx": 2,
                        "mapInfo": "107블록 25열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 326,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00025열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098545,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5674.525,
                                "y": 4658.601
                            },
                            "se": {
                                "x": 5683.199,
                                "y": 4663.577
                            },
                            "sw": {
                                "x": 5679.501,
                                "y": 4649.927
                            },
                            "nw": {
                                "x": 5688.175,
                                "y": 4654.903
                            }
                        },
                        "position": {
                            "x": 5681.35,
                            "y": 4656.752
                        },
                        "rowIdx": 24,
                        "colIdx": 3,
                        "mapInfo": "107블록 25열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 327,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00025열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098546,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5681.495,
                                "y": 4646.457
                            },
                            "se": {
                                "x": 5690.169,
                                "y": 4651.433
                            },
                            "sw": {
                                "x": 5686.4707,
                                "y": 4637.783
                            },
                            "nw": {
                                "x": 5695.145,
                                "y": 4642.759
                            }
                        },
                        "position": {
                            "x": 5688.32,
                            "y": 4644.608
                        },
                        "rowIdx": 24,
                        "colIdx": 4,
                        "mapInfo": "107블록 25열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 328,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00025열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098547,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5688.455,
                                "y": 4634.313
                            },
                            "se": {
                                "x": 5697.129,
                                "y": 4639.289
                            },
                            "sw": {
                                "x": 5693.431,
                                "y": 4625.639
                            },
                            "nw": {
                                "x": 5702.105,
                                "y": 4630.615
                            }
                        },
                        "position": {
                            "x": 5695.2803,
                            "y": 4632.464
                        },
                        "rowIdx": 24,
                        "colIdx": 5,
                        "mapInfo": "107블록 25열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 329,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00025열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098548,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5695.425,
                                "y": 4622.169
                            },
                            "se": {
                                "x": 5704.099,
                                "y": 4627.145
                            },
                            "sw": {
                                "x": 5700.401,
                                "y": 4613.495
                            },
                            "nw": {
                                "x": 5709.075,
                                "y": 4618.471
                            }
                        },
                        "position": {
                            "x": 5702.25,
                            "y": 4620.32
                        },
                        "rowIdx": 24,
                        "colIdx": 6,
                        "mapInfo": "107블록 25열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 330,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00025열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098549,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5702.395,
                                "y": 4610.025
                            },
                            "se": {
                                "x": 5711.069,
                                "y": 4615.001
                            },
                            "sw": {
                                "x": 5707.371,
                                "y": 4601.351
                            },
                            "nw": {
                                "x": 5716.045,
                                "y": 4606.327
                            }
                        },
                        "position": {
                            "x": 5709.2197,
                            "y": 4608.176
                        },
                        "rowIdx": 24,
                        "colIdx": 7,
                        "mapInfo": "107블록 25열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950968,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 331,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "25열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00025열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098556,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5665.775,
                                "y": 4701.999
                            },
                            "se": {
                                "x": 5674.449,
                                "y": 4706.975
                            },
                            "sw": {
                                "x": 5670.751,
                                "y": 4693.325
                            },
                            "nw": {
                                "x": 5679.425,
                                "y": 4698.301
                            }
                        },
                        "position": {
                            "x": 5672.6,
                            "y": 4700.15
                        },
                        "rowIdx": 25,
                        "colIdx": 0,
                        "mapInfo": "107블록 26열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 338,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00026열00014번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098557,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5672.735,
                                "y": 4689.855
                            },
                            "se": {
                                "x": 5681.409,
                                "y": 4694.831
                            },
                            "sw": {
                                "x": 5677.711,
                                "y": 4681.181
                            },
                            "nw": {
                                "x": 5686.3853,
                                "y": 4686.157
                            }
                        },
                        "position": {
                            "x": 5679.56,
                            "y": 4688.006
                        },
                        "rowIdx": 25,
                        "colIdx": 1,
                        "mapInfo": "107블록 26열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 339,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00026열00013번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098558,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5679.705,
                                "y": 4677.711
                            },
                            "se": {
                                "x": 5688.379,
                                "y": 4682.687
                            },
                            "sw": {
                                "x": 5684.681,
                                "y": 4669.037
                            },
                            "nw": {
                                "x": 5693.355,
                                "y": 4674.013
                            }
                        },
                        "position": {
                            "x": 5686.5303,
                            "y": 4675.862
                        },
                        "rowIdx": 25,
                        "colIdx": 2,
                        "mapInfo": "107블록 26열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 340,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00026열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098559,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5686.675,
                                "y": 4665.567
                            },
                            "se": {
                                "x": 5695.349,
                                "y": 4670.543
                            },
                            "sw": {
                                "x": 5691.651,
                                "y": 4656.893
                            },
                            "nw": {
                                "x": 5700.325,
                                "y": 4661.869
                            }
                        },
                        "position": {
                            "x": 5693.5,
                            "y": 4663.718
                        },
                        "rowIdx": 25,
                        "colIdx": 3,
                        "mapInfo": "107블록 26열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 341,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00026열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098560,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5693.635,
                                "y": 4653.423
                            },
                            "se": {
                                "x": 5702.309,
                                "y": 4658.399
                            },
                            "sw": {
                                "x": 5698.611,
                                "y": 4644.749
                            },
                            "nw": {
                                "x": 5707.285,
                                "y": 4649.725
                            }
                        },
                        "position": {
                            "x": 5700.46,
                            "y": 4651.574
                        },
                        "rowIdx": 25,
                        "colIdx": 4,
                        "mapInfo": "107블록 26열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 342,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00026열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098561,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5700.605,
                                "y": 4641.279
                            },
                            "se": {
                                "x": 5709.2793,
                                "y": 4646.255
                            },
                            "sw": {
                                "x": 5705.581,
                                "y": 4632.605
                            },
                            "nw": {
                                "x": 5714.255,
                                "y": 4637.581
                            }
                        },
                        "position": {
                            "x": 5707.43,
                            "y": 4639.43
                        },
                        "rowIdx": 25,
                        "colIdx": 5,
                        "mapInfo": "107블록 26열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 343,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00026열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098562,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5707.565,
                                "y": 4629.135
                            },
                            "se": {
                                "x": 5716.2393,
                                "y": 4634.111
                            },
                            "sw": {
                                "x": 5712.541,
                                "y": 4620.461
                            },
                            "nw": {
                                "x": 5721.215,
                                "y": 4625.437
                            }
                        },
                        "position": {
                            "x": 5714.39,
                            "y": 4627.286
                        },
                        "rowIdx": 25,
                        "colIdx": 6,
                        "mapInfo": "107블록 26열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 344,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00026열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098563,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5714.535,
                                "y": 4616.991
                            },
                            "se": {
                                "x": 5723.209,
                                "y": 4621.967
                            },
                            "sw": {
                                "x": 5719.5107,
                                "y": 4608.317
                            },
                            "nw": {
                                "x": 5728.185,
                                "y": 4613.293
                            }
                        },
                        "position": {
                            "x": 5721.36,
                            "y": 4615.142
                        },
                        "rowIdx": 25,
                        "colIdx": 7,
                        "mapInfo": "107블록 26열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950982,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 345,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "26열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00026열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098570,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5684.885,
                                "y": 4696.821
                            },
                            "se": {
                                "x": 5693.559,
                                "y": 4701.797
                            },
                            "sw": {
                                "x": 5689.861,
                                "y": 4688.147
                            },
                            "nw": {
                                "x": 5698.535,
                                "y": 4693.123
                            }
                        },
                        "position": {
                            "x": 5691.71,
                            "y": 4694.972
                        },
                        "rowIdx": 26,
                        "colIdx": 1,
                        "mapInfo": "107블록 27열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 352,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00027열00013번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098571,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5691.8447,
                                "y": 4684.677
                            },
                            "se": {
                                "x": 5700.519,
                                "y": 4689.653
                            },
                            "sw": {
                                "x": 5696.8213,
                                "y": 4676.003
                            },
                            "nw": {
                                "x": 5705.495,
                                "y": 4680.979
                            }
                        },
                        "position": {
                            "x": 5698.67,
                            "y": 4682.828
                        },
                        "rowIdx": 26,
                        "colIdx": 2,
                        "mapInfo": "107블록 27열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 353,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00027열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098572,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5698.815,
                                "y": 4672.533
                            },
                            "se": {
                                "x": 5707.4893,
                                "y": 4677.509
                            },
                            "sw": {
                                "x": 5703.791,
                                "y": 4663.859
                            },
                            "nw": {
                                "x": 5712.465,
                                "y": 4668.835
                            }
                        },
                        "position": {
                            "x": 5705.64,
                            "y": 4670.684
                        },
                        "rowIdx": 26,
                        "colIdx": 3,
                        "mapInfo": "107블록 27열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 354,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00027열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098573,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5705.785,
                                "y": 4660.389
                            },
                            "se": {
                                "x": 5714.459,
                                "y": 4665.365
                            },
                            "sw": {
                                "x": 5710.7607,
                                "y": 4651.715
                            },
                            "nw": {
                                "x": 5719.435,
                                "y": 4656.691
                            }
                        },
                        "position": {
                            "x": 5712.61,
                            "y": 4658.54
                        },
                        "rowIdx": 26,
                        "colIdx": 4,
                        "mapInfo": "107블록 27열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 355,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00027열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098574,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5712.745,
                                "y": 4648.245
                            },
                            "se": {
                                "x": 5721.419,
                                "y": 4653.221
                            },
                            "sw": {
                                "x": 5717.7207,
                                "y": 4639.571
                            },
                            "nw": {
                                "x": 5726.395,
                                "y": 4644.547
                            }
                        },
                        "position": {
                            "x": 5719.57,
                            "y": 4646.396
                        },
                        "rowIdx": 26,
                        "colIdx": 5,
                        "mapInfo": "107블록 27열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 356,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00027열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098575,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5719.715,
                                "y": 4636.101
                            },
                            "se": {
                                "x": 5728.389,
                                "y": 4641.077
                            },
                            "sw": {
                                "x": 5724.691,
                                "y": 4627.427
                            },
                            "nw": {
                                "x": 5733.365,
                                "y": 4632.403
                            }
                        },
                        "position": {
                            "x": 5726.54,
                            "y": 4634.252
                        },
                        "rowIdx": 26,
                        "colIdx": 6,
                        "mapInfo": "107블록 27열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 357,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00027열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098576,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5726.675,
                                "y": 4623.957
                            },
                            "se": {
                                "x": 5735.349,
                                "y": 4628.933
                            },
                            "sw": {
                                "x": 5731.651,
                                "y": 4615.283
                            },
                            "nw": {
                                "x": 5740.325,
                                "y": 4620.259
                            }
                        },
                        "position": {
                            "x": 5733.5,
                            "y": 4622.108
                        },
                        "rowIdx": 26,
                        "colIdx": 7,
                        "mapInfo": "107블록 27열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 358,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00027열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098577,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5733.645,
                                "y": 4611.813
                            },
                            "se": {
                                "x": 5742.319,
                                "y": 4616.789
                            },
                            "sw": {
                                "x": 5738.621,
                                "y": 4603.1387
                            },
                            "nw": {
                                "x": 5747.295,
                                "y": 4608.115
                            }
                        },
                        "position": {
                            "x": 5740.4697,
                            "y": 4609.964
                        },
                        "rowIdx": 26,
                        "colIdx": 8,
                        "mapInfo": "107블록 27열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6950995,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 359,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "27열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00027열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098583,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5690.065,
                                "y": 4715.931
                            },
                            "se": {
                                "x": 5698.7393,
                                "y": 4720.907
                            },
                            "sw": {
                                "x": 5695.041,
                                "y": 4707.257
                            },
                            "nw": {
                                "x": 5703.715,
                                "y": 4712.233
                            }
                        },
                        "position": {
                            "x": 5696.89,
                            "y": 4714.082
                        },
                        "rowIdx": 27,
                        "colIdx": 0,
                        "mapInfo": "107블록 28열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 365,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00028열00014번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098584,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5697.025,
                                "y": 4703.787
                            },
                            "se": {
                                "x": 5705.699,
                                "y": 4708.763
                            },
                            "sw": {
                                "x": 5702.001,
                                "y": 4695.113
                            },
                            "nw": {
                                "x": 5710.675,
                                "y": 4700.089
                            }
                        },
                        "position": {
                            "x": 5703.85,
                            "y": 4701.938
                        },
                        "rowIdx": 27,
                        "colIdx": 1,
                        "mapInfo": "107블록 28열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 366,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00028열00013번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098585,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5703.995,
                                "y": 4691.643
                            },
                            "se": {
                                "x": 5712.669,
                                "y": 4696.619
                            },
                            "sw": {
                                "x": 5708.9707,
                                "y": 4682.9688
                            },
                            "nw": {
                                "x": 5717.645,
                                "y": 4687.945
                            }
                        },
                        "position": {
                            "x": 5710.82,
                            "y": 4689.794
                        },
                        "rowIdx": 27,
                        "colIdx": 2,
                        "mapInfo": "107블록 28열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 367,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00028열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098586,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5710.955,
                                "y": 4679.499
                            },
                            "se": {
                                "x": 5719.629,
                                "y": 4684.475
                            },
                            "sw": {
                                "x": 5715.931,
                                "y": 4670.825
                            },
                            "nw": {
                                "x": 5724.605,
                                "y": 4675.801
                            }
                        },
                        "position": {
                            "x": 5717.7803,
                            "y": 4677.65
                        },
                        "rowIdx": 27,
                        "colIdx": 3,
                        "mapInfo": "107블록 28열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 368,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00028열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098587,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5717.925,
                                "y": 4667.355
                            },
                            "se": {
                                "x": 5726.599,
                                "y": 4672.331
                            },
                            "sw": {
                                "x": 5722.901,
                                "y": 4658.681
                            },
                            "nw": {
                                "x": 5731.575,
                                "y": 4663.657
                            }
                        },
                        "position": {
                            "x": 5724.75,
                            "y": 4665.506
                        },
                        "rowIdx": 27,
                        "colIdx": 4,
                        "mapInfo": "107블록 28열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 369,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00028열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098588,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5724.895,
                                "y": 4655.211
                            },
                            "se": {
                                "x": 5733.569,
                                "y": 4660.187
                            },
                            "sw": {
                                "x": 5729.871,
                                "y": 4646.537
                            },
                            "nw": {
                                "x": 5738.545,
                                "y": 4651.513
                            }
                        },
                        "position": {
                            "x": 5731.7197,
                            "y": 4653.362
                        },
                        "rowIdx": 27,
                        "colIdx": 5,
                        "mapInfo": "107블록 28열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 370,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00028열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098589,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5731.855,
                                "y": 4643.067
                            },
                            "se": {
                                "x": 5740.5293,
                                "y": 4648.043
                            },
                            "sw": {
                                "x": 5736.831,
                                "y": 4634.393
                            },
                            "nw": {
                                "x": 5745.505,
                                "y": 4639.369
                            }
                        },
                        "position": {
                            "x": 5738.68,
                            "y": 4641.218
                        },
                        "rowIdx": 27,
                        "colIdx": 6,
                        "mapInfo": "107블록 28열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 371,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00028열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098590,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5738.825,
                                "y": 4630.923
                            },
                            "se": {
                                "x": 5747.499,
                                "y": 4635.899
                            },
                            "sw": {
                                "x": 5743.801,
                                "y": 4622.249
                            },
                            "nw": {
                                "x": 5752.475,
                                "y": 4627.225
                            }
                        },
                        "position": {
                            "x": 5745.65,
                            "y": 4629.074
                        },
                        "rowIdx": 27,
                        "colIdx": 7,
                        "mapInfo": "107블록 28열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 372,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00028열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098591,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5745.785,
                                "y": 4618.779
                            },
                            "se": {
                                "x": 5754.459,
                                "y": 4623.755
                            },
                            "sw": {
                                "x": 5750.7607,
                                "y": 4610.105
                            },
                            "nw": {
                                "x": 5759.435,
                                "y": 4615.081
                            }
                        },
                        "position": {
                            "x": 5752.61,
                            "y": 4616.93
                        },
                        "rowIdx": 27,
                        "colIdx": 8,
                        "mapInfo": "107블록 28열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951009,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 373,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "28열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00028열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098597,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5709.175,
                                "y": 4710.753
                            },
                            "se": {
                                "x": 5717.849,
                                "y": 4715.729
                            },
                            "sw": {
                                "x": 5714.151,
                                "y": 4702.079
                            },
                            "nw": {
                                "x": 5722.825,
                                "y": 4707.055
                            }
                        },
                        "position": {
                            "x": 5716.0,
                            "y": 4708.904
                        },
                        "rowIdx": 28,
                        "colIdx": 1,
                        "mapInfo": "107블록 29열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 379,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00029열00013번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098598,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5716.135,
                                "y": 4698.609
                            },
                            "se": {
                                "x": 5724.809,
                                "y": 4703.585
                            },
                            "sw": {
                                "x": 5721.111,
                                "y": 4689.935
                            },
                            "nw": {
                                "x": 5729.785,
                                "y": 4694.911
                            }
                        },
                        "position": {
                            "x": 5722.96,
                            "y": 4696.76
                        },
                        "rowIdx": 28,
                        "colIdx": 2,
                        "mapInfo": "107블록 29열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 380,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00029열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098599,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5723.105,
                                "y": 4686.465
                            },
                            "se": {
                                "x": 5731.7793,
                                "y": 4691.441
                            },
                            "sw": {
                                "x": 5728.081,
                                "y": 4677.791
                            },
                            "nw": {
                                "x": 5736.755,
                                "y": 4682.767
                            }
                        },
                        "position": {
                            "x": 5729.93,
                            "y": 4684.616
                        },
                        "rowIdx": 28,
                        "colIdx": 3,
                        "mapInfo": "107블록 29열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 381,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00029열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098600,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5730.065,
                                "y": 4674.321
                            },
                            "se": {
                                "x": 5738.7393,
                                "y": 4679.297
                            },
                            "sw": {
                                "x": 5735.041,
                                "y": 4665.647
                            },
                            "nw": {
                                "x": 5743.715,
                                "y": 4670.623
                            }
                        },
                        "position": {
                            "x": 5736.89,
                            "y": 4672.472
                        },
                        "rowIdx": 28,
                        "colIdx": 4,
                        "mapInfo": "107블록 29열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 382,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00029열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098601,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5737.035,
                                "y": 4662.177
                            },
                            "se": {
                                "x": 5745.709,
                                "y": 4667.153
                            },
                            "sw": {
                                "x": 5742.0107,
                                "y": 4653.503
                            },
                            "nw": {
                                "x": 5750.685,
                                "y": 4658.479
                            }
                        },
                        "position": {
                            "x": 5743.86,
                            "y": 4660.328
                        },
                        "rowIdx": 28,
                        "colIdx": 5,
                        "mapInfo": "107블록 29열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 383,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00029열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098602,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5744.005,
                                "y": 4650.033
                            },
                            "se": {
                                "x": 5752.6787,
                                "y": 4655.009
                            },
                            "sw": {
                                "x": 5748.981,
                                "y": 4641.359
                            },
                            "nw": {
                                "x": 5757.6553,
                                "y": 4646.335
                            }
                        },
                        "position": {
                            "x": 5750.83,
                            "y": 4648.184
                        },
                        "rowIdx": 28,
                        "colIdx": 6,
                        "mapInfo": "107블록 29열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 384,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00029열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098603,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5750.965,
                                "y": 4637.889
                            },
                            "se": {
                                "x": 5759.639,
                                "y": 4642.865
                            },
                            "sw": {
                                "x": 5755.941,
                                "y": 4629.215
                            },
                            "nw": {
                                "x": 5764.615,
                                "y": 4634.191
                            }
                        },
                        "position": {
                            "x": 5757.79,
                            "y": 4636.04
                        },
                        "rowIdx": 28,
                        "colIdx": 7,
                        "mapInfo": "107블록 29열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 385,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00029열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098604,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5757.935,
                                "y": 4625.745
                            },
                            "se": {
                                "x": 5766.609,
                                "y": 4630.721
                            },
                            "sw": {
                                "x": 5762.911,
                                "y": 4617.071
                            },
                            "nw": {
                                "x": 5771.585,
                                "y": 4622.047
                            }
                        },
                        "position": {
                            "x": 5764.76,
                            "y": 4623.896
                        },
                        "rowIdx": 28,
                        "colIdx": 8,
                        "mapInfo": "107블록 29열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 386,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00029열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098605,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5764.895,
                                "y": 4613.602
                            },
                            "se": {
                                "x": 5773.569,
                                "y": 4618.578
                            },
                            "sw": {
                                "x": 5769.871,
                                "y": 4604.9277
                            },
                            "nw": {
                                "x": 5778.545,
                                "y": 4609.904
                            }
                        },
                        "position": {
                            "x": 5771.7197,
                            "y": 4611.753
                        },
                        "rowIdx": 28,
                        "colIdx": 9,
                        "mapInfo": "107블록 29열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951022,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 387,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "29열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00029열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098610,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5714.3447,
                                "y": 4729.863
                            },
                            "se": {
                                "x": 5723.019,
                                "y": 4734.839
                            },
                            "sw": {
                                "x": 5719.3213,
                                "y": 4721.189
                            },
                            "nw": {
                                "x": 5727.995,
                                "y": 4726.165
                            }
                        },
                        "position": {
                            "x": 5721.17,
                            "y": 4728.014
                        },
                        "rowIdx": 29,
                        "colIdx": 0,
                        "mapInfo": "107블록 30열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 392,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00030열00014번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098611,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5721.315,
                                "y": 4717.7188
                            },
                            "se": {
                                "x": 5729.9893,
                                "y": 4722.695
                            },
                            "sw": {
                                "x": 5726.291,
                                "y": 4709.045
                            },
                            "nw": {
                                "x": 5734.965,
                                "y": 4714.021
                            }
                        },
                        "position": {
                            "x": 5728.14,
                            "y": 4715.87
                        },
                        "rowIdx": 29,
                        "colIdx": 1,
                        "mapInfo": "107블록 30열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 393,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00030열00013번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098612,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5728.285,
                                "y": 4705.575
                            },
                            "se": {
                                "x": 5736.959,
                                "y": 4710.551
                            },
                            "sw": {
                                "x": 5733.2607,
                                "y": 4696.901
                            },
                            "nw": {
                                "x": 5741.935,
                                "y": 4701.877
                            }
                        },
                        "position": {
                            "x": 5735.11,
                            "y": 4703.726
                        },
                        "rowIdx": 29,
                        "colIdx": 2,
                        "mapInfo": "107블록 30열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 394,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00030열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098613,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5735.245,
                                "y": 4693.431
                            },
                            "se": {
                                "x": 5743.919,
                                "y": 4698.407
                            },
                            "sw": {
                                "x": 5740.2207,
                                "y": 4684.757
                            },
                            "nw": {
                                "x": 5748.895,
                                "y": 4689.733
                            }
                        },
                        "position": {
                            "x": 5742.07,
                            "y": 4691.582
                        },
                        "rowIdx": 29,
                        "colIdx": 3,
                        "mapInfo": "107블록 30열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 395,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00030열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098614,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5742.215,
                                "y": 4681.287
                            },
                            "se": {
                                "x": 5750.889,
                                "y": 4686.263
                            },
                            "sw": {
                                "x": 5747.191,
                                "y": 4672.613
                            },
                            "nw": {
                                "x": 5755.865,
                                "y": 4677.589
                            }
                        },
                        "position": {
                            "x": 5749.04,
                            "y": 4679.438
                        },
                        "rowIdx": 29,
                        "colIdx": 4,
                        "mapInfo": "107블록 30열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 396,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00030열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098615,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5749.175,
                                "y": 4669.143
                            },
                            "se": {
                                "x": 5757.849,
                                "y": 4674.119
                            },
                            "sw": {
                                "x": 5754.151,
                                "y": 4660.4688
                            },
                            "nw": {
                                "x": 5762.825,
                                "y": 4665.445
                            }
                        },
                        "position": {
                            "x": 5756.0,
                            "y": 4667.294
                        },
                        "rowIdx": 29,
                        "colIdx": 5,
                        "mapInfo": "107블록 30열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 397,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00030열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098616,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5756.145,
                                "y": 4656.999
                            },
                            "se": {
                                "x": 5764.819,
                                "y": 4661.975
                            },
                            "sw": {
                                "x": 5761.121,
                                "y": 4648.325
                            },
                            "nw": {
                                "x": 5769.795,
                                "y": 4653.301
                            }
                        },
                        "position": {
                            "x": 5762.9697,
                            "y": 4655.15
                        },
                        "rowIdx": 29,
                        "colIdx": 6,
                        "mapInfo": "107블록 30열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 398,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00030열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098617,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5763.1147,
                                "y": 4644.855
                            },
                            "se": {
                                "x": 5771.789,
                                "y": 4649.831
                            },
                            "sw": {
                                "x": 5768.091,
                                "y": 4636.181
                            },
                            "nw": {
                                "x": 5776.765,
                                "y": 4641.157
                            }
                        },
                        "position": {
                            "x": 5769.94,
                            "y": 4643.006
                        },
                        "rowIdx": 29,
                        "colIdx": 7,
                        "mapInfo": "107블록 30열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 399,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00030열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098618,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5770.075,
                                "y": 4632.711
                            },
                            "se": {
                                "x": 5778.749,
                                "y": 4637.687
                            },
                            "sw": {
                                "x": 5775.051,
                                "y": 4624.037
                            },
                            "nw": {
                                "x": 5783.725,
                                "y": 4629.013
                            }
                        },
                        "position": {
                            "x": 5776.9,
                            "y": 4630.862
                        },
                        "rowIdx": 29,
                        "colIdx": 8,
                        "mapInfo": "107블록 30열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 400,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00030열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098619,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5777.045,
                                "y": 4620.568
                            },
                            "se": {
                                "x": 5785.7188,
                                "y": 4625.544
                            },
                            "sw": {
                                "x": 5782.021,
                                "y": 4611.894
                            },
                            "nw": {
                                "x": 5790.6953,
                                "y": 4616.87
                            }
                        },
                        "position": {
                            "x": 5783.87,
                            "y": 4618.7188
                        },
                        "rowIdx": 29,
                        "colIdx": 9,
                        "mapInfo": "107블록 30열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951036,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 401,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "30열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00030열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098624,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5733.455,
                                "y": 4724.685
                            },
                            "se": {
                                "x": 5742.129,
                                "y": 4729.661
                            },
                            "sw": {
                                "x": 5738.431,
                                "y": 4716.0107
                            },
                            "nw": {
                                "x": 5747.105,
                                "y": 4720.987
                            }
                        },
                        "position": {
                            "x": 5740.2803,
                            "y": 4722.836
                        },
                        "rowIdx": 30,
                        "colIdx": 1,
                        "mapInfo": "107블록 31열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 406,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00031열00013번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098625,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5740.425,
                                "y": 4712.541
                            },
                            "se": {
                                "x": 5749.099,
                                "y": 4717.517
                            },
                            "sw": {
                                "x": 5745.401,
                                "y": 4703.867
                            },
                            "nw": {
                                "x": 5754.075,
                                "y": 4708.843
                            }
                        },
                        "position": {
                            "x": 5747.25,
                            "y": 4710.692
                        },
                        "rowIdx": 30,
                        "colIdx": 2,
                        "mapInfo": "107블록 31열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 407,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00031열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098626,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5747.395,
                                "y": 4700.397
                            },
                            "se": {
                                "x": 5756.069,
                                "y": 4705.373
                            },
                            "sw": {
                                "x": 5752.371,
                                "y": 4691.723
                            },
                            "nw": {
                                "x": 5761.045,
                                "y": 4696.699
                            }
                        },
                        "position": {
                            "x": 5754.2197,
                            "y": 4698.548
                        },
                        "rowIdx": 30,
                        "colIdx": 3,
                        "mapInfo": "107블록 31열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 408,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00031열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098627,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5754.355,
                                "y": 4688.253
                            },
                            "se": {
                                "x": 5763.0293,
                                "y": 4693.229
                            },
                            "sw": {
                                "x": 5759.331,
                                "y": 4679.579
                            },
                            "nw": {
                                "x": 5768.005,
                                "y": 4684.555
                            }
                        },
                        "position": {
                            "x": 5761.18,
                            "y": 4686.404
                        },
                        "rowIdx": 30,
                        "colIdx": 4,
                        "mapInfo": "107블록 31열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 409,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00031열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098628,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5761.325,
                                "y": 4676.109
                            },
                            "se": {
                                "x": 5769.999,
                                "y": 4681.085
                            },
                            "sw": {
                                "x": 5766.301,
                                "y": 4667.435
                            },
                            "nw": {
                                "x": 5774.975,
                                "y": 4672.411
                            }
                        },
                        "position": {
                            "x": 5768.15,
                            "y": 4674.26
                        },
                        "rowIdx": 30,
                        "colIdx": 5,
                        "mapInfo": "107블록 31열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 410,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00031열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098629,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5768.285,
                                "y": 4663.965
                            },
                            "se": {
                                "x": 5776.959,
                                "y": 4668.941
                            },
                            "sw": {
                                "x": 5773.2607,
                                "y": 4655.291
                            },
                            "nw": {
                                "x": 5781.935,
                                "y": 4660.267
                            }
                        },
                        "position": {
                            "x": 5775.11,
                            "y": 4662.116
                        },
                        "rowIdx": 30,
                        "colIdx": 6,
                        "mapInfo": "107블록 31열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 411,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00031열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098630,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5775.255,
                                "y": 4651.821
                            },
                            "se": {
                                "x": 5783.9287,
                                "y": 4656.797
                            },
                            "sw": {
                                "x": 5780.231,
                                "y": 4643.147
                            },
                            "nw": {
                                "x": 5788.9053,
                                "y": 4648.123
                            }
                        },
                        "position": {
                            "x": 5782.08,
                            "y": 4649.972
                        },
                        "rowIdx": 30,
                        "colIdx": 7,
                        "mapInfo": "107블록 31열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 412,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00031열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098631,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5782.225,
                                "y": 4639.677
                            },
                            "se": {
                                "x": 5790.899,
                                "y": 4644.653
                            },
                            "sw": {
                                "x": 5787.201,
                                "y": 4631.003
                            },
                            "nw": {
                                "x": 5795.875,
                                "y": 4635.979
                            }
                        },
                        "position": {
                            "x": 5789.05,
                            "y": 4637.828
                        },
                        "rowIdx": 30,
                        "colIdx": 8,
                        "mapInfo": "107블록 31열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 413,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00031열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098632,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5789.185,
                                "y": 4627.534
                            },
                            "se": {
                                "x": 5797.859,
                                "y": 4632.51
                            },
                            "sw": {
                                "x": 5794.161,
                                "y": 4618.86
                            },
                            "nw": {
                                "x": 5802.835,
                                "y": 4623.836
                            }
                        },
                        "position": {
                            "x": 5796.01,
                            "y": 4625.685
                        },
                        "rowIdx": 30,
                        "colIdx": 9,
                        "mapInfo": "107블록 31열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 414,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00031열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098633,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5796.155,
                                "y": 4615.39
                            },
                            "se": {
                                "x": 5804.829,
                                "y": 4620.366
                            },
                            "sw": {
                                "x": 5801.131,
                                "y": 4606.716
                            },
                            "nw": {
                                "x": 5809.805,
                                "y": 4611.692
                            }
                        },
                        "position": {
                            "x": 5802.98,
                            "y": 4613.541
                        },
                        "rowIdx": 30,
                        "colIdx": 10,
                        "mapInfo": "107블록 31열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951049,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 415,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "31열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00031열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098637,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5738.635,
                                "y": 4743.795
                            },
                            "se": {
                                "x": 5747.309,
                                "y": 4748.771
                            },
                            "sw": {
                                "x": 5743.611,
                                "y": 4735.121
                            },
                            "nw": {
                                "x": 5752.285,
                                "y": 4740.097
                            }
                        },
                        "position": {
                            "x": 5745.46,
                            "y": 4741.946
                        },
                        "rowIdx": 31,
                        "colIdx": 0,
                        "mapInfo": "107블록 32열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 419,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00032열00014번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098638,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5745.605,
                                "y": 4731.651
                            },
                            "se": {
                                "x": 5754.2793,
                                "y": 4736.627
                            },
                            "sw": {
                                "x": 5750.581,
                                "y": 4722.977
                            },
                            "nw": {
                                "x": 5759.255,
                                "y": 4727.953
                            }
                        },
                        "position": {
                            "x": 5752.43,
                            "y": 4729.802
                        },
                        "rowIdx": 31,
                        "colIdx": 1,
                        "mapInfo": "107블록 32열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 420,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00032열00013번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098639,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5752.565,
                                "y": 4719.507
                            },
                            "se": {
                                "x": 5761.2393,
                                "y": 4724.483
                            },
                            "sw": {
                                "x": 5757.541,
                                "y": 4710.833
                            },
                            "nw": {
                                "x": 5766.215,
                                "y": 4715.809
                            }
                        },
                        "position": {
                            "x": 5759.39,
                            "y": 4717.658
                        },
                        "rowIdx": 31,
                        "colIdx": 2,
                        "mapInfo": "107블록 32열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 421,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00032열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098640,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5759.535,
                                "y": 4707.363
                            },
                            "se": {
                                "x": 5768.209,
                                "y": 4712.339
                            },
                            "sw": {
                                "x": 5764.5107,
                                "y": 4698.689
                            },
                            "nw": {
                                "x": 5773.185,
                                "y": 4703.665
                            }
                        },
                        "position": {
                            "x": 5766.36,
                            "y": 4705.514
                        },
                        "rowIdx": 31,
                        "colIdx": 3,
                        "mapInfo": "107블록 32열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 422,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00032열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098641,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5766.505,
                                "y": 4695.2188
                            },
                            "se": {
                                "x": 5775.1787,
                                "y": 4700.195
                            },
                            "sw": {
                                "x": 5771.481,
                                "y": 4686.545
                            },
                            "nw": {
                                "x": 5780.1553,
                                "y": 4691.521
                            }
                        },
                        "position": {
                            "x": 5773.33,
                            "y": 4693.37
                        },
                        "rowIdx": 31,
                        "colIdx": 4,
                        "mapInfo": "107블록 32열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 423,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00032열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098642,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5773.465,
                                "y": 4683.075
                            },
                            "se": {
                                "x": 5782.139,
                                "y": 4688.051
                            },
                            "sw": {
                                "x": 5778.441,
                                "y": 4674.401
                            },
                            "nw": {
                                "x": 5787.115,
                                "y": 4679.377
                            }
                        },
                        "position": {
                            "x": 5780.29,
                            "y": 4681.226
                        },
                        "rowIdx": 31,
                        "colIdx": 5,
                        "mapInfo": "107블록 32열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 424,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00032열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098643,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5780.435,
                                "y": 4670.931
                            },
                            "se": {
                                "x": 5789.109,
                                "y": 4675.907
                            },
                            "sw": {
                                "x": 5785.411,
                                "y": 4662.257
                            },
                            "nw": {
                                "x": 5794.085,
                                "y": 4667.233
                            }
                        },
                        "position": {
                            "x": 5787.26,
                            "y": 4669.082
                        },
                        "rowIdx": 31,
                        "colIdx": 6,
                        "mapInfo": "107블록 32열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 425,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00032열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098644,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5787.395,
                                "y": 4658.787
                            },
                            "se": {
                                "x": 5796.069,
                                "y": 4663.763
                            },
                            "sw": {
                                "x": 5792.371,
                                "y": 4650.113
                            },
                            "nw": {
                                "x": 5801.045,
                                "y": 4655.089
                            }
                        },
                        "position": {
                            "x": 5794.2197,
                            "y": 4656.938
                        },
                        "rowIdx": 31,
                        "colIdx": 7,
                        "mapInfo": "107블록 32열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 426,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00032열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098645,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5794.3647,
                                "y": 4646.643
                            },
                            "se": {
                                "x": 5803.039,
                                "y": 4651.619
                            },
                            "sw": {
                                "x": 5799.341,
                                "y": 4637.9688
                            },
                            "nw": {
                                "x": 5808.015,
                                "y": 4642.945
                            }
                        },
                        "position": {
                            "x": 5801.19,
                            "y": 4644.794
                        },
                        "rowIdx": 31,
                        "colIdx": 8,
                        "mapInfo": "107블록 32열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 427,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00032열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098646,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5801.335,
                                "y": 4634.5
                            },
                            "se": {
                                "x": 5810.009,
                                "y": 4639.476
                            },
                            "sw": {
                                "x": 5806.311,
                                "y": 4625.826
                            },
                            "nw": {
                                "x": 5814.9854,
                                "y": 4630.802
                            }
                        },
                        "position": {
                            "x": 5808.16,
                            "y": 4632.651
                        },
                        "rowIdx": 31,
                        "colIdx": 9,
                        "mapInfo": "107블록 32열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 428,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00032열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098647,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5808.295,
                                "y": 4622.356
                            },
                            "se": {
                                "x": 5816.9688,
                                "y": 4627.332
                            },
                            "sw": {
                                "x": 5813.271,
                                "y": 4613.682
                            },
                            "nw": {
                                "x": 5821.9453,
                                "y": 4618.658
                            }
                        },
                        "position": {
                            "x": 5815.12,
                            "y": 4620.507
                        },
                        "rowIdx": 31,
                        "colIdx": 10,
                        "mapInfo": "107블록 32열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 429,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00032열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098648,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5815.2646,
                                "y": 4610.212
                            },
                            "se": {
                                "x": 5823.939,
                                "y": 4615.188
                            },
                            "sw": {
                                "x": 5820.241,
                                "y": 4601.538
                            },
                            "nw": {
                                "x": 5828.915,
                                "y": 4606.514
                            }
                        },
                        "position": {
                            "x": 5822.09,
                            "y": 4608.363
                        },
                        "rowIdx": 31,
                        "colIdx": 11,
                        "mapInfo": "107블록 32열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951063,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 430,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "32열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00032열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098651,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5757.745,
                                "y": 4738.617
                            },
                            "se": {
                                "x": 5766.419,
                                "y": 4743.593
                            },
                            "sw": {
                                "x": 5762.7207,
                                "y": 4729.943
                            },
                            "nw": {
                                "x": 5771.395,
                                "y": 4734.919
                            }
                        },
                        "position": {
                            "x": 5764.57,
                            "y": 4736.768
                        },
                        "rowIdx": 32,
                        "colIdx": 1,
                        "mapInfo": "107블록 33열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 433,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00033열00013번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098652,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5764.715,
                                "y": 4726.473
                            },
                            "se": {
                                "x": 5773.389,
                                "y": 4731.449
                            },
                            "sw": {
                                "x": 5769.691,
                                "y": 4717.799
                            },
                            "nw": {
                                "x": 5778.365,
                                "y": 4722.775
                            }
                        },
                        "position": {
                            "x": 5771.54,
                            "y": 4724.624
                        },
                        "rowIdx": 32,
                        "colIdx": 2,
                        "mapInfo": "107블록 33열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 434,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00033열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098653,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5771.675,
                                "y": 4714.329
                            },
                            "se": {
                                "x": 5780.349,
                                "y": 4719.305
                            },
                            "sw": {
                                "x": 5776.651,
                                "y": 4705.6553
                            },
                            "nw": {
                                "x": 5785.325,
                                "y": 4710.631
                            }
                        },
                        "position": {
                            "x": 5778.5,
                            "y": 4712.48
                        },
                        "rowIdx": 32,
                        "colIdx": 3,
                        "mapInfo": "107블록 33열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 435,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00033열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098654,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5778.645,
                                "y": 4702.185
                            },
                            "se": {
                                "x": 5787.319,
                                "y": 4707.161
                            },
                            "sw": {
                                "x": 5783.621,
                                "y": 4693.5107
                            },
                            "nw": {
                                "x": 5792.295,
                                "y": 4698.487
                            }
                        },
                        "position": {
                            "x": 5785.4697,
                            "y": 4700.336
                        },
                        "rowIdx": 32,
                        "colIdx": 4,
                        "mapInfo": "107블록 33열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 436,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00033열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098655,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5785.6147,
                                "y": 4690.041
                            },
                            "se": {
                                "x": 5794.289,
                                "y": 4695.017
                            },
                            "sw": {
                                "x": 5790.591,
                                "y": 4681.367
                            },
                            "nw": {
                                "x": 5799.265,
                                "y": 4686.343
                            }
                        },
                        "position": {
                            "x": 5792.44,
                            "y": 4688.192
                        },
                        "rowIdx": 32,
                        "colIdx": 5,
                        "mapInfo": "107블록 33열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 437,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00033열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098656,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5792.575,
                                "y": 4677.897
                            },
                            "se": {
                                "x": 5801.249,
                                "y": 4682.873
                            },
                            "sw": {
                                "x": 5797.551,
                                "y": 4669.223
                            },
                            "nw": {
                                "x": 5806.225,
                                "y": 4674.199
                            }
                        },
                        "position": {
                            "x": 5799.4,
                            "y": 4676.048
                        },
                        "rowIdx": 32,
                        "colIdx": 6,
                        "mapInfo": "107블록 33열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 438,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00033열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098657,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5799.545,
                                "y": 4665.753
                            },
                            "se": {
                                "x": 5808.2188,
                                "y": 4670.729
                            },
                            "sw": {
                                "x": 5804.521,
                                "y": 4657.079
                            },
                            "nw": {
                                "x": 5813.1953,
                                "y": 4662.055
                            }
                        },
                        "position": {
                            "x": 5806.37,
                            "y": 4663.904
                        },
                        "rowIdx": 32,
                        "colIdx": 7,
                        "mapInfo": "107블록 33열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 439,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00033열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098658,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5806.505,
                                "y": 4653.609
                            },
                            "se": {
                                "x": 5815.1787,
                                "y": 4658.585
                            },
                            "sw": {
                                "x": 5811.481,
                                "y": 4644.935
                            },
                            "nw": {
                                "x": 5820.1553,
                                "y": 4649.911
                            }
                        },
                        "position": {
                            "x": 5813.33,
                            "y": 4651.76
                        },
                        "rowIdx": 32,
                        "colIdx": 8,
                        "mapInfo": "107블록 33열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 440,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00033열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098659,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5813.475,
                                "y": 4641.466
                            },
                            "se": {
                                "x": 5822.149,
                                "y": 4646.442
                            },
                            "sw": {
                                "x": 5818.451,
                                "y": 4632.792
                            },
                            "nw": {
                                "x": 5827.125,
                                "y": 4637.768
                            }
                        },
                        "position": {
                            "x": 5820.3,
                            "y": 4639.617
                        },
                        "rowIdx": 32,
                        "colIdx": 9,
                        "mapInfo": "107블록 33열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 441,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00033열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098660,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5820.445,
                                "y": 4629.3223
                            },
                            "se": {
                                "x": 5829.119,
                                "y": 4634.298
                            },
                            "sw": {
                                "x": 5825.421,
                                "y": 4620.648
                            },
                            "nw": {
                                "x": 5834.095,
                                "y": 4625.624
                            }
                        },
                        "position": {
                            "x": 5827.27,
                            "y": 4627.473
                        },
                        "rowIdx": 32,
                        "colIdx": 10,
                        "mapInfo": "107블록 33열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 442,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00033열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098661,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5827.405,
                                "y": 4617.1777
                            },
                            "se": {
                                "x": 5836.079,
                                "y": 4622.154
                            },
                            "sw": {
                                "x": 5832.381,
                                "y": 4608.504
                            },
                            "nw": {
                                "x": 5841.055,
                                "y": 4613.48
                            }
                        },
                        "position": {
                            "x": 5834.23,
                            "y": 4615.329
                        },
                        "rowIdx": 32,
                        "colIdx": 11,
                        "mapInfo": "107블록 33열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951076,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 443,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "33열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00033열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098664,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5762.925,
                                "y": 4757.727
                            },
                            "se": {
                                "x": 5771.599,
                                "y": 4762.703
                            },
                            "sw": {
                                "x": 5767.901,
                                "y": 4749.0527
                            },
                            "nw": {
                                "x": 5776.575,
                                "y": 4754.029
                            }
                        },
                        "position": {
                            "x": 5769.75,
                            "y": 4755.878
                        },
                        "rowIdx": 33,
                        "colIdx": 0,
                        "mapInfo": "107블록 34열 14번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 446,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "14번"
                        ],
                        "sortMapInfo": "00107블록00034열00014번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098665,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5769.895,
                                "y": 4745.583
                            },
                            "se": {
                                "x": 5778.569,
                                "y": 4750.559
                            },
                            "sw": {
                                "x": 5774.871,
                                "y": 4736.909
                            },
                            "nw": {
                                "x": 5783.545,
                                "y": 4741.885
                            }
                        },
                        "position": {
                            "x": 5776.7197,
                            "y": 4743.734
                        },
                        "rowIdx": 33,
                        "colIdx": 1,
                        "mapInfo": "107블록 34열 13번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 447,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "13번"
                        ],
                        "sortMapInfo": "00107블록00034열00013번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098666,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5776.855,
                                "y": 4733.439
                            },
                            "se": {
                                "x": 5785.5293,
                                "y": 4738.415
                            },
                            "sw": {
                                "x": 5781.831,
                                "y": 4724.765
                            },
                            "nw": {
                                "x": 5790.505,
                                "y": 4729.741
                            }
                        },
                        "position": {
                            "x": 5783.68,
                            "y": 4731.59
                        },
                        "rowIdx": 33,
                        "colIdx": 2,
                        "mapInfo": "107블록 34열 12번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 448,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "12번"
                        ],
                        "sortMapInfo": "00107블록00034열00012번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098667,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5783.825,
                                "y": 4721.295
                            },
                            "se": {
                                "x": 5792.499,
                                "y": 4726.271
                            },
                            "sw": {
                                "x": 5788.801,
                                "y": 4712.621
                            },
                            "nw": {
                                "x": 5797.475,
                                "y": 4717.597
                            }
                        },
                        "position": {
                            "x": 5790.65,
                            "y": 4719.446
                        },
                        "rowIdx": 33,
                        "colIdx": 3,
                        "mapInfo": "107블록 34열 11번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 449,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "11번"
                        ],
                        "sortMapInfo": "00107블록00034열00011번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098668,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5790.785,
                                "y": 4709.151
                            },
                            "se": {
                                "x": 5799.459,
                                "y": 4714.127
                            },
                            "sw": {
                                "x": 5795.7607,
                                "y": 4700.477
                            },
                            "nw": {
                                "x": 5804.435,
                                "y": 4705.453
                            }
                        },
                        "position": {
                            "x": 5797.61,
                            "y": 4707.302
                        },
                        "rowIdx": 33,
                        "colIdx": 4,
                        "mapInfo": "107블록 34열 10번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 450,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "10번"
                        ],
                        "sortMapInfo": "00107블록00034열00010번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098669,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5797.755,
                                "y": 4697.007
                            },
                            "se": {
                                "x": 5806.4287,
                                "y": 4701.983
                            },
                            "sw": {
                                "x": 5802.731,
                                "y": 4688.333
                            },
                            "nw": {
                                "x": 5811.4053,
                                "y": 4693.309
                            }
                        },
                        "position": {
                            "x": 5804.58,
                            "y": 4695.158
                        },
                        "rowIdx": 33,
                        "colIdx": 5,
                        "mapInfo": "107블록 34열 9번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 451,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "9번"
                        ],
                        "sortMapInfo": "00107블록00034열00009번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098670,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5804.725,
                                "y": 4684.863
                            },
                            "se": {
                                "x": 5813.399,
                                "y": 4689.839
                            },
                            "sw": {
                                "x": 5809.701,
                                "y": 4676.189
                            },
                            "nw": {
                                "x": 5818.375,
                                "y": 4681.165
                            }
                        },
                        "position": {
                            "x": 5811.55,
                            "y": 4683.014
                        },
                        "rowIdx": 33,
                        "colIdx": 6,
                        "mapInfo": "107블록 34열 8번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 452,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "8번"
                        ],
                        "sortMapInfo": "00107블록00034열00008번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098671,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5811.685,
                                "y": 4672.7188
                            },
                            "se": {
                                "x": 5820.359,
                                "y": 4677.695
                            },
                            "sw": {
                                "x": 5816.661,
                                "y": 4664.045
                            },
                            "nw": {
                                "x": 5825.335,
                                "y": 4669.021
                            }
                        },
                        "position": {
                            "x": 5818.51,
                            "y": 4670.87
                        },
                        "rowIdx": 33,
                        "colIdx": 7,
                        "mapInfo": "107블록 34열 7번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 453,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "7번"
                        ],
                        "sortMapInfo": "00107블록00034열00007번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098672,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5818.655,
                                "y": 4660.575
                            },
                            "se": {
                                "x": 5827.329,
                                "y": 4665.551
                            },
                            "sw": {
                                "x": 5823.631,
                                "y": 4651.901
                            },
                            "nw": {
                                "x": 5832.305,
                                "y": 4656.877
                            }
                        },
                        "position": {
                            "x": 5825.48,
                            "y": 4658.726
                        },
                        "rowIdx": 33,
                        "colIdx": 8,
                        "mapInfo": "107블록 34열 6번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 454,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "6번"
                        ],
                        "sortMapInfo": "00107블록00034열00006번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098673,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5825.6147,
                                "y": 4648.432
                            },
                            "se": {
                                "x": 5834.289,
                                "y": 4653.408
                            },
                            "sw": {
                                "x": 5830.591,
                                "y": 4639.758
                            },
                            "nw": {
                                "x": 5839.265,
                                "y": 4644.734
                            }
                        },
                        "position": {
                            "x": 5832.44,
                            "y": 4646.583
                        },
                        "rowIdx": 33,
                        "colIdx": 9,
                        "mapInfo": "107블록 34열 5번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 455,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "5번"
                        ],
                        "sortMapInfo": "00107블록00034열00005번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098674,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5832.585,
                                "y": 4636.288
                            },
                            "se": {
                                "x": 5841.259,
                                "y": 4641.264
                            },
                            "sw": {
                                "x": 5837.561,
                                "y": 4627.6143
                            },
                            "nw": {
                                "x": 5846.2354,
                                "y": 4632.59
                            }
                        },
                        "position": {
                            "x": 5839.41,
                            "y": 4634.439
                        },
                        "rowIdx": 33,
                        "colIdx": 10,
                        "mapInfo": "107블록 34열 4번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 456,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "4번"
                        ],
                        "sortMapInfo": "00107블록00034열00004번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098675,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5839.5547,
                                "y": 4624.144
                            },
                            "se": {
                                "x": 5848.229,
                                "y": 4629.12
                            },
                            "sw": {
                                "x": 5844.5312,
                                "y": 4615.4697
                            },
                            "nw": {
                                "x": 5853.205,
                                "y": 4620.446
                            }
                        },
                        "position": {
                            "x": 5846.38,
                            "y": 4622.295
                        },
                        "rowIdx": 33,
                        "colIdx": 11,
                        "mapInfo": "107블록 34열 3번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 457,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "3번"
                        ],
                        "sortMapInfo": "00107블록00034열00003번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446098676,
                        "gradeId": 79343,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5846.5146,
                                "y": 4612.0
                            },
                            "se": {
                                "x": 5855.189,
                                "y": 4616.976
                            },
                            "sw": {
                                "x": 5851.491,
                                "y": 4603.326
                            },
                            "nw": {
                                "x": 5860.165,
                                "y": 4608.302
                            }
                        },
                        "position": {
                            "x": 5853.34,
                            "y": 4610.151
                        },
                        "rowIdx": 33,
                        "colIdx": 12,
                        "mapInfo": "107블록 34열 2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951090,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 458,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "34열",
                            "2번"
                        ],
                        "sortMapInfo": "00107블록00034열00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446109911,
                        "gradeId": 79350,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5842.945,
                                "y": 4674.507
                            },
                            "se": {
                                "x": 5851.619,
                                "y": 4679.483
                            },
                            "sw": {
                                "x": 5847.921,
                                "y": 4665.833
                            },
                            "nw": {
                                "x": 5856.595,
                                "y": 4670.809
                            }
                        },
                        "position": {
                            "x": 5849.77,
                            "y": 4672.658
                        },
                        "rowIdx": 35,
                        "colIdx": 8,
                        "mapInfo": "107블록 W16-2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951092,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 460,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "",
                            "W16-2번"
                        ],
                        "sortMapInfo": "00107블록W00016-00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446109912,
                        "gradeId": 79350,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5849.905,
                                "y": 4662.3643
                            },
                            "se": {
                                "x": 5858.579,
                                "y": 4667.34
                            },
                            "sw": {
                                "x": 5854.881,
                                "y": 4653.69
                            },
                            "nw": {
                                "x": 5863.555,
                                "y": 4658.666
                            }
                        },
                        "position": {
                            "x": 5856.73,
                            "y": 4660.515
                        },
                        "rowIdx": 35,
                        "colIdx": 9,
                        "mapInfo": "107블록 W16-1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951092,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 461,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "",
                            "W16-1번"
                        ],
                        "sortMapInfo": "00107블록W00016-00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446109913,
                        "gradeId": 79350,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5863.835,
                                "y": 4638.076
                            },
                            "se": {
                                "x": 5872.509,
                                "y": 4643.052
                            },
                            "sw": {
                                "x": 5868.811,
                                "y": 4629.402
                            },
                            "nw": {
                                "x": 5877.4854,
                                "y": 4634.378
                            }
                        },
                        "position": {
                            "x": 5870.66,
                            "y": 4636.227
                        },
                        "rowIdx": 35,
                        "colIdx": 11,
                        "mapInfo": "107블록 W15-2번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951094,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 462,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "",
                            "W15-2번"
                        ],
                        "sortMapInfo": "00107블록W00015-00002번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    },
                    {
                        "logicalSeatId": 1446109914,
                        "gradeId": 79350,
                        "allotmentCode": "TKL",
                        "cornerPoints": {
                            "ne": {
                                "x": 5870.8047,
                                "y": 4625.932
                            },
                            "se": {
                                "x": 5879.479,
                                "y": 4630.908
                            },
                            "sw": {
                                "x": 5875.7812,
                                "y": 4617.258
                            },
                            "nw": {
                                "x": 5884.455,
                                "y": 4622.234
                            }
                        },
                        "position": {
                            "x": 5877.63,
                            "y": 4624.083
                        },
                        "rowIdx": 35,
                        "colIdx": 12,
                        "mapInfo": "107블록 W15-1번",
                        "seatCount": 1,
                        "groupId": 0,
                        "linkedId": 6951094,
                        "gate": "2,3 GATE",
                        "blockId": 100699,
                        "orderNum": 463,
                        "attributes": [
                            "",
                            "",
                            "",
                            "107블록",
                            "",
                            "W15-1번"
                        ],
                        "sortMapInfo": "00107블록W00015-00001번",
                        "area": {
                            "virtualX": 22,
                            "virtualY": 18
                        },
                         
                        "sectionId": 26536
                    }
                ]
}
idx = 0
for key, value in json_data.items():
    for item in value:
        serializer = SeatSerializer(data=item)
        if serializer.is_valid():
            serializer.save()
        else:
            print("Validation error:", serializer.errors)
        print(idx)
        idx = idx + 1