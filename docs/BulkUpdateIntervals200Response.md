# BulkUpdateIntervals200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_updated** | **int** |  | [optional] 
**updated_intervals** | [**List[Interval]**](Interval.md) |  | [optional] 
**num_failed** | **int** |  | [optional] 
**failed_intervals** | [**List[BulkUpdateIntervals200ResponseFailedIntervalsInner]**](BulkUpdateIntervals200ResponseFailedIntervalsInner.md) |  | [optional] 

## Example

```python
from oden.models.bulk_update_intervals200_response import BulkUpdateIntervals200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateIntervals200Response from a JSON string
bulk_update_intervals200_response_instance = BulkUpdateIntervals200Response.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateIntervals200Response.to_json())

# convert the object into a dict
bulk_update_intervals200_response_dict = bulk_update_intervals200_response_instance.to_dict()
# create an instance of BulkUpdateIntervals200Response from a dict
bulk_update_intervals200_response_from_dict = BulkUpdateIntervals200Response.from_dict(bulk_update_intervals200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


