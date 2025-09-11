# Target

An object representing a performance target for a line, product, and metric group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_group** | [**MetricGroup**](MetricGroup.md) |  | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**line** | [**Line**](Line.md) |  | [optional] 
**target_value** | **float** |  | [optional] 
**lsl** | **float** |  | [optional] 
**usl** | **float** |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] [default to Match.UNIQUE]

## Example

```python
from oden.models.target import Target

# TODO update the JSON string below
json = "{}"
# create an instance of Target from a JSON string
target_instance = Target.from_json(json)
# print the JSON string representation of the object
print(Target.to_json())

# convert the object into a dict
target_dict = target_instance.to_dict()
# create an instance of Target from a dict
target_from_dict = Target.from_dict(target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


