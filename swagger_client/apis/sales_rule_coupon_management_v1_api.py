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


class SalesRuleCouponManagementV1Api(object):
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

    def sales_rule_coupon_management_v1_delete_by_codes_post(self, **kwargs):
        """
        Delete coupon by coupon codes.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sales_rule_coupon_management_v1_delete_by_codes_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Body129 body:
        :return: SalesRuleDataCouponMassDeleteResultInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sales_rule_coupon_management_v1_delete_by_codes_post_with_http_info(**kwargs)
        else:
            (data) = self.sales_rule_coupon_management_v1_delete_by_codes_post_with_http_info(**kwargs)
            return data

    def sales_rule_coupon_management_v1_delete_by_codes_post_with_http_info(self, **kwargs):
        """
        Delete coupon by coupon codes.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sales_rule_coupon_management_v1_delete_by_codes_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Body129 body:
        :return: SalesRuleDataCouponMassDeleteResultInterface
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
                    " to method sales_rule_coupon_management_v1_delete_by_codes_post" % key
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

        return self.api_client.call_api('/V1/coupons/deleteByCodes', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SalesRuleDataCouponMassDeleteResultInterface',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def sales_rule_coupon_management_v1_delete_by_ids_post(self, **kwargs):
        """
        Delete coupon by coupon ids.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sales_rule_coupon_management_v1_delete_by_ids_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Body128 body:
        :return: SalesRuleDataCouponMassDeleteResultInterface
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sales_rule_coupon_management_v1_delete_by_ids_post_with_http_info(**kwargs)
        else:
            (data) = self.sales_rule_coupon_management_v1_delete_by_ids_post_with_http_info(**kwargs)
            return data

    def sales_rule_coupon_management_v1_delete_by_ids_post_with_http_info(self, **kwargs):
        """
        Delete coupon by coupon ids.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sales_rule_coupon_management_v1_delete_by_ids_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Body128 body:
        :return: SalesRuleDataCouponMassDeleteResultInterface
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
                    " to method sales_rule_coupon_management_v1_delete_by_ids_post" % key
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

        return self.api_client.call_api('/V1/coupons/deleteByIds', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SalesRuleDataCouponMassDeleteResultInterface',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def sales_rule_coupon_management_v1_generate_post(self, **kwargs):
        """
        Generate coupon for a rule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sales_rule_coupon_management_v1_generate_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Body127 body:
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sales_rule_coupon_management_v1_generate_post_with_http_info(**kwargs)
        else:
            (data) = self.sales_rule_coupon_management_v1_generate_post_with_http_info(**kwargs)
            return data

    def sales_rule_coupon_management_v1_generate_post_with_http_info(self, **kwargs):
        """
        Generate coupon for a rule
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sales_rule_coupon_management_v1_generate_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Body127 body:
        :return: list[str]
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
                    " to method sales_rule_coupon_management_v1_generate_post" % key
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

        return self.api_client.call_api('/V1/coupons/generate', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[str]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
