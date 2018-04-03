# isi_sdk_8_0.FsaApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_fsa_result**](FsaApi.md#delete_fsa_result) | **DELETE** /platform/3/fsa/results/{FsaResultId} | 
[**delete_fsa_settings**](FsaApi.md#delete_fsa_settings) | **DELETE** /platform/1/fsa/settings | 
[**get_fsa_result**](FsaApi.md#get_fsa_result) | **GET** /platform/3/fsa/results/{FsaResultId} | 
[**get_fsa_results**](FsaApi.md#get_fsa_results) | **GET** /platform/3/fsa/results | 
[**get_fsa_settings**](FsaApi.md#get_fsa_settings) | **GET** /platform/1/fsa/settings | 
[**update_fsa_result**](FsaApi.md#update_fsa_result) | **PUT** /platform/3/fsa/results/{FsaResultId} | 
[**update_fsa_settings**](FsaApi.md#update_fsa_settings) | **PUT** /platform/1/fsa/settings | 


# **delete_fsa_result**
> delete_fsa_result(fsa_result_id)



Delete the result set.

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
api_instance = isi_sdk_8_0.FsaApi(isi_sdk_8_0.ApiClient(configuration))
fsa_result_id = 'fsa_result_id_example' # str | Delete the result set.

try:
    api_instance.delete_fsa_result(fsa_result_id)
except ApiException as e:
    print("Exception when calling FsaApi->delete_fsa_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fsa_result_id** | **str**| Delete the result set. | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fsa_settings**
> delete_fsa_settings()



Revert all settings to their defaults.

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
api_instance = isi_sdk_8_0.FsaApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_instance.delete_fsa_settings()
except ApiException as e:
    print("Exception when calling FsaApi->delete_fsa_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fsa_result**
> FsaResults get_fsa_result(fsa_result_id)



Retrieve result set information.

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
api_instance = isi_sdk_8_0.FsaApi(isi_sdk_8_0.ApiClient(configuration))
fsa_result_id = 'fsa_result_id_example' # str | Retrieve result set information.

try:
    api_response = api_instance.get_fsa_result(fsa_result_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaApi->get_fsa_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fsa_result_id** | **str**| Retrieve result set information. | 

### Return type

[**FsaResults**](FsaResults.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fsa_results**
> FsaResultsExtended get_fsa_results()



List all results.

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
api_instance = isi_sdk_8_0.FsaApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_fsa_results()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaApi->get_fsa_results: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FsaResultsExtended**](FsaResultsExtended.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fsa_settings**
> FsaSettings get_fsa_settings()



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
api_instance = isi_sdk_8_0.FsaApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_fsa_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaApi->get_fsa_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FsaSettings**](FsaSettings.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fsa_result**
> update_fsa_result(fsa_result, fsa_result_id)



Modify result set. Only the pinned property can be changed at this time.

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
api_instance = isi_sdk_8_0.FsaApi(isi_sdk_8_0.ApiClient(configuration))
fsa_result = isi_sdk_8_0.FsaResult() # FsaResult | 
fsa_result_id = 'fsa_result_id_example' # str | Modify result set. Only the pinned property can be changed at this time.

try:
    api_instance.update_fsa_result(fsa_result, fsa_result_id)
except ApiException as e:
    print("Exception when calling FsaApi->update_fsa_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fsa_result** | [**FsaResult**](FsaResult.md)|  | 
 **fsa_result_id** | **str**| Modify result set. Only the pinned property can be changed at this time. | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fsa_settings**
> update_fsa_settings(fsa_settings)



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
api_instance = isi_sdk_8_0.FsaApi(isi_sdk_8_0.ApiClient(configuration))
fsa_settings = isi_sdk_8_0.FsaSettingsSettings() # FsaSettingsSettings | 

try:
    api_instance.update_fsa_settings(fsa_settings)
except ApiException as e:
    print("Exception when calling FsaApi->update_fsa_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fsa_settings** | [**FsaSettingsSettings**](FsaSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

