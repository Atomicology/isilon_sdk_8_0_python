# isi_sdk_8_0.ZonesSummaryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_zones_summary**](ZonesSummaryApi.md#get_zones_summary) | **GET** /platform/1/zones-summary | 
[**get_zones_summary_zone**](ZonesSummaryApi.md#get_zones_summary_zone) | **GET** /platform/1/zones-summary/{ZonesSummaryZone} | 


# **get_zones_summary**
> ZonesSummaryExtended get_zones_summary(groupnet=groupnet)



Retrieve access zone summary information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure API key authorization: sessionAuth
configuration = isi_sdk_8_0.Configuration()
configuration.api_key['cookie'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# create an instance of the API class
api_instance = isi_sdk_8_0.ZonesSummaryApi(isi_sdk_8_0.ApiClient(configuration))
groupnet = 'groupnet_example' # str | Name of groupnet in which to list zones. (optional)

try:
    api_response = api_instance.get_zones_summary(groupnet=groupnet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesSummaryApi->get_zones_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet** | **str**| Name of groupnet in which to list zones. | [optional] 

### Return type

[**ZonesSummaryExtended**](ZonesSummaryExtended.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zones_summary_zone**
> ZonesSummary get_zones_summary_zone(zones_summary_zone)



Retrieve non-privileged access zone information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure API key authorization: sessionAuth
configuration = isi_sdk_8_0.Configuration()
configuration.api_key['cookie'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# create an instance of the API class
api_instance = isi_sdk_8_0.ZonesSummaryApi(isi_sdk_8_0.ApiClient(configuration))
zones_summary_zone = 56 # int | Retrieve non-privileged access zone information.

try:
    api_response = api_instance.get_zones_summary_zone(zones_summary_zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZonesSummaryApi->get_zones_summary_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zones_summary_zone** | **int**| Retrieve non-privileged access zone information. | 

### Return type

[**ZonesSummary**](ZonesSummary.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

