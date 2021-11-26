#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

from logging import getLogger
from service_client.core.client import BaseClientAPI

from .apps import AppsAPI

logger = getLogger(__name__)


class PhpAPI(BaseClientAPI):
    """ Php接口类 """

    apps = AppsAPI()
