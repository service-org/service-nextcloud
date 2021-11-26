#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

import typing as t

from logging import getLogger
from urllib.parse import urlencode
from service_green.core.green import urllib3
from service_client.core.client import BaseClient

from .apis.apps import AppsAPI

logger = getLogger(__name__)


class NextCloudClient(BaseClient):
    """ NextCloud通用连接类

    doc: https://github.com/matejak/nextcloud-API
    """

    apps = AppsAPI()

    def __init__(self, username: t.Text, password: t.Text, **kwargs: t.Any) -> None:
        """ 初始化实例

        :param username: 认证账户
        :param password: 认证密码
        :param kwargs: 其它参数
        """
        self.username = username
        self.password = password
        super(NextCloudClient, self).__init__(**kwargs)

    def request(self, method: t.Text, url: t.Text, **kwargs: t.Any) -> t.Any:
        """ 请求处理方法

        :param method: 请求方法
        :param url: 请求地址
        :param kwargs: 请求参数
        :return: t.Any
        """
        url = f'{url}?' + urlencode({'format': 'json'})
        if 'timeout' not in kwargs:
            kwargs['timeout'] = 2.0
        if 'retries' not in kwargs:
            kwargs['retries'] = 2
        headers = kwargs.setdefault('headers', {})
        headers['OCS-APIRequest'] = 'true'
        basic_auth = f'{self.username}:{self.password}'
        headers.update(
            urllib3.make_headers(basic_auth=basic_auth)
        )
        return super(NextCloudClient, self).request(method, url, **kwargs)
