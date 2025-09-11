# QualityTest

An object representing a QA test for a line for a particular run or batch interval. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**raw_data** | **object** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**interval** | [**Interval**](Interval.md) |  | [optional] 
**quality_schema** | [**QualitySchema**](QualitySchema.md) |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] [default to Match.UNIQUE]

## Example

```python
from oden.models.quality_test import QualityTest

# TODO update the JSON string below
json = "{}"
# create an instance of QualityTest from a JSON string
quality_test_instance = QualityTest.from_json(json)
# print the JSON string representation of the object
print(QualityTest.to_json())

# convert the object into a dict
quality_test_dict = quality_test_instance.to_dict()
# create an instance of QualityTest from a dict
quality_test_from_dict = QualityTest.from_dict(quality_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


