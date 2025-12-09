from tinydb import TinyDB, Query


class UserProfileDBManager:
    """Manage user profiles stored in a TinyDB table named 'profiles'.

    Each profile document contains the fields: name, email, title, profession.
    """

    def __init__(self, db_path: str = "email_system.json"):
        """Initialize the TinyDB database and the `profiles` table.

        Args:
            db_path: Path to the TinyDB JSON database file.
        """
        self.db = TinyDB(db_path)
        self.table = self.db.table("profiles")
        # templates table stores documents with fields: name, body
        self.templates = self.db.table("templates")
        # user_profiles stores operator profiles with required and optional fields
        self.user_profiles = self.db.table("user_profiles")

    def create_profile(self, name: str, email: str, title: str, profession: str) -> dict:
        """Insert a new profile into the 'profiles' table.

        Raises a ValueError if a profile with the same email already exists.
        Returns the inserted document (as a dict).
        """
        Q = Query()
        if self.table.contains(Q.email == email):
            raise ValueError(f"Profile with email '{email}' already exists")

        doc = {"name": name, "email": email, "title": title, "profession": profession}
        self.table.insert(doc)
        return doc

    def get_profile_by_email(self, email: str) -> dict | None:
        """Retrieve a single profile document by email.

        Returns the profile dict, or None if not found.
        """
        Q = Query()
        return self.table.get(Q.email == email)

    def delete_profile_by_email(self, email: str) -> bool:
        """Delete a profile by email.

        Returns True if a profile was deleted, False if no matching profile existed.
        """
        Q = Query()
        if not self.table.contains(Q.email == email):
            return False
        self.table.remove(Q.email == email)
        return True

    def get_all_profiles(self) -> list:
        """Return a list of all profile documents in the table."""
        return self.table.all()

    # --- Templates table management ---
    def create_template(self, name: str, body: str) -> dict:
        """Insert a new template into the 'templates' table.

        Raises a ValueError if a template with the same name already exists.
        Returns the inserted document (as a dict).
        """
        Q = Query()
        if self.templates.contains(Q.name == name):
            raise ValueError(f"Template with name '{name}' already exists")

        doc = {"name": name, "body": body}
        self.templates.insert(doc)
        return doc

    def get_template_by_name(self, name: str) -> dict | None:
        """Retrieve a single template document by name.

        Returns the template dict, or None if not found.
        """
        Q = Query()
        return self.templates.get(Q.name == name)

    def delete_template_by_name(self, name: str) -> bool:
        """Delete a template by name.

        Returns True if a template was deleted, False if no matching template existed.
        """
        Q = Query()
        if not self.templates.contains(Q.name == name):
            return False
        self.templates.remove(Q.name == name)
        return True

    def list_all_templates(self) -> list:
        """Return a list of all template documents in the table."""
        return self.templates.all()

    # --- User profiles (operators) table management ---
    def create_user_profile(self, name: str, degree: str, profession: str, university: str, **optional_fields) -> dict:
        """Insert a new user profile into the 'user_profiles' table.

        Required fields: name, degree, profession, university.
        Optional fields (supported): linkedin, github, x, personal_website, email, signature.
        Optional fields default to empty string if not provided.

        If an `email` is provided it must be unique across `user_profiles`.
        """
        Q = Query()
        optional_keys = {"linkedin", "github", "x", "personal_website", "email", "signature"}

        doc = {
            "name": name,
            "degree": degree,
            "profession": profession,
            "university": university,
        }

        # Populate optional fields with provided values or default to empty string
        for key in optional_keys:
            doc[key] = optional_fields.get(key, "")

        # If email provided, enforce uniqueness
        email = doc.get("email", "")
        if email:
            if self.user_profiles.contains(Q.email == email):
                raise ValueError(f"User profile with email '{email}' already exists")

        self.user_profiles.insert(doc)
        return doc

    def get_user_profile_by_email(self, email: str) -> dict | None:
        """Retrieve a single user profile by email.

        Returns the profile dict, or None if not found.
        """
        Q = Query()
        return self.user_profiles.get(Q.email == email)

    def delete_user_profile_by_email(self, email: str) -> bool:
        """Delete a user profile by email.

        Returns True if a profile was deleted, False if no matching profile existed.
        """
        Q = Query()
        if not self.user_profiles.contains(Q.email == email):
            return False
        self.user_profiles.remove(Q.email == email)
        return True

    def list_all_user_profiles(self) -> list:
        """Return a list of all user profile documents in the table."""
        return self.user_profiles.all()

    def close(self) -> None:
        """Close the underlying TinyDB database."""
        try:
            self.db.close()
        except Exception:
            pass


if __name__ == "__main__":
    # Example usage of UserProfileDBManager
    manager = UserProfileDBManager(db_path="email_system.json")

    # Create profiles (handle duplicates)
    try:
        p1 = manager.create_profile(
            name="Alice Example",
            email="alice@example.com",
            title="Senior Engineer",
            profession="Software Engineering",
        )
        print("Created:", p1)
    except ValueError as e:
        print("Create error:", e)

    try:
        p2 = manager.create_profile(
            name="Bob Example",
            email="bob@example.com",
            title="Product Manager",
            profession="Product",
        )
        print("Created:", p2)
    except ValueError as e:
        print("Create error:", e)

    # Retrieve a profile by email
    found = manager.get_profile_by_email("alice@example.com")
    print("Found by email:", found)

    # List all profiles
    all_profiles = manager.get_all_profiles()
    print("All profiles:")
    for p in all_profiles:
        print(" -", p)

    # Delete a profile
    deleted = manager.delete_profile_by_email("bob@example.com")
    print("Deleted bob@example.com:", deleted)

    # Verify deletion
    print("All profiles after deletion:", manager.get_all_profiles())

    # --- Templates example usage ---
    try:
        t1 = manager.create_template(
            name="Welcome",
            body="Hello {name},\nWelcome to our service!",
        )
        print("Created template:", t1)
    except ValueError as e:
        print("Create template error:", e)

    try:
        t2 = manager.create_template(
            name="PasswordReset",
            body="Hi {name},\nUse this token to reset your password: {token}",
        )
        print("Created template:", t2)
    except ValueError as e:
        print("Create template error:", e)

    # Retrieve a template by name
    found_t = manager.get_template_by_name("Welcome")
    print("Found template:", found_t)

    # List all templates
    print("All templates:")
    for t in manager.list_all_templates():
        print(" -", t)

    # Delete a template
    deleted_t = manager.delete_template_by_name("PasswordReset")
    print("Deleted PasswordReset:", deleted_t)

    # Verify templates after deletion
    print("All templates after deletion:", manager.list_all_templates())

    # --- User profiles (operators) example usage ---
    try:
        up1 = manager.create_user_profile(
            name="Carol Admin",
            degree="MSc Computer Science",
            profession="Administrator",
            university="State University",
            email="carol@company.com",
            linkedin="https://linkedin.com/in/carol",
            github="carolgit",
        )
        print("Created user profile:", up1)
    except ValueError as e:
        print("Create user profile error:", e)

    # Create a user profile without optional social/contact fields
    up2 = manager.create_user_profile(
        name="Dave Operator",
        degree="BSc Information Systems",
        profession="Operator",
        university="Tech Institute",
    )
    print("Created user profile without optional fields:", up2)

    # Retrieve a user profile by email
    found_up = manager.get_user_profile_by_email("carol@company.com")
    print("Found user profile:", found_up)

    # List all user profiles
    print("All user profiles:")
    for u in manager.list_all_user_profiles():
        print(" -", u)

    # Delete a user profile
    deleted_up = manager.delete_user_profile_by_email("carol@company.com")
    print("Deleted carol@company.com:", deleted_up)

    # Verify deletion
    print("All user profiles after deletion:", manager.list_all_user_profiles())

    manager.close()
