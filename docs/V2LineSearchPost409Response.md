# V2LineSearchPost409Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_name** | **str** |  | 
**num_matches** | **int** |  | 
**error** | **str** |  | 
**retryable** | **bool** |  | 

## Example

```python
from oden.models.v2_line_search_post409_response import V2LineSearchPost409Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2LineSearchPost409Response from a JSON string
v2_line_search_post409_response_instance = V2LineSearchPost409Response.from_json(json)
# print the JSON string representation of the object
print(V2LineSearchPost409Response.to_json())

# convert the object into a dict
v2_line_search_post409_response_dict = v2_line_search_post409_response_instance.to_dict()
# create an instance of V2LineSearchPost409Response from a dict
v2_line_search_post409_response_from_dict = V2LineSearchPost409Response.from_dict(v2_line_search_post409_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


