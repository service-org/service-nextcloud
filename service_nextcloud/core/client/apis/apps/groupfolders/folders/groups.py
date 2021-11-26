#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

import typing as t

from logging import getLogger
from service_green.core.green import cjson
from service_client.core.client import BaseClientAPI
from service_nextcloud.exception import NextCloudError

logger = getLogger(__name__)


class GroupsAPI(BaseClientAPI):
    """ Groups接口类 """

    def set_permissions(self, group_folder_id: int, group_name, **kwargs) -> t.Dict[t.Text, t.Any]:
        """ 设置组文件夹对应组权限

        data = {'permissions': 31}

        :param group_folder_id: 组文件夹id
        :param group_name: 组名称, 唯一标识
        :param kwargs: 请求参数
        :return: t.Dict[t.Text, t.Any]
        """
        url = f'{self._base_url}/apps/groupfolders/folders/{group_folder_id}/groups/{group_name}'
        rsp = self._post(url, **kwargs)
        data = rsp.data.decode('utf-8')
        dict_data = cjson.loads(data)
        status = dict_data['ocs']['meta']['status']
        errors = dict_data['ocs']['meta']['message']
        if status != 'ok': raise NextCloudError(errors, original=url)
        return dict_data['ocs']['data']
