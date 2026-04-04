/* @odoo-module */

import { Chatter } from "@mail/core/web/chatter";

import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";

patch(Chatter.prototype, {
    setup() {
        super.setup(...arguments);
        this.dialogService = useService("dialog");
        this.notificationService = useService("notification");
        this.orm = useService("orm");
        this.userService = useService("user");
        this.canClearChatterMessages = false;
        this._initClearChatterAccess();
    },

    async _initClearChatterAccess() {
        this.canClearChatterMessages = await this.userService.hasGroup(
            "chatter_message_clear_tspl.group_chatter_message_clear"
        );
    },

    async onClickClearChatterMessages() {
        const thread = this.state.thread;
        if (!thread?.id || !this.canClearChatterMessages) {
            return;
        }
        this.dialogService.add(ConfirmationDialog, {
            title: _t("Clear Chatter"),
            body: _t("This will permanently delete all messages from this chatter. This action cannot be undone."),
            confirmLabel: _t("Clear"),
            confirmClass: "btn-danger",
            confirm: async () => {
                const deletedCount = await this.orm.call(
                    thread.model,
                    "action_clear_chatter_messages",
                    [[thread.id]]
                );
                this.state.composerType = false;
                for (const message of [...thread.messages]) {
                    message.delete();
                }
                thread.pendingNewMessages = [];
                this.load(thread, ["messages"]);
                this.notificationService.add(
                    deletedCount
                        ? _t("Chatter messages cleared.")
                        : _t("There were no chatter messages to clear."),
                    { type: deletedCount ? "success" : "warning" }
                );
            },
        });
    },
});
