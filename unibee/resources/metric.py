# coding: utf-8
"""
Metric Resource

Provides methods for managing billable metrics.
"""

from typing import Any, Dict, List, Optional

from openapi_client import ApiClient
from openapi_client.api.metric import Metric as MetricApi
from openapi_client.rest import ApiException

from unibee.resources.base import BaseResource


class MetricResource(BaseResource):
    """Billable metric management."""
    
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)
        self._api = MetricApi(api_client)
    
    def list(self, **kwargs) -> Any:
        """List all metrics."""
        try:
            response = self._api.metric_list_get()
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def get(self, metric_id: int, **kwargs) -> Any:
        """Get metric details."""
        from openapi_client.models.unibee_api_merchant_metric_detail_req import (
            UnibeeApiMerchantMetricDetailReq
        )
        try:
            req = UnibeeApiMerchantMetricDetailReq(metric_id=metric_id)
            response = self._api.metric_detail_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def create(
        self,
        metric_name: str,
        code: str,
        metric_type: int,
        aggregation_type: int,
        **kwargs
    ) -> Any:
        """
        Create a new metric.
        
        Args:
            metric_name: Metric name
            code: Unique metric code
            metric_type: Type of metric
            aggregation_type: How to aggregate values
        """
        from openapi_client.models.unibee_api_merchant_metric_new_req import (
            UnibeeApiMerchantMetricNewReq
        )
        try:
            req = UnibeeApiMerchantMetricNewReq(
                metric_name=metric_name,
                code=code,
                type=metric_type,
                aggregation_type=aggregation_type,
            )
            response = self._api.metric_new_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def edit(self, metric_id: int, metric_name: Optional[str] = None, **kwargs) -> Any:
        """Edit a metric."""
        from openapi_client.models.unibee_api_merchant_metric_edit_req import (
            UnibeeApiMerchantMetricEditReq
        )
        try:
            req = UnibeeApiMerchantMetricEditReq(
                metric_id=metric_id, metric_name=metric_name
            )
            response = self._api.metric_edit_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def delete(self, metric_id: int, **kwargs) -> Any:
        """Delete a metric."""
        from openapi_client.models.unibee_api_merchant_metric_delete_req import (
            UnibeeApiMerchantMetricDeleteReq
        )
        try:
            req = UnibeeApiMerchantMetricDeleteReq(metric_id=metric_id)
            response = self._api.metric_delete_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
    
    def new_event(
        self,
        metric_code: str,
        external_user_id: str,
        metric_value: int,
        **kwargs
    ) -> Any:
        """Record a new metric event."""
        from openapi_client.models.unibee_api_merchant_metric_new_event_req import (
            UnibeeApiMerchantMetricNewEventReq
        )
        try:
            req = UnibeeApiMerchantMetricNewEventReq(
                metric_code=metric_code,
                external_user_id=external_user_id,
                metric_value=metric_value,
            )
            response = self._api.metric_event_new_post(req)
            return self._extract_data(response)
        except ApiException as e:
            self._handle_api_exception(e)
