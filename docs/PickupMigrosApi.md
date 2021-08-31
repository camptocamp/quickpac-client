# swagger_client.PickupMigrosApi

All URIs are relative to *https://api.quickpac.ch*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pickmup_set_paket_status_get**](PickupMigrosApi.md#pickmup_set_paket_status_get) | **GET** /Pickmup/SetPaketStatus | SetPaketStatus
[**pickmup_set_paket_status_post**](PickupMigrosApi.md#pickmup_set_paket_status_post) | **POST** /Pickmup/SetPaketStatus | SetPaketStatus
[**pickmup_set_ruecksendung_get**](PickupMigrosApi.md#pickmup_set_ruecksendung_get) | **GET** /Pickmup/SetRuecksendung | SetRuecksendung
[**pickmup_set_ruecksendung_post**](PickupMigrosApi.md#pickmup_set_ruecksendung_post) | **POST** /Pickmup/SetRuecksendung | SetRuecksendung

# **pickmup_set_paket_status_get**
> PickupMigrosCallbackResultResponse pickmup_set_paket_status_get(use_production=use_production, validation_only=validation_only, password=password, barcode_nr=barcode_nr, paketstatus_old=paketstatus_old, paketstatus_neu=paketstatus_neu)

SetPaketStatus

### SetPaketStatus

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
api_instance = swagger_client.PickupMigrosApi(swagger_client.ApiClient(configuration))
use_production = true # bool |  (optional)
validation_only = true # bool |  (optional)
password = 'password_example' # str |  (optional)
barcode_nr = 'barcode_nr_example' # str |  (optional)
paketstatus_old = 56 # int |  (optional)
paketstatus_neu = 56 # int |  (optional)

try:
    # SetPaketStatus
    api_response = api_instance.pickmup_set_paket_status_get(use_production=use_production, validation_only=validation_only, password=password, barcode_nr=barcode_nr, paketstatus_old=paketstatus_old, paketstatus_neu=paketstatus_neu)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickupMigrosApi->pickmup_set_paket_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_production** | **bool**|  | [optional] 
 **validation_only** | **bool**|  | [optional] 
 **password** | **str**|  | [optional] 
 **barcode_nr** | **str**|  | [optional] 
 **paketstatus_old** | **int**|  | [optional] 
 **paketstatus_neu** | **int**|  | [optional] 

### Return type

[**PickupMigrosCallbackResultResponse**](PickupMigrosCallbackResultResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pickmup_set_paket_status_post**
> PickupMigrosCallbackResultResponse pickmup_set_paket_status_post(body=body)

SetPaketStatus

### SetPaketStatus

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
api_instance = swagger_client.PickupMigrosApi(swagger_client.ApiClient(configuration))
body = swagger_client.PickupMigrosSetPaketStatusRequest() # PickupMigrosSetPaketStatusRequest |  (optional)

try:
    # SetPaketStatus
    api_response = api_instance.pickmup_set_paket_status_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickupMigrosApi->pickmup_set_paket_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PickupMigrosSetPaketStatusRequest**](PickupMigrosSetPaketStatusRequest.md)|  | [optional] 

### Return type

[**PickupMigrosCallbackResultResponse**](PickupMigrosCallbackResultResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pickmup_set_ruecksendung_get**
> PickupMigrosCallbackResultResponse pickmup_set_ruecksendung_get(use_production=use_production, validation_only=validation_only, password=password, barcode_nr=barcode_nr, abholort_id=abholort_id)

SetRuecksendung

### SetRuecksendung

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
api_instance = swagger_client.PickupMigrosApi(swagger_client.ApiClient(configuration))
use_production = true # bool |  (optional)
validation_only = true # bool |  (optional)
password = 'password_example' # str |  (optional)
barcode_nr = 'barcode_nr_example' # str |  (optional)
abholort_id = 'abholort_id_example' # str |  (optional)

try:
    # SetRuecksendung
    api_response = api_instance.pickmup_set_ruecksendung_get(use_production=use_production, validation_only=validation_only, password=password, barcode_nr=barcode_nr, abholort_id=abholort_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickupMigrosApi->pickmup_set_ruecksendung_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_production** | **bool**|  | [optional] 
 **validation_only** | **bool**|  | [optional] 
 **password** | **str**|  | [optional] 
 **barcode_nr** | **str**|  | [optional] 
 **abholort_id** | **str**|  | [optional] 

### Return type

[**PickupMigrosCallbackResultResponse**](PickupMigrosCallbackResultResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pickmup_set_ruecksendung_post**
> PickupMigrosCallbackResultResponse pickmup_set_ruecksendung_post(body=body)

SetRuecksendung

### SetRuecksendung

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
api_instance = swagger_client.PickupMigrosApi(swagger_client.ApiClient(configuration))
body = swagger_client.PickupMigrosSetRuecksendung() # PickupMigrosSetRuecksendung |  (optional)

try:
    # SetRuecksendung
    api_response = api_instance.pickmup_set_ruecksendung_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickupMigrosApi->pickmup_set_ruecksendung_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PickupMigrosSetRuecksendung**](PickupMigrosSetRuecksendung.md)|  | [optional] 

### Return type

[**PickupMigrosCallbackResultResponse**](PickupMigrosCallbackResultResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

