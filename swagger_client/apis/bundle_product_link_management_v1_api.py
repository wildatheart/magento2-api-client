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


class BundleProductLinkManagementV1Api(object):
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

    def bundle_product_link_management_v1_add_child_by_product_sku_post(self, sku, option_id, **kwargs):
        """
        Add child product to specified Bundle option by product sku
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.bundle_product_link_management_v1_add_child_by_product_sku_post(sku, option_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param int option_id: (required)
        :param Body79 body:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.bundle_product_link_management_v1_add_child_by_product_sku_post_with_http_info(sku, option_id, **kwargs)
        else:
            (data) = self.bundle_product_link_management_v1_add_child_by_product_sku_post_with_http_info(sku, option_id, **kwargs)
            return data

    def bundle_product_link_management_v1_add_child_by_product_sku_post_with_http_info(self, sku, option_id, **kwargs):
        """
        Add child product to specified Bundle option by product sku
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.bundle_product_link_management_v1_add_child_by_product_sku_post_with_http_info(sku, option_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param int option_id: (required)
        :param Body79 body:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sku', 'option_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bundle_product_link_management_v1_add_child_by_product_sku_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku' is set
        if ('sku' not in params) or (params['sku'] is None):
            raise ValueError("Missing the required parameter `sku` when calling `bundle_product_link_management_v1_add_child_by_product_sku_post`")
        # verify the required parameter 'option_id' is set
        if ('option_id' not in params) or (params['option_id'] is None):
            raise ValueError("Missing the required parameter `option_id` when calling `bundle_product_link_management_v1_add_child_by_product_sku_post`")


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
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/bundle-products/{sku}/links/{optionId}', 'POST',
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

    def bundle_product_link_management_v1_get_children_get(self, product_sku, **kwargs):
        """
        Get all children for Bundle product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.bundle_product_link_management_v1_get_children_get(product_sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str product_sku: (required)
        :param int option_id:
        :return: list[BundleDataLinkInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.bundle_product_link_management_v1_get_children_get_with_http_info(product_sku, **kwargs)
        else:
            (data) = self.bundle_product_link_management_v1_get_children_get_with_http_info(product_sku, **kwargs)
            return data

    def bundle_product_link_management_v1_get_children_get_with_http_info(self, product_sku, **kwargs):
        """
        Get all children for Bundle product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.bundle_product_link_management_v1_get_children_get_with_http_info(product_sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str product_sku: (required)
        :param int option_id:
        :return: list[BundleDataLinkInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_sku', 'option_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bundle_product_link_management_v1_get_children_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_sku' is set
        if ('product_sku' not in params) or (params['product_sku'] is None):
            raise ValueError("Missing the required parameter `product_sku` when calling `bundle_product_link_management_v1_get_children_get`")


        collection_formats = {}

        path_params = {}
        if 'product_sku' in params:
            path_params['productSku'] = params['product_sku']

        query_params = []
        if 'option_id' in params:
            query_params.append(('optionId', params['option_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/bundle-products/{productSku}/children', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[BundleDataLinkInterface]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def bundle_product_link_management_v1_remove_child_delete(self, sku, option_id, child_sku, **kwargs):
        """
        Remove product from Bundle product option
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.bundle_product_link_management_v1_remove_child_delete(sku, option_id, child_sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param int option_id: (required)
        :param str child_sku: (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.bundle_product_link_management_v1_remove_child_delete_with_http_info(sku, option_id, child_sku, **kwargs)
        else:
            (data) = self.bundle_product_link_management_v1_remove_child_delete_with_http_info(sku, option_id, child_sku, **kwargs)
            return data

    def bundle_product_link_management_v1_remove_child_delete_with_http_info(self, sku, option_id, child_sku, **kwargs):
        """
        Remove product from Bundle product option
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.bundle_product_link_management_v1_remove_child_delete_with_http_info(sku, option_id, child_sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param int option_id: (required)
        :param str child_sku: (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sku', 'option_id', 'child_sku']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bundle_product_link_management_v1_remove_child_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku' is set
        if ('sku' not in params) or (params['sku'] is None):
            raise ValueError("Missing the required parameter `sku` when calling `bundle_product_link_management_v1_remove_child_delete`")
        # verify the required parameter 'option_id' is set
        if ('option_id' not in params) or (params['option_id'] is None):
            raise ValueError("Missing the required parameter `option_id` when calling `bundle_product_link_management_v1_remove_child_delete`")
        # verify the required parameter 'child_sku' is set
        if ('child_sku' not in params) or (params['child_sku'] is None):
            raise ValueError("Missing the required parameter `child_sku` when calling `bundle_product_link_management_v1_remove_child_delete`")


        collection_formats = {}

        path_params = {}
        if 'sku' in params:
            path_params['sku'] = params['sku']
        if 'option_id' in params:
            path_params['optionId'] = params['option_id']
        if 'child_sku' in params:
            path_params['childSku'] = params['child_sku']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/bundle-products/{sku}/options/{optionId}/children/{childSku}', 'DELETE',
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

    def bundle_product_link_management_v1_save_child_put(self, sku, id, **kwargs):
        """
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.bundle_product_link_management_v1_save_child_put(sku, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param str id: (required)
        :param Body80 body:
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.bundle_product_link_management_v1_save_child_put_with_http_info(sku, id, **kwargs)
        else:
            (data) = self.bundle_product_link_management_v1_save_child_put_with_http_info(sku, id, **kwargs)
            return data

    def bundle_product_link_management_v1_save_child_put_with_http_info(self, sku, id, **kwargs):
        """
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.bundle_product_link_management_v1_save_child_put_with_http_info(sku, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param str id: (required)
        :param Body80 body:
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sku', 'id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bundle_product_link_management_v1_save_child_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku' is set
        if ('sku' not in params) or (params['sku'] is None):
            raise ValueError("Missing the required parameter `sku` when calling `bundle_product_link_management_v1_save_child_put`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `bundle_product_link_management_v1_save_child_put`")


        collection_formats = {}

        path_params = {}
        if 'sku' in params:
            path_params['sku'] = params['sku']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/bundle-products/{sku}/links/{id}', 'PUT',
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