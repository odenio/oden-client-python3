# ScrapYieldSchema

Scrap yield schema represents a factory's scrap/yield data ingestion configuration. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**factory** | [**Factory**](Factory.md) |  | [optional] 
**scrap_conversion_factor** | **float** |  | [optional] 
**scrap_unit** | [**Unit**](Unit.md) |  | [optional] 
**yield_conversion_factor** | **float** |  | [optional] 
**yield_unit** | [**Unit**](Unit.md) |  | [optional] 

## Example

```python
from oden.models.scrap_yield_schema import ScrapYieldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ScrapYieldSchema from a JSON string
scrap_yield_schema_instance = ScrapYieldSchema.from_json(json)
# print the JSON string representation of the object
print(ScrapYieldSchema.to_json())

# convert the object into a dict
scrap_yield_schema_dict = scrap_yield_schema_instance.to_dict()
# create an instance of ScrapYieldSchema from a dict
scrap_yield_schema_from_dict = ScrapYieldSchema.from_dict(scrap_yield_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


