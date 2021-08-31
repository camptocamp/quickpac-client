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

class Recipient(object):
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
        'title': 'str',
        'personally_addressed': 'bool',
        'personally_addressed_specified': 'bool',
        'name1': 'str',
        'first_name': 'str',
        'name2': 'str',
        'name3': 'str',
        'address_suffix': 'str',
        'street': 'str',
        'house_no': 'str',
        'po_box': 'str',
        'zip': 'str',
        'city': 'str',
        'country': 'str',
        'mobile': 'str',
        'e_mail': 'str',
        'label_address': 'list[str]',
        'what3words': 'str'
    }

    attribute_map = {
        'title': 'Title',
        'personally_addressed': 'PersonallyAddressed',
        'personally_addressed_specified': 'PersonallyAddressedSpecified',
        'name1': 'Name1',
        'first_name': 'FirstName',
        'name2': 'Name2',
        'name3': 'Name3',
        'address_suffix': 'AddressSuffix',
        'street': 'Street',
        'house_no': 'HouseNo',
        'po_box': 'POBox',
        'zip': 'ZIP',
        'city': 'City',
        'country': 'Country',
        'mobile': 'Mobile',
        'e_mail': 'EMail',
        'label_address': 'LabelAddress',
        'what3words': 'what3words'
    }

    def __init__(self, title=None, personally_addressed=None, personally_addressed_specified=None, name1=None, first_name=None, name2=None, name3=None, address_suffix=None, street=None, house_no=None, po_box=None, zip=None, city=None, country=None, mobile=None, e_mail=None, label_address=None, what3words=None):  # noqa: E501
        """Recipient - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._personally_addressed = None
        self._personally_addressed_specified = None
        self._name1 = None
        self._first_name = None
        self._name2 = None
        self._name3 = None
        self._address_suffix = None
        self._street = None
        self._house_no = None
        self._po_box = None
        self._zip = None
        self._city = None
        self._country = None
        self._mobile = None
        self._e_mail = None
        self._label_address = None
        self._what3words = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if personally_addressed is not None:
            self.personally_addressed = personally_addressed
        if personally_addressed_specified is not None:
            self.personally_addressed_specified = personally_addressed_specified
        if name1 is not None:
            self.name1 = name1
        if first_name is not None:
            self.first_name = first_name
        if name2 is not None:
            self.name2 = name2
        if name3 is not None:
            self.name3 = name3
        if address_suffix is not None:
            self.address_suffix = address_suffix
        if street is not None:
            self.street = street
        if house_no is not None:
            self.house_no = house_no
        if po_box is not None:
            self.po_box = po_box
        if zip is not None:
            self.zip = zip
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if mobile is not None:
            self.mobile = mobile
        if e_mail is not None:
            self.e_mail = e_mail
        if label_address is not None:
            self.label_address = label_address
        if what3words is not None:
            self.what3words = what3words

    @property
    def title(self):
        """Gets the title of this Recipient.  # noqa: E501


        :return: The title of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Recipient.


        :param title: The title of this Recipient.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def personally_addressed(self):
        """Gets the personally_addressed of this Recipient.  # noqa: E501


        :return: The personally_addressed of this Recipient.  # noqa: E501
        :rtype: bool
        """
        return self._personally_addressed

    @personally_addressed.setter
    def personally_addressed(self, personally_addressed):
        """Sets the personally_addressed of this Recipient.


        :param personally_addressed: The personally_addressed of this Recipient.  # noqa: E501
        :type: bool
        """

        self._personally_addressed = personally_addressed

    @property
    def personally_addressed_specified(self):
        """Gets the personally_addressed_specified of this Recipient.  # noqa: E501


        :return: The personally_addressed_specified of this Recipient.  # noqa: E501
        :rtype: bool
        """
        return self._personally_addressed_specified

    @personally_addressed_specified.setter
    def personally_addressed_specified(self, personally_addressed_specified):
        """Sets the personally_addressed_specified of this Recipient.


        :param personally_addressed_specified: The personally_addressed_specified of this Recipient.  # noqa: E501
        :type: bool
        """

        self._personally_addressed_specified = personally_addressed_specified

    @property
    def name1(self):
        """Gets the name1 of this Recipient.  # noqa: E501


        :return: The name1 of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._name1

    @name1.setter
    def name1(self, name1):
        """Sets the name1 of this Recipient.


        :param name1: The name1 of this Recipient.  # noqa: E501
        :type: str
        """

        self._name1 = name1

    @property
    def first_name(self):
        """Gets the first_name of this Recipient.  # noqa: E501


        :return: The first_name of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Recipient.


        :param first_name: The first_name of this Recipient.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def name2(self):
        """Gets the name2 of this Recipient.  # noqa: E501


        :return: The name2 of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._name2

    @name2.setter
    def name2(self, name2):
        """Sets the name2 of this Recipient.


        :param name2: The name2 of this Recipient.  # noqa: E501
        :type: str
        """

        self._name2 = name2

    @property
    def name3(self):
        """Gets the name3 of this Recipient.  # noqa: E501


        :return: The name3 of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._name3

    @name3.setter
    def name3(self, name3):
        """Sets the name3 of this Recipient.


        :param name3: The name3 of this Recipient.  # noqa: E501
        :type: str
        """

        self._name3 = name3

    @property
    def address_suffix(self):
        """Gets the address_suffix of this Recipient.  # noqa: E501


        :return: The address_suffix of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._address_suffix

    @address_suffix.setter
    def address_suffix(self, address_suffix):
        """Sets the address_suffix of this Recipient.


        :param address_suffix: The address_suffix of this Recipient.  # noqa: E501
        :type: str
        """

        self._address_suffix = address_suffix

    @property
    def street(self):
        """Gets the street of this Recipient.  # noqa: E501


        :return: The street of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this Recipient.


        :param street: The street of this Recipient.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def house_no(self):
        """Gets the house_no of this Recipient.  # noqa: E501


        :return: The house_no of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._house_no

    @house_no.setter
    def house_no(self, house_no):
        """Sets the house_no of this Recipient.


        :param house_no: The house_no of this Recipient.  # noqa: E501
        :type: str
        """

        self._house_no = house_no

    @property
    def po_box(self):
        """Gets the po_box of this Recipient.  # noqa: E501


        :return: The po_box of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._po_box

    @po_box.setter
    def po_box(self, po_box):
        """Sets the po_box of this Recipient.


        :param po_box: The po_box of this Recipient.  # noqa: E501
        :type: str
        """

        self._po_box = po_box

    @property
    def zip(self):
        """Gets the zip of this Recipient.  # noqa: E501


        :return: The zip of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this Recipient.


        :param zip: The zip of this Recipient.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def city(self):
        """Gets the city of this Recipient.  # noqa: E501


        :return: The city of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Recipient.


        :param city: The city of this Recipient.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this Recipient.  # noqa: E501


        :return: The country of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Recipient.


        :param country: The country of this Recipient.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def mobile(self):
        """Gets the mobile of this Recipient.  # noqa: E501


        :return: The mobile of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this Recipient.


        :param mobile: The mobile of this Recipient.  # noqa: E501
        :type: str
        """

        self._mobile = mobile

    @property
    def e_mail(self):
        """Gets the e_mail of this Recipient.  # noqa: E501


        :return: The e_mail of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._e_mail

    @e_mail.setter
    def e_mail(self, e_mail):
        """Sets the e_mail of this Recipient.


        :param e_mail: The e_mail of this Recipient.  # noqa: E501
        :type: str
        """

        self._e_mail = e_mail

    @property
    def label_address(self):
        """Gets the label_address of this Recipient.  # noqa: E501


        :return: The label_address of this Recipient.  # noqa: E501
        :rtype: list[str]
        """
        return self._label_address

    @label_address.setter
    def label_address(self, label_address):
        """Sets the label_address of this Recipient.


        :param label_address: The label_address of this Recipient.  # noqa: E501
        :type: list[str]
        """

        self._label_address = label_address

    @property
    def what3words(self):
        """Gets the what3words of this Recipient.  # noqa: E501

        Gets or sets the what3words.  In lower case!  # noqa: E501

        :return: The what3words of this Recipient.  # noqa: E501
        :rtype: str
        """
        return self._what3words

    @what3words.setter
    def what3words(self, what3words):
        """Sets the what3words of this Recipient.

        Gets or sets the what3words.  In lower case!  # noqa: E501

        :param what3words: The what3words of this Recipient.  # noqa: E501
        :type: str
        """

        self._what3words = what3words

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
        if issubclass(Recipient, dict):
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
        if not isinstance(other, Recipient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other