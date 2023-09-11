from enum import Enum

class PaymentErrorCode(Enum):
    INVALID = "invalid_phone"
    PAYMENT_ERROR = "payment_error"