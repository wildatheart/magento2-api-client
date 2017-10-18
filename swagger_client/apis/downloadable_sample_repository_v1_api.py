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


class DownloadableSampleRepositoryV1Api(object):
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

    def downloadable_sample_repository_v1_delete_delete(self, id, **kwargs):
        """
        Delete downloadable sample
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.downloadable_sample_repository_v1_delete_delete(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.downloadable_sample_repository_v1_delete_delete_with_http_info(id, **kwargs)
        else:
            (data) = self.downloadable_sample_repository_v1_delete_delete_with_http_info(id, **kwargs)
            return data

    def downloadable_sample_repository_v1_delete_delete_with_http_info(self, id, **kwargs):
        """
        Delete downloadable sample
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.downloadable_sample_repository_v1_delete_delete_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id: (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method downloadable_sample_repository_v1_delete_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `downloadable_sample_repository_v1_delete_delete`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/products/downloadable-links/samples/{id}', 'DELETE',
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

    def downloadable_sample_repository_v1_get_list_get(self, sku, **kwargs):
        """
        List of samples for downloadable product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.downloadable_sample_repository_v1_get_list_get(sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :return: list[DownloadableDataSampleInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.downloadable_sample_repository_v1_get_list_get_with_http_info(sku, **kwargs)
        else:
            (data) = self.downloadable_sample_repository_v1_get_list_get_with_http_info(sku, **kwargs)
            return data

    def downloadable_sample_repository_v1_get_list_get_with_http_info(self, sku, **kwargs):
        """
        List of samples for downloadable product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.downloadable_sample_repository_v1_get_list_get_with_http_info(sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :return: list[DownloadableDataSampleInterface]
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
                    " to method downloadable_sample_repository_v1_get_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku' is set
        if ('sku' not in params) or (params['sku'] is None):
            raise ValueError("Missing the required parameter `sku` when calling `downloadable_sample_repository_v1_get_list_get`")


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

        return self.api_client.call_api('/V1/products/{sku}/downloadable-links/samples', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[DownloadableDataSampleInterface]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def downloadable_sample_repository_v1_save_post(self, sku, **kwargs):
        """
        Update downloadable sample of the given product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.downloadable_sample_repository_v1_save_post(sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param Body85 body:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.downloadable_sample_repository_v1_save_post_with_http_info(sku, **kwargs)
        else:
            (data) = self.downloadable_sample_repository_v1_save_post_with_http_info(sku, **kwargs)
            return data

    def downloadable_sample_repository_v1_save_post_with_http_info(self, sku, **kwargs):
        """
        Update downloadable sample of the given product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.downloadable_sample_repository_v1_save_post_with_http_info(sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param Body85 body:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sku', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method downloadable_sample_repository_v1_save_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku' is set
        if ('sku' not in params) or (params['sku'] is None):
            raise ValueError("Missing the required parameter `sku` when calling `downloadable_sample_repository_v1_save_post`")


        collection_formats = {}

        path_params = {}
        if 'sku' in params:
            path_params['sku'] = params['sku']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/products/{sku}/downloadable-links/samples', 'POST',
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

    def downloadable_sample_repository_v1_save_put(self, sku, id, **kwargs):
        """
        Update downloadable sample of the given product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.downloadable_sample_repository_v1_save_put(sku, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param str id: (required)
        :param Body86 body:
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.downloadable_sample_repository_v1_save_put_with_http_info(sku, id, **kwargs)
        else:
            (data) = self.downloadable_sample_repository_v1_save_put_with_http_info(sku, id, **kwargs)
            return data

    def downloadable_sample_repository_v1_save_put_with_http_info(self, sku, id, **kwargs):
        """
        Update downloadable sample of the given product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.downloadable_sample_repository_v1_save_put_with_http_info(sku, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param str id: (required)
        :param Body86 body:
        :return: int
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
                    " to method downloadable_sample_repository_v1_save_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku' is set
        if ('sku' not in params) or (params['sku'] is None):
            raise ValueError("Missing the required parameter `sku` when calling `downloadable_sample_repository_v1_save_put`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `downloadable_sample_repository_v1_save_put`")


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

        return self.api_client.call_api('/V1/products/{sku}/downloadable-links/samples/{id}', 'PUT',
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
