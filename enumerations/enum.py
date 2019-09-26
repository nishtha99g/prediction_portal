 #all enums
from enum import Enum


class BloodGroup(Enum):
    OM = "O-Minus"
    OP = "O-Positive"
    AM = "A-Minus"
    AP = "A-Positive"
    BM = "B-Minus"
    ABM = "AB-Minus"
    ABP = "AB-Positive"
    BP = "B-Positive"


class Gender(Enum):
    M = "Male"
    F = "Female"
    OT = "Other"


class Category(Enum):
    GEN = "General"
    OBC = "Other Backward Class"
    SC = "Scheduled Caste"
    ST = "Scheduled Tribe"
