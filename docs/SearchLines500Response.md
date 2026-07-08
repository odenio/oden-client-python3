# SearchLines500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**retryable** | **bool** |  | 
**id** | **UUID** |  | 

## Example

```python
from oden.models.search_lines500_response import SearchLines500Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchLines500Response from a JSON string
search_lines500_response_instance = SearchLines500Response.from_json(json)
# print the JSON string representation of the object
print(SearchLines500Response.to_json())

# convert the object into a dict
search_lines500_response_dict = search_lines500_response_instance.to_dict()
# create an instance of SearchLines500Response from a dict
search_lines500_response_from_dict = SearchLines500Response.from_dict(search_lines500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


