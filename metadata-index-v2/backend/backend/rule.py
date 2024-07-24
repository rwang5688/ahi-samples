"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0

Generates EventBridge rule for the application.
"""

from constructs import Construct
import aws_cdk as cdk
from aws_cdk import (
    aws_events as events,
    aws_sqs as sqs,
    Duration as Duration,
)

class Rule(Construct):

    def __init__(self, scope: Construct, id: str, display_name: str, queue: sqs.Queue, dead_letter_queue: sqs.Queue, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # define rule
        self._rule = events.Rule(self, id,
            event_pattern=events.EventPattern(
                source=["aws.medical-imaging"]
            )
        )
        
        # add target
        