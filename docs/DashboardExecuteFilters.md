# DashboardExecuteFilters

Optional filter overrides applied to every module. Every field is optional; omitting one means \"no override on that dimension\". 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | [**List[DashboardExecuteFiltersLinesInner]**](DashboardExecuteFiltersLinesInner.md) | Lines to restrict to. Each entry must supply &#x60;id&#x60;, &#x60;name&#x60;, or both; entries that supply neither are rejected. Other Line fields (factory, secondary_name, match) are not used here and are intentionally omitted so generated clients don&#39;t suggest them as inputs.  | [optional] 
**shifts** | **List[int]** |  | [optional] 
**product_ids** | **List[UUID]** |  | [optional] 
**product_attribute_value_ids** | **List[UUID]** |  | [optional] 
**scrap_categories** | **List[UUID]** |  | [optional] 
**states** | [**DashboardExecuteFiltersStates**](DashboardExecuteFiltersStates.md) |  | [optional] 
**custom_intervals** | [**List[DashboardExecuteFiltersCustomIntervalsInner]**](DashboardExecuteFiltersCustomIntervalsInner.md) |  | [optional] 

## Example

```python
from oden.models.dashboard_execute_filters import DashboardExecuteFilters

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardExecuteFilters from a JSON string
dashboard_execute_filters_instance = DashboardExecuteFilters.from_json(json)
# print the JSON string representation of the object
print(DashboardExecuteFilters.to_json())

# convert the object into a dict
dashboard_execute_filters_dict = dashboard_execute_filters_instance.to_dict()
# create an instance of DashboardExecuteFilters from a dict
dashboard_execute_filters_from_dict = DashboardExecuteFilters.from_dict(dashboard_execute_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


