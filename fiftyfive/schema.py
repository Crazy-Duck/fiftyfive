import sgqlc.types
import sgqlc.types.datetime

schema = sgqlc.types.Schema()


########################################################################
# Scalars and Enumerations
########################################################################
class AccessOptionsEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Private", "PublicFree", "PublicPaid")


class AuthorizationMode(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("AutoCharge", "SwipeAndCharge")


class BankAccountScheme(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("IBAN", "UK_SORT_CODE")


Boolean = sgqlc.types.Boolean


class Capability(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "CASH_PAYABLE",
        "CHARGE_BACK",
        "CHARGING_PREFERENCES_CAPABLE",
        "CHARGING_PROFILE_CAPABLE",
        "CHIP_CARD_SUPPORT",
        "CONTACTLESS_CARD_SUPPORT",
        "CREDIT_CARD_PAYABLE",
        "DEBIT_CARD_PAYABLE",
        "DIRECT_PAYMENT",
        "FREE_TRANSACTION",
        "HAS_METER_VALUES",
        "HUBJECT",
        "IEC_15118",
        "PED_TERMINAL",
        "REMOTE_DIRECT_PAYMENT",
        "REMOTE_START_STOP_CAPABLE",
        "RESERVABLE",
        "RFID_READER",
        "TOKEN_GROUP_CAPABLE",
        "UNLOCK_CAPABLE",
    )


class CardDetailsStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("ACTIVE",)


class CardState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Active", "Blocked", "Deactivated", "Inactive", "MarkedForDeletion")


class CardType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "Anonymous",
        "Barcode",
        "Group",
        "IEC_15118",
        "PlugAndCharge",
        "QRcode",
        "RFID",
        "Remote",
    )


class ChargeGroupType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Home", "Other")


class ChargeStationChannelAcDc(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("AC", "DC")


class ChargeStationChannelCapability(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "CashPayable",
        "ChargeBack",
        "ChargingProfile",
        "CreditCardPayable",
        "DebitCardPayable",
        "FreeTransaction",
        "HasMeterValues",
        "Hubject",
        "Iec15118",
        "LocalKey",
        "LocalPrepaid",
        "MaxOverridableCurrent",
        "NoAuthorization",
        "RemotePrepaid",
        "RemoteStartStop",
        "Reservable",
        "Rfid",
        "Unlockable",
    )


class ChargeStationChannelConnectorFormat(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Cable", "Socket")


class ChargeStationChannelConnectorType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "Chademo",
        "DomesticA",
        "DomesticB",
        "DomesticC",
        "DomesticD",
        "DomesticE",
        "DomesticF",
        "DomesticG",
        "DomesticH",
        "DomesticI",
        "DomesticJ",
        "DomesticK",
        "DomesticL",
        "Iec603092Single16",
        "Iec603092Three16",
        "Iec603092Three32",
        "Iec603092Three64",
        "Iec62196T1",
        "Iec62196T1Combo",
        "Iec62196T2",
        "Iec62196T2Combo",
        "Iec62196T3A",
        "Iec62196T3C",
        "TeslaR",
        "TeslaS",
    )


class ChargeStationChannelGlobalStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "Available",
        "Charging",
        "Faulty",
        "NoCommunication",
        "PoweredOff",
        "Reserved",
        "Unavailable",
        "Unknown",
    )


class ChargeStationChannelStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "AlarmInputActivated",
        "Blocked",
        "CableUnderrated",
        "CardExpired",
        "ChannelRelay1Active",
        "ChannelRelay2Active",
        "ChargingComplete",
        "ChargingProfileActive",
        "CpDiodeDetectionError",
        "CpStateCDetected",
        "CpStateChangedTooOften",
        "CpUnknown",
        "DccIsolationError",
        "DccPowerSupplyRelatedError",
        "DccVehicleRelatedError",
        "EmergencySwitch",
        "EventlogFull",
        "FoundLowCosphi",
        "FuseTripped",
        "GenericFaulty",
        "KwhError",
        "LockEngaged",
        "NoCommunication",
        "Ok",
        "OvercurrentError",
        "PowerFailure",
        "PrepaidLimitReached",
        "Rcd2Tripped",
        "RcdTripped",
        "RelayError",
        "SimpleChargerNetworkFound",
        "StateCbABDetected",
        "TagReaderError",
        "TemperatureLimitReached",
        "TemperatureWarning",
        "Transaction",
        "UtilityKwhError",
        "VentilationRequired",
        "WatchdogResetOccured",
    )


class ChargeStationState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Active", "Blocked", "Inactive")


class ChargeStationSubscriptionState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Active",)


class ChargingMode(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("MaxSolar", "OptimizedSolar", "PureSolar", "RegularCharging")


class ConnectorFormat(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("CABLE", "SOCKET")


class ConnectorType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "CHADEMO",
        "DOMESTIC_A",
        "DOMESTIC_B",
        "DOMESTIC_C",
        "DOMESTIC_D",
        "DOMESTIC_E",
        "DOMESTIC_F",
        "DOMESTIC_G",
        "DOMESTIC_H",
        "DOMESTIC_I",
        "DOMESTIC_J",
        "DOMESTIC_K",
        "DOMESTIC_L",
        "IEC_60309_2_single_16",
        "IEC_60309_2_three_16",
        "IEC_60309_2_three_32",
        "IEC_60309_2_three_64",
        "IEC_62196_T1",
        "IEC_62196_T1_COMBO",
        "IEC_62196_T2",
        "IEC_62196_T2_COMBO",
        "IEC_62196_T3A",
        "IEC_62196_T3C",
        "PANTOGRAPH_BOTTOM_UP",
        "PANTOGRAPH_TOP_DOWN",
        "TESLA_R",
        "TESLA_S",
    )


class CustomerElectronicInvoice(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("NONE", "OHNL_FORMAT")


class CustomerFilterState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "Active",
        "Blocked",
        "Deactivated",
        "EmailChecked",
        "NonActive",
        "Registered",
    )


class CustomerFilterType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Company", "Employee", "Private", "Template")


class CustomerReimbursementMode(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("NONE", "PER_CHARGE_STATION", "PER_EMPLOYEE")


class CustomerSalutation(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("EMPTY", "MR", "MRS")


class CustomerState(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "ACTIVE",
        "BLOCKED",
        "DEACTIVATED",
        "EMAIL_CHECKED",
        "NON_ACTIVE",
        "REGISTERED",
    )


class CustomerType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("COMPANY", "EMPLOYEE", "PRIVATE", "TEMPLATE")


Date = sgqlc.types.datetime.Date


class DateTimeISO(sgqlc.types.Scalar):
    __schema__ = schema


class DayOfWeek(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "FRIDAY",
        "MONDAY",
        "SATURDAY",
        "SUNDAY",
        "THURSDAY",
        "TUESDAY",
        "WEDNESDAY",
    )


class DeactivationReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Admin", "CardExpired", "Customer", "SeeCustomer")


class DeviceType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("ANDROID", "IOS", "OTHER")


class EnergySourceCategory(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "COAL",
        "GAS",
        "GENERAL_FOSSIL",
        "GENERAL_GREEN",
        "NUCLEAR",
        "SOLAR",
        "WATER",
        "WIND",
    )


class EnvironmentalImpactCategory(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("CARBON_DIOXIDE", "NUCLEAR_WASTE")


class EvseStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "AVAILABLE",
        "BLOCKED",
        "CHARGING",
        "INOPERATIVE",
        "OUTOFORDER",
        "PLANNED",
        "PRE_RESERVED",
        "REMOVED",
        "RESERVED",
        "SYSTEM_RESERVED",
        "UNKNOWN",
    )


class FeatureName(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("GUEST_MODE", "SHELL_FIRST_TIME_ONBOARDING", "VOICE_AGENT")


class FeatureSource(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("APP", "CUSTOMER", "DYNAMIC")


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int


class InvoiceBillingType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Regular", "Reimbursement", "ReimbursementPayout", "Selfbill")


class InvoicePaymentMethod(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "AutoCollection",
        "Direct",
        "Free",
        "Invoice",
        "PaymentTerminal",
        "Wallet",
    )


class InvoiceStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "Blocked",
        "Created",
        "CreditNoteCreated",
        "CreditNoteSent",
        "CustomIgnored",
        "CustomPaid",
        "CustomRefused",
        "DirectDebitCreated",
        "NewDebitInvoiceCreated",
        "Overpaid",
        "Paid",
        "PaidAfterActionTaken",
        "PaymentActionTaken",
        "PaymentOverdue",
        "PaymentOverdueLastCall",
        "PaymentTakeAction",
        "Seen",
        "Sent",
        "WaitingForPayment",
    )


class InvoiceType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Customer", "Prepaid", "Provider", "Roaming", "RoamingIncoming")


class InvoiceVatType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("ChargingCountry", "Default", "NoVat", "OutsideVat", "ReverseCharge")


class JSON(sgqlc.types.Scalar):
    __schema__ = schema


class LegacyTariffItemType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("kwh", "minute", "minute_parking", "start")


class LegacyTariffTimeslotDayOfWeek(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "friday",
        "monday",
        "saturday",
        "sunday",
        "thursday",
        "tuesday",
        "wednesday",
    )


class LiveKitPlatformType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("android", "ios", "macos", "web", "windows")


class LiveKitVoiceAgentEnvironment(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("DEV", "LOCAL", "PROD", "STAGING")


class LmsAvailability(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("ALL", "AVAILABLE")


class LmsLocationType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "CarPark",
        "Other",
        "ParkingInPublicSpace",
        "ParkingLot",
        "PrivateLocation",
        "TestStation",
        "UndergroundCarPark",
        "Unknown",
    )


class OdooIntervalType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("days", "hours", "minutes")


class OdooOrderDirection(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("asc", "desc")


class OdooTeamId(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("CHARGECARD_L1", "TARIFF_CHANGE_L2")


class OdooTicketStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("CLOSED", "OPEN")


class PowerType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("AC", "AC_1_PHASE", "AC_3_PHASE", "DC")


class ProductPaymentMode(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("CustomerPays", "ProviderPays")


class ProductPaymentPeriodMode(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Monthly", "Once")


class ProductSelectionMode(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("NotSelectable", "Selectable", "SelectableOnlyX")


class ProductType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Card", "PaymentTerminal", "RechargeSpot")


class ProductUsageType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "Card",
        "Free",
        "InvoiceOnly",
        "Other",
        "Private",
        "PriveProduct",
        "PublicProduct",
        "SimOnly",
    )


class ProviderCategory(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "AT",
        "BE",
        "CHF",
        "DE",
        "ES",
        "FR",
        "IT",
        "NL",
        "None",
        "PL",
        "UBER",
        "UK",
    )


class PublicOrPrivate(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Private", "Public")


class PushNotificationType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("ACCOUNT", "CHARGEPOINT", "SUPPORT", "TARIFF")


class ReservationRestrictionType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("RESERVATION", "RESERVATION_EXPIRES")


class RetrievePasswordStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("INVALID", "INVALID_REQUEST", "VALID", "VERSION_TOO_LOW")


class RoamingRole(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("CPO", "DataConsumer", "DataSupplier", "LmsDataConsumer", "MSP")


class Salutation(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("EMPTY", "MR", "MRS")


class ScheduleName(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("RunChargeStationMailing", "RunTicketMigration")


class SortDirection(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("asc", "desc")


String = sgqlc.types.String


class TariffDimensionType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("ENERGY", "FLAT", "PARKING_TIME", "TIME")


class TariffType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "AD_HOC_PAYMENT",
        "PROFILE_CHEAP",
        "PROFILE_FAST",
        "PROFILE_GREEN",
        "REGULAR",
    )


class TicketSource(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "AutoGenerated",
        "ContactForm",
        "Email",
        "Mail",
        "Other",
        "Telephone",
    )


class TicketStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Close", "Generated", "Open")


class TicketType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Alteration", "Complaint", "Inquiry", "Issue", "Note")


class TransactionBillingType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Regular", "Reimbursement", "ReimbursementPayout", "Selfbill")


class TransactionConnectorFormat(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Cable", "Socket")


class TransactionConnectorType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "Chademo",
        "DomesticA",
        "DomesticB",
        "DomesticC",
        "DomesticD",
        "DomesticE",
        "DomesticF",
        "DomesticG",
        "DomesticH",
        "DomesticI",
        "DomesticJ",
        "DomesticK",
        "DomesticL",
        "Iec603092Single16",
        "Iec603092Three16",
        "Iec603092Three32",
        "Iec603092Three64",
        "Iec62196T1",
        "Iec62196T1Combo",
        "Iec62196T2",
        "Iec62196T2Combo",
        "Iec62196T3A",
        "Iec62196T3C",
        "TeslaR",
        "TeslaS",
    )


class TransactionCurrentType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("AC", "DC")


class TransactionGlobalStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "GlobalStatusActive",
        "GlobalStatusBillable",
        "GlobalStatusBilled",
        "GlobalStatusBillingDelegated",
        "GlobalStatusCompleted",
        "GlobalStatusInvalid",
        "GlobalStatusPending",
    )


class TransactionMethod(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Remote", "Whitelist")


class TransactionPaymentMethod(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Direct", "Invoice", "Wallet")


class TransactionPeriodItemSource(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "Costs",
        "Margin",
        "PaymentTerminalProcessingFees",
        "Surcharge",
        "Tariff",
    )


class TransactionPeriodItemType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "CpoAdditionalProvider",
        "CpoAppManager",
        "CpoCustomer",
        "CpoProvider",
        "CpoRoaming",
        "MspAdditionalProvider",
        "MspAppManager",
        "MspAppManagerToProvider",
        "MspCpo",
        "MspCustomer",
        "MspProvider",
        "MspRoaming",
    )


class TransactionPeriodSex(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Female", "Male")


class TransactionProfileType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Cheap", "Fast", "Green", "Regular")


class TransactionStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("Billable", "Billed", "BillingDelegated")


class TransactionType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = (
        "CPOUnknown",
        "Direct",
        "ExternalRoamingCPO",
        "ExternalRoamingMSP",
        "InternalRoaming",
        "InternalRoamingDiffRoamingProfiles",
        "Local",
        "MSPUnknown",
    )


class TransactionVatType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("ChargingCountry", "Default", "NoVat", "OutsideVat", "ReverseCharge")


class WhitelistType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ("RealtimeWhitelistIfOffline", "Whitelist", "WhitelistOrRealtime")


########################################################################
# Input Objects
########################################################################
class AccessOptionInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("charge_card", "authorization_mode")
    charge_card = sgqlc.types.Field(String, graphql_name="chargeCard")
    authorization_mode = sgqlc.types.Field(
        AuthorizationMode, graphql_name="authorizationMode"
    )


class AudienceInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("platform", "provider_ids", "user_group_ids", "user_ids")
    platform = sgqlc.types.Field(
        sgqlc.types.list_of(DeviceType), graphql_name="platform"
    )
    provider_ids = sgqlc.types.Field(
        sgqlc.types.list_of(ID), graphql_name="providerIds"
    )
    user_group_ids = sgqlc.types.Field(
        sgqlc.types.list_of(ID), graphql_name="userGroupIds"
    )
    user_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="userIds")


class BankAccountInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "id",
        "scheme",
        "holder_name",
        "iban",
        "bic",
        "account_number",
        "sort_code",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    scheme = sgqlc.types.Field(
        sgqlc.types.non_null(BankAccountScheme), graphql_name="scheme"
    )
    holder_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="holderName"
    )
    iban = sgqlc.types.Field(String, graphql_name="iban")
    bic = sgqlc.types.Field(String, graphql_name="bic")
    account_number = sgqlc.types.Field(String, graphql_name="account_number")
    sort_code = sgqlc.types.Field(String, graphql_name="sort_code")


class BulkUpdateCpmsIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("cpms_id", "email")
    cpms_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="cpmsId")
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="email")


class CardActionTypeSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")


class CardCardProviderSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")


class CardCustomerFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")


class CardFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "page",
        "items_per_page",
        "search",
        "internal_id",
        "external_id",
        "contract_id",
        "info",
        "usergroup",
        "is_global",
        "attached",
        "wallet",
        "customer",
        "transaction_customer",
        "product_customer",
        "date_from",
        "date_to",
    )
    page = sgqlc.types.Field(Int, graphql_name="page")
    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    search = sgqlc.types.Field(String, graphql_name="search")
    internal_id = sgqlc.types.Field(String, graphql_name="internalId")
    external_id = sgqlc.types.Field(String, graphql_name="externalId")
    contract_id = sgqlc.types.Field(String, graphql_name="contractId")
    info = sgqlc.types.Field(String, graphql_name="info")
    usergroup = sgqlc.types.Field("CardUserGroupFilter", graphql_name="usergroup")
    is_global = sgqlc.types.Field(Boolean, graphql_name="isGlobal")
    attached = sgqlc.types.Field(Boolean, graphql_name="attached")
    wallet = sgqlc.types.Field(Boolean, graphql_name="wallet")
    customer = sgqlc.types.Field(CardCustomerFilter, graphql_name="customer")
    transaction_customer = sgqlc.types.Field(
        "CardTransactionCustomerFilter", graphql_name="transactionCustomer"
    )
    product_customer = sgqlc.types.Field(
        "CardProductCustomerFilter", graphql_name="productCustomer"
    )
    date_from = sgqlc.types.Field(String, graphql_name="dateFrom")
    date_to = sgqlc.types.Field(String, graphql_name="dateTo")


class CardProductCustomerFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")


class CardSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "id",
        "creation_date",
        "internal_id",
        "external_id",
        "contract_id",
        "info",
        "usergroup",
        "is_global",
        "card_provider",
        "action_type",
        "state",
        "roaming",
    )
    id = sgqlc.types.Field(SortDirection, graphql_name="id")
    creation_date = sgqlc.types.Field(SortDirection, graphql_name="creationDate")
    internal_id = sgqlc.types.Field(SortDirection, graphql_name="internalId")
    external_id = sgqlc.types.Field(SortDirection, graphql_name="externalId")
    contract_id = sgqlc.types.Field(SortDirection, graphql_name="contractId")
    info = sgqlc.types.Field(SortDirection, graphql_name="info")
    usergroup = sgqlc.types.Field("CardUserGroupSort", graphql_name="usergroup")
    is_global = sgqlc.types.Field(SortDirection, graphql_name="isGlobal")
    card_provider = sgqlc.types.Field(CardCardProviderSort, graphql_name="cardProvider")
    action_type = sgqlc.types.Field(CardActionTypeSort, graphql_name="actionType")
    state = sgqlc.types.Field(SortDirection, graphql_name="state")
    roaming = sgqlc.types.Field(SortDirection, graphql_name="roaming")


class CardTransactionCustomerFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")


class CardUserGroupFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("ids", "name", "provider")
    ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="ids")
    name = sgqlc.types.Field(String, graphql_name="name")
    provider = sgqlc.types.Field("CardUserGroupProviderFilter", graphql_name="provider")


class CardUserGroupProviderFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")


class CardUserGroupProviderSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")


class CardUserGroupSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name", "provider")
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    provider = sgqlc.types.Field(CardUserGroupProviderSort, graphql_name="provider")


class ChargeGroupFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "page",
        "items_per_page",
        "id",
        "usergroup",
        "name",
        "info",
        "tariff",
        "type",
    )
    page = sgqlc.types.Field(Int, graphql_name="page")
    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    id = sgqlc.types.Field(ID, graphql_name="id")
    usergroup = sgqlc.types.Field(
        "ChargeGroupUserGroupFilter", graphql_name="usergroup"
    )
    name = sgqlc.types.Field(String, graphql_name="name")
    info = sgqlc.types.Field(String, graphql_name="info")
    tariff = sgqlc.types.Field("ChargeGroupTariffFilter", graphql_name="tariff")
    type = sgqlc.types.Field(ChargeGroupType, graphql_name="type")


class ChargeGroupSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id", "name", "info", "type", "usergroup", "tariff")
    id = sgqlc.types.Field(SortDirection, graphql_name="id")
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    info = sgqlc.types.Field(SortDirection, graphql_name="info")
    type = sgqlc.types.Field(SortDirection, graphql_name="type")
    usergroup = sgqlc.types.Field("ChargeGroupUserGroupSort", graphql_name="usergroup")
    tariff = sgqlc.types.Field("ChargeGroupTariffSort", graphql_name="tariff")


class ChargeGroupTariffFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")


class ChargeGroupTariffSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")


class ChargeGroupUserGroupFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("ids", "name")
    ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="ids")
    name = sgqlc.types.Field(String, graphql_name="name")


class ChargeGroupUserGroupSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")


class ChargeStationChargeFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("transactions",)
    transactions = sgqlc.types.Field(
        "ChargeStationTransactionFilter", graphql_name="transactions"
    )


class ChargeStationChargeGroupFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id", "name", "tariff")
    id = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")
    tariff = sgqlc.types.Field("ChargeStationTariffFilter", graphql_name="tariff")


class ChargeStationChargeGroupSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name", "tariff")
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    tariff = sgqlc.types.Field("ChargeStationTariffSort", graphql_name="tariff")


class ChargeStationCountryFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("code",)
    code = sgqlc.types.Field(String, graphql_name="code")


class ChargeStationFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "page",
        "items_per_page",
        "id",
        "search",
        "state",
        "subscription",
        "name",
        "physical_number",
        "location",
        "phone",
        "comm_id",
        "software",
        "charge_group",
        "sim",
        "usergroup",
        "parameter_set",
        "manufacturer_type",
        "owner",
        "channel_physical_ids",
        "payer",
        "recipient",
        "reference",
    )
    page = sgqlc.types.Field(Int, graphql_name="page")
    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="id")
    search = sgqlc.types.Field(String, graphql_name="search")
    state = sgqlc.types.Field(ChargeStationState, graphql_name="state")
    subscription = sgqlc.types.Field(
        ChargeStationSubscriptionState, graphql_name="subscription"
    )
    name = sgqlc.types.Field(String, graphql_name="name")
    physical_number = sgqlc.types.Field(String, graphql_name="physicalNumber")
    location = sgqlc.types.Field("ChargeStationLocationFilter", graphql_name="location")
    phone = sgqlc.types.Field(String, graphql_name="phone")
    comm_id = sgqlc.types.Field(String, graphql_name="commId")
    software = sgqlc.types.Field(String, graphql_name="software")
    charge_group = sgqlc.types.Field(
        ChargeStationChargeGroupFilter, graphql_name="chargeGroup"
    )
    sim = sgqlc.types.Field("ChargeStationSimFilter", graphql_name="sim")
    usergroup = sgqlc.types.Field(
        "ChargeStationUsergroupFilter", graphql_name="usergroup"
    )
    parameter_set = sgqlc.types.Field(
        "ChargeStationParameterSetFilter", graphql_name="parameterSet"
    )
    manufacturer_type = sgqlc.types.Field(
        "ChargeStationManufacturerTypeFilter", graphql_name="manufacturerType"
    )
    owner = sgqlc.types.Field("ChargeStationOwnerFilter", graphql_name="owner")
    channel_physical_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="channelPhysicalIds"
    )
    payer = sgqlc.types.Field("ChargeStationPayerFilter", graphql_name="payer")
    recipient = sgqlc.types.Field(
        "ChargeStationRecipientFilter", graphql_name="recipient"
    )
    reference = sgqlc.types.Field(String, graphql_name="reference")


class ChargeStationLocationFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id", "address", "city", "country")
    id = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name="id")
    address = sgqlc.types.Field(String, graphql_name="address")
    city = sgqlc.types.Field(String, graphql_name="city")
    country = sgqlc.types.Field(ChargeStationCountryFilter, graphql_name="country")


class ChargeStationLocationSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("address", "city")
    address = sgqlc.types.Field(SortDirection, graphql_name="address")
    city = sgqlc.types.Field(SortDirection, graphql_name="city")


class ChargeStationManufacturerTypeFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("vendor", "model")
    vendor = sgqlc.types.Field(String, graphql_name="vendor")
    model = sgqlc.types.Field(String, graphql_name="model")


class ChargeStationOwnerFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id", "first_name", "last_name", "company_name")
    id = sgqlc.types.Field(ID, graphql_name="id")
    first_name = sgqlc.types.Field(String, graphql_name="firstName")
    last_name = sgqlc.types.Field(String, graphql_name="lastName")
    company_name = sgqlc.types.Field(String, graphql_name="companyName")


class ChargeStationParameterSetFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")


class ChargeStationParameterSetSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")


class ChargeStationPayerFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("subscription",)
    subscription = sgqlc.types.Field(
        "ChargeStationSubscriptionFilter", graphql_name="subscription"
    )


class ChargeStationProviderFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")


class ChargeStationRecipientFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("charge",)
    charge = sgqlc.types.Field(ChargeStationChargeFilter, graphql_name="charge")


class ChargeStationSimFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("sim_number", "iccid")
    sim_number = sgqlc.types.Field(String, graphql_name="simNumber")
    iccid = sgqlc.types.Field(String, graphql_name="iccid")


class ChargeStationSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "id",
        "name",
        "physical_number",
        "location",
        "parameter_set",
        "charge_group",
        "usergroup",
        "last_communication_date",
        "status",
    )
    id = sgqlc.types.Field(SortDirection, graphql_name="id")
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    physical_number = sgqlc.types.Field(SortDirection, graphql_name="physicalNumber")
    location = sgqlc.types.Field(ChargeStationLocationSort, graphql_name="location")
    parameter_set = sgqlc.types.Field(
        ChargeStationParameterSetSort, graphql_name="parameterSet"
    )
    charge_group = sgqlc.types.Field(
        ChargeStationChargeGroupSort, graphql_name="chargeGroup"
    )
    usergroup = sgqlc.types.Field(
        "ChargeStationUsergroupSort", graphql_name="usergroup"
    )
    last_communication_date = sgqlc.types.Field(
        SortDirection, graphql_name="lastCommunicationDate"
    )
    status = sgqlc.types.Field(SortDirection, graphql_name="status")


class ChargeStationSubscriptionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")


class ChargeStationTariffFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")


class ChargeStationTariffSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")


class ChargeStationTransactionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")


class ChargeStationUsergroupFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("ids", "name", "provider")
    ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="ids")
    name = sgqlc.types.Field(String, graphql_name="name")
    provider = sgqlc.types.Field(
        "ChargeStationUsergroupProviderFilter", graphql_name="provider"
    )


class ChargeStationUsergroupProviderFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")


class ChargeStationUsergroupSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")


class CodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("code",)
    code = sgqlc.types.Field(String, graphql_name="code")


class CreateAIVoiceTicketInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("title", "description", "status", "team_key_id")
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="title")
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )
    status = sgqlc.types.Field(
        sgqlc.types.non_null(OdooTicketStatus), graphql_name="status"
    )
    team_key_id = sgqlc.types.Field(ID, graphql_name="teamKeyId")


class CreateCustomerBacsMandateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("bank_account_no", "bank_sort_code", "email")
    bank_account_no = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="bankAccountNo"
    )
    bank_sort_code = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="bankSortCode"
    )
    email = sgqlc.types.Field(String, graphql_name="email")


class CreateEreMandateTicketInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("ean_code", "mandate_period")
    ean_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="eanCode")
    mandate_period = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="mandatePeriod"
    )


class CreateScheduleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name", "payload")
    name = sgqlc.types.Field(ScheduleName, graphql_name="name")
    payload = sgqlc.types.Field("SchedulePayloadInput", graphql_name="payload")


class CreateUpdateCustomerMandateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "accepted",
        "billing_account_number",
        "bic",
        "billing_account_name",
    )
    accepted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="accepted")
    billing_account_number = sgqlc.types.Field(
        String, graphql_name="billingAccountNumber"
    )
    bic = sgqlc.types.Field(String, graphql_name="bic")
    billing_account_name = sgqlc.types.Field(String, graphql_name="billingAccountName")


class CurrencyFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("supported",)
    supported = sgqlc.types.Field(Boolean, graphql_name="supported")


class CustomerBankFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("account",)
    account = sgqlc.types.Field(String, graphql_name="account")


class CustomerCompanyFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name", "id")
    name = sgqlc.types.Field(String, graphql_name="name")
    id = sgqlc.types.Field(ID, graphql_name="id")


class CustomerCountryFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("code",)
    code = sgqlc.types.Field(String, graphql_name="code")


class CustomerFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "page",
        "items_per_page",
        "id",
        "search",
        "type",
        "state",
        "object_id",
        "usergroup",
        "provider",
        "name",
        "city",
        "country",
        "street",
        "street_number",
        "street_number_ext",
        "zip_code",
        "phone",
        "mobile",
        "company",
        "email",
        "bank",
    )
    page = sgqlc.types.Field(Int, graphql_name="page")
    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    id = sgqlc.types.Field(ID, graphql_name="id")
    search = sgqlc.types.Field(String, graphql_name="search")
    type = sgqlc.types.Field(CustomerFilterType, graphql_name="type")
    state = sgqlc.types.Field(CustomerFilterState, graphql_name="state")
    object_id = sgqlc.types.Field(String, graphql_name="objectId")
    usergroup = sgqlc.types.Field("CustomerUserGroupFilter", graphql_name="usergroup")
    provider = sgqlc.types.Field("CustomerProviderFilter", graphql_name="provider")
    name = sgqlc.types.Field(String, graphql_name="name")
    city = sgqlc.types.Field(String, graphql_name="city")
    country = sgqlc.types.Field(CustomerCountryFilter, graphql_name="country")
    street = sgqlc.types.Field(String, graphql_name="street")
    street_number = sgqlc.types.Field(String, graphql_name="streetNumber")
    street_number_ext = sgqlc.types.Field(String, graphql_name="streetNumberExt")
    zip_code = sgqlc.types.Field(String, graphql_name="zipCode")
    phone = sgqlc.types.Field(String, graphql_name="phone")
    mobile = sgqlc.types.Field(String, graphql_name="mobile")
    company = sgqlc.types.Field(CustomerCompanyFilter, graphql_name="company")
    email = sgqlc.types.Field(String, graphql_name="email")
    bank = sgqlc.types.Field(CustomerBankFilter, graphql_name="bank")


class CustomerProviderFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")


class CustomerSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "id",
        "name",
        "city",
        "phone",
        "usergroup",
        "type",
        "creation_date",
    )
    id = sgqlc.types.Field(SortDirection, graphql_name="id")
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    city = sgqlc.types.Field(SortDirection, graphql_name="city")
    phone = sgqlc.types.Field(SortDirection, graphql_name="phone")
    usergroup = sgqlc.types.Field("CustomerUserGroupSort", graphql_name="usergroup")
    type = sgqlc.types.Field(SortDirection, graphql_name="type")
    creation_date = sgqlc.types.Field(SortDirection, graphql_name="creationDate")


class CustomerUserGroupFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(ID, graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")


class CustomerUserGroupSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")


class EndCustomerBacsMandateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("mandate_reference", "end_date")
    mandate_reference = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="mandateReference"
    )
    end_date = sgqlc.types.Field(String, graphql_name="endDate")


class EndCustomerMandateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id", "stop_date")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    stop_date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="stopDate")


class GeoPointInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("latitude", "longitude")
    latitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="latitude")
    longitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="longitude")


class IdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")


class InvoiceCustomerFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "id",
        "first_name",
        "last_name",
        "company_name",
        "object_id",
        "billing_account_number",
        "billing_account_name",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    first_name = sgqlc.types.Field(String, graphql_name="firstName")
    last_name = sgqlc.types.Field(String, graphql_name="lastName")
    company_name = sgqlc.types.Field(String, graphql_name="companyName")
    object_id = sgqlc.types.Field(String, graphql_name="objectId")
    billing_account_number = sgqlc.types.Field(
        String, graphql_name="billingAccountNumber"
    )
    billing_account_name = sgqlc.types.Field(String, graphql_name="billingAccountName")


class InvoiceFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "amount",
        "currency",
        "status",
        "type",
        "country",
        "date_from",
        "date_to",
        "customer",
        "user_group",
        "provider",
    )
    amount = sgqlc.types.Field(String, graphql_name="amount")
    currency = sgqlc.types.Field(String, graphql_name="currency")
    status = sgqlc.types.Field(InvoiceStatus, graphql_name="status")
    type = sgqlc.types.Field(InvoiceType, graphql_name="type")
    country = sgqlc.types.Field(String, graphql_name="country")
    date_from = sgqlc.types.Field(String, graphql_name="dateFrom")
    date_to = sgqlc.types.Field(String, graphql_name="dateTo")
    customer = sgqlc.types.Field(InvoiceCustomerFilter, graphql_name="customer")
    user_group = sgqlc.types.Field("InvoiceUserGroupFilter", graphql_name="userGroup")
    provider = sgqlc.types.Field("InvoiceProviderFilter", graphql_name="provider")


class InvoiceProviderFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(ID, graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")


class InvoiceSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "previous_invoices_id",
        "countries",
        "vat_type",
        "vat_entity",
        "billing_type",
        "credit",
        "invoice_date",
        "customer",
        "provider_profiles",
        "price_incl_vat",
        "cust_price_incl_vat",
        "state",
        "regenerated",
    )
    previous_invoices_id = sgqlc.types.Field(
        SortDirection, graphql_name="previousInvoicesId"
    )
    countries = sgqlc.types.Field("InvoiceSortCountries", graphql_name="countries")
    vat_type = sgqlc.types.Field(SortDirection, graphql_name="vatType")
    vat_entity = sgqlc.types.Field("InvoiceSortVatEntity", graphql_name="vatEntity")
    billing_type = sgqlc.types.Field(SortDirection, graphql_name="billingType")
    credit = sgqlc.types.Field(SortDirection, graphql_name="credit")
    invoice_date = sgqlc.types.Field(SortDirection, graphql_name="invoiceDate")
    customer = sgqlc.types.Field("InvoiceSortCustomer", graphql_name="customer")
    provider_profiles = sgqlc.types.Field(
        "InvoiceSortProviderProfiles", graphql_name="providerProfiles"
    )
    price_incl_vat = sgqlc.types.Field(SortDirection, graphql_name="priceInclVat")
    cust_price_incl_vat = sgqlc.types.Field(
        SortDirection, graphql_name="custPriceInclVat"
    )
    state = sgqlc.types.Field(SortDirection, graphql_name="state")
    regenerated = sgqlc.types.Field(SortDirection, graphql_name="regenerated")


class InvoiceSortCountries(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("localname",)
    localname = sgqlc.types.Field(SortDirection, graphql_name="localname")


class InvoiceSortCustomer(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "first_name",
        "last_name",
        "company_name",
        "id",
        "type",
        "state",
        "billing_account_no",
    )
    first_name = sgqlc.types.Field(SortDirection, graphql_name="firstName")
    last_name = sgqlc.types.Field(SortDirection, graphql_name="lastName")
    company_name = sgqlc.types.Field(SortDirection, graphql_name="companyName")
    id = sgqlc.types.Field(SortDirection, graphql_name="id")
    type = sgqlc.types.Field(SortDirection, graphql_name="type")
    state = sgqlc.types.Field(SortDirection, graphql_name="state")
    billing_account_no = sgqlc.types.Field(
        SortDirection, graphql_name="BillingAccountNo"
    )


class InvoiceSortProviderProfiles(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")


class InvoiceSortVatEntity(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")


class InvoiceUserGroupFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")


class LanguageFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("supported",)
    supported = sgqlc.types.Field(Boolean, graphql_name="supported")


class LiveKitTokenInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("environment", "language", "country", "source", "platform")
    environment = sgqlc.types.Field(
        sgqlc.types.non_null(LiveKitVoiceAgentEnvironment), graphql_name="environment"
    )
    language = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="language")
    country = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="country")
    source = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="source")
    platform = sgqlc.types.Field(
        sgqlc.types.non_null(LiveKitPlatformType), graphql_name="platform"
    )


class LocationBoundsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("sw", "ne")
    sw = sgqlc.types.Field(sgqlc.types.non_null(GeoPointInput), graphql_name="sw")
    ne = sgqlc.types.Field(sgqlc.types.non_null(GeoPointInput), graphql_name="ne")


class LocationsFiltersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "search_latitude",
        "search_longitude",
        "search_string",
        "search_location_ids",
        "search_device_ids",
        "search_channel_ids",
        "search_qr_code",
        "heading",
        "speed",
        "availability",
        "connector_types",
        "min_power",
        "capabilities",
        "providers",
        "profiles",
        "return_fields",
    )
    search_latitude = sgqlc.types.Field(Float, graphql_name="searchLatitude")
    search_longitude = sgqlc.types.Field(Float, graphql_name="searchLongitude")
    search_string = sgqlc.types.Field(String, graphql_name="searchString")
    search_location_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="searchLocationIds",
    )
    search_device_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="searchDeviceIds",
    )
    search_channel_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="searchChannelIds",
    )
    search_qr_code = sgqlc.types.Field(String, graphql_name="searchQrCode")
    heading = sgqlc.types.Field(Float, graphql_name="heading")
    speed = sgqlc.types.Field(Float, graphql_name="speed")
    availability = sgqlc.types.Field(LmsAvailability, graphql_name="availability")
    connector_types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ConnectorType)),
        graphql_name="connectorTypes",
    )
    min_power = sgqlc.types.Field(Float, graphql_name="minPower")
    capabilities = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Capability)),
        graphql_name="capabilities",
    )
    providers = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="providers"
    )
    profiles = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="profiles"
    )
    return_fields = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="returnFields"
    )


class MapLocationsFiltersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("connector_types", "availability", "min_power", "capabilities")
    connector_types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ConnectorType)),
        graphql_name="connectorTypes",
    )
    availability = sgqlc.types.Field(LmsAvailability, graphql_name="availability")
    min_power = sgqlc.types.Field(Float, graphql_name="minPower")
    capabilities = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Capability)),
        graphql_name="capabilities",
    )


class OdooChargeStationFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("user_group",)
    user_group = sgqlc.types.Field("OdooUserGroupFilter", graphql_name="userGroup")


class OdooChargeStationSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("last_communication_date",)
    last_communication_date = sgqlc.types.Field(
        String, graphql_name="lastCommunicationDate"
    )


class OdooScheduleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "cron_expression",
        "interval_type",
        "interval_number",
        "run_immediately",
    )
    cron_expression = sgqlc.types.Field(String, graphql_name="cronExpression")
    interval_type = sgqlc.types.Field(OdooIntervalType, graphql_name="intervalType")
    interval_number = sgqlc.types.Field(Int, graphql_name="intervalNumber")
    run_immediately = sgqlc.types.Field(Boolean, graphql_name="runImmediately")


class OdooUserGroupFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")


class PushNotificationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("title", "body", "extended_body", "type")
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="title")
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="body")
    extended_body = sgqlc.types.Field(String, graphql_name="extendedBody")
    type = sgqlc.types.Field(PushNotificationType, graphql_name="type")


class ScheduleComplexInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("block", "charge")
    block = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="block")
    charge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="charge")


class ScheduleComplexUpdate(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("chargepoint_id", "schedules")
    chargepoint_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="chargepointId"
    )
    schedules = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(ScheduleComplexInput)),
        graphql_name="schedules",
    )


class ScheduleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("weekday", "start_time", "stop_time")
    weekday = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="weekday")
    start_time = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="startTime"
    )
    stop_time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="stopTime")


class SchedulePayloadInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "schedule",
        "provider_name",
        "order_direction",
        "dry_run",
        "close_tickets",
    )
    schedule = sgqlc.types.Field(
        sgqlc.types.non_null(OdooScheduleInput), graphql_name="schedule"
    )
    provider_name = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="providerName"
    )
    order_direction = sgqlc.types.Field(
        OdooOrderDirection, graphql_name="orderDirection"
    )
    dry_run = sgqlc.types.Field(Boolean, graphql_name="dryRun")
    close_tickets = sgqlc.types.Field(Boolean, graphql_name="closeTickets")


class ScheduleSimpleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("weekday", "charge", "times")
    weekday = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="weekday")
    charge = sgqlc.types.Field(Boolean, graphql_name="charge")
    times = sgqlc.types.Field("TimeInput", graphql_name="times")


class ScheduleSimpleUpdate(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("chargepoint_id", "schedules")
    chargepoint_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="chargepointId"
    )
    schedules = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(ScheduleSimpleInput)),
        graphql_name="schedules",
    )


class ScheduleUpdate(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("chargepoint_id", "schedules")
    chargepoint_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="chargepointId"
    )
    schedules = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(ScheduleInput)),
        graphql_name="schedules",
    )


class TicketActionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("taken",)
    taken = sgqlc.types.Field(String, graphql_name="taken")


class TicketChargeStationFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(Int, graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")


class TicketCreatorFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("company",)
    company = sgqlc.types.Field(String, graphql_name="company")


class TicketCustomerFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(Int, graphql_name="id")


class TicketFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "page",
        "items_per_page",
        "id",
        "search",
        "status",
        "description",
        "reported_by",
        "charge_station",
        "usergroup",
        "customer",
        "creator",
        "action",
    )
    page = sgqlc.types.Field(Int, graphql_name="page")
    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    id = sgqlc.types.Field(Int, graphql_name="id")
    search = sgqlc.types.Field(String, graphql_name="search")
    status = sgqlc.types.Field(TicketStatus, graphql_name="status")
    description = sgqlc.types.Field(String, graphql_name="description")
    reported_by = sgqlc.types.Field(String, graphql_name="reportedBy")
    charge_station = sgqlc.types.Field(
        TicketChargeStationFilter, graphql_name="chargeStation"
    )
    usergroup = sgqlc.types.Field("TicketUsergroupFilter", graphql_name="usergroup")
    customer = sgqlc.types.Field(TicketCustomerFilter, graphql_name="customer")
    creator = sgqlc.types.Field(TicketCreatorFilter, graphql_name="creator")
    action = sgqlc.types.Field(TicketActionFilter, graphql_name="action")


class TicketSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "id",
        "charge_station",
        "user_group",
        "customer",
        "creator",
        "action",
        "reported_by",
    )
    id = sgqlc.types.Field(SortDirection, graphql_name="id")
    charge_station = sgqlc.types.Field(
        "TicketSortChargeStation", graphql_name="chargeStation"
    )
    user_group = sgqlc.types.Field("TicketSortUserGroup", graphql_name="userGroup")
    customer = sgqlc.types.Field("TicketSortCustomer", graphql_name="customer")
    creator = sgqlc.types.Field("TicketSortCreator", graphql_name="creator")
    action = sgqlc.types.Field("TicketSortAction", graphql_name="action")
    reported_by = sgqlc.types.Field(SortDirection, graphql_name="reportedBy")


class TicketSortAction(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("taken",)
    taken = sgqlc.types.Field(SortDirection, graphql_name="taken")


class TicketSortChargeStation(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(SortDirection, graphql_name="id")


class TicketSortCreator(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("company",)
    company = sgqlc.types.Field(SortDirection, graphql_name="company")


class TicketSortCustomer(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(SortDirection, graphql_name="id")


class TicketSortUserGroup(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(SortDirection, graphql_name="id")


class TicketUsergroupFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(Int, graphql_name="id")


class TimeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("start_time", "stop_time")
    start_time = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="startTime"
    )
    stop_time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="stopTime")


class TokenUpdate(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "cost_center_number",
        "expiry_date",
        "info",
        "qr_code",
        "reference",
        "remote_password",
        "roaming_home_charging_enabled",
        "roaming",
        "state",
    )
    cost_center_number = sgqlc.types.Field(String, graphql_name="costCenterNumber")
    expiry_date = sgqlc.types.Field(String, graphql_name="expiryDate")
    info = sgqlc.types.Field(String, graphql_name="info")
    qr_code = sgqlc.types.Field(String, graphql_name="qrCode")
    reference = sgqlc.types.Field(String, graphql_name="reference")
    remote_password = sgqlc.types.Field(String, graphql_name="remotePassword")
    roaming_home_charging_enabled = sgqlc.types.Field(
        Boolean, graphql_name="roamingHomeChargingEnabled"
    )
    roaming = sgqlc.types.Field(Boolean, graphql_name="roaming")
    state = sgqlc.types.Field(String, graphql_name="state")


class TransactionCardFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")


class TransactionChargeStationFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")


class TransactionCustomerFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")


class TransactionFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "page",
        "items_per_page",
        "id",
        "customer",
        "charge_station",
        "card",
        "invoice",
        "provider",
        "status",
        "date_from",
        "date_to",
        "start_date_from",
        "start_date_to",
        "payment_method",
    )
    page = sgqlc.types.Field(Int, graphql_name="page")
    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    id = sgqlc.types.Field(ID, graphql_name="id")
    customer = sgqlc.types.Field(TransactionCustomerFilter, graphql_name="customer")
    charge_station = sgqlc.types.Field(
        TransactionChargeStationFilter, graphql_name="chargeStation"
    )
    card = sgqlc.types.Field(TransactionCardFilter, graphql_name="card")
    invoice = sgqlc.types.Field("TransactionInvoiceFilter", graphql_name="invoice")
    provider = sgqlc.types.Field("TransactionProviderFilter", graphql_name="provider")
    status = sgqlc.types.Field(TransactionStatus, graphql_name="status")
    date_from = sgqlc.types.Field(String, graphql_name="dateFrom")
    date_to = sgqlc.types.Field(String, graphql_name="dateTo")
    start_date_from = sgqlc.types.Field(String, graphql_name="startDateFrom")
    start_date_to = sgqlc.types.Field(String, graphql_name="startDateTo")
    payment_method = sgqlc.types.Field(
        sgqlc.types.list_of(TransactionPaymentMethod), graphql_name="paymentMethod"
    )


class TransactionInvoiceFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")


class TransactionProviderFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")


class TransactionSort(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "id",
        "last_update_date",
        "remote_last_update_date",
        "total_energy",
        "start_date",
        "total_duration",
    )
    id = sgqlc.types.Field(SortDirection, graphql_name="id")
    last_update_date = sgqlc.types.Field(SortDirection, graphql_name="lastUpdateDate")
    remote_last_update_date = sgqlc.types.Field(
        SortDirection, graphql_name="remoteLastUpdateDate"
    )
    total_energy = sgqlc.types.Field(SortDirection, graphql_name="totalEnergy")
    start_date = sgqlc.types.Field(SortDirection, graphql_name="startDate")
    total_duration = sgqlc.types.Field(SortDirection, graphql_name="totalDuration")


class UpdateCustomerInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = (
        "company",
        "company_name",
        "salutation",
        "first_name",
        "last_name",
        "email",
        "username",
        "street",
        "street_number",
        "street_number_ext",
        "zip_code",
        "city",
        "country",
        "preferred_language",
        "invoice_name",
        "invoice_street",
        "invoice_street_number",
        "invoice_street_number_ext",
        "invoice_zip_code",
        "invoice_city",
        "invoice_country",
        "invoice_email",
        "phone",
        "mobile",
        "billing_account_number",
        "bic",
        "billing_account_name",
        "license_plate",
        "info",
        "reference",
        "cost_center_number",
    )
    company = sgqlc.types.Field(IdInput, graphql_name="company")
    company_name = sgqlc.types.Field(String, graphql_name="companyName")
    salutation = sgqlc.types.Field(Salutation, graphql_name="salutation")
    first_name = sgqlc.types.Field(String, graphql_name="firstName")
    last_name = sgqlc.types.Field(String, graphql_name="lastName")
    email = sgqlc.types.Field(String, graphql_name="email")
    username = sgqlc.types.Field(String, graphql_name="username")
    street = sgqlc.types.Field(String, graphql_name="street")
    street_number = sgqlc.types.Field(String, graphql_name="streetNumber")
    street_number_ext = sgqlc.types.Field(String, graphql_name="streetNumberExt")
    zip_code = sgqlc.types.Field(String, graphql_name="zipCode")
    city = sgqlc.types.Field(String, graphql_name="city")
    country = sgqlc.types.Field(CodeInput, graphql_name="country")
    preferred_language = sgqlc.types.Field(CodeInput, graphql_name="preferredLanguage")
    invoice_name = sgqlc.types.Field(String, graphql_name="invoiceName")
    invoice_street = sgqlc.types.Field(String, graphql_name="invoiceStreet")
    invoice_street_number = sgqlc.types.Field(
        String, graphql_name="invoiceStreetNumber"
    )
    invoice_street_number_ext = sgqlc.types.Field(
        String, graphql_name="invoiceStreetNumberExt"
    )
    invoice_zip_code = sgqlc.types.Field(String, graphql_name="invoiceZipCode")
    invoice_city = sgqlc.types.Field(String, graphql_name="invoiceCity")
    invoice_country = sgqlc.types.Field(CodeInput, graphql_name="invoiceCountry")
    invoice_email = sgqlc.types.Field(String, graphql_name="invoiceEmail")
    phone = sgqlc.types.Field(String, graphql_name="phone")
    mobile = sgqlc.types.Field(String, graphql_name="mobile")
    billing_account_number = sgqlc.types.Field(
        String, graphql_name="billingAccountNumber"
    )
    bic = sgqlc.types.Field(String, graphql_name="bic")
    billing_account_name = sgqlc.types.Field(String, graphql_name="billingAccountName")
    license_plate = sgqlc.types.Field(String, graphql_name="licensePlate")
    info = sgqlc.types.Field(String, graphql_name="info")
    reference = sgqlc.types.Field(String, graphql_name="reference")
    cost_center_number = sgqlc.types.Field(String, graphql_name="costCenterNumber")


class UserGroupFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("page", "items_per_page")
    page = sgqlc.types.Field(Int, graphql_name="page")
    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")


########################################################################
# Output Objects and Interfaces
########################################################################
class AccessOptions(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "access_type",
        "private_access_cards",
        "auto_charge_support",
        "authorization_mode",
        "charge_card",
        "published_on_map",
    )
    access_type = sgqlc.types.Field(AccessOptionsEnum, graphql_name="accessType")
    private_access_cards = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(ID)), graphql_name="privateAccessCards"
    )
    auto_charge_support = sgqlc.types.Field(Boolean, graphql_name="autoChargeSupport")
    authorization_mode = sgqlc.types.Field(
        AuthorizationMode, graphql_name="authorizationMode"
    )
    charge_card = sgqlc.types.Field(String, graphql_name="chargeCard")
    published_on_map = sgqlc.types.Field(Boolean, graphql_name="publishedOnMap")


class ActionType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")


class App(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "uid",
        "device_type",
        "push_notification_token",
        "created_at",
        "updated_at",
        "integration_id",
        "device_model_name",
        "user_id",
        "app_version",
        "device_manufacturer",
        "device_version",
        "external_customer_id",
        "external_usergroup_id",
        "external_app_provider_id",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    uid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="uid")
    device_type = sgqlc.types.Field(
        sgqlc.types.non_null(DeviceType), graphql_name="deviceType"
    )
    push_notification_token = sgqlc.types.Field(
        String, graphql_name="pushNotificationToken"
    )
    created_at = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="createdAt"
    )
    updated_at = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="updatedAt"
    )
    integration_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="integrationId"
    )
    device_model_name = sgqlc.types.Field(String, graphql_name="deviceModelName")
    user_id = sgqlc.types.Field(String, graphql_name="userId")
    app_version = sgqlc.types.Field(String, graphql_name="appVersion")
    device_manufacturer = sgqlc.types.Field(String, graphql_name="deviceManufacturer")
    device_version = sgqlc.types.Field(String, graphql_name="deviceVersion")
    external_customer_id = sgqlc.types.Field(String, graphql_name="externalCustomerId")
    external_usergroup_id = sgqlc.types.Field(
        String, graphql_name="externalUsergroupId"
    )
    external_app_provider_id = sgqlc.types.Field(
        String, graphql_name="externalAppProviderId"
    )


class AppFeature(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "enabled", "app", "feature_key")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")
    app = sgqlc.types.Field(sgqlc.types.non_null("AppIdentifier"), graphql_name="app")
    feature_key = sgqlc.types.Field(
        sgqlc.types.non_null("FeatureKey"), graphql_name="featureKey"
    )


class AppIdentifier(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "android_bundle_id",
        "ios_bundle_id",
        "app_features",
        "customer_features",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")
    android_bundle_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="androidBundleId"
    )
    ios_bundle_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="iosBundleId"
    )
    app_features = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AppFeature)),
        graphql_name="appFeatures",
    )
    customer_features = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("CustomerFeature")),
        graphql_name="customerFeatures",
    )


class Authorisation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "method")
    id = sgqlc.types.Field(ID, graphql_name="id")
    method = sgqlc.types.Field(TransactionMethod, graphql_name="method")


class BankAccount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "scheme", "holder_name", "fields", "status", "customer")
    id = sgqlc.types.Field(ID, graphql_name="id")
    scheme = sgqlc.types.Field(BankAccountScheme, graphql_name="scheme")
    holder_name = sgqlc.types.Field(String, graphql_name="holderName")
    fields = sgqlc.types.Field("BankAccountFields", graphql_name="fields")
    status = sgqlc.types.Field(String, graphql_name="status")
    customer = sgqlc.types.Field("Customer", graphql_name="customer")


class BankAccountFields(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("iban", "bic", "account_number", "sort_code")
    iban = sgqlc.types.Field(String, graphql_name="iban")
    bic = sgqlc.types.Field(String, graphql_name="bic")
    account_number = sgqlc.types.Field(String, graphql_name="account_number")
    sort_code = sgqlc.types.Field(String, graphql_name="sort_code")


class BillingProfile(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "name",
        "billing_account_name",
        "billing_account_address",
        "billing_account_country_code",
        "billing_account_zip_code",
        "billing_account_city",
    )
    name = sgqlc.types.Field(String, graphql_name="name")
    billing_account_name = sgqlc.types.Field(String, graphql_name="billingAccountName")
    billing_account_address = sgqlc.types.Field(
        String, graphql_name="billingAccountAddress"
    )
    billing_account_country_code = sgqlc.types.Field(
        String, graphql_name="billingAccountCountryCode"
    )
    billing_account_zip_code = sgqlc.types.Field(
        String, graphql_name="billingAccountZipCode"
    )
    billing_account_city = sgqlc.types.Field(String, graphql_name="billingAccountCity")


class Card(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "user_group",
        "internal_id",
        "external_id",
        "contract_id",
        "customer",
        "transaction_customer",
        "product_customer",
        "creation_date",
        "last_update_date",
        "info",
        "state",
        "expiry_date",
        "activation_date",
        "type",
        "action_type",
        "card_provider",
        "roaming",
        "deactivation_reason",
        "is_global",
        "roaming_home_charging_enabled",
        "roaming_hub_status",
        "reference",
        "qr_code",
        "parent_card",
        "cost_center_number",
        "user_groups",
        "subscriptions",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    internal_id = sgqlc.types.Field(String, graphql_name="internalId")
    external_id = sgqlc.types.Field(String, graphql_name="externalId")
    contract_id = sgqlc.types.Field(String, graphql_name="contractId")
    customer = sgqlc.types.Field("Customer", graphql_name="customer")
    transaction_customer = sgqlc.types.Field(
        "Customer", graphql_name="transactionCustomer"
    )
    product_customer = sgqlc.types.Field("Customer", graphql_name="productCustomer")
    creation_date = sgqlc.types.Field(String, graphql_name="creationDate")
    last_update_date = sgqlc.types.Field(String, graphql_name="lastUpdateDate")
    info = sgqlc.types.Field(String, graphql_name="info")
    state = sgqlc.types.Field(CardState, graphql_name="state")
    expiry_date = sgqlc.types.Field(String, graphql_name="expiryDate")
    activation_date = sgqlc.types.Field(String, graphql_name="activationDate")
    type = sgqlc.types.Field(CardType, graphql_name="type")
    action_type = sgqlc.types.Field(ActionType, graphql_name="actionType")
    card_provider = sgqlc.types.Field("CardProvider", graphql_name="cardProvider")
    roaming = sgqlc.types.Field(Boolean, graphql_name="roaming")
    deactivation_reason = sgqlc.types.Field(
        DeactivationReason, graphql_name="deactivationReason"
    )
    is_global = sgqlc.types.Field(Boolean, graphql_name="isGlobal")
    roaming_home_charging_enabled = sgqlc.types.Field(
        Boolean, graphql_name="roamingHomeChargingEnabled"
    )
    roaming_hub_status = sgqlc.types.Field(CardState, graphql_name="roamingHubStatus")
    reference = sgqlc.types.Field(String, graphql_name="reference")
    qr_code = sgqlc.types.Field(String, graphql_name="qrCode")
    parent_card = sgqlc.types.Field(String, graphql_name="parentCard")
    cost_center_number = sgqlc.types.Field(String, graphql_name="costCenterNumber")
    user_groups = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("UserGroup")),
        graphql_name="userGroups",
    )
    subscriptions = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("LmsSubscription")),
        graphql_name="subscriptions",
    )


class CardCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(Card), graphql_name="items")
    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")


class CardDetails(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "card_holder",
        "card_reference",
        "contract_id",
        "cost_center_number",
        "expiry_date",
        "is_global_card",
        "issuer",
        "payer",
        "provider_identifier",
        "roaming_enabled",
        "status",
        "subscriber",
        "type",
        "visual_number",
        "wallet",
        "help_desk_name",
        "help_desk_phone",
    )
    card_holder = sgqlc.types.Field(
        sgqlc.types.non_null("CardHolder"), graphql_name="cardHolder"
    )
    card_reference = sgqlc.types.Field(ID, graphql_name="cardReference")
    contract_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="contractId"
    )
    cost_center_number = sgqlc.types.Field(ID, graphql_name="costCenterNumber")
    expiry_date = sgqlc.types.Field(ID, graphql_name="expiryDate")
    is_global_card = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isGlobalCard"
    )
    issuer = sgqlc.types.Field(ID, graphql_name="issuer")
    payer = sgqlc.types.Field(sgqlc.types.non_null("CardHolder"), graphql_name="payer")
    provider_identifier = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="providerIdentifier"
    )
    roaming_enabled = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="roamingEnabled"
    )
    status = sgqlc.types.Field(
        sgqlc.types.non_null(CardDetailsStatus), graphql_name="status"
    )
    subscriber = sgqlc.types.Field(
        sgqlc.types.non_null("CardHolder"), graphql_name="subscriber"
    )
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="type")
    visual_number = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="visualNumber"
    )
    wallet = sgqlc.types.Field(ID, graphql_name="wallet")
    help_desk_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="helpDeskName"
    )
    help_desk_phone = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="helpDeskPhone"
    )


class CardHolder(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("customer_id", "full_name", "first_name", "last_name")
    customer_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="customerId")
    full_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="fullName")
    first_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="firstName"
    )
    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="lastName")


class CardProvider(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")


class CardRoaming(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "internal_id",
        "external_id",
        "contract_id",
        "state",
        "type",
        "issuer",
        "creation_date",
        "expiry_date",
        "last_update_date",
        "roaming_profile",
        "roaming_profile_hub",
        "whitelist_type",
        "roaming",
        "reference",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    internal_id = sgqlc.types.Field(String, graphql_name="internalId")
    external_id = sgqlc.types.Field(String, graphql_name="externalId")
    contract_id = sgqlc.types.Field(String, graphql_name="contractId")
    state = sgqlc.types.Field(CardState, graphql_name="state")
    type = sgqlc.types.Field(CardType, graphql_name="type")
    issuer = sgqlc.types.Field(String, graphql_name="issuer")
    creation_date = sgqlc.types.Field(String, graphql_name="creationDate")
    expiry_date = sgqlc.types.Field(String, graphql_name="expiryDate")
    last_update_date = sgqlc.types.Field(String, graphql_name="lastUpdateDate")
    roaming_profile = sgqlc.types.Field("RoamingProfile", graphql_name="roamingProfile")
    roaming_profile_hub = sgqlc.types.Field(
        "RoamingProfileHub", graphql_name="roamingProfileHub"
    )
    whitelist_type = sgqlc.types.Field(WhitelistType, graphql_name="whitelistType")
    roaming = sgqlc.types.Field(Boolean, graphql_name="roaming")
    reference = sgqlc.types.Field(String, graphql_name="reference")


class ChargeGroup(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "name",
        "info",
        "accessible_for_public_use",
        "direct_payments_enabled",
        "accessible_for_roaming",
        "social_charging_available",
        "type",
        "smart_charging_opt_out_allowed",
        "tariff",
        "prepaid_tariff",
        "anonymous_tariff",
        "tariff_vat",
        "prepaid_tariff_vat",
        "anonymous_tariff_vat",
        "user_group",
        "charge_stations",
        "customers",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")
    info = sgqlc.types.Field(String, graphql_name="info")
    accessible_for_public_use = sgqlc.types.Field(
        Boolean, graphql_name="accessibleForPublicUse"
    )
    direct_payments_enabled = sgqlc.types.Field(
        Boolean, graphql_name="directPaymentsEnabled"
    )
    accessible_for_roaming = sgqlc.types.Field(
        Boolean, graphql_name="accessibleForRoaming"
    )
    social_charging_available = sgqlc.types.Field(
        Boolean, graphql_name="socialChargingAvailable"
    )
    type = sgqlc.types.Field(ChargeGroupType, graphql_name="type")
    smart_charging_opt_out_allowed = sgqlc.types.Field(
        Boolean, graphql_name="smartChargingOptOutAllowed"
    )
    tariff = sgqlc.types.Field("Tariff", graphql_name="tariff")
    prepaid_tariff = sgqlc.types.Field("Tariff", graphql_name="prepaidTariff")
    anonymous_tariff = sgqlc.types.Field("Tariff", graphql_name="anonymousTariff")
    tariff_vat = sgqlc.types.Field("TariffResult", graphql_name="tariffVat")
    prepaid_tariff_vat = sgqlc.types.Field(
        "TariffResult", graphql_name="prepaidTariffVat"
    )
    anonymous_tariff_vat = sgqlc.types.Field(
        "TariffResult", graphql_name="anonymousTariffVat"
    )
    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    charge_stations = sgqlc.types.Field(
        "ChargeStationCollection",
        graphql_name="chargeStations",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        ChargeStationFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(
                        ChargeStationSort, graphql_name="sort", default=None
                    ),
                ),
            )
        ),
    )
    customers = sgqlc.types.Field(
        sgqlc.types.list_of("ChargeGroupCustomer"), graphql_name="customers"
    )


class ChargeGroupCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(ChargeGroup), graphql_name="items")
    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")


class ChargeGroupCustomer(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "first_name",
        "last_name",
        "company_name",
        "type",
        "user_group",
        "tariff",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    first_name = sgqlc.types.Field(String, graphql_name="firstName")
    last_name = sgqlc.types.Field(String, graphql_name="lastName")
    company_name = sgqlc.types.Field(String, graphql_name="companyName")
    type = sgqlc.types.Field(CustomerType, graphql_name="type")
    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    tariff = sgqlc.types.Field("LmsTariff", graphql_name="tariff")


class ChargeStation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "name",
        "reference",
        "comm_id",
        "comm_key",
        "comm_medium",
        "comm_mode",
        "comm_status",
        "comm_version",
        "cost_center_number",
        "state",
        "physical_number",
        "gps_address",
        "gps_city",
        "gps_country",
        "last_communication_date",
        "channels",
        "parameter_set",
        "charge_group",
        "owner",
        "usergroup",
        "location",
        "sim_number",
        "software_version",
        "activation_date",
        "subscriptions",
        "manufacturer_type",
        "parameters",
        "payer_subscription",
        "recipient_charge_transactions",
        "access_options",
        "home_charging_compensation",
        "transactions",
        "tickets",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    reference = sgqlc.types.Field(String, graphql_name="reference")
    comm_id = sgqlc.types.Field(String, graphql_name="commId")
    comm_key = sgqlc.types.Field(String, graphql_name="commKey")
    comm_medium = sgqlc.types.Field(String, graphql_name="commMedium")
    comm_mode = sgqlc.types.Field(String, graphql_name="commMode")
    comm_status = sgqlc.types.Field(String, graphql_name="commStatus")
    comm_version = sgqlc.types.Field(Float, graphql_name="commVersion")
    cost_center_number = sgqlc.types.Field(String, graphql_name="costCenterNumber")
    state = sgqlc.types.Field(ChargeStationState, graphql_name="state")
    physical_number = sgqlc.types.Field(String, graphql_name="physicalNumber")
    gps_address = sgqlc.types.Field(String, graphql_name="gpsAddress")
    gps_city = sgqlc.types.Field(String, graphql_name="gpsCity")
    gps_country = sgqlc.types.Field("Country", graphql_name="gpsCountry")
    last_communication_date = sgqlc.types.Field(
        String, graphql_name="lastCommunicationDate"
    )
    channels = sgqlc.types.Field(
        sgqlc.types.list_of("ChargeStationChannel"), graphql_name="channels"
    )
    parameter_set = sgqlc.types.Field("ParameterSet", graphql_name="parameterSet")
    charge_group = sgqlc.types.Field(ChargeGroup, graphql_name="chargeGroup")
    owner = sgqlc.types.Field("Customer", graphql_name="owner")
    usergroup = sgqlc.types.Field("UserGroup", graphql_name="usergroup")
    location = sgqlc.types.Field("Location", graphql_name="location")
    sim_number = sgqlc.types.Field(String, graphql_name="simNumber")
    software_version = sgqlc.types.Field(String, graphql_name="softwareVersion")
    activation_date = sgqlc.types.Field(String, graphql_name="activationDate")
    subscriptions = sgqlc.types.Field(
        sgqlc.types.list_of("LmsSubscription"), graphql_name="subscriptions"
    )
    manufacturer_type = sgqlc.types.Field(
        "ManufacturerType", graphql_name="manufacturerType"
    )
    parameters = sgqlc.types.Field(
        sgqlc.types.list_of("ChargeStationParameter"), graphql_name="parameters"
    )
    payer_subscription = sgqlc.types.Field("Customer", graphql_name="payerSubscription")
    recipient_charge_transactions = sgqlc.types.Field(
        "Customer", graphql_name="recipientChargeTransactions"
    )
    access_options = sgqlc.types.Field(
        sgqlc.types.non_null(AccessOptions), graphql_name="accessOptions"
    )
    home_charging_compensation = sgqlc.types.Field(
        "HomeChargingCompensation", graphql_name="homeChargingCompensation"
    )
    transactions = sgqlc.types.Field(
        "TransactionCollection",
        graphql_name="transactions",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        TransactionFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(TransactionSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    tickets = sgqlc.types.Field(
        "TicketCollection",
        graphql_name="tickets",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(TicketFilter, graphql_name="filters", default=None),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(TicketSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )


class ChargeStationChannel(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "channel_no",
        "meter_id",
        "obis_code",
        "auto_connector",
        "connector_type",
        "phases",
        "amp",
        "power",
        "voltage",
        "ac_dc",
        "negate_meter",
        "last_status_change_date",
        "physical_number",
        "connector_format",
        "hubject_compatible",
        "evse_id",
        "evse_id_clean",
        "qr_code",
        "qr_code_full",
        "capabilities",
        "global_status",
        "statuses",
        "charge_station",
        "channel_profile",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    channel_no = sgqlc.types.Field(Int, graphql_name="channelNo")
    meter_id = sgqlc.types.Field(String, graphql_name="meterId")
    obis_code = sgqlc.types.Field(String, graphql_name="obisCode")
    auto_connector = sgqlc.types.Field(Boolean, graphql_name="autoConnector")
    connector_type = sgqlc.types.Field(
        ChargeStationChannelConnectorType, graphql_name="connectorType"
    )
    phases = sgqlc.types.Field(Int, graphql_name="phases")
    amp = sgqlc.types.Field(Int, graphql_name="amp")
    power = sgqlc.types.Field(Int, graphql_name="power")
    voltage = sgqlc.types.Field(Int, graphql_name="voltage")
    ac_dc = sgqlc.types.Field(ChargeStationChannelAcDc, graphql_name="acDc")
    negate_meter = sgqlc.types.Field(Boolean, graphql_name="negateMeter")
    last_status_change_date = sgqlc.types.Field(
        String, graphql_name="lastStatusChangeDate"
    )
    physical_number = sgqlc.types.Field(String, graphql_name="physicalNumber")
    connector_format = sgqlc.types.Field(
        ChargeStationChannelConnectorFormat, graphql_name="connectorFormat"
    )
    hubject_compatible = sgqlc.types.Field(Boolean, graphql_name="hubjectCompatible")
    evse_id = sgqlc.types.Field(String, graphql_name="evseId")
    evse_id_clean = sgqlc.types.Field(String, graphql_name="evseIdClean")
    qr_code = sgqlc.types.Field(String, graphql_name="qrCode")
    qr_code_full = sgqlc.types.Field(String, graphql_name="qrCodeFull")
    capabilities = sgqlc.types.Field(
        sgqlc.types.list_of(ChargeStationChannelCapability), graphql_name="capabilities"
    )
    global_status = sgqlc.types.Field(
        ChargeStationChannelGlobalStatus, graphql_name="globalStatus"
    )
    statuses = sgqlc.types.Field(
        sgqlc.types.list_of(ChargeStationChannelStatus), graphql_name="statuses"
    )
    charge_station = sgqlc.types.Field(ChargeStation, graphql_name="chargeStation")
    channel_profile = sgqlc.types.Field(String, graphql_name="channelProfile")


class ChargeStationCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(ChargeStation), graphql_name="items")
    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")


class ChargeStationParameter(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "charge_station",
        "parameter_info",
        "value",
        "boot",
        "is_default",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    charge_station = sgqlc.types.Field(ChargeStation, graphql_name="chargeStation")
    parameter_info = sgqlc.types.Field(
        "ChargeStationParameterInfo", graphql_name="parameterInfo"
    )
    value = sgqlc.types.Field(String, graphql_name="value")
    boot = sgqlc.types.Field(Boolean, graphql_name="boot")
    is_default = sgqlc.types.Field(Boolean, graphql_name="isDefault")


class ChargeStationParameterInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "name",
        "full_name",
        "type",
        "min_value",
        "max_value",
        "flags",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")
    full_name = sgqlc.types.Field(String, graphql_name="fullName")
    type = sgqlc.types.Field(String, graphql_name="type")
    min_value = sgqlc.types.Field(String, graphql_name="minValue")
    max_value = sgqlc.types.Field(String, graphql_name="maxValue")
    flags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="flags")


class ChargeStationSchedule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "chargepoint_id",
        "time_zone",
        "randomized_delay",
        "net_balanced_charging",
        "schedule_blocks",
    )
    chargepoint_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="chargepointId"
    )
    time_zone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="timeZone")
    randomized_delay = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="randomizedDelay"
    )
    net_balanced_charging = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="netBalancedCharging"
    )
    schedule_blocks = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("ScheduleBlock"))
        ),
        graphql_name="scheduleBlocks",
    )


class ChargeTimes(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("start_time", "stop_time")
    start_time = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="startTime"
    )
    stop_time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="stopTime")


class ConnectorExtras(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("tariffs", "vat")
    tariffs = sgqlc.types.Field("ConnectorExtrasTariffs", graphql_name="tariffs")
    vat = sgqlc.types.Field(Float, graphql_name="vat")


class ConnectorExtrasTariffs(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("common", "prepaid", "anonymous")
    common = sgqlc.types.Field(String, graphql_name="common")
    prepaid = sgqlc.types.Field(String, graphql_name="prepaid")
    anonymous = sgqlc.types.Field(String, graphql_name="anonymous")


class Connectors(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "standard",
        "format",
        "power_type",
        "voltage",
        "amperage",
        "vat",
        "max_electric_power",
        "tariff_ids",
        "extras",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    standard = sgqlc.types.Field(
        sgqlc.types.non_null(ConnectorType), graphql_name="standard"
    )
    format = sgqlc.types.Field(
        sgqlc.types.non_null(ConnectorFormat), graphql_name="format"
    )
    power_type = sgqlc.types.Field(
        sgqlc.types.non_null(PowerType), graphql_name="powerType"
    )
    voltage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="voltage")
    amperage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="amperage")
    vat = sgqlc.types.Field(Float, graphql_name="vat")
    max_electric_power = sgqlc.types.Field(Float, graphql_name="maxElectricPower")
    tariff_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="tariffIds"
    )
    extras = sgqlc.types.Field(ConnectorExtras, graphql_name="extras")


class Country(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "code",
        "code3_chars",
        "name",
        "local_name",
        "phone_country_code",
        "currency",
        "default_time_zone",
        "default_interface_language",
        "default_language",
        "languages",
        "vat_union",
        "outside_vat_union_vat_applicable",
    )
    code = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="code")
    code3_chars = sgqlc.types.Field(String, graphql_name="code3Chars")
    name = sgqlc.types.Field(String, graphql_name="name")
    local_name = sgqlc.types.Field(String, graphql_name="localName")
    phone_country_code = sgqlc.types.Field(Int, graphql_name="phoneCountryCode")
    currency = sgqlc.types.Field("Currency", graphql_name="currency")
    default_time_zone = sgqlc.types.Field(String, graphql_name="defaultTimeZone")
    default_interface_language = sgqlc.types.Field(
        "CountryLanguage", graphql_name="defaultInterfaceLanguage"
    )
    default_language = sgqlc.types.Field(
        "CountryLanguage", graphql_name="defaultLanguage"
    )
    languages = sgqlc.types.Field(
        sgqlc.types.list_of("CountryLanguage"), graphql_name="languages"
    )
    vat_union = sgqlc.types.Field(String, graphql_name="vatUnion")
    outside_vat_union_vat_applicable = sgqlc.types.Field(
        Boolean, graphql_name="outsideVatUnionVatApplicable"
    )


class CountryCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(Country), graphql_name="items")
    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")


class CountryLanguage(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "code",
        "code2_chars",
        "code3_chars",
        "name",
        "country",
        "supported",
    )
    code = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="code")
    code2_chars = sgqlc.types.Field(String, graphql_name="code2Chars")
    code3_chars = sgqlc.types.Field(String, graphql_name="code3Chars")
    name = sgqlc.types.Field(String, graphql_name="name")
    country = sgqlc.types.Field(Country, graphql_name="country")
    supported = sgqlc.types.Field(Boolean, graphql_name="supported")


class CountryLanguageCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(
        sgqlc.types.list_of(CountryLanguage), graphql_name="items"
    )
    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")


class CreateScheduleResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("uuid", "name", "payload", "created_at")
    uuid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="uuid")
    name = sgqlc.types.Field(sgqlc.types.non_null(ScheduleName), graphql_name="name")
    payload = sgqlc.types.Field("SchedulePayload", graphql_name="payload")
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name="createdAt")


class Currency(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("code", "symbol", "name", "supported")
    code = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="code")
    symbol = sgqlc.types.Field(String, graphql_name="symbol")
    name = sgqlc.types.Field(String, graphql_name="name")
    supported = sgqlc.types.Field(Boolean, graphql_name="supported")


class CurrencyCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(Currency), graphql_name="items")
    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")


class Customer(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "usergroup_name",
        "user_group",
        "object_id",
        "type",
        "salutation",
        "first_name",
        "last_name",
        "company_name",
        "company",
        "gender",
        "email",
        "user_name",
        "username",
        "street",
        "street_number",
        "street_number_ext",
        "zip_code",
        "city",
        "country",
        "country_details",
        "preferred_language",
        "time_zone",
        "phone",
        "mobile",
        "agreement_condition",
        "agreement_conditions",
        "state",
        "reimbursement_mode",
        "electronic_invoice",
        "public_rech_groups",
        "receive_newsletters",
        "send_email",
        "disabled_login",
        "info",
        "cost_center_number",
        "reference",
        "invoice_name",
        "invoice_street",
        "invoice_street_number",
        "invoice_street_number_ext",
        "invoice_zip_code",
        "invoice_city",
        "invoice_country",
        "invoice_email",
        "invoice_reference",
        "billing_account_number",
        "bic",
        "billing_account_name",
        "license_plate",
        "charge_stations",
        "mandate",
        "bacs_mandate",
        "is_invoice_address_different",
        "provider_category",
        "cards",
        "transactions",
        "invoices",
        "tickets",
        "srs_onboarding_complete",
        "effective_app_features",
        "is_shell_user",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    usergroup_name = sgqlc.types.Field(String, graphql_name="usergroupName")
    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    object_id = sgqlc.types.Field(String, graphql_name="objectId")
    type = sgqlc.types.Field(sgqlc.types.non_null(CustomerType), graphql_name="type")
    salutation = sgqlc.types.Field(CustomerSalutation, graphql_name="salutation")
    first_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="firstName"
    )
    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="lastName")
    company_name = sgqlc.types.Field(String, graphql_name="companyName")
    company = sgqlc.types.Field(String, graphql_name="company")
    gender = sgqlc.types.Field(String, graphql_name="gender")
    email = sgqlc.types.Field(String, graphql_name="email")
    user_name = sgqlc.types.Field(String, graphql_name="userName")
    username = sgqlc.types.Field(String, graphql_name="username")
    street = sgqlc.types.Field(String, graphql_name="street")
    street_number = sgqlc.types.Field(String, graphql_name="streetNumber")
    street_number_ext = sgqlc.types.Field(String, graphql_name="streetNumberExt")
    zip_code = sgqlc.types.Field(String, graphql_name="zipCode")
    city = sgqlc.types.Field(String, graphql_name="city")
    country = sgqlc.types.Field(String, graphql_name="country")
    country_details = sgqlc.types.Field(Country, graphql_name="countryDetails")
    preferred_language = sgqlc.types.Field(
        CountryLanguage, graphql_name="preferredLanguage"
    )
    time_zone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="timeZone")
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="phone")
    mobile = sgqlc.types.Field(String, graphql_name="mobile")
    agreement_condition = sgqlc.types.Field(Boolean, graphql_name="agreementCondition")
    agreement_conditions = sgqlc.types.Field(
        Boolean, graphql_name="agreementConditions"
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(CustomerState), graphql_name="state")
    reimbursement_mode = sgqlc.types.Field(
        sgqlc.types.non_null(CustomerReimbursementMode),
        graphql_name="reimbursementMode",
    )
    electronic_invoice = sgqlc.types.Field(
        sgqlc.types.non_null(CustomerElectronicInvoice),
        graphql_name="electronicInvoice",
    )
    public_rech_groups = sgqlc.types.Field(Boolean, graphql_name="publicRechGroups")
    receive_newsletters = sgqlc.types.Field(Boolean, graphql_name="receiveNewsletters")
    send_email = sgqlc.types.Field(Boolean, graphql_name="sendEmail")
    disabled_login = sgqlc.types.Field(Boolean, graphql_name="disabledLogin")
    info = sgqlc.types.Field(String, graphql_name="info")
    cost_center_number = sgqlc.types.Field(String, graphql_name="costCenterNumber")
    reference = sgqlc.types.Field(String, graphql_name="reference")
    invoice_name = sgqlc.types.Field(String, graphql_name="invoiceName")
    invoice_street = sgqlc.types.Field(String, graphql_name="invoiceStreet")
    invoice_street_number = sgqlc.types.Field(
        String, graphql_name="invoiceStreetNumber"
    )
    invoice_street_number_ext = sgqlc.types.Field(
        String, graphql_name="invoiceStreetNumberExt"
    )
    invoice_zip_code = sgqlc.types.Field(String, graphql_name="invoiceZipCode")
    invoice_city = sgqlc.types.Field(String, graphql_name="invoiceCity")
    invoice_country = sgqlc.types.Field(Country, graphql_name="invoiceCountry")
    invoice_email = sgqlc.types.Field(String, graphql_name="invoiceEmail")
    invoice_reference = sgqlc.types.Field(String, graphql_name="invoiceReference")
    billing_account_number = sgqlc.types.Field(
        String, graphql_name="billingAccountNumber"
    )
    bic = sgqlc.types.Field(String, graphql_name="bic")
    billing_account_name = sgqlc.types.Field(String, graphql_name="billingAccountName")
    license_plate = sgqlc.types.Field(String, graphql_name="licensePlate")
    charge_stations = sgqlc.types.Field(
        sgqlc.types.list_of(ChargeStation), graphql_name="chargeStations"
    )
    mandate = sgqlc.types.Field("CustomerMandate", graphql_name="mandate")
    bacs_mandate = sgqlc.types.Field("CustomerBacsMandate", graphql_name="bacsMandate")
    is_invoice_address_different = sgqlc.types.Field(
        Boolean, graphql_name="isInvoiceAddressDifferent"
    )
    provider_category = sgqlc.types.Field(
        ProviderCategory, graphql_name="providerCategory"
    )
    cards = sgqlc.types.Field(sgqlc.types.list_of(Card), graphql_name="cards")
    transactions = sgqlc.types.Field(
        "TransactionCollection",
        graphql_name="transactions",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        TransactionFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(TransactionSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    invoices = sgqlc.types.Field(
        "InvoiceCollection",
        graphql_name="invoices",
        args=sgqlc.types.ArgDict(
            (
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
                (
                    "items_per_page",
                    sgqlc.types.Arg(Int, graphql_name="itemsPerPage", default=None),
                ),
                (
                    "filters",
                    sgqlc.types.Arg(
                        InvoiceFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(InvoiceSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    tickets = sgqlc.types.Field(
        "TicketCollection",
        graphql_name="tickets",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(TicketFilter, graphql_name="filters", default=None),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(TicketSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    srs_onboarding_complete = sgqlc.types.Field(
        Boolean, graphql_name="srsOnboardingComplete"
    )
    effective_app_features = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EffectiveAppFeature")),
        graphql_name="effectiveAppFeatures",
        args=sgqlc.types.ArgDict(
            (
                (
                    "app_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="appId", default=None
                    ),
                ),
            )
        ),
    )
    is_shell_user = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isShellUser"
    )


class CustomerBacsMandate(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "bank_account_no",
        "bank_sort_code",
        "mandate_reference",
        "status",
        "start_date",
        "end_date",
        "email",
        "first_name",
        "last_name",
        "company_name",
        "address",
        "city",
        "zip",
        "country",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    bank_account_no = sgqlc.types.Field(String, graphql_name="bankAccountNo")
    bank_sort_code = sgqlc.types.Field(String, graphql_name="bankSortCode")
    mandate_reference = sgqlc.types.Field(String, graphql_name="mandateReference")
    status = sgqlc.types.Field(String, graphql_name="status")
    start_date = sgqlc.types.Field(String, graphql_name="startDate")
    end_date = sgqlc.types.Field(String, graphql_name="endDate")
    email = sgqlc.types.Field(String, graphql_name="email")
    first_name = sgqlc.types.Field(String, graphql_name="firstName")
    last_name = sgqlc.types.Field(String, graphql_name="lastName")
    company_name = sgqlc.types.Field(String, graphql_name="companyName")
    address = sgqlc.types.Field(String, graphql_name="address")
    city = sgqlc.types.Field(String, graphql_name="city")
    zip = sgqlc.types.Field(String, graphql_name="zip")
    country = sgqlc.types.Field(String, graphql_name="country")


class CustomerCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(Customer), graphql_name="items")
    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")


class CustomerFeature(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("user_id", "enabled", "app", "app_features", "feature_key")
    user_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="user_id")
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")
    app = sgqlc.types.Field(sgqlc.types.non_null(AppIdentifier), graphql_name="app")
    app_features = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AppFeature))),
        graphql_name="appFeatures",
        args=sgqlc.types.ArgDict(
            (
                (
                    "app_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="appId", default=None
                    ),
                ),
            )
        ),
    )
    feature_key = sgqlc.types.Field(
        sgqlc.types.non_null("FeatureKey"), graphql_name="featureKey"
    )


class CustomerMandate(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "accepted",
        "customer",
        "stop_date",
        "billing_account_number",
        "bic",
        "billing_account_name",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    accepted = sgqlc.types.Field(Boolean, graphql_name="accepted")
    customer = sgqlc.types.Field(Customer, graphql_name="customer")
    stop_date = sgqlc.types.Field(String, graphql_name="stopDate")
    billing_account_number = sgqlc.types.Field(
        String, graphql_name="billingAccountNumber"
    )
    bic = sgqlc.types.Field(String, graphql_name="bic")
    billing_account_name = sgqlc.types.Field(String, graphql_name="billingAccountName")


class DisplayText(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("language", "text")
    language = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="language")
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="text")


class EffectiveAppFeature(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("key", "enabled", "source")
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="key")
    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")
    source = sgqlc.types.Field(
        sgqlc.types.non_null(FeatureSource), graphql_name="source"
    )


class EnergyMix(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("is_green_energy",)
    is_green_energy = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isGreenEnergy"
    )


class EnergySource(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("source", "percentage")
    source = sgqlc.types.Field(EnergySourceCategory, graphql_name="source")
    percentage = sgqlc.types.Field(Float, graphql_name="percentage")


class EnvironmentalImpact(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("category", "amount")
    category = sgqlc.types.Field(
        sgqlc.types.non_null(EnvironmentalImpactCategory), graphql_name="category"
    )
    amount = sgqlc.types.Field(Float, graphql_name="amount")


class Evse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "uid",
        "evse_id",
        "status",
        "connectors",
        "capabilities",
        "payment_methods",
    )
    uid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="uid")
    evse_id = sgqlc.types.Field(String, graphql_name="evseId")
    status = sgqlc.types.Field(sgqlc.types.non_null(EvseStatus), graphql_name="status")
    connectors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Connectors))),
        graphql_name="connectors",
    )
    capabilities = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Capability)),
        graphql_name="capabilities",
    )
    payment_methods = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("EvsePaymentMethod")),
        graphql_name="paymentMethods",
    )


class EvsePaymentConditions(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("conditions_id", "conditions_link_pdf", "conditions_link_html")
    conditions_id = sgqlc.types.Field(ID, graphql_name="conditionsId")
    conditions_link_pdf = sgqlc.types.Field(String, graphql_name="conditionsLinkPdf")
    conditions_link_html = sgqlc.types.Field(String, graphql_name="conditionsLinkHtml")


class EvsePaymentConditionsWebApp(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("conditions_id", "conditions_link_pdf", "conditions_link_html")
    conditions_id = sgqlc.types.Field(ID, graphql_name="conditionsId")
    conditions_link_pdf = sgqlc.types.Field(String, graphql_name="conditionsLinkPdf")
    conditions_link_html = sgqlc.types.Field(String, graphql_name="conditionsLinkHtml")


class EvsePaymentMethod(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "type",
        "name",
        "conditions",
        "conditions_web_app",
        "authorisation_amount",
        "direct_payment_surcharge",
    )
    type = sgqlc.types.Field(Float, graphql_name="type")
    name = sgqlc.types.Field(String, graphql_name="name")
    conditions = sgqlc.types.Field(EvsePaymentConditions, graphql_name="conditions")
    conditions_web_app = sgqlc.types.Field(
        EvsePaymentConditionsWebApp, graphql_name="conditionsWebApp"
    )
    authorisation_amount = sgqlc.types.Field(Float, graphql_name="authorisationAmount")
    direct_payment_surcharge = sgqlc.types.Field(
        Float, graphql_name="directPaymentSurcharge"
    )


class FeatureKey(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "feature_key",
        "description",
        "app_features",
        "customer_features",
    )
    feature_key = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="featureKey"
    )
    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )
    app_features = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AppFeature)),
        graphql_name="appFeatures",
    )
    customer_features = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CustomerFeature)),
        graphql_name="customerFeatures",
    )


class HomeChargingCompensation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("hcc_enabled", "hcc_tariff", "hcc_cards")
    hcc_enabled = sgqlc.types.Field(Boolean, graphql_name="hccEnabled")
    hcc_tariff = sgqlc.types.Field(Float, graphql_name="hccTariff")
    hcc_cards = sgqlc.types.Field(sgqlc.types.list_of(Card), graphql_name="hccCards")


class Invoice(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "invoice_uuid",
        "credit",
        "billing_type",
        "vat_type",
        "country",
        "date",
        "customer",
        "payment_method",
        "payment_reference",
        "currency",
        "cust_currency",
        "amount_excl_vat",
        "vat_amount",
        "amount_incl_vat",
        "cust_price_incl_vat",
        "regenerated",
        "status",
        "type",
        "vat_number",
        "invoice_product_details",
        "items",
        "transactions",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    invoice_uuid = sgqlc.types.Field(String, graphql_name="invoiceUuid")
    credit = sgqlc.types.Field(Boolean, graphql_name="credit")
    billing_type = sgqlc.types.Field(InvoiceBillingType, graphql_name="billingType")
    vat_type = sgqlc.types.Field(InvoiceVatType, graphql_name="vatType")
    country = sgqlc.types.Field(Country, graphql_name="country")
    date = sgqlc.types.Field(String, graphql_name="date")
    customer = sgqlc.types.Field(Customer, graphql_name="customer")
    payment_method = sgqlc.types.Field(
        InvoicePaymentMethod, graphql_name="paymentMethod"
    )
    payment_reference = sgqlc.types.Field(String, graphql_name="paymentReference")
    currency = sgqlc.types.Field(Currency, graphql_name="currency")
    cust_currency = sgqlc.types.Field(Currency, graphql_name="custCurrency")
    amount_excl_vat = sgqlc.types.Field(Float, graphql_name="amountExclVAT")
    vat_amount = sgqlc.types.Field(Float, graphql_name="vatAmount")
    amount_incl_vat = sgqlc.types.Field(Float, graphql_name="amountInclVat")
    cust_price_incl_vat = sgqlc.types.Field(Float, graphql_name="custPriceInclVat")
    regenerated = sgqlc.types.Field(Boolean, graphql_name="regenerated")
    status = sgqlc.types.Field(InvoiceStatus, graphql_name="status")
    type = sgqlc.types.Field(InvoiceType, graphql_name="type")
    vat_number = sgqlc.types.Field(String, graphql_name="vatNumber")
    invoice_product_details = sgqlc.types.Field(
        String, graphql_name="invoiceProductDetails"
    )
    items = sgqlc.types.Field(sgqlc.types.list_of("InvoiceItem"), graphql_name="items")
    transactions = sgqlc.types.Field(
        "TransactionCollection",
        graphql_name="transactions",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        TransactionFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(TransactionSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )


class InvoiceCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(Invoice), graphql_name="items")
    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")


class InvoiceItem(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "invoice",
        "product_name",
        "number",
        "number_text",
        "full_unit_price_excl_vat",
        "discount_percentage",
        "vat_percentage",
        "vat_type",
        "full_unit_price_excl_vat_cust_currency",
        "conversion_fee_amount",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    invoice = sgqlc.types.Field(Invoice, graphql_name="invoice")
    product_name = sgqlc.types.Field(String, graphql_name="productName")
    number = sgqlc.types.Field(Int, graphql_name="number")
    number_text = sgqlc.types.Field(String, graphql_name="numberText")
    full_unit_price_excl_vat = sgqlc.types.Field(
        Float, graphql_name="fullUnitPriceExclVat"
    )
    discount_percentage = sgqlc.types.Field(Float, graphql_name="discountPercentage")
    vat_percentage = sgqlc.types.Field(Float, graphql_name="vatPercentage")
    vat_type = sgqlc.types.Field(InvoiceVatType, graphql_name="vatType")
    full_unit_price_excl_vat_cust_currency = sgqlc.types.Field(
        Float, graphql_name="fullUnitPriceExclVatCustCurrency"
    )
    conversion_fee_amount = sgqlc.types.Field(Float, graphql_name="conversionFeeAmount")


class JwtToken(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("access_token", "token_type", "expires_in")
    access_token = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="access_token"
    )
    token_type = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="token_type"
    )
    expires_in = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="expires_in")


class LegacyTariff(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "tariff_id",
        "currency",
        "min_price",
        "max_price",
        "excl_service_provider_costs",
        "free",
        "timeslots",
        "exchange_rate",
        "conversion_fee",
        "msp_currency",
    )
    tariff_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="tariffId")
    currency = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="currency")
    min_price = sgqlc.types.Field(Float, graphql_name="minPrice")
    max_price = sgqlc.types.Field(Float, graphql_name="maxPrice")
    excl_service_provider_costs = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="exclServiceProviderCosts"
    )
    free = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="free")
    timeslots = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("LegacyTariffTimeslot"))
        ),
        graphql_name="timeslots",
    )
    exchange_rate = sgqlc.types.Field(Float, graphql_name="exchangeRate")
    conversion_fee = sgqlc.types.Field(Float, graphql_name="conversionFee")
    msp_currency = sgqlc.types.Field(String, graphql_name="mspCurrency")


class LegacyTariffItem(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("type", "price")
    type = sgqlc.types.Field(
        sgqlc.types.non_null(LegacyTariffItemType), graphql_name="type"
    )
    price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="price")


class LegacyTariffTimeslot(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "timeslot_no",
        "days_of_week",
        "start_period_valid",
        "end_period_valid",
        "start_time_of_day",
        "end_time_of_day",
        "vehicle_full",
        "full_threshold",
        "min_energy",
        "max_energy",
        "min_power",
        "max_power",
        "min_duration",
        "max_duration",
        "always",
        "items",
    )
    timeslot_no = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="timeslotNo"
    )
    days_of_week = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(LegacyTariffTimeslotDayOfWeek)),
        graphql_name="daysOfWeek",
    )
    start_period_valid = sgqlc.types.Field(String, graphql_name="startPeriodValid")
    end_period_valid = sgqlc.types.Field(String, graphql_name="endPeriodValid")
    start_time_of_day = sgqlc.types.Field(String, graphql_name="startTimeOfDay")
    end_time_of_day = sgqlc.types.Field(String, graphql_name="endTimeOfDay")
    vehicle_full = sgqlc.types.Field(Boolean, graphql_name="vehicleFull")
    full_threshold = sgqlc.types.Field(Int, graphql_name="fullThreshold")
    min_energy = sgqlc.types.Field(Int, graphql_name="minEnergy")
    max_energy = sgqlc.types.Field(Int, graphql_name="maxEnergy")
    min_power = sgqlc.types.Field(Int, graphql_name="minPower")
    max_power = sgqlc.types.Field(Int, graphql_name="maxPower")
    min_duration = sgqlc.types.Field(Int, graphql_name="minDuration")
    max_duration = sgqlc.types.Field(Int, graphql_name="maxDuration")
    always = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="always")
    items = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(LegacyTariffItem))
        ),
        graphql_name="items",
    )


class LiveKitTokenResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("token", "live_kit_room_url", "name")
    token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="token")
    live_kit_room_url = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="liveKitRoomUrl"
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class LmsLocationsResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "has_more")
    items = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("Location"))),
        graphql_name="items",
    )
    has_more = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="hasMore")


class LmsPayment(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "extern_id",
        "amount",
        "vat_percentage",
        "type",
        "extern_payment_transaction_id",
        "payment_date",
        "remarks",
        "payer_id",
        "billing_account_no",
        "status",
        "creation_date",
        "refund",
        "locale",
        "payment_id",
        "description",
        "invoice_id",
        "bank_file_id",
        "billing_profile_id",
        "back_url",
        "info",
        "sub_type",
        "customer_id",
        "recurrent_prepaid_payment_id",
        "recurrent_prepaid_payment_pin",
        "handle_remarks",
        "conditions_id",
        "currency",
        "authorized_amount",
        "target_amount",
        "app_device_id",
        "payment_method",
        "privacy_policy_read",
        "user_email_address",
        "send_invoice_consent",
        "send_payment_confirmation_email",
        "app_status",
        "receipt_link",
    )
    id = sgqlc.types.Field(String, graphql_name="id")
    extern_id = sgqlc.types.Field(String, graphql_name="externId")
    amount = sgqlc.types.Field(Float, graphql_name="amount")
    vat_percentage = sgqlc.types.Field(Float, graphql_name="vatPercentage")
    type = sgqlc.types.Field(Int, graphql_name="type")
    extern_payment_transaction_id = sgqlc.types.Field(
        String, graphql_name="externPaymentTransactionId"
    )
    payment_date = sgqlc.types.Field(String, graphql_name="paymentDate")
    remarks = sgqlc.types.Field(String, graphql_name="remarks")
    payer_id = sgqlc.types.Field(String, graphql_name="payerId")
    billing_account_no = sgqlc.types.Field(String, graphql_name="billingAccountNo")
    status = sgqlc.types.Field(Int, graphql_name="status")
    creation_date = sgqlc.types.Field(String, graphql_name="creationDate")
    refund = sgqlc.types.Field(Float, graphql_name="refund")
    locale = sgqlc.types.Field(String, graphql_name="locale")
    payment_id = sgqlc.types.Field(String, graphql_name="paymentId")
    description = sgqlc.types.Field(String, graphql_name="description")
    invoice_id = sgqlc.types.Field(String, graphql_name="invoiceId")
    bank_file_id = sgqlc.types.Field(String, graphql_name="bankFileId")
    billing_profile_id = sgqlc.types.Field(Int, graphql_name="billingProfileId")
    back_url = sgqlc.types.Field(String, graphql_name="backUrl")
    info = sgqlc.types.Field(String, graphql_name="info")
    sub_type = sgqlc.types.Field(String, graphql_name="subType")
    customer_id = sgqlc.types.Field(Int, graphql_name="customerId")
    recurrent_prepaid_payment_id = sgqlc.types.Field(
        String, graphql_name="recurrentPrepaidPaymentId"
    )
    recurrent_prepaid_payment_pin = sgqlc.types.Field(
        String, graphql_name="recurrentPrepaidPaymentPin"
    )
    handle_remarks = sgqlc.types.Field(String, graphql_name="handleRemarks")
    conditions_id = sgqlc.types.Field(Int, graphql_name="conditionsId")
    currency = sgqlc.types.Field(String, graphql_name="currency")
    authorized_amount = sgqlc.types.Field(Float, graphql_name="authorizedAmount")
    target_amount = sgqlc.types.Field(Float, graphql_name="targetAmount")
    app_device_id = sgqlc.types.Field(String, graphql_name="appDeviceId")
    payment_method = sgqlc.types.Field(String, graphql_name="paymentMethod")
    privacy_policy_read = sgqlc.types.Field(Boolean, graphql_name="privacyPolicyRead")
    user_email_address = sgqlc.types.Field(String, graphql_name="userEmailAddress")
    send_invoice_consent = sgqlc.types.Field(Boolean, graphql_name="sendInvoiceConsent")
    send_payment_confirmation_email = sgqlc.types.Field(
        Boolean, graphql_name="sendPaymentConfirmationEmail"
    )
    app_status = sgqlc.types.Field(String, graphql_name="appStatus")
    receipt_link = sgqlc.types.Field(String, graphql_name="receiptLink")


class LmsPaymentsResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "has_more")
    items = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LmsPayment))),
        graphql_name="items",
    )
    has_more = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="hasMore")


class LmsSubscription(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "type",
        "approved",
        "start_date",
        "end_date",
        "product",
        "charge_station",
        "card",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    type = sgqlc.types.Field(String, graphql_name="type")
    approved = sgqlc.types.Field(Boolean, graphql_name="approved")
    start_date = sgqlc.types.Field(String, graphql_name="startDate")
    end_date = sgqlc.types.Field(String, graphql_name="endDate")
    product = sgqlc.types.Field("Product", graphql_name="product")
    charge_station = sgqlc.types.Field(ChargeStation, graphql_name="chargeStation")
    card = sgqlc.types.Field(Card, graphql_name="card")


class LmsTariff(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")


class LmsTariffsResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "has_more")
    items = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("Tariff"))),
        graphql_name="items",
    )
    has_more = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="hasMore")


class LmsTransaction(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "provider_transaction_id",
        "status",
        "global_status",
        "type",
        "start_date",
        "last_update_date",
        "remote_last_update_date",
        "creation_date",
        "vehicle_full_date",
        "total_energy",
        "total_duration",
        "total_idle_time",
        "profile_type",
        "msp_provider",
        "card_snapshot",
        "customer",
        "customer_reference",
        "location_snapshot",
        "home_charging",
        "cpo_provider",
        "charge_station",
        "cost_center_number_station",
        "charge_station_owner_customer",
        "transaction_prices",
        "transaction_tariff_timeslots",
        "transaction_periods",
        "authorisation",
        "incoming_cdr_file",
        "parent",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    provider_transaction_id = sgqlc.types.Field(
        String, graphql_name="providerTransactionId"
    )
    status = sgqlc.types.Field(
        sgqlc.types.non_null(TransactionStatus), graphql_name="status"
    )
    global_status = sgqlc.types.Field(
        TransactionGlobalStatus, graphql_name="globalStatus"
    )
    type = sgqlc.types.Field(TransactionType, graphql_name="type")
    start_date = sgqlc.types.Field(String, graphql_name="startDate")
    last_update_date = sgqlc.types.Field(String, graphql_name="lastUpdateDate")
    remote_last_update_date = sgqlc.types.Field(
        String, graphql_name="remoteLastUpdateDate"
    )
    creation_date = sgqlc.types.Field(String, graphql_name="creationDate")
    vehicle_full_date = sgqlc.types.Field(String, graphql_name="vehicleFullDate")
    total_energy = sgqlc.types.Field(Float, graphql_name="totalEnergy")
    total_duration = sgqlc.types.Field(Float, graphql_name="totalDuration")
    total_idle_time = sgqlc.types.Field(Float, graphql_name="totalIdleTime")
    profile_type = sgqlc.types.Field(TransactionProfileType, graphql_name="profileType")
    msp_provider = sgqlc.types.Field("Provider", graphql_name="mspProvider")
    card_snapshot = sgqlc.types.Field("TransactionCard", graphql_name="cardSnapshot")
    customer = sgqlc.types.Field(Customer, graphql_name="customer")
    customer_reference = sgqlc.types.Field(String, graphql_name="customerReference")
    location_snapshot = sgqlc.types.Field(
        "TransactionLocation", graphql_name="locationSnapshot"
    )
    home_charging = sgqlc.types.Field(Boolean, graphql_name="homeCharging")
    cpo_provider = sgqlc.types.Field("Provider", graphql_name="cpoProvider")
    charge_station = sgqlc.types.Field(ChargeStation, graphql_name="chargeStation")
    cost_center_number_station = sgqlc.types.Field(
        String, graphql_name="costCenterNumberStation"
    )
    charge_station_owner_customer = sgqlc.types.Field(
        Customer, graphql_name="chargeStationOwnerCustomer"
    )
    transaction_prices = sgqlc.types.Field(
        sgqlc.types.list_of("TransactionPrice"), graphql_name="transactionPrices"
    )
    transaction_tariff_timeslots = sgqlc.types.Field(
        sgqlc.types.list_of("TariffTimeslot"), graphql_name="transactionTariffTimeslots"
    )
    transaction_periods = sgqlc.types.Field(
        sgqlc.types.list_of("TransactionPeriod"), graphql_name="transactionPeriods"
    )
    authorisation = sgqlc.types.Field(Authorisation, graphql_name="authorisation")
    incoming_cdr_file = sgqlc.types.Field(String, graphql_name="incomingCdrFile")
    parent = sgqlc.types.Field("LmsTransaction", graphql_name="parent")


class LmsTransactionsResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "has_more")
    items = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("Transaction"))),
        graphql_name="items",
    )
    has_more = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="hasMore")


class Location(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "ranking",
        "country_code",
        "latitude",
        "longitude",
        "party",
        "name",
        "type",
        "address",
        "city",
        "postal_code",
        "country",
        "evses",
        "operator",
        "distance",
        "evse_uid",
        "evse_uids",
        "connector_id",
        "duration",
        "is_open",
        "evses_operative_count",
        "evses_occupied_count",
        "evses_now_available_count",
        "evses_queued_available_count",
        "evses_total_count",
        "opening_times",
        "energy_mix",
        "country_details",
        "user_group",
        "user_group_name",
        "publish",
        "always_open",
        "time_zone",
        "charging_when_closed",
        "directions",
        "opening_hours_text",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    ranking = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="ranking")
    country_code = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="countryCode"
    )
    latitude = sgqlc.types.Field(Float, graphql_name="latitude")
    longitude = sgqlc.types.Field(Float, graphql_name="longitude")
    party = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="party")
    name = sgqlc.types.Field(String, graphql_name="name")
    type = sgqlc.types.Field(String, graphql_name="type")
    address = sgqlc.types.Field(String, graphql_name="address")
    city = sgqlc.types.Field(String, graphql_name="city")
    postal_code = sgqlc.types.Field(String, graphql_name="postalCode")
    country = sgqlc.types.Field(String, graphql_name="country")
    evses = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Evse))),
        graphql_name="evses",
    )
    operator = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="operator")
    distance = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="distance")
    evse_uid = sgqlc.types.Field(String, graphql_name="evseUid")
    evse_uids = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="evseUids",
    )
    connector_id = sgqlc.types.Field(String, graphql_name="connectorId")
    duration = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="duration")
    is_open = sgqlc.types.Field(Boolean, graphql_name="isOpen")
    evses_operative_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="evsesOperativeCount"
    )
    evses_occupied_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="evsesOccupiedCount"
    )
    evses_now_available_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="evsesNowAvailableCount"
    )
    evses_queued_available_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="evsesQueuedAvailableCount"
    )
    evses_total_count = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="evsesTotalCount"
    )
    opening_times = sgqlc.types.Field(
        "LocationOpeningHours", graphql_name="openingTimes"
    )
    energy_mix = sgqlc.types.Field("LocationEnergyMix", graphql_name="energyMix")
    country_details = sgqlc.types.Field(Country, graphql_name="countryDetails")
    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    user_group_name = sgqlc.types.Field(String, graphql_name="userGroupName")
    publish = sgqlc.types.Field(Boolean, graphql_name="publish")
    always_open = sgqlc.types.Field(Boolean, graphql_name="alwaysOpen")
    time_zone = sgqlc.types.Field(String, graphql_name="timeZone")
    charging_when_closed = sgqlc.types.Field(Boolean, graphql_name="chargingWhenClosed")
    directions = sgqlc.types.Field(String, graphql_name="directions")
    opening_hours_text = sgqlc.types.Field(String, graphql_name="openingHoursText")


class LocationEnergyMix(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "is_green_energy",
        "energy_sources",
        "environ_impact",
        "supplier_name",
        "energy_product_name",
    )
    is_green_energy = sgqlc.types.Field(Boolean, graphql_name="isGreenEnergy")
    energy_sources = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EnergySource)),
        graphql_name="energySources",
    )
    environ_impact = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EnvironmentalImpact)),
        graphql_name="environImpact",
    )
    supplier_name = sgqlc.types.Field(String, graphql_name="supplierName")
    energy_product_name = sgqlc.types.Field(String, graphql_name="energyProductName")


class LocationExceptionalPeriod(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("period_begin", "period_end")
    period_begin = sgqlc.types.Field(DateTimeISO, graphql_name="periodBegin")
    period_end = sgqlc.types.Field(DateTimeISO, graphql_name="periodEnd")


class LocationOpeningHours(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "twentyfourseven",
        "regular_hours",
        "exceptional_openings",
        "exceptional_closings",
    )
    twentyfourseven = sgqlc.types.Field(Boolean, graphql_name="twentyfourseven")
    regular_hours = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("LocationRegularHours")),
        graphql_name="regularHours",
    )
    exceptional_openings = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(LocationExceptionalPeriod)),
        graphql_name="exceptionalOpenings",
    )
    exceptional_closings = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(LocationExceptionalPeriod)),
        graphql_name="exceptionalClosings",
    )


class LocationRegularHours(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("weekday", "period_begin", "period_end")
    weekday = sgqlc.types.Field(Float, graphql_name="weekday")
    period_begin = sgqlc.types.Field(String, graphql_name="period_begin")
    period_end = sgqlc.types.Field(String, graphql_name="period_end")


class ManufacturerType(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "vendor", "model", "is_external", "is_default")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    vendor = sgqlc.types.Field(String, graphql_name="vendor")
    model = sgqlc.types.Field(String, graphql_name="model")
    is_external = sgqlc.types.Field(Boolean, graphql_name="isExternal")
    is_default = sgqlc.types.Field(Boolean, graphql_name="isDefault")


class MigrateTicketsResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("success", "message")
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="success")
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="message")


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "login_fifty_five",
        "update_token_by_id",
        "block_card_by_id",
        "unblock_card_by_id",
        "activate_card_by_id",
        "add_authorized_card",
        "add50five_card",
        "remove_hcc_card",
        "deactivate_card_by_id",
        "unlock_connector",
        "start_transaction",
        "stop_transaction",
        "soft_reset",
        "hard_reset",
        "update_hcc_tariff",
        "update_customer",
        "update_customer_bank_account",
        "update_srs_onboarding_completed",
        "update_access_options",
        "update_public_or_private",
        "update_publish_on_map",
        "create_app_feature",
        "update_app_feature",
        "delete_app_feature",
        "create_customer_feature",
        "update_customer_feature",
        "delete_customer_feature",
        "generate_live_kit_token",
        "solar_charging_enable",
        "reset_charge_station_parameters_cache",
        "update_customer_mandate",
        "end_customer_mandate",
        "create_customer_mandate",
        "end_customer_bacs_mandate",
        "create_customer_bacs_mandate",
        "update_schedule",
        "override_schedule",
        "update_schedule_simple",
        "delete_schedule",
        "update_schedule_complex",
        "net_balanced_charging",
        "update_net_balanced_charging",
        "register_application",
        "bulk_update_cpms_id",
        "create_aivoice_ticket",
        "create_partner",
        "create_ticket",
        "import_lms_tickets",
        "import_lms_customers",
        "send_mail",
        "update_ticket",
        "create_ere_mandate_ticket",
    )
    login_fifty_five = sgqlc.types.Field(
        sgqlc.types.non_null(JwtToken),
        graphql_name="loginFiftyFive",
        args=sgqlc.types.ArgDict(
            (
                (
                    "password",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="password",
                        default=None,
                    ),
                ),
                (
                    "email",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="email", default=None
                    ),
                ),
            )
        ),
    )
    update_token_by_id = sgqlc.types.Field(
        "TokenResponse",
        graphql_name="updateTokenById",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(TokenUpdate, graphql_name="input", default=None),
                ),
            )
        ),
    )
    block_card_by_id = sgqlc.types.Field(
        "TokenResponse",
        graphql_name="blockCardById",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    unblock_card_by_id = sgqlc.types.Field(
        "TokenResponse",
        graphql_name="unblockCardById",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    activate_card_by_id = sgqlc.types.Field(
        "TokenResponse",
        graphql_name="activateCardById",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    add_authorized_card = sgqlc.types.Field(
        "TokenResponse",
        graphql_name="addAuthorizedCard",
        args=sgqlc.types.ArgDict(
            (
                (
                    "external_card_visual_number",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="externalCardVisualNumber",
                        default=None,
                    ),
                ),
                (
                    "roaming_home_charging_enabled",
                    sgqlc.types.Arg(
                        Boolean, graphql_name="roamingHomeChargingEnabled", default=None
                    ),
                ),
                (
                    "customer_id",
                    sgqlc.types.Arg(ID, graphql_name="customerId", default=None),
                ),
            )
        ),
    )
    add50five_card = sgqlc.types.Field(
        "TokenResponse",
        graphql_name="add50fiveCard",
        args=sgqlc.types.ArgDict(
            (
                (
                    "external_card_visual_number",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="externalCardVisualNumber",
                        default=None,
                    ),
                ),
                (
                    "customer_id",
                    sgqlc.types.Arg(ID, graphql_name="customerId", default=None),
                ),
            )
        ),
    )
    remove_hcc_card = sgqlc.types.Field(
        Boolean,
        graphql_name="removeHccCard",
        args=sgqlc.types.ArgDict(
            (
                (
                    "external_card_visual_number",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="externalCardVisualNumber",
                        default=None,
                    ),
                ),
                (
                    "customer_id",
                    sgqlc.types.Arg(ID, graphql_name="customerId", default=None),
                ),
            )
        ),
    )
    deactivate_card_by_id = sgqlc.types.Field(
        "TokenResponse",
        graphql_name="deactivateCardById",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    unlock_connector = sgqlc.types.Field(
        Boolean,
        graphql_name="unlockConnector",
        args=sgqlc.types.ArgDict(
            (
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
                (
                    "channel_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="channelId", default=None
                    ),
                ),
            )
        ),
    )
    start_transaction = sgqlc.types.Field(
        Boolean,
        graphql_name="startTransaction",
        args=sgqlc.types.ArgDict(
            (
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
                (
                    "channel_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="channelId", default=None
                    ),
                ),
                ("card", sgqlc.types.Arg(String, graphql_name="card", default=None)),
            )
        ),
    )
    stop_transaction = sgqlc.types.Field(
        Boolean,
        graphql_name="stopTransaction",
        args=sgqlc.types.ArgDict(
            (
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
                (
                    "channel_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="channelId", default=None
                    ),
                ),
            )
        ),
    )
    soft_reset = sgqlc.types.Field(
        Boolean,
        graphql_name="softReset",
        args=sgqlc.types.ArgDict(
            (
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    hard_reset = sgqlc.types.Field(
        Boolean,
        graphql_name="hardReset",
        args=sgqlc.types.ArgDict(
            (
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_hcc_tariff = sgqlc.types.Field(
        Boolean,
        graphql_name="updateHccTariff",
        args=sgqlc.types.ArgDict(
            (
                (
                    "tariff",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Float), graphql_name="tariff", default=None
                    ),
                ),
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
                (
                    "customer_id",
                    sgqlc.types.Arg(ID, graphql_name="customerId", default=None),
                ),
            )
        ),
    )
    update_customer = sgqlc.types.Field(
        Customer,
        graphql_name="updateCustomer",
        args=sgqlc.types.ArgDict(
            (
                ("id", sgqlc.types.Arg(ID, graphql_name="id", default=None)),
                (
                    "input",
                    sgqlc.types.Arg(
                        UpdateCustomerInput, graphql_name="input", default=None
                    ),
                ),
            )
        ),
    )
    update_customer_bank_account = sgqlc.types.Field(
        BankAccount,
        graphql_name="updateCustomerBankAccount",
        args=sgqlc.types.ArgDict(
            (
                (
                    "customer_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="customerId",
                        default=None,
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(BankAccountInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_srs_onboarding_completed = sgqlc.types.Field(
        Boolean,
        graphql_name="updateSrsOnboardingCompleted",
        args=sgqlc.types.ArgDict(
            (
                (
                    "customer_id",
                    sgqlc.types.Arg(ID, graphql_name="customerId", default=None),
                ),
                (
                    "completed",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="completed",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_access_options = sgqlc.types.Field(
        AccessOptions,
        graphql_name="updateAccessOptions",
        args=sgqlc.types.ArgDict(
            (
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
                (
                    "access_options",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(AccessOptionInput),
                        graphql_name="accessOptions",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_public_or_private = sgqlc.types.Field(
        AccessOptions,
        graphql_name="updatePublicOrPrivate",
        args=sgqlc.types.ArgDict(
            (
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
                (
                    "public_or_private",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(PublicOrPrivate),
                        graphql_name="publicOrPrivate",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_publish_on_map = sgqlc.types.Field(
        AccessOptions,
        graphql_name="updatePublishOnMap",
        args=sgqlc.types.ArgDict(
            (
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
                (
                    "publish_on_map",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="publishOnMap",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_app_feature = sgqlc.types.Field(
        AppFeature,
        graphql_name="createAppFeature",
        args=sgqlc.types.ArgDict(
            (
                (
                    "app_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="appId", default=None
                    ),
                ),
                (
                    "feature_key",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="featureKey",
                        default=None,
                    ),
                ),
                (
                    "enabled",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="enabled",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_app_feature = sgqlc.types.Field(
        AppFeature,
        graphql_name="updateAppFeature",
        args=sgqlc.types.ArgDict(
            (
                (
                    "app_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="appId", default=None
                    ),
                ),
                (
                    "feature_key",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="featureKey",
                        default=None,
                    ),
                ),
                (
                    "enabled",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="enabled",
                        default=None,
                    ),
                ),
            )
        ),
    )
    delete_app_feature = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean),
        graphql_name="deleteAppFeature",
        args=sgqlc.types.ArgDict(
            (
                (
                    "app_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="appId", default=None
                    ),
                ),
                (
                    "feature_key",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="featureKey",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_customer_feature = sgqlc.types.Field(
        CustomerFeature,
        graphql_name="createCustomerFeature",
        args=sgqlc.types.ArgDict(
            (
                (
                    "customer_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="customerId",
                        default=None,
                    ),
                ),
                (
                    "app_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="appId", default=None
                    ),
                ),
                (
                    "feature_key",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="featureKey",
                        default=None,
                    ),
                ),
                (
                    "enabled",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="enabled",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_customer_feature = sgqlc.types.Field(
        CustomerFeature,
        graphql_name="updateCustomerFeature",
        args=sgqlc.types.ArgDict(
            (
                (
                    "customer_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="customerId",
                        default=None,
                    ),
                ),
                (
                    "app_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="appId", default=None
                    ),
                ),
                (
                    "feature_key",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="featureKey",
                        default=None,
                    ),
                ),
                (
                    "enabled",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="enabled",
                        default=None,
                    ),
                ),
            )
        ),
    )
    delete_customer_feature = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean),
        graphql_name="deleteCustomerFeature",
        args=sgqlc.types.ArgDict(
            (
                (
                    "customer_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="customerId",
                        default=None,
                    ),
                ),
                (
                    "app_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="appId", default=None
                    ),
                ),
                (
                    "feature_key",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="featureKey",
                        default=None,
                    ),
                ),
            )
        ),
    )
    generate_live_kit_token = sgqlc.types.Field(
        sgqlc.types.non_null(LiveKitTokenResponse),
        graphql_name="generateLiveKitToken",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(LiveKitTokenInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    solar_charging_enable = sgqlc.types.Field(
        sgqlc.types.non_null(ChargingMode),
        graphql_name="solarChargingEnable",
        args=sgqlc.types.ArgDict(
            (
                (
                    "chargepoint_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargepointId",
                        default=None,
                    ),
                ),
                (
                    "charging_mode",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ChargingMode),
                        graphql_name="chargingMode",
                        default=None,
                    ),
                ),
            )
        ),
    )
    reset_charge_station_parameters_cache = sgqlc.types.Field(
        Boolean,
        graphql_name="resetChargeStationParametersCache",
        args=sgqlc.types.ArgDict(
            (
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_customer_mandate = sgqlc.types.Field(
        CustomerMandate,
        graphql_name="updateCustomerMandate",
        args=sgqlc.types.ArgDict(
            (
                (
                    "customer_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="customerId",
                        default=None,
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(
                        CreateUpdateCustomerMandateInput,
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    end_customer_mandate = sgqlc.types.Field(
        Boolean,
        graphql_name="endCustomerMandate",
        args=sgqlc.types.ArgDict(
            (
                (
                    "customer_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="customerId",
                        default=None,
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(
                        EndCustomerMandateInput, graphql_name="input", default=None
                    ),
                ),
            )
        ),
    )
    create_customer_mandate = sgqlc.types.Field(
        CustomerMandate,
        graphql_name="createCustomerMandate",
        args=sgqlc.types.ArgDict(
            (
                (
                    "customer_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="customerId",
                        default=None,
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(
                        CreateUpdateCustomerMandateInput,
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    end_customer_bacs_mandate = sgqlc.types.Field(
        Boolean,
        graphql_name="endCustomerBacsMandate",
        args=sgqlc.types.ArgDict(
            (
                (
                    "customer_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="customerId",
                        default=None,
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(
                        EndCustomerBacsMandateInput, graphql_name="input", default=None
                    ),
                ),
            )
        ),
    )
    create_customer_bacs_mandate = sgqlc.types.Field(
        CustomerBacsMandate,
        graphql_name="createCustomerBacsMandate",
        args=sgqlc.types.ArgDict(
            (
                (
                    "customer_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="customerId",
                        default=None,
                    ),
                ),
                (
                    "input",
                    sgqlc.types.Arg(
                        CreateCustomerBacsMandateInput,
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_schedule = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("Schedule")),
        graphql_name="updateSchedule",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ScheduleUpdate),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    override_schedule = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean),
        graphql_name="overrideSchedule",
        args=sgqlc.types.ArgDict(
            (
                (
                    "chargepoint_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargepointId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_schedule_simple = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("ScheduleSimple")),
        graphql_name="updateScheduleSimple",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ScheduleSimpleUpdate),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    delete_schedule = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("Schedule")),
        graphql_name="deleteSchedule",
        args=sgqlc.types.ArgDict(
            (
                (
                    "chargepoint_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargepointId",
                        default=None,
                    ),
                ),
                (
                    "week_days",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(Int)),
                        graphql_name="weekDays",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_schedule_complex = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("ScheduleBlock")),
        graphql_name="updateScheduleComplex",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ScheduleComplexUpdate),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    net_balanced_charging = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("Schedule")),
        graphql_name="netBalancedCharging",
        args=sgqlc.types.ArgDict(
            (
                (
                    "chargepoint_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargepointId",
                        default=None,
                    ),
                ),
                (
                    "enabled",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="enabled",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_net_balanced_charging = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean),
        graphql_name="updateNetBalancedCharging",
        args=sgqlc.types.ArgDict(
            (
                (
                    "chargepoint_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargepointId",
                        default=None,
                    ),
                ),
                (
                    "enabled",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Boolean),
                        graphql_name="enabled",
                        default=None,
                    ),
                ),
            )
        ),
    )
    register_application = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean),
        graphql_name="registerApplication",
        args=sgqlc.types.ArgDict(
            (
                (
                    "uid",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="uid", default=None
                    ),
                ),
                (
                    "device_type",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(DeviceType),
                        graphql_name="deviceType",
                        default=None,
                    ),
                ),
                (
                    "push_notification_token",
                    sgqlc.types.Arg(
                        String, graphql_name="pushNotificationToken", default=None
                    ),
                ),
                (
                    "device_model_name",
                    sgqlc.types.Arg(
                        String, graphql_name="deviceModelName", default=None
                    ),
                ),
                (
                    "app_version",
                    sgqlc.types.Arg(String, graphql_name="appVersion", default=None),
                ),
                (
                    "device_manufacturer",
                    sgqlc.types.Arg(
                        String, graphql_name="deviceManufacturer", default=None
                    ),
                ),
                (
                    "device_version",
                    sgqlc.types.Arg(String, graphql_name="deviceVersion", default=None),
                ),
                (
                    "external_customer_id",
                    sgqlc.types.Arg(
                        String, graphql_name="externalCustomerId", default=None
                    ),
                ),
                (
                    "external_usergroup_id",
                    sgqlc.types.Arg(
                        String, graphql_name="externalUsergroupId", default=None
                    ),
                ),
                (
                    "external_app_provider_id",
                    sgqlc.types.Arg(
                        String, graphql_name="externalAppProviderId", default=None
                    ),
                ),
            )
        ),
    )
    bulk_update_cpms_id = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean),
        graphql_name="bulkUpdateCpmsId",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(
                            sgqlc.types.list_of(
                                sgqlc.types.non_null(BulkUpdateCpmsIdInput)
                            )
                        ),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_aivoice_ticket = sgqlc.types.Field(
        sgqlc.types.non_null("OdooTicket"),
        graphql_name="createAIVoiceTicket",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(CreateAIVoiceTicketInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_partner = sgqlc.types.Field(
        sgqlc.types.non_null("OdooCreatePartnerResponse"),
        graphql_name="createPartner",
        args=sgqlc.types.ArgDict(
            (
                (
                    "name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="name", default=None
                    ),
                ),
                (
                    "email",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="email", default=None
                    ),
                ),
            )
        ),
    )
    create_ticket = sgqlc.types.Field(
        "OdooTicket",
        graphql_name="createTicket",
        args=sgqlc.types.ArgDict(
            (
                (
                    "partner_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int),
                        graphql_name="partnerId",
                        default=None,
                    ),
                ),
                (
                    "team_key",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="teamKey",
                        default=None,
                    ),
                ),
                (
                    "name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="name", default=None
                    ),
                ),
                (
                    "description",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="description",
                        default=None,
                    ),
                ),
                (
                    "xx_category_id",
                    sgqlc.types.Arg(Int, graphql_name="xx_category_id", default=None),
                ),
                (
                    "xx_subcategory_id",
                    sgqlc.types.Arg(
                        Int, graphql_name="xx_subcategory_id", default=None
                    ),
                ),
                (
                    "status",
                    sgqlc.types.Arg(
                        OdooTicketStatus, graphql_name="status", default=None
                    ),
                ),
                (
                    "xx_source_id",
                    sgqlc.types.Arg(Int, graphql_name="xx_source_id", default=None),
                ),
            )
        ),
    )
    import_lms_tickets = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="importLmsTickets"
    )
    import_lms_customers = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="importLmsCustomers"
    )
    send_mail = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean),
        graphql_name="sendMail",
        args=sgqlc.types.ArgDict(
            (
                (
                    "user_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="userId", default=None
                    ),
                ),
                (
                    "template_name",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="templateName",
                        default=None,
                    ),
                ),
            )
        ),
    )
    update_ticket = sgqlc.types.Field(
        "OdooTicket",
        graphql_name="updateTicket",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ticket_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="ticketId", default=None
                    ),
                ),
                ("name", sgqlc.types.Arg(String, graphql_name="name", default=None)),
                (
                    "description",
                    sgqlc.types.Arg(String, graphql_name="description", default=None),
                ),
                (
                    "comments",
                    sgqlc.types.Arg(
                        sgqlc.types.list_of(String),
                        graphql_name="comments",
                        default=None,
                    ),
                ),
            )
        ),
    )
    create_ere_mandate_ticket = sgqlc.types.Field(
        sgqlc.types.non_null("OdooTicket"),
        graphql_name="createEreMandateTicket",
        args=sgqlc.types.ArgDict(
            (
                (
                    "input",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(CreateEreMandateTicketInput),
                        graphql_name="input",
                        default=None,
                    ),
                ),
            )
        ),
    )


class OdooApiVersion(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "server_version",
        "server_version_info",
        "server_serie",
        "protocol_version",
    )
    server_version = sgqlc.types.Field(String, graphql_name="server_version")
    server_version_info = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="server_version_info"
    )
    server_serie = sgqlc.types.Field(String, graphql_name="server_serie")
    protocol_version = sgqlc.types.Field(Int, graphql_name="protocol_version")


class OdooChargeStation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "name",
        "comm_id",
        "state",
        "owner",
        "last_communication_date",
        "channels",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")
    comm_id = sgqlc.types.Field(String, graphql_name="commId")
    state = sgqlc.types.Field(String, graphql_name="state")
    owner = sgqlc.types.Field("OdooChargeStationOwner", graphql_name="owner")
    last_communication_date = sgqlc.types.Field(
        String, graphql_name="lastCommunicationDate"
    )
    channels = sgqlc.types.Field(
        sgqlc.types.list_of("OdooChargeStationChannel"), graphql_name="channels"
    )


class OdooChargeStationChannel(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("global_status", "last_status_change_date")
    global_status = sgqlc.types.Field(String, graphql_name="globalStatus")
    last_status_change_date = sgqlc.types.Field(
        String, graphql_name="lastStatusChangeDate"
    )


class OdooChargeStationCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("get_charge_stations",)
    get_charge_stations = sgqlc.types.Field(
        "OdooChargeStationConnection", graphql_name="getChargeStations"
    )


class OdooChargeStationConnection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null(OdooChargeStation))
        ),
        graphql_name="items",
    )
    total_items = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="totalItems"
    )


class OdooChargeStationOwner(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "user_group",
        "first_name",
        "last_name",
        "email",
        "srs_onboarding_complete",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")
    user_group = sgqlc.types.Field("OdooUserGroup", graphql_name="userGroup")
    first_name = sgqlc.types.Field(String, graphql_name="firstName")
    last_name = sgqlc.types.Field(String, graphql_name="lastName")
    email = sgqlc.types.Field(String, graphql_name="email")
    srs_onboarding_complete = sgqlc.types.Field(
        Boolean, graphql_name="srsOnboardingComplete"
    )


class OdooCreateMailingContactResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("contact_id",)
    contact_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="contactId")


class OdooCreateMailingList(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("create_mailing_list",)
    create_mailing_list = sgqlc.types.Field(
        "OdooCreateMailingListResponse", graphql_name="createMailingList"
    )


class OdooCreateMailingListResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("mailing_list_id",)
    mailing_list_id = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="mailingListId"
    )


class OdooCreatePartnerResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("partner_id",)
    partner_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="partnerId")


class OdooLoginUid(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("uid",)
    uid = sgqlc.types.Field(Int, graphql_name="uid")


class OdooMailingContactResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("create_mailing_contact",)
    create_mailing_contact = sgqlc.types.Field(
        "OdooMailingContactResultItem", graphql_name="createMailingContact"
    )


class OdooMailingContactResultItem(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("contact_id",)
    contact_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="contactId")


class OdooMessages(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "tracking_value_ids")
    id = sgqlc.types.Field(Int, graphql_name="id")
    tracking_value_ids = sgqlc.types.Field(String, graphql_name="tracking_value_ids")


class OdooModel(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "model", "name", "info")
    id = sgqlc.types.Field(Int, graphql_name="id")
    model = sgqlc.types.Field(String, graphql_name="model")
    name = sgqlc.types.Field(String, graphql_name="name")
    info = sgqlc.types.Field(String, graphql_name="info")


class OdooPartner(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(Int, graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")


class OdooProcessMailingListResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "success",
        "mailing_list_id",
        "processed_contacts",
        "errors",
        "message",
    )
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="success")
    mailing_list_id = sgqlc.types.Field(Int, graphql_name="mailingListId")
    processed_contacts = sgqlc.types.Field(
        sgqlc.types.non_null(Int), graphql_name="processedContacts"
    )
    errors = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))),
        graphql_name="errors",
    )
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="message")


class OdooProvider(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")


class OdooScheduleResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("scheduled", "next_run_time", "uuid")
    scheduled = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="scheduled"
    )
    next_run_time = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="nextRunTime"
    )
    uuid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="uuid")


class OdooTicket(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "name",
        "description",
        "stage_id",
        "create_date",
        "write_date",
        "priority",
        "ticket_type_id",
        "xx_category_id",
        "xx_subcategory_id",
        "partner_id",
        "messages",
        "ticket_ref",
    )
    id = sgqlc.types.Field(Int, graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")
    description = sgqlc.types.Field(String, graphql_name="description")
    stage_id = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="stage_id")
    create_date = sgqlc.types.Field(String, graphql_name="create_date")
    write_date = sgqlc.types.Field(String, graphql_name="write_date")
    priority = sgqlc.types.Field(String, graphql_name="priority")
    ticket_type_id = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="ticket_type_id"
    )
    xx_category_id = sgqlc.types.Field(String, graphql_name="xx_category_id")
    xx_subcategory_id = sgqlc.types.Field(String, graphql_name="xx_subcategory_id")
    partner_id = sgqlc.types.Field(OdooPartner, graphql_name="partner_id")
    messages = sgqlc.types.Field(
        sgqlc.types.list_of("OdooTicketMessage"), graphql_name="messages"
    )
    ticket_ref = sgqlc.types.Field(String, graphql_name="ticket_ref")


class OdooTicketMessage(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "subject",
        "body",
        "create_date",
        "author_id",
        "message_type",
        "date",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="id")
    subject = sgqlc.types.Field(String, graphql_name="subject")
    body = sgqlc.types.Field(String, graphql_name="body")
    create_date = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="create_date"
    )
    author_id = sgqlc.types.Field(
        sgqlc.types.non_null(OdooPartner), graphql_name="author_id"
    )
    message_type = sgqlc.types.Field(String, graphql_name="message_type")
    date = sgqlc.types.Field(String, graphql_name="date")


class OdooTicketTracking(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "old_value_char",
        "new_value_char",
        "create_date",
        "ticket_ref",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    old_value_char = sgqlc.types.Field(String, graphql_name="old_value_char")
    new_value_char = sgqlc.types.Field(String, graphql_name="new_value_char")
    create_date = sgqlc.types.Field(String, graphql_name="create_date")
    ticket_ref = sgqlc.types.Field(String, graphql_name="ticket_ref")


class OdooTicketVariables(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "partner_id",
        "team_id",
        "name",
        "description",
        "xx_category_id",
        "xx_subcategory_id",
    )
    partner_id = sgqlc.types.Field(Int, graphql_name="partner_id")
    team_id = sgqlc.types.Field(Int, graphql_name="team_id")
    name = sgqlc.types.Field(String, graphql_name="name")
    description = sgqlc.types.Field(String, graphql_name="description")
    xx_category_id = sgqlc.types.Field(Int, graphql_name="xx_category_id")
    xx_subcategory_id = sgqlc.types.Field(Int, graphql_name="xx_subcategory_id")


class OdooUserGroup(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "name", "provider")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    provider = sgqlc.types.Field(OdooProvider, graphql_name="provider")


class ParameterSet(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "name",
        "connected_device_count",
        "is_default",
        "user_group",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")
    connected_device_count = sgqlc.types.Field(Int, graphql_name="connectedDeviceCount")
    is_default = sgqlc.types.Field(Boolean, graphql_name="isDefault")
    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")


class Payment(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "payment_id",
        "extern_id",
        "feedback",
        "date",
        "user_email_address",
        "send_invoice_consent",
        "id",
    )
    payment_id = sgqlc.types.Field(Int, graphql_name="paymentId")
    extern_id = sgqlc.types.Field(ID, graphql_name="externId")
    feedback = sgqlc.types.Field(String, graphql_name="feedback")
    date = sgqlc.types.Field(String, graphql_name="date")
    user_email_address = sgqlc.types.Field(String, graphql_name="userEmailAddress")
    send_invoice_consent = sgqlc.types.Field(Boolean, graphql_name="sendInvoiceConsent")
    id = sgqlc.types.Field(ID, graphql_name="id")


class Person(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(ID, graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")


class Price(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("currency", "value")
    currency = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="currency")
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="value")


class PriceComponent(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("type", "price", "vat", "step_size")
    type = sgqlc.types.Field(
        sgqlc.types.non_null(TariffDimensionType), graphql_name="type"
    )
    price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="price")
    vat = sgqlc.types.Field(Float, graphql_name="vat")
    step_size = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="stepSize")


class PriceElement(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("type", "price")
    type = sgqlc.types.Field(String, graphql_name="type")
    price = sgqlc.types.Field(Float, graphql_name="price")


class Product(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "name",
        "description",
        "invoice_name",
        "provider",
        "type",
        "usage_type",
        "selection_mode",
        "payment_mode",
        "payment_period_mode",
        "auto_approve",
        "owner_access",
        "attach_customer_to_transaction",
        "sim_activated",
        "network_types",
        "customer_types",
        "currency",
        "items",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")
    description = sgqlc.types.Field(String, graphql_name="description")
    invoice_name = sgqlc.types.Field(String, graphql_name="invoiceName")
    provider = sgqlc.types.Field("Provider", graphql_name="provider")
    type = sgqlc.types.Field(ProductType, graphql_name="type")
    usage_type = sgqlc.types.Field(ProductUsageType, graphql_name="usageType")
    selection_mode = sgqlc.types.Field(
        ProductSelectionMode, graphql_name="selectionMode"
    )
    payment_mode = sgqlc.types.Field(ProductPaymentMode, graphql_name="paymentMode")
    payment_period_mode = sgqlc.types.Field(
        ProductPaymentPeriodMode, graphql_name="paymentPeriodMode"
    )
    auto_approve = sgqlc.types.Field(Boolean, graphql_name="autoApprove")
    owner_access = sgqlc.types.Field(Boolean, graphql_name="ownerAccess")
    attach_customer_to_transaction = sgqlc.types.Field(
        Boolean, graphql_name="attachCustomerToTransaction"
    )
    sim_activated = sgqlc.types.Field(Boolean, graphql_name="simActivated")
    network_types = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="networkTypes"
    )
    customer_types = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="customerTypes"
    )
    currency = sgqlc.types.Field(Currency, graphql_name="currency")
    items = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="items")


class Provider(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "name",
        "category",
        "transactions",
        "invoices",
        "user_groups",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")
    category = sgqlc.types.Field(ProviderCategory, graphql_name="category")
    transactions = sgqlc.types.Field(
        "TransactionCollection",
        graphql_name="transactions",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        TransactionFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(TransactionSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    invoices = sgqlc.types.Field(
        InvoiceCollection,
        graphql_name="invoices",
        args=sgqlc.types.ArgDict(
            (
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
                (
                    "items_per_page",
                    sgqlc.types.Arg(Int, graphql_name="itemsPerPage", default=None),
                ),
                (
                    "filters",
                    sgqlc.types.Arg(
                        InvoiceFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(InvoiceSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    user_groups = sgqlc.types.Field(
        "UserGroupCollection",
        graphql_name="userGroups",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        UserGroupFilter, graphql_name="filters", default=None
                    ),
                ),
            )
        ),
    )


class ProviderDetails(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("provider_logo_url", "provider_logo_background_color")
    provider_logo_url = sgqlc.types.Field(String, graphql_name="providerLogoUrl")
    provider_logo_background_color = sgqlc.types.Field(
        String, graphql_name="providerLogoBackgroundColor"
    )


class PushNotification(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "title", "body", "extended_body", "created_at", "type")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="title")
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="body")
    extended_body = sgqlc.types.Field(String, graphql_name="extendedBody")
    created_at = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="createdAt"
    )
    type = sgqlc.types.Field(PushNotificationType, graphql_name="type")


class Query(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "lms_card_details",
        "lms_map_locations",
        "lms_location",
        "lms_locations",
        "lms_payments",
        "lms_legacy_tariff",
        "lms_tariff",
        "lms_tariffs",
        "lms_tariff_vat",
        "lms_location_tariff",
        "lms_transactions",
        "lms_active_transaction",
        "retrieve_password",
        "get_tokens",
        "get_token_by_id",
        "get_token_by_internal_id",
        "get_token_by_external_id",
        "get_token_by_contract_id",
        "get_roaming_token",
        "get_charge_stations",
        "get_charge_stations_by_id",
        "get_charge_station_by_id",
        "get_customer_by_id",
        "get_customer_bank_accounts",
        "get_customer_charge_stations",
        "get_invoices",
        "get_invoice_by_id",
        "get_charge_station_channel",
        "get_tickets",
        "get_app_features_by_app_id",
        "get_customer_features_by_app_id",
        "is_hcc_allowed",
        "reimbursement_tariff_range",
        "get_solar_charging_available",
        "get_charging_mode",
        "get_currency",
        "get_currencies",
        "get_country",
        "get_countries",
        "get_language",
        "get_languages",
        "get_cards",
        "get_transactions",
        "get_transaction",
        "get_charge_group_by_id",
        "get_charge_groups",
        "get_user_groups",
        "get_user_group_by_id",
        "get_customers",
        "get_schedules",
        "schedules_simple",
        "schedules_complex",
        "get_net_balanced_charging_status",
        "get_application",
        "push_notifications",
        "get_api_version",
        "get_helpdesk_ticket_by_id",
        "get_helpdesk_tickets_by_partner_id",
        "get_helpdesk_ticket_tracking_history",
        "get_partner_by_email",
    )
    lms_card_details = sgqlc.types.Field(
        sgqlc.types.non_null(CardDetails),
        graphql_name="lmsCardDetails",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    lms_map_locations = sgqlc.types.Field(
        sgqlc.types.non_null(LmsLocationsResult),
        graphql_name="lmsMapLocations",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        MapLocationsFiltersInput, graphql_name="filters", default=None
                    ),
                ),
                (
                    "bounds",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(LocationBoundsInput),
                        graphql_name="bounds",
                        default=None,
                    ),
                ),
            )
        ),
    )
    lms_location = sgqlc.types.Field(
        Location,
        graphql_name="lmsLocation",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    lms_locations = sgqlc.types.Field(
        sgqlc.types.non_null(LmsLocationsResult),
        graphql_name="lmsLocations",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        LocationsFiltersInput, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="sort", default=None
                    ),
                ),
                (
                    "end_result",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Float),
                        graphql_name="endResult",
                        default=None,
                    ),
                ),
                (
                    "start_result",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Float),
                        graphql_name="startResult",
                        default=None,
                    ),
                ),
                ("radius", sgqlc.types.Arg(Float, graphql_name="radius", default=None)),
                (
                    "ref_longitude",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Float),
                        graphql_name="refLongitude",
                        default=None,
                    ),
                ),
                (
                    "ref_latitude",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Float),
                        graphql_name="refLatitude",
                        default=None,
                    ),
                ),
            )
        ),
    )
    lms_payments = sgqlc.types.Field(
        sgqlc.types.non_null(LmsPaymentsResult),
        graphql_name="lmsPayments",
        args=sgqlc.types.ArgDict(
            (
                (
                    "end_result",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Float),
                        graphql_name="endResult",
                        default=None,
                    ),
                ),
                (
                    "start_result",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Float),
                        graphql_name="startResult",
                        default=None,
                    ),
                ),
            )
        ),
    )
    lms_legacy_tariff = sgqlc.types.Field(
        sgqlc.types.non_null(LegacyTariff),
        graphql_name="lmsLegacyTariff",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    lms_tariff = sgqlc.types.Field(
        sgqlc.types.non_null("Tariff"),
        graphql_name="lmsTariff",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    lms_tariffs = sgqlc.types.Field(
        sgqlc.types.non_null(LmsTariffsResult),
        graphql_name="lmsTariffs",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ids",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(
                            sgqlc.types.list_of(sgqlc.types.non_null(ID))
                        ),
                        graphql_name="ids",
                        default=None,
                    ),
                ),
            )
        ),
    )
    lms_tariff_vat = sgqlc.types.Field(
        sgqlc.types.non_null("TariffResult"),
        graphql_name="lmsTariffVat",
        args=sgqlc.types.ArgDict(
            (
                (
                    "tariff_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="tariffId",
                        default=None,
                    ),
                ),
                (
                    "vat",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Float), graphql_name="vat", default=None
                    ),
                ),
            )
        ),
    )
    lms_location_tariff = sgqlc.types.Field(
        sgqlc.types.non_null("TariffResult"),
        graphql_name="lmsLocationTariff",
        args=sgqlc.types.ArgDict(
            (
                (
                    "connector_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="connectorId",
                        default=None,
                    ),
                ),
                (
                    "evse_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="evseId",
                        default=None,
                    ),
                ),
                (
                    "location_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="locationId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    lms_transactions = sgqlc.types.Field(
        sgqlc.types.non_null(LmsTransactionsResult),
        graphql_name="lmsTransactions",
        args=sgqlc.types.ArgDict(
            (
                (
                    "end_result",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Float),
                        graphql_name="endResult",
                        default=None,
                    ),
                ),
                (
                    "start_result",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Float),
                        graphql_name="startResult",
                        default=None,
                    ),
                ),
            )
        ),
    )
    lms_active_transaction = sgqlc.types.Field(
        "Transaction", graphql_name="lmsActiveTransaction"
    )
    retrieve_password = sgqlc.types.Field(
        sgqlc.types.non_null("RetrievePasswordResult"),
        graphql_name="retrievePassword",
        args=sgqlc.types.ArgDict(
            (
                (
                    "email",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="email", default=None
                    ),
                ),
            )
        ),
    )
    get_tokens = sgqlc.types.Field(
        sgqlc.types.list_of("TokenResponse"), graphql_name="getTokens"
    )
    get_token_by_id = sgqlc.types.Field(
        sgqlc.types.list_of("TokenResponse"),
        graphql_name="getTokenById",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(ID)),
                        graphql_name="id",
                        default=None,
                    ),
                ),
            )
        ),
    )
    get_token_by_internal_id = sgqlc.types.Field(
        sgqlc.types.list_of("TokenResponse"),
        graphql_name="getTokenByInternalId",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(ID)),
                        graphql_name="id",
                        default=None,
                    ),
                ),
            )
        ),
    )
    get_token_by_external_id = sgqlc.types.Field(
        sgqlc.types.list_of("TokenResponse"),
        graphql_name="getTokenByExternalId",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(ID)),
                        graphql_name="id",
                        default=None,
                    ),
                ),
            )
        ),
    )
    get_token_by_contract_id = sgqlc.types.Field(
        sgqlc.types.list_of("TokenResponse"),
        graphql_name="getTokenByContractId",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(ID)),
                        graphql_name="id",
                        default=None,
                    ),
                ),
            )
        ),
    )
    get_roaming_token = sgqlc.types.Field(
        CardRoaming,
        graphql_name="getRoamingToken",
        args=sgqlc.types.ArgDict(
            (
                (
                    "internal_id",
                    sgqlc.types.Arg(ID, graphql_name="internalId", default=None),
                ),
                (
                    "external_id",
                    sgqlc.types.Arg(ID, graphql_name="externalId", default=None),
                ),
                (
                    "contract_id",
                    sgqlc.types.Arg(ID, graphql_name="contractId", default=None),
                ),
            )
        ),
    )
    get_charge_stations = sgqlc.types.Field(
        ChargeStationCollection,
        graphql_name="getChargeStations",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        ChargeStationFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(
                        ChargeStationSort, graphql_name="sort", default=None
                    ),
                ),
            )
        ),
    )
    get_charge_stations_by_id = sgqlc.types.Field(
        sgqlc.types.list_of(ChargeStation),
        graphql_name="getChargeStationsById",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(sgqlc.types.list_of(ID)),
                        graphql_name="id",
                        default=None,
                    ),
                ),
            )
        ),
    )
    get_charge_station_by_id = sgqlc.types.Field(
        ChargeStation,
        graphql_name="getChargeStationById",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    get_customer_by_id = sgqlc.types.Field(
        Customer,
        graphql_name="getCustomerById",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(ID, graphql_name="id", default=None)),)
        ),
    )
    get_customer_bank_accounts = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(BankAccount)),
        graphql_name="getCustomerBankAccounts",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(ID, graphql_name="id", default=None)),)
        ),
    )
    get_customer_charge_stations = sgqlc.types.Field(
        sgqlc.types.list_of(ChargeStation),
        graphql_name="getCustomerChargeStations",
        args=sgqlc.types.ArgDict(
            (
                (
                    "customer_id",
                    sgqlc.types.Arg(ID, graphql_name="customerId", default=None),
                ),
            )
        ),
    )
    get_invoices = sgqlc.types.Field(
        InvoiceCollection,
        graphql_name="getInvoices",
        args=sgqlc.types.ArgDict(
            (
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
                (
                    "items_per_page",
                    sgqlc.types.Arg(Int, graphql_name="itemsPerPage", default=None),
                ),
                (
                    "filters",
                    sgqlc.types.Arg(
                        InvoiceFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(InvoiceSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    get_invoice_by_id = sgqlc.types.Field(
        Invoice,
        graphql_name="getInvoiceById",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(ID, graphql_name="id", default=None)),)
        ),
    )
    get_charge_station_channel = sgqlc.types.Field(
        ChargeStationChannel,
        graphql_name="getChargeStationChannel",
        args=sgqlc.types.ArgDict(
            (
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
                (
                    "channel_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="channelId", default=None
                    ),
                ),
            )
        ),
    )
    get_tickets = sgqlc.types.Field(
        "TicketCollection",
        graphql_name="getTickets",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(TicketFilter, graphql_name="filters", default=None),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(TicketSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    get_app_features_by_app_id = sgqlc.types.Field(
        sgqlc.types.list_of(EffectiveAppFeature),
        graphql_name="getAppFeaturesByAppId",
        args=sgqlc.types.ArgDict(
            (
                (
                    "app_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="appId", default=None
                    ),
                ),
            )
        ),
    )
    get_customer_features_by_app_id = sgqlc.types.Field(
        sgqlc.types.list_of(CustomerFeature),
        graphql_name="getCustomerFeaturesByAppId",
        args=sgqlc.types.ArgDict(
            (
                (
                    "customer_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String),
                        graphql_name="customerId",
                        default=None,
                    ),
                ),
                (
                    "app_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="appId", default=None
                    ),
                ),
            )
        ),
    )
    is_hcc_allowed = sgqlc.types.Field(
        Boolean,
        graphql_name="isHccAllowed",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    reimbursement_tariff_range = sgqlc.types.Field(
        "TariffRange", graphql_name="reimbursementTariffRange"
    )
    get_solar_charging_available = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean),
        graphql_name="getSolarChargingAvailable",
        args=sgqlc.types.ArgDict(
            (
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    get_charging_mode = sgqlc.types.Field(
        sgqlc.types.non_null(ChargingMode),
        graphql_name="getChargingMode",
        args=sgqlc.types.ArgDict(
            (
                (
                    "charge_station_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargeStationId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    get_currency = sgqlc.types.Field(
        Currency,
        graphql_name="getCurrency",
        args=sgqlc.types.ArgDict(
            (
                (
                    "code",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="code", default=None
                    ),
                ),
            )
        ),
    )
    get_currencies = sgqlc.types.Field(
        CurrencyCollection,
        graphql_name="getCurrencies",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        CurrencyFilter, graphql_name="filters", default=None
                    ),
                ),
            )
        ),
    )
    get_country = sgqlc.types.Field(
        Country,
        graphql_name="getCountry",
        args=sgqlc.types.ArgDict(
            (
                (
                    "code",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="code", default=None
                    ),
                ),
            )
        ),
    )
    get_countries = sgqlc.types.Field(CountryCollection, graphql_name="getCountries")
    get_language = sgqlc.types.Field(
        CountryLanguage,
        graphql_name="getLanguage",
        args=sgqlc.types.ArgDict(
            (
                (
                    "code",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="code", default=None
                    ),
                ),
            )
        ),
    )
    get_languages = sgqlc.types.Field(
        CountryLanguageCollection,
        graphql_name="getLanguages",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        LanguageFilter, graphql_name="filters", default=None
                    ),
                ),
            )
        ),
    )
    get_cards = sgqlc.types.Field(
        CardCollection,
        graphql_name="getCards",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(CardFilter, graphql_name="filters", default=None),
                ),
                ("sort", sgqlc.types.Arg(CardSort, graphql_name="sort", default=None)),
            )
        ),
    )
    get_transactions = sgqlc.types.Field(
        "TransactionCollection",
        graphql_name="getTransactions",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        TransactionFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(TransactionSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    get_transaction = sgqlc.types.Field(
        LmsTransaction,
        graphql_name="getTransaction",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    get_charge_group_by_id = sgqlc.types.Field(
        ChargeGroup,
        graphql_name="getChargeGroupById",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    get_charge_groups = sgqlc.types.Field(
        ChargeGroupCollection,
        graphql_name="getChargeGroups",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        ChargeGroupFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(ChargeGroupSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    get_user_groups = sgqlc.types.Field(
        "UserGroupCollection",
        graphql_name="getUserGroups",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        UserGroupFilter, graphql_name="filters", default=None
                    ),
                ),
            )
        ),
    )
    get_user_group_by_id = sgqlc.types.Field(
        "UserGroup",
        graphql_name="getUserGroupById",
        args=sgqlc.types.ArgDict(
            (
                (
                    "id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID), graphql_name="id", default=None
                    ),
                ),
            )
        ),
    )
    get_customers = sgqlc.types.Field(
        CustomerCollection,
        graphql_name="getCustomers",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        CustomerFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(CustomerSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    get_schedules = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("Schedule")),
        graphql_name="getSchedules",
        args=sgqlc.types.ArgDict(
            (
                (
                    "chargepoint_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargepointId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    schedules_simple = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("Schedule")),
        graphql_name="schedulesSimple",
        args=sgqlc.types.ArgDict(
            (
                (
                    "chargepoint_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargepointId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    schedules_complex = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("ScheduleBlock")),
        graphql_name="schedulesComplex",
        args=sgqlc.types.ArgDict(
            (
                (
                    "chargepoint_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargepointId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    get_net_balanced_charging_status = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean),
        graphql_name="getNetBalancedChargingStatus",
        args=sgqlc.types.ArgDict(
            (
                (
                    "chargepoint_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(ID),
                        graphql_name="chargepointId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    get_application = sgqlc.types.Field(
        App,
        graphql_name="getApplication",
        args=sgqlc.types.ArgDict(
            (
                (
                    "uid",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="uid", default=None
                    ),
                ),
            )
        ),
    )
    push_notifications = sgqlc.types.Field(
        sgqlc.types.list_of(PushNotification),
        graphql_name="pushNotifications",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(ID, graphql_name="id", default=None)),)
        ),
    )
    get_api_version = sgqlc.types.Field(OdooApiVersion, graphql_name="getApiVersion")
    get_helpdesk_ticket_by_id = sgqlc.types.Field(
        OdooTicket,
        graphql_name="getHelpdeskTicketById",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ticket_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="ticketId", default=None
                    ),
                ),
            )
        ),
    )
    get_helpdesk_tickets_by_partner_id = sgqlc.types.Field(
        sgqlc.types.list_of(OdooTicket),
        graphql_name="getHelpdeskTicketsByPartnerId",
        args=sgqlc.types.ArgDict(
            (
                (
                    "partner_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int),
                        graphql_name="partnerId",
                        default=None,
                    ),
                ),
            )
        ),
    )
    get_helpdesk_ticket_tracking_history = sgqlc.types.Field(
        sgqlc.types.list_of(OdooTicketTracking),
        graphql_name="getHelpdeskTicketTrackingHistory",
        args=sgqlc.types.ArgDict(
            (
                (
                    "ticket_id",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(Int), graphql_name="ticketId", default=None
                    ),
                ),
            )
        ),
    )
    get_partner_by_email = sgqlc.types.Field(
        OdooPartner,
        graphql_name="getPartnerByEmail",
        args=sgqlc.types.ArgDict(
            (
                (
                    "email",
                    sgqlc.types.Arg(
                        sgqlc.types.non_null(String), graphql_name="email", default=None
                    ),
                ),
            )
        ),
    )


class RetrievePasswordResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("status",)
    status = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("RetrievePasswordResultStatus"))
        ),
        graphql_name="status",
    )


class RetrievePasswordResultStatus(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("app_identifier", "status")
    app_identifier = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="appIdentifier"
    )
    status = sgqlc.types.Field(
        sgqlc.types.non_null(RetrievePasswordStatus), graphql_name="status"
    )


class RoamingProfile(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(ID, graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")


class RoamingProfileHub(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "role", "roaming_hub")
    id = sgqlc.types.Field(ID, graphql_name="id")
    role = sgqlc.types.Field(RoamingRole, graphql_name="role")
    roaming_hub = sgqlc.types.Field(RoamingProfile, graphql_name="roamingHub")


class Schedule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("weekday", "start_time", "stop_time")
    weekday = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="weekday")
    start_time = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="startTime"
    )
    stop_time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="stopTime")


class ScheduleBlock(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("block", "charge")
    block = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="block")
    charge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="charge")


class SchedulePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "schedule",
        "provider_name",
        "order_direction",
        "dry_run",
        "close_tickets",
    )
    schedule = sgqlc.types.Field(
        sgqlc.types.non_null("ScheduleResult"), graphql_name="schedule"
    )
    provider_name = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="providerName"
    )
    order_direction = sgqlc.types.Field(
        OdooOrderDirection, graphql_name="orderDirection"
    )
    dry_run = sgqlc.types.Field(Boolean, graphql_name="dryRun")
    close_tickets = sgqlc.types.Field(Boolean, graphql_name="closeTickets")


class ScheduleResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "cron_expression",
        "interval_type",
        "interval_number",
        "run_immediately",
    )
    cron_expression = sgqlc.types.Field(String, graphql_name="cronExpression")
    interval_type = sgqlc.types.Field(OdooIntervalType, graphql_name="intervalType")
    interval_number = sgqlc.types.Field(Int, graphql_name="intervalNumber")
    run_immediately = sgqlc.types.Field(Boolean, graphql_name="runImmediately")


class ScheduleSimple(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("weekday", "times", "charge")
    weekday = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="weekday")
    times = sgqlc.types.Field(ChargeTimes, graphql_name="times")
    charge = sgqlc.types.Field(Boolean, graphql_name="charge")


class Tariff(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "country_code",
        "party_id",
        "id",
        "currency",
        "type",
        "tariff_alt_text",
        "tariff_alt_url",
        "min_price",
        "max_price",
        "elements",
        "start_date_time",
        "end_date_time",
        "energy_mix",
        "last_updated",
    )
    country_code = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="countryCode"
    )
    party_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="partyId")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    currency = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="currency")
    type = sgqlc.types.Field(TariffType, graphql_name="type")
    tariff_alt_text = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(DisplayText)),
        graphql_name="tariffAltText",
    )
    tariff_alt_url = sgqlc.types.Field(String, graphql_name="tariffAltUrl")
    min_price = sgqlc.types.Field(Price, graphql_name="minPrice")
    max_price = sgqlc.types.Field(Price, graphql_name="maxPrice")
    elements = sgqlc.types.Field(
        sgqlc.types.non_null(
            sgqlc.types.list_of(sgqlc.types.non_null("TariffElement"))
        ),
        graphql_name="elements",
    )
    start_date_time = sgqlc.types.Field(String, graphql_name="startDateTime")
    end_date_time = sgqlc.types.Field(String, graphql_name="endDateTime")
    energy_mix = sgqlc.types.Field(EnergyMix, graphql_name="energyMix")
    last_updated = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="lastUpdated"
    )


class TariffElement(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("price_components", "restrictions")
    price_components = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PriceComponent))),
        graphql_name="priceComponents",
    )
    restrictions = sgqlc.types.Field("TariffRestrictions", graphql_name="restrictions")


class TariffRange(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("min", "max")
    min = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="min")
    max = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="max")


class TariffRestrictions(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "start_time",
        "end_time",
        "start_date",
        "end_date",
        "min_kwh",
        "max_kwh",
        "min_current",
        "max_current",
        "min_power",
        "max_power",
        "min_duration",
        "max_duration",
        "day_of_week",
        "reservation",
    )
    start_time = sgqlc.types.Field(String, graphql_name="startTime")
    end_time = sgqlc.types.Field(String, graphql_name="endTime")
    start_date = sgqlc.types.Field(String, graphql_name="startDate")
    end_date = sgqlc.types.Field(String, graphql_name="endDate")
    min_kwh = sgqlc.types.Field(Float, graphql_name="minKwh")
    max_kwh = sgqlc.types.Field(Float, graphql_name="maxKwh")
    min_current = sgqlc.types.Field(Float, graphql_name="minCurrent")
    max_current = sgqlc.types.Field(Float, graphql_name="maxCurrent")
    min_power = sgqlc.types.Field(Float, graphql_name="minPower")
    max_power = sgqlc.types.Field(Float, graphql_name="maxPower")
    min_duration = sgqlc.types.Field(Float, graphql_name="minDuration")
    max_duration = sgqlc.types.Field(Float, graphql_name="maxDuration")
    day_of_week = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(DayOfWeek)), graphql_name="dayOfWeek"
    )
    reservation = sgqlc.types.Field(
        ReservationRestrictionType, graphql_name="reservation"
    )


class TariffResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "energy", "flat", "parking_time", "time", "vat")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    energy = sgqlc.types.Field(Float, graphql_name="energy")
    flat = sgqlc.types.Field(Float, graphql_name="flat")
    parking_time = sgqlc.types.Field(Float, graphql_name="parkingTime")
    time = sgqlc.types.Field(Float, graphql_name="time")
    vat = sgqlc.types.Field(Float, graphql_name="vat")


class TariffTimeslot(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("timeslot_number", "items")
    timeslot_number = sgqlc.types.Field(Int, graphql_name="timeslotNumber")
    items = sgqlc.types.Field(
        sgqlc.types.list_of("TariffTimeslotItem"), graphql_name="items"
    )


class TariffTimeslotItem(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "type",
        "start_price",
        "energy_price",
        "minute_price",
        "idle_minute_price",
        "source",
        "additional_provider",
        "vat_type",
    )
    type = sgqlc.types.Field(TransactionPeriodItemType, graphql_name="type")
    start_price = sgqlc.types.Field(Float, graphql_name="startPrice")
    energy_price = sgqlc.types.Field(Float, graphql_name="energyPrice")
    minute_price = sgqlc.types.Field(Float, graphql_name="minutePrice")
    idle_minute_price = sgqlc.types.Field(Float, graphql_name="idleMinutePrice")
    source = sgqlc.types.Field(TransactionPeriodItemSource, graphql_name="source")
    additional_provider = sgqlc.types.Field(Provider, graphql_name="additionalProvider")
    vat_type = sgqlc.types.Field(InvoiceVatType, graphql_name="vatType")


class Ticket(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "sign_on_date",
        "last_action_date",
        "creator",
        "creator_company",
        "reported_by",
        "customer",
        "customer_name",
        "user_group",
        "status",
        "charge_station",
        "charge_station_name",
        "type",
        "source",
        "description",
        "extra_info",
        "action_holder",
        "action_taken",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    sign_on_date = sgqlc.types.Field(String, graphql_name="signOnDate")
    last_action_date = sgqlc.types.Field(String, graphql_name="lastActionDate")
    creator = sgqlc.types.Field(String, graphql_name="creator")
    creator_company = sgqlc.types.Field(String, graphql_name="creatorCompany")
    reported_by = sgqlc.types.Field(String, graphql_name="reportedBy")
    customer = sgqlc.types.Field(Customer, graphql_name="customer")
    customer_name = sgqlc.types.Field(String, graphql_name="customerName")
    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    status = sgqlc.types.Field(TicketStatus, graphql_name="status")
    charge_station = sgqlc.types.Field(ChargeStation, graphql_name="chargeStation")
    charge_station_name = sgqlc.types.Field(String, graphql_name="chargeStationName")
    type = sgqlc.types.Field(TicketType, graphql_name="type")
    source = sgqlc.types.Field(TicketSource, graphql_name="source")
    description = sgqlc.types.Field(String, graphql_name="description")
    extra_info = sgqlc.types.Field(String, graphql_name="extraInfo")
    action_holder = sgqlc.types.Field(String, graphql_name="actionHolder")
    action_taken = sgqlc.types.Field(String, graphql_name="actionTaken")


class TicketCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(Ticket), graphql_name="items")
    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")


class TokenResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "owner_person",
        "transaction_customer",
        "customer",
        "product_customer",
        "usergroup_id",
        "usergroup",
        "token_issuer_id",
        "expiry_date",
        "external_id",
        "internal_id",
        "info",
        "status",
        "roaming",
        "payer_transactions",
        "payer_subscriptions",
        "reference",
        "remote_password",
        "roaming_home_charging_enabled",
        "type",
        "global_",
        "contract_id",
        "emi3_id",
        "roaming_hub_status",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    owner_person = sgqlc.types.Field(Person, graphql_name="ownerPerson")
    transaction_customer = sgqlc.types.Field(
        Customer, graphql_name="transactionCustomer"
    )
    customer = sgqlc.types.Field(Customer, graphql_name="customer")
    product_customer = sgqlc.types.Field(Customer, graphql_name="productCustomer")
    usergroup_id = sgqlc.types.Field(ID, graphql_name="usergroupId")
    usergroup = sgqlc.types.Field("UserGroup", graphql_name="usergroup")
    token_issuer_id = sgqlc.types.Field(Int, graphql_name="tokenIssuerId")
    expiry_date = sgqlc.types.Field(String, graphql_name="expiryDate")
    external_id = sgqlc.types.Field(String, graphql_name="externalId")
    internal_id = sgqlc.types.Field(String, graphql_name="internalId")
    info = sgqlc.types.Field(String, graphql_name="info")
    status = sgqlc.types.Field(String, graphql_name="status")
    roaming = sgqlc.types.Field(Boolean, graphql_name="roaming")
    payer_transactions = sgqlc.types.Field(Int, graphql_name="payerTransactions")
    payer_subscriptions = sgqlc.types.Field(Int, graphql_name="payerSubscriptions")
    reference = sgqlc.types.Field(String, graphql_name="reference")
    remote_password = sgqlc.types.Field(String, graphql_name="remotePassword")
    roaming_home_charging_enabled = sgqlc.types.Field(
        Boolean, graphql_name="roamingHomeChargingEnabled"
    )
    type = sgqlc.types.Field(String, graphql_name="type")
    global_ = sgqlc.types.Field(Boolean, graphql_name="global")
    contract_id = sgqlc.types.Field(String, graphql_name="contractId")
    emi3_id = sgqlc.types.Field(String, graphql_name="emi3Id")
    roaming_hub_status = sgqlc.types.Field(CardState, graphql_name="roamingHubStatus")


class Transaction(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "transaction_id",
        "transaction_status",
        "energy_delivered",
        "vat",
        "total_amount",
        "payment_method",
        "duration_charging",
        "duration_idle",
        "tariff_id",
        "min_price",
        "max_price",
        "price_elements",
        "start_date",
        "end_date",
        "update_date",
        "channel_id",
        "channel_visible_id",
        "channel_name",
        "evse_id",
        "connector_no",
        "address",
        "zip_code",
        "city",
        "province",
        "country_code",
        "time_zone",
        "currency",
        "loyalty_card_identifier",
        "loyalty_card_type",
        "payment",
        "chosen_payment_method",
        "billing_profile",
        "cust_currency",
        "exchange_rate",
        "conversion_fee",
        "provider_details",
        "charging_profile_type",
    )
    transaction_id = sgqlc.types.Field(
        sgqlc.types.non_null(ID), graphql_name="transactionId"
    )
    transaction_status = sgqlc.types.Field(String, graphql_name="transactionStatus")
    energy_delivered = sgqlc.types.Field(Float, graphql_name="energyDelivered")
    vat = sgqlc.types.Field(Float, graphql_name="vat")
    total_amount = sgqlc.types.Field(Float, graphql_name="totalAmount")
    payment_method = sgqlc.types.Field(String, graphql_name="paymentMethod")
    duration_charging = sgqlc.types.Field(Float, graphql_name="durationCharging")
    duration_idle = sgqlc.types.Field(Float, graphql_name="durationIdle")
    tariff_id = sgqlc.types.Field(ID, graphql_name="tariffId")
    min_price = sgqlc.types.Field(Float, graphql_name="minPrice")
    max_price = sgqlc.types.Field(Float, graphql_name="maxPrice")
    price_elements = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(PriceElement)),
        graphql_name="priceElements",
    )
    start_date = sgqlc.types.Field(String, graphql_name="startDate")
    end_date = sgqlc.types.Field(String, graphql_name="endDate")
    update_date = sgqlc.types.Field(String, graphql_name="updateDate")
    channel_id = sgqlc.types.Field(ID, graphql_name="channelId")
    channel_visible_id = sgqlc.types.Field(String, graphql_name="channelVisibleId")
    channel_name = sgqlc.types.Field(String, graphql_name="channelName")
    evse_id = sgqlc.types.Field(String, graphql_name="evseId")
    connector_no = sgqlc.types.Field(ID, graphql_name="connectorNo")
    address = sgqlc.types.Field(String, graphql_name="address")
    zip_code = sgqlc.types.Field(String, graphql_name="zipCode")
    city = sgqlc.types.Field(String, graphql_name="city")
    province = sgqlc.types.Field(String, graphql_name="province")
    country_code = sgqlc.types.Field(String, graphql_name="countryCode")
    time_zone = sgqlc.types.Field(String, graphql_name="timeZone")
    currency = sgqlc.types.Field(String, graphql_name="currency")
    loyalty_card_identifier = sgqlc.types.Field(
        ID, graphql_name="loyaltyCardIdentifier"
    )
    loyalty_card_type = sgqlc.types.Field(String, graphql_name="loyaltyCardType")
    payment = sgqlc.types.Field(Payment, graphql_name="payment")
    chosen_payment_method = sgqlc.types.Field(
        String, graphql_name="chosenPaymentMethod"
    )
    billing_profile = sgqlc.types.Field(BillingProfile, graphql_name="billingProfile")
    cust_currency = sgqlc.types.Field(String, graphql_name="custCurrency")
    exchange_rate = sgqlc.types.Field(Float, graphql_name="exchangeRate")
    conversion_fee = sgqlc.types.Field(Float, graphql_name="conversionFee")
    provider_details = sgqlc.types.Field(
        ProviderDetails, graphql_name="providerDetails"
    )
    charging_profile_type = sgqlc.types.Field(
        String, graphql_name="chargingProfileType"
    )


class TransactionCard(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("internal_id", "external_id", "contract_id", "type", "is_global")
    internal_id = sgqlc.types.Field(String, graphql_name="internalId")
    external_id = sgqlc.types.Field(String, graphql_name="externalId")
    contract_id = sgqlc.types.Field(String, graphql_name="contractId")
    type = sgqlc.types.Field(CardType, graphql_name="type")
    is_global = sgqlc.types.Field(Boolean, graphql_name="isGlobal")


class TransactionCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "has_next")
    items = sgqlc.types.Field(sgqlc.types.list_of(LmsTransaction), graphql_name="items")
    has_next = sgqlc.types.Field(Boolean, graphql_name="hasNext")


class TransactionLocation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "address",
        "city",
        "country",
        "postal_code",
        "charge_station_id",
        "charge_station_name",
        "timezone",
        "evse",
    )
    address = sgqlc.types.Field(String, graphql_name="address")
    city = sgqlc.types.Field(String, graphql_name="city")
    country = sgqlc.types.Field(Country, graphql_name="country")
    postal_code = sgqlc.types.Field(String, graphql_name="postalCode")
    charge_station_id = sgqlc.types.Field(ID, graphql_name="chargeStationId")
    charge_station_name = sgqlc.types.Field(String, graphql_name="chargeStationName")
    timezone = sgqlc.types.Field(String, graphql_name="timezone")
    evse = sgqlc.types.Field("TransactionLocationEvse", graphql_name="evse")


class TransactionLocationEvse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "channel_no",
        "meter_id",
        "obis_code",
        "power",
        "connector_type",
        "connector_format",
        "current_type",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    channel_no = sgqlc.types.Field(Int, graphql_name="channelNo")
    meter_id = sgqlc.types.Field(String, graphql_name="meterId")
    obis_code = sgqlc.types.Field(String, graphql_name="obisCode")
    power = sgqlc.types.Field(Int, graphql_name="power")
    connector_type = sgqlc.types.Field(
        TransactionConnectorType, graphql_name="connectorType"
    )
    connector_format = sgqlc.types.Field(
        TransactionConnectorFormat, graphql_name="connectorFormat"
    )
    current_type = sgqlc.types.Field(TransactionCurrentType, graphql_name="currentType")


class TransactionPeriod(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "timeslot_number",
        "start_date",
        "end_date",
        "remote_last_update_date",
        "energy_start",
        "energy_consumed",
        "start_used",
        "duration_charging",
        "duration_idle",
        "period_items",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    timeslot_number = sgqlc.types.Field(Int, graphql_name="timeslotNumber")
    start_date = sgqlc.types.Field(String, graphql_name="startDate")
    end_date = sgqlc.types.Field(String, graphql_name="endDate")
    remote_last_update_date = sgqlc.types.Field(
        String, graphql_name="remoteLastUpdateDate"
    )
    energy_start = sgqlc.types.Field(Float, graphql_name="energyStart")
    energy_consumed = sgqlc.types.Field(Float, graphql_name="energyConsumed")
    start_used = sgqlc.types.Field(Boolean, graphql_name="startUsed")
    duration_charging = sgqlc.types.Field(Int, graphql_name="durationCharging")
    duration_idle = sgqlc.types.Field(Int, graphql_name="durationIdle")
    period_items = sgqlc.types.Field(
        sgqlc.types.list_of("TransactionPeriodItem"), graphql_name="periodItems"
    )


class TransactionPeriodItem(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "type",
        "start_cost",
        "energy_cost",
        "minute_cost",
        "idle_minute_cost",
        "total_cost",
        "source",
        "additional_provider",
        "vat_type",
    )
    id = sgqlc.types.Field(ID, graphql_name="id")
    type = sgqlc.types.Field(TransactionPeriodItemType, graphql_name="type")
    start_cost = sgqlc.types.Field(Float, graphql_name="startCost")
    energy_cost = sgqlc.types.Field(Float, graphql_name="energyCost")
    minute_cost = sgqlc.types.Field(Float, graphql_name="minuteCost")
    idle_minute_cost = sgqlc.types.Field(Float, graphql_name="idleMinuteCost")
    total_cost = sgqlc.types.Field(Float, graphql_name="totalCost")
    source = sgqlc.types.Field(TransactionPeriodItemSource, graphql_name="source")
    additional_provider = sgqlc.types.Field(Provider, graphql_name="additionalProvider")
    vat_type = sgqlc.types.Field(InvoiceVatType, graphql_name="vatType")


class TransactionPrice(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "type",
        "start_cost",
        "energy_cost",
        "minute_cost",
        "idle_minute_cost",
        "total_cost",
        "vat_percentage",
        "vat_type",
        "vat_country",
        "currency",
        "customer_currency",
        "exchange_rate",
        "conversion_fee",
        "conversion_amount",
        "customer",
        "provider",
        "roaming_profile",
        "billing_type",
        "invoice",
    )
    type = sgqlc.types.Field(TransactionPeriodItemType, graphql_name="type")
    start_cost = sgqlc.types.Field(Float, graphql_name="startCost")
    energy_cost = sgqlc.types.Field(Float, graphql_name="energyCost")
    minute_cost = sgqlc.types.Field(Float, graphql_name="minuteCost")
    idle_minute_cost = sgqlc.types.Field(Float, graphql_name="idleMinuteCost")
    total_cost = sgqlc.types.Field(Float, graphql_name="totalCost")
    vat_percentage = sgqlc.types.Field(Float, graphql_name="vatPercentage")
    vat_type = sgqlc.types.Field(TransactionVatType, graphql_name="vatType")
    vat_country = sgqlc.types.Field(Country, graphql_name="vatCountry")
    currency = sgqlc.types.Field(Currency, graphql_name="currency")
    customer_currency = sgqlc.types.Field(Currency, graphql_name="customerCurrency")
    exchange_rate = sgqlc.types.Field(Float, graphql_name="exchangeRate")
    conversion_fee = sgqlc.types.Field(Float, graphql_name="conversionFee")
    conversion_amount = sgqlc.types.Field(Float, graphql_name="conversionAmount")
    customer = sgqlc.types.Field(Customer, graphql_name="customer")
    provider = sgqlc.types.Field(Provider, graphql_name="provider")
    roaming_profile = sgqlc.types.Field(String, graphql_name="roamingProfile")
    billing_type = sgqlc.types.Field(TransactionBillingType, graphql_name="billingType")
    invoice = sgqlc.types.Field(Invoice, graphql_name="invoice")


class UserGroup(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = (
        "id",
        "name",
        "provider",
        "user_group_profile",
        "default_app_profile",
        "full_path",
        "cards",
        "invoices",
        "tickets",
        "charge_groups",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    name = sgqlc.types.Field(String, graphql_name="name")
    provider = sgqlc.types.Field(Provider, graphql_name="provider")
    user_group_profile = sgqlc.types.Field(String, graphql_name="userGroupProfile")
    default_app_profile = sgqlc.types.Field(String, graphql_name="defaultAppProfile")
    full_path = sgqlc.types.Field(String, graphql_name="fullPath")
    cards = sgqlc.types.Field(
        CardCollection,
        graphql_name="cards",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(CardFilter, graphql_name="filters", default=None),
                ),
                ("sort", sgqlc.types.Arg(CardSort, graphql_name="sort", default=None)),
            )
        ),
    )
    invoices = sgqlc.types.Field(
        InvoiceCollection,
        graphql_name="invoices",
        args=sgqlc.types.ArgDict(
            (
                ("page", sgqlc.types.Arg(Int, graphql_name="page", default=None)),
                (
                    "items_per_page",
                    sgqlc.types.Arg(Int, graphql_name="itemsPerPage", default=None),
                ),
                (
                    "filters",
                    sgqlc.types.Arg(
                        InvoiceFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(InvoiceSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    tickets = sgqlc.types.Field(
        TicketCollection,
        graphql_name="tickets",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(TicketFilter, graphql_name="filters", default=None),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(TicketSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )
    charge_groups = sgqlc.types.Field(
        ChargeGroupCollection,
        graphql_name="chargeGroups",
        args=sgqlc.types.ArgDict(
            (
                (
                    "filters",
                    sgqlc.types.Arg(
                        ChargeGroupFilter, graphql_name="filters", default=None
                    ),
                ),
                (
                    "sort",
                    sgqlc.types.Arg(ChargeGroupSort, graphql_name="sort", default=None),
                ),
            )
        ),
    )


class UserGroupCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(UserGroup), graphql_name="items")
    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")


########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None
