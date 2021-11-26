#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

from logging import getLogger
from service_client.core.client import BaseClientAPI

from .v1 import V1API

logger = getLogger(__name__)


class OcsAPI(BaseClientAPI):
    """ Ocs接口类 """

    v1 = V1API()
