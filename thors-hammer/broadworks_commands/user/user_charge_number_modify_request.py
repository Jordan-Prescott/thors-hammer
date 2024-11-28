from typing import Optional

from ..base_command import BroadworksCommand


class UserChargeNumberModifyRequest(BroadworksCommand):
    """
    Represents the `UserChargeNumberModifyRequest` command.

    This command modifies the charge number settings for a user.

    Args:
        user_id (str): The user ID associated with the charge number settings.
        service_provider_id (Optional[str]): The service provider ID.
        phone_number (Optional[str]): The charge phone number.
        use_charge_number_for_enhanced_translations (Optional[bool]): Whether to use the charge number for enhanced translations.
        send_charge_number_to_network (Optional[bool]): Whether to send the charge number to the network.
    """

    def __init__(
        self,
        user_id: str,
        service_provider_id: Optional[str] = None,
        phone_number: Optional[str] = None,
        use_charge_number_for_enhanced_translations: Optional[bool] = None,
        send_charge_number_to_network: Optional[bool] = None,
    ) -> None:
        super().__init__(
            "UserChargeNumberModifyRequest",
            user_id=user_id,
            service_provider_id=service_provider_id,
            phone_number=phone_number,
            use_charge_number_for_enhanced_translations=use_charge_number_for_enhanced_translations,
            send_charge_number_to_network=send_charge_number_to_network,
        )
