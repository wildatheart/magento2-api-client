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


class CatalogProductRepositoryV1Api(object):
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

    def catalog_product_repository_v1_delete_by_id_delete(self, sku, **kwargs):
        """
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_repository_v1_delete_by_id_delete(sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.catalog_product_repository_v1_delete_by_id_delete_with_http_info(sku, **kwargs)
        else:
            (data) = self.catalog_product_repository_v1_delete_by_id_delete_with_http_info(sku, **kwargs)
            return data

    def catalog_product_repository_v1_delete_by_id_delete_with_http_info(self, sku, **kwargs):
        """
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_repository_v1_delete_by_id_delete_with_http_info(sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :return: bool
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
                    " to method catalog_product_repository_v1_delete_by_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku' is set
        if ('sku' not in params) or (params['sku'] is None):
            raise ValueError("Missing the required parameter `sku` when calling `catalog_product_repository_v1_delete_by_id_delete`")


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

        return self.api_client.call_api('/V1/products/{sku}', 'DELETE',
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

    def catalog_product_repository_v1_get_get(self, sku, **kwargs):
        """
        Get info about product by product SKU
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_repository_v1_get_get(sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param bool edit_mode:
        :param int store_id:
        :param bool force_reload:
        :return: CatalogDataProductInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.catalog_product_repository_v1_get_get_with_http_info(sku, **kwargs)
        else:
            (data) = self.catalog_product_repository_v1_get_get_with_http_info(sku, **kwargs)
            return data

    def catalog_product_repository_v1_get_get_with_http_info(self, sku, **kwargs):
        """
        Get info about product by product SKU
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_repository_v1_get_get_with_http_info(sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param bool edit_mode:
        :param int store_id:
        :param bool force_reload:
        :return: CatalogDataProductInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sku', 'edit_mode', 'store_id', 'force_reload']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_product_repository_v1_get_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku' is set
        if ('sku' not in params) or (params['sku'] is None):
            raise ValueError("Missing the required parameter `sku` when calling `catalog_product_repository_v1_get_get`")


        collection_formats = {}

        path_params = {}
        if 'sku' in params:
            path_params['sku'] = params['sku']

        query_params = []
        if 'edit_mode' in params:
            query_params.append(('editMode', params['edit_mode']))
        if 'store_id' in params:
            query_params.append(('storeId', params['store_id']))
        if 'force_reload' in params:
            query_params.append(('forceReload', params['force_reload']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/products/{sku}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CatalogDataProductInterface',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def catalog_product_repository_v1_get_list_get(self, **kwargs):
        """
        Get product list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_repository_v1_get_list_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search_criteria_filter_groups_filters_field: Field
        :param str search_criteria_filter_groups_filters_value: Value
        :param str search_criteria_filter_groups_filters_condition_type: Condition type
        :param str search_criteria_sort_orders_field: Sorting field.
        :param str search_criteria_sort_orders_direction: Sorting direction.
        :param int search_criteria_page_size: Page size.
        :param int search_criteria_current_page: Current page.
        :return: CatalogDataProductSearchResultsInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.catalog_product_repository_v1_get_list_get_with_http_info(**kwargs)
        else:
            (data) = self.catalog_product_repository_v1_get_list_get_with_http_info(**kwargs)
            return data

    def catalog_product_repository_v1_get_list_get_with_http_info(self, **kwargs):
        """
        Get product list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_repository_v1_get_list_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search_criteria_filter_groups_filters_field: Field
        :param str search_criteria_filter_groups_filters_value: Value
        :param str search_criteria_filter_groups_filters_condition_type: Condition type
        :param str search_criteria_sort_orders_field: Sorting field.
        :param str search_criteria_sort_orders_direction: Sorting direction.
        :param int search_criteria_page_size: Page size.
        :param int search_criteria_current_page: Current page.
        :return: CatalogDataProductSearchResultsInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_criteria_filter_groups_filters_field', 'search_criteria_filter_groups_filters_value', 'search_criteria_filter_groups_filters_condition_type', 'search_criteria_sort_orders_field', 'search_criteria_sort_orders_direction', 'search_criteria_page_size', 'search_criteria_current_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_product_repository_v1_get_list_get" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_criteria_filter_groups_filters_field' in params:
            query_params.append(('searchCriteria[filterGroups][][filters][][field]', params['search_criteria_filter_groups_filters_field']))
        if 'search_criteria_filter_groups_filters_value' in params:
            query_params.append(('searchCriteria[filterGroups][][filters][][value]', params['search_criteria_filter_groups_filters_value']))
        if 'search_criteria_filter_groups_filters_condition_type' in params:
            query_params.append(('searchCriteria[filterGroups][][filters][][conditionType]', params['search_criteria_filter_groups_filters_condition_type']))
        if 'search_criteria_sort_orders_field' in params:
            query_params.append(('searchCriteria[sortOrders][][field]', params['search_criteria_sort_orders_field']))
        if 'search_criteria_sort_orders_direction' in params:
            query_params.append(('searchCriteria[sortOrders][][direction]', params['search_criteria_sort_orders_direction']))
        if 'search_criteria_page_size' in params:
            query_params.append(('searchCriteria[pageSize]', params['search_criteria_page_size']))
        if 'search_criteria_current_page' in params:
            query_params.append(('searchCriteria[currentPage]', params['search_criteria_current_page']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/products', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CatalogDataProductSearchResultsInterface',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def catalog_product_repository_v1_save_post(self, **kwargs):
        """
        Create product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_repository_v1_save_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Body18 body:
        :return: CatalogDataProductInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.catalog_product_repository_v1_save_post_with_http_info(**kwargs)
        else:
            (data) = self.catalog_product_repository_v1_save_post_with_http_info(**kwargs)
            return data

    def catalog_product_repository_v1_save_post_with_http_info(self, **kwargs):
        """
        Create product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_repository_v1_save_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Body18 body:
        :return: CatalogDataProductInterface
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
                    " to method catalog_product_repository_v1_save_post" % key
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

        return self.api_client.call_api('/V1/products', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CatalogDataProductInterface',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def catalog_product_repository_v1_save_put(self, sku, **kwargs):
        """
        Create product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_repository_v1_save_put(sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param Body19 body:
        :return: CatalogDataProductInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.catalog_product_repository_v1_save_put_with_http_info(sku, **kwargs)
        else:
            (data) = self.catalog_product_repository_v1_save_put_with_http_info(sku, **kwargs)
            return data

    def catalog_product_repository_v1_save_put_with_http_info(self, sku, **kwargs):
        """
        Create product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_repository_v1_save_put_with_http_info(sku, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sku: (required)
        :param Body19 body:
        :return: CatalogDataProductInterface
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
                    " to method catalog_product_repository_v1_save_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sku' is set
        if ('sku' not in params) or (params['sku'] is None):
            raise ValueError("Missing the required parameter `sku` when calling `catalog_product_repository_v1_save_put`")


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

        return self.api_client.call_api('/V1/products/{sku}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='CatalogDataProductInterface',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
