"""
Network-free unit tests for the Peakflo update_purchase_order tool.

Covers the schema contract (required fields, replace semantics, shared
custom-field schema reuse) without requiring MCP or live credentials.
"""

import sys
import os

_SERVERS_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "src", "servers"
)
sys.path.insert(0, _SERVERS_PATH)

from peakflo.schemas.purchase_order import (
    update_purchase_order_schema,
    po_item_schema,
)
from peakflo.schemas.common import custom_field_schema


def test_schema_required_fields_match_api_contract():
    required = set(update_purchase_order_schema["required"])
    # API vendorPurchaseOrderSchema required set (minus tenantId, which is
    # popped before the request body is sent).
    expected = {
        "externalId",
        "POAmount",
        "currency",
        "issueDate",
        "dueDate",
        "status",
        "items",
        "PONumber",
        "vendorId",
        "tenantId",
    }
    assert expected <= required
    assert "additionalProperties" not in update_purchase_order_schema or (
        update_purchase_order_schema["additionalProperties"] is False
    )


def test_item_schema_required_fields():
    required = set(po_item_schema["required"])
    assert {"sourceId", "name", "quantity", "unitPrice"} <= required


def test_custom_field_reuses_shared_schema():
    # PO-level customField must reuse the shared common.custom_field_schema items
    po_cf = update_purchase_order_schema["properties"]["customField"]
    assert po_cf["items"] == custom_field_schema["items"]

    # line-item-level customField must also reuse it
    line_cf = po_item_schema["properties"]["customField"]
    assert line_cf["items"] == custom_field_schema["items"]


def test_custom_field_required_keys():
    items = update_purchase_order_schema["properties"]["customField"]["items"]
    assert set(items.get("required", [])) >= {"customFieldNumber", "value"}
