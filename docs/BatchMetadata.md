# BatchMetadata

Metadata associated with a batch interval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_type** | **str** |  | [optional] [readonly] 
**run** | [**Interval**](Interval.md) |  | [optional] 

## Example

```python
from oden.models.batch_metadata import BatchMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of BatchMetadata from a JSON string
batch_metadata_instance = BatchMetadata.from_json(json)
# print the JSON string representation of the object
print(BatchMetadata.to_json())

# convert the object into a dict
batch_metadata_dict = batch_metadata_instance.to_dict()
# create an instance of BatchMetadata from a dict
batch_metadata_from_dict = BatchMetadata.from_dict(batch_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


