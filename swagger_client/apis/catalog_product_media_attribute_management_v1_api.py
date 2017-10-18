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


class CatalogProductMediaAttributeManagementV1Api(object):
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

    def catalog_product_media_attribute_management_v1_get_list_get(self, attribute_set_name, **kwargs):
        """
        Retrieve the list of media attributes (fronted input type is media_image) assigned to the given attribute set.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_media_attribute_management_v1_get_list_get(attribute_set_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str attribute_set_name: (required)
        :return: list[CatalogDataProductAttributeInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.catalog_product_media_attribute_management_v1_get_list_get_with_http_info(attribute_set_name, **kwargs)
        else:
            (data) = self.catalog_product_media_attribute_management_v1_get_list_get_with_http_info(attribute_set_name, **kwargs)
            return data

    def catalog_product_media_attribute_management_v1_get_list_get_with_http_info(self, attribute_set_name, **kwargs):
        """
        Retrieve the list of media attributes (fronted input type is media_image) assigned to the given attribute set.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.catalog_product_media_attribute_management_v1_get_list_get_with_http_info(attribute_set_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str attribute_set_name: (required)
        :return: list[CatalogDataProductAttributeInterface]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['attribute_set_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method catalog_product_media_attribute_management_v1_get_list_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'attribute_set_name' is set
        if ('attribute_set_name' not in params) or (params['attribute_set_name'] is None):
            raise ValueError("Missing the required parameter `attribute_set_name` when calling `catalog_product_media_attribute_management_v1_get_list_get`")


        collection_formats = {}

        path_params = {}
        if 'attribute_set_name' in params:
            path_params['attributeSetName'] = params['attribute_set_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/V1/products/media/types/{attributeSetName}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[CatalogDataProductAttributeInterface]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
