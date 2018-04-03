# isi_sdk_8_0.FileFilterApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file_filter_settings**](FileFilterApi.md#get_file_filter_settings) | **GET** /platform/3/file-filter/settings | 
[**update_file_filter_settings**](FileFilterApi.md#update_file_filter_settings) | **PUT** /platform/3/file-filter/settings | 


# **get_file_filter_settings**
> FileFilterSettings get_file_filter_settings(zone=zone)



View File Filtering settings of an access zone

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
api_instance = isi_sdk_8_0.FileFilterApi(isi_sdk_8_0.ApiClient(configuration))
zone = 'zone_example' # str | Specifies the access zones in which these settings apply. (optional)

try:
    api_response = api_instance.get_file_filter_settings(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileFilterApi->get_file_filter_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Specifies the access zones in which these settings apply. | [optional] 

### Return type

[**FileFilterSettings**](FileFilterSettings.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_filter_settings**
> update_file_filter_settings(file_filter_settings, zone=zone)



Modify one or more File Filtering settings for an access zone

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
api_instance = isi_sdk_8_0.FileFilterApi(isi_sdk_8_0.ApiClient(configuration))
file_filter_settings = isi_sdk_8_0.FileFilterSettingsExtended() # FileFilterSettingsExtended | 
zone = 'zone_example' # str | Specifies the access zones in which these settings apply. (optional)

try:
    api_instance.update_file_filter_settings(file_filter_settings, zone=zone)
except ApiException as e:
    print("Exception when calling FileFilterApi->update_file_filter_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_filter_settings** | [**FileFilterSettingsExtended**](FileFilterSettingsExtended.md)|  | 
 **zone** | **str**| Specifies the access zones in which these settings apply. | [optional] 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

