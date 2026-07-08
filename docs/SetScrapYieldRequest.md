# SetScrapYieldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ScrapYieldData**](ScrapYieldData.md) |  | 
**interval** | [**Interval**](Interval.md) |  | 

## Example

```python
from oden.models.set_scrap_yield_request import SetScrapYieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetScrapYieldRequest from a JSON string
set_scrap_yield_request_instance = SetScrapYieldRequest.from_json(json)
# print the JSON string representation of the object
print(SetScrapYieldRequest.to_json())

# convert the object into a dict
set_scrap_yield_request_dict = set_scrap_yield_request_instance.to_dict()
# create an instance of SetScrapYieldRequest from a dict
set_scrap_yield_request_from_dict = SetScrapYieldRequest.from_dict(set_scrap_yield_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


