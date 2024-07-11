import helpers
from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings


VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@2.4.1/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.4.1/dist/flowbite.min.js",
}

STATICFILES_VENDORS_DIR = getattr(settings, 'STATICFILES_VENDORS_DIR')

# Command to download vendor static files 
class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files")

        # Check download completion
        completed_urls =[]

        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDORS_DIR / name
            dl_success = helpers.download_to_local(url, out_path)
            
            # Check if download complete
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f'Failed to download {url}')
                )

        # Check if all vendors files are downloaded
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                    self.style.SUCCESS('Successfully updated vendor static files.')
                )
        else:
            self.stdout.write(
                    self.style.WARNING('Some static files were not downloaded.')
                )