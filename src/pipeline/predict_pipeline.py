import sys
import pandas as pd
from dataclasses import dataclass
from src.exception import CustomException
from src.utils import load_object

@dataclass
class PredicPipeline:
    def __init__(self):
        pass
    
class CustomData:
    def __init__(self,
                gender: str,
                race_enthnicity: int,
                parental_level_of_education,
                lunch:int,
                test_preparation_course: int,
                reading_score : str,
                writing_score : str,
                 )
