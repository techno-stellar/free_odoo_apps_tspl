from odoo import models
from odoo.exceptions import AccessError


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    def action_clear_chatter_messages(self):
        self.ensure_one()
        if not self.env.user.has_group("chatter_message_clear_tspl.group_chatter_message_clear"):
            raise AccessError(self.env._("You are not allowed to clear chatter messages."))
        messages = self.env["mail.message"].sudo().search([
            ("model", "=", self._name),
            ("res_id", "=", self.id),
            ("message_type", "!=", "user_notification"),
        ])
        deleted_count = len(messages)
        if messages:
            messages.unlink()
        return deleted_count
