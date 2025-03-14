uv run ./manage.py createsuperuser --no-input

python manage.py migrate

# uv run ./manage.py startapp users                      
# uv run ./manage.py startapp hplates                      
# uv run ./manage.py startapp exemptions                      
# uv run ./manage.py startapp affidavits                    
# uv run ./manage.py startapp book_records                      
# uv run ./manage.py startapp customs     
# uv run ./manage.py startapp disabled_parking
# uv run ./manage.py startapp incoming_correspondences
# uv run ./manage.py startapp cancelled_insurance_policies
# uv run ./manage.py startapp invoices_payments           
# uv run ./manage.py startapp minibus_records  
# uv run ./manage.py startapp outgoing_correspondences
# uv run ./manage.py startapp personalized_number_plates
# uv run ./manage.py startapp special_permits




# uv run ./manage.py inspectdb hplates > ./hplates/models.py
# uv run ./manage.py inspectdb exemptions > ./exemptions/models.py
# uv run ./manage.py inspectdb affidavits > ./affidavits/models.py
# uv run ./manage.py inspectdb book_records > ./book_records/models.py
# uv run ./manage.py inspectdb customs > ./customs/models.py
# uv run ./manage.py inspectdb disabled_parking > ./disabled_parking/models.py
# uv run ./manage.py inspectdb incoming_correspondences > ./incoming_correspondences/models.py
# uv run ./manage.py inspectdb cancelled_insurance_policies > ./cancelled_insurance_policies/models.py
# uv run ./manage.py inspectdb invoices_payments > ./invoices_payments/models.py
# uv run ./manage.py inspectdb minibus_records > ./minibus_records/models.py
# uv run ./manage.py inspectdb outgoing_correspondences > ./outgoing_correspondences/models.py
# uv run ./manage.py inspectdb personalized_number_plates > ./personalized_number_plates/models.py
# uv run ./manage.py inspectdb special_permits > ./special_permits/models.py

