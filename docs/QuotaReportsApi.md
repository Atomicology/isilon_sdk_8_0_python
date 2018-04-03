# isi_sdk_8_0.QuotaReportsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_about**](QuotaReportsApi.md#get_report_about) | **GET** /platform/1/quota/reports/{Rid}/about | 


# **get_report_about**
> ReportAbout get_report_about(rid)



Retrieve report meta-data information.

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
api_instance = isi_sdk_8_0.QuotaReportsApi(isi_sdk_8_0.ApiClient(configuration))
rid = 'rid_example' # str | 

try:
    api_response = api_instance.get_report_about(rid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaReportsApi->get_report_about: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**|  | 

### Return type

[**ReportAbout**](ReportAbout.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

