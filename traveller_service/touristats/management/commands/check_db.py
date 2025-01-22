from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Check database connection"

    def handle(self, *args, **options):
        self.stdout.write("Testing database connection...")

        try:
            db_conn = connections["default"]
            with db_conn.cursor() as cursor:
                cursor.execute("SELECT 1")
                row = cursor.fetchone()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Database connection successful! Test query returned: {row[0]}"
                    )
                )

                # Print connection info
                self.stdout.write(f"Connected to: {db_conn.settings_dict['NAME']}")
                self.stdout.write(f"Host: {db_conn.settings_dict['HOST']}")
                self.stdout.write(f"User: {db_conn.settings_dict['USER']}")

        except OperationalError as e:
            self.stdout.write(self.style.ERROR(f"Database connection failed! Error: {str(e)}"))
