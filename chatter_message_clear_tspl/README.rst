Chatter Message Clear
=====================

Overview
--------

``chatter_message_clear`` adds a trash icon in the backend chatter of Odoo
records and allows authorized users to delete all chatter messages for the
current record after an explicit confirmation.

This module is designed for cases where a business wants controlled cleanup of
record discussions without giving that capability to every internal user.

Features
--------

- Adds a trash icon in the chatter top bar.
- Shows a confirmation dialog before deleting messages.
- Deletes all chatter messages linked to the current record.
- Restricts access through a dedicated security group.
- Hides the trash icon for users who do not have permission.

Security
--------

The module creates a dedicated group:

- ``Chatter Message Clear``

Only users assigned to this group can clear chatter messages.
The backend method also validates this group membership before deleting any
messages, so the action is not enforced only at the user interface level.

How It Works
------------

When an authorized user opens a record with chatter:

- a trash icon is shown in the chatter top bar
- clicking the icon opens a confirmation dialog
- confirming the action deletes all ``mail.message`` records related to that
  document, excluding ``user_notification`` messages
- the chatter view is refreshed immediately after deletion

Installation
------------

1. Place the module in your custom addons path.
2. Restart the Odoo server.
3. Update the Apps list.
4. Install the module ``Chatter Message Clear``.
5. Assign the ``Chatter Message Clear`` group to the users who should be
   allowed to delete chatter messages.

Usage
-----

1. Open any form view that contains chatter.
2. Verify that the current user belongs to the ``Chatter Message Clear`` group.
3. Click the trash icon in the chatter top bar.
4. Review the warning dialog.
5. Confirm the action to clear the chatter messages for that record.

Technical Notes
---------------

- Backend logic is implemented by extending ``mail.thread``.
- Frontend behavior is implemented by patching the Odoo chatter component.
- The delete action is limited to backend chatter usage.
- The action removes the message history for the current record only.

Files
-----

- ``models/mail_thread.py``: server-side delete logic and access checks
- ``security/chatter_message_clear_security.xml``: dedicated security group
- ``static/src/js/chatter_clear_patch.js``: chatter patch and confirmation flow
- ``static/src/xml/chatter_clear_button.xml``: trash icon injection in chatter

Version History
---------------

**17.0.1.0.0**

- Initial Odoo 17 release
- Added chatter trash icon for bulk message deletion
- Added confirmation dialog before deletion
- Added group-based access control
