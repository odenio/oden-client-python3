# DashboardExecuteFiltersStates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_types** | **List[str]** |  | [optional] 
**state_category_and_reasons** | [**List[DashboardExecuteFiltersStatesStateCategoryAndReasonsInner]**](DashboardExecuteFiltersStatesStateCategoryAndReasonsInner.md) |  | [optional] 

## Example

```python
from oden.models.dashboard_execute_filters_states import DashboardExecuteFiltersStates

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardExecuteFiltersStates from a JSON string
dashboard_execute_filters_states_instance = DashboardExecuteFiltersStates.from_json(json)
# print the JSON string representation of the object
print(DashboardExecuteFiltersStates.to_json())

# convert the object into a dict
dashboard_execute_filters_states_dict = dashboard_execute_filters_states_instance.to_dict()
# create an instance of DashboardExecuteFiltersStates from a dict
dashboard_execute_filters_states_from_dict = DashboardExecuteFiltersStates.from_dict(dashboard_execute_filters_states_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


