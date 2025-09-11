# V2QualityTestsDeletePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 
**line** | [**Line**](Line.md) |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 

## Example

```python
from oden.models.v2_quality_tests_delete_post_request import V2QualityTestsDeletePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2QualityTestsDeletePostRequest from a JSON string
v2_quality_tests_delete_post_request_instance = V2QualityTestsDeletePostRequest.from_json(json)
# print the JSON string representation of the object
print(V2QualityTestsDeletePostRequest.to_json())

# convert the object into a dict
v2_quality_tests_delete_post_request_dict = v2_quality_tests_delete_post_request_instance.to_dict()
# create an instance of V2QualityTestsDeletePostRequest from a dict
v2_quality_tests_delete_post_request_from_dict = V2QualityTestsDeletePostRequest.from_dict(v2_quality_tests_delete_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


