# Quickpac
Here you will find all public interfaces to the Quickpac system.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1.00
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 3.4+

## Installation & Usage
### pip install

```sh
pip install quickpac
```

Or you can install directly from Github:
```sh
pip install git+https://github.com/camptocamp/quickpac-client.git
```

### Swagger client generation

Generate via [Swagger codegen](https://pypi.org/project/swagger-codegen).

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import quickpac
from quickpac.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = quickpac.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = quickpac.BarcodeApi(quickpac.ApiClient(configuration))
body = quickpac.GenerateLabelRequest() # GenerateLabelRequest |  (optional)

try:
    # Generates an address label
    api_response = api_instance.barcode_generate_label_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BarcodeApi->barcode_generate_label_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.quickpac.ch*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BarcodeApi* | [**barcode_generate_label_post**](docs/BarcodeApi.md#barcode_generate_label_post) | **POST** /Barcode/GenerateLabel | Generates an address label
*PickupMigrosApi* | [**pickmup_set_paket_status_get**](docs/PickupMigrosApi.md#pickmup_set_paket_status_get) | **GET** /Pickmup/SetPaketStatus | SetPaketStatus
*PickupMigrosApi* | [**pickmup_set_paket_status_post**](docs/PickupMigrosApi.md#pickmup_set_paket_status_post) | **POST** /Pickmup/SetPaketStatus | SetPaketStatus
*PickupMigrosApi* | [**pickmup_set_ruecksendung_get**](docs/PickupMigrosApi.md#pickmup_set_ruecksendung_get) | **GET** /Pickmup/SetRuecksendung | SetRuecksendung
*PickupMigrosApi* | [**pickmup_set_ruecksendung_post**](docs/PickupMigrosApi.md#pickmup_set_ruecksendung_post) | **POST** /Pickmup/SetRuecksendung | SetRuecksendung
*ZIPApi* | [**z_ip_get_all_zip_codes_get**](docs/ZIPApi.md#z_ip_get_all_zip_codes_get) | **GET** /ZIP/GetAllZipCodes | Returns all currently deliverable and planned postcodes.
*ZIPApi* | [**z_ip_is_deliverable_zip_code_get**](docs/ZIPApi.md#z_ip_is_deliverable_zip_code_get) | **GET** /ZIP/IsDeliverableZipCode | Checks whether the requested postcode can currently be delivered.

## Documentation For Models

 - [Communication](docs/Communication.md)
 - [Dimensions](docs/Dimensions.md)
 - [GenerateLabelCustomer](docs/GenerateLabelCustomer.md)
 - [GenerateLabelDefinition](docs/GenerateLabelDefinition.md)
 - [GenerateLabelEnvelope](docs/GenerateLabelEnvelope.md)
 - [GenerateLabelFileInfos](docs/GenerateLabelFileInfos.md)
 - [GenerateLabelRequest](docs/GenerateLabelRequest.md)
 - [GenerateLabelResponse](docs/GenerateLabelResponse.md)
 - [GenerateLabelResponseDefinition](docs/GenerateLabelResponseDefinition.md)
 - [GenerateLabelResponseEnvelope](docs/GenerateLabelResponseEnvelope.md)
 - [GenerateLabelResponseEnvelopeData](docs/GenerateLabelResponseEnvelopeData.md)
 - [GenerateLabelResponseEnvelopeDataProvider](docs/GenerateLabelResponseEnvelopeDataProvider.md)
 - [GenerateLabelResponseEnvelopeDataProviderSending](docs/GenerateLabelResponseEnvelopeDataProviderSending.md)
 - [Item](docs/Item.md)
 - [ItemChoiceType](docs/ItemChoiceType.md)
 - [LabelData](docs/LabelData.md)
 - [LabelDataProvider](docs/LabelDataProvider.md)
 - [LabelDataProviderSending](docs/LabelDataProviderSending.md)
 - [LabelResponseItem](docs/LabelResponseItem.md)
 - [Language](docs/Language.md)
 - [LanguageCode](docs/LanguageCode.md)
 - [LogoAspectRatio](docs/LogoAspectRatio.md)
 - [LogoHorizontalAlign](docs/LogoHorizontalAlign.md)
 - [LogoVerticalAlign](docs/LogoVerticalAlign.md)
 - [MessageType](docs/MessageType.md)
 - [ModeType](docs/ModeType.md)
 - [Notification](docs/Notification.md)
 - [NotificationType](docs/NotificationType.md)
 - [PickupMigrosCallbackResultResponse](docs/PickupMigrosCallbackResultResponse.md)
 - [PickupMigrosSetPaketStatusRequest](docs/PickupMigrosSetPaketStatusRequest.md)
 - [PickupMigrosSetRuecksendung](docs/PickupMigrosSetRuecksendung.md)
 - [PrintAddressesType](docs/PrintAddressesType.md)
 - [Recipient](docs/Recipient.md)
 - [ServiceCodeAttributes](docs/ServiceCodeAttributes.md)
 - [ZIPAllResponse](docs/ZIPAllResponse.md)
 - [ZIPIsCurrentResponse](docs/ZIPIsCurrentResponse.md)
 - [ZIPModel](docs/ZIPModel.md)

## Documentation For Authorization


## Basic

- **Type**: HTTP basic authentication


## Author


