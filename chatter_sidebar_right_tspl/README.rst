Chatter Sidebar Right
=====================

Overview
--------

``chatter_sidebar_right_tspl`` keeps the backend chatter on the right side of
Odoo form views. It is useful when users prefer a consistent sidebar reading
flow instead of having the chatter move under the form when the browser zoom or
viewport changes.

The module uses a focused compiler-level frontend override so the form renderer
and chatter container keep a stable side layout on medium and larger screens.

Features
--------

- Keeps chatter rendered on the right side on medium and larger backend layouts.
- Can be enabled per user from user preferences.
- Works as a backend web asset without adding models or settings.
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

- Built for Odoo 17 backend form views.
- Depends on ``mail`` and ``web`` only.
- Adds one boolean field on ``res.users`` to control the behavior per user.
- Implemented through ``web.assets_backend``.
- The effective logic lives in ``static/src/js/form_compiler_patch.js``.
- Styling is limited to ordering and sizing the form sheet and chatter columns.
- No Python business logic is added.
- No server-side data changes are introduced.

Installation
------------

1. Place the module in your custom addons path.
2. Restart the Odoo server.
3. Update the Apps list.
4. Install or upgrade the module ``Chatter Sidebar Right``.
5. Open the target user preferences and enable ``Lock Chatter on the Right``.
6. Reload the web client and open a form view with chatter on a large screen.

Usage
-----

1. Open any mail-enabled form view in the backend.
2. Use a medium or larger layout in the browser.
3. Confirm that the chatter stays on the right side only for users who enabled the preference.

Limitations
-----------

- The module targets backend form chatter only.
- Below medium screen width, the form can still stack vertically.
- Attachment preview inside the form is intentionally disabled to keep chatter
  fixed on the right side.

Version History
---------------

**17.0.1.0.0**

- Added a per-user preference to enable the right-side chatter lock
- Exposed the user preference to the web client session
- Added compiler-level right-side chatter enforcement
- Removed alternate chatter placement paths that caused bottom chatter fallback
