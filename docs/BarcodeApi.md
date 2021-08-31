# swagger_client.BarcodeApi

All URIs are relative to *https://api.quickpac.ch*

Method | HTTP request | Description
------------- | ------------- | -------------
[**barcode_generate_label_post**](BarcodeApi.md#barcode_generate_label_post) | **POST** /Barcode/GenerateLabel | Generates an address label

# **barcode_generate_label_post**
> GenerateLabelResponse barcode_generate_label_post(body=body)

Generates an address label

### Generates an address label   * In the event of an error, the 'Error' or 'Warning' property is set with one or more corresponding messages.   * You can find further information in the technical documentation.

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
api_instance = swagger_client.BarcodeApi(swagger_client.ApiClient(configuration))
body = swagger_client.GenerateLabelRequest() # GenerateLabelRequest |  (optional)

try:
    # Generates an address label
    api_response = api_instance.barcode_generate_label_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeApi->barcode_generate_label_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GenerateLabelRequest**](GenerateLabelRequest.md)|  | [optional] 

### Return type

[**GenerateLabelResponse**](GenerateLabelResponse.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json, application/xml, text/xml, application/*+xml
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

