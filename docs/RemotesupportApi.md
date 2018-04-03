# isi_sdk_8_0.RemotesupportApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_remotesupport_connectemc**](RemotesupportApi.md#get_remotesupport_connectemc) | **GET** /platform/1/remotesupport/connectemc | 
[**update_remotesupport_connectemc**](RemotesupportApi.md#update_remotesupport_connectemc) | **PUT** /platform/1/remotesupport/connectemc | 


# **get_remotesupport_connectemc**
> RemotesupportConnectemc get_remotesupport_connectemc()



List all settings.

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
api_instance = isi_sdk_8_0.RemotesupportApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_remotesupport_connectemc()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemotesupportApi->get_remotesupport_connectemc: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RemotesupportConnectemc**](RemotesupportConnectemc.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_remotesupport_connectemc**
> update_remotesupport_connectemc(remotesupport_connectemc)



Modify one or more settings.

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
api_instance = isi_sdk_8_0.RemotesupportApi(isi_sdk_8_0.ApiClient(configuration))
remotesupport_connectemc = isi_sdk_8_0.RemotesupportConnectemcConnectemc() # RemotesupportConnectemcConnectemc | 

try:
    api_instance.update_remotesupport_connectemc(remotesupport_connectemc)
except ApiException as e:
    print("Exception when calling RemotesupportApi->update_remotesupport_connectemc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remotesupport_connectemc** | [**RemotesupportConnectemcConnectemc**](RemotesupportConnectemcConnectemc.md)|  | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

