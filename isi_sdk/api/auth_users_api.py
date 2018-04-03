# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 8.0
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from isi_sdk_8_0.api_client import ApiClient


class AuthUsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_user_member_of_item(self, user_member_of_item, user, **kwargs):  # noqa: E501
        """create_user_member_of_item  # noqa: E501

        Add the user to a group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_user_member_of_item(user_member_of_item, user, async=True)
        >>> result = thread.get()

        :param async bool
        :param GroupMember user_member_of_item: (required)
        :param str user: (required)
        :param str zone: Filter groups by zone.
        :param str provider: Filter groups by provider.
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_user_member_of_item_with_http_info(user_member_of_item, user, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_member_of_item_with_http_info(user_member_of_item, user, **kwargs)  # noqa: E501
            return data

    def create_user_member_of_item_with_http_info(self, user_member_of_item, user, **kwargs):  # noqa: E501
        """create_user_member_of_item  # noqa: E501

        Add the user to a group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_user_member_of_item_with_http_info(user_member_of_item, user, async=True)
        >>> result = thread.get()

        :param async bool
        :param GroupMember user_member_of_item: (required)
        :param str user: (required)
        :param str zone: Filter groups by zone.
        :param str provider: Filter groups by provider.
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_member_of_item', 'user', 'zone', 'provider']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user_member_of_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_member_of_item' is set
        if ('user_member_of_item' not in params or
                params['user_member_of_item'] is None):
            raise ValueError("Missing the required parameter `user_member_of_item` when calling `create_user_member_of_item`")  # noqa: E501
        # verify the required parameter 'user' is set
        if ('user' not in params or
                params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `create_user_member_of_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user' in params:
            path_params['User'] = params['user']  # noqa: E501

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501
        if 'provider' in params:
            query_params.append(('provider', params['provider']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_member_of_item' in params:
            body_params = params['user_member_of_item']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sessionAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/auth/users/{User}/member-of', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_user_member_of_member_of(self, user_member_of_member_of, user, **kwargs):  # noqa: E501
        """delete_user_member_of_member_of  # noqa: E501

        Remove the user from the group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_user_member_of_member_of(user_member_of_member_of, user, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_member_of_member_of: Remove the user from the group. (required)
        :param str user: (required)
        :param str zone: Filter groups by zone.
        :param str provider: Filter groups by provider.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_user_member_of_member_of_with_http_info(user_member_of_member_of, user, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_user_member_of_member_of_with_http_info(user_member_of_member_of, user, **kwargs)  # noqa: E501
            return data

    def delete_user_member_of_member_of_with_http_info(self, user_member_of_member_of, user, **kwargs):  # noqa: E501
        """delete_user_member_of_member_of  # noqa: E501

        Remove the user from the group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_user_member_of_member_of_with_http_info(user_member_of_member_of, user, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_member_of_member_of: Remove the user from the group. (required)
        :param str user: (required)
        :param str zone: Filter groups by zone.
        :param str provider: Filter groups by provider.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_member_of_member_of', 'user', 'zone', 'provider']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_member_of_member_of" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_member_of_member_of' is set
        if ('user_member_of_member_of' not in params or
                params['user_member_of_member_of'] is None):
            raise ValueError("Missing the required parameter `user_member_of_member_of` when calling `delete_user_member_of_member_of`")  # noqa: E501
        # verify the required parameter 'user' is set
        if ('user' not in params or
                params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `delete_user_member_of_member_of`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_member_of_member_of' in params:
            path_params['UserMemberOfMemberOf'] = params['user_member_of_member_of']  # noqa: E501
        if 'user' in params:
            path_params['User'] = params['user']  # noqa: E501

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501
        if 'provider' in params:
            query_params.append(('provider', params['provider']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sessionAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/auth/users/{User}/member-of/{UserMemberOfMemberOf}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_user_member_of(self, user, **kwargs):  # noqa: E501
        """list_user_member_of  # noqa: E501

        List all groups the user is a member of.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_user_member_of(user, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user: (required)
        :param bool resolve_names: Resolve names of personas.
        :param str zone: Filter groups by zone.
        :param str provider: Filter groups by provider.
        :return: UserMemberOf
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.list_user_member_of_with_http_info(user, **kwargs)  # noqa: E501
        else:
            (data) = self.list_user_member_of_with_http_info(user, **kwargs)  # noqa: E501
            return data

    def list_user_member_of_with_http_info(self, user, **kwargs):  # noqa: E501
        """list_user_member_of  # noqa: E501

        List all groups the user is a member of.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_user_member_of_with_http_info(user, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user: (required)
        :param bool resolve_names: Resolve names of personas.
        :param str zone: Filter groups by zone.
        :param str provider: Filter groups by provider.
        :return: UserMemberOf
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user', 'resolve_names', 'zone', 'provider']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_member_of" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user' is set
        if ('user' not in params or
                params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `list_user_member_of`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user' in params:
            path_params['User'] = params['user']  # noqa: E501

        query_params = []
        if 'resolve_names' in params:
            query_params.append(('resolve_names', params['resolve_names']))  # noqa: E501
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501
        if 'provider' in params:
            query_params.append(('provider', params['provider']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sessionAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/auth/users/{User}/member-of', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserMemberOf',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_user_change_password(self, user_change_password, user, **kwargs):  # noqa: E501
        """update_user_change_password  # noqa: E501

        Change the user's password.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_user_change_password(user_change_password, user, async=True)
        >>> result = thread.get()

        :param async bool
        :param UserChangePassword user_change_password: (required)
        :param str user: (required)
        :param str zone: Specifies access zone containing user.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_user_change_password_with_http_info(user_change_password, user, **kwargs)  # noqa: E501
        else:
            (data) = self.update_user_change_password_with_http_info(user_change_password, user, **kwargs)  # noqa: E501
            return data

    def update_user_change_password_with_http_info(self, user_change_password, user, **kwargs):  # noqa: E501
        """update_user_change_password  # noqa: E501

        Change the user's password.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_user_change_password_with_http_info(user_change_password, user, async=True)
        >>> result = thread.get()

        :param async bool
        :param UserChangePassword user_change_password: (required)
        :param str user: (required)
        :param str zone: Specifies access zone containing user.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_change_password', 'user', 'zone']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user_change_password" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_change_password' is set
        if ('user_change_password' not in params or
                params['user_change_password'] is None):
            raise ValueError("Missing the required parameter `user_change_password` when calling `update_user_change_password`")  # noqa: E501
        # verify the required parameter 'user' is set
        if ('user' not in params or
                params['user'] is None):
            raise ValueError("Missing the required parameter `user` when calling `update_user_change_password`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user' in params:
            path_params['User'] = params['user']  # noqa: E501

        query_params = []
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_change_password' in params:
            body_params = params['user_change_password']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['sessionAuth']  # noqa: E501

        return self.api_client.call_api(
            '/platform/3/auth/users/{User}/change-password', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
