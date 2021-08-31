# swagger_client.ZIPApi

All URIs are relative to *https://api.quickpac.ch*

Method | HTTP request | Description
------------- | ------------- | -------------
[**z_ip_get_all_zip_codes_get**](ZIPApi.md#z_ip_get_all_zip_codes_get) | **GET** /ZIP/GetAllZipCodes | Returns all currently deliverable and planned postcodes.
[**z_ip_is_deliverable_zip_code_get**](ZIPApi.md#z_ip_is_deliverable_zip_code_get) | **GET** /ZIP/IsDeliverableZipCode | Checks whether the requested postcode can currently be delivered.

# **z_ip_get_all_zip_codes_get**
> ZIPAllResponse z_ip_get_all_zip_codes_get()

Returns all currently deliverable and planned postcodes.

### Deliverable and planned postcodes   * This API returns all postcodes in a list which can be supplied by Quickpac now or in the future.   * Each postcode contains the first and last day of delivery by Quickpac   * In the event of an error, the 'Error' or 'Warning' property is set with one or more corresponding messages. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ZIPApi(swagger_client.ApiClient(configuration))

try:
    # Returns all currently deliverable and planned postcodes.
    api_response = api_instance.z_ip_get_all_zip_codes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZIPApi->z_ip_get_all_zip_codes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ZIPAllResponse**](ZIPAllResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **z_ip_is_deliverable_zip_code_get**
> ZIPIsCurrentResponse z_ip_is_deliverable_zip_code_get(zip_code=zip_code)

Checks whether the requested postcode can currently be delivered.

### Deliverable zip code   * This API checks whether the requested zip code can currently be supplied by Quickpac.   * In the event of an error, the 'Error' or 'Warning' property is set with one or more corresponding messages. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ZIPApi(swagger_client.ApiClient(configuration))
zip_code = 789 # int | ZIP code in the range from 1,000 - 9,999. (optional)

try:
    # Checks whether the requested postcode can currently be delivered.
    api_response = api_instance.z_ip_is_deliverable_zip_code_get(zip_code=zip_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZIPApi->z_ip_is_deliverable_zip_code_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zip_code** | **int**| ZIP code in the range from 1,000 - 9,999. | [optional] 

### Return type

[**ZIPIsCurrentResponse**](ZIPIsCurrentResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

