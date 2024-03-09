# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_subscription_timeline_list_get200_response import MerchantSubscriptionTimelineListGet200Response

class TestMerchantSubscriptionTimelineListGet200Response(unittest.TestCase):
    """MerchantSubscriptionTimelineListGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantSubscriptionTimelineListGet200Response:
        """Test MerchantSubscriptionTimelineListGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantSubscriptionTimelineListGet200Response`
        """
        model = MerchantSubscriptionTimelineListGet200Response()
        if include_optional:
            return MerchantSubscriptionTimelineListGet200Response(
                code = 56,
                data = openapi_client.models._merchant_subscription_timeline_list_get_200_response_data._merchant_subscription_timeline_list_get_200_response_data(
                    subscription_time_lines = [
                        openapi_client.models.unibee/internal/logic/gateway/ro/subscription_time_line_detail_vo.unibee.internal.logic.gateway.ro.SubscriptionTimeLineDetailVo(
                            addons = [
                                openapi_client.models.unibee/internal/logic/gateway/ro/plan_addon_vo.unibee.internal.logic.gateway.ro.PlanAddonVo(
                                    addon_plan = openapi_client.models.unibee/internal/logic/gateway/ro/plan_simplify.unibee.internal.logic.gateway.ro.PlanSimplify(
                                        amount = 56, 
                                        binding_addon_ids = '', 
                                        create_time = 56, 
                                        currency = '', 
                                        description = '', 
                                        extra_metric_data = '', 
                                        home_url = '', 
                                        id = 56, 
                                        image_url = '', 
                                        interval_count = 56, 
                                        interval_unit = '', 
                                        merchant_id = 56, 
                                        plan_name = '', 
                                        product_description = '', 
                                        product_name = '', 
                                        publish_status = 56, 
                                        status = 56, 
                                        tax_scale = 56, 
                                        type = 56, ), 
                                    quantity = 56, )
                                ], 
                            create_time = 56, 
                            currency = '', 
                            gateway_id = 56, 
                            invoice_id = '', 
                            merchant_id = 56, 
                            period_end = 56, 
                            period_end_time = '', 
                            period_start = 56, 
                            period_start_time = '', 
                            plan = openapi_client.models.unibee/internal/logic/gateway/ro/plan_simplify.unibee.internal.logic.gateway.ro.PlanSimplify(
                                amount = 56, 
                                binding_addon_ids = '', 
                                create_time = 56, 
                                currency = '', 
                                description = '', 
                                extra_metric_data = '', 
                                home_url = '', 
                                id = 56, 
                                image_url = '', 
                                interval_count = 56, 
                                interval_unit = '', 
                                merchant_id = 56, 
                                plan_name = '', 
                                product_description = '', 
                                product_name = '', 
                                publish_status = 56, 
                                status = 56, 
                                tax_scale = 56, 
                                type = 56, ), 
                            plan_id = 56, 
                            quantity = 56, 
                            subscription_id = '', 
                            unique_id = '', 
                            user_id = 56, )
                        ], ),
                message = '',
                redirect = '',
                request_id = ''
            )
        else:
            return MerchantSubscriptionTimelineListGet200Response(
        )
        """

    def testMerchantSubscriptionTimelineListGet200Response(self):
        """Test MerchantSubscriptionTimelineListGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
