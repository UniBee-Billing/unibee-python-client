# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_subscription_detail_get200_response_data import MerchantSubscriptionDetailGet200ResponseData

class TestMerchantSubscriptionDetailGet200ResponseData(unittest.TestCase):
    """MerchantSubscriptionDetailGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantSubscriptionDetailGet200ResponseData:
        """Test MerchantSubscriptionDetailGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantSubscriptionDetailGet200ResponseData`
        """
        model = MerchantSubscriptionDetailGet200ResponseData()
        if include_optional:
            return MerchantSubscriptionDetailGet200ResponseData(
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
                gateway = openapi_client.models.unibee/internal/logic/gateway/ro/gateway_simplify.unibee.internal.logic.gateway.ro.GatewaySimplify(
                    gateway_id = 56, 
                    gateway_logo = '', 
                    gateway_name = '', ),
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
                subscription = openapi_client.models.unibee/internal/logic/gateway/ro/subscription_simplify.unibee.internal.logic.gateway.ro.SubscriptionSimplify(
                    addon_data = '', 
                    amount = 56, 
                    billing_cycle_anchor = 56, 
                    cancel_at_period_end = 56, 
                    cancel_reason = '', 
                    country_code = '', 
                    create_time = 56, 
                    currency = '', 
                    current_period_end = 56, 
                    current_period_start = 56, 
                    dunning_time = 56, 
                    first_paid_time = 56, 
                    gateway_id = 56, 
                    gateway_item_data = '', 
                    gateway_status = '', 
                    id = 56, 
                    last_update_time = 56, 
                    latest_invoice_id = '', 
                    link = '', 
                    merchant_id = 56, 
                    pending_update_id = '', 
                    plan_id = 56, 
                    quantity = 56, 
                    return_url = '', 
                    status = 56, 
                    subscription_id = '', 
                    task_time = '', 
                    tax_scale = 56, 
                    test_clock = 56, 
                    trial_end = 56, 
                    type = 56, 
                    user_id = 56, 
                    vat_number = '', ),
                unfinished_subscription_pending_update = openapi_client.models.unibee/internal/logic/gateway/ro/subscription_pending_update_detail_vo.unibee.internal.logic.gateway.ro.SubscriptionPendingUpdateDetailVo(
                    addon_data = '', 
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
                    amount = 56, 
                    currency = '', 
                    effect_immediate = 56, 
                    effect_time = 56, 
                    gateway_id = 56, 
                    gmt_create = '', 
                    gmt_modify = '', 
                    link = '', 
                    merchant_id = 56, 
                    merchant_member = openapi_client.models.unibee/internal/logic/gateway/ro/merchant_member_simplify.unibee.internal.logic.gateway.ro.MerchantMemberSimplify(
                        create_time = 56, 
                        email = '', 
                        first_name = '', 
                        id = 56, 
                        last_name = '', 
                        merchant_id = 56, ), 
                    note = '', 
                    paid = 56, 
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
                    proration_amount = 56, 
                    quantity = 56, 
                    status = 56, 
                    subscription_id = '', 
                    update_addon_data = '', 
                    update_addons = [
                        openapi_client.models.unibee/internal/logic/gateway/ro/plan_addon_vo.unibee.internal.logic.gateway.ro.PlanAddonVo(
                            quantity = 56, )
                        ], 
                    update_amount = 56, 
                    update_currency = '', 
                    update_plan = , 
                    update_plan_id = 56, 
                    update_quantity = 56, 
                    update_subscription_id = '', 
                    user_id = 56, ),
                user = openapi_client.models.unibee/internal/logic/gateway/ro/user_account_simplify.unibee.internal.logic.gateway.ro.UserAccountSimplify(
                    address = '', 
                    create_time = 56, 
                    email = '', 
                    external_user_id = '', 
                    first_name = '', 
                    id = 56, 
                    last_name = '', 
                    merchant_id = 56, )
            )
        else:
            return MerchantSubscriptionDetailGet200ResponseData(
        )
        """

    def testMerchantSubscriptionDetailGet200ResponseData(self):
        """Test MerchantSubscriptionDetailGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
