# role_builder.py
class RoleBuilder:
    ROLES = ["UNDEFINED", "DEVELOPER", "TEST_ENGINEER", "SR_DEVELOPER", "DESIGNER"]

    @staticmethod
    def get_role_description(role_id):
        if role_id < 1 or role_id > 4:
            return "UNDEFINED"
        return RoleBuilder.ROLES[role_id]
