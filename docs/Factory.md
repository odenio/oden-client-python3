# Factory

An entity representing a factory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**secondary_name** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] [default to Match.UNIQUE]

## Example

```python
from oden.models.factory import Factory

# TODO update the JSON string below
json = "{}"
# create an instance of Factory from a JSON string
factory_instance = Factory.from_json(json)
# print the JSON string representation of the object
print(Factory.to_json())

# convert the object into a dict
factory_dict = factory_instance.to_dict()
# create an instance of Factory from a dict
factory_from_dict = Factory.from_dict(factory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


