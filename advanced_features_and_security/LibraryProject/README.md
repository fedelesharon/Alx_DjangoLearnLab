# README.md
Sharon MUINGO
# Django Permissions and Groups Implementation

This project demonstrates how to implement and manage user permissions and groups within a Django application.

## Custom Permissions
- `can_view`: Permission to view books.
- `can_create`: Permission to create books.
- `can_edit`: Permission to edit books.
- `can_delete`: Permission to delete books.

## Groups
- **Viewers**: Can only view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Can view, create, edit, and delete books.

## Views
Permissions are enforced using the `@permission_required` decorator, ensuring that users can only access views based on their assigned permissions.

## How to Test
1. Create users and assign them to the appropriate groups in Django Admin.
2. Log in as the user and attempt to access different views to test permissions.
