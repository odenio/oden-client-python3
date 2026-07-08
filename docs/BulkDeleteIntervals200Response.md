# BulkDeleteIntervals200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_deleted** | **int** |  | [optional] 
**failed_intervals** | **List[str]** |  | [optional] 

## Example

```python
from oden.models.bulk_delete_intervals200_response import BulkDeleteIntervals200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteIntervals200Response from a JSON string
bulk_delete_intervals200_response_instance = BulkDeleteIntervals200Response.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteIntervals200Response.to_json())

# convert the object into a dict
bulk_delete_intervals200_response_dict = bulk_delete_intervals200_response_instance.to_dict()
# create an instance of BulkDeleteIntervals200Response from a dict
bulk_delete_intervals200_response_from_dict = BulkDeleteIntervals200Response.from_dict(bulk_delete_intervals200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


