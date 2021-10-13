#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "cfa7be14-4ea7-4e57-80a6-556caf517d46")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "dd9a36d3-a20a-4b4e-bcad-0d73e347bb27")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://qnaftest-ws2.azurewebsites.net/qnamaker")
