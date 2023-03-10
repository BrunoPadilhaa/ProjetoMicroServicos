# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.get_telemetry_data_response import GetTelemetryDataResponse  # noqa: F401,E501
from swagger_server import util


class ListTelemetryDataResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, content: List[GetTelemetryDataResponse]=None, total_results: int=None):  # noqa: E501
        """ListTelemetryDataResponse - a model defined in Swagger

        :param content: The content of this ListTelemetryDataResponse.  # noqa: E501
        :type content: List[GetTelemetryDataResponse]
        :param total_results: The total_results of this ListTelemetryDataResponse.  # noqa: E501
        :type total_results: int
        """
        self.swagger_types = {
            'content': List[GetTelemetryDataResponse],
            'total_results': int
        }

        self.attribute_map = {
            'content': 'content',
            'total_results': 'totalResults'
        }
        self._content = content
        self._total_results = total_results

    @classmethod
    def from_dict(cls, dikt) -> 'ListTelemetryDataResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListTelemetryDataResponse of this ListTelemetryDataResponse.  # noqa: E501
        :rtype: ListTelemetryDataResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content(self) -> List[GetTelemetryDataResponse]:
        """Gets the content of this ListTelemetryDataResponse.

        list of paged items  # noqa: E501

        :return: The content of this ListTelemetryDataResponse.
        :rtype: List[GetTelemetryDataResponse]
        """
        return self._content

    @content.setter
    def content(self, content: List[GetTelemetryDataResponse]):
        """Sets the content of this ListTelemetryDataResponse.

        list of paged items  # noqa: E501

        :param content: The content of this ListTelemetryDataResponse.
        :type content: List[GetTelemetryDataResponse]
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def total_results(self) -> int:
        """Gets the total_results of this ListTelemetryDataResponse.

        total number of records  # noqa: E501

        :return: The total_results of this ListTelemetryDataResponse.
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results: int):
        """Sets the total_results of this ListTelemetryDataResponse.

        total number of records  # noqa: E501

        :param total_results: The total_results of this ListTelemetryDataResponse.
        :type total_results: int
        """
        if total_results is None:
            raise ValueError("Invalid value for `total_results`, must not be `None`")  # noqa: E501

        self._total_results = total_results
