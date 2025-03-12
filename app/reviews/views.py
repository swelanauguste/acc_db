import os
import sqlite3
import subprocess
from urllib.parse import urlencode
import pandas as pd
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, TemplateView
from django.db.models import Q
from .models import Exemptions, HPlates
from .tasks import download_file, export_to_sqlite


def export_to_sqlite(request):
    """Exports ACCDB tables to SQLite upon user request."""

    db = os.path.join(settings.BASE_DIR, "static/db/data.accdb")

    if not os.path.exists(db):
        messages.error(
            request, "Error: The ACCDB file does not exist. Please download it first."
        )
        return redirect("/")

    tables = {
        "hplates": "h plates",
        "exemptions": "exemptions",
    }

    conn = sqlite3.connect(os.path.join(settings.BASE_DIR, "db.sqlite3"))

    for table_name, access_table in tables.items():
        csv_file = f"static/csv/{table_name}.csv"
        export_command = f"mdb-export {db} '{access_table}' > {csv_file}"

        result = subprocess.run(
            export_command, shell=True, capture_output=True, text=True
        )

        if result.returncode == 0:
            df = pd.read_csv(csv_file)
            df.to_sql(table_name, conn, if_exists="replace", index=False)
        else:
            messages.error(request, f"Error exporting {access_table}: {result.stderr}")

    conn.close()
    messages.success(request, "Data successfully imported into SQLite.")
    return redirect("/")


def download_file(request):
    """Downloads the ACCDB file from the SMB server upon user request."""

    server = "//10.137.8.9/cworks"
    username = "cworks"
    password = "password3"
    remote_path = "cto_support/TRANSPORT SECRETARY/CORRESPONDENCE_DATABASE_TRANSPORT.accdb"
    local_path = os.path.join(settings.BASE_DIR, "static/db/data.accdb")

    command = f'smbclient "{server}" -U "{username}%{password}" -c "get \\"{remote_path}\\" {local_path}"'

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            messages.success(request, "Database file downloaded successfully.")
        else:
            messages.error(request, f"Error downloading file: {result.stderr}")
            return redirect("/")

    except Exception as e:
        messages.error(request, f"Exception: {str(e)}")
        return redirect("/")

    return redirect("export_to_sqlite")  # Redirect to next step


def index(request):
    return render(request, "reviews/index.html")


class HPplateListView(ListView):
    model = HPlates
    paginate_by = 20
    
    def get_queryset(self):
        queryset = self.model.objects.all()
        
        query = self.request.GET.get("query")

        if query:
             queryset = queryset.filter(
                    Q(applicant_s_name__icontains=query)
                    | Q(primary_contact_number__icontains=query)
                    | Q(registration_number__icontains=query)
                    | Q(vehicle_model_man__icontains=query)
                    | Q(chassis_vin_number__icontains=query)
                    | Q(action_taken__icontains=query)
                    | Q(status__icontains=query)
                    | Q(secondary_contact__icontains=query)
                )
        return queryset
    
        # Preserve query parameters for pagination
        query_params = self.request.GET.copy()
        if "page" in query_params:
            query_params.pop(
                "page"
            )  # Remove 'page' from query parameters to prevent duplication
        context["query_params"] = urlencode(query_params)

        return context

class HPplatesDetailView(DetailView):
    model = HPlates


class ExemptionListView(ListView):
    model = Exemptions
    paginate_by = 20

    
    def get_queryset(self):
        queryset = self.model.objects.all()
        
        query = self.request.GET.get("query")

        if query:
             queryset = queryset.filter(
                    Q(name_of_applicant__icontains=query)
                    | Q(type_of_exemption__icontains=query)
                    | Q(telephone_no_1__icontains=query)
                    | Q(telephone_no_2__icontains=query)
                    | Q(email__icontains=query)
                    | Q(status_1__icontains=query)
                    | Q(date_of_status_update__icontains=query)
                    | Q(notes__icontains=query)
                    | Q(comments__icontains=query)
                    | Q(comments__icontains=query)
                    | Q(comments__icontains=query)
                )
        return queryset
    
        # Preserve query parameters for pagination
        query_params = self.request.GET.copy()
        if "page" in query_params:
            query_params.pop(
                "page"
            )  # Remove 'page' from query parameters to prevent duplication
        context["query_params"] = urlencode(query_params)

        return context


class ExemptionDetailView(DetailView):
    model = Exemptions
