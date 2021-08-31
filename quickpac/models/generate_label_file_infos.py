# coding: utf-8

"""
    Quickpac API

    Here you will find all public interfaces to the Quickpac system.  # noqa: E501

    OpenAPI spec version: v1.00
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GenerateLabelFileInfos(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mode': 'ModeType',
        'franking_license': 'str',
        'customer': 'GenerateLabelCustomer'
    }

    attribute_map = {
        'mode': 'Mode',
        'franking_license': 'FrankingLicense',
        'customer': 'Customer'
    }

    def __init__(self, mode=None, franking_license=None, customer=None):  # noqa: E501
        """GenerateLabelFileInfos - a model defined in Swagger"""  # noqa: E501
        self._mode = None
        self._franking_license = None
        self._customer = None
        self.discriminator = None
        if mode is not None:
            self.mode = mode
        if franking_license is not None:
            self.franking_license = franking_license
        if customer is not None:
            self.customer = customer

    @property
    def mode(self):
        """Gets the mode of this GenerateLabelFileInfos.  # noqa: E501


        :return: The mode of this GenerateLabelFileInfos.  # noqa: E501
        :rtype: ModeType
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this GenerateLabelFileInfos.


        :param mode: The mode of this GenerateLabelFileInfos.  # noqa: E501
        :type: ModeType
        """

        self._mode = mode

    @property
    def franking_license(self):
        """Gets the franking_license of this GenerateLabelFileInfos.  # noqa: E501


        :return: The franking_license of this GenerateLabelFileInfos.  # noqa: E501
        :rtype: str
        """
        return self._franking_license

    @franking_license.setter
    def franking_license(self, franking_license):
        """Sets the franking_license of this GenerateLabelFileInfos.


        :param franking_license: The franking_license of this GenerateLabelFileInfos.  # noqa: E501
        :type: str
        """

        self._franking_license = franking_license

    @property
    def customer(self):
        """Gets the customer of this GenerateLabelFileInfos.  # noqa: E501


        :return: The customer of this GenerateLabelFileInfos.  # noqa: E501
        :rtype: GenerateLabelCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this GenerateLabelFileInfos.


        :param customer: The customer of this GenerateLabelFileInfos.  # noqa: E501
        :type: GenerateLabelCustomer
        """

        self._customer = customer

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GenerateLabelFileInfos, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GenerateLabelFileInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other