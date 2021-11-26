#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

from logging import getLogger
from service_client.core.client import BaseClientAPI

from .groupfolders import GroupFoldersAPI

logger = getLogger(__name__)


class AppsAPI(BaseClientAPI):
    """ Apps接口类 """

    groupfolders = GroupFoldersAPI()
