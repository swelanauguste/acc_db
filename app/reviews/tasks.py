import sqlite3
import subprocess

import pandas as pd
from django.contrib import messages


def export_to_sqlite():

    db = "static/db/data.accdb"

    export_hplates = f"mdb-export {db} 'h plates' > hplates.csv"
    export_hplates_result = subprocess.run(
        export_hplates, shell=True, capture_output=True, text=True
    )

    conn = sqlite3.connect("db.sqlite3")
    df = pd.read_csv("hplates.csv")
    df.to_sql("hplates", conn, if_exists="replace", index=False)
    conn.close()

    export_exemptions = f"mdb-export {db} 'exemptions' > exemptions.csv"
    export_exemptions_result = subprocess.run(
        export_exemptions, shell=True, capture_output=True, text=True
    )

    conn = sqlite3.connect("db.sqlite3")
    df = pd.read_csv("exemptions.csv")
    df.to_sql("exemptions", conn, if_exists="replace", index=False)
    conn.close()


# subprocess.run("./manage.py inspectdb 'h-plates' 'exemptions' > core/models.py ", shell=True)


def download_file(request):

    # SMB connection details
    server = "//10.137.8.9/cworks"
    username = "cworks"
    password = "password3"
    remote_path = "cto_support/TRANSPORT SECRETARY/data.accdb"
    local_path = "static/db/data.accdb"

    # Construct the smbclient command
    command = f'smbclient "{server}" -U "{username}%{password}" -c "get \\"{remote_path}\\" {local_path}"'

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check for errors
        if result.returncode == 0:
            # print(f"File downloaded successfully to {local_path}")
            messages.success(request, "Database file downloaded successfully.")
        else:
            # print(f"Error downloading file: {result.stderr}")
            messages.error(request, f"Error downloading file: {result.stderr}")
            return redirect("/")
    except Exception as e:
        # print(f"Exception occurred: {e}")
        messages.error(request, f"Exception: {str(e)}")
        return redirect("/")