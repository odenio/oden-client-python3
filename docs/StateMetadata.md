# StateMetadata

Metadata associated with a state interval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_type** | **str** |  | [optional] [readonly] 
**reason** | [**StateReason**](StateReason.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**category** | [**StateCategory**](StateCategory.md) |  | [optional] 

## Example

```python
from oden.models.state_metadata import StateMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of StateMetadata from a JSON string
state_metadata_instance = StateMetadata.from_json(json)
# print the JSON string representation of the object
print(StateMetadata.to_json())

# convert the object into a dict
state_metadata_dict = state_metadata_instance.to_dict()
# create an instance of StateMetadata from a dict
state_metadata_from_dict = StateMetadata.from_dict(state_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


