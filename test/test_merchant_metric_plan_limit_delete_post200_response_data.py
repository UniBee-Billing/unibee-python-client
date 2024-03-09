# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_metric_plan_limit_delete_post200_response_data import MerchantMetricPlanLimitDeletePost200ResponseData

class TestMerchantMetricPlanLimitDeletePost200ResponseData(unittest.TestCase):
    """MerchantMetricPlanLimitDeletePost200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantMetricPlanLimitDeletePost200ResponseData:
        """Test MerchantMetricPlanLimitDeletePost200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantMetricPlanLimitDeletePost200ResponseData`
        """
        model = MerchantMetricPlanLimitDeletePost200ResponseData()
        if include_optional:
            return MerchantMetricPlanLimitDeletePost200ResponseData(
                merchant_metric_plan_limit = openapi_client.models.unibee/internal/logic/gateway/ro/merchant_metric_plan_limit_vo.unibee.internal.logic.gateway.ro.MerchantMetricPlanLimitVo(
                    create_time = 56, 
                    gmt_modify = 56, 
                    id = 56, 
                    merchant_id = 56, 
                    merchant_metric_vo = openapi_client.models.unibee/internal/logic/gateway/ro/merchant_metric_vo.unibee.internal.logic.gateway.ro.MerchantMetricVo(
                        aggregation_property = '', 
                        aggregation_type = 56, 
                        code = '', 
                        create_time = 56, 
                        gmt_modify = 56, 
                        id = 56, 
                        merchant_id = 56, 
                        metric_description = '', 
                        metric_name = '', 
                        type = 56, ), 
                    metric_id = 56, 
                    metric_limit = 56, 
                    plan_id = 56, )
            )
        else:
            return MerchantMetricPlanLimitDeletePost200ResponseData(
        )
        """

    def testMerchantMetricPlanLimitDeletePost200ResponseData(self):
        """Test MerchantMetricPlanLimitDeletePost200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
