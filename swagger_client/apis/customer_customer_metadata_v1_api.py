# coding: utf-8

"""
    Magento Community

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CustomerCustomerMetadataV1Api(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def customer_customer_metadata_v1_get_all_attributes_metadata_get(self, **kwargs):
        """
        Get all attribute metadata.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customer_metadata_v1_get_all_attributes_metadata_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[CustomerDataAttributeMetadataInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.customer_customer_metadata_v1_get_all_attributes_metadata_get_with_http_info(**kwargs)
        else:
            (data) = self.customer_customer_metadata_v1_get_all_attributes_metadata_get_with_http_info(**kwargs)
            return data

    def customer_customer_metadata_v1_get_all_attributes_metadata_get_with_http_info(self, **kwargs):
        """
        Get all attribute metadata.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customer_metadata_v1_get_all_attributes_metadata_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: list[CustomerDataAttributeMetadataInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method customer_customer_metadata_v1_get_all_attributes_metadata_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/attributeMetadata/customer', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[CustomerDataAttributeMetadataInterface]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def customer_customer_metadata_v1_get_attribute_metadata_get(self, attribute_code, **kwargs):
        """
        Retrieve attribute metadata.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customer_metadata_v1_get_attribute_metadata_get(attribute_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str attribute_code: (required)
        :return: CustomerDataAttributeMetadataInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.customer_customer_metadata_v1_get_attribute_metadata_get_with_http_info(attribute_code, **kwargs)
        else:
            (data) = self.customer_customer_metadata_v1_get_attribute_metadata_get_with_http_info(attribute_code, **kwargs)
            return data

    def customer_customer_metadata_v1_get_attribute_metadata_get_with_http_info(self, attribute_code, **kwargs):
        """
        Retrieve attribute metadata.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customer_metadata_v1_get_attribute_metadata_get_with_http_info(attribute_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str attribute_code: (required)
        :return: CustomerDataAttributeMetadataInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['attribute_code']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method customer_customer_metadata_v1_get_attribute_metadata_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'attribute_code' is set
        if ('attribute_code' not in params) or (params['attribute_code'] is None):
            raise ValueError("Missing the required parameter `attribute_code` when calling `customer_customer_metadata_v1_get_attribute_metadata_get`")


        collection_formats = {}

        path_params = {}
        if 'attribute_code' in params:
            path_params['attributeCode'] = params['attribute_code']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/attributeMetadata/customer/attribute/{attributeCode}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CustomerDataAttributeMetadataInterface',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def customer_customer_metadata_v1_get_attributes_get(self, form_code, **kwargs):
        """
        Retrieve all attributes filtered by form code
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customer_metadata_v1_get_attributes_get(form_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str form_code: (required)
        :return: list[CustomerDataAttributeMetadataInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.customer_customer_metadata_v1_get_attributes_get_with_http_info(form_code, **kwargs)
        else:
            (data) = self.customer_customer_metadata_v1_get_attributes_get_with_http_info(form_code, **kwargs)
            return data

    def customer_customer_metadata_v1_get_attributes_get_with_http_info(self, form_code, **kwargs):
        """
        Retrieve all attributes filtered by form code
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customer_metadata_v1_get_attributes_get_with_http_info(form_code, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str form_code: (required)
        :return: list[CustomerDataAttributeMetadataInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['form_code']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method customer_customer_metadata_v1_get_attributes_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'form_code' is set
        if ('form_code' not in params) or (params['form_code'] is None):
            raise ValueError("Missing the required parameter `form_code` when calling `customer_customer_metadata_v1_get_attributes_get`")


        collection_formats = {}

        path_params = {}
        if 'form_code' in params:
            path_params['formCode'] = params['form_code']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/attributeMetadata/customer/form/{formCode}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[CustomerDataAttributeMetadataInterface]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def customer_customer_metadata_v1_get_custom_attributes_metadata_get(self, **kwargs):
        """
        Get custom attributes metadata for the given data interface.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customer_metadata_v1_get_custom_attributes_metadata_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str data_interface_name:
        :return: list[CustomerDataAttributeMetadataInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.customer_customer_metadata_v1_get_custom_attributes_metadata_get_with_http_info(**kwargs)
        else:
            (data) = self.customer_customer_metadata_v1_get_custom_attributes_metadata_get_with_http_info(**kwargs)
            return data

    def customer_customer_metadata_v1_get_custom_attributes_metadata_get_with_http_info(self, **kwargs):
        """
        Get custom attributes metadata for the given data interface.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.customer_customer_metadata_v1_get_custom_attributes_metadata_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str data_interface_name:
        :return: list[CustomerDataAttributeMetadataInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_interface_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method customer_customer_metadata_v1_get_custom_attributes_metadata_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'data_interface_name' in params:
            query_params.append(('dataInterfaceName', params['data_interface_name']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/attributeMetadata/customer/custom', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[CustomerDataAttributeMetadataInterface]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
