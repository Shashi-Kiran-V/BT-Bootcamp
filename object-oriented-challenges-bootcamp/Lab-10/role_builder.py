class RoleBuilder:
    """
    Private data member
    """
    ROLES = ["UNDEFINED", "DEVELOPER", "TEST_ENGINEER", "SR_DEVELOPER", "DESIGNER"]

    """
    Method to get role description for a given role id
    """
    @staticmethod
    def get_role_description(role_id):
        if role_id <1 or role_id>4:
            return RoleBuilder.ROLES[0]
        return RoleBuilder.ROLES[role_id]
