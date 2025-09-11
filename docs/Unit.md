# Unit

A Unit describes a unit of measurement. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**symbol** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**kind_of_quantity** | **str** |  | [optional] 

## Example

```python
from oden.models.unit import Unit

# TODO update the JSON string below
json = "{}"
# create an instance of Unit from a JSON string
unit_instance = Unit.from_json(json)
# print the JSON string representation of the object
print(Unit.to_json())

# convert the object into a dict
unit_dict = unit_instance.to_dict()
# create an instance of Unit from a dict
unit_from_dict = Unit.from_dict(unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


