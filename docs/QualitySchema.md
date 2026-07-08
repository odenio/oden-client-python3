# QualitySchema

A schema for quality tests. Note: the id is currently implemented as a string, but that string should be a stringified integer. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**factory** | [**Factory**](Factory.md) |  | [optional] 
**var_schema** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] [default to Match.UNIQUE]

## Example

```python
from oden.models.quality_schema import QualitySchema

# TODO update the JSON string below
json = "{}"
# create an instance of QualitySchema from a JSON string
quality_schema_instance = QualitySchema.from_json(json)
# print the JSON string representation of the object
print(QualitySchema.to_json())

# convert the object into a dict
quality_schema_dict = quality_schema_instance.to_dict()
# create an instance of QualitySchema from a dict
quality_schema_from_dict = QualitySchema.from_dict(quality_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


