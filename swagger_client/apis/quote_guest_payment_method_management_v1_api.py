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


class QuoteGuestPaymentMethodManagementV1Api(object):
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

    def quote_guest_payment_method_management_v1_get_get(self, cart_id, **kwargs):
        """
        Return the payment method for a specified shopping cart.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.quote_guest_payment_method_management_v1_get_get(cart_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cart_id: The cart ID. (required)
        :return: QuoteDataPaymentInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.quote_guest_payment_method_management_v1_get_get_with_http_info(cart_id, **kwargs)
        else:
            (data) = self.quote_guest_payment_method_management_v1_get_get_with_http_info(cart_id, **kwargs)
            return data

    def quote_guest_payment_method_management_v1_get_get_with_http_info(self, cart_id, **kwargs):
        """
        Return the payment method for a specified shopping cart.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.quote_guest_payment_method_management_v1_get_get_with_http_info(cart_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cart_id: The cart ID. (required)
        :return: QuoteDataPaymentInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cart_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method quote_guest_payment_method_management_v1_get_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cart_id' is set
        if ('cart_id' not in params) or (params['cart_id'] is None):
            raise ValueError("Missing the required parameter `cart_id` when calling `quote_guest_payment_method_management_v1_get_get`")


        collection_formats = {}

        path_params = {}
        if 'cart_id' in params:
            path_params['cartId'] = params['cart_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/guest-carts/{cartId}/selected-payment-method', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='QuoteDataPaymentInterface',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def quote_guest_payment_method_management_v1_get_list_get(self, cart_id, **kwargs):
        """
        List available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See http://devdocs.magento.com/codelinks/attributes.html#GuestPaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.quote_guest_payment_method_management_v1_get_list_get(cart_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cart_id: The cart ID. (required)
        :return: list[QuoteDataPaymentMethodInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.quote_guest_payment_method_management_v1_get_list_get_with_http_info(cart_id, **kwargs)
        else:
            (data) = self.quote_guest_payment_method_management_v1_get_list_get_with_http_info(cart_id, **kwargs)
            return data

    def quote_guest_payment_method_management_v1_get_list_get_with_http_info(self, cart_id, **kwargs):
        """
        List available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See http://devdocs.magento.com/codelinks/attributes.html#GuestPaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.quote_guest_payment_method_management_v1_get_list_get_with_http_info(cart_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cart_id: The cart ID. (required)
        :return: list[QuoteDataPaymentMethodInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cart_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method quote_guest_payment_method_management_v1_get_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cart_id' is set
        if ('cart_id' not in params) or (params['cart_id'] is None):
            raise ValueError("Missing the required parameter `cart_id` when calling `quote_guest_payment_method_management_v1_get_list_get`")


        collection_formats = {}

        path_params = {}
        if 'cart_id' in params:
            path_params['cartId'] = params['cart_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/guest-carts/{cartId}/payment-methods', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[QuoteDataPaymentMethodInterface]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def quote_guest_payment_method_management_v1_set_put(self, cart_id, **kwargs):
        """
        Add a specified payment method to a specified shopping cart.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.quote_guest_payment_method_management_v1_set_put(cart_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cart_id: The cart ID. (required)
        :param Body72 body:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.quote_guest_payment_method_management_v1_set_put_with_http_info(cart_id, **kwargs)
        else:
            (data) = self.quote_guest_payment_method_management_v1_set_put_with_http_info(cart_id, **kwargs)
            return data

    def quote_guest_payment_method_management_v1_set_put_with_http_info(self, cart_id, **kwargs):
        """
        Add a specified payment method to a specified shopping cart.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.quote_guest_payment_method_management_v1_set_put_with_http_info(cart_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str cart_id: The cart ID. (required)
        :param Body72 body:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cart_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method quote_guest_payment_method_management_v1_set_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cart_id' is set
        if ('cart_id' not in params) or (params['cart_id'] is None):
            raise ValueError("Missing the required parameter `cart_id` when calling `quote_guest_payment_method_management_v1_set_put`")


        collection_formats = {}

        path_params = {}
        if 'cart_id' in params:
            path_params['cartId'] = params['cart_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/guest-carts/{cartId}/selected-payment-method', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='int',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)