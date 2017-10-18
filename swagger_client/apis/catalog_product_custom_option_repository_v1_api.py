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


class CatalogProductCustomOptionRepositoryV1Api(object):
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

    def catalog_product_custom_option_repository_v1_delete_by_identifier_delete(self, sku, option_id, **kwargs):
        """
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_custom_option_repository_v1_delete_by_identifier_delete(sku, option_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param int option_id: (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.catalog_product_custom_option_repository_v1_delete_by_identifier_delete_with_http_info(sku, option_id, **kwargs)
        else:
            (data) = self.catalog_product_custom_option_repository_v1_delete_by_identifier_delete_with_http_info(sku, option_id, **kwargs)
            return data

    def catalog_product_custom_option_repository_v1_delete_by_identifier_delete_with_http_info(self, sku, option_id, **kwargs):
        """
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_custom_option_repository_v1_delete_by_identifier_delete_with_http_info(sku, option_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param int option_id: (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sku', 'option_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_product_custom_option_repository_v1_delete_by_identifier_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku' is set
        if ('sku' not in params) or (params['sku'] is None):
            raise ValueError("Missing the required parameter `sku` when calling `catalog_product_custom_option_repository_v1_delete_by_identifier_delete`")
        # verify the required parameter 'option_id' is set
        if ('option_id' not in params) or (params['option_id'] is None):
            raise ValueError("Missing the required parameter `option_id` when calling `catalog_product_custom_option_repository_v1_delete_by_identifier_delete`")


        collection_formats = {}

        path_params = {}
        if 'sku' in params:
            path_params['sku'] = params['sku']
        if 'option_id' in params:
            path_params['optionId'] = params['option_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/products/{sku}/options/{optionId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='bool',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def catalog_product_custom_option_repository_v1_get_get(self, sku, option_id, **kwargs):
        """
        Get custom option for a specific product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_custom_option_repository_v1_get_get(sku, option_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param int option_id: (required)
        :return: CatalogDataProductCustomOptionInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.catalog_product_custom_option_repository_v1_get_get_with_http_info(sku, option_id, **kwargs)
        else:
            (data) = self.catalog_product_custom_option_repository_v1_get_get_with_http_info(sku, option_id, **kwargs)
            return data

    def catalog_product_custom_option_repository_v1_get_get_with_http_info(self, sku, option_id, **kwargs):
        """
        Get custom option for a specific product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_custom_option_repository_v1_get_get_with_http_info(sku, option_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param int option_id: (required)
        :return: CatalogDataProductCustomOptionInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sku', 'option_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_product_custom_option_repository_v1_get_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku' is set
        if ('sku' not in params) or (params['sku'] is None):
            raise ValueError("Missing the required parameter `sku` when calling `catalog_product_custom_option_repository_v1_get_get`")
        # verify the required parameter 'option_id' is set
        if ('option_id' not in params) or (params['option_id'] is None):
            raise ValueError("Missing the required parameter `option_id` when calling `catalog_product_custom_option_repository_v1_get_get`")


        collection_formats = {}

        path_params = {}
        if 'sku' in params:
            path_params['sku'] = params['sku']
        if 'option_id' in params:
            path_params['optionId'] = params['option_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/products/{sku}/options/{optionId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CatalogDataProductCustomOptionInterface',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def catalog_product_custom_option_repository_v1_get_list_get(self, sku, **kwargs):
        """
        Get the list of custom options for a specific product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_custom_option_repository_v1_get_list_get(sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :return: list[CatalogDataProductCustomOptionInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.catalog_product_custom_option_repository_v1_get_list_get_with_http_info(sku, **kwargs)
        else:
            (data) = self.catalog_product_custom_option_repository_v1_get_list_get_with_http_info(sku, **kwargs)
            return data

    def catalog_product_custom_option_repository_v1_get_list_get_with_http_info(self, sku, **kwargs):
        """
        Get the list of custom options for a specific product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_custom_option_repository_v1_get_list_get_with_http_info(sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :return: list[CatalogDataProductCustomOptionInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sku']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_product_custom_option_repository_v1_get_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku' is set
        if ('sku' not in params) or (params['sku'] is None):
            raise ValueError("Missing the required parameter `sku` when calling `catalog_product_custom_option_repository_v1_get_list_get`")


        collection_formats = {}

        path_params = {}
        if 'sku' in params:
            path_params['sku'] = params['sku']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/products/{sku}/options', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[CatalogDataProductCustomOptionInterface]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def catalog_product_custom_option_repository_v1_save_post(self, **kwargs):
        """
        Save Custom Option
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_custom_option_repository_v1_save_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Body45 body:
        :return: CatalogDataProductCustomOptionInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.catalog_product_custom_option_repository_v1_save_post_with_http_info(**kwargs)
        else:
            (data) = self.catalog_product_custom_option_repository_v1_save_post_with_http_info(**kwargs)
            return data

    def catalog_product_custom_option_repository_v1_save_post_with_http_info(self, **kwargs):
        """
        Save Custom Option
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_custom_option_repository_v1_save_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Body45 body:
        :return: CatalogDataProductCustomOptionInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_product_custom_option_repository_v1_save_post" % key
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
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/products/options', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CatalogDataProductCustomOptionInterface',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def catalog_product_custom_option_repository_v1_save_put(self, option_id, **kwargs):
        """
        Save Custom Option
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_custom_option_repository_v1_save_put(option_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str option_id: (required)
        :param Body46 body:
        :return: CatalogDataProductCustomOptionInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.catalog_product_custom_option_repository_v1_save_put_with_http_info(option_id, **kwargs)
        else:
            (data) = self.catalog_product_custom_option_repository_v1_save_put_with_http_info(option_id, **kwargs)
            return data

    def catalog_product_custom_option_repository_v1_save_put_with_http_info(self, option_id, **kwargs):
        """
        Save Custom Option
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_custom_option_repository_v1_save_put_with_http_info(option_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str option_id: (required)
        :param Body46 body:
        :return: CatalogDataProductCustomOptionInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['option_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_product_custom_option_repository_v1_save_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'option_id' is set
        if ('option_id' not in params) or (params['option_id'] is None):
            raise ValueError("Missing the required parameter `option_id` when calling `catalog_product_custom_option_repository_v1_save_put`")


        collection_formats = {}

        path_params = {}
        if 'option_id' in params:
            path_params['optionId'] = params['option_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/products/options/{optionId}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CatalogDataProductCustomOptionInterface',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)