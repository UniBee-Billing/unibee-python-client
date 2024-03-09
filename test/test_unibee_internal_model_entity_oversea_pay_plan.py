# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_internal_model_entity_oversea_pay_plan import UnibeeInternalModelEntityOverseaPayPlan

class TestUnibeeInternalModelEntityOverseaPayPlan(unittest.TestCase):
    """UnibeeInternalModelEntityOverseaPayPlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeInternalModelEntityOverseaPayPlan:
        """Test UnibeeInternalModelEntityOverseaPayPlan
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeInternalModelEntityOverseaPayPlan`
        """
        model = UnibeeInternalModelEntityOverseaPayPlan()
        if include_optional:
            return UnibeeInternalModelEntityOverseaPayPlan(
                amount = 56,
                binding_addon_ids = '',
                company_id = 56,
                create_time = 56,
                currency = '',
                description = '',
                extra_metric_data = '',
                gateway_product_description = '',
                gateway_product_name = '',
                gmt_create = '',
                gmt_modify = '',
                home_url = '',
                id = 56,
                image_url = '',
                interval_count = 56,
                interval_unit = '',
                is_deleted = 56,
                merchant_id = 56,
                plan_name = '',
                publish_status = 56,
                status = 56,
                tax_inclusive = 56,
                tax_scale = 56,
                type = 56
            )
        else:
            return UnibeeInternalModelEntityOverseaPayPlan(
        )
        """

    def testUnibeeInternalModelEntityOverseaPayPlan(self):
        """Test UnibeeInternalModelEntityOverseaPayPlan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
