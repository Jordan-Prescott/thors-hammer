from typing import Optional, Any
from .base_command import BroadworksCommand


class UserChargeNumberModifyRequest(BroadworksCommand):
    """
    Represents the `UserChargeNumberModifyRequest` command.

    Modifies the charge number settings for a user.

    Args:
        user_id (str): The user ID associated with the charge number settings.
        service_provider_id (Optional[str]): The service provider ID.
        phone_number (Optional[str]): The charge phone number.
        use_charge_number_for_enhanced_translations (Optional[bool]): Whether to use the charge number for enhanced translations.
        send_charge_number_to_network (Optional[bool]): Whether to send the charge number to the network.
    """

    user_id: str
    service_provider_id: Optional[str] = None
    phone_number: Optional[str] = None
    use_charge_number_for_enhanced_translations: Optional[bool] = None
    send_charge_number_to_network: Optional[bool] = None

    def __init__(self, **data: Any):
        super().__init__(command="UserChargeNumberModifyRequest", **data)
