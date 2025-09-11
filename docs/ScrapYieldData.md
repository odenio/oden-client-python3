# ScrapYieldData

An object representing scrap and yield data for a line for a particular run or batch interval. Data can be sent unstructured in the `raw_data` field as long as we have a scrap/yield schema for the factory. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_data** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**var_schema** | [**ScrapYieldSchema**](ScrapYieldSchema.md) |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] [default to Match.UNIQUE]

## Example

```python
from oden.models.scrap_yield_data import ScrapYieldData

# TODO update the JSON string below
json = "{}"
# create an instance of ScrapYieldData from a JSON string
scrap_yield_data_instance = ScrapYieldData.from_json(json)
# print the JSON string representation of the object
print(ScrapYieldData.to_json())

# convert the object into a dict
scrap_yield_data_dict = scrap_yield_data_instance.to_dict()
# create an instance of ScrapYieldData from a dict
scrap_yield_data_from_dict = ScrapYieldData.from_dict(scrap_yield_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


