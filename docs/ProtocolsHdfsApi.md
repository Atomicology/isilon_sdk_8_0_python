# isi_sdk_8_0.ProtocolsHdfsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_proxyusers_name_member**](ProtocolsHdfsApi.md#create_proxyusers_name_member) | **POST** /platform/1/protocols/hdfs/proxyusers/{Name}/members | 
[**delete_proxyusers_name_member**](ProtocolsHdfsApi.md#delete_proxyusers_name_member) | **DELETE** /platform/1/protocols/hdfs/proxyusers/{Name}/members/{ProxyusersNameMemberId} | 
[**list_proxyusers_name_members**](ProtocolsHdfsApi.md#list_proxyusers_name_members) | **GET** /platform/1/protocols/hdfs/proxyusers/{Name}/members | 
[**update_proxyusers_name_member**](ProtocolsHdfsApi.md#update_proxyusers_name_member) | **PUT** /platform/1/protocols/hdfs/proxyusers/{Name}/members/{ProxyusersNameMemberId} | 


# **create_proxyusers_name_member**
> CreateResponse create_proxyusers_name_member(proxyusers_name_member, name, zone=zone)



Add a member to the HDFS proxyuser.

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
api_instance = isi_sdk_8_0.ProtocolsHdfsApi(isi_sdk_8_0.ApiClient(configuration))
proxyusers_name_member = isi_sdk_8_0.GroupMember() # GroupMember | 
name = 'name_example' # str | 
zone = 'zone_example' # str | Specifies which access zone or zones to use. (optional)

try:
    api_response = api_instance.create_proxyusers_name_member(proxyusers_name_member, name, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsHdfsApi->create_proxyusers_name_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxyusers_name_member** | [**GroupMember**](GroupMember.md)|  | 
 **name** | **str**|  | 
 **zone** | **str**| Specifies which access zone or zones to use. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_proxyusers_name_member**
> delete_proxyusers_name_member(proxyusers_name_member_id, name, zone=zone)



Remove a member from the HDFS proxyuser.

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
api_instance = isi_sdk_8_0.ProtocolsHdfsApi(isi_sdk_8_0.ApiClient(configuration))
proxyusers_name_member_id = 'proxyusers_name_member_id_example' # str | Remove a member from the HDFS proxyuser.
name = 'name_example' # str | 
zone = 'zone_example' # str | Specifies which access zone or zones to use. (optional)

try:
    api_instance.delete_proxyusers_name_member(proxyusers_name_member_id, name, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsHdfsApi->delete_proxyusers_name_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxyusers_name_member_id** | **str**| Remove a member from the HDFS proxyuser. | 
 **name** | **str**|  | 
 **zone** | **str**| Specifies which access zone or zones to use. | [optional] 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_proxyusers_name_members**
> GroupMembers list_proxyusers_name_members(name, zone=zone)



List all the members of the HDFS proxyuser.

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
api_instance = isi_sdk_8_0.ProtocolsHdfsApi(isi_sdk_8_0.ApiClient(configuration))
name = 'name_example' # str | 
zone = 'zone_example' # str | Specifies which access zone or zones to use. (optional)

try:
    api_response = api_instance.list_proxyusers_name_members(name, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsHdfsApi->list_proxyusers_name_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **zone** | **str**| Specifies which access zone or zones to use. | [optional] 

### Return type

[**GroupMembers**](GroupMembers.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_proxyusers_name_member**
> update_proxyusers_name_member(proxyusers_name_member, proxyusers_name_member_id, name, zone=zone)



Create a new HDFS proxyuser.

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
api_instance = isi_sdk_8_0.ProtocolsHdfsApi(isi_sdk_8_0.ApiClient(configuration))
proxyusers_name_member = isi_sdk_8_0.Empty() # Empty | 
proxyusers_name_member_id = 'proxyusers_name_member_id_example' # str | Create a new HDFS proxyuser.
name = 'name_example' # str | 
zone = 'zone_example' # str | Specifies which access zone or zones to use. (optional)

try:
    api_instance.update_proxyusers_name_member(proxyusers_name_member, proxyusers_name_member_id, name, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsHdfsApi->update_proxyusers_name_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxyusers_name_member** | [**Empty**](Empty.md)|  | 
 **proxyusers_name_member_id** | **str**| Create a new HDFS proxyuser. | 
 **name** | **str**|  | 
 **zone** | **str**| Specifies which access zone or zones to use. | [optional] 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

