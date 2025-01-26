from django.core.management.base import BaseCommand
from touristats.models import AllCountryStats, TimeFrame


class Command(BaseCommand):
    """Delete all data from AllCountryStats and related TimeFrames.

    This command allows you to delete data from the AllCountryStats model and its
    related TimeFrames. You can delete all data or specify a particular year.
    A confirmation prompt is shown by default but can be bypassed using --confirm.

    Examples:
        Delete all data:
            >>> python manage.py allcountrystats_delete_data

        Delete data for a specific year:
            >>> python manage.py allcountrystats_delete_data --year 2023

        Delete data for a specific year (with confirmation):
            >>> python manage.py allcountrystats_delete_data --year 2023 --confirm

        Delete all data (with confirmation):
            >>> python manage.py allcountrystats_delete_data --confirm

    Args:
        --year (int, optional): Specific year to delete data from.
        --confirm (bool, optional): Skip confirmation prompt if provided.

    Returns:
        None. Prints success or cancellation message to stdout.
    """

    help = "Delete all data from AllCountryStats and related TimeFrames"

    def add_arguments(self, parser):
        parser.add_argument(
            "--year", type=int, help="Specific year to delete data from (optional)", required=False
        )
        parser.add_argument(
            "--confirm",
            action="store_true",
            help="Confirm deletion without prompting",
        )

    def handle(self, *args, **options):
        year = options.get("year")
        confirm = options.get("confirm")

        if year:
            message = f"This will delete all data for year {year}"
            queryset = AllCountryStats.objects.filter(timeframe__year=year)
        else:
            message = "This will delete ALL data from AllCountryStats"
            queryset = AllCountryStats.objects.all()

        # Count records that will be deleted
        count = queryset.count()
        message += f" ({count} records)"

        # If not pre-confirmed, ask for confirmation
        if not confirm:
            self.stdout.write(message)
            user_input = input("Are you sure you want to proceed? (yes/no): ")
            if user_input.lower() != "yes":
                self.stdout.write(self.style.WARNING("Operation cancelled."))
                return

        # Delete the records
        queryset.delete()

        # Clean up orphaned TimeFrames
        if year:
            TimeFrame.objects.filter(year=year, allcountrystats__isnull=True).delete()
        else:
            TimeFrame.objects.filter(allcountrystats__isnull=True).delete()

        self.stdout.write(self.style.SUCCESS(f"Successfully deleted {count} records!"))
