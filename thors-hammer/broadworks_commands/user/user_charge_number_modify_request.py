from ..base_command import BroadworksCommand


class UserChargeNumberModifyRequest(BroadworksCommand):
    """
    Represents the UserChargeNumberModifyRequest command.
    """

    def __init__(
        self,
        user_id: str,
        service_provider_id: str = None,
        phone_number: str = None,
        use_charge_number_for_enhanced_translations: bool = None,
        send_charge_number_to_network: bool = None,
    ):
        super().__init__(
            "UserChargeNumberModifyRequest",
            user_id=user_id,
            service_provider_id=service_provider_id,
            phone_number=phone_number,
            use_charge_number_for_enhanced_translations=use_charge_number_for_enhanced_translations,
            send_charge_number_to_network=send_charge_number_to_network,
        )
