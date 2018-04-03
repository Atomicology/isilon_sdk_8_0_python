# isi_sdk_8_0.ClusterNodesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_drives_drive_add_item**](ClusterNodesApi.md#create_drives_drive_add_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/add | 
[**create_drives_drive_firmware_update_item**](ClusterNodesApi.md#create_drives_drive_firmware_update_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/firmware/update | 
[**create_drives_drive_format_item**](ClusterNodesApi.md#create_drives_drive_format_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/format | 
[**create_drives_drive_purpose_item**](ClusterNodesApi.md#create_drives_drive_purpose_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/purpose | 
[**create_drives_drive_smartfail_item**](ClusterNodesApi.md#create_drives_drive_smartfail_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/smartfail | 
[**create_drives_drive_stopfail_item**](ClusterNodesApi.md#create_drives_drive_stopfail_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/stopfail | 
[**create_drives_drive_suspend_item**](ClusterNodesApi.md#create_drives_drive_suspend_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/suspend | 
[**create_node_reboot_item**](ClusterNodesApi.md#create_node_reboot_item) | **POST** /platform/3/cluster/nodes/{Lnn}/reboot | 
[**create_node_shutdown_item**](ClusterNodesApi.md#create_node_shutdown_item) | **POST** /platform/3/cluster/nodes/{Lnn}/shutdown | 
[**get_drives_drive_firmware**](ClusterNodesApi.md#get_drives_drive_firmware) | **GET** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/firmware | 
[**get_node_drive**](ClusterNodesApi.md#get_node_drive) | **GET** /platform/3/cluster/nodes/{Lnn}/drives/{NodeDriveId} | 
[**get_node_drives**](ClusterNodesApi.md#get_node_drives) | **GET** /platform/3/cluster/nodes/{Lnn}/drives | 
[**get_node_drives_purposelist**](ClusterNodesApi.md#get_node_drives_purposelist) | **GET** /platform/3/cluster/nodes/{Lnn}/drives-purposelist | 
[**get_node_hardware**](ClusterNodesApi.md#get_node_hardware) | **GET** /platform/3/cluster/nodes/{Lnn}/hardware | 
[**get_node_hardware_fast**](ClusterNodesApi.md#get_node_hardware_fast) | **GET** /platform/3/cluster/nodes/{Lnn}/hardware-fast | 
[**get_node_partitions**](ClusterNodesApi.md#get_node_partitions) | **GET** /platform/3/cluster/nodes/{Lnn}/partitions | 
[**get_node_sensors**](ClusterNodesApi.md#get_node_sensors) | **GET** /platform/3/cluster/nodes/{Lnn}/sensors | 
[**get_node_state**](ClusterNodesApi.md#get_node_state) | **GET** /platform/3/cluster/nodes/{Lnn}/state | 
[**get_node_state_readonly**](ClusterNodesApi.md#get_node_state_readonly) | **GET** /platform/3/cluster/nodes/{Lnn}/state/readonly | 
[**get_node_state_servicelight**](ClusterNodesApi.md#get_node_state_servicelight) | **GET** /platform/3/cluster/nodes/{Lnn}/state/servicelight | 
[**get_node_state_smartfail**](ClusterNodesApi.md#get_node_state_smartfail) | **GET** /platform/3/cluster/nodes/{Lnn}/state/smartfail | 
[**get_node_status**](ClusterNodesApi.md#get_node_status) | **GET** /platform/3/cluster/nodes/{Lnn}/status | 
[**get_node_status_batterystatus**](ClusterNodesApi.md#get_node_status_batterystatus) | **GET** /platform/3/cluster/nodes/{Lnn}/status/batterystatus | 
[**list_drives_drive_firmware_update**](ClusterNodesApi.md#list_drives_drive_firmware_update) | **GET** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/firmware/update | 
[**update_node_state_readonly**](ClusterNodesApi.md#update_node_state_readonly) | **PUT** /platform/3/cluster/nodes/{Lnn}/state/readonly | 
[**update_node_state_servicelight**](ClusterNodesApi.md#update_node_state_servicelight) | **PUT** /platform/3/cluster/nodes/{Lnn}/state/servicelight | 
[**update_node_state_smartfail**](ClusterNodesApi.md#update_node_state_smartfail) | **PUT** /platform/3/cluster/nodes/{Lnn}/state/smartfail | 


# **create_drives_drive_add_item**
> Empty create_drives_drive_add_item(drives_drive_add_item, lnn, driveid)



Add a drive to a node.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
drives_drive_add_item = isi_sdk_8_0.Empty() # Empty | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_add_item(drives_drive_add_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_add_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_add_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drives_drive_firmware_update_item**
> Empty create_drives_drive_firmware_update_item(drives_drive_firmware_update_item, lnn, driveid)



Start a drive firmware update.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
drives_drive_firmware_update_item = isi_sdk_8_0.DrivesDriveFirmwareUpdateItem() # DrivesDriveFirmwareUpdateItem | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_firmware_update_item(drives_drive_firmware_update_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_firmware_update_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_firmware_update_item** | [**DrivesDriveFirmwareUpdateItem**](DrivesDriveFirmwareUpdateItem.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drives_drive_format_item**
> Empty create_drives_drive_format_item(drives_drive_format_item, lnn, driveid)



Format a drive for use by OneFS.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
drives_drive_format_item = isi_sdk_8_0.DrivesDriveFormatItem() # DrivesDriveFormatItem | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_format_item(drives_drive_format_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_format_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_format_item** | [**DrivesDriveFormatItem**](DrivesDriveFormatItem.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drives_drive_purpose_item**
> Empty create_drives_drive_purpose_item(drives_drive_purpose_item, lnn, driveid)



Assign a drive to a specific use case.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
drives_drive_purpose_item = isi_sdk_8_0.DrivesDrivePurposeItem() # DrivesDrivePurposeItem | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_purpose_item(drives_drive_purpose_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_purpose_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_purpose_item** | [**DrivesDrivePurposeItem**](DrivesDrivePurposeItem.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drives_drive_smartfail_item**
> Empty create_drives_drive_smartfail_item(drives_drive_smartfail_item, lnn, driveid)



Remove a drive from use by OneFS.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
drives_drive_smartfail_item = isi_sdk_8_0.Empty() # Empty | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_smartfail_item(drives_drive_smartfail_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_smartfail_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_smartfail_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drives_drive_stopfail_item**
> Empty create_drives_drive_stopfail_item(drives_drive_stopfail_item, lnn, driveid)



Stop restriping from a smartfailing drive.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
drives_drive_stopfail_item = isi_sdk_8_0.Empty() # Empty | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_stopfail_item(drives_drive_stopfail_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_stopfail_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_stopfail_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drives_drive_suspend_item**
> Empty create_drives_drive_suspend_item(drives_drive_suspend_item, lnn, driveid)



Temporarily remove a drive from use by OneFS.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
drives_drive_suspend_item = isi_sdk_8_0.Empty() # Empty | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_suspend_item(drives_drive_suspend_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_suspend_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_suspend_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node_reboot_item**
> Empty create_node_reboot_item(node_reboot_item, lnn)



Reboot the node specified by <LNN>.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
node_reboot_item = isi_sdk_8_0.Empty() # Empty | 
lnn = 56 # int | 

try:
    api_response = api_instance.create_node_reboot_item(node_reboot_item, lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_node_reboot_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_reboot_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node_shutdown_item**
> Empty create_node_shutdown_item(node_shutdown_item, lnn)



Shutdown the node specified by <LNN>.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
node_shutdown_item = isi_sdk_8_0.Empty() # Empty | 
lnn = 56 # int | 

try:
    api_response = api_instance.create_node_shutdown_item(node_shutdown_item, lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_node_shutdown_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_shutdown_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drives_drive_firmware**
> DrivesDriveFirmware get_drives_drive_firmware(lnn, driveid)



Retrieve drive firmware information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.get_drives_drive_firmware(lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_drives_drive_firmware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**DrivesDriveFirmware**](DrivesDriveFirmware.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_drive**
> NodeDrives get_node_drive(node_drive_id, lnn)



Retrieve drive information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
node_drive_id = 'node_drive_id_example' # str | Retrieve drive information.
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_drive(node_drive_id, lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_drive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_drive_id** | **str**| Retrieve drive information. | 
 **lnn** | **int**|  | 

### Return type

[**NodeDrives**](NodeDrives.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_drives**
> NodeDrives get_node_drives(lnn)



List the drives on this node.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_drives(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_drives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeDrives**](NodeDrives.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_drives_purposelist**
> NodeDrivesPurposelist get_node_drives_purposelist(lnn)



Lists the available purposes for drives in this node.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_drives_purposelist(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_drives_purposelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeDrivesPurposelist**](NodeDrivesPurposelist.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_hardware**
> NodeHardware get_node_hardware(lnn)



Retrieve node hardware identity information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_hardware(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_hardware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeHardware**](NodeHardware.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_hardware_fast**
> NodeHardwareFast get_node_hardware_fast(lnn)



Quickly retrieve a subset of node hardware identity information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_hardware_fast(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_hardware_fast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeHardwareFast**](NodeHardwareFast.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_partitions**
> NodePartitions get_node_partitions(lnn)



Retrieve node partition information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_partitions(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_partitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodePartitions**](NodePartitions.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_sensors**
> NodeSensors get_node_sensors(lnn)



Retrieve node sensor information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_sensors(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_sensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeSensors**](NodeSensors.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_state**
> NodeState get_node_state(lnn)



Retrieve node state information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_state(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeState**](NodeState.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_state_readonly**
> NodeStateReadonly get_node_state_readonly(lnn)



Retrieve node readonly state information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_state_readonly(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_state_readonly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeStateReadonly**](NodeStateReadonly.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_state_servicelight**
> NodeStateServicelight get_node_state_servicelight(lnn)



Retrieve node service light state information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_state_servicelight(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_state_servicelight: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeStateServicelight**](NodeStateServicelight.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_state_smartfail**
> NodeStateSmartfail get_node_state_smartfail(lnn)



Retrieve node smartfail state information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_state_smartfail(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_state_smartfail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeStateSmartfail**](NodeStateSmartfail.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_status**
> NodeStatus get_node_status(lnn)



Retrieve node status information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_status(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeStatus**](NodeStatus.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_status_batterystatus**
> NodeStatusBatterystatus get_node_status_batterystatus(lnn)



Retrieve node battery status information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_status_batterystatus(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_status_batterystatus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeStatusBatterystatus**](NodeStatusBatterystatus.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_drives_drive_firmware_update**
> DrivesDriveFirmwareUpdate list_drives_drive_firmware_update(lnn, driveid)



Retrieve firmware update information.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.list_drives_drive_firmware_update(lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->list_drives_drive_firmware_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**DrivesDriveFirmwareUpdate**](DrivesDriveFirmwareUpdate.md)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_state_readonly**
> update_node_state_readonly(node_state_readonly, lnn)



Modify one or more node readonly state settings.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
node_state_readonly = isi_sdk_8_0.NodeStateReadonlyExtended() # NodeStateReadonlyExtended | 
lnn = 56 # int | 

try:
    api_instance.update_node_state_readonly(node_state_readonly, lnn)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->update_node_state_readonly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_state_readonly** | [**NodeStateReadonlyExtended**](NodeStateReadonlyExtended.md)|  | 
 **lnn** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_state_servicelight**
> update_node_state_servicelight(node_state_servicelight, lnn)



Modify one or more node service light state settings.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
node_state_servicelight = isi_sdk_8_0.NodeStateServicelightExtended() # NodeStateServicelightExtended | 
lnn = 56 # int | 

try:
    api_instance.update_node_state_servicelight(node_state_servicelight, lnn)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->update_node_state_servicelight: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_state_servicelight** | [**NodeStateServicelightExtended**](NodeStateServicelightExtended.md)|  | 
 **lnn** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_state_smartfail**
> update_node_state_smartfail(node_state_smartfail, lnn)



Modify smartfail state of the node.  Only the 'smartfailed' body member has any effect on node smartfail state.

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
api_instance = isi_sdk_8_0.ClusterNodesApi(isi_sdk_8_0.ApiClient(configuration))
node_state_smartfail = isi_sdk_8_0.NodeStateSmartfailExtended() # NodeStateSmartfailExtended | 
lnn = 56 # int | 

try:
    api_instance.update_node_state_smartfail(node_state_smartfail, lnn)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->update_node_state_smartfail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_state_smartfail** | [**NodeStateSmartfailExtended**](NodeStateSmartfailExtended.md)|  | 
 **lnn** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[sessionAuth](../README.md#sessionAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

