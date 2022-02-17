# we can simply our own module as
from Python_RoadMap.a_package import Converter_module
from Python_RoadMap.a_package.Converter_module import kg_to_lbs,lbs_to_kg
from Python_RoadMap.a_package.Converter_module import find_max as max
print(Converter_module.lbs_to_kg(70))
print(lbs_to_kg(70))
print(kg_to_lbs(70))
numbers=[2, 3, 4, 3, 5, 98]
print(max(numbers))