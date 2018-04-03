# isi_sdk_8_0.AuthRolesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role_member**](AuthRolesApi.md#create_role_member) | **POST** /platform/1/auth/roles/{Role}/members | 
[**create_role_privilege**](AuthRolesApi.md#create_role_privilege) | **POST** /platform/1/auth/roles/{Role}/privileges | 
[**delete_role_member**](AuthRolesApi.md#delete_role_member) | **DELETE** /platform/1/auth/roles/{Role}/members/{RoleMemberId} | 
[**delete_role_privilege**](AuthRolesApi.md#delete_role_privilege) | **DELETE** /platform/1/auth/roles/{Role}/privileges/{RolePrivilegeId} | 
[**list_role_members**](AuthRolesApi.md#list_role_members) | **GET** /platform/1/auth/roles/{Role}/members | 
[**list_role_privileges**](AuthRolesApi.md#list_role_privileges) | **GET** /platform/1/auth/roles/{Role}/privileges | 


# **create_role_member**
> CreateResponse create_role_member(role_member, role)



Add a member to the role.

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
api_instance = isi_sdk_8_0.AuthRolesApi(isi_sdk_8_0.ApiClient(configuration))
role_member = isi_sdk_8_0.GroupMember() # GroupMember | 
role = 'role_example' # str | 

try:
    api_response = api_instance.create_role_member(role_member, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->create_role_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_member** | [**GroupMember**](GroupMember.md)|  | 
 **role** | **str**|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role_privilege**
> CreateResponse create_role_privilege(role_privilege, role)



Add a privilege to the role.

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
api_instance = isi_sdk_8_0.AuthRolesApi(isi_sdk_8_0.ApiClient(configuration))
role_privilege = isi_sdk_8_0.AuthIdNtokenPrivilegeItem() # AuthIdNtokenPrivilegeItem | 
role = 'role_example' # str | 

try:
    api_response = api_instance.create_role_privilege(role_privilege, role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->create_role_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_privilege** | [**AuthIdNtokenPrivilegeItem**](AuthIdNtokenPrivilegeItem.md)|  | 
 **role** | **str**|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_member**
> delete_role_member(role_member_id, role)



Remove a member from the role.

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
api_instance = isi_sdk_8_0.AuthRolesApi(isi_sdk_8_0.ApiClient(configuration))
role_member_id = 'role_member_id_example' # str | Remove a member from the role.
role = 'role_example' # str | 

try:
    api_instance.delete_role_member(role_member_id, role)
except ApiException as e:
    print("Exception when calling AuthRolesApi->delete_role_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_member_id** | **str**| Remove a member from the role. | 
 **role** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_privilege**
> delete_role_privilege(role_privilege_id, role)



Remove a privilege from a role.

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
api_instance = isi_sdk_8_0.AuthRolesApi(isi_sdk_8_0.ApiClient(configuration))
role_privilege_id = 'role_privilege_id_example' # str | Remove a privilege from a role.
role = 'role_example' # str | 

try:
    api_instance.delete_role_privilege(role_privilege_id, role)
except ApiException as e:
    print("Exception when calling AuthRolesApi->delete_role_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_privilege_id** | **str**| Remove a privilege from a role. | 
 **role** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_members**
> GroupMembers list_role_members(role, resolve_names=resolve_names)



List all the members of the role.

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
api_instance = isi_sdk_8_0.AuthRolesApi(isi_sdk_8_0.ApiClient(configuration))
role = 'role_example' # str | 
resolve_names = true # bool | Resolve names of personas. (optional)

try:
    api_response = api_instance.list_role_members(role, resolve_names=resolve_names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->list_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**|  | 
 **resolve_names** | **bool**| Resolve names of personas. | [optional] 

### Return type

[**GroupMembers**](GroupMembers.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_privileges**
> RolePrivileges list_role_privileges(role)



List all privileges in the role.

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
api_instance = isi_sdk_8_0.AuthRolesApi(isi_sdk_8_0.ApiClient(configuration))
role = 'role_example' # str | 

try:
    api_response = api_instance.list_role_privileges(role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->list_role_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**|  | 

### Return type

[**RolePrivileges**](RolePrivileges.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

