def main(api, service_provider_id: str, group_id: str, alias: int):
    # logger = api.logger

    # utilise threading

    # 1. Fetch BREs
    group_aa_lst = api.raw_command(
        "GroupAutoAttendantGetInstanceListRequest",
        service_provider_id=service_provider_id,
        group_id=group_id,
    ).auto_attendant_table

    group_hg_lst = api.raw_command(
        "GroupHuntGroupGetInstanceListRequest",
        service_provider_id=service_provider_id,
        group_id=group_id,
    ).hunt_group_table

    group_cc_lst = api.raw_command(
        "GroupHuntGroupGetInstanceListRequest",
        service_provider_id=service_provider_id,
        group_id=group_id,
    )

    # GroupAutoAttendantGetInstanceRequest24 for single instances
    # GroupHuntGroupGetInstanceRequest20 for single instances
    # GroupCallCenterGetInstanceRequest22 for single instances

    # 4. Check BREs

    # 5. Fetch users

    # 6. Check users

    # 7. Return alias if found else return THAliasNotFound
