# isi_sdk.ClusterApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_add_node_item**](ClusterApi.md#create_cluster_add_node_item) | **POST** /platform/3/cluster/add-node | 
[**get_cluster_config**](ClusterApi.md#get_cluster_config) | **GET** /platform/3/cluster/config | 
[**get_cluster_email**](ClusterApi.md#get_cluster_email) | **GET** /platform/1/cluster/email | 
[**get_cluster_identity**](ClusterApi.md#get_cluster_identity) | **GET** /platform/3/cluster/identity | 
[**get_cluster_node**](ClusterApi.md#get_cluster_node) | **GET** /platform/3/cluster/nodes/{ClusterNodeId} | 
[**get_cluster_nodes**](ClusterApi.md#get_cluster_nodes) | **GET** /platform/3/cluster/nodes | 
[**get_cluster_nodes_available**](ClusterApi.md#get_cluster_nodes_available) | **GET** /platform/3/cluster/nodes-available | 
[**get_cluster_owner**](ClusterApi.md#get_cluster_owner) | **GET** /platform/1/cluster/owner | 
[**get_cluster_statfs**](ClusterApi.md#get_cluster_statfs) | **GET** /platform/1/cluster/statfs | 
[**get_cluster_time**](ClusterApi.md#get_cluster_time) | **GET** /platform/3/cluster/time | 
[**get_cluster_timezone**](ClusterApi.md#get_cluster_timezone) | **GET** /platform/3/cluster/timezone | 
[**get_cluster_version**](ClusterApi.md#get_cluster_version) | **GET** /platform/3/cluster/version | 
[**get_timezone_region**](ClusterApi.md#get_timezone_region) | **GET** /platform/3/cluster/timezone/regions/{TimezoneRegionId} | 
[**get_timezone_settings**](ClusterApi.md#get_timezone_settings) | **GET** /platform/3/cluster/timezone/settings | 
[**update_cluster_email**](ClusterApi.md#update_cluster_email) | **PUT** /platform/1/cluster/email | 
[**update_cluster_identity**](ClusterApi.md#update_cluster_identity) | **PUT** /platform/3/cluster/identity | 
[**update_cluster_node**](ClusterApi.md#update_cluster_node) | **PUT** /platform/3/cluster/nodes/{ClusterNodeId} | 
[**update_cluster_owner**](ClusterApi.md#update_cluster_owner) | **PUT** /platform/1/cluster/owner | 
[**update_cluster_time**](ClusterApi.md#update_cluster_time) | **PUT** /platform/3/cluster/time | 
[**update_cluster_timezone**](ClusterApi.md#update_cluster_timezone) | **PUT** /platform/3/cluster/timezone | 
[**update_timezone_settings**](ClusterApi.md#update_timezone_settings) | **PUT** /platform/3/cluster/timezone/settings | 


# **create_cluster_add_node_item**
> Empty create_cluster_add_node_item(cluster_add_node_item)



Serial number and arguments of node to add.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()
cluster_add_node_item = isi_sdk.ClusterAddNodeItem() # ClusterAddNodeItem | 

try: 
    api_response = api_instance.create_cluster_add_node_item(cluster_add_node_item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->create_cluster_add_node_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_add_node_item** | [**ClusterAddNodeItem**](ClusterAddNodeItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_config**
> ClusterConfig get_cluster_config()



Retrieve the cluster information.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()

try: 
    api_response = api_instance.get_cluster_config()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_cluster_config: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterConfig**](ClusterConfig.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_email**
> ClusterEmail get_cluster_email()



Get the cluster email notification settings.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()

try: 
    api_response = api_instance.get_cluster_email()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_cluster_email: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterEmail**](ClusterEmail.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_identity**
> ClusterIdentity get_cluster_identity()



Retrieve the login information.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()

try: 
    api_response = api_instance.get_cluster_identity()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_cluster_identity: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterIdentity**](ClusterIdentity.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node**
> ClusterNodes get_cluster_node(cluster_node_id)



Retrieve node information.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()
cluster_node_id = 56 # int | Retrieve node information.

try: 
    api_response = api_instance.get_cluster_node(cluster_node_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_cluster_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_node_id** | **int**| Retrieve node information. | 

### Return type

[**ClusterNodes**](ClusterNodes.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_nodes**
> ClusterNodesExtended get_cluster_nodes()



List the nodes on this cluster.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()

try: 
    api_response = api_instance.get_cluster_nodes()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_cluster_nodes: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterNodesExtended**](ClusterNodesExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_nodes_available**
> ClusterNodesAvailable get_cluster_nodes_available()



List all nodes that are available to add to this cluster.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()

try: 
    api_response = api_instance.get_cluster_nodes_available()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_cluster_nodes_available: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterNodesAvailable**](ClusterNodesAvailable.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_owner**
> ClusterOwner get_cluster_owner()



Get the cluster contact info settings

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()

try: 
    api_response = api_instance.get_cluster_owner()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_cluster_owner: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterOwner**](ClusterOwner.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_statfs**
> ClusterStatfs get_cluster_statfs()



Retrieve the filesystem statistics.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()

try: 
    api_response = api_instance.get_cluster_statfs()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_cluster_statfs: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterStatfs**](ClusterStatfs.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_time**
> ClusterTime get_cluster_time()



Retrieve the current time as reported by each node.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()

try: 
    api_response = api_instance.get_cluster_time()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_cluster_time: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterTime**](ClusterTime.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_timezone**
> ClusterTimezone get_cluster_timezone()



Get the cluster timezone.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()

try: 
    api_response = api_instance.get_cluster_timezone()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_cluster_timezone: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterTimezone**](ClusterTimezone.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_version**
> ClusterVersion get_cluster_version()



Retrieve the OneFS version as reported by each node.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()

try: 
    api_response = api_instance.get_cluster_version()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_cluster_version: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterVersion**](ClusterVersion.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timezone_region**
> TimezoneRegions get_timezone_region(timezone_region_id, sort=sort, resume=resume, show_all=show_all, dst_reset=dst_reset, limit=limit, dir=dir)



List timezone regions.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()
timezone_region_id = 'timezone_region_id_example' # str | List timezone regions.
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
show_all = true # bool | Show all timezones within the region specified in the URI. (optional)
dst_reset = true # bool | This query arg is not needed in normal use cases. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try: 
    api_response = api_instance.get_timezone_region(timezone_region_id, sort=sort, resume=resume, show_all=show_all, dst_reset=dst_reset, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_timezone_region: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timezone_region_id** | **str**| List timezone regions. | 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **show_all** | **bool**| Show all timezones within the region specified in the URI. | [optional] 
 **dst_reset** | **bool**| This query arg is not needed in normal use cases. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**TimezoneRegions**](TimezoneRegions.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timezone_settings**
> TimezoneSettings get_timezone_settings()



Retrieve the cluster timezone.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()

try: 
    api_response = api_instance.get_timezone_settings()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ClusterApi->get_timezone_settings: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TimezoneSettings**](TimezoneSettings.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_email**
> update_cluster_email(cluster_email)



Modify the cluster email notification settings.  All input fields are optional, but one or more must be supplied.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()
cluster_email = isi_sdk.ClusterEmailExtended() # ClusterEmailExtended | 

try: 
    api_instance.update_cluster_email(cluster_email)
except ApiException as e:
    print "Exception when calling ClusterApi->update_cluster_email: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_email** | [**ClusterEmailExtended**](ClusterEmailExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_identity**
> update_cluster_identity(cluster_identity)



Modify the login information.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()
cluster_identity = isi_sdk.ClusterIdentityExtended() # ClusterIdentityExtended | 

try: 
    api_instance.update_cluster_identity(cluster_identity)
except ApiException as e:
    print "Exception when calling ClusterApi->update_cluster_identity: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_identity** | [**ClusterIdentityExtended**](ClusterIdentityExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_node**
> update_cluster_node(cluster_node, cluster_node_id)



Modify one or more node settings.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()
cluster_node = isi_sdk.ClusterNode() # ClusterNode | 
cluster_node_id = 56 # int | Modify one or more node settings.

try: 
    api_instance.update_cluster_node(cluster_node, cluster_node_id)
except ApiException as e:
    print "Exception when calling ClusterApi->update_cluster_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_node** | [**ClusterNode**](ClusterNode.md)|  | 
 **cluster_node_id** | **int**| Modify one or more node settings. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_owner**
> update_cluster_owner(cluster_owner)



Modify the cluster contact info settings.  All input fields are optional, but one or more must be supplied.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()
cluster_owner = isi_sdk.ClusterOwner() # ClusterOwner | 

try: 
    api_instance.update_cluster_owner(cluster_owner)
except ApiException as e:
    print "Exception when calling ClusterApi->update_cluster_owner: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_owner** | [**ClusterOwner**](ClusterOwner.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_time**
> update_cluster_time(cluster_time)



Set cluster time.  Time will mostly be synchronized across nodes, but there may be slight drift.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()
cluster_time = isi_sdk.ClusterTimeExtended() # ClusterTimeExtended | 

try: 
    api_instance.update_cluster_time(cluster_time)
except ApiException as e:
    print "Exception when calling ClusterApi->update_cluster_time: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_time** | [**ClusterTimeExtended**](ClusterTimeExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_timezone**
> update_cluster_timezone(cluster_timezone)



Set a new timezone for the cluster.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()
cluster_timezone = isi_sdk.ClusterTimezoneExtended() # ClusterTimezoneExtended | 

try: 
    api_instance.update_cluster_timezone(cluster_timezone)
except ApiException as e:
    print "Exception when calling ClusterApi->update_cluster_timezone: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_timezone** | [**ClusterTimezoneExtended**](ClusterTimezoneExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_timezone_settings**
> update_timezone_settings(timezone_settings)



Modify the cluster timezone.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.ClusterApi()
timezone_settings = isi_sdk.TimezoneRegionTimezone() # TimezoneRegionTimezone | 

try: 
    api_instance.update_timezone_settings(timezone_settings)
except ApiException as e:
    print "Exception when calling ClusterApi->update_timezone_settings: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timezone_settings** | [**TimezoneRegionTimezone**](TimezoneRegionTimezone.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

