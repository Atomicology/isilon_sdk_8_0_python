# isi_sdk_8_0.LocalApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_time**](LocalApi.md#get_cluster_time) | **GET** /platform/3/local/cluster/time | 


# **get_cluster_time**
> ClusterTimeExtendedExtended get_cluster_time()



Get the current time on the local node.

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
api_instance = isi_sdk_8_0.LocalApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalApi->get_cluster_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterTimeExtendedExtended**](ClusterTimeExtendedExtended.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

