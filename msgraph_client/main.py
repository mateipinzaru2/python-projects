import asyncio
import csv
import datetime
import os

from user_service import get_user_pages
from mfa_service import get_mfa_pages


os.makedirs("output", exist_ok=True)
now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"output/graphsdk_output_{now_str}.csv"


async def process_data():
    mfa_pages = await get_mfa_pages()
    mfa_dict = {}
    if mfa_pages:
        for mfas in mfa_pages:
            if mfas and mfas.value:
                for mfa in mfas.value:
                    mfa_dict[mfa.id] = "Yes" if mfa.is_mfa_registered else "No"

    users_pages = await get_user_pages()
    if users_pages:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                [
                    "User Principal Name",
                    "MFA Registered",
                    "Last sign-in date and time",
                    "Entra Role Assignments",
                    "Entra Group Assignments",
                ]
            )
            for users in users_pages:
                if users and users.value:
                    for user in users.value:
                        groups = []
                        roles = []
                        if user.transitive_member_of:
                            for directory_object in user.transitive_member_of:
                                if (
                                    directory_object.odata_type
                                    == "#microsoft.graph.group"
                                ):
                                    groups.append(directory_object.display_name)
                                elif (
                                    directory_object.odata_type
                                    == "#microsoft.graph.directoryRole"
                                ):
                                    roles.append(directory_object.display_name)
                        sign_in_date = (
                            user.sign_in_activity.last_sign_in_date_time
                            if user.sign_in_activity
                            else "N/A"
                        )
                        mfa_registered = mfa_dict.get(user.id, "No")
                        writer.writerow(
                            [
                                user.user_principal_name,
                                mfa_registered,
                                sign_in_date,
                                ", ".join(roles) if roles else "N/A",
                                ", ".join(groups) if groups else "N/A",
                            ]
                        )


asyncio.run(process_data())
