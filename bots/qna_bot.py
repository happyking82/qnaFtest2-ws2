# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import string
from typing import List
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from botbuilder.core import (
    ActivityHandler,
    TurnContext,
    ConversationState,
    UserState,
)
from botbuilder.dialogs import Dialog
from botbuilder.dialogs import DialogSet,WaterfallDialog,WaterfallStepContext
from botbuilder.schema import ChannelAccount

from helpers.dialog_helper import DialogHelper
from botbuilder.dialogs.prompts import TextPrompt,NumberPrompt,PromptOptions,PromptValidatorContext

client_answer = "question is \n"

class QnABot(ActivityHandler):

    def __init__(
        self,
        conversation_state: ConversationState,
        user_state: UserState,
        dialog: Dialog,
    ):
        self.conversation_state = conversation_state
        self.user_state = user_state
        self.dialog = dialog

    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)
        await self.conversation_state.save_changes(turn_context)
        await self.user_state.save_changes(turn_context)

    async def on_members_added_activity(
        self, members_added: List[ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
    async def send_message(self, turn_context2: string):
        host = "smtp.qq.com"
        mail_pass = "iaqfotkwamjhcaig"
        sender = '85157355@qq.com'
        receiver = '85157355@qq.com'
        content = "message content is " + turn_context2
        print(content)
        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = Header("ICT support", 'utf-8')
        message['To'] = Header("Lao Gao", 'utf-8')
        subject = 'testing message'
        message['Subject'] = Header(subject, "utf-8")
        smtpObj = smtplib.SMTP_SSL(host, 465)
        smtpObj.login(sender, mail_pass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        smtpObj.quit()
        print('done')
    #async def keep_conversation(self, turn_context3: TurnContext, message_content=None):
     #   await message_content += turn_context3.activity.text + "\n"
      #  return message_content



    async def on_message_activity(self, turn_context: TurnContext):
        global client_answer
        await DialogHelper.run_dialog(
            self.dialog,
            turn_context,
            self.conversation_state.create_property("DialogState"),
        )
        trigger_answer = "OK, Let us send a message to let IT support you."

        if trigger_answer != turn_context.activity.text:
            client_answer += turn_context.activity.text + "\n"
        else:
            await self.send_message(client_answer)
            await turn_context.send_activity("sent already")

    # async def GetMobileNumber(self,waterfall_step:WaterfallStepContext):
    #     name = waterfall_step._turn_context.activity.text
