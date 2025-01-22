from datetime import datetime
from typing import Dict, List, Optional


def verified_model(
    description: str,
    version: Optional[str] = "1.0.0",
    verified_by: str = None,
    verification_type: str = "initial",
):
    """Decorator to mark a model as verified and track its version history.

    Args:
        description (str): Description of the model version or verification
        version (str, optional): Version number. Defaults to "1.0.0"
        verified_by (str, optional): Name or ID of the verifier
        verification_type (str, optional): Type of verification (initial/review/audit)
    """

    def decorator(cls):
        if not hasattr(cls, "_model_history"):
            cls._model_history = []

        if not hasattr(cls, "_verifications"):
            cls._verifications = {}

        version_key = version
        verification_info = {
            "verified_by": verified_by,
            "verification_type": verification_type,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": description,
        }

        # Add verification to the version
        if version_key not in cls._verifications:
            cls._verifications[version_key] = []
        cls._verifications[version_key].append(verification_info)

        # Only add to model history if it's a new version
        if not cls._model_history or cls._model_history[-1]["version"] != version:
            version_info = {
                "version": version,
                "initial_description": description,
                "created_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "fields": {f.name: f.get_internal_type() for f in cls._meta.fields},
            }
            cls._model_history.append(version_info)

        @classmethod
        def get_version_history(model_cls) -> List[Dict]:
            """Get the complete version history of the model."""
            return model_cls._model_history

        @classmethod
        def get_verifications(model_cls, version: str = None) -> Dict:
            """Get verifications for all versions or a specific version."""
            if version:
                return model_cls._verifications.get(version, [])
            return model_cls._verifications

        @classmethod
        def print_version_history(model_cls):
            """Print the version history with all verifications."""
            for version in model_cls._model_history:
                print(f"\nVersion: {version['version']}")
                print(f"Created: {version['created_date']}")
                print(f"Initial Description: {version['initial_description']}")
                print("\nFields:")
                for field_name, field_type in version["fields"].items():
                    print(f"  - {field_name}: {field_type}")

                print("\nVerifications:")
                verifications = model_cls._verifications.get(version["version"], [])
                for idx, v in enumerate(verifications, 1):
                    print(f"  {idx}. Date: {v['date']}")
                    print(f"     Type: {v['verification_type']}")
                    print(f"     By: {v['verified_by']}")
                    print(f"     Notes: {v['description']}")
                print("-" * 50)

        cls.get_version_history = get_version_history
        cls.get_verifications = get_verifications
        cls.print_version_history = print_version_history

        return cls

    return decorator
