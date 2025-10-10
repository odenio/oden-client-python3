# RunMetadata

Metadata associated with a run interval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_type** | **str** |  | [optional] [readonly] 
**product** | [**Product**](Product.md) |  | [optional] 
**target** | [**Target**](Target.md) |  | [optional] 

## Example

```python
from oden.models.run_metadata import RunMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RunMetadata from a JSON string
run_metadata_instance = RunMetadata.from_json(json)
# print the JSON string representation of the object
print(RunMetadata.to_json())

# convert the object into a dict
run_metadata_dict = run_metadata_instance.to_dict()
# create an instance of RunMetadata from a dict
run_metadata_from_dict = RunMetadata.from_dict(run_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


