#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#

from typing import Any, List, Mapping, Optional

import requests
from airbyte_cdk.sources.declarative.requesters.paginators.pagination_strategy import PaginationStrategy


class PageIncrement(PaginationStrategy):
    """
    Pagination strategy that returns the number of pages reads so far and returns it as the next page token
    """

    def __init__(self, page_size: int):
        self._page_size = page_size
        self._offset = 0

    def next_page_token(self, response: requests.Response, last_records: List[Mapping[str, Any]]) -> Optional[Any]:
        if len(last_records) < self._page_size:
            return None
        else:
            self._offset += 1
            return self._offset
