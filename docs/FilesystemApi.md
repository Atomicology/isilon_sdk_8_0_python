# isi_sdk_8_0.FilesystemApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings_access_time**](FilesystemApi.md#get_settings_access_time) | **GET** /platform/1/filesystem/settings/access-time | 
[**get_settings_character_encodings**](FilesystemApi.md#get_settings_character_encodings) | **GET** /platform/1/filesystem/settings/character-encodings | 
[**update_settings_access_time**](FilesystemApi.md#update_settings_access_time) | **PUT** /platform/1/filesystem/settings/access-time | 
[**update_settings_character_encodings**](FilesystemApi.md#update_settings_character_encodings) | **PUT** /platform/1/filesystem/settings/character-encodings | 


# **get_settings_access_time**
> SettingsAccessTime get_settings_access_time()



Retrieve settings for access time.

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
api_instance = isi_sdk_8_0.FilesystemApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_settings_access_time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemApi->get_settings_access_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsAccessTime**](SettingsAccessTime.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_character_encodings**
> SettingsCharacterEncodings get_settings_character_encodings()



Retrieve current cluster character encoding settings.

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
api_instance = isi_sdk_8_0.FilesystemApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_settings_character_encodings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemApi->get_settings_character_encodings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsCharacterEncodings**](SettingsCharacterEncodings.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_access_time**
> update_settings_access_time(settings_access_time)



Set settings for access time.

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
api_instance = isi_sdk_8_0.FilesystemApi(isi_sdk_8_0.ApiClient(configuration))
settings_access_time = isi_sdk_8_0.SettingsAccessTimeExtended() # SettingsAccessTimeExtended | 

try:
    api_instance.update_settings_access_time(settings_access_time)
except ApiException as e:
    print("Exception when calling FilesystemApi->update_settings_access_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_access_time** | [**SettingsAccessTimeExtended**](SettingsAccessTimeExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_character_encodings**
> update_settings_character_encodings(settings_character_encodings)



Set current character encoding.

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
api_instance = isi_sdk_8_0.FilesystemApi(isi_sdk_8_0.ApiClient(configuration))
settings_character_encodings = isi_sdk_8_0.SettingsCharacterEncodingsExtended() # SettingsCharacterEncodingsExtended | 

try:
    api_instance.update_settings_character_encodings(settings_character_encodings)
except ApiException as e:
    print("Exception when calling FilesystemApi->update_settings_character_encodings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_character_encodings** | [**SettingsCharacterEncodingsExtended**](SettingsCharacterEncodingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

