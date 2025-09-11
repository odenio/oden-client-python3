# V2ScrapYieldSearchPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ScrapYieldData**](ScrapYieldData.md) |  | [optional] 
**interval** | [**Interval**](Interval.md) |  | 

## Example

```python
from oden.models.v2_scrap_yield_search_post_request import V2ScrapYieldSearchPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2ScrapYieldSearchPostRequest from a JSON string
v2_scrap_yield_search_post_request_instance = V2ScrapYieldSearchPostRequest.from_json(json)
# print the JSON string representation of the object
print(V2ScrapYieldSearchPostRequest.to_json())

# convert the object into a dict
v2_scrap_yield_search_post_request_dict = v2_scrap_yield_search_post_request_instance.to_dict()
# create an instance of V2ScrapYieldSearchPostRequest from a dict
v2_scrap_yield_search_post_request_from_dict = V2ScrapYieldSearchPostRequest.from_dict(v2_scrap_yield_search_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


