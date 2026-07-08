# OQLQuery

An object representing an OQL query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | 

## Example

```python
from oden.models.oql_query import OQLQuery

# TODO update the JSON string below
json = "{}"
# create an instance of OQLQuery from a JSON string
oql_query_instance = OQLQuery.from_json(json)
# print the JSON string representation of the object
print(OQLQuery.to_json())

# convert the object into a dict
oql_query_dict = oql_query_instance.to_dict()
# create an instance of OQLQuery from a dict
oql_query_from_dict = OQLQuery.from_dict(oql_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


