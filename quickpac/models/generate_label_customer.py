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

class GenerateLabelCustomer(object):
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
        'name1': 'str',
        'name2': 'str',
        'street': 'str',
        'po_box': 'str',
        'zip': 'str',
        'city': 'str',
        'country': 'str',
        'logo': 'str',
        'logo_format': 'str',
        'logo_rotation': 'int',
        'logo_rotation_specified': 'bool',
        'logo_aspect_ratio': 'LogoAspectRatio',
        'logo_aspect_ratio_specified': 'bool',
        'logo_horizontal_align': 'LogoHorizontalAlign',
        'logo_horizontal_align_specified': 'bool',
        'logo_vertical_align': 'LogoVerticalAlign',
        'logo_vertical_align_specified': 'bool'
    }

    attribute_map = {
        'name1': 'Name1',
        'name2': 'Name2',
        'street': 'Street',
        'po_box': 'POBox',
        'zip': 'ZIP',
        'city': 'City',
        'country': 'Country',
        'logo': 'Logo',
        'logo_format': 'LogoFormat',
        'logo_rotation': 'LogoRotation',
        'logo_rotation_specified': 'LogoRotationSpecified',
        'logo_aspect_ratio': 'LogoAspectRatio',
        'logo_aspect_ratio_specified': 'LogoAspectRatioSpecified',
        'logo_horizontal_align': 'LogoHorizontalAlign',
        'logo_horizontal_align_specified': 'LogoHorizontalAlignSpecified',
        'logo_vertical_align': 'LogoVerticalAlign',
        'logo_vertical_align_specified': 'LogoVerticalAlignSpecified'
    }

    def __init__(self, name1=None, name2=None, street=None, po_box=None, zip=None, city=None, country=None, logo=None, logo_format=None, logo_rotation=None, logo_rotation_specified=None, logo_aspect_ratio=None, logo_aspect_ratio_specified=None, logo_horizontal_align=None, logo_horizontal_align_specified=None, logo_vertical_align=None, logo_vertical_align_specified=None):  # noqa: E501
        """GenerateLabelCustomer - a model defined in Swagger"""  # noqa: E501
        self._name1 = None
        self._name2 = None
        self._street = None
        self._po_box = None
        self._zip = None
        self._city = None
        self._country = None
        self._logo = None
        self._logo_format = None
        self._logo_rotation = None
        self._logo_rotation_specified = None
        self._logo_aspect_ratio = None
        self._logo_aspect_ratio_specified = None
        self._logo_horizontal_align = None
        self._logo_horizontal_align_specified = None
        self._logo_vertical_align = None
        self._logo_vertical_align_specified = None
        self.discriminator = None
        if name1 is not None:
            self.name1 = name1
        if name2 is not None:
            self.name2 = name2
        if street is not None:
            self.street = street
        if po_box is not None:
            self.po_box = po_box
        if zip is not None:
            self.zip = zip
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if logo is not None:
            self.logo = logo
        if logo_format is not None:
            self.logo_format = logo_format
        if logo_rotation is not None:
            self.logo_rotation = logo_rotation
        if logo_rotation_specified is not None:
            self.logo_rotation_specified = logo_rotation_specified
        if logo_aspect_ratio is not None:
            self.logo_aspect_ratio = logo_aspect_ratio
        if logo_aspect_ratio_specified is not None:
            self.logo_aspect_ratio_specified = logo_aspect_ratio_specified
        if logo_horizontal_align is not None:
            self.logo_horizontal_align = logo_horizontal_align
        if logo_horizontal_align_specified is not None:
            self.logo_horizontal_align_specified = logo_horizontal_align_specified
        if logo_vertical_align is not None:
            self.logo_vertical_align = logo_vertical_align
        if logo_vertical_align_specified is not None:
            self.logo_vertical_align_specified = logo_vertical_align_specified

    @property
    def name1(self):
        """Gets the name1 of this GenerateLabelCustomer.  # noqa: E501


        :return: The name1 of this GenerateLabelCustomer.  # noqa: E501
        :rtype: str
        """
        return self._name1

    @name1.setter
    def name1(self, name1):
        """Sets the name1 of this GenerateLabelCustomer.


        :param name1: The name1 of this GenerateLabelCustomer.  # noqa: E501
        :type: str
        """

        self._name1 = name1

    @property
    def name2(self):
        """Gets the name2 of this GenerateLabelCustomer.  # noqa: E501


        :return: The name2 of this GenerateLabelCustomer.  # noqa: E501
        :rtype: str
        """
        return self._name2

    @name2.setter
    def name2(self, name2):
        """Sets the name2 of this GenerateLabelCustomer.


        :param name2: The name2 of this GenerateLabelCustomer.  # noqa: E501
        :type: str
        """

        self._name2 = name2

    @property
    def street(self):
        """Gets the street of this GenerateLabelCustomer.  # noqa: E501


        :return: The street of this GenerateLabelCustomer.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this GenerateLabelCustomer.


        :param street: The street of this GenerateLabelCustomer.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def po_box(self):
        """Gets the po_box of this GenerateLabelCustomer.  # noqa: E501


        :return: The po_box of this GenerateLabelCustomer.  # noqa: E501
        :rtype: str
        """
        return self._po_box

    @po_box.setter
    def po_box(self, po_box):
        """Sets the po_box of this GenerateLabelCustomer.


        :param po_box: The po_box of this GenerateLabelCustomer.  # noqa: E501
        :type: str
        """

        self._po_box = po_box

    @property
    def zip(self):
        """Gets the zip of this GenerateLabelCustomer.  # noqa: E501


        :return: The zip of this GenerateLabelCustomer.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this GenerateLabelCustomer.


        :param zip: The zip of this GenerateLabelCustomer.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def city(self):
        """Gets the city of this GenerateLabelCustomer.  # noqa: E501


        :return: The city of this GenerateLabelCustomer.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this GenerateLabelCustomer.


        :param city: The city of this GenerateLabelCustomer.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this GenerateLabelCustomer.  # noqa: E501


        :return: The country of this GenerateLabelCustomer.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this GenerateLabelCustomer.


        :param country: The country of this GenerateLabelCustomer.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def logo(self):
        """Gets the logo of this GenerateLabelCustomer.  # noqa: E501


        :return: The logo of this GenerateLabelCustomer.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this GenerateLabelCustomer.


        :param logo: The logo of this GenerateLabelCustomer.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def logo_format(self):
        """Gets the logo_format of this GenerateLabelCustomer.  # noqa: E501


        :return: The logo_format of this GenerateLabelCustomer.  # noqa: E501
        :rtype: str
        """
        return self._logo_format

    @logo_format.setter
    def logo_format(self, logo_format):
        """Sets the logo_format of this GenerateLabelCustomer.


        :param logo_format: The logo_format of this GenerateLabelCustomer.  # noqa: E501
        :type: str
        """

        self._logo_format = logo_format

    @property
    def logo_rotation(self):
        """Gets the logo_rotation of this GenerateLabelCustomer.  # noqa: E501


        :return: The logo_rotation of this GenerateLabelCustomer.  # noqa: E501
        :rtype: int
        """
        return self._logo_rotation

    @logo_rotation.setter
    def logo_rotation(self, logo_rotation):
        """Sets the logo_rotation of this GenerateLabelCustomer.


        :param logo_rotation: The logo_rotation of this GenerateLabelCustomer.  # noqa: E501
        :type: int
        """

        self._logo_rotation = logo_rotation

    @property
    def logo_rotation_specified(self):
        """Gets the logo_rotation_specified of this GenerateLabelCustomer.  # noqa: E501


        :return: The logo_rotation_specified of this GenerateLabelCustomer.  # noqa: E501
        :rtype: bool
        """
        return self._logo_rotation_specified

    @logo_rotation_specified.setter
    def logo_rotation_specified(self, logo_rotation_specified):
        """Sets the logo_rotation_specified of this GenerateLabelCustomer.


        :param logo_rotation_specified: The logo_rotation_specified of this GenerateLabelCustomer.  # noqa: E501
        :type: bool
        """

        self._logo_rotation_specified = logo_rotation_specified

    @property
    def logo_aspect_ratio(self):
        """Gets the logo_aspect_ratio of this GenerateLabelCustomer.  # noqa: E501


        :return: The logo_aspect_ratio of this GenerateLabelCustomer.  # noqa: E501
        :rtype: LogoAspectRatio
        """
        return self._logo_aspect_ratio

    @logo_aspect_ratio.setter
    def logo_aspect_ratio(self, logo_aspect_ratio):
        """Sets the logo_aspect_ratio of this GenerateLabelCustomer.


        :param logo_aspect_ratio: The logo_aspect_ratio of this GenerateLabelCustomer.  # noqa: E501
        :type: LogoAspectRatio
        """

        self._logo_aspect_ratio = logo_aspect_ratio

    @property
    def logo_aspect_ratio_specified(self):
        """Gets the logo_aspect_ratio_specified of this GenerateLabelCustomer.  # noqa: E501


        :return: The logo_aspect_ratio_specified of this GenerateLabelCustomer.  # noqa: E501
        :rtype: bool
        """
        return self._logo_aspect_ratio_specified

    @logo_aspect_ratio_specified.setter
    def logo_aspect_ratio_specified(self, logo_aspect_ratio_specified):
        """Sets the logo_aspect_ratio_specified of this GenerateLabelCustomer.


        :param logo_aspect_ratio_specified: The logo_aspect_ratio_specified of this GenerateLabelCustomer.  # noqa: E501
        :type: bool
        """

        self._logo_aspect_ratio_specified = logo_aspect_ratio_specified

    @property
    def logo_horizontal_align(self):
        """Gets the logo_horizontal_align of this GenerateLabelCustomer.  # noqa: E501


        :return: The logo_horizontal_align of this GenerateLabelCustomer.  # noqa: E501
        :rtype: LogoHorizontalAlign
        """
        return self._logo_horizontal_align

    @logo_horizontal_align.setter
    def logo_horizontal_align(self, logo_horizontal_align):
        """Sets the logo_horizontal_align of this GenerateLabelCustomer.


        :param logo_horizontal_align: The logo_horizontal_align of this GenerateLabelCustomer.  # noqa: E501
        :type: LogoHorizontalAlign
        """

        self._logo_horizontal_align = logo_horizontal_align

    @property
    def logo_horizontal_align_specified(self):
        """Gets the logo_horizontal_align_specified of this GenerateLabelCustomer.  # noqa: E501


        :return: The logo_horizontal_align_specified of this GenerateLabelCustomer.  # noqa: E501
        :rtype: bool
        """
        return self._logo_horizontal_align_specified

    @logo_horizontal_align_specified.setter
    def logo_horizontal_align_specified(self, logo_horizontal_align_specified):
        """Sets the logo_horizontal_align_specified of this GenerateLabelCustomer.


        :param logo_horizontal_align_specified: The logo_horizontal_align_specified of this GenerateLabelCustomer.  # noqa: E501
        :type: bool
        """

        self._logo_horizontal_align_specified = logo_horizontal_align_specified

    @property
    def logo_vertical_align(self):
        """Gets the logo_vertical_align of this GenerateLabelCustomer.  # noqa: E501


        :return: The logo_vertical_align of this GenerateLabelCustomer.  # noqa: E501
        :rtype: LogoVerticalAlign
        """
        return self._logo_vertical_align

    @logo_vertical_align.setter
    def logo_vertical_align(self, logo_vertical_align):
        """Sets the logo_vertical_align of this GenerateLabelCustomer.


        :param logo_vertical_align: The logo_vertical_align of this GenerateLabelCustomer.  # noqa: E501
        :type: LogoVerticalAlign
        """

        self._logo_vertical_align = logo_vertical_align

    @property
    def logo_vertical_align_specified(self):
        """Gets the logo_vertical_align_specified of this GenerateLabelCustomer.  # noqa: E501


        :return: The logo_vertical_align_specified of this GenerateLabelCustomer.  # noqa: E501
        :rtype: bool
        """
        return self._logo_vertical_align_specified

    @logo_vertical_align_specified.setter
    def logo_vertical_align_specified(self, logo_vertical_align_specified):
        """Sets the logo_vertical_align_specified of this GenerateLabelCustomer.


        :param logo_vertical_align_specified: The logo_vertical_align_specified of this GenerateLabelCustomer.  # noqa: E501
        :type: bool
        """

        self._logo_vertical_align_specified = logo_vertical_align_specified

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
        if issubclass(GenerateLabelCustomer, dict):
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
        if not isinstance(other, GenerateLabelCustomer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
