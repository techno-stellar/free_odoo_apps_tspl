Chatter Sidebar Right
=====================

Overview
--------

``chatter_sidebar_right_tspl`` keeps the backend chatter on the right side of
Odoo form views for users who enable the preference. It is useful when some
users prefer a consistent sidebar reading flow instead of having the chatter
move under the form when the browser zoom or viewport changes.

The module uses a focused compiler-level frontend override so the form renderer
and chatter container keep a stable side layout on medium and larger screens.

Features
--------

- Keeps chatter rendered on the right side on medium and larger backend layouts.
- Adds a per-user preference to enable or disable the right-side chatter lock.
- Uses a compiler-level layout override instead of relying only on CSS.
- Removes the alternate chatter clone that can move chatter below the form.

How It Works
------------

When Odoo compiles a backend form view with chatter, this module adjusts the
generated form structure before it is rendered:

- the form renderer keeps a row layout from medium screens and above
- the main chatter container is always treated as an aside panel
- the secondary in-sheet chatter clone is disabled
- attachment preview is hidden to avoid Odoo switching back to combo chatter layout

Technical Notes
---------------

- Built for Odoo 18 backend form views.
- Depends on ``mail``, and ``web``.
- Implemented through ``web.assets_backend``.
- The effective logic lives in ``static/src/js/form_compiler_patch.js``.
- The per-user preference is added on ``res.users`` and exposed through
  ``ir.http.session_info``.
- Styling is limited to ordering and sizing the form sheet and chatter columns.

Installation
------------

1. Place the module in your custom addons path.
2. Restart the Odoo server.
3. Update the Apps list.
4. Install the module ``Chatter Sidebar Right``.
5. Open a form view with chatter on a large screen to verify the right sidebar.

Usage
-----

1. Open user preferences and enable ``Lock Chatter on the Right``.
2. Reload the web client.
3. Open any mail-enabled form view in the backend.
4. Use a medium or larger layout in the browser.
5. Confirm that the chatter stays on the right side of the form.

Limitations
-----------

- The module targets backend form chatter only.
- Below medium screen width, the form can still stack vertically.
- Attachment preview inside the form is intentionally disabled to keep chatter
  fixed on the right side.

Version History
---------------

**18.0.1.0.0**

- Initial Odoo 18 release
- Added a per-user chatter lock preference on user settings
- Passed the user preference to the web client session
- Enabled the right-side chatter override only for opted-in users
- Added compiler-level right-side chatter enforcement
- Removed alternate chatter placement paths that caused bottom chatter fallback
