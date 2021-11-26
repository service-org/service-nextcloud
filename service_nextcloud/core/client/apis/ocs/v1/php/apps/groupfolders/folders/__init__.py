#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

import typing as t

from logging import getLogger
from service_green.core.green import cjson
from service_client.core.client import BaseClientAPI
from service_nextcloud.exception import NextCloudError

from .groups import GroupsAPI

logger = getLogger(__name__)


class FoldersAPI(BaseClientAPI):
    """ Folders接口类 """

    groups = GroupsAPI()

    def list(self, **kwargs) -> t.Dict[t.Text, t.Any]:
        """ 列出所有组文件夹

        :param kwargs: 请求参数
        :return: t.Dict[t.Text, t.Any]
        """
        url = f'{self._base_url}/apps/groupfolders/folders'
        rsp = self._get(url, **kwargs)
        data = rsp.data.decode('utf-8')
        dict_data = cjson.loads(data)
        status = dict_data['ocs']['meta']['status']
        errors = dict_data['ocs']['meta']['message']
        if status != 'ok': raise NextCloudError(errors, original=url)
        return dict_data['ocs']['data']

    def set_quota(self, group_folder_id: int, **kwargs) -> t.Dict[t.Text, t.Any]:
        """ 设置组文件夹配额

        data = {'quota': 0}

        :param group_folder_id: 组文件夹id
        :return: t.Dict[t.Text, t.Any]
        """
        url = f'{self._base_url}/apps/groupfolders/folders/{group_folder_id}/quota'
        rsp = self._post(url, **kwargs)
        data = rsp.data.decode('utf-8')
        dict_data = cjson.loads(data)
        status = dict_data['ocs']['meta']['status']
        errors = dict_data['ocs']['meta']['message']
        if status != 'ok': raise NextCloudError(errors, original=url)
        return dict_data['ocs']['data']
