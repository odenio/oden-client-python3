# IntervalType

An object representing a interval type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**factory** | [**Factory**](Factory.md) |  | [optional] 
**name** | **str** |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] [default to Match.UNIQUE]

## Example

```python
from oden.models.interval_type import IntervalType

# TODO update the JSON string below
json = "{}"
# create an instance of IntervalType from a JSON string
interval_type_instance = IntervalType.from_json(json)
# print the JSON string representation of the object
print(IntervalType.to_json())

# convert the object into a dict
interval_type_dict = interval_type_instance.to_dict()
# create an instance of IntervalType from a dict
interval_type_from_dict = IntervalType.from_dict(interval_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


