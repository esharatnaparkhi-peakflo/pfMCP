po_custom_field_schema = {
    "type": "object",
    "properties": {
        "customFieldNumber": {
            "type": "string",
            "description": "Custom field number can be seen in the peakflo web UI",
        },
        "name": {
            "type": "string",
            "description": "Custom field name",
        },
        "value": {
            "description": "Custom field value. Can be string, number or array. Dates need to be sent in ISO 8601 date format",
        },
    },
    "required": ["customFieldNumber", "value"],
}


po_custom_field_output_schema = {
    "type": "object",
    "description": "Custom field as returned by the API on reads (no customFieldNumber echoed back)",
    "properties": {
        "name": {
            "type": "string",
            "description": "Custom field name",
        },
        "value": {
            "description": "Custom field value",
        },
    },
}


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
            "items": po_custom_field_schema,
        },
    },
    "required": ["sourceId", "name", "quantity", "unitPrice"],
}


po_item_output_schema = {
    "type": "object",
    "properties": {
        **{k: v for k, v in po_item_schema["properties"].items() if k != "customField"},
        "itemId": {
            "type": ["string", "null"],
            "description": "ID of the item. Null when the line item has no external item ID.",
        },
        "quantity": {
            "type": "number",
            "description": "Quantity of the item",
        },
        "customFields": {
            "type": "array",
            "description": "Array of custom fields for the item",
            "items": po_custom_field_output_schema,
        },
    },
}


po_attachment_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "Name of the attachment",
        },
        "dateCreated": {
            "type": "string",
            "description": "Timestamp of attachment creation",
        },
        "contentType": {
            "type": "string",
            "description": "MIME type of the attachment",
        },
        "fileSize": {
            "type": "integer",
            "description": "Size of the attachment in bytes",
        },
        "fileType": {
            "type": "string",
            "description": "Type of attachment",
            "enum": [
                "transaction",
                "statement",
                "cabinet",
                "invoice",
                "paymentProof",
                "other",
            ],
        },
        "signedUrl": {
            "type": "string",
            "description": "Signed url for the attachment",
        },
    },
}


read_purchase_order_output = {
    "type": "object",
    "properties": {
        "externalId": {
            "type": "string",
            "description": "External ID of the purchase order",
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
        "paidAmount": {
            "type": "number",
            "description": "Amount already paid",
        },
        "balanceAmount": {
            "type": "number",
            "description": "Remaining balance amount",
        },
        "currency": {
            "type": "string",
            "description": "Currency of the purchase order",
        },
        "issueDate": {
            "type": "string",
            "description": "Issue date of the purchase order (ISO8601 date format)",
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
            "description": "Status of the purchase order",
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
        "attachments": {
            "type": "array",
            "description": "List of attachments",
            "items": po_attachment_schema,
        },
        "items": {
            "type": "array",
            "description": "List of items included in the purchase order",
            "items": po_item_output_schema,
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
        "receiptDate": {
            "type": "string",
            "description": "Date of purchase order receipt (ISO8601 format)",
        },
        "deliveryDate": {
            "type": "string",
            "description": "Date of expected delivery (ISO8601 format)",
        },
        "bills": {
            "type": "array",
            "description": "List of associated bill IDs",
            "items": {"type": "string"},
        },
        "receiptNotes": {
            "type": "array",
            "description": "Notes related to the receipt",
            "items": {"type": "string"},
        },
        "balanceQuantity": {
            "type": "number",
            "description": "Remaining quantity balance",
        },
        "customFields": {
            "type": "array",
            "description": "Array of custom fields",
            "items": po_custom_field_output_schema,
        },
        "subsidiaryReference": {
            "type": ["string", "null"],
            "description": "Subsidiary reference. Null when unassigned.",
        },
    },
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
            "description": "Status of the purchase order",
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
            "description": "Array of custom fields",
            "items": po_custom_field_schema,
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
    "additionalProperties": false,
}
