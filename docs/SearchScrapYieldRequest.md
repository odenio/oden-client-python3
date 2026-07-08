# SearchScrapYieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ScrapYieldData**](ScrapYieldData.md) |  | [optional] 
**interval** | [**Interval**](Interval.md) |  | 

## Example

```python
from oden.models.search_scrap_yield_request import SearchScrapYieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchScrapYieldRequest from a JSON string
search_scrap_yield_request_instance = SearchScrapYieldRequest.from_json(json)
# print the JSON string representation of the object
print(SearchScrapYieldRequest.to_json())

# convert the object into a dict
search_scrap_yield_request_dict = search_scrap_yield_request_instance.to_dict()
# create an instance of SearchScrapYieldRequest from a dict
search_scrap_yield_request_from_dict = SearchScrapYieldRequest.from_dict(search_scrap_yield_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


