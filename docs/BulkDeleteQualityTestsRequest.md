# BulkDeleteQualityTestsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[UUID]** |  | [optional] 
**line** | [**Line**](Line.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 

## Example

```python
from oden.models.bulk_delete_quality_tests_request import BulkDeleteQualityTestsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteQualityTestsRequest from a JSON string
bulk_delete_quality_tests_request_instance = BulkDeleteQualityTestsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteQualityTestsRequest.to_json())

# convert the object into a dict
bulk_delete_quality_tests_request_dict = bulk_delete_quality_tests_request_instance.to_dict()
# create an instance of BulkDeleteQualityTestsRequest from a dict
bulk_delete_quality_tests_request_from_dict = BulkDeleteQualityTestsRequest.from_dict(bulk_delete_quality_tests_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


