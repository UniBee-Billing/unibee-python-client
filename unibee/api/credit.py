# coding: utf-8
"""
UniBee Credit API

Manage credits and promo credits.
"""

from typing import Any, Dict, Optional

from unibee.api.base import BaseAPI


class CreditAPI(BaseAPI):
    """
    API for managing credits and promo credits.
    
    Example:
        ```python
        from unibee import UniBeeClient
        
        client = UniBeeClient(api_key="your-api-key")
        
        # Get promo credit config
        config = client.credit.get_promo_config()
        
        # Add promo credit to a user
        client.credit.add_promo_credit(
            user_id=123,
            amount=1000,  # $10.00
            description="Welcome bonus",
        )
        ```
    """
    
    # Credit Config
    def list_configs(self) -> Dict[str, Any]:
        """
        List credit configurations.
        
        Returns:
            List of credit configurations.
        """
        return self._get("/merchant/credit/config_list")
    
    def setup_config(
        self,
        currency: str,
        exchange_rate: int,
        name: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Setup a new credit configuration.
        
        Args:
            currency: Currency code.
            exchange_rate: Exchange rate (credits per currency unit).
            name: Credit configuration name.
            description: Description.
            **kwargs: Additional parameters.
        
        Returns:
            Created credit configuration.
        """
        data = {
            "currency": currency,
            "exchangeRate": exchange_rate,
            "name": name,
            "description": description,
            **kwargs,
        }
        return self._post("/merchant/credit/config_new", data=data)
    
    def edit_config(
        self,
        config_id: int,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Edit a credit configuration.
        
        Args:
            config_id: The configuration ID.
            **kwargs: Parameters to update.
        
        Returns:
            Updated credit configuration.
        """
        data = {
            "id": config_id,
            **kwargs,
        }
        return self._post("/merchant/credit/config_edit", data=data)
    
    # Credit Accounts
    def list_accounts(
        self,
        user_id: Optional[int] = None,
        page: int = 0,
        count: int = 20,
    ) -> Dict[str, Any]:
        """
        List credit accounts.
        
        Args:
            user_id: Filter by user ID.
            page: Page number (0-indexed).
            count: Number of results per page.
        
        Returns:
            List of credit accounts.
        """
        return self._get(
            "/merchant/credit/account_list",
            params={
                "userId": user_id,
                "page": page,
                "count": count,
            },
        )
    
    def get_account(
        self,
        user_id: int,
    ) -> Dict[str, Any]:
        """
        Get user credit account details.
        
        Args:
            user_id: The user ID.
        
        Returns:
            Credit account details.
        """
        return self._get(
            "/merchant/credit/account_detail",
            params={"userId": user_id},
        )
    
    # Credit Transactions
    def list_transactions(
        self,
        user_id: Optional[int] = None,
        page: int = 0,
        count: int = 20,
    ) -> Dict[str, Any]:
        """
        List credit transactions.
        
        Args:
            user_id: Filter by user ID.
            page: Page number (0-indexed).
            count: Number of results per page.
        
        Returns:
            List of credit transactions.
        """
        return self._post(
            "/merchant/credit/transaction_list",
            data={
                "userId": user_id,
                "page": page,
                "count": count,
            },
        )
    
    def recharge(
        self,
        user_id: int,
        amount: int,
        currency: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Recharge/add credits to a user account.
        
        Args:
            user_id: The user ID.
            amount: Amount in smallest currency unit.
            currency: Currency code.
            name: Transaction name.
            description: Transaction description.
            **kwargs: Additional parameters.
        
        Returns:
            Recharge result.
        """
        data = {
            "userId": user_id,
            "amount": amount,
            "currency": currency,
            "name": name,
            "description": description,
            **kwargs,
        }
        return self._post("/merchant/credit/recharge", data=data)
    
    # Promo Credits
    def get_promo_config(self) -> Dict[str, Any]:
        """
        Get promo credit configuration.
        
        Returns:
            Promo credit configuration.
        """
        return self._get("/merchant/promo_credit/config")
    
    def edit_promo_config(
        self,
        **config,
    ) -> Dict[str, Any]:
        """
        Edit promo credit configuration.
        
        Args:
            **config: Configuration parameters.
        
        Returns:
            Updated promo credit configuration.
        """
        return self._post("/merchant/promo_credit/config_edit", data=config)
    
    def get_promo_stats(self) -> Dict[str, Any]:
        """
        Get promo credit statistics.
        
        Returns:
            Promo credit statistics.
        """
        return self._get("/merchant/promo_credit/statistics")
    
    def add_promo_credit(
        self,
        user_id: int,
        amount: int,
        currency: str,
        description: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Add promo credit to a user.
        
        Args:
            user_id: The user ID.
            amount: Amount in smallest currency unit.
            currency: Currency code.
            description: Description for the credit.
            **kwargs: Additional parameters.
        
        Returns:
            Updated promo credit balance.
        """
        data = {
            "userId": user_id,
            "amount": amount,
            "currency": currency,
            "description": description,
            **kwargs,
        }
        return self._post("/merchant/promo_credit/increment", data=data)
    
    def deduct_promo_credit(
        self,
        user_id: int,
        amount: int,
        currency: str,
        description: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Deduct promo credit from a user.
        
        Args:
            user_id: The user ID.
            amount: Amount in smallest currency unit.
            currency: Currency code.
            description: Description for the deduction.
            **kwargs: Additional parameters.
        
        Returns:
            Updated promo credit balance.
        """
        data = {
            "userId": user_id,
            "amount": amount,
            "currency": currency,
            "description": description,
            **kwargs,
        }
        return self._post("/merchant/promo_credit/decrement", data=data)
    
    def refund_promo_credit(
        self,
        user_id: int,
        amount: int,
        currency: str,
        transaction_id: str,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Refund promo credit to a user.
        
        Args:
            user_id: The user ID.
            amount: Amount to refund.
            currency: Currency code.
            transaction_id: Original transaction ID.
            **kwargs: Additional parameters.
        
        Returns:
            Refund result.
        """
        data = {
            "userId": user_id,
            "amount": amount,
            "currency": currency,
            "transactionId": transaction_id,
            **kwargs,
        }
        return self._post("/merchant/promo_credit/refund", data=data)
