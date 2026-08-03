from peakflo.schemas.common import custom_field_schema


po_item_schema = {
    "type": "object",
    "properties": {
        "itemId": {
            "type": "string",
            "description": "ID of the item",
        },
        "sourceId": {
            "type": "string",
            "description": "Unique identifier of line item, used in 3 Way Matching. For a given object there should be no 2 line items with same sourceId.",
        },
        "name": {
            "type": "string",
            "description": "Name of the item",
        },
        "unit": {
            "type": "string",
            "description": "Unit of measurement",
        },
        "description": {
            "type": "string",
            "description": "Description of the item",
        },
        "quantity": {
            "type": "number",
            "exclusiveMinimum": 0,
            "description": "Quantity of the item, must be a positive number (fractional quantities allowed)",
        },
        "unitPrice": {
            "type": "number",
            "description": "Price per unit of the item",
        },
        "accountId": {
            "type": "string",
            "description": "ID of the account associated with the item",
        },
        "currency": {
            "type": "string",
            "description": "Currency of the item",
        },
        "type": {
            "type": "string",
            "description": "Type of the item",
            "enum": [
                "None",
                "Product",
                "Service",
                "Hour",
                "Day",
                "Month",
                "Year",
                "Expense",
                "Shipping",
            ],
        },
        "wht": {
            "type": "object",
            "description": "Withholding tax details for the item",
        },
        "taxes": {
            "type": "array",
            "description": "Array of tax details for the item",
            "items": {"type": "object"},
        },
        "discounts": {
            "type": "array",
            "description": "Array of discount details for the item",
            "items": {"type": "object"},
        },
        "totalTax": {
            "type": "number",
            "description": "Total tax amount for the item",
        },
        "totalDiscount": {
            "type": "number",
            "description": "Total discount amount for the item",
        },
        "total": {
            "type": "number",
            "description": "Total amount for the item",
        },
        "customField": {
            "type": "array",
            "description": "Array of custom fields for the item",
            "items": custom_field_schema["items"],
        },
    },
    "required": ["sourceId", "name", "quantity", "unitPrice"],
}


update_purchase_order_schema = {
    "type": "object",
    "properties": {
        "externalId": {
            "type": "string",
            "description": "External ID of the purchase order to update",
        },
        "tenantId": {
            "type": "string",
            "description": "Tenant ID",
        },
        "totalAmount": {
            "type": "number",
            "description": "Total amount of the purchase order",
        },
        "POAmount": {
            "type": "number",
            "description": "Amount related to the purchase order",
        },
        "totalWHT": {
            "type": "number",
            "description": "Total withholding tax amount",
        },
        "currency": {
            "type": "string",
            "description": "Currency of the purchase order",
        },
        "issueDate": {
            "type": "string",
            "description": "Issue date of the purchase order (ISO8601 date format)",
        },
        "requestedBy": {
            "type": "string",
            "description": "Person who requested the purchase order",
        },
        "dueDate": {
            "type": "string",
            "description": "Due date of the purchase order (ISO8601 date format)",
        },
        "notes": {
            "type": "string",
            "description": "Notes related to the purchase order",
        },
        "deliveryInstructions": {
            "type": "string",
            "description": "Instructions for delivery",
        },
        "status": {
            "type": "string",
            "description": "Status value carried on the purchase order. Note: this endpoint does NOT transition PO status - status changes are handled by the dedicated PO status workflow. Provide the current status here as required by the validation contract; it will not be applied as a status change.",
        },
        "totalTax": {
            "type": "number",
            "description": "Total tax amount",
        },
        "fxRate": {
            "type": "number",
            "description": "Currency conversion rate",
        },
        "convertedAmount": {
            "type": "number",
            "description": "Converted amount in base currency",
        },
        "paymentTerms": {
            "type": "number",
            "description": "Payment terms in days",
        },
        "items": {
            "type": "array",
            "description": "List of items included in the purchase order",
            "items": po_item_schema,
        },
        "PONumber": {
            "type": "string",
            "description": "Purchase order number",
        },
        "PQNumber": {
            "type": "string",
            "description": "Purchase quote number",
        },
        "updatedAt": {
            "type": "string",
            "description": "Date when the purchase order was last updated (ISO8601 format)",
        },
        "vendorId": {
            "type": "string",
            "description": "ID of the vendor associated with the purchase order",
        },
        "vendorName": {
            "type": "string",
            "description": "Name of the vendor associated with the purchase order",
        },
        "receiptDate": {
            "type": "string",
            "description": "Date of purchase order receipt (ISO8601 format)",
        },
        "deliveryDate": {
            "type": "string",
            "description": "Date of expected delivery (ISO8601 format)",
        },
        "customField": {
            "type": "array",
            "description": "Array of custom fields. REPLACES the entire existing custom-field array (no merge) - include every custom field to preserve it; omitting this key keeps existing custom fields unchanged.",
            "items": custom_field_schema["items"],
        },
        "subsidiaryReference": {
            "type": "string",
            "description": "Subsidiary reference",
        },
    },
    "required": [
        "externalId",
        "tenantId",
        "POAmount",
        "currency",
        "issueDate",
        "dueDate",
        "status",
        "items",
        "PONumber",
        "vendorId",
    ],
    "additionalProperties": False,
}
