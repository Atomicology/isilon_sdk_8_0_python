# isi_sdk_8_0.StoragepoolApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_compatibilities_class_active_item**](StoragepoolApi.md#create_compatibilities_class_active_item) | **POST** /platform/1/storagepool/compatibilities/class/active | 
[**create_compatibilities_ssd_active_item**](StoragepoolApi.md#create_compatibilities_ssd_active_item) | **POST** /platform/3/storagepool/compatibilities/ssd/active | 
[**create_storagepool_nodepool**](StoragepoolApi.md#create_storagepool_nodepool) | **POST** /platform/3/storagepool/nodepools | 
[**create_storagepool_tier**](StoragepoolApi.md#create_storagepool_tier) | **POST** /platform/1/storagepool/tiers | 
[**delete_compatibilities_class_active_by_id**](StoragepoolApi.md#delete_compatibilities_class_active_by_id) | **DELETE** /platform/1/storagepool/compatibilities/class/active/{CompatibilitiesClassActiveId} | 
[**delete_compatibilities_ssd_active_by_id**](StoragepoolApi.md#delete_compatibilities_ssd_active_by_id) | **DELETE** /platform/3/storagepool/compatibilities/ssd/active/{CompatibilitiesSsdActiveId} | 
[**delete_storagepool_nodepool**](StoragepoolApi.md#delete_storagepool_nodepool) | **DELETE** /platform/3/storagepool/nodepools/{StoragepoolNodepoolId} | 
[**delete_storagepool_tier**](StoragepoolApi.md#delete_storagepool_tier) | **DELETE** /platform/1/storagepool/tiers/{StoragepoolTierId} | 
[**delete_storagepool_tiers**](StoragepoolApi.md#delete_storagepool_tiers) | **DELETE** /platform/1/storagepool/tiers | 
[**get_compatibilities_class_active_by_id**](StoragepoolApi.md#get_compatibilities_class_active_by_id) | **GET** /platform/1/storagepool/compatibilities/class/active/{CompatibilitiesClassActiveId} | 
[**get_compatibilities_class_available**](StoragepoolApi.md#get_compatibilities_class_available) | **GET** /platform/1/storagepool/compatibilities/class/available | 
[**get_compatibilities_ssd_active_by_id**](StoragepoolApi.md#get_compatibilities_ssd_active_by_id) | **GET** /platform/3/storagepool/compatibilities/ssd/active/{CompatibilitiesSsdActiveId} | 
[**get_compatibilities_ssd_available**](StoragepoolApi.md#get_compatibilities_ssd_available) | **GET** /platform/1/storagepool/compatibilities/ssd/available | 
[**get_storagepool_nodepool**](StoragepoolApi.md#get_storagepool_nodepool) | **GET** /platform/3/storagepool/nodepools/{StoragepoolNodepoolId} | 
[**get_storagepool_settings**](StoragepoolApi.md#get_storagepool_settings) | **GET** /platform/1/storagepool/settings | 
[**get_storagepool_status**](StoragepoolApi.md#get_storagepool_status) | **GET** /platform/1/storagepool/status | 
[**get_storagepool_storagepools**](StoragepoolApi.md#get_storagepool_storagepools) | **GET** /platform/3/storagepool/storagepools | 
[**get_storagepool_suggested_protection_nid**](StoragepoolApi.md#get_storagepool_suggested_protection_nid) | **GET** /platform/3/storagepool/suggested-protection/{StoragepoolSuggestedProtectionNid} | 
[**get_storagepool_tier**](StoragepoolApi.md#get_storagepool_tier) | **GET** /platform/1/storagepool/tiers/{StoragepoolTierId} | 
[**get_storagepool_unprovisioned**](StoragepoolApi.md#get_storagepool_unprovisioned) | **GET** /platform/1/storagepool/unprovisioned | 
[**list_compatibilities_class_active**](StoragepoolApi.md#list_compatibilities_class_active) | **GET** /platform/1/storagepool/compatibilities/class/active | 
[**list_compatibilities_ssd_active**](StoragepoolApi.md#list_compatibilities_ssd_active) | **GET** /platform/3/storagepool/compatibilities/ssd/active | 
[**list_storagepool_nodepools**](StoragepoolApi.md#list_storagepool_nodepools) | **GET** /platform/3/storagepool/nodepools | 
[**list_storagepool_tiers**](StoragepoolApi.md#list_storagepool_tiers) | **GET** /platform/1/storagepool/tiers | 
[**update_compatibilities_ssd_active_by_id**](StoragepoolApi.md#update_compatibilities_ssd_active_by_id) | **PUT** /platform/3/storagepool/compatibilities/ssd/active/{CompatibilitiesSsdActiveId} | 
[**update_storagepool_nodepool**](StoragepoolApi.md#update_storagepool_nodepool) | **PUT** /platform/3/storagepool/nodepools/{StoragepoolNodepoolId} | 
[**update_storagepool_settings**](StoragepoolApi.md#update_storagepool_settings) | **PUT** /platform/1/storagepool/settings | 
[**update_storagepool_tier**](StoragepoolApi.md#update_storagepool_tier) | **PUT** /platform/1/storagepool/tiers/{StoragepoolTierId} | 


# **create_compatibilities_class_active_item**
> CreateCompatibilitiesClassActiveItemResponse create_compatibilities_class_active_item(compatibilities_class_active_item)



Create a new compatibility

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
compatibilities_class_active_item = isi_sdk_8_0.CompatibilitiesClassActiveItem() # CompatibilitiesClassActiveItem | 

try:
    api_response = api_instance.create_compatibilities_class_active_item(compatibilities_class_active_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->create_compatibilities_class_active_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compatibilities_class_active_item** | [**CompatibilitiesClassActiveItem**](CompatibilitiesClassActiveItem.md)|  | 

### Return type

[**CreateCompatibilitiesClassActiveItemResponse**](CreateCompatibilitiesClassActiveItemResponse.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_compatibilities_ssd_active_item**
> CreateCompatibilitiesClassActiveItemResponse create_compatibilities_ssd_active_item(compatibilities_ssd_active_item)



Create a new ssd compatibility

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
compatibilities_ssd_active_item = isi_sdk_8_0.CompatibilitiesSsdActiveItem() # CompatibilitiesSsdActiveItem | 

try:
    api_response = api_instance.create_compatibilities_ssd_active_item(compatibilities_ssd_active_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->create_compatibilities_ssd_active_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compatibilities_ssd_active_item** | [**CompatibilitiesSsdActiveItem**](CompatibilitiesSsdActiveItem.md)|  | 

### Return type

[**CreateCompatibilitiesClassActiveItemResponse**](CreateCompatibilitiesClassActiveItemResponse.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_storagepool_nodepool**
> CreateStoragepoolTierResponse create_storagepool_nodepool(storagepool_nodepool)



Create a new node pool.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
storagepool_nodepool = isi_sdk_8_0.StoragepoolNodepoolCreateParams() # StoragepoolNodepoolCreateParams | 

try:
    api_response = api_instance.create_storagepool_nodepool(storagepool_nodepool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->create_storagepool_nodepool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_nodepool** | [**StoragepoolNodepoolCreateParams**](StoragepoolNodepoolCreateParams.md)|  | 

### Return type

[**CreateStoragepoolTierResponse**](CreateStoragepoolTierResponse.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_storagepool_tier**
> CreateStoragepoolTierResponse create_storagepool_tier(storagepool_tier)



Create a new tier.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
storagepool_tier = isi_sdk_8_0.StoragepoolTierCreateParams() # StoragepoolTierCreateParams | 

try:
    api_response = api_instance.create_storagepool_tier(storagepool_tier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->create_storagepool_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_tier** | [**StoragepoolTierCreateParams**](StoragepoolTierCreateParams.md)|  | 

### Return type

[**CreateStoragepoolTierResponse**](CreateStoragepoolTierResponse.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_compatibilities_class_active_by_id**
> delete_compatibilities_class_active_by_id(compatibilities_class_active_id)



Delete an active compatibility by id

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
compatibilities_class_active_id = 'compatibilities_class_active_id_example' # str | Delete an active compatibility by id

try:
    api_instance.delete_compatibilities_class_active_by_id(compatibilities_class_active_id)
except ApiException as e:
    print("Exception when calling StoragepoolApi->delete_compatibilities_class_active_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compatibilities_class_active_id** | **str**| Delete an active compatibility by id | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_compatibilities_ssd_active_by_id**
> delete_compatibilities_ssd_active_by_id(compatibilities_ssd_active_id)



Delete an active ssd compatibility by id

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
compatibilities_ssd_active_id = 'compatibilities_ssd_active_id_example' # str | Delete an active ssd compatibility by id

try:
    api_instance.delete_compatibilities_ssd_active_by_id(compatibilities_ssd_active_id)
except ApiException as e:
    print("Exception when calling StoragepoolApi->delete_compatibilities_ssd_active_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compatibilities_ssd_active_id** | **str**| Delete an active ssd compatibility by id | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storagepool_nodepool**
> delete_storagepool_nodepool(storagepool_nodepool_id)



Delete node pool.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
storagepool_nodepool_id = 'storagepool_nodepool_id_example' # str | Delete node pool.

try:
    api_instance.delete_storagepool_nodepool(storagepool_nodepool_id)
except ApiException as e:
    print("Exception when calling StoragepoolApi->delete_storagepool_nodepool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_nodepool_id** | **str**| Delete node pool. | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storagepool_tier**
> delete_storagepool_tier(storagepool_tier_id)



Delete tier.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
storagepool_tier_id = 'storagepool_tier_id_example' # str | Delete tier.

try:
    api_instance.delete_storagepool_tier(storagepool_tier_id)
except ApiException as e:
    print("Exception when calling StoragepoolApi->delete_storagepool_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_tier_id** | **str**| Delete tier. | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storagepool_tiers**
> delete_storagepool_tiers()



Delete all tiers.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_instance.delete_storagepool_tiers()
except ApiException as e:
    print("Exception when calling StoragepoolApi->delete_storagepool_tiers: %s\n" % e)
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

# **get_compatibilities_class_active_by_id**
> CompatibilitiesClassActive get_compatibilities_class_active_by_id(compatibilities_class_active_id)



Get an active compatibilities by id

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
compatibilities_class_active_id = 'compatibilities_class_active_id_example' # str | Get an active compatibilities by id

try:
    api_response = api_instance.get_compatibilities_class_active_by_id(compatibilities_class_active_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_compatibilities_class_active_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compatibilities_class_active_id** | **str**| Get an active compatibilities by id | 

### Return type

[**CompatibilitiesClassActive**](CompatibilitiesClassActive.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compatibilities_class_available**
> CompatibilitiesClassAvailable get_compatibilities_class_available()



Get a list of available compatibilities

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_compatibilities_class_available()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_compatibilities_class_available: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CompatibilitiesClassAvailable**](CompatibilitiesClassAvailable.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compatibilities_ssd_active_by_id**
> CompatibilitiesSsdActive get_compatibilities_ssd_active_by_id(compatibilities_ssd_active_id)



Get a active ssd compatibilities by id

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
compatibilities_ssd_active_id = 'compatibilities_ssd_active_id_example' # str | Get a active ssd compatibilities by id

try:
    api_response = api_instance.get_compatibilities_ssd_active_by_id(compatibilities_ssd_active_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_compatibilities_ssd_active_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compatibilities_ssd_active_id** | **str**| Get a active ssd compatibilities by id | 

### Return type

[**CompatibilitiesSsdActive**](CompatibilitiesSsdActive.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compatibilities_ssd_available**
> CompatibilitiesSsdAvailable get_compatibilities_ssd_available()



Get a list of available ssd compatibilities

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_compatibilities_ssd_available()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_compatibilities_ssd_available: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CompatibilitiesSsdAvailable**](CompatibilitiesSsdAvailable.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_nodepool**
> StoragepoolNodepools get_storagepool_nodepool(storagepool_nodepool_id)



Retrieve node pool information.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
storagepool_nodepool_id = 'storagepool_nodepool_id_example' # str | Retrieve node pool information.

try:
    api_response = api_instance.get_storagepool_nodepool(storagepool_nodepool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_nodepool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_nodepool_id** | **str**| Retrieve node pool information. | 

### Return type

[**StoragepoolNodepools**](StoragepoolNodepools.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_settings**
> StoragepoolSettings get_storagepool_settings()



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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_storagepool_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoragepoolSettings**](StoragepoolSettings.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_status**
> StoragepoolStatus get_storagepool_status()



List any health conditions detected.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_storagepool_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoragepoolStatus**](StoragepoolStatus.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_storagepools**
> StoragepoolStoragepools get_storagepool_storagepools()



List all storage pools.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_storagepool_storagepools()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_storagepools: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoragepoolStoragepools**](StoragepoolStoragepools.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_suggested_protection_nid**
> StoragepoolSuggestedProtection get_storagepool_suggested_protection_nid(storagepool_suggested_protection_nid)



Retrieve the suggested protection policy.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
storagepool_suggested_protection_nid = 'storagepool_suggested_protection_nid_example' # str | Retrieve the suggested protection policy.

try:
    api_response = api_instance.get_storagepool_suggested_protection_nid(storagepool_suggested_protection_nid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_suggested_protection_nid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_suggested_protection_nid** | **str**| Retrieve the suggested protection policy. | 

### Return type

[**StoragepoolSuggestedProtection**](StoragepoolSuggestedProtection.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_tier**
> StoragepoolTiers get_storagepool_tier(storagepool_tier_id)



Retrieve tier information.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
storagepool_tier_id = 'storagepool_tier_id_example' # str | Retrieve tier information.

try:
    api_response = api_instance.get_storagepool_tier(storagepool_tier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_tier_id** | **str**| Retrieve tier information. | 

### Return type

[**StoragepoolTiers**](StoragepoolTiers.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_unprovisioned**
> StoragepoolUnprovisioned get_storagepool_unprovisioned()



Get the unprovisioned nodes and drives

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_storagepool_unprovisioned()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_unprovisioned: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoragepoolUnprovisioned**](StoragepoolUnprovisioned.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compatibilities_class_active**
> CompatibilitiesClassActiveExtended list_compatibilities_class_active()



Get a list of active compatibilities

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.list_compatibilities_class_active()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->list_compatibilities_class_active: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CompatibilitiesClassActiveExtended**](CompatibilitiesClassActiveExtended.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_compatibilities_ssd_active**
> CompatibilitiesSsdActiveExtended list_compatibilities_ssd_active()



Get a list of active ssd compatibilities

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.list_compatibilities_ssd_active()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->list_compatibilities_ssd_active: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CompatibilitiesSsdActiveExtended**](CompatibilitiesSsdActiveExtended.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_storagepool_nodepools**
> StoragepoolNodepoolsExtended list_storagepool_nodepools()



List all node pools.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.list_storagepool_nodepools()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->list_storagepool_nodepools: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoragepoolNodepoolsExtended**](StoragepoolNodepoolsExtended.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_storagepool_tiers**
> StoragepoolTiersExtended list_storagepool_tiers()



List all tiers.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.list_storagepool_tiers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->list_storagepool_tiers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoragepoolTiersExtended**](StoragepoolTiersExtended.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_compatibilities_ssd_active_by_id**
> update_compatibilities_ssd_active_by_id(compatibilities_ssd_active_id_params, compatibilities_ssd_active_id)



Modify an ssd compatibility by id

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
compatibilities_ssd_active_id_params = isi_sdk_8_0.CompatibilitiesSsdActiveIdParams() # CompatibilitiesSsdActiveIdParams | 
compatibilities_ssd_active_id = 'compatibilities_ssd_active_id_example' # str | Modify an ssd compatibility by id

try:
    api_instance.update_compatibilities_ssd_active_by_id(compatibilities_ssd_active_id_params, compatibilities_ssd_active_id)
except ApiException as e:
    print("Exception when calling StoragepoolApi->update_compatibilities_ssd_active_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compatibilities_ssd_active_id_params** | [**CompatibilitiesSsdActiveIdParams**](CompatibilitiesSsdActiveIdParams.md)|  | 
 **compatibilities_ssd_active_id** | **str**| Modify an ssd compatibility by id | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storagepool_nodepool**
> update_storagepool_nodepool(storagepool_nodepool, storagepool_nodepool_id)



Modify node pool. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
storagepool_nodepool = isi_sdk_8_0.StoragepoolNodepool() # StoragepoolNodepool | 
storagepool_nodepool_id = 'storagepool_nodepool_id_example' # str | Modify node pool. All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_storagepool_nodepool(storagepool_nodepool, storagepool_nodepool_id)
except ApiException as e:
    print("Exception when calling StoragepoolApi->update_storagepool_nodepool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_nodepool** | [**StoragepoolNodepool**](StoragepoolNodepool.md)|  | 
 **storagepool_nodepool_id** | **str**| Modify node pool. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storagepool_settings**
> update_storagepool_settings(storagepool_settings)



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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
storagepool_settings = isi_sdk_8_0.StoragepoolSettingsExtended() # StoragepoolSettingsExtended | 

try:
    api_instance.update_storagepool_settings(storagepool_settings)
except ApiException as e:
    print("Exception when calling StoragepoolApi->update_storagepool_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_settings** | [**StoragepoolSettingsExtended**](StoragepoolSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storagepool_tier**
> update_storagepool_tier(storagepool_tier, storagepool_tier_id)



Modify tier. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk_8_0.StoragepoolApi(isi_sdk_8_0.ApiClient(configuration))
storagepool_tier = isi_sdk_8_0.StoragepoolTier() # StoragepoolTier | 
storagepool_tier_id = 'storagepool_tier_id_example' # str | Modify tier. All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_storagepool_tier(storagepool_tier, storagepool_tier_id)
except ApiException as e:
    print("Exception when calling StoragepoolApi->update_storagepool_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_tier** | [**StoragepoolTier**](StoragepoolTier.md)|  | 
 **storagepool_tier_id** | **str**| Modify tier. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

