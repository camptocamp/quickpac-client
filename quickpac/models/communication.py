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

class Communication(object):
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
        'item': 'str',
        'email': 'str',
        'mobile': 'str',
        'item_element_name': 'ItemChoiceType'
    }

    attribute_map = {
        'item': 'Item',
        'email': 'Email',
        'mobile': 'Mobile',
        'item_element_name': 'ItemElementName'
    }

    def __init__(self, item=None, email=None, mobile=None, item_element_name=None):  # noqa: E501
        """Communication - a model defined in Swagger"""  # noqa: E501
        self._item = None
        self._email = None
        self._mobile = None
        self._item_element_name = None
        self.discriminator = None
        if item is not None:
            self.item = item
        if email is not None:
            self.email = email
        if mobile is not None:
            self.mobile = mobile
        if item_element_name is not None:
            self.item_element_name = item_element_name

    @property
    def item(self):
        """Gets the item of this Communication.  # noqa: E501


        :return: The item of this Communication.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this Communication.


        :param item: The item of this Communication.  # noqa: E501
        :type: str
        """

        self._item = item

    @property
    def email(self):
        """Gets the email of this Communication.  # noqa: E501


        :return: The email of this Communication.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Communication.


        :param email: The email of this Communication.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def mobile(self):
        """Gets the mobile of this Communication.  # noqa: E501


        :return: The mobile of this Communication.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this Communication.


        :param mobile: The mobile of this Communication.  # noqa: E501
        :type: str
        """

        self._mobile = mobile

    @property
    def item_element_name(self):
        """Gets the item_element_name of this Communication.  # noqa: E501


        :return: The item_element_name of this Communication.  # noqa: E501
        :rtype: ItemChoiceType
        """
        return self._item_element_name

    @item_element_name.setter
    def item_element_name(self, item_element_name):
        """Sets the item_element_name of this Communication.


        :param item_element_name: The item_element_name of this Communication.  # noqa: E501
        :type: ItemChoiceType
        """

        self._item_element_name = item_element_name

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
        if issubclass(Communication, dict):
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
        if not isinstance(other, Communication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
