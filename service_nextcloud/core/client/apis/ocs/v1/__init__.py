#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

from logging import getLogger
from service_client.core.client import BaseClientAPI

from .php import PhpAPI

logger = getLogger(__name__)


class V1API(BaseClientAPI):
    """ V1接口类 """

    php = PhpAPI()
