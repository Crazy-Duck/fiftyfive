import sgqlc.types
import sgqlc.types.datetime

schema = sgqlc.types.Schema()


__docformat__ = "markdown"


########################################################################
# Scalars and Enumerations
########################################################################
class AccessOptionsEnum(sgqlc.types.Enum):
    """Defines who can access the charge station and under what
    conditions.

    Enumeration Choices:

    * `Private`: Restricted access, only authorized users (e.g.
      employees or tenants).
    * `PublicFree`: Open and free to the public.
    * `PublicPaid`: Publicly available, but requires payment.
    """

    __schema__ = schema
    __choices__ = ("Private", "PublicFree", "PublicPaid")


class AuthorizationMode(sgqlc.types.Enum):
    """Defines how charging sessions are authorized at a station.

    Enumeration Choices:

    * `AutoCharge`: Automatic authorization, typically for known users
      or registered vehicles.
    * `SwipeAndCharge`: Requires physical interaction (e.g. RFID card
      swipe) before charging starts.
    """

    __schema__ = schema
    __choices__ = ("AutoCharge", "SwipeAndCharge")


class BankAccountScheme(sgqlc.types.Enum):
    """Enumeration Choices:

    * `IBAN`: International Bank Account Number
    * `UK_SORT_CODE`: Bank Sort Code
    """

    __schema__ = schema
    __choices__ = ("IBAN", "UK_SORT_CODE")


Boolean = sgqlc.types.Boolean


class Capability(sgqlc.types.Enum):
    """Enumeration Choices:

    * `CASH_PAYABLE`None
    * `CHARGE_BACK`None
    * `CHARGING_PREFERENCES_CAPABLE`None
    * `CHARGING_PROFILE_CAPABLE`None
    * `CHIP_CARD_SUPPORT`None
    * `CONTACTLESS_CARD_SUPPORT`None
    * `CREDIT_CARD_PAYABLE`None
    * `DEBIT_CARD_PAYABLE`None
    * `DIRECT_PAYMENT`None
    * `FREE_TRANSACTION`None
    * `HAS_METER_VALUES`None
    * `HUBJECT`None
    * `IEC_15118`None
    * `PED_TERMINAL`None
    * `REMOTE_DIRECT_PAYMENT`None
    * `REMOTE_START_STOP_CAPABLE`None
    * `RESERVABLE`None
    * `RFID_READER`None
    * `TOKEN_GROUP_CAPABLE`None
    * `UNLOCK_CAPABLE`None
    """

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
    """Enumeration Choices:

    * `ACTIVE`None
    """

    __schema__ = schema
    __choices__ = ("ACTIVE",)


class CardState(sgqlc.types.Enum):
    """Lifecycle states of an RFID or digital charging card.

    Enumeration Choices:

    * `Active`: Active.
    * `Blocked`: Blocked.
    * `Deactivated`: Deactivated.
    * `Inactive`: Inactive.
    * `MarkedForDeletion`: Marked for deletion.
    """

    __schema__ = schema
    __choices__ = ("Active", "Blocked", "Deactivated", "Inactive", "MarkedForDeletion")


class CardType(sgqlc.types.Enum):
    """Types of charging authentication tokens/cards.

    Enumeration Choices:

    * `Anonymous`: Anonymous.
    * `Barcode`: Barcode.
    * `Group`: Group.
    * `IEC_15118`: IEC 15118.
    * `PlugAndCharge`: Plug and charge.
    * `QRcode`: QR code.
    * `RFID`: RFID.
    * `Remote`: Remote.
    """

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
    """Enumeration of charge group categories.   Defines the general
    classification of a charge group, which determines its typical use
    case (e.g., residential charging vs. commercial or public
    charging).

    Enumeration Choices:

    * `Home`: A charge group associated with a residential or home
      installation.
    * `Other`: A charge group associated with non-residential
      installations such as workplaces, fleets, or public sites.
    """

    __schema__ = schema
    __choices__ = ("Home", "Other")


class ChargeStationChannelAcDc(sgqlc.types.Enum):
    """Whether the channel provides alternating current (AC) or direct
    current (DC). AC is typical for home and slow charging, DC for
    fast charging.

    Enumeration Choices:

    * `AC`: Alternating current (AC).
    * `DC`: Direct current (DC).
    """

    __schema__ = schema
    __choices__ = ("AC", "DC")


class ChargeStationChannelCapability(sgqlc.types.Enum):
    """Functional capabilities supported by a charge station channel.
    Defines optional features like reservation, authorization, or
    payment mechanisms.

    Enumeration Choices:

    * `CashPayable`: Supports cash payments at the station.
    * `ChargeBack`: Supports chargeback / reimbursement reporting.
    * `ChargingProfile`: Supports configurable charging profiles
      (power limits, schedules).
    * `CreditCardPayable`: Supports on-site credit card payments.
    * `DebitCardPayable`: Supports on-site debit card payments.
    * `FreeTransaction`: Allows free-of-charge transactions.
    * `HasMeterValues`: Provides metered values (e.g., kWh delivered).
    * `Hubject`: Compatible with Hubject roaming platform.
    * `Iec15118`: Supports ISO 15118 (Plug & Charge).
    * `LocalKey`: Supports local key-based authorization.
    * `LocalPrepaid`: Supports local prepaid tokens or vouchers.
    * `MaxOverridableCurrent`: Maximum charging current can be
      overridden.
    * `NoAuthorization`: Allows charging without explicit
      authorization.
    * `RemotePrepaid`: Supports remote prepaid sessions.
    * `RemoteStartStop`: Supports remote start and stop of charging
      sessions.
    * `Reservable`: Channel can be reserved in advance.
    * `Rfid`: Supports RFID authentication.
    * `Unlockable`: Connector can be remotely unlocked.
    """

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
    """Format of the connector presented by the channel. A connector may
    be a fixed cable or a socket into which drivers plug their own
    cable.

    Enumeration Choices:

    * `Cable`: Permanently attached charging cable supplied by the
      station.
    * `Socket`: Socket outlet where a driver must provide their own
      cable.
    """

    __schema__ = schema
    __choices__ = ("Cable", "Socket")


class ChargeStationChannelConnectorType(sgqlc.types.Enum):
    """Standardized connector type attached to a channel. Defines the
    physical plug interface supported by the EVSE.

    Enumeration Choices:

    * `Chademo`: CHAdeMO DC fast charging connector.
    * `DomesticA`: Domestic socket type A.
    * `DomesticB`: Domestic socket type B.
    * `DomesticC`: Domestic socket type C.
    * `DomesticD`: Domestic socket type D.
    * `DomesticE`: Domestic socket type E.
    * `DomesticF`: Domestic Schuko plug (Type F).
    * `DomesticG`: Domestic socket type G.
    * `DomesticH`: Domestic socket type H.
    * `DomesticI`: Domestic socket type I.
    * `DomesticJ`: Domestic socket type J.
    * `DomesticK`: Domestic socket type K.
    * `DomesticL`: Domestic socket type L.
    * `Iec603092Single16`: IEC 60309 2P+E 16A single-phase (blue
      industrial plug).
    * `Iec603092Three16`: IEC 60309 three-phase industrial plugs
      (16A).
    * `Iec603092Three32`: IEC 60309 three-phase industrial plugs
      (32A).
    * `Iec603092Three64`: IEC 60309 three-phase industrial plugs
      (64A).
    * `Iec62196T1`: Type 1 socket (SAE J1772).
    * `Iec62196T1Combo`: Type 1 Combo (CCS1).
    * `Iec62196T2`: Type 2 socket (IEC 62196).
    * `Iec62196T2Combo`: Type 2 Combo (CCS2).
    * `Iec62196T3A`: Type 3A socket (low-power).
    * `Iec62196T3C`: Type 3C socket (three-phase).
    * `TeslaR`: Tesla proprietary connector R.
    * `TeslaS`: Tesla proprietary connector S.
    """

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
    """High-level availability status of a charge station channel.
    Aggregates technical status into user-friendly categories.

    Enumeration Choices:

    * `Available`: Channel is available and ready for a charging
      session.
    * `Charging`: A charging session is currently active on this
      channel.
    * `Faulty`: A fault or error condition prevents usage of this
      channel.
    * `NoCommunication`: Channel cannot communicate with the station
      backend or controller.
    * `PoweredOff`: The physical hardware is powered off.
    * `Reserved`: Channel is reserved for a user but not yet charging.
    * `Unavailable`: Channel is temporarily unavailable (e.g., locked
      by admin or in transition).
    * `Unknown`: The current state of the channel is unknown or not
      reported.
    """

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
    """Technical or error status reported by the charge station channel.
    Provides granular diagnostic info about hardware or transaction
    conditions.

    Enumeration Choices:

    * `AlarmInputActivated`: Alarm input triggered (e.g., emergency
      stop).
    * `Blocked`: Channel blocked (administrative or technical).
    * `CableUnderrated`: Connected cable is underrated for requested
      current.
    * `CardExpired`: Authentication error: card expired.
    * `ChannelRelay1Active`: Relay 1 is active (internal switching
      element).
    * `ChannelRelay2Active`: Relay 2 is active (internal switching
      element).
    * `ChargingComplete`: Charging session complete.
    * `ChargingProfileActive`: Active charging profile in use.
    * `CpDiodeDetectionError`: Control pilot diode detection error.
    * `CpStateCDetected`: Control pilot state C detected.
    * `CpStateChangedTooOften`: Control pilot state changed too often.
    * `CpUnknown`: Control pilot unknown.
    * `DccIsolationError`: DC charging isolation error.
    * `DccPowerSupplyRelatedError`: DC charging power supply related
      error.
    * `DccVehicleRelatedError`: DC vehicle related error.
    * `EmergencySwitch`: Emergency switch activated.
    * `EventlogFull`: Event log storage full.
    * `FoundLowCosphi`: Power factor (cos φ) too low.
    * `FuseTripped`: Fuse tripped.
    * `GenericFaulty`: Generic or unknown fault condition.
    * `KwhError`: Energy metering error.
    * `LockEngaged`: Connector lock is engaged.
    * `NoCommunication`: Communication issue.
    * `Ok`: Channel is healthy and operational.
    * `OvercurrentError`: Overcurrent detected.
    * `PowerFailure`: Power failure.
    * `PrepaidLimitReached`: Prepaid limit reached.
    * `Rcd2Tripped`: Residual current device 2 tripped.
    * `RcdTripped`: Residual current device tripped.
    * `RelayError`: Error in power relay or fuse tripped.
    * `SimpleChargerNetworkFound`: Non-standard/simple charger
      detected on the network.
    * `StateCbABDetected`: Control pilot detected abnormal state.
    * `TagReaderError`: Tag reader malfunction.
    * `TemperatureLimitReached`: Overtemperature limit reached.
    * `TemperatureWarning`: Overtemperature warnings or limits
      reached.
    * `Transaction`: A transaction is currently active.
    * `UtilityKwhError`: Utility energy metering error.
    * `VentilationRequired`: Ventilation is required for safe
      charging.
    * `WatchdogResetOccured`: Watchdog reset has occurred.
    """

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
    """Operational state of a charge station. Indicates whether the
    charging hardware is available, out of service, or
    administratively blocked.

    Enumeration Choices:

    * `Active`: The station is online and operational for charging.
    * `Blocked`: The station is blocked, either due to administrative
      lock, maintenance, or policy restrictions.
    * `Inactive`: The station is offline, disabled, or not currently
      usable.
    """

    __schema__ = schema
    __choices__ = ("Active", "Blocked", "Inactive")


class ChargeStationSubscriptionState(sgqlc.types.Enum):
    """Possible subscription states of a charge station. Indicates
    whether a subscription is active or terminated.

    Enumeration Choices:

    * `Active`: Subscription is currently active.
    """

    __schema__ = schema
    __choices__ = ("Active",)


class ChargingMode(sgqlc.types.Enum):
    """Enumeration Choices:

    * `MaxSolar`None
    * `OptimizedSolar`None
    * `PureSolar`None
    * `RegularCharging`None
    """

    __schema__ = schema
    __choices__ = ("MaxSolar", "OptimizedSolar", "PureSolar", "RegularCharging")


class ConnectorFormat(sgqlc.types.Enum):
    """Enumeration Choices:

    * `CABLE`None
    * `SOCKET`None
    """

    __schema__ = schema
    __choices__ = ("CABLE", "SOCKET")


class ConnectorType(sgqlc.types.Enum):
    """Enumeration Choices:

    * `CHADEMO`None
    * `DOMESTIC_A`None
    * `DOMESTIC_B`None
    * `DOMESTIC_C`None
    * `DOMESTIC_D`None
    * `DOMESTIC_E`None
    * `DOMESTIC_F`None
    * `DOMESTIC_G`None
    * `DOMESTIC_H`None
    * `DOMESTIC_I`None
    * `DOMESTIC_J`None
    * `DOMESTIC_K`None
    * `DOMESTIC_L`None
    * `IEC_60309_2_single_16`None
    * `IEC_60309_2_three_16`None
    * `IEC_60309_2_three_32`None
    * `IEC_60309_2_three_64`None
    * `IEC_62196_T1`None
    * `IEC_62196_T1_COMBO`None
    * `IEC_62196_T2`None
    * `IEC_62196_T2_COMBO`None
    * `IEC_62196_T3A`None
    * `IEC_62196_T3C`None
    * `PANTOGRAPH_BOTTOM_UP`None
    * `PANTOGRAPH_TOP_DOWN`None
    * `TESLA_R`None
    * `TESLA_S`None
    """

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
    """Defines the format of electronic invoices sent to the customer.

    Enumeration Choices:

    * `NONE`: No electronic invoice
    * `OHNL_FORMAT`: OHNL invoice format
    """

    __schema__ = schema
    __choices__ = ("NONE", "OHNL_FORMAT")


class CustomerFilterState(sgqlc.types.Enum):
    """Filter input for selecting customers by state

    Enumeration Choices:

    * `Active`None
    * `Blocked`None
    * `Deactivated`None
    * `EmailChecked`None
    * `NonActive`None
    * `Registered`None
    """

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
    """Filter input for selecting customers by type

    Enumeration Choices:

    * `Company`None
    * `Employee`None
    * `Private`None
    * `Template`None
    """

    __schema__ = schema
    __choices__ = ("Company", "Employee", "Private", "Template")


class CustomerReimbursementMode(sgqlc.types.Enum):
    """Defines how reimbursements are handled for this customer.

    Enumeration Choices:

    * `NONE`: No reimbursement configured
    * `PER_CHARGE_STATION`: Reimbursement is per charge station
    * `PER_EMPLOYEE`: Reimbursement is per employee
    """

    __schema__ = schema
    __choices__ = ("NONE", "PER_CHARGE_STATION", "PER_EMPLOYEE")


class CustomerSalutation(sgqlc.types.Enum):
    """Customer salutation for formal communication.

    Enumeration Choices:

    * `EMPTY`: No salutation provided
    * `MR`: Mr.
    * `MRS`: Mrs.
    """

    __schema__ = schema
    __choices__ = ("EMPTY", "MR", "MRS")


class CustomerState(sgqlc.types.Enum):
    """Represents the operational or account state of the customer.

    Enumeration Choices:

    * `ACTIVE`: Customer is active and fully operational
    * `BLOCKED`: Customer has been blocked due to issues (e.g., fraud,
      misuse)
    * `DEACTIVATED`: Customer has been deactivated but may retain
      historical data
    * `EMAIL_CHECKED`: Customer's email has been verified
    * `NON_ACTIVE`: Customer is inactive and cannot perform actions
    * `REGISTERED`: Customer has registered but may require email or
      verification
    """

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
    """Defines the type of customer, e.g., private individual, company,
    or employee.

    Enumeration Choices:

    * `COMPANY`: Company customer
    * `EMPLOYEE`: Employee linked to a company or organization
    * `PRIVATE`: Private individual customer
    * `TEMPLATE`: Template customer for testing or default
      configurations
    """

    __schema__ = schema
    __choices__ = ("COMPANY", "EMPLOYEE", "PRIVATE", "TEMPLATE")


Date = sgqlc.types.datetime.Date


class DateTimeISO(sgqlc.types.Scalar):
    """A date-time string at UTC, such as 2007-12-03T10:15:30Z, compliant
    with the `date-time` format outlined in section 5.6 of the RFC
    3339 profile of the ISO 8601 standard for representation of dates
    and times using the Gregorian calendar.This scalar is serialized
    to a string in ISO 8601 format and parsed from a string in ISO
    8601 format.
    """

    __schema__ = schema


class DayOfWeek(sgqlc.types.Enum):
    """Enumeration Choices:

    * `FRIDAY`None
    * `MONDAY`None
    * `SATURDAY`None
    * `SUNDAY`None
    * `THURSDAY`None
    * `TUESDAY`None
    * `WEDNESDAY`None
    """

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
    """Reason why a card/token has been deactivated. Nullable if no
    deactivation occurred.

    Enumeration Choices:

    * `Admin`: Admin.
    * `CardExpired`: Card expired.
    * `Customer`: Customer.
    * `SeeCustomer`: See customer.
    """

    __schema__ = schema
    __choices__ = ("Admin", "CardExpired", "Customer", "SeeCustomer")


class DeviceType(sgqlc.types.Enum):
    """Enumeration Choices:

    * `ANDROID`None
    * `IOS`None
    * `OTHER`None
    """

    __schema__ = schema
    __choices__ = ("ANDROID", "IOS", "OTHER")


class EnergySourceCategory(sgqlc.types.Enum):
    """Categories of energy sources

    Enumeration Choices:

    * `COAL`: Fossil power from coal
    * `GAS`: Fossil power from gas
    * `GENERAL_FOSSIL`: All kinds of fossil power sources
    * `GENERAL_GREEN`: All kinds of regenerative power sources
    * `NUCLEAR`: Nuclear power sources
    * `SOLAR`: Regenerative power from PV
    * `WATER`: Regenerative power from water turbines
    * `WIND`: Regenerative power from wind turbines
    """

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
    """Categories of environmental impact values

    Enumeration Choices:

    * `CARBON_DIOXIDE`: Exhausted carbon dioxide in grams per
      kilowatthour
    * `NUCLEAR_WASTE`: Produced nuclear waste in grams per
      kilowatthour
    """

    __schema__ = schema
    __choices__ = ("CARBON_DIOXIDE", "NUCLEAR_WASTE")


class EvseStatus(sgqlc.types.Enum):
    """Enumeration Choices:

    * `AVAILABLE`None
    * `BLOCKED`None
    * `CHARGING`None
    * `INOPERATIVE`None
    * `OUTOFORDER`None
    * `PLANNED`None
    * `PRE_RESERVED`None
    * `REMOVED`None
    * `RESERVED`None
    * `SYSTEM_RESERVED`None
    * `UNKNOWN`None
    """

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
    """Represents the available app features.

    Enumeration Choices:

    * `GUEST_MODE`None
    * `SHELL_FIRST_TIME_ONBOARDING`None
    * `VOICE_AGENT`None
    """

    __schema__ = schema
    __choices__ = ("GUEST_MODE", "SHELL_FIRST_TIME_ONBOARDING", "VOICE_AGENT")


class FeatureSource(sgqlc.types.Enum):
    """Represents the source of an effective app feature.

    Enumeration Choices:

    * `APP`None
    * `CUSTOMER`None
    * `DYNAMIC`None
    """

    __schema__ = schema
    __choices__ = ("APP", "CUSTOMER", "DYNAMIC")


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int


class InvoiceBillingType(sgqlc.types.Enum):
    """Defines the billing type for an invoice, specifying how the
    invoice is handled financially.

    Enumeration Choices:

    * `Regular`: Standard invoice issued to the customer
    * `Reimbursement`: Invoice related to reimbursement
    * `ReimbursementPayout`: Invoice representing a reimbursement
      payout
    * `Selfbill`: Self-billed invoice issued automatically by the
      system
    """

    __schema__ = schema
    __choices__ = ("Regular", "Reimbursement", "ReimbursementPayout", "Selfbill")


class InvoicePaymentMethod(sgqlc.types.Enum):
    """Payment method used to settle the invoice.

    Enumeration Choices:

    * `AutoCollection`: Payment automatically collected by system
    * `Direct`: Direct payment by customer
    * `Free`: No payment required (free service)
    * `Invoice`: Standard invoice payment
    * `PaymentTerminal`: Paid at a physical payment terminal
    * `Wallet`: Paid using wallet balance
    """

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
    """Represents the current status of an invoice, indicating processing
    stage and payment state.

    Enumeration Choices:

    * `Blocked`: Customer is blocked from further payments
    * `Created`: Invoice has been created but not yet sent
    * `CreditNoteCreated`: Credit note created for invoice
    * `CreditNoteSent`: Credit note has been sent to customer
    * `CustomIgnored`: Invoice ignored by customer
    * `CustomPaid`: Invoice paid by customer
    * `CustomRefused`: Invoice refused by customer
    * `DirectDebitCreated`: Direct debit setup has been created
    * `NewDebitInvoiceCreated`: A new debit invoice was created to
      adjust previous invoices
    * `Overpaid`: Overpayment detected
    * `Paid`: Invoice fully paid
    * `PaidAfterActionTaken`: Paid after an action was taken
    * `PaymentActionTaken`: Payment action has been taken
    * `PaymentOverdue`: Payment is overdue
    * `PaymentOverdueLastCall`: Payment overdue, last reminder sent
    * `PaymentTakeAction`: Payment requires administrative action
    * `Seen`: Invoice has been viewed by the customer
    * `Sent`: Invoice has been sent to the customer
    * `WaitingForPayment`: Waiting for payment from the customer
    """

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
    """Defines the type of invoice, representing the context of the
    billing.

    Enumeration Choices:

    * `Customer`: Invoice issued to a regular customer
    * `Prepaid`: Invoice related to prepaid accounts
    * `Provider`: Invoice issued by provider
    * `Roaming`: Roaming invoice for customer charging outside home
      network
    * `RoamingIncoming`: Incoming roaming invoice received from
      external network
    """

    __schema__ = schema
    __choices__ = ("Customer", "Prepaid", "Provider", "Roaming", "RoamingIncoming")


class InvoiceVatType(sgqlc.types.Enum):
    """Specifies the VAT (Value Added Tax) treatment for an invoice.

    Enumeration Choices:

    * `ChargingCountry`: VAT based on the country where charging
      occurs
    * `Default`: Default VAT rate applicable in system
    * `NoVat`: No VAT applied
    * `OutsideVat`: VAT does not apply because the transaction is
      outside VAT jurisdiction
    * `ReverseCharge`: Reverse charge VAT mechanism
    """

    __schema__ = schema
    __choices__ = ("ChargingCountry", "Default", "NoVat", "OutsideVat", "ReverseCharge")


class JSON(sgqlc.types.Scalar):
    __schema__ = schema


class LegacyTariffItemType(sgqlc.types.Enum):
    """Enumeration Choices:

    * `kwh`None
    * `minute`None
    * `minute_parking`None
    * `start`None
    """

    __schema__ = schema
    __choices__ = ("kwh", "minute", "minute_parking", "start")


class LegacyTariffTimeslotDayOfWeek(sgqlc.types.Enum):
    """Enumeration Choices:

    * `friday`None
    * `monday`None
    * `saturday`None
    * `sunday`None
    * `thursday`None
    * `tuesday`None
    * `wednesday`None
    """

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
    """Represents the platform type of the user.

    Enumeration Choices:

    * `android`: Android platform
    * `ios`: iOS platform
    * `macos`: Mac OS platform
    * `web`: Web platform
    * `windows`: Windows platform
    """

    __schema__ = schema
    __choices__ = ("android", "ios", "macos", "web", "windows")


class LiveKitVoiceAgentEnvironment(sgqlc.types.Enum):
    """Represents the environment of the voice agent.

    Enumeration Choices:

    * `DEV`None
    * `LOCAL`None
    * `PROD`None
    * `STAGING`None
    """

    __schema__ = schema
    __choices__ = ("DEV", "LOCAL", "PROD", "STAGING")


class LmsAvailability(sgqlc.types.Enum):
    """LMS availability filter

    Enumeration Choices:

    * `ALL`: All locations
    * `AVAILABLE`: Only available locations
    """

    __schema__ = schema
    __choices__ = ("ALL", "AVAILABLE")


class LmsLocationType(sgqlc.types.Enum):
    """Classifies the physical type of a charging location. Used to
    distinguish between public parking lots, underground garages,
    private sites, etc.

    Enumeration Choices:

    * `CarPark`: Car park.
    * `Other`: Other.
    * `ParkingInPublicSpace`: Parking in public space.
    * `ParkingLot`: Parking lot.
    * `PrivateLocation`: Private location.
    * `TestStation`: Test station.
    * `UndergroundCarPark`: Underground car park.
    * `Unknown`: Unknown.
    """

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
    """Enumeration Choices:

    * `days`None
    * `hours`None
    * `minutes`None
    """

    __schema__ = schema
    __choices__ = ("days", "hours", "minutes")


class OdooOrderDirection(sgqlc.types.Enum):
    """Enumeration Choices:

    * `asc`None
    * `desc`None
    """

    __schema__ = schema
    __choices__ = ("asc", "desc")


class OdooTeamId(sgqlc.types.Enum):
    """Enumeration Choices:

    * `CHARGECARD_L1`None
    * `TARIFF_CHANGE_L2`None
    """

    __schema__ = schema
    __choices__ = ("CHARGECARD_L1", "TARIFF_CHANGE_L2")


class OdooTicketStatus(sgqlc.types.Enum):
    """Enumeration Choices:

    * `CLOSED`None
    * `OPEN`None
    """

    __schema__ = schema
    __choices__ = ("CLOSED", "OPEN")


class PowerType(sgqlc.types.Enum):
    """Enumeration Choices:

    * `AC`None
    * `AC_1_PHASE`None
    * `AC_3_PHASE`None
    * `DC`None
    """

    __schema__ = schema
    __choices__ = ("AC", "AC_1_PHASE", "AC_3_PHASE", "DC")


class ProductPaymentMode(sgqlc.types.Enum):
    """Payment mode of the subscription product

    Enumeration Choices:

    * `CustomerPays`: Customer pays
    * `ProviderPays`: Provider pays
    """

    __schema__ = schema
    __choices__ = ("CustomerPays", "ProviderPays")


class ProductPaymentPeriodMode(sgqlc.types.Enum):
    """Payment period mode of the subscription product

    Enumeration Choices:

    * `Monthly`: Monthly
    * `Once`: Once
    """

    __schema__ = schema
    __choices__ = ("Monthly", "Once")


class ProductSelectionMode(sgqlc.types.Enum):
    """Selection mode of the subscription product

    Enumeration Choices:

    * `NotSelectable`: Not selectable
    * `Selectable`: Selectable
    * `SelectableOnlyX`: Selectable only X
    """

    __schema__ = schema
    __choices__ = ("NotSelectable", "Selectable", "SelectableOnlyX")


class ProductType(sgqlc.types.Enum):
    """Type of the subscription product

    Enumeration Choices:

    * `Card`: Card product
    * `PaymentTerminal`: Payment terminal product
    * `RechargeSpot`: Recharge spot product
    """

    __schema__ = schema
    __choices__ = ("Card", "PaymentTerminal", "RechargeSpot")


class ProductUsageType(sgqlc.types.Enum):
    """Usage type of the subscription product

    Enumeration Choices:

    * `Card`: Card product
    * `Free`: Free product
    * `InvoiceOnly`: Invoice only product
    * `Other`: Other product
    * `Private`: Private product
    * `PriveProduct`: Prive product
    * `PublicProduct`: Public product
    * `SimOnly`: Sim only product
    """

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
    """The category of the provider that the customer belongs to, for
    example NL, UK, DE, etc.

    Enumeration Choices:

    * `AT`: AT provider category
    * `BE`: BE provider category
    * `CHF`: CHF provider category
    * `DE`: DE provider category
    * `ES`: ES provider category
    * `FR`: FR provider category
    * `IT`: IT provider category
    * `NL`: NL provider category
    * `None`: No provider category
    * `PL`: PL provider category
    * `UBER`: UBER provider category
    * `UK`: UK provider category
    """

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
    """Defines whether a charge station is accessible publicly or
    privately.

    Enumeration Choices:

    * `Private`: Charge station is accessible privately.
    * `Public`: Charge station is accessible publicly.
    """

    __schema__ = schema
    __choices__ = ("Private", "Public")


class PushNotificationType(sgqlc.types.Enum):
    """Enumeration Choices:

    * `ACCOUNT`None
    * `CHARGEPOINT`None
    * `SUPPORT`None
    * `TARIFF`None
    """

    __schema__ = schema
    __choices__ = ("ACCOUNT", "CHARGEPOINT", "SUPPORT", "TARIFF")


class ReservationRestrictionType(sgqlc.types.Enum):
    """Enumeration Choices:

    * `RESERVATION`None
    * `RESERVATION_EXPIRES`None
    """

    __schema__ = schema
    __choices__ = ("RESERVATION", "RESERVATION_EXPIRES")


class RetrievePasswordStatus(sgqlc.types.Enum):
    """Retrieve password status

    Enumeration Choices:

    * `INVALID`: Invalid password retrieval
    * `INVALID_REQUEST`: Invalid request
    * `VALID`: Valid password retrieval
    * `VERSION_TOO_LOW`: Version too low
    """

    __schema__ = schema
    __choices__ = ("INVALID", "INVALID_REQUEST", "VALID", "VERSION_TOO_LOW")


class RoamingRole(sgqlc.types.Enum):
    """Defines the role of this card when participating in roaming
    networks.

    Enumeration Choices:

    * `CPO`: Charge Point Operator (CPO) role.
    * `DataConsumer`: Entity that consumes roaming data.
    * `DataSupplier`: Entity that supplies roaming data (whitelists,
      authorizations, etc.).
    * `LmsDataConsumer`: Consumer of LMS-specific roaming data.
    * `MSP`: Mobility Service Provider (MSP) role.
    """

    __schema__ = schema
    __choices__ = ("CPO", "DataConsumer", "DataSupplier", "LmsDataConsumer", "MSP")


class Salutation(sgqlc.types.Enum):
    """Enumeration of possible salutations used for a customer.

    Enumeration Choices:

    * `EMPTY`: Empty.
    * `MR`: Mr.
    * `MRS`: Mrs.
    """

    __schema__ = schema
    __choices__ = ("EMPTY", "MR", "MRS")


class ScheduleName(sgqlc.types.Enum):
    """Enumeration Choices:

    * `RunChargeStationMailing`None
    * `RunTicketMigration`None
    """

    __schema__ = schema
    __choices__ = ("RunChargeStationMailing", "RunTicketMigration")


class SortDirection(sgqlc.types.Enum):
    """Sorting direction for queries.

    Enumeration Choices:

    * `asc`: Sort in ascending order.
    * `desc`: Sort in descending order.
    """

    __schema__ = schema
    __choices__ = ("asc", "desc")


String = sgqlc.types.String


class TariffDimensionType(sgqlc.types.Enum):
    """Enumeration Choices:

    * `ENERGY`None
    * `FLAT`None
    * `PARKING_TIME`None
    * `TIME`None
    """

    __schema__ = schema
    __choices__ = ("ENERGY", "FLAT", "PARKING_TIME", "TIME")


class TariffType(sgqlc.types.Enum):
    """Enumeration Choices:

    * `AD_HOC_PAYMENT`None
    * `PROFILE_CHEAP`None
    * `PROFILE_FAST`None
    * `PROFILE_GREEN`None
    * `REGULAR`None
    """

    __schema__ = schema
    __choices__ = (
        "AD_HOC_PAYMENT",
        "PROFILE_CHEAP",
        "PROFILE_FAST",
        "PROFILE_GREEN",
        "REGULAR",
    )


class TicketSource(sgqlc.types.Enum):
    """Represents the origin/source of a support ticket

    Enumeration Choices:

    * `AutoGenerated`: Automatically generated by the system
    * `ContactForm`: Ticket submitted via web contact form
    * `Email`: Ticket submitted via email
    * `Mail`: Ticket submitted via physical mail
    * `Other`: Any other unspecified source
    * `Telephone`: Ticket submitted via telephone call
    """

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
    """Represents the current status of a support ticket within the
    system

    Enumeration Choices:

    * `Close`: Ticket has been resolved and closed
    * `Generated`: Ticket has been created but no action has been
      taken
    * `Open`: Ticket is actively being processed or awaiting action
    """

    __schema__ = schema
    __choices__ = ("Close", "Generated", "Open")


class TicketType(sgqlc.types.Enum):
    """Represents the category or nature of a support ticket

    Enumeration Choices:

    * `Alteration`: Request for change or modification
    * `Complaint`: Complaint or formal issue raised
    * `Inquiry`: General inquiry or question
    * `Issue`: Technical or operational problem
    * `Note`: Internal note or informational ticket
    """

    __schema__ = schema
    __choices__ = ("Alteration", "Complaint", "Inquiry", "Issue", "Note")


class TransactionBillingType(sgqlc.types.Enum):
    """Billing type for the transaction

    Enumeration Choices:

    * `Regular`: Regular invoicing
    * `Reimbursement`: Reimbursement scenario
    * `ReimbursementPayout`: Reimbursement payout scenario
    * `Selfbill`: Self-billed transaction
    """

    __schema__ = schema
    __choices__ = ("Regular", "Reimbursement", "ReimbursementPayout", "Selfbill")


class TransactionConnectorFormat(sgqlc.types.Enum):
    """Physical format of the connector

    Enumeration Choices:

    * `Cable`: Pre-attached cable
    * `Socket`: Socket outlet
    """

    __schema__ = schema
    __choices__ = ("Cable", "Socket")


class TransactionConnectorType(sgqlc.types.Enum):
    """Type of connector used during the transaction

    Enumeration Choices:

    * `Chademo`: Chademo
    * `DomesticA`: Domestic A
    * `DomesticB`: Domestic B
    * `DomesticC`: Domestic C
    * `DomesticD`: Domestic D
    * `DomesticE`: Domestic E
    * `DomesticF`: Domestic F
    * `DomesticG`: Domestic G
    * `DomesticH`: Domestic H
    * `DomesticI`: Domestic I
    * `DomesticJ`: Domestic J
    * `DomesticK`: Domestic K
    * `DomesticL`: Domestic L
    * `Iec603092Single16`: IEC 60309 2-single-16
    * `Iec603092Three16`: IEC 60309 2-three-16
    * `Iec603092Three32`: IEC 60309 2-three-32
    * `Iec603092Three64`: IEC 60309 2-three-64
    * `Iec62196T1`: IEC 62196 T1
    * `Iec62196T1Combo`: IEC 62196 T1 Combo
    * `Iec62196T2`: IEC 62196 T2
    * `Iec62196T2Combo`: IEC 62196 T2 Combo
    * `Iec62196T3A`: IEC 62196 T3 A
    * `Iec62196T3C`: IEC 62196 T3 C
    * `TeslaR`: Tesla R
    * `TeslaS`: Tesla S
    """

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
    """Electrical current type for the transaction

    Enumeration Choices:

    * `AC`: Alternating current (AC)
    * `DC`: Direct current (DC)
    """

    __schema__ = schema
    __choices__ = ("AC", "DC")


class TransactionGlobalStatus(sgqlc.types.Enum):
    """Overall global status for the transaction across systems

    Enumeration Choices:

    * `GlobalStatusActive`: Transaction is active or ongoing
    * `GlobalStatusBillable`: Transaction is billable globally
    * `GlobalStatusBilled`: Transaction has been globally billed
    * `GlobalStatusBillingDelegated`: Billing responsibility globally
      delegated
    * `GlobalStatusCompleted`: Transaction is completed from
      operational perspective
    * `GlobalStatusInvalid`: Transaction is invalid or cannot be
      processed
    * `GlobalStatusPending`: Transaction pending further processing
    """

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
    """Method used to authorise or initiate a transaction

    Enumeration Choices:

    * `Remote`: Transaction initiated remotely via system or app
    * `Whitelist`: Transaction initiated via pre-approved whitelist
      card or ID
    """

    __schema__ = schema
    __choices__ = ("Remote", "Whitelist")


class TransactionPaymentMethod(sgqlc.types.Enum):
    """Payment method used to settle the transaction

    Enumeration Choices:

    * `Direct`: Direct
    * `Invoice`: Invoice
    * `Wallet`: Wallet
    """

    __schema__ = schema
    __choices__ = ("Direct", "Invoice", "Wallet")


class TransactionPeriodItemSource(sgqlc.types.Enum):
    """Source of charges or fees applied to a transaction period item

    Enumeration Choices:

    * `Costs`: Direct costs incurred
    * `Margin`: Profit margin
    * `PaymentTerminalProcessingFees`: Payment terminal processing
      fees
    * `Surcharge`: Any additional surcharge applied
    * `Tariff`: Base tariff
    """

    __schema__ = schema
    __choices__ = (
        "Costs",
        "Margin",
        "PaymentTerminalProcessingFees",
        "Surcharge",
        "Tariff",
    )


class TransactionPeriodItemType(sgqlc.types.Enum):
    """Type of item in a transaction period, indicating revenue or cost
    source

    Enumeration Choices:

    * `CpoAdditionalProvider`: Revenue from additional provider via
      CPO
    * `CpoAppManager`: Revenue from CPO app management fees
    * `CpoCustomer`: Revenue from CPO's own customers
    * `CpoProvider`: Revenue from CPO's contracted providers
    * `CpoRoaming`: Revenue from CPO roaming services
    * `MspAdditionalProvider`: Revenue from additional provider via
      MSP
    * `MspAppManager`: Revenue from MSP app management fees
    * `MspAppManagerToProvider`: Revenue from MSP app manager routed
      to provider
    * `MspCpo`: Revenue from CPO billed by MSP
    * `MspCustomer`: Revenue from MSP's own customers
    * `MspProvider`: Revenue from MSP's contracted providers
    * `MspRoaming`: Revenue from MSP roaming services
    """

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
    """Gender of user for period-based analytics

    Enumeration Choices:

    * `Female`: Female user
    * `Male`: Male user
    """

    __schema__ = schema
    __choices__ = ("Female", "Male")


class TransactionProfileType(sgqlc.types.Enum):
    """Profile type of the transaction for analytics or categorisation

    Enumeration Choices:

    * `Cheap`: Cost-optimized/cheap charging profile
    * `Fast`: Fast charging profile
    * `Green`: Green or eco-friendly charging profile
    * `Regular`: Standard/regular charging profile
    """

    __schema__ = schema
    __choices__ = ("Cheap", "Fast", "Green", "Regular")


class TransactionStatus(sgqlc.types.Enum):
    """Status of a transaction related to billing

    Enumeration Choices:

    * `Billable`: Transaction is billable and awaiting invoicing
    * `Billed`: Transaction has been fully billed
    * `BillingDelegated`: Billing responsibility delegated to another
      party
    """

    __schema__ = schema
    __choices__ = ("Billable", "Billed", "BillingDelegated")


class TransactionType(sgqlc.types.Enum):
    """Category or type of transaction based on origin or system role

    Enumeration Choices:

    * `CPOUnknown`: Transaction with unknown CPO (Charge Point
      Operator)
    * `Direct`: Direct transaction not routed through roaming
    * `ExternalRoamingCPO`: Roaming transaction initiated by external
      Charge Point Operator
    * `ExternalRoamingMSP`: Roaming transaction initiated by external
      Mobility Service Provider
    * `InternalRoaming`: Roaming transaction within internal network
    * `InternalRoamingDiffRoamingProfiles`: Roaming transaction across
      different internal roaming profiles
    * `Local`: Local transaction within a single operator or network
    * `MSPUnknown`: Transaction with unknown MSP (Mobility Service
      Provider)
    """

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
    """VAT classification for the transaction

    Enumeration Choices:

    * `ChargingCountry`: VAT based on charging location country
    * `Default`: Standard VAT applied
    * `NoVat`: No VAT applied
    * `OutsideVat`: Outside VAT jurisdiction
    * `ReverseCharge`: Reverse charge VAT
    """

    __schema__ = schema
    __choices__ = ("ChargingCountry", "Default", "NoVat", "OutsideVat", "ReverseCharge")


class WhitelistType(sgqlc.types.Enum):
    """Defines how this card is validated by external roaming hubs.

    Enumeration Choices:

    * `RealtimeWhitelistIfOffline`: The card requires real-time
      validation, but can fall back to whitelist when offline.
    * `Whitelist`: The card is always validated via a static
      whitelist.
    * `WhitelistOrRealtime`: The card may be validated either by
      whitelist or real-time lookup.
    """

    __schema__ = schema
    __choices__ = ("RealtimeWhitelistIfOffline", "Whitelist", "WhitelistOrRealtime")


########################################################################
# Input Objects
########################################################################
class AccessOptionInput(sgqlc.types.Input):
    """Input object for updating access options of a charge station."""

    __schema__ = schema
    __field_names__ = ("charge_card", "authorization_mode")
    charge_card = sgqlc.types.Field(String, graphql_name="chargeCard")
    """Charge card identifier to associate with this access option."""

    authorization_mode = sgqlc.types.Field(
        AuthorizationMode, graphql_name="authorizationMode"
    )
    """Authorization mode (e.g. SwipeAndCharge, AutoCharge)."""


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
    """Input object for updating customer bank account. If id is
    provided, that bank account will be deleted; otherwise, a new bank
    account will be added.
    """

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
    """Bank account ID to be deleted"""

    scheme = sgqlc.types.Field(
        sgqlc.types.non_null(BankAccountScheme), graphql_name="scheme"
    )
    """Bank account scheme (e.g., IBAN, SORT)"""

    holder_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="holderName"
    )
    """Name of the account holder"""

    iban = sgqlc.types.Field(String, graphql_name="iban")
    """International Bank Account Number"""

    bic = sgqlc.types.Field(String, graphql_name="bic")
    """Bank Identifier Code"""

    account_number = sgqlc.types.Field(String, graphql_name="account_number")
    """Account number for the bank account"""

    sort_code = sgqlc.types.Field(String, graphql_name="sort_code")
    """Sort code for the bank account"""


class BulkUpdateCpmsIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("cpms_id", "email")
    cpms_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="cpmsId")

    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="email")


class CardActionTypeSort(sgqlc.types.Input):
    """Sorting options for action type fields."""

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort by action type name."""


class CardCardProviderSort(sgqlc.types.Input):
    """Sorting options for card provider fields."""

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort by provider name."""


class CardCustomerFilter(sgqlc.types.Input):
    """Filters for querying cards based on their customer association."""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Filter by customer ID."""


class CardFilter(sgqlc.types.Input):
    """Filters for searching and narrowing down a list of cards."""

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
    """Page number for pagination (1-based)."""

    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    """Number of items per page for pagination."""

    search = sgqlc.types.Field(String, graphql_name="search")
    """Free-text search across supported card fields (ID, reference,
    etc.).
    """

    internal_id = sgqlc.types.Field(String, graphql_name="internalId")
    """Filter by internal card ID."""

    external_id = sgqlc.types.Field(String, graphql_name="externalId")
    """Filter by external card ID."""

    contract_id = sgqlc.types.Field(String, graphql_name="contractId")
    """Filter by contract ID."""

    info = sgqlc.types.Field(String, graphql_name="info")
    """Filter by info/description field."""

    usergroup = sgqlc.types.Field("CardUserGroupFilter", graphql_name="usergroup")
    """Filter by user group association."""

    is_global = sgqlc.types.Field(Boolean, graphql_name="isGlobal")
    """Filter by global card flag."""

    attached = sgqlc.types.Field(Boolean, graphql_name="attached")
    """Filter by whether the card is currently attached/active in the
    system.
    """

    wallet = sgqlc.types.Field(Boolean, graphql_name="wallet")
    """Filter by wallet availability flag."""

    customer = sgqlc.types.Field(CardCustomerFilter, graphql_name="customer")
    """Filter by linked customer."""

    transaction_customer = sgqlc.types.Field(
        "CardTransactionCustomerFilter", graphql_name="transactionCustomer"
    )
    """Filter by linked transaction customer."""

    product_customer = sgqlc.types.Field(
        "CardProductCustomerFilter", graphql_name="productCustomer"
    )
    """Filter by linked product customer."""

    date_from = sgqlc.types.Field(String, graphql_name="dateFrom")
    """Filter cards created/updated after this date (ISO 8601)."""

    date_to = sgqlc.types.Field(String, graphql_name="dateTo")
    """Filter cards created/updated before this date (ISO 8601)."""


class CardProductCustomerFilter(sgqlc.types.Input):
    """Filters for querying cards based on their product customer."""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Filter by product customer ID."""


class CardSort(sgqlc.types.Input):
    """Sorting options for card queries across multiple fields."""

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
    """Sort by card ID."""

    creation_date = sgqlc.types.Field(SortDirection, graphql_name="creationDate")
    """Sort by creation date."""

    internal_id = sgqlc.types.Field(SortDirection, graphql_name="internalId")
    """Sort by internal ID."""

    external_id = sgqlc.types.Field(SortDirection, graphql_name="externalId")
    """Sort by external ID."""

    contract_id = sgqlc.types.Field(SortDirection, graphql_name="contractId")
    """Sort by contract ID."""

    info = sgqlc.types.Field(SortDirection, graphql_name="info")
    """Sort by info/description field."""

    usergroup = sgqlc.types.Field("CardUserGroupSort", graphql_name="usergroup")
    """Sort by user group fields."""

    is_global = sgqlc.types.Field(SortDirection, graphql_name="isGlobal")
    """Sort by global flag."""

    card_provider = sgqlc.types.Field(CardCardProviderSort, graphql_name="cardProvider")
    """Sort by card provider fields."""

    action_type = sgqlc.types.Field(CardActionTypeSort, graphql_name="actionType")
    """Sort by action type fields."""

    state = sgqlc.types.Field(SortDirection, graphql_name="state")
    """Sort by lifecycle state."""

    roaming = sgqlc.types.Field(SortDirection, graphql_name="roaming")
    """Sort by roaming flag."""


class CardTransactionCustomerFilter(sgqlc.types.Input):
    """Filters for querying cards based on their transaction customer."""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Filter by transaction customer ID."""


class CardUserGroupFilter(sgqlc.types.Input):
    """Filters for querying cards based on their linked user groups."""

    __schema__ = schema
    __field_names__ = ("ids", "name", "provider")
    ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="ids")
    """Filter by one or more user group IDs."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Filter by the user group name."""

    provider = sgqlc.types.Field("CardUserGroupProviderFilter", graphql_name="provider")
    """Filter by user group provider."""


class CardUserGroupProviderFilter(sgqlc.types.Input):
    """Filters for querying cards based on the provider of their user
    group.
    """

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")
    """Filter by the provider's name."""


class CardUserGroupProviderSort(sgqlc.types.Input):
    """Sorting options for user group provider fields."""

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort by provider name."""


class CardUserGroupSort(sgqlc.types.Input):
    """Sorting options for card queries by user group fields."""

    __schema__ = schema
    __field_names__ = ("name", "provider")
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort by user group name."""

    provider = sgqlc.types.Field(CardUserGroupProviderSort, graphql_name="provider")
    """Sort by user group provider name."""


class ChargeGroupFilter(sgqlc.types.Input):
    """Filter criteria for retrieving charge groups.   Combines
    pagination, attribute-based filtering, and nested filters on
    related entities such as user groups and tariffs.
    """

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
    """The page number of results to retrieve (used for pagination)."""

    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    """The number of items per page (used for pagination)."""

    id = sgqlc.types.Field(ID, graphql_name="id")
    """Filter charge groups by a specific unique identifier."""

    usergroup = sgqlc.types.Field(
        "ChargeGroupUserGroupFilter", graphql_name="usergroup"
    )
    """Filter charge groups by associated user group properties (IDs,
    names).
    """

    name = sgqlc.types.Field(String, graphql_name="name")
    """Filter charge groups by their display name."""

    info = sgqlc.types.Field(String, graphql_name="info")
    """Filter charge groups by their informational text or description."""

    tariff = sgqlc.types.Field("ChargeGroupTariffFilter", graphql_name="tariff")
    """Filter charge groups by tariff-related properties (IDs, names)."""

    type = sgqlc.types.Field(ChargeGroupType, graphql_name="type")
    """Restrict charge groups to a specific type (e.g., Home or Other)."""


class ChargeGroupSort(sgqlc.types.Input):
    """Sorting options for charge groups.   Defines how results are
    ordered when retrieving collections of charge groups.
    """

    __schema__ = schema
    __field_names__ = ("id", "name", "info", "type", "usergroup", "tariff")
    id = sgqlc.types.Field(SortDirection, graphql_name="id")
    """Sort charge groups by their unique identifier."""

    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort charge groups by their display name."""

    info = sgqlc.types.Field(SortDirection, graphql_name="info")
    """Sort charge groups by their informational description."""

    type = sgqlc.types.Field(SortDirection, graphql_name="type")
    """Sort charge groups by type (Home vs Other)."""

    usergroup = sgqlc.types.Field("ChargeGroupUserGroupSort", graphql_name="usergroup")
    """Sort by attributes of the associated user group."""

    tariff = sgqlc.types.Field("ChargeGroupTariffSort", graphql_name="tariff")
    """Sort by attributes of the associated tariff."""


class ChargeGroupTariffFilter(sgqlc.types.Input):
    """Filter criteria for narrowing down charge groups based on their
    assigned tariffs. A tariff defines the pricing or billing rules
    applied when using the group.
    """

    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="id")
    """One or more unique identifiers of tariffs to match charge groups
    against.
    """

    name = sgqlc.types.Field(String, graphql_name="name")
    """Filter charge groups by the tariff’s display name."""


class ChargeGroupTariffSort(sgqlc.types.Input):
    """Sorting options for charge groups’ associated tariffs.
    Determines the order in which results are returned based on tariff
    attributes.
    """

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort tariffs by their name (ascending or descending)."""


class ChargeGroupUserGroupFilter(sgqlc.types.Input):
    """Filter criteria for narrowing down charge groups based on their
    associated user groups. User groups represent sets of users with
    shared access rights or billing relationships.
    """

    __schema__ = schema
    __field_names__ = ("ids", "name")
    ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="ids")
    """One or more unique identifiers of user groups to match charge
    groups against.
    """

    name = sgqlc.types.Field(String, graphql_name="name")
    """Filter charge groups by the exact name of the associated user
    group.
    """


class ChargeGroupUserGroupSort(sgqlc.types.Input):
    """Sorting options for charge groups’ associated user groups.
    Determines the order in which results are returned based on user
    group attributes.
    """

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort user groups by their name (ascending or descending)."""


class ChargeStationChargeFilter(sgqlc.types.Input):
    """Filter criteria for charges associated with a charge station."""

    __schema__ = schema
    __field_names__ = ("transactions",)
    transactions = sgqlc.types.Field(
        "ChargeStationTransactionFilter", graphql_name="transactions"
    )
    """Transaction-based filtering."""


class ChargeStationChargeGroupFilter(sgqlc.types.Input):
    """Filter criteria for charge groups associated with charge stations.
    A charge group is a logical grouping of stations under shared
    rules and tariffs.
    """

    __schema__ = schema
    __field_names__ = ("id", "name", "tariff")
    id = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name="id")
    """One or more group IDs to match."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Group name to match."""

    tariff = sgqlc.types.Field("ChargeStationTariffFilter", graphql_name="tariff")
    """Tariff applied to the charge group."""


class ChargeStationChargeGroupSort(sgqlc.types.Input):
    """Sorting options for charge station groups."""

    __schema__ = schema
    __field_names__ = ("name", "tariff")
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort by group name."""

    tariff = sgqlc.types.Field("ChargeStationTariffSort", graphql_name="tariff")
    """Sort by tariff attributes."""


class ChargeStationCountryFilter(sgqlc.types.Input):
    """Filter for matching a country by ISO code (e.g., DE, NL, US)."""

    __schema__ = schema
    __field_names__ = ("code",)
    code = sgqlc.types.Field(String, graphql_name="code")
    """ISO country code of the station."""


class ChargeStationFilter(sgqlc.types.Input):
    """High-level filtering criteria for retrieving charge stations.
    Combines IDs, states, location, ownership, communication, and
    grouping.
    """

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
    """Page number of results to fetch (pagination)."""

    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    """Items per page (pagination)."""

    id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="id")
    """Filter by one or more unique station IDs."""

    search = sgqlc.types.Field(String, graphql_name="search")
    """Free-text search across name, reference, or metadata."""

    state = sgqlc.types.Field(ChargeStationState, graphql_name="state")
    """Operational state of the station (active/inactive/blocked)."""

    subscription = sgqlc.types.Field(
        ChargeStationSubscriptionState, graphql_name="subscription"
    )
    """Subscription status of the station."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Name of the station."""

    physical_number = sgqlc.types.Field(String, graphql_name="physicalNumber")
    """Physical hardware number assigned to the station."""

    location = sgqlc.types.Field("ChargeStationLocationFilter", graphql_name="location")
    """Location attributes to filter by address, city, or country."""

    phone = sgqlc.types.Field(String, graphql_name="phone")
    """Contact phone number registered with the station."""

    comm_id = sgqlc.types.Field(String, graphql_name="commId")
    """Communication ID used for backend integration."""

    software = sgqlc.types.Field(String, graphql_name="software")
    """Software version running on the station."""

    charge_group = sgqlc.types.Field(
        ChargeStationChargeGroupFilter, graphql_name="chargeGroup"
    )
    """Associated charge group of the station."""

    sim = sgqlc.types.Field("ChargeStationSimFilter", graphql_name="sim")
    """SIM details associated with the station."""

    usergroup = sgqlc.types.Field(
        "ChargeStationUsergroupFilter", graphql_name="usergroup"
    )
    """User group linked to the station."""

    parameter_set = sgqlc.types.Field(
        "ChargeStationParameterSetFilter", graphql_name="parameterSet"
    )
    """Parameter set applied to the station."""

    manufacturer_type = sgqlc.types.Field(
        "ChargeStationManufacturerTypeFilter", graphql_name="manufacturerType"
    )
    """Manufacturer and model of the station hardware."""

    owner = sgqlc.types.Field("ChargeStationOwnerFilter", graphql_name="owner")
    """Owner details of the station."""

    channel_physical_ids = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="channelPhysicalIds"
    )
    """Physical IDs of individual station channels."""

    payer = sgqlc.types.Field("ChargeStationPayerFilter", graphql_name="payer")
    """Payer information linked to station billing."""

    recipient = sgqlc.types.Field(
        "ChargeStationRecipientFilter", graphql_name="recipient"
    )
    """Recipient of financial settlements."""

    reference = sgqlc.types.Field(String, graphql_name="reference")
    """External reference identifier."""


class ChargeStationLocationFilter(sgqlc.types.Input):
    """Filter criteria for locating charge stations by physical address
    or country.
    """

    __schema__ = schema
    __field_names__ = ("id", "address", "city", "country")
    id = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name="id")
    """One or more unique location IDs."""

    address = sgqlc.types.Field(String, graphql_name="address")
    """Street address of the station location."""

    city = sgqlc.types.Field(String, graphql_name="city")
    """City where the station is located."""

    country = sgqlc.types.Field(ChargeStationCountryFilter, graphql_name="country")
    """Country of the station (by code)."""


class ChargeStationLocationSort(sgqlc.types.Input):
    """Sorting options for charge station locations. Controls result
    ordering by address or city.
    """

    __schema__ = schema
    __field_names__ = ("address", "city")
    address = sgqlc.types.Field(SortDirection, graphql_name="address")
    """Sort by street address."""

    city = sgqlc.types.Field(SortDirection, graphql_name="city")
    """Sort by city name."""


class ChargeStationManufacturerTypeFilter(sgqlc.types.Input):
    """Filter criteria for manufacturer details of a charge station.
    Useful for asset management and hardware-specific queries.
    """

    __schema__ = schema
    __field_names__ = ("vendor", "model")
    vendor = sgqlc.types.Field(String, graphql_name="vendor")
    """Hardware vendor/manufacturer of the station."""

    model = sgqlc.types.Field(String, graphql_name="model")
    """Specific model identifier of the station."""


class ChargeStationOwnerFilter(sgqlc.types.Input):
    """Filter criteria for identifying charge station owners. Owners can
    be individuals or organizations responsible for the asset.
    """

    __schema__ = schema
    __field_names__ = ("id", "first_name", "last_name", "company_name")
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Unique ID of the owner."""

    first_name = sgqlc.types.Field(String, graphql_name="firstName")
    """First name (if owner is an individual)."""

    last_name = sgqlc.types.Field(String, graphql_name="lastName")
    """Last name (if owner is an individual)."""

    company_name = sgqlc.types.Field(String, graphql_name="companyName")
    """Company name (if owner is an organization)."""


class ChargeStationParameterSetFilter(sgqlc.types.Input):
    """Filter criteria for charge station parameter sets. Allows querying
    stations configured with specific parameter bundles.
    """

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")
    """Name of the parameter set."""


class ChargeStationParameterSetSort(sgqlc.types.Input):
    """Sorting options for charge station parameter sets."""

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort by parameter set name."""


class ChargeStationPayerFilter(sgqlc.types.Input):
    """Filter criteria for station payers (the party responsible for
    payments). May link to subscriptions or payment contracts.
    """

    __schema__ = schema
    __field_names__ = ("subscription",)
    subscription = sgqlc.types.Field(
        "ChargeStationSubscriptionFilter", graphql_name="subscription"
    )
    """Subscription contract under which the station is billed."""


class ChargeStationProviderFilter(sgqlc.types.Input):
    """Filter criteria for station provider information. Providers
    operate charge stations under their brand or platform.
    """

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")
    """Name of the provider company."""


class ChargeStationRecipientFilter(sgqlc.types.Input):
    """Filter criteria for charge station recipients (beneficiaries of
    payments). Allows targeting specific financial settlement flows.
    """

    __schema__ = schema
    __field_names__ = ("charge",)
    charge = sgqlc.types.Field(ChargeStationChargeFilter, graphql_name="charge")
    """Charge relationship of the recipient."""


class ChargeStationSimFilter(sgqlc.types.Input):
    """Filter criteria for SIM cards associated with charge stations.
    Useful for backend diagnostics and device connectivity management.
    """

    __schema__ = schema
    __field_names__ = ("sim_number", "iccid")
    sim_number = sgqlc.types.Field(String, graphql_name="simNumber")
    """SIM phone number assigned to the station."""

    iccid = sgqlc.types.Field(String, graphql_name="iccid")
    """ICCID (integrated circuit card identifier) of the SIM."""


class ChargeStationSort(sgqlc.types.Input):
    """Sorting options for charge stations. Allows ordering by ID, name,
    physical attributes, and associations.
    """

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
    """Sort by station ID."""

    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort by station name."""

    physical_number = sgqlc.types.Field(SortDirection, graphql_name="physicalNumber")
    """Sort by physical number."""

    location = sgqlc.types.Field(ChargeStationLocationSort, graphql_name="location")
    """Sort by location attributes."""

    parameter_set = sgqlc.types.Field(
        ChargeStationParameterSetSort, graphql_name="parameterSet"
    )
    """Sort by applied parameter set."""

    charge_group = sgqlc.types.Field(
        ChargeStationChargeGroupSort, graphql_name="chargeGroup"
    )
    """Sort by associated charge group."""

    usergroup = sgqlc.types.Field(
        "ChargeStationUsergroupSort", graphql_name="usergroup"
    )
    """Sort by associated user group."""

    last_communication_date = sgqlc.types.Field(
        SortDirection, graphql_name="lastCommunicationDate"
    )
    """Sort by timestamp of last communication."""

    status = sgqlc.types.Field(SortDirection, graphql_name="status")
    """Sort by station operational status."""


class ChargeStationSubscriptionFilter(sgqlc.types.Input):
    """Filter criteria for charge station subscriptions. Subscriptions
    represent contractual access to charging services.
    """

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Unique identifier of the subscription."""


class ChargeStationTariffFilter(sgqlc.types.Input):
    """Filter criteria for tariffs assigned to a charge station or group.
    Tariffs define pricing structures for charging sessions.
    """

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")
    """Human-readable name of the tariff."""


class ChargeStationTariffSort(sgqlc.types.Input):
    """Sorting options for tariffs assigned to charge stations."""

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort by tariff name."""


class ChargeStationTransactionFilter(sgqlc.types.Input):
    """Filter criteria for transactions linked to a charge station."""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Unique ID of the transaction."""


class ChargeStationUsergroupFilter(sgqlc.types.Input):
    """Filter criteria for user groups associated with charge stations.
    User groups manage access rights and pricing models for sets of
    users.
    """

    __schema__ = schema
    __field_names__ = ("ids", "name", "provider")
    ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="ids")
    """One or more user group IDs."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """User group name."""

    provider = sgqlc.types.Field(
        "ChargeStationUsergroupProviderFilter", graphql_name="provider"
    )
    """Provider managing the user group."""


class ChargeStationUsergroupProviderFilter(sgqlc.types.Input):
    """Filter criteria for user group providers. Associates charge
    stations with user groups managed by external providers.
    """

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")
    """Name of the user group provider."""


class ChargeStationUsergroupSort(sgqlc.types.Input):
    """Sorting options for user groups assigned to charge stations."""

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort by user group name."""


class CodeInput(sgqlc.types.Input):
    """Wrapper input for referencing an object by a code (e.g. ISO code,
    system code).
    """

    __schema__ = schema
    __field_names__ = ("code",)
    code = sgqlc.types.Field(String, graphql_name="code")
    """Code of the object (system or ISO format)."""


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
    """ "Input object for creating a customer BACS mandate."""

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
    """The period and fee for the mandate. Example: 1 year, 23% fee
    (calendar year 2026)
    """


class CreateScheduleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("name", "payload")
    name = sgqlc.types.Field(ScheduleName, graphql_name="name")

    payload = sgqlc.types.Field("SchedulePayloadInput", graphql_name="payload")


class CreateUpdateCustomerMandateInput(sgqlc.types.Input):
    """Input object for creating or updating a customer mandate."""

    __schema__ = schema
    __field_names__ = (
        "accepted",
        "billing_account_number",
        "bic",
        "billing_account_name",
    )
    accepted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="accepted")
    """Whether the mandate is accepted"""

    billing_account_number = sgqlc.types.Field(
        String, graphql_name="billingAccountNumber"
    )
    """Bank account number"""

    bic = sgqlc.types.Field(String, graphql_name="bic")
    """BIC code"""

    billing_account_name = sgqlc.types.Field(String, graphql_name="billingAccountName")
    """Name on the billing account"""


class CurrencyFilter(sgqlc.types.Input):
    """Filter input for selecting currencies."""

    __schema__ = schema
    __field_names__ = ("supported",)
    supported = sgqlc.types.Field(Boolean, graphql_name="supported")
    """Whether this currency is supported for payments."""


class CustomerBankFilter(sgqlc.types.Input):
    """Filter input for selecting customers by bank"""

    __schema__ = schema
    __field_names__ = ("account",)
    account = sgqlc.types.Field(String, graphql_name="account")
    """Account of the bank to filter customers"""


class CustomerCompanyFilter(sgqlc.types.Input):
    """Filter input for selecting customers by company"""

    __schema__ = schema
    __field_names__ = ("name", "id")
    name = sgqlc.types.Field(String, graphql_name="name")
    """Name of the company to filter customers"""

    id = sgqlc.types.Field(ID, graphql_name="id")
    """ID of the company to filter customers"""


class CustomerCountryFilter(sgqlc.types.Input):
    """Filter input for selecting customers by country"""

    __schema__ = schema
    __field_names__ = ("code",)
    code = sgqlc.types.Field(String, graphql_name="code")
    """Code of the country to filter customers"""


class CustomerFilter(sgqlc.types.Input):
    """Filter input for selecting customers"""

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
    """Page number for pagination"""

    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    """Number of items per page for pagination"""

    id = sgqlc.types.Field(ID, graphql_name="id")
    """ID of the customer to filter customers"""

    search = sgqlc.types.Field(String, graphql_name="search")
    """Search for customers"""

    type = sgqlc.types.Field(CustomerFilterType, graphql_name="type")
    """Type of customer to filter customers"""

    state = sgqlc.types.Field(CustomerFilterState, graphql_name="state")
    """State of customer to filter customers"""

    object_id = sgqlc.types.Field(String, graphql_name="objectId")
    """Object ID of the customer to filter customers"""

    usergroup = sgqlc.types.Field("CustomerUserGroupFilter", graphql_name="usergroup")
    """User group of the customer to filter customers"""

    provider = sgqlc.types.Field("CustomerProviderFilter", graphql_name="provider")
    """Provider of the customer to filter customers"""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Name of the customer to filter customers"""

    city = sgqlc.types.Field(String, graphql_name="city")
    """City of the customer to filter customers"""

    country = sgqlc.types.Field(CustomerCountryFilter, graphql_name="country")
    """Country of the customer to filter customers"""

    street = sgqlc.types.Field(String, graphql_name="street")
    """Street of the customer to filter customers"""

    street_number = sgqlc.types.Field(String, graphql_name="streetNumber")
    """Street number of the customer to filter customers"""

    street_number_ext = sgqlc.types.Field(String, graphql_name="streetNumberExt")
    """Street number extension of the customer to filter customers"""

    zip_code = sgqlc.types.Field(String, graphql_name="zipCode")
    """Zip code of the customer to filter customers"""

    phone = sgqlc.types.Field(String, graphql_name="phone")
    """Phone of the customer to filter customers"""

    mobile = sgqlc.types.Field(String, graphql_name="mobile")
    """Mobile of the customer to filter customers"""

    company = sgqlc.types.Field(CustomerCompanyFilter, graphql_name="company")
    """Company of the customer to filter customers"""

    email = sgqlc.types.Field(String, graphql_name="email")
    """Email of the customer to filter customers"""

    bank = sgqlc.types.Field(CustomerBankFilter, graphql_name="bank")
    """Bank of the customer to filter customers"""


class CustomerProviderFilter(sgqlc.types.Input):
    """Filter input for selecting customers by provider"""

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")
    """Name of the provider to filter customers"""


class CustomerSort(sgqlc.types.Input):
    """Sort input for selecting customers"""

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
    """Sort direction by customer ID"""

    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort direction by customer name"""

    city = sgqlc.types.Field(SortDirection, graphql_name="city")
    """Sort direction by customer city"""

    phone = sgqlc.types.Field(SortDirection, graphql_name="phone")
    """Sort direction by customer phone"""

    usergroup = sgqlc.types.Field("CustomerUserGroupSort", graphql_name="usergroup")
    """Sort direction by customer user group"""

    type = sgqlc.types.Field(SortDirection, graphql_name="type")
    """Sort direction by customer type"""

    creation_date = sgqlc.types.Field(SortDirection, graphql_name="creationDate")
    """Sort direction by customer creation date"""


class CustomerUserGroupFilter(sgqlc.types.Input):
    """Filter input for selecting customers by user group"""

    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(ID, graphql_name="id")
    """ID of the user group to filter customers"""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Name of the user group to filter customers"""


class CustomerUserGroupSort(sgqlc.types.Input):
    """Sort input for selecting customers by user group"""

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort direction by user group name"""


class EndCustomerBacsMandateInput(sgqlc.types.Input):
    """ "Input object for ending a customer BACS mandate."""

    __schema__ = schema
    __field_names__ = ("mandate_reference", "end_date")
    mandate_reference = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="mandateReference"
    )

    end_date = sgqlc.types.Field(String, graphql_name="endDate")


class EndCustomerMandateInput(sgqlc.types.Input):
    """Input object for ending a customer mandate."""

    __schema__ = schema
    __field_names__ = ("id", "stop_date")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    """Mandate identifier"""

    stop_date = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="stopDate")
    """Date the mandate should end"""


class GeoPointInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("latitude", "longitude")
    latitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="latitude")

    longitude = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name="longitude")


class IdInput(sgqlc.types.Input):
    """Wrapper input for referencing an object by ID."""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Unique identifier of the object."""


class InvoiceCustomerFilter(sgqlc.types.Input):
    """Filter object to find invoices related to a specific customer."""

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
    """Customer unique identifier"""

    first_name = sgqlc.types.Field(String, graphql_name="firstName")
    """Customer first name"""

    last_name = sgqlc.types.Field(String, graphql_name="lastName")
    """Customer last name"""

    company_name = sgqlc.types.Field(String, graphql_name="companyName")
    """Customer company name"""

    object_id = sgqlc.types.Field(String, graphql_name="objectId")
    """Internal object ID"""

    billing_account_number = sgqlc.types.Field(
        String, graphql_name="billingAccountNumber"
    )
    """Billing account number"""

    billing_account_name = sgqlc.types.Field(String, graphql_name="billingAccountName")
    """Billing account holder name"""


class InvoiceFilter(sgqlc.types.Input):
    """Filter object for querying invoices with multiple criteria."""

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
    """Invoice amount filter"""

    currency = sgqlc.types.Field(String, graphql_name="currency")
    """Currency filter"""

    status = sgqlc.types.Field(InvoiceStatus, graphql_name="status")
    """Invoice status filter"""

    type = sgqlc.types.Field(InvoiceType, graphql_name="type")
    """Invoice type filter"""

    country = sgqlc.types.Field(String, graphql_name="country")
    """Country filter"""

    date_from = sgqlc.types.Field(String, graphql_name="dateFrom")
    """Start date for invoice search"""

    date_to = sgqlc.types.Field(String, graphql_name="dateTo")
    """End date for invoice search"""

    customer = sgqlc.types.Field(InvoiceCustomerFilter, graphql_name="customer")
    """Customer filter"""

    user_group = sgqlc.types.Field("InvoiceUserGroupFilter", graphql_name="userGroup")
    """User group filter"""

    provider = sgqlc.types.Field("InvoiceProviderFilter", graphql_name="provider")
    """Provider filter"""


class InvoiceProviderFilter(sgqlc.types.Input):
    """Filter object to find invoices related to a specific provider."""

    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Provider unique identifier"""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Provider name"""


class InvoiceSort(sgqlc.types.Input):
    """Overall sorting input for invoices."""

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
    """Sort by previous invoices ID"""

    countries = sgqlc.types.Field("InvoiceSortCountries", graphql_name="countries")
    """Sort by countries"""

    vat_type = sgqlc.types.Field(SortDirection, graphql_name="vatType")
    """Sort by VAT type"""

    vat_entity = sgqlc.types.Field("InvoiceSortVatEntity", graphql_name="vatEntity")
    """Sort by VAT entity"""

    billing_type = sgqlc.types.Field(SortDirection, graphql_name="billingType")
    """Sort by billing type"""

    credit = sgqlc.types.Field(SortDirection, graphql_name="credit")
    """Sort by credit invoices"""

    invoice_date = sgqlc.types.Field(SortDirection, graphql_name="invoiceDate")
    """Sort by invoice date"""

    customer = sgqlc.types.Field("InvoiceSortCustomer", graphql_name="customer")
    """Sort by customer fields"""

    provider_profiles = sgqlc.types.Field(
        "InvoiceSortProviderProfiles", graphql_name="providerProfiles"
    )
    """Sort by provider profiles"""

    price_incl_vat = sgqlc.types.Field(SortDirection, graphql_name="priceInclVat")
    """Sort by price including VAT"""

    cust_price_incl_vat = sgqlc.types.Field(
        SortDirection, graphql_name="custPriceInclVat"
    )
    """Sort by customer price including VAT"""

    state = sgqlc.types.Field(SortDirection, graphql_name="state")
    """Sort by invoice state"""

    regenerated = sgqlc.types.Field(SortDirection, graphql_name="regenerated")
    """Sort by regenerated invoices"""


class InvoiceSortCountries(sgqlc.types.Input):
    """Sorting input for countries in invoice queries."""

    __schema__ = schema
    __field_names__ = ("localname",)
    localname = sgqlc.types.Field(SortDirection, graphql_name="localname")
    """Localized country name sort direction"""


class InvoiceSortCustomer(sgqlc.types.Input):
    """Sorting input for customer fields in invoice queries."""

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
    """Sort by first name"""

    last_name = sgqlc.types.Field(SortDirection, graphql_name="lastName")
    """Sort by last name"""

    company_name = sgqlc.types.Field(SortDirection, graphql_name="companyName")
    """Sort by company name"""

    id = sgqlc.types.Field(SortDirection, graphql_name="id")
    """Sort by customer ID"""

    type = sgqlc.types.Field(SortDirection, graphql_name="type")
    """Sort by customer type"""

    state = sgqlc.types.Field(SortDirection, graphql_name="state")
    """Sort by customer state"""

    billing_account_no = sgqlc.types.Field(
        SortDirection, graphql_name="BillingAccountNo"
    )
    """Sort by billing account number"""


class InvoiceSortProviderProfiles(sgqlc.types.Input):
    """Sorting input for provider profiles in invoice queries."""

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """Sort by provider name"""


class InvoiceSortVatEntity(sgqlc.types.Input):
    """Sorting input for VAT entities in invoice queries."""

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(SortDirection, graphql_name="name")
    """VAT entity name sort direction"""


class InvoiceUserGroupFilter(sgqlc.types.Input):
    """Filter object for querying invoices related to a specific user
    group.
    """

    __schema__ = schema
    __field_names__ = ("name",)
    name = sgqlc.types.Field(String, graphql_name="name")
    """User group name"""


class LanguageFilter(sgqlc.types.Input):
    """Filter input for selecting languages."""

    __schema__ = schema
    __field_names__ = ("supported",)
    supported = sgqlc.types.Field(Boolean, graphql_name="supported")
    """Whether the language is officially supported by the platform."""


class LiveKitTokenInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("environment", "language", "country", "source", "platform")
    environment = sgqlc.types.Field(
        sgqlc.types.non_null(LiveKitVoiceAgentEnvironment), graphql_name="environment"
    )
    """The environment of the agent"""

    language = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="language")
    """The language of the user"""

    country = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="country")
    """The country of the user"""

    source = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="source")
    """The source of the user"""

    platform = sgqlc.types.Field(
        sgqlc.types.non_null(LiveKitPlatformType), graphql_name="platform"
    )
    """The platform of the user"""


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
    """Either searchLatitude/searchLongitude should be set or
    searchString or searchId
    """

    search_longitude = sgqlc.types.Field(Float, graphql_name="searchLongitude")
    """Either searchLatitude/searchLongitude should be set or
    searchString or searchId
    """

    search_string = sgqlc.types.Field(String, graphql_name="searchString")
    """Either searchLatitude/searchLongitude should be set or
    searchString or searchId
    """

    search_location_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="searchLocationIds",
    )
    """When given, an exact search will be done on the given IDs"""

    search_device_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="searchDeviceIds",
    )

    search_channel_ids = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)),
        graphql_name="searchChannelIds",
    )
    """When given, an exact search will be done on the given IDs
    (Location with the given IDs will be returned)
    """

    search_qr_code = sgqlc.types.Field(String, graphql_name="searchQrCode")

    heading = sgqlc.types.Field(Float, graphql_name="heading")

    speed = sgqlc.types.Field(Float, graphql_name="speed")

    availability = sgqlc.types.Field(LmsAvailability, graphql_name="availability")
    """all | available"""

    connector_types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ConnectorType)),
        graphql_name="connectorTypes",
    )

    min_power = sgqlc.types.Field(Float, graphql_name="minPower")
    """in W. When given, channels with a minimum power of minPower will
    be returned
    """

    capabilities = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Capability)),
        graphql_name="capabilities",
    )
    """List of capabilities"""

    providers = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="providers"
    )
    """List of providers"""

    profiles = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="profiles"
    )
    """Chargepoint | PowerSupply"""

    return_fields = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name="returnFields"
    )
    """Fields to return. If empty all fields will be returned. Note: To
    filter channel fields start the element with channels.
    """


class MapLocationsFiltersInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("connector_types", "availability", "min_power", "capabilities")
    connector_types = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(ConnectorType)),
        graphql_name="connectorTypes",
    )

    availability = sgqlc.types.Field(LmsAvailability, graphql_name="availability")
    """all | available"""

    min_power = sgqlc.types.Field(Float, graphql_name="minPower")
    """in W. When given, channels with a minimum power of minPower will
    be returned
    """

    capabilities = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(Capability)),
        graphql_name="capabilities",
    )
    """List of capabilities"""


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
    """The block number of the schedule (0-671)"""

    charge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="charge")
    """The charge status of the schedule block"""


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
    """The weekday, 1-7 being Monday-Sunday"""

    start_time = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="startTime"
    )
    """The start time of the schedule in UTC"""

    stop_time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="stopTime")
    """The stop time of the schedule in UTC"""


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
    """Represents a simple schedule input, with either a boolean charge
    status or a start-stop time. Times take precedence over charge
    status.
    """

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
    """Filter input for selecting tickets by action taken"""

    __schema__ = schema
    __field_names__ = ("taken",)
    taken = sgqlc.types.Field(String, graphql_name="taken")
    """Description of action taken to filter tickets"""


class TicketChargeStationFilter(sgqlc.types.Input):
    """Filter input for selecting tickets by charge station"""

    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(Int, graphql_name="id")
    """ID of the charge station to filter tickets"""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Name of the charge station to filter tickets"""


class TicketCreatorFilter(sgqlc.types.Input):
    """Filter input for selecting tickets by creator"""

    __schema__ = schema
    __field_names__ = ("company",)
    company = sgqlc.types.Field(String, graphql_name="company")
    """Company of the ticket creator to filter tickets"""


class TicketCustomerFilter(sgqlc.types.Input):
    """Filter input for selecting tickets by customer"""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(Int, graphql_name="id")
    """ID of the customer to filter tickets"""


class TicketFilter(sgqlc.types.Input):
    """Comprehensive input for filtering tickets with multiple criteria"""

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
    """Page number for pagination"""

    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    """Number of items per page for pagination"""

    id = sgqlc.types.Field(Int, graphql_name="id")
    """Filter by ticket ID"""

    search = sgqlc.types.Field(String, graphql_name="search")
    """Text search filter across ticket fields"""

    status = sgqlc.types.Field(TicketStatus, graphql_name="status")
    """Filter by ticket status"""

    description = sgqlc.types.Field(String, graphql_name="description")
    """Filter by ticket description text"""

    reported_by = sgqlc.types.Field(String, graphql_name="reportedBy")
    """Filter by who reported the ticket"""

    charge_station = sgqlc.types.Field(
        TicketChargeStationFilter, graphql_name="chargeStation"
    )
    """Filter by associated charge station"""

    usergroup = sgqlc.types.Field("TicketUsergroupFilter", graphql_name="usergroup")
    """Filter by associated user group"""

    customer = sgqlc.types.Field(TicketCustomerFilter, graphql_name="customer")
    """Filter by associated customer"""

    creator = sgqlc.types.Field(TicketCreatorFilter, graphql_name="creator")
    """Filter by creator of the ticket"""

    action = sgqlc.types.Field(TicketActionFilter, graphql_name="action")
    """Filter by actions taken on the ticket"""


class TicketSort(sgqlc.types.Input):
    """Comprehensive input for sorting tickets by multiple fields"""

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
    """Sort direction by ticket ID"""

    charge_station = sgqlc.types.Field(
        "TicketSortChargeStation", graphql_name="chargeStation"
    )
    """Sort direction by charge station fields"""

    user_group = sgqlc.types.Field("TicketSortUserGroup", graphql_name="userGroup")
    """Sort direction by user group fields"""

    customer = sgqlc.types.Field("TicketSortCustomer", graphql_name="customer")
    """Sort direction by customer fields"""

    creator = sgqlc.types.Field("TicketSortCreator", graphql_name="creator")
    """Sort direction by creator fields"""

    action = sgqlc.types.Field("TicketSortAction", graphql_name="action")
    """Sort direction by action fields"""

    reported_by = sgqlc.types.Field(SortDirection, graphql_name="reportedBy")
    """Sort direction by reported by field"""


class TicketSortAction(sgqlc.types.Input):
    """Sort input for ordering tickets by action fields"""

    __schema__ = schema
    __field_names__ = ("taken",)
    taken = sgqlc.types.Field(SortDirection, graphql_name="taken")
    """Sort direction by action taken"""


class TicketSortChargeStation(sgqlc.types.Input):
    """Sort input for ordering tickets by charge station fields"""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(SortDirection, graphql_name="id")
    """Sort direction by charge station ID"""


class TicketSortCreator(sgqlc.types.Input):
    """Sort input for ordering tickets by creator fields"""

    __schema__ = schema
    __field_names__ = ("company",)
    company = sgqlc.types.Field(SortDirection, graphql_name="company")
    """Sort direction by creator company"""


class TicketSortCustomer(sgqlc.types.Input):
    """Sort input for ordering tickets by customer fields"""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(SortDirection, graphql_name="id")
    """Sort direction by customer ID"""


class TicketSortUserGroup(sgqlc.types.Input):
    """Sort input for ordering tickets by user group fields"""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(SortDirection, graphql_name="id")
    """Sort direction by user group ID"""


class TicketUsergroupFilter(sgqlc.types.Input):
    """Filter input for selecting tickets by user group"""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(Int, graphql_name="id")
    """ID of the user group to filter tickets"""


class TimeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("start_time", "stop_time")
    start_time = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="startTime"
    )
    """The start time of the schedule in UTC"""

    stop_time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="stopTime")
    """The stop time of the schedule in UTC"""


class TokenUpdate(sgqlc.types.Input):
    """Input type for updating a customer charge card (token). Some
    fields are deprecated because they are no longer supported by the
    API.
    """

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
    """Cost center identifier for internal accounting purposes."""

    expiry_date = sgqlc.types.Field(String, graphql_name="expiryDate")
    """Expiry date of the charge card, usually in YYYY-MM format."""

    info = sgqlc.types.Field(String, graphql_name="info")
    """Free-text notes or metadata linked to the charge card."""

    qr_code = sgqlc.types.Field(String, graphql_name="qrCode")
    """QR code string associated with the charge card (for scanning)."""

    reference = sgqlc.types.Field(String, graphql_name="reference")
    """Reference or identifier assigned to the charge card (for
    business/customer use).
    """

    remote_password = sgqlc.types.Field(String, graphql_name="remotePassword")
    """Remote password used for authenticating charge sessions via remote
    systems.
    """

    roaming_home_charging_enabled = sgqlc.types.Field(
        Boolean, graphql_name="roamingHomeChargingEnabled"
    )
    """Whether roaming home charging is enabled for this card. If true,
    card can be used for home charging sessions that roam onto public
    networks.
    """

    roaming = sgqlc.types.Field(Boolean, graphql_name="roaming")
    """Whether roaming in general is enabled for this card. Determines if
    the card can be used on partner networks.
    """

    state = sgqlc.types.Field(String, graphql_name="state")
    """Current state of the charge card. Examples: Active, Blocked,
    Inactive, Deactivated.
    """


class TransactionCardFilter(sgqlc.types.Input):
    """Filter by card for transaction queries"""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Card ID to filter. This API requires either a dateFrom, the
    invoice.id or, card.id and startDateFrom to be provided. If
    card.id is provided, startDateFrom is required.
    """


class TransactionChargeStationFilter(sgqlc.types.Input):
    """Filter by charge station for transaction queries"""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Charge station ID to filter"""


class TransactionCustomerFilter(sgqlc.types.Input):
    """Filter by customer for transaction queries"""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Customer ID to filter"""


class TransactionFilter(sgqlc.types.Input):
    """Comprehensive transaction filter input. This API requires either a
    dateFrom, the invoice.id or, card.id and startDateFrom to be
    provided. If card.id is provided, startDateFrom is required. Use
    dateFrom and dateTo to define the range to filter results, based
    on lastUpdatedDate. Difference between dates is not allowed to
    exceed 1 month. All pagination keys (itemsPerPage, page) MUST go
    here.
    """

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
    """The collection page number. MUST be inside filters, not root
    level.
    """

    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    """The number of transactions in the result collection. MUST be
    inside filters, not root level.
    """

    id = sgqlc.types.Field(ID, graphql_name="id")
    """Filter by transaction ID"""

    customer = sgqlc.types.Field(TransactionCustomerFilter, graphql_name="customer")
    """Customer filter"""

    charge_station = sgqlc.types.Field(
        TransactionChargeStationFilter, graphql_name="chargeStation"
    )
    """Charge station filter"""

    card = sgqlc.types.Field(TransactionCardFilter, graphql_name="card")
    """Charge card filter. This API requires either a dateFrom, the
    invoice.id or, card.id and startDateFrom to be provided. If
    card.id is provided, startDateFrom is required.
    """

    invoice = sgqlc.types.Field("TransactionInvoiceFilter", graphql_name="invoice")
    """Invoice filter. This API requires either a dateFrom, the
    invoice.id or, card.id and startDateFrom to be provided. If
    card.id is provided, startDateFrom is required.
    """

    provider = sgqlc.types.Field("TransactionProviderFilter", graphql_name="provider")
    """Provider filter"""

    status = sgqlc.types.Field(TransactionStatus, graphql_name="status")
    """Status filter"""

    date_from = sgqlc.types.Field(String, graphql_name="dateFrom")
    """Filter transactions starting from this date. This API requires
    either a dateFrom, the invoice.id or, card.id and startDateFrom to
    be provided. If card.id is provided, startDateFrom is required.
    Use dateFrom and dateTo to define the range to filter results,
    based on lastUpdatedDate. Difference between dates is not allowed
    to exceed 1 month.
    """

    date_to = sgqlc.types.Field(String, graphql_name="dateTo")
    """Filter transactions up to this date. This API requires either a
    dateFrom, the invoice.id or, card.id and startDateFrom to be
    provided. If card.id is provided, startDateFrom is required. Use
    dateFrom and dateTo to define the range to filter results, based
    on lastUpdatedDate. Difference between dates is not allowed to
    exceed 1 month. If dateTo is omitted, a range of 1 month is used
    by default.
    """

    start_date_from = sgqlc.types.Field(String, graphql_name="startDateFrom")
    """Filter transactions starting from this date. When provided,
    filters results based on the transaction startDate field, starting
    from the given startDateFrom. Must be used in combination with
    startDateTo. The maximum allowed time range is 1 year. If
    startDateTo is omitted, a range of 1 year is used by default.
    """

    start_date_to = sgqlc.types.Field(String, graphql_name="startDateTo")
    """Filter transactions up to this date. When provided, filters
    results based on the transaction startDate field, starting from
    the given startDateFrom. Must be used in combination with
    startDateTo. The maximum allowed time range is 1 year. If
    startDateTo is omitted, a range of 1 year is used by default.
    """

    payment_method = sgqlc.types.Field(
        sgqlc.types.list_of(TransactionPaymentMethod), graphql_name="paymentMethod"
    )
    """Filter transactions by payment method"""


class TransactionInvoiceFilter(sgqlc.types.Input):
    """Filter by invoice for transaction queries. This API requires
    either a dateFrom, the invoice.id or, card.id and startDateFrom to
    be provided. If card.id is provided, startDateFrom is required.
    """

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Invoice ID to filter"""


class TransactionProviderFilter(sgqlc.types.Input):
    """Filter by provider for transaction queries"""

    __schema__ = schema
    __field_names__ = ("id",)
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Provider ID to filter"""


class TransactionSort(sgqlc.types.Input):
    """Sorting input for transaction queries"""

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
    """Sort by transaction ID"""

    last_update_date = sgqlc.types.Field(SortDirection, graphql_name="lastUpdateDate")
    """Sort by last update date"""

    remote_last_update_date = sgqlc.types.Field(
        SortDirection, graphql_name="remoteLastUpdateDate"
    )
    """Sort by remote last update date"""

    total_energy = sgqlc.types.Field(SortDirection, graphql_name="totalEnergy")
    """Sort by total energy consumed"""

    start_date = sgqlc.types.Field(SortDirection, graphql_name="startDate")
    """Sort by start date of transaction"""

    total_duration = sgqlc.types.Field(SortDirection, graphql_name="totalDuration")
    """Sort by total duration of transaction"""


class UpdateCustomerInput(sgqlc.types.Input):
    """Input type for updating customer details, including personal,
    address, billing, and invoice-related information.
    """

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
    """Reference to the company entity in IRI format. Example:
    /api/platform/customers/12345
    """

    company_name = sgqlc.types.Field(String, graphql_name="companyName")
    """Full company name of the customer."""

    salutation = sgqlc.types.Field(Salutation, graphql_name="salutation")
    """Salutation for the customer (Mr, Mrs, or empty)."""

    first_name = sgqlc.types.Field(String, graphql_name="firstName")
    """First name of the customer contact person."""

    last_name = sgqlc.types.Field(String, graphql_name="lastName")
    """Last name of the customer contact person."""

    email = sgqlc.types.Field(String, graphql_name="email")
    """Primary email address of the customer contact person."""

    username = sgqlc.types.Field(String, graphql_name="username")
    """Username used by the customer to log into the platform."""

    street = sgqlc.types.Field(String, graphql_name="street")
    """Street name of the customer’s address."""

    street_number = sgqlc.types.Field(String, graphql_name="streetNumber")
    """Street number of the customer’s address."""

    street_number_ext = sgqlc.types.Field(String, graphql_name="streetNumberExt")
    """Additional street number extension (e.g., A, B, bis)."""

    zip_code = sgqlc.types.Field(String, graphql_name="zipCode")
    """Postal code (zip code) of the customer’s address."""

    city = sgqlc.types.Field(String, graphql_name="city")
    """City of the customer’s address."""

    country = sgqlc.types.Field(CodeInput, graphql_name="country")
    """Country of the customer’s address, referenced by code. Example:
    /api/platform/countries/12345
    """

    preferred_language = sgqlc.types.Field(CodeInput, graphql_name="preferredLanguage")
    """Preferred language of the customer interface. Example:
    /api/platform/languages/12345
    """

    invoice_name = sgqlc.types.Field(String, graphql_name="invoiceName")
    """Invoice recipient name (can differ from customer name)."""

    invoice_street = sgqlc.types.Field(String, graphql_name="invoiceStreet")
    """Street name of the invoice address."""

    invoice_street_number = sgqlc.types.Field(
        String, graphql_name="invoiceStreetNumber"
    )
    """Street number of the invoice address."""

    invoice_street_number_ext = sgqlc.types.Field(
        String, graphql_name="invoiceStreetNumberExt"
    )
    """Street number extension of the invoice address."""

    invoice_zip_code = sgqlc.types.Field(String, graphql_name="invoiceZipCode")
    """Postal code (zip code) of the invoice address."""

    invoice_city = sgqlc.types.Field(String, graphql_name="invoiceCity")
    """City of the invoice address."""

    invoice_country = sgqlc.types.Field(CodeInput, graphql_name="invoiceCountry")
    """Country of the invoice address, referenced by code. Example:
    /api/platform/countries/12345
    """

    invoice_email = sgqlc.types.Field(String, graphql_name="invoiceEmail")
    """Email address for sending invoices."""

    phone = sgqlc.types.Field(String, graphql_name="phone")
    """Phone number of the customer contact person."""

    mobile = sgqlc.types.Field(String, graphql_name="mobile")
    """Mobile phone number of the customer contact person."""

    billing_account_number = sgqlc.types.Field(
        String, graphql_name="billingAccountNumber"
    )
    """Billing account number used for financial transactions."""

    bic = sgqlc.types.Field(String, graphql_name="bic")
    """Bank Identifier Code (BIC). Kept for validation logic
    compatibility. Not always required.
    """

    billing_account_name = sgqlc.types.Field(String, graphql_name="billingAccountName")
    """Billing account holder name."""

    license_plate = sgqlc.types.Field(String, graphql_name="licensePlate")
    """Vehicle license plate associated with the customer."""

    info = sgqlc.types.Field(String, graphql_name="info")
    """Additional notes or metadata related to the customer."""

    reference = sgqlc.types.Field(String, graphql_name="reference")
    """Reference identifier for the customer (internal or external)."""

    cost_center_number = sgqlc.types.Field(String, graphql_name="costCenterNumber")
    """Cost center number for customer accounting purposes."""


class UserGroupFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ("page", "items_per_page")
    page = sgqlc.types.Field(Int, graphql_name="page")
    """Page number"""

    items_per_page = sgqlc.types.Field(Int, graphql_name="itemsPerPage")
    """Number of items per page"""


########################################################################
# Output Objects and Interfaces
########################################################################
class AccessOptions(sgqlc.types.Type):
    """Configuration options controlling who can access a location and
    how.
    """

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
    """The general access type (private, public paid, public free)."""

    private_access_cards = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(ID)), graphql_name="privateAccessCards"
    )
    """List of private access cards allowed for this chargepoint."""

    auto_charge_support = sgqlc.types.Field(Boolean, graphql_name="autoChargeSupport")
    """Whether the location supports auto-charge."""

    authorization_mode = sgqlc.types.Field(
        AuthorizationMode, graphql_name="authorizationMode"
    )
    """The specific authorization mode"""

    charge_card = sgqlc.types.Field(String, graphql_name="chargeCard")
    """Charge card visual number or reference in use for auto-charge (if
    applicable).
    """

    published_on_map = sgqlc.types.Field(Boolean, graphql_name="publishedOnMap")
    """Indicates whether the station should be visible on public
    maps/apps.
    """


class ActionType(sgqlc.types.Type):
    """Describes a specific type of action/event within the system."""

    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    """Unique identifier of the action type."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Human-readable name of the action type."""


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
    """Represents a app feature entity."""

    __schema__ = schema
    __field_names__ = ("id", "enabled", "app", "feature_key")
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")
    """Unique ID of the app feature setting"""

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")
    """Whether the feature is enabled globally for the associated app"""

    app = sgqlc.types.Field(sgqlc.types.non_null("AppIdentifier"), graphql_name="app")
    """The specific application this feature setting applies to"""

    feature_key = sgqlc.types.Field(
        sgqlc.types.non_null("FeatureKey"), graphql_name="featureKey"
    )
    """The key defining the app-specific feature"""


class AppIdentifier(sgqlc.types.Type):
    """Represents a app identifier entity."""

    __schema__ = schema
    __field_names__ = (
        "id",
        "android_bundle_id",
        "ios_bundle_id",
        "app_features",
        "customer_features",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="id")
    """Unique ID of the application"""

    android_bundle_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="androidBundleId"
    )
    """The Android bundle ID"""

    ios_bundle_id = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="iosBundleId"
    )
    """The iOS bundle ID"""

    app_features = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AppFeature)),
        graphql_name="appFeatures",
    )
    """List of app-specific features"""

    customer_features = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("CustomerFeature")),
        graphql_name="customerFeatures",
    )
    """List of customer-specific features"""


class Authorisation(sgqlc.types.Type):
    """Authorisation details for a transaction"""

    __schema__ = schema
    __field_names__ = ("id", "method")
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Unique ID of the authorisation record"""

    method = sgqlc.types.Field(TransactionMethod, graphql_name="method")
    """Method used to authorise the transaction"""


class BankAccount(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("id", "scheme", "holder_name", "fields", "status", "customer")
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Unique identifier of the bank account"""

    scheme = sgqlc.types.Field(BankAccountScheme, graphql_name="scheme")
    """Bank account scheme (e.g., IBAN, SORT)"""

    holder_name = sgqlc.types.Field(String, graphql_name="holderName")
    """Name of the account holder"""

    fields = sgqlc.types.Field("BankAccountFields", graphql_name="fields")
    """Additional fields related to the bank account"""

    status = sgqlc.types.Field(String, graphql_name="status")
    """Status of the bank account (e.g., verified, unverified)"""

    customer = sgqlc.types.Field("Customer", graphql_name="customer")
    """Customer associated with this bank account"""


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
    """A charge card represents a physical RFID card or a virtual card
    (e.g. app-based token) that authorizes charging sessions at charge
    points. Cards are linked to customers, contracts, providers, and
    roaming settings.
    """

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
    """Unique identifier of the card in the system."""

    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    """The user group this card belongs to (e.g. fleet, department, or
    business unit).
    """

    internal_id = sgqlc.types.Field(String, graphql_name="internalId")
    """Internal identifier of the card. For RFID cards this must be 8 or
    14 hex characters.
    """

    external_id = sgqlc.types.Field(String, graphql_name="externalId")
    """External identifier of the card, as defined by an external system
    or provider.
    """

    contract_id = sgqlc.types.Field(String, graphql_name="contractId")
    """Unique contract identifier associated with this card."""

    customer = sgqlc.types.Field("Customer", graphql_name="customer")
    """The customer account this card is assigned to."""

    transaction_customer = sgqlc.types.Field(
        "Customer", graphql_name="transactionCustomer"
    )
    """The customer account used for billing charging transactions of
    this card.
    """

    product_customer = sgqlc.types.Field("Customer", graphql_name="productCustomer")
    """The customer account linked for product and subscription purposes."""

    creation_date = sgqlc.types.Field(String, graphql_name="creationDate")
    """Timestamp when the card was first created in the system (ISO
    8601).
    """

    last_update_date = sgqlc.types.Field(String, graphql_name="lastUpdateDate")
    """Timestamp when the card was last updated in the system (ISO 8601)."""

    info = sgqlc.types.Field(String, graphql_name="info")
    """Optional human-readable description or metadata about the card."""

    state = sgqlc.types.Field(CardState, graphql_name="state")
    """Current lifecycle state of the card (e.g. Active, Blocked,
    Expired).
    """

    expiry_date = sgqlc.types.Field(String, graphql_name="expiryDate")
    """Date when the card expires and can no longer be used (ISO 8601)."""

    activation_date = sgqlc.types.Field(String, graphql_name="activationDate")
    """Date when the card becomes valid and can first be used (ISO 8601)."""

    type = sgqlc.types.Field(CardType, graphql_name="type")
    """Type of the card (e.g. RFID, Virtual, App)."""

    action_type = sgqlc.types.Field(ActionType, graphql_name="actionType")
    """Action type linked to the card (e.g. authentication or
    authorization type).
    """

    card_provider = sgqlc.types.Field("CardProvider", graphql_name="cardProvider")
    """Provider that issued or manages this card."""

    roaming = sgqlc.types.Field(Boolean, graphql_name="roaming")
    """Indicates whether this card can be used for roaming across
    external networks.
    """

    deactivation_reason = sgqlc.types.Field(
        DeactivationReason, graphql_name="deactivationReason"
    )
    """Reason the card was deactivated (if state is inactive)."""

    is_global = sgqlc.types.Field(Boolean, graphql_name="isGlobal")
    """Indicates whether this card is a global/master card (e.g. company-
    wide use).
    """

    roaming_home_charging_enabled = sgqlc.types.Field(
        Boolean, graphql_name="roamingHomeChargingEnabled"
    )
    """Indicates if this card is used for home charging but managed by
    another MSP (roaming MSP).
    """

    roaming_hub_status = sgqlc.types.Field(CardState, graphql_name="roamingHubStatus")
    """Current roaming state of the charge card. Will return inactive if
    the card is not found in the roaming network.
    """

    reference = sgqlc.types.Field(String, graphql_name="reference")
    """Reference string assigned to the card for internal or external
    correlation.
    """

    qr_code = sgqlc.types.Field(String, graphql_name="qrCode")
    """QR code linked to this card, often used for mobile app
    identification.
    """

    parent_card = sgqlc.types.Field(String, graphql_name="parentCard")
    """Reference to the parent card if this card is a derivative or sub-
    card.
    """

    cost_center_number = sgqlc.types.Field(String, graphql_name="costCenterNumber")
    """Cost center number associated with this card for
    accounting/billing purposes.
    """

    user_groups = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("UserGroup")),
        graphql_name="userGroups",
    )
    """User groups that are associated with this card."""

    subscriptions = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null("LmsSubscription")),
        graphql_name="subscriptions",
    )
    """Subscriptions (e.g. charging plans, services) linked to this card."""


class CardCollection(sgqlc.types.Type):
    """A paginated collection of cards returned from queries."""

    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(Card), graphql_name="items")
    """List of card items for the current page."""

    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")
    """Total number of matching cards across all pages."""


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
    """Provider of charging cards."""

    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    """Unique identifier of the provider."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Provider name."""


class CardRoaming(sgqlc.types.Type):
    """Roaming-related properties of a card, typically synchronized with
    external hubs.
    """

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
    """Unique identifier of the card."""

    internal_id = sgqlc.types.Field(String, graphql_name="internalId")
    """Internal identifier used by the issuing system."""

    external_id = sgqlc.types.Field(String, graphql_name="externalId")
    """External identifier used in roaming contexts."""

    contract_id = sgqlc.types.Field(String, graphql_name="contractId")
    """Contract identifier of the card."""

    state = sgqlc.types.Field(CardState, graphql_name="state")
    """Lifecycle state of the card (e.g. Active, Blocked)."""

    type = sgqlc.types.Field(CardType, graphql_name="type")
    """Type of the card (e.g. RFID, Virtual)."""

    issuer = sgqlc.types.Field(String, graphql_name="issuer")
    """Entity or provider that issued the card."""

    creation_date = sgqlc.types.Field(String, graphql_name="creationDate")
    """Timestamp when the card was created (ISO 8601)."""

    expiry_date = sgqlc.types.Field(String, graphql_name="expiryDate")
    """Timestamp when the card expires (ISO 8601)."""

    last_update_date = sgqlc.types.Field(String, graphql_name="lastUpdateDate")
    """Timestamp of the last update to the card (ISO 8601)."""

    roaming_profile = sgqlc.types.Field("RoamingProfile", graphql_name="roamingProfile")
    """Roaming profile configuration for the card."""

    roaming_profile_hub = sgqlc.types.Field(
        "RoamingProfileHub", graphql_name="roamingProfileHub"
    )
    """Roaming hub configuration linked to this card."""

    whitelist_type = sgqlc.types.Field(WhitelistType, graphql_name="whitelistType")
    """Method by which the card is whitelisted/validated for roaming."""

    roaming = sgqlc.types.Field(Boolean, graphql_name="roaming")
    """Whether roaming is enabled for this card."""

    reference = sgqlc.types.Field(String, graphql_name="reference")
    """Optional external reference for correlation in roaming networks."""


class ChargeGroup(sgqlc.types.Type):
    """Represents a logical grouping of charging stations or connectors.
    Charge groups define shared attributes like accessibility,
    tariffs, and user group permissions that apply across multiple
    charging points.
    """

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
    """Unique identifier of the charge group."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Human-readable name of the charge group (e.g., 'Downtown Garage
    Chargers').
    """

    info = sgqlc.types.Field(String, graphql_name="info")
    """Optional descriptive text or notes about the charge group."""

    accessible_for_public_use = sgqlc.types.Field(
        Boolean, graphql_name="accessibleForPublicUse"
    )
    """Whether the charge group is open for public use (accessible
    without restrictions).
    """

    direct_payments_enabled = sgqlc.types.Field(
        Boolean, graphql_name="directPaymentsEnabled"
    )
    """Whether direct, ad-hoc payments are allowed without a user account
    or contract.
    """

    accessible_for_roaming = sgqlc.types.Field(
        Boolean, graphql_name="accessibleForRoaming"
    )
    """Whether the group is accessible via roaming (through external
    e-mobility providers).
    """

    social_charging_available = sgqlc.types.Field(
        Boolean, graphql_name="socialChargingAvailable"
    )
    """Whether the group participates in social charging (e.g., community
    sharing features).
    """

    type = sgqlc.types.Field(ChargeGroupType, graphql_name="type")
    """The classification of the charge group (Home or Other)."""

    smart_charging_opt_out_allowed = sgqlc.types.Field(
        Boolean, graphql_name="smartChargingOptOutAllowed"
    )
    """Whether users can opt out of smart charging (automated load
    management).
    """

    tariff = sgqlc.types.Field("Tariff", graphql_name="tariff")
    """The default tariff applied when using this charge group."""

    prepaid_tariff = sgqlc.types.Field("Tariff", graphql_name="prepaidTariff")
    """A prepaid tariff option available for this charge group, if
    applicable.
    """

    anonymous_tariff = sgqlc.types.Field("Tariff", graphql_name="anonymousTariff")
    """A tariff applied for anonymous users (no account / roaming
    contract).
    """

    tariff_vat = sgqlc.types.Field("TariffResult", graphql_name="tariffVat")
    """Tariff including VAT (value-added tax) for regular usage."""

    prepaid_tariff_vat = sgqlc.types.Field(
        "TariffResult", graphql_name="prepaidTariffVat"
    )
    """Prepaid tariff including VAT."""

    anonymous_tariff_vat = sgqlc.types.Field(
        "TariffResult", graphql_name="anonymousTariffVat"
    )
    """Anonymous tariff including VAT."""

    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    """The user group associated with this charge group (controls access
    and permissions).
    """

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
    """Returns a collection of charge stations belonging to this charge
    group, supporting filters and sorting. Returns a collection of
    charge stations.

    Arguments:

    * `filters` (`ChargeStationFilter`)None
    * `sort` (`ChargeStationSort`)None
    """

    customers = sgqlc.types.Field(
        sgqlc.types.list_of("ChargeGroupCustomer"), graphql_name="customers"
    )
    """List of customers associated with this charge group. Returns a
    collection of charge group customers.
    """


class ChargeGroupCollection(sgqlc.types.Type):
    """A paginated collection of charge groups.   Includes the actual
    list of groups and metadata such as total item count.
    """

    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(ChargeGroup), graphql_name="items")
    """The list of charge groups matching the filter and sort criteria."""

    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")
    """The total number of charge groups available (ignores pagination)."""


class ChargeGroupCustomer(sgqlc.types.Type):
    """Represents a customer within a charge group context."""

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
    """Unique identifier"""

    first_name = sgqlc.types.Field(String, graphql_name="firstName")
    """First name of the customer"""

    last_name = sgqlc.types.Field(String, graphql_name="lastName")
    """Last name of the customer"""

    company_name = sgqlc.types.Field(String, graphql_name="companyName")
    """Company name if applicable"""

    type = sgqlc.types.Field(CustomerType, graphql_name="type")
    """Customer type"""

    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    """User group associated with the customer"""

    tariff = sgqlc.types.Field("LmsTariff", graphql_name="tariff")
    """Assigned tariff plan for the customer"""


class ChargeStation(sgqlc.types.Type):
    """Represents a full charge station with its channels, hardware,
    software, and operational metadata. Used in APIs to manage,
    monitor, and query EVSE assets.
    """

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
    """Unique identifier of the charge station."""

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    """Human-readable name of the station (used in UIs and reporting)."""

    reference = sgqlc.types.Field(String, graphql_name="reference")
    """External reference for the station (optional, may be used in
    contracts or asset management).
    """

    comm_id = sgqlc.types.Field(String, graphql_name="commId")
    """Communication ID used to identify the station in backend systems."""

    comm_key = sgqlc.types.Field(String, graphql_name="commKey")
    """Communication key for secure messaging with the station."""

    comm_medium = sgqlc.types.Field(String, graphql_name="commMedium")
    """Medium used for communication (e.g., Ethernet, 4G, Wi-Fi)."""

    comm_mode = sgqlc.types.Field(String, graphql_name="commMode")
    """Mode of communication (protocol or interface type)."""

    comm_status = sgqlc.types.Field(String, graphql_name="commStatus")
    """Status of the communication link (connected, disconnected, error)."""

    comm_version = sgqlc.types.Field(Float, graphql_name="commVersion")
    """Version of the communication software or protocol."""

    cost_center_number = sgqlc.types.Field(String, graphql_name="costCenterNumber")
    """Reference to the provider operating this station."""

    state = sgqlc.types.Field(ChargeStationState, graphql_name="state")
    """Operational state of the station (Active, Inactive, Blocked)."""

    physical_number = sgqlc.types.Field(String, graphql_name="physicalNumber")
    """Physical hardware number of the station. Useful for maintenance
    and asset tagging.
    """

    gps_address = sgqlc.types.Field(String, graphql_name="gpsAddress")
    """Street address where the station is physically installed."""

    gps_city = sgqlc.types.Field(String, graphql_name="gpsCity")
    """City where the station is located."""

    gps_country = sgqlc.types.Field("Country", graphql_name="gpsCountry")
    """Country of installation (links to standardized Country type)."""

    last_communication_date = sgqlc.types.Field(
        String, graphql_name="lastCommunicationDate"
    )
    """Timestamp of the last communication received from the station."""

    channels = sgqlc.types.Field(
        sgqlc.types.list_of("ChargeStationChannel"), graphql_name="channels"
    )
    """List of channels available on this station. Each channel
    represents a single connector.
    """

    parameter_set = sgqlc.types.Field("ParameterSet", graphql_name="parameterSet")
    """Parameter set currently applied to this station, defining default
    operational and billing rules.
    """

    charge_group = sgqlc.types.Field(ChargeGroup, graphql_name="chargeGroup")
    """Charge group that this station belongs to, defining tariffs and
    operational policies.
    """

    owner = sgqlc.types.Field("Customer", graphql_name="owner")
    """Customer or organization that owns this station."""

    usergroup = sgqlc.types.Field("UserGroup", graphql_name="usergroup")
    """User group controlling access permissions to this station."""

    location = sgqlc.types.Field("Location", graphql_name="location")
    """Physical location details for the station, used for geolocation
    queries.
    """

    sim_number = sgqlc.types.Field(String, graphql_name="simNumber")
    """SIM number assigned to the station for cellular connectivity."""

    software_version = sgqlc.types.Field(String, graphql_name="softwareVersion")
    """Software version currently installed on the station."""

    activation_date = sgqlc.types.Field(String, graphql_name="activationDate")
    """Activation date when the station became operational."""

    subscriptions = sgqlc.types.Field(
        sgqlc.types.list_of("LmsSubscription"), graphql_name="subscriptions"
    )
    """Subscriptions linked to this station (e.g., billing or service
    plans).
    """

    manufacturer_type = sgqlc.types.Field(
        "ManufacturerType", graphql_name="manufacturerType"
    )
    """Manufacturer and model type of the station hardware."""

    parameters = sgqlc.types.Field(
        sgqlc.types.list_of("ChargeStationParameter"), graphql_name="parameters"
    )
    """List of all configurable parameters of the station, including
    runtime values.
    """

    payer_subscription = sgqlc.types.Field("Customer", graphql_name="payerSubscription")
    """Customer or organization that pays for the subscription on this
    station.
    """

    recipient_charge_transactions = sgqlc.types.Field(
        "Customer", graphql_name="recipientChargeTransactions"
    )
    """Customer or organization that receives the compensation on
    transactions of this station.
    """

    access_options = sgqlc.types.Field(
        sgqlc.types.non_null(AccessOptions), graphql_name="accessOptions"
    )
    """Access options defining how users can interact with this station
    (keys, RFID, remote control, etc.).
    """

    home_charging_compensation = sgqlc.types.Field(
        "HomeChargingCompensation", graphql_name="homeChargingCompensation"
    )
    """Home charging compensation configuration if the station is
    eligible for energy reimbursement.
    """

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
    """Lists transactions for this charge station. Specify one or more
    query parameters to filter the transaction that appear in the
    response. Each item in the list includes basic transaction
    details.  This API requires either a dateFrom, the invoice.id or,
    card.id and startDateFrom to be provided. If card.id is provided,
    startDateFrom is required. Use dateFrom and dateTo to define the
    range to filter results, based on lastUpdatedDate. Difference
    between dates is not allowed to exceed 1 month.

    Arguments:

    * `filters` (`TransactionFilter`)None
    * `sort` (`TransactionSort`)None
    """

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
    """Retrieve tickets associated with this charge station, supporting
    filters and sorting. Returns a collection of tickets.

    Arguments:

    * `filters` (`TicketFilter`)None
    * `sort` (`TicketSort`)None
    """


class ChargeStationChannel(sgqlc.types.Type):
    """Represents a single physical charging channel on a charge station.
    Each channel corresponds to one connector and supports specific
    AC/DC, phases, power, and capabilities.
    """

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
    """Unique identifier of the channel."""

    channel_no = sgqlc.types.Field(Int, graphql_name="channelNo")
    """Logical channel number assigned by the charge station. Typically
    used in user interfaces or OCPP messages.
    """

    meter_id = sgqlc.types.Field(String, graphql_name="meterId")
    """Identifier of the meter attached to this channel for energy
    measurement.
    """

    obis_code = sgqlc.types.Field(String, graphql_name="obisCode")
    """OBIS (Object Identification System) code used for metering and
    energy data standardization.
    """

    auto_connector = sgqlc.types.Field(Boolean, graphql_name="autoConnector")
    """Indicates if the station automatically selects the connector for
    the vehicle.
    """

    connector_type = sgqlc.types.Field(
        ChargeStationChannelConnectorType, graphql_name="connectorType"
    )
    """Type of physical connector (e.g., Type 2, CHAdeMO, Tesla)
    supported by this channel.
    """

    phases = sgqlc.types.Field(Int, graphql_name="phases")
    """Number of electrical phases supplied by this channel. Typically 1
    or 3.
    """

    amp = sgqlc.types.Field(Int, graphql_name="amp")
    """Maximum current (in Amperes) supported by this channel."""

    power = sgqlc.types.Field(Int, graphql_name="power")
    """Maximum power output (in kW) of this channel."""

    voltage = sgqlc.types.Field(Int, graphql_name="voltage")
    """Voltage supplied by the channel (in Volts)."""

    ac_dc = sgqlc.types.Field(ChargeStationChannelAcDc, graphql_name="acDc")
    """Indicates whether the channel provides AC or DC current."""

    negate_meter = sgqlc.types.Field(Boolean, graphql_name="negateMeter")
    """Flag indicating whether the meter reading should be negated (e.g.,
    for energy export accounting).
    """

    last_status_change_date = sgqlc.types.Field(
        String, graphql_name="lastStatusChangeDate"
    )
    """Timestamp of the last status change reported by the channel."""

    physical_number = sgqlc.types.Field(String, graphql_name="physicalNumber")
    """Physical identifier of the channel (used for maintenance or
    hardware labeling).
    """

    connector_format = sgqlc.types.Field(
        ChargeStationChannelConnectorFormat, graphql_name="connectorFormat"
    )
    """Indicates whether the connector is a socket (driver-provided
    cable) or a fixed cable.
    """

    hubject_compatible = sgqlc.types.Field(Boolean, graphql_name="hubjectCompatible")
    """True if the channel supports Hubject roaming platform for
    interoperability.
    """

    evse_id = sgqlc.types.Field(String, graphql_name="evseId")
    """EVSE identifier assigned to this channel for backend systems and
    roaming.
    """

    evse_id_clean = sgqlc.types.Field(String, graphql_name="evseIdClean")
    """Cleaned or normalized EVSE ID for database indexing or API
    responses.
    """

    qr_code = sgqlc.types.Field(String, graphql_name="qrCode")
    """Short QR code string associated with this channel (used for
    scanning to start a session).
    """

    qr_code_full = sgqlc.types.Field(String, graphql_name="qrCodeFull")
    """Full QR code content including station and channel metadata."""

    capabilities = sgqlc.types.Field(
        sgqlc.types.list_of(ChargeStationChannelCapability), graphql_name="capabilities"
    )
    """Functional capabilities supported by the channel (authorization,
    payment, remote start/stop, etc.).
    """

    global_status = sgqlc.types.Field(
        ChargeStationChannelGlobalStatus, graphql_name="globalStatus"
    )
    """Aggregated global status of the channel (available, charging,
    reserved, faulty, etc.).
    """

    statuses = sgqlc.types.Field(
        sgqlc.types.list_of(ChargeStationChannelStatus), graphql_name="statuses"
    )
    """Detailed technical or error statuses reported by the channel."""

    charge_station = sgqlc.types.Field(ChargeStation, graphql_name="chargeStation")
    """Reference to the parent charge station that owns this channel."""

    channel_profile = sgqlc.types.Field(String, graphql_name="channelProfile")
    """Optional channel profile or configuration string describing power
    schedules, limits, or profiles.
    """


class ChargeStationCollection(sgqlc.types.Type):
    """Paginated collection of charge stations. Includes station list and
    total item count.
    """

    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(ChargeStation), graphql_name="items")
    """List of stations returned by the query."""

    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")
    """Total number of stations matching the filter (ignores pagination)."""


class ChargeStationParameter(sgqlc.types.Type):
    """Actual parameter instance applied to a charge station. Represents
    the current value of a parameter and its metadata.
    """

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
    """Unique identifier of this parameter instance."""

    charge_station = sgqlc.types.Field(ChargeStation, graphql_name="chargeStation")
    """The charge station to which this parameter belongs."""

    parameter_info = sgqlc.types.Field(
        "ChargeStationParameterInfo", graphql_name="parameterInfo"
    )
    """Definition metadata of this parameter."""

    value = sgqlc.types.Field(String, graphql_name="value")
    """Current value set for this parameter."""

    boot = sgqlc.types.Field(Boolean, graphql_name="boot")
    """Whether this parameter is set at boot time."""

    is_default = sgqlc.types.Field(Boolean, graphql_name="isDefault")
    """Whether this parameter is part of the station’s default
    configuration.
    """


class ChargeStationParameterInfo(sgqlc.types.Type):
    """Metadata describing a configurable parameter of a charge station.
    Provides technical limits and context for parameter adjustments.
    """

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
    """Unique identifier of the parameter definition."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Short name of the parameter."""

    full_name = sgqlc.types.Field(String, graphql_name="fullName")
    """Full descriptive name of the parameter."""

    type = sgqlc.types.Field(String, graphql_name="type")
    """Data type of the parameter (e.g., string, integer, boolean)."""

    min_value = sgqlc.types.Field(String, graphql_name="minValue")
    """Minimum allowed value."""

    max_value = sgqlc.types.Field(String, graphql_name="maxValue")
    """Maximum allowed value."""

    flags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name="flags")
    """Flags providing additional metadata (e.g., read-only, requires
    reboot).
    """


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
    """The start time of the schedule in UTC"""

    stop_time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="stopTime")
    """The stop time of the schedule in UTC"""


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
    """Represents a country with charging, currency, and tax details."""

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
    """ISO 3166-1 alpha-2 country code (e.g. NL, DE)."""

    code3_chars = sgqlc.types.Field(String, graphql_name="code3Chars")
    """ISO 3166-1 alpha-3 code (e.g. NLD)."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Full English name of the country."""

    local_name = sgqlc.types.Field(String, graphql_name="localName")
    """Localized name of the country in its native language."""

    phone_country_code = sgqlc.types.Field(Int, graphql_name="phoneCountryCode")
    """International dialing code (e.g. 31 for Netherlands)."""

    currency = sgqlc.types.Field("Currency", graphql_name="currency")
    """Primary currency used in this country."""

    default_time_zone = sgqlc.types.Field(String, graphql_name="defaultTimeZone")
    """Default timezone for this country."""

    default_interface_language = sgqlc.types.Field(
        "CountryLanguage", graphql_name="defaultInterfaceLanguage"
    )
    """Default interface language (used in UI for users in this country)."""

    default_language = sgqlc.types.Field(
        "CountryLanguage", graphql_name="defaultLanguage"
    )
    """Default spoken/written language."""

    languages = sgqlc.types.Field(
        sgqlc.types.list_of("CountryLanguage"), graphql_name="languages"
    )
    """List of supported languages in this country."""

    vat_union = sgqlc.types.Field(String, graphql_name="vatUnion")
    """VAT (tax) union membership (e.g. "EU")."""

    outside_vat_union_vat_applicable = sgqlc.types.Field(
        Boolean, graphql_name="outsideVatUnionVatApplicable"
    )
    """Whether VAT applies when trading outside of the union."""


class CountryCollection(sgqlc.types.Type):
    """A collection of countries."""

    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(Country), graphql_name="items")
    """List of countries for the current page."""

    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")
    """Total number of countries across all pages."""


class CountryLanguage(sgqlc.types.Type):
    """Represents a language as spoken in a specific country."""

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
    """Language code (internal ID)."""

    code2_chars = sgqlc.types.Field(String, graphql_name="code2Chars")
    """ISO 639-1 two-letter language code (e.g. "en")."""

    code3_chars = sgqlc.types.Field(String, graphql_name="code3Chars")
    """ISO 639-2 three-letter language code (e.g. "eng")."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Full name of the language (e.g. "English")."""

    country = sgqlc.types.Field(Country, graphql_name="country")
    """Associated country of this language."""

    supported = sgqlc.types.Field(Boolean, graphql_name="supported")
    """Whether the language is officially supported by the platform."""


class CountryLanguageCollection(sgqlc.types.Type):
    """A collection of currencies."""

    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(
        sgqlc.types.list_of(CountryLanguage), graphql_name="items"
    )
    """List of languages for the current page."""

    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")
    """Total number of languages across all pages."""


class CreateScheduleResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("uuid", "name", "payload", "created_at")
    uuid = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="uuid")

    name = sgqlc.types.Field(sgqlc.types.non_null(ScheduleName), graphql_name="name")

    payload = sgqlc.types.Field("SchedulePayload", graphql_name="payload")

    created_at = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name="createdAt")


class Currency(sgqlc.types.Type):
    """Currency supported in charging transactions."""

    __schema__ = schema
    __field_names__ = ("code", "symbol", "name", "supported")
    code = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="code")
    """ISO 4217 currency code (e.g. EUR, USD)."""

    symbol = sgqlc.types.Field(String, graphql_name="symbol")
    """Currency symbol (€, $, etc)."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Full name of the currency."""

    supported = sgqlc.types.Field(Boolean, graphql_name="supported")
    """Whether this currency is supported for payments."""


class CurrencyCollection(sgqlc.types.Type):
    """A collection of currencies."""

    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(Currency), graphql_name="items")
    """List of currencies for the current page."""

    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")
    """Total number of currencies across all pages."""


class Customer(sgqlc.types.Type):
    """Core customer entity with personal, billing, and operational data."""

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
    """Unique identifier"""

    usergroup_name = sgqlc.types.Field(String, graphql_name="usergroupName")
    """Deprecated: Name of the user group"""

    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    """User group the customer belongs to"""

    object_id = sgqlc.types.Field(String, graphql_name="objectId")
    """Deprecated: Object identifier"""

    type = sgqlc.types.Field(sgqlc.types.non_null(CustomerType), graphql_name="type")
    """Type of customer"""

    salutation = sgqlc.types.Field(CustomerSalutation, graphql_name="salutation")
    """Salutation for formal address"""

    first_name = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="firstName"
    )
    """Customer first name"""

    last_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="lastName")
    """Customer last name"""

    company_name = sgqlc.types.Field(String, graphql_name="companyName")
    """Name of the company the customer belongs to"""

    company = sgqlc.types.Field(String, graphql_name="company")
    """Company affiliation"""

    gender = sgqlc.types.Field(String, graphql_name="gender")
    """Gender of the customer"""

    email = sgqlc.types.Field(String, graphql_name="email")
    """Email address"""

    user_name = sgqlc.types.Field(String, graphql_name="userName")
    """Deprecated: username"""

    username = sgqlc.types.Field(String, graphql_name="username")
    """Login username"""

    street = sgqlc.types.Field(String, graphql_name="street")
    """Street address"""

    street_number = sgqlc.types.Field(String, graphql_name="streetNumber")
    """Street number"""

    street_number_ext = sgqlc.types.Field(String, graphql_name="streetNumberExt")
    """Street number extension"""

    zip_code = sgqlc.types.Field(String, graphql_name="zipCode")
    """Postal code"""

    city = sgqlc.types.Field(String, graphql_name="city")
    """City of residence"""

    country = sgqlc.types.Field(String, graphql_name="country")
    """Country code or name"""

    country_details = sgqlc.types.Field(Country, graphql_name="countryDetails")
    """Detailed country object"""

    preferred_language = sgqlc.types.Field(
        CountryLanguage, graphql_name="preferredLanguage"
    )
    """Preferred language of the customer"""

    time_zone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="timeZone")
    """Time zone identifier"""

    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="phone")
    """Primary phone number"""

    mobile = sgqlc.types.Field(String, graphql_name="mobile")
    """Mobile phone number"""

    agreement_condition = sgqlc.types.Field(Boolean, graphql_name="agreementCondition")
    """Deprecated: single agreement condition"""

    agreement_conditions = sgqlc.types.Field(
        Boolean, graphql_name="agreementConditions"
    )
    """Current agreement conditions"""

    state = sgqlc.types.Field(sgqlc.types.non_null(CustomerState), graphql_name="state")
    """Customer account state"""

    reimbursement_mode = sgqlc.types.Field(
        sgqlc.types.non_null(CustomerReimbursementMode),
        graphql_name="reimbursementMode",
    )
    """Reimbursement mode for this customer"""

    electronic_invoice = sgqlc.types.Field(
        sgqlc.types.non_null(CustomerElectronicInvoice),
        graphql_name="electronicInvoice",
    )
    """Electronic invoice configuration"""

    public_rech_groups = sgqlc.types.Field(Boolean, graphql_name="publicRechGroups")
    """Indicates if customer is part of public recharge groups"""

    receive_newsletters = sgqlc.types.Field(Boolean, graphql_name="receiveNewsletters")
    """Newsletter subscription preference"""

    send_email = sgqlc.types.Field(Boolean, graphql_name="sendEmail")
    """Whether emails should be sent to this customer"""

    disabled_login = sgqlc.types.Field(Boolean, graphql_name="disabledLogin")
    """If login is disabled"""

    info = sgqlc.types.Field(String, graphql_name="info")
    """Free-form information or notes about the customer"""

    cost_center_number = sgqlc.types.Field(String, graphql_name="costCenterNumber")
    """Internal cost center reference"""

    reference = sgqlc.types.Field(String, graphql_name="reference")
    """External reference identifier"""

    invoice_name = sgqlc.types.Field(String, graphql_name="invoiceName")
    """Name for invoices"""

    invoice_street = sgqlc.types.Field(String, graphql_name="invoiceStreet")
    """Street for invoice"""

    invoice_street_number = sgqlc.types.Field(
        String, graphql_name="invoiceStreetNumber"
    )
    """Street number for invoice"""

    invoice_street_number_ext = sgqlc.types.Field(
        String, graphql_name="invoiceStreetNumberExt"
    )
    """Street number extension for invoice"""

    invoice_zip_code = sgqlc.types.Field(String, graphql_name="invoiceZipCode")
    """Postal code for invoice"""

    invoice_city = sgqlc.types.Field(String, graphql_name="invoiceCity")
    """City for invoice"""

    invoice_country = sgqlc.types.Field(Country, graphql_name="invoiceCountry")
    """Country for invoice"""

    invoice_email = sgqlc.types.Field(String, graphql_name="invoiceEmail")
    """Email for invoice communication"""

    invoice_reference = sgqlc.types.Field(String, graphql_name="invoiceReference")
    """Reference for invoice"""

    billing_account_number = sgqlc.types.Field(
        String, graphql_name="billingAccountNumber"
    )
    """Billing account number"""

    bic = sgqlc.types.Field(String, graphql_name="bic")
    """Bank Identifier Code"""

    billing_account_name = sgqlc.types.Field(String, graphql_name="billingAccountName")
    """Billing account holder name"""

    license_plate = sgqlc.types.Field(String, graphql_name="licensePlate")
    """License plate associated with the customer (optional)"""

    charge_stations = sgqlc.types.Field(
        sgqlc.types.list_of(ChargeStation), graphql_name="chargeStations"
    )
    """List of charge stations assigned to this customer"""

    mandate = sgqlc.types.Field("CustomerMandate", graphql_name="mandate")
    """Mandate details"""

    bacs_mandate = sgqlc.types.Field("CustomerBacsMandate", graphql_name="bacsMandate")
    """Bacs Mandate details"""

    is_invoice_address_different = sgqlc.types.Field(
        Boolean, graphql_name="isInvoiceAddressDifferent"
    )
    """True if the invoice address differs from the main address"""

    provider_category = sgqlc.types.Field(
        ProviderCategory, graphql_name="providerCategory"
    )
    """The category of the provider that the customer belongs to, for
    example NL, UK, DE, etc.
    """

    cards = sgqlc.types.Field(sgqlc.types.list_of(Card), graphql_name="cards")
    """List of charge cards directly associated with this customer.
    Returns a collection of charge cards.
    """

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
    """Lists transactions for this customer. Specify one or more query
    parameters to filter the transaction that appear in the response.
    Each item in the list includes basic transaction details.  This
    API requires either a dateFrom, the invoice.id or, card.id and
    startDateFrom to be provided. If card.id is provided,
    startDateFrom is required. Use dateFrom and dateTo to define the
    range to filter results, based on lastUpdatedDate. Difference
    between dates is not allowed to exceed 1 month.

    Arguments:

    * `filters` (`TransactionFilter`)None
    * `sort` (`TransactionSort`)None
    """

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
    """Retrieve a paginated collection of invoices for this customer,
    with filtering and sorting options. Returns a collection of
    invoices.

    Arguments:

    * `page` (`Int`)None
    * `items_per_page` (`Int`)None
    * `filters` (`InvoiceFilter`)None
    * `sort` (`InvoiceSort`)None
    """

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
    """Retrieve tickets associated with this customer, supporting filters
    and sorting. Returns a collection of tickets.

    Arguments:

    * `filters` (`TicketFilter`)None
    * `sort` (`TicketSort`)None
    """

    srs_onboarding_complete = sgqlc.types.Field(
        Boolean, graphql_name="srsOnboardingComplete"
    )
    """Indicates if SRS onboarding is completed for this customer."""

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
    """List of effective features

    Arguments:

    * `app_id` (`String!`)None
    """

    is_shell_user = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="isShellUser"
    )
    """Indicates if the customer is a shell user."""


class CustomerBacsMandate(sgqlc.types.Type):
    """Represents thedetails of the customer's active UK BACS direct
    debit mandate
    """

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
    """A paginated collection of customers returned from queries."""

    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(Customer), graphql_name="items")
    """List of customer items for the current page."""

    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")
    """Total number of matching customers across all pages."""


class CustomerFeature(sgqlc.types.Type):
    """Represents a customer feature entity."""

    __schema__ = schema
    __field_names__ = ("user_id", "enabled", "app", "app_features", "feature_key")
    user_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="user_id")
    """The ID of the user this feature setting applies to"""

    enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="enabled")
    """Whether the feature is enabled for this specific customer"""

    app = sgqlc.types.Field(sgqlc.types.non_null(AppIdentifier), graphql_name="app")
    """The specific application this feature setting applies to"""

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
    """List of app-specific features

    Arguments:

    * `app_id` (`String!`)None
    """

    feature_key = sgqlc.types.Field(
        sgqlc.types.non_null("FeatureKey"), graphql_name="featureKey"
    )
    """The key defining the cutomer-specific feature"""


class CustomerMandate(sgqlc.types.Type):
    """Represents a financial mandate associated with a customer for
    billing purposes.
    """

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
    """Unique identifier of the mandate"""

    accepted = sgqlc.types.Field(Boolean, graphql_name="accepted")
    """Whether the customer has accepted the mandate"""

    customer = sgqlc.types.Field(Customer, graphql_name="customer")
    """Customer linked to this mandate"""

    stop_date = sgqlc.types.Field(String, graphql_name="stopDate")
    """Date when the mandate stops being valid"""

    billing_account_number = sgqlc.types.Field(
        String, graphql_name="billingAccountNumber"
    )
    """Bank account number associated with the mandate"""

    bic = sgqlc.types.Field(String, graphql_name="bic")
    """BIC (Bank Identifier Code) associated with the mandate"""

    billing_account_name = sgqlc.types.Field(String, graphql_name="billingAccountName")
    """Name of the account holder"""


class DisplayText(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("language", "text")
    language = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="language")

    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="text")


class EffectiveAppFeature(sgqlc.types.Type):
    """Represents an effective app feature."""

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
    """The type of energy source"""

    percentage = sgqlc.types.Field(Float, graphql_name="percentage")
    """Percentage of this source (0-100) in the mix"""


class EnvironmentalImpact(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("category", "amount")
    category = sgqlc.types.Field(
        sgqlc.types.non_null(EnvironmentalImpactCategory), graphql_name="category"
    )
    """The environmental impact category of this value"""

    amount = sgqlc.types.Field(Float, graphql_name="amount")
    """Amount of this portion in g/kWh"""


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
    """Represents a feature key entity."""

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
    """The primary key and unique identifier for the feature (e.g.,
    'dark_mode')
    """

    description = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="description"
    )
    """Description of the feature"""

    app_features = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(AppFeature)),
        graphql_name="appFeatures",
    )
    """List of application-level feature settings using this key"""

    customer_features = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(CustomerFeature)),
        graphql_name="customerFeatures",
    )
    """List of customer-level feature settings using this key"""


class HomeChargingCompensation(sgqlc.types.Type):
    """Settings for compensating home charging sessions (typically for
    employees).
    """

    __schema__ = schema
    __field_names__ = ("hcc_enabled", "hcc_tariff", "hcc_cards")
    hcc_enabled = sgqlc.types.Field(Boolean, graphql_name="hccEnabled")
    """Whether home charging compensation is enabled."""

    hcc_tariff = sgqlc.types.Field(Float, graphql_name="hccTariff")
    """Compensation tariff (cost per kWh or session)."""

    hcc_cards = sgqlc.types.Field(sgqlc.types.list_of(Card), graphql_name="hccCards")
    """List of cards eligible for home charging compensation."""


class Invoice(sgqlc.types.Type):
    """Represents a single invoice with all billing, VAT, customer, and
    payment information.
    """

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
        "vat_percentage",
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
    """Unique identifier for the invoice"""

    invoice_uuid = sgqlc.types.Field(String, graphql_name="invoiceUuid")
    """Universally unique identifier for the invoice"""

    credit = sgqlc.types.Field(Boolean, graphql_name="credit")
    """True if the invoice represents a credit transaction"""

    billing_type = sgqlc.types.Field(InvoiceBillingType, graphql_name="billingType")
    """Billing type for the invoice"""

    vat_type = sgqlc.types.Field(InvoiceVatType, graphql_name="vatType")
    """VAT type applied"""

    country = sgqlc.types.Field(Country, graphql_name="country")
    """Country in which the invoice applies"""

    date = sgqlc.types.Field(String, graphql_name="date")
    """Date when the invoice was issued"""

    customer = sgqlc.types.Field(Customer, graphql_name="customer")
    """Customer associated with this invoice"""

    payment_method = sgqlc.types.Field(
        InvoicePaymentMethod, graphql_name="paymentMethod"
    )
    """Payment method used"""

    payment_reference = sgqlc.types.Field(String, graphql_name="paymentReference")
    """Reference for payment processing"""

    currency = sgqlc.types.Field(Currency, graphql_name="currency")
    """Currency code for the invoice amounts"""

    cust_currency = sgqlc.types.Field(Currency, graphql_name="custCurrency")
    """Customer-specific currency"""

    amount_excl_vat = sgqlc.types.Field(Float, graphql_name="amountExclVAT")
    """Total amount excluding VAT"""

    vat_percentage = sgqlc.types.Field(Float, graphql_name="vatPercentage")
    """Percentage rate of VAT applied"""

    vat_amount = sgqlc.types.Field(Float, graphql_name="vatAmount")
    """Total VAT amount"""

    amount_incl_vat = sgqlc.types.Field(Float, graphql_name="amountInclVat")
    """Total amount including VAT"""

    cust_price_incl_vat = sgqlc.types.Field(Float, graphql_name="custPriceInclVat")
    """Total price including VAT in customer's currency"""

    regenerated = sgqlc.types.Field(Boolean, graphql_name="regenerated")
    """True if the invoice has been regenerated after modifications"""

    status = sgqlc.types.Field(InvoiceStatus, graphql_name="status")
    """Current status of the invoice"""

    type = sgqlc.types.Field(InvoiceType, graphql_name="type")
    """Type of invoice"""

    vat_number = sgqlc.types.Field(String, graphql_name="vatNumber")
    """VAT registration number of the customer"""

    invoice_product_details = sgqlc.types.Field(
        String, graphql_name="invoiceProductDetails"
    )
    """Details of the invoice products"""

    items = sgqlc.types.Field(sgqlc.types.list_of("InvoiceItem"), graphql_name="items")
    """Individual line items in the invoice"""

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
    """Lists transactions for this invoice. Specify one or more query
    parameters to filter the transaction that appear in the response.
    Each item in the list includes basic transaction details.  This
    API requires either a dateFrom, the invoice.id or, card.id and
    startDateFrom to be provided. If card.id is provided,
    startDateFrom is required. Use dateFrom and dateTo to define the
    range to filter results, based on lastUpdatedDate. Difference
    between dates is not allowed to exceed 1 month.

    Arguments:

    * `filters` (`TransactionFilter`)None
    * `sort` (`TransactionSort`)None
    """


class InvoiceCollection(sgqlc.types.Type):
    """Collection of invoices, supporting pagination."""

    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(Invoice), graphql_name="items")
    """List of invoices"""

    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")
    """Total number of invoices available"""


class InvoiceItem(sgqlc.types.Type):
    """Represents a single item or product within an invoice."""

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
    """Unique identifier for the invoice item"""

    invoice = sgqlc.types.Field(Invoice, graphql_name="invoice")
    """Parent invoice for this item"""

    product_name = sgqlc.types.Field(String, graphql_name="productName")
    """Name of the product or service"""

    number = sgqlc.types.Field(Int, graphql_name="number")
    """Quantity of the product"""

    number_text = sgqlc.types.Field(String, graphql_name="numberText")
    """Quantity as text (useful for PDFs or reports)"""

    full_unit_price_excl_vat = sgqlc.types.Field(
        Float, graphql_name="fullUnitPriceExclVat"
    )
    """Unit price excluding VAT"""

    discount_percentage = sgqlc.types.Field(Float, graphql_name="discountPercentage")
    """Discount applied to the item as a percentage"""

    vat_percentage = sgqlc.types.Field(Float, graphql_name="vatPercentage")
    """VAT rate applied to this item"""

    vat_type = sgqlc.types.Field(InvoiceVatType, graphql_name="vatType")
    """VAT type applied to this item"""

    full_unit_price_excl_vat_cust_currency = sgqlc.types.Field(
        Float, graphql_name="fullUnitPriceExclVatCustCurrency"
    )
    """Unit price excluding VAT in customer's currency"""

    conversion_fee_amount = sgqlc.types.Field(Float, graphql_name="conversionFeeAmount")
    """Any conversion fees applied to this item"""


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
    """ISO 4217"""

    min_price = sgqlc.types.Field(Float, graphql_name="minPrice")
    """in currency excl VAT"""

    max_price = sgqlc.types.Field(Float, graphql_name="maxPrice")
    """in currency excl VAT"""

    excl_service_provider_costs = sgqlc.types.Field(
        sgqlc.types.non_null(Boolean), graphql_name="exclServiceProviderCosts"
    )
    """If true, the service provider's costs are not included"""

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
    """ISO date-time string"""

    end_period_valid = sgqlc.types.Field(String, graphql_name="endPeriodValid")
    """ISO date-time string"""

    start_time_of_day = sgqlc.types.Field(String, graphql_name="startTimeOfDay")
    """Format hh:mm"""

    end_time_of_day = sgqlc.types.Field(String, graphql_name="endTimeOfDay")
    """Format hh:mm"""

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
    """The token for the user"""

    live_kit_room_url = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="liveKitRoomUrl"
    )
    """The URL of the LiveKit room"""

    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="name")
    """The name of the agent"""


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
    """Represents a subscription assigned to a customer, card, or charge
    station. Tracks validity, approvals, and linked product.
    """

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
    """Unique identifier of the subscription"""

    type = sgqlc.types.Field(String, graphql_name="type")
    """Type/category of this subscription (e.g., roaming, prepaid)"""

    approved = sgqlc.types.Field(Boolean, graphql_name="approved")
    """True if this subscription has been approved for use"""

    start_date = sgqlc.types.Field(String, graphql_name="startDate")
    """Start date of the subscription validity period"""

    end_date = sgqlc.types.Field(String, graphql_name="endDate")
    """End date of the subscription validity period"""

    product = sgqlc.types.Field("Product", graphql_name="product")
    """Subscription product associated with this subscription"""

    charge_station = sgqlc.types.Field(ChargeStation, graphql_name="chargeStation")
    """Charge station associated with this subscription, if any"""

    card = sgqlc.types.Field(Card, graphql_name="card")
    """Card assigned to this subscription for access or billing"""


class LmsTariff(sgqlc.types.Type):
    """A lightweight tariff object exposed by LMS. Note: This schema is
    incomplete; fields may expand in the future.
    """

    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    """Unique identifier of the LMS tariff."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Human-readable name of the tariff."""


class LmsTariffsResult(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "has_more")
    items = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null("Tariff"))),
        graphql_name="items",
    )

    has_more = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="hasMore")


class LmsTransaction(sgqlc.types.Type):
    """LMS (central system) transaction representation"""

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
    """Unique ID"""

    provider_transaction_id = sgqlc.types.Field(
        String, graphql_name="providerTransactionId"
    )
    """Provider-side transaction ID"""

    status = sgqlc.types.Field(
        sgqlc.types.non_null(TransactionStatus), graphql_name="status"
    )
    """Billing status"""

    global_status = sgqlc.types.Field(
        TransactionGlobalStatus, graphql_name="globalStatus"
    )
    """Global transaction status"""

    type = sgqlc.types.Field(TransactionType, graphql_name="type")
    """Transaction type"""

    start_date = sgqlc.types.Field(String, graphql_name="startDate")
    """Start date/time"""

    last_update_date = sgqlc.types.Field(String, graphql_name="lastUpdateDate")
    """Last update date/time"""

    remote_last_update_date = sgqlc.types.Field(
        String, graphql_name="remoteLastUpdateDate"
    )
    """Remote system last update"""

    creation_date = sgqlc.types.Field(String, graphql_name="creationDate")
    """Transaction creation date"""

    vehicle_full_date = sgqlc.types.Field(String, graphql_name="vehicleFullDate")
    """Vehicle-related timestamp"""

    total_energy = sgqlc.types.Field(Float, graphql_name="totalEnergy")
    """Total energy consumed"""

    total_duration = sgqlc.types.Field(Float, graphql_name="totalDuration")
    """Total charging duration"""

    total_idle_time = sgqlc.types.Field(Float, graphql_name="totalIdleTime")
    """Total idle duration"""

    profile_type = sgqlc.types.Field(TransactionProfileType, graphql_name="profileType")
    """Profile type"""

    msp_provider = sgqlc.types.Field("Provider", graphql_name="mspProvider")
    """MSP provider"""

    card_snapshot = sgqlc.types.Field("TransactionCard", graphql_name="cardSnapshot")
    """Card snapshot used in this transaction"""

    customer = sgqlc.types.Field(Customer, graphql_name="customer")
    """Customer involved"""

    customer_reference = sgqlc.types.Field(String, graphql_name="customerReference")
    """Customer reference identifier"""

    location_snapshot = sgqlc.types.Field(
        "TransactionLocation", graphql_name="locationSnapshot"
    )
    """Location snapshot"""

    home_charging = sgqlc.types.Field(Boolean, graphql_name="homeCharging")
    """True if home charging"""

    cpo_provider = sgqlc.types.Field("Provider", graphql_name="cpoProvider")
    """CPO provider"""

    charge_station = sgqlc.types.Field(ChargeStation, graphql_name="chargeStation")
    """Charge station associated"""

    cost_center_number_station = sgqlc.types.Field(
        String, graphql_name="costCenterNumberStation"
    )
    """Cost center number for station"""

    charge_station_owner_customer = sgqlc.types.Field(
        Customer, graphql_name="chargeStationOwnerCustomer"
    )
    """Customer who owns the charge station"""

    transaction_prices = sgqlc.types.Field(
        sgqlc.types.list_of("TransactionPrice"), graphql_name="transactionPrices"
    )
    """Transaction prices"""

    transaction_tariff_timeslots = sgqlc.types.Field(
        sgqlc.types.list_of("TariffTimeslot"), graphql_name="transactionTariffTimeslots"
    )
    """Tariff timeslots"""

    transaction_periods = sgqlc.types.Field(
        sgqlc.types.list_of("TransactionPeriod"), graphql_name="transactionPeriods"
    )
    """Periods of the transaction"""

    authorisation = sgqlc.types.Field(Authorisation, graphql_name="authorisation")
    """Authorisation info"""

    incoming_cdr_file = sgqlc.types.Field(String, graphql_name="incomingCdrFile")
    """Incoming CDR file path or reference"""

    parent = sgqlc.types.Field("LmsTransaction", graphql_name="parent")
    """Parent LMS transaction if this is a child"""


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
    """Unique identifier of the location."""

    ranking = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="ranking")

    country_code = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="countryCode"
    )

    latitude = sgqlc.types.Field(Float, graphql_name="latitude")
    """Latitude coordinate in decimal degrees."""

    longitude = sgqlc.types.Field(Float, graphql_name="longitude")
    """Longitude coordinate in decimal degrees."""

    party = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="party")

    name = sgqlc.types.Field(String, graphql_name="name")
    """Display name for the location (e.g. "Main Office Parking")."""

    type = sgqlc.types.Field(String, graphql_name="type")
    """Type of location (public, private, car park, etc)."""

    address = sgqlc.types.Field(String, graphql_name="address")
    """Street address of the location."""

    city = sgqlc.types.Field(String, graphql_name="city")
    """City or municipality of the location."""

    postal_code = sgqlc.types.Field(String, graphql_name="postalCode")
    """Postal or ZIP code of the location."""

    country = sgqlc.types.Field(String, graphql_name="country")
    """Country in which the location is situated (ISO code)."""

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
    """Full country details for the location (name, timezone, languages)."""

    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    """User group that manages or owns this location."""

    user_group_name = sgqlc.types.Field(String, graphql_name="userGroupName")
    """Name of the associated user group."""

    publish = sgqlc.types.Field(Boolean, graphql_name="publish")
    """Whether this location is published and visible to external users."""

    always_open = sgqlc.types.Field(Boolean, graphql_name="alwaysOpen")
    """True if the location is accessible 24/7."""

    time_zone = sgqlc.types.Field(String, graphql_name="timeZone")
    """IANA timezone identifier (e.g. "Europe/Amsterdam")."""

    charging_when_closed = sgqlc.types.Field(Boolean, graphql_name="chargingWhenClosed")
    """Indicates whether charging is possible even when the site is
    officially closed.
    """

    directions = sgqlc.types.Field(String, graphql_name="directions")
    """Extra navigation or parking instructions."""

    opening_hours_text = sgqlc.types.Field(String, graphql_name="openingHoursText")
    """Human-readable description of opening hours."""


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
    """True if 100% from regenerative sources. (CO2 and nuclear waste is
    zero)
    """

    energy_sources = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EnergySource)),
        graphql_name="energySources",
    )
    """Key-value pairs (enum + percentage) of energy sources of this
    location’s tariff
    """

    environ_impact = sgqlc.types.Field(
        sgqlc.types.list_of(sgqlc.types.non_null(EnvironmentalImpact)),
        graphql_name="environImpact",
    )
    """Key-value pairs (enum + percentage) of nuclear waste and CO2
    exhaust of this location’s tariff
    """

    supplier_name = sgqlc.types.Field(String, graphql_name="supplierName")
    """Name of the energy supplier, delivering the energy for this
    location or tariff
    """

    energy_product_name = sgqlc.types.Field(String, graphql_name="energyProductName")
    """Name of the energy suppliers product/tariff plan used at this
    location
    """


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
    """Describes a supported charger manufacturer and model."""

    __schema__ = schema
    __field_names__ = ("id", "vendor", "model", "is_external", "is_default")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    """Internal ID of the manufacturer record."""

    vendor = sgqlc.types.Field(String, graphql_name="vendor")
    """Vendor/manufacturer name (e.g. ABB, Alfen, Tesla)."""

    model = sgqlc.types.Field(String, graphql_name="model")
    """Charger model identifier (e.g. Wallbox Pulsar, Terra DC)."""

    is_external = sgqlc.types.Field(Boolean, graphql_name="isExternal")
    """Indicates whether this manufacturer is external to the platform
    (imported or third-party).
    """

    is_default = sgqlc.types.Field(Boolean, graphql_name="isDefault")
    """Marks this manufacturer/model as the default option in selection
    lists.
    """


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
    """Arguments:

    * `password` (`String!`)None
    * `email` (`String!`)None
    """

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
    """Update a customer token (charge card) by token ID. Returns a token
    response.

    Arguments:

    * `id` (`ID!`)None
    * `input` (`TokenUpdate`)None
    """

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
    """Block a customer token (charge card) by token ID, preventing
    usage. Returns a token response.

    Arguments:

    * `id` (`ID!`)None
    """

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
    """Unblock a previously blocked customer token (charge card) by token
    ID. Returns a token response.

    Arguments:

    * `id` (`ID!`)None
    """

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
    """Activate a customer token (charge card) by token ID. Returns a
    token response.

    Arguments:

    * `id` (`ID!`)None
    """

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
    """Add authorized card to a customer by external card visual number
    and customer ID. Returns a token response.

    Arguments:

    * `external_card_visual_number` (`String!`)None
    * `roaming_home_charging_enabled` (`Boolean`)None
    * `customer_id` (`ID`)None
    """

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
    """Add 50five card to a customer by external card visual number and
    customer ID. Returns a token response.

    Arguments:

    * `external_card_visual_number` (`String!`)None
    * `customer_id` (`ID`)None
    """

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
    """Remove a Home Charging Compensation (HCC) card from a customer by
    external card visual number and customer ID. Returns a boolean.

    Arguments:

    * `external_card_visual_number` (`String!`)None
    * `customer_id` (`ID`)None
    """

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
    """Deactivate a customer token (charge card) by card/token ID.
    Returns a token response.

    Arguments:

    * `id` (`ID!`)None
    """

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
    """Unlock a specific connector at a charge station channel by charge
    station ID and charge station channel ID. Returns a boolean.

    Arguments:

    * `charge_station_id` (`ID!`)None
    * `channel_id` (`ID!`)None
    """

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
    """Start a transaction at a given charge station and channel, using a
    card by charge station ID, charge station channel ID, and card ID.
    Returns a boolean.

    Arguments:

    * `charge_station_id` (`ID!`)None
    * `channel_id` (`ID!`)None
    * `card` (`String`)None
    """

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
    """Stop a transaction at a given charge station and channel by charge
    station ID and charge station channel ID. Returns a boolean.

    Arguments:

    * `charge_station_id` (`ID!`)None
    * `channel_id` (`ID!`)None
    """

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
    """Perform a soft reset on a charge station (non-disruptive restart)
    by charge station ID. Returns a boolean.

    Arguments:

    * `charge_station_id` (`ID!`)None
    """

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
    """Perform a hard reset on a charge station (full reboot) by charge
    station ID. Returns a boolean.

    Arguments:

    * `charge_station_id` (`ID!`)None
    """

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
    """Update the Home Charging Compensation (HCC) tariff for a customer
    station by tariff, charge station ID, and customer ID. Returns a
    boolean.

    Arguments:

    * `tariff` (`Float!`)None
    * `charge_station_id` (`ID!`)None
    * `customer_id` (`ID`)None
    """

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
    """Update customer details by customer ID and new customer data
    input. Returns a customer.

    Arguments:

    * `id` (`ID`)None
    * `input` (`UpdateCustomerInput`)None
    """

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
    """Update bank account for a customer by customer ID and bank account
    input. Returns a bank account.

    Arguments:

    * `customer_id` (`ID!`)None
    * `input` (`BankAccountInput!`)None
    """

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
    """Mark SRS onboarding as completed (or not) for a customer by
    customer ID and completed flag. Returns a boolean.

    Arguments:

    * `customer_id` (`ID`)None
    * `completed` (`Boolean!`)None
    """

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
    """Update access options (e.g. authorization mode, charge card) for a
    charge station by charge station ID and access options input.
    Returns access options.

    Arguments:

    * `charge_station_id` (`ID!`)None
    * `access_options` (`AccessOptionInput!`)None
    """

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
    """Set whether a charge station is public or private by charge
    station ID and public or private flag. Returns access options.

    Arguments:

    * `charge_station_id` (`ID!`)None
    * `public_or_private` (`PublicOrPrivate!`)None
    """

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
    """Toggle whether a charge station is published on public maps by
    charge station ID and publish on map flag. Returns access options.

    Arguments:

    * `charge_station_id` (`ID!`)None
    * `publish_on_map` (`Boolean!`)None
    """

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
    """Create a App Feature

    Arguments:

    * `app_id` (`String!`)None
    * `feature_key` (`String!`)None
    * `enabled` (`Boolean!`)None
    """

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
    """Update the feature availability for a app

    Arguments:

    * `app_id` (`String!`)None
    * `feature_key` (`String!`)None
    * `enabled` (`Boolean!`)None
    """

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
    """Delete a App Feature

    Arguments:

    * `app_id` (`String!`)None
    * `feature_key` (`String!`)None
    """

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
    """Create a Customer Feature

    Arguments:

    * `customer_id` (`String!`)None
    * `app_id` (`String!`)None
    * `feature_key` (`String!`)None
    * `enabled` (`Boolean!`)None
    """

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
    """Update the feature availability for a customer

    Arguments:

    * `customer_id` (`String!`)None
    * `app_id` (`String!`)None
    * `feature_key` (`String!`)None
    * `enabled` (`Boolean!`)None
    """

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
    """Delete a Customer Feature

    Arguments:

    * `customer_id` (`String!`)None
    * `app_id` (`String!`)None
    * `feature_key` (`String!`)None
    """

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
    """Generate a LiveKit token for a user

    Arguments:

    * `input` (`LiveKitTokenInput!`)None
    """

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
    """Activate or deactivate charging mode. Returns current charging
    mode.

    Arguments:

    * `chargepoint_id` (`ID!`)None
    * `charging_mode` (`ChargingMode!`)None
    """

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
    """Reset the cache of charge station parameters by charge station ID.
    Returns a boolean when done.

    Arguments:

    * `charge_station_id` (`ID!`)None
    """

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
    """Update a customer mandate using customer ID and input fields.
    Returns a customer mandate.

    Arguments:

    * `customer_id` (`ID!`)None
    * `input` (`CreateUpdateCustomerMandateInput`)None
    """

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
    """End a customer mandate using customer ID and input fields. Returns
    a boolean.

    Arguments:

    * `customer_id` (`ID!`)None
    * `input` (`EndCustomerMandateInput`)None
    """

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
    """Create a new customer mandate using customer ID and input fields.
    Returns a customer mandate.

    Arguments:

    * `customer_id` (`ID!`)None
    * `input` (`CreateUpdateCustomerMandateInput`)None
    """

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
    """End a customer BACS mandate using customer ID and input fields.
    Returns a boolean.

    Arguments:

    * `customer_id` (`ID!`)None
    * `input` (`EndCustomerBacsMandateInput`)None
    """

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
    """Create a new customer BACS mandate using customer ID and input
    fields. Returns a customer BACS mandate.

    Arguments:

    * `customer_id` (`ID!`)None
    * `input` (`CreateCustomerBacsMandateInput`)None
    """

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
    """Update a schedule. Returns all set schedules.

    Arguments:

    * `input` (`ScheduleUpdate!`)None
    """

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
    """Override any set schedule for a chargepoint. Returns a boolean
    indicating success.

    Arguments:

    * `chargepoint_id` (`ID!`)None
    """

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
    """Update a schedule in simple format. Define times as start/stop
    pairs, or boolean charge status for the entire day. Returns all
    set schedules.

    Arguments:

    * `input` (`ScheduleSimpleUpdate!`)None
    """

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
    """Delete a schedule. Returns all set schedules.

    Arguments:

    * `chargepoint_id` (`ID!`)None
    * `week_days` (`[Int]!`)None
    """

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
    """Update a schedule in complex (blocks) format. Returns all set
    schedules.

    Arguments:

    * `input` (`ScheduleComplexUpdate!`)None
    """

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
    """Activate or deactivate net balanced charging. Returns all set
    schedules. This will override any existing schedules.

    Arguments:

    * `chargepoint_id` (`ID!`)None
    * `enabled` (`Boolean!`)None
    """

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
    """Activate or deactivate net balanced charging. Returns the updated
    status. This will override any existing schedules.

    Arguments:

    * `chargepoint_id` (`ID!`)None
    * `enabled` (`Boolean!`)None
    """

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
    """Arguments:

    * `uid` (`String!`)None
    * `device_type` (`DeviceType!`)None
    * `push_notification_token` (`String`)None
    * `device_model_name` (`String`)None
    * `app_version` (`String`)None
    * `device_manufacturer` (`String`)None
    * `device_version` (`String`)None
    * `external_customer_id` (`String`)None
    * `external_usergroup_id` (`String`)None
    * `external_app_provider_id` (`String`)None
    """

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
    """Arguments:

    * `input` (`[BulkUpdateCpmsIdInput!]!`)None
    """

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
    """Arguments:

    * `input` (`CreateAIVoiceTicketInput!`)None
    """

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
    """Arguments:

    * `name` (`String!`)None
    * `email` (`String!`)None
    """

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
    """Arguments:

    * `partner_id` (`Int!`)None
    * `team_key` (`String!`)None
    * `name` (`String!`)None
    * `description` (`String!`)None
    * `xx_category_id` (`Int`)None
    * `xx_subcategory_id` (`Int`)None
    * `status` (`OdooTicketStatus`)None
    * `xx_source_id` (`Int`)None
    """

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
    """Arguments:

    * `user_id` (`Int!`)None
    * `template_name` (`String!`)None
    """

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
    """Arguments:

    * `ticket_id` (`Int!`)None
    * `name` (`String`)None
    * `description` (`String`)None
    * `comments` (`[String]`)None
    """

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
    """Arguments:

    * `input` (`CreateEreMandateTicketInput!`)None
    """


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
    """A reusable configuration of parameters applied to one or more
    charge stations. Parameter sets simplify management of station
    groups by bundling operational settings.
    """

    __schema__ = schema
    __field_names__ = (
        "id",
        "name",
        "connected_device_count",
        "is_default",
        "user_group",
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    """Unique identifier of the parameter set."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Human-readable name of the parameter set."""

    connected_device_count = sgqlc.types.Field(Int, graphql_name="connectedDeviceCount")
    """Number of devices currently using this parameter set."""

    is_default = sgqlc.types.Field(Boolean, graphql_name="isDefault")
    """Indicates if this is the default parameter set for new stations."""

    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    """User group associated with this parameter set (access rights,
    billing).
    """


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
    """Represents a natural person (e.g. customer, account owner, or
    user).
    """

    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Unique identifier of the person."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Full display name of the person (may include first and last name)."""


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
    """Represents a subscription product available for customers or
    charge stations. Contains all product metadata, billing, and usage
    details.
    """

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
    """Unique identifier of the subscription product"""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Human-readable name of the subscription product"""

    description = sgqlc.types.Field(String, graphql_name="description")
    """Detailed description of what the subscription product offers"""

    invoice_name = sgqlc.types.Field(String, graphql_name="invoiceName")
    """Name to be displayed on invoices for this product"""

    provider = sgqlc.types.Field("Provider", graphql_name="provider")
    """Provider offering this subscription product"""

    type = sgqlc.types.Field(ProductType, graphql_name="type")
    """Internal type/category of the subscription product"""

    usage_type = sgqlc.types.Field(ProductUsageType, graphql_name="usageType")
    """Defines how the product can be used (e.g., per session, per kWh,
    flat fee)
    """

    selection_mode = sgqlc.types.Field(
        ProductSelectionMode, graphql_name="selectionMode"
    )
    """How the product can be selected by users (e.g., automatic, manual)"""

    payment_mode = sgqlc.types.Field(ProductPaymentMode, graphql_name="paymentMode")
    """Payment method applicable for this product"""

    payment_period_mode = sgqlc.types.Field(
        ProductPaymentPeriodMode, graphql_name="paymentPeriodMode"
    )
    """Billing interval for the subscription product (e.g., monthly,
    yearly)
    """

    auto_approve = sgqlc.types.Field(Boolean, graphql_name="autoApprove")
    """If true, the subscription is automatically approved upon purchase"""

    owner_access = sgqlc.types.Field(Boolean, graphql_name="ownerAccess")
    """Indicates if the product can be accessed by the owner directly"""

    attach_customer_to_transaction = sgqlc.types.Field(
        Boolean, graphql_name="attachCustomerToTransaction"
    )
    """If true, associates the customer with the transaction
    automatically
    """

    sim_activated = sgqlc.types.Field(Boolean, graphql_name="simActivated")
    """True if a SIM card activation is required or has been completed"""

    network_types = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="networkTypes"
    )
    """List of network types (e.g., LTE, 5G) compatible with this product"""

    customer_types = sgqlc.types.Field(
        sgqlc.types.list_of(String), graphql_name="customerTypes"
    )
    """List of allowed customer types (e.g., PRIVATE, COMPANY) for this
    product
    """

    currency = sgqlc.types.Field(Currency, graphql_name="currency")
    """Currency in which this subscription product is billed"""

    items = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name="items")
    """IDs of individual items included in this subscription product"""


class Provider(sgqlc.types.Type):
    """Represents a charging service provider."""

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
    """Unique identifier of the provider."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Provider name (e.g. Shell Recharge, EVBox)."""

    category = sgqlc.types.Field(ProviderCategory, graphql_name="category")
    """Provider category (market/region grouping), e.g. DE, AT, CHF."""

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
    """Lists transactions for this provider. Specify one or more query
    parameters to filter the transaction that appear in the response.
    Each item in the list includes basic transaction details.  This
    API requires either a dateFrom, the invoice.id or, card.id and
    startDateFrom to be provided. If card.id is provided,
    startDateFrom is required. Use dateFrom and dateTo to define the
    range to filter results, based on lastUpdatedDate. Difference
    between dates is not allowed to exceed 1 month.

    Arguments:

    * `filters` (`TransactionFilter`)None
    * `sort` (`TransactionSort`)None
    """

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
    """Retrieve a paginated collection of invoices for this provider,
    with filtering and sorting options. Returns a collection of
    invoices.

    Arguments:

    * `page` (`Int`)None
    * `items_per_page` (`Int`)None
    * `filters` (`InvoiceFilter`)None
    * `sort` (`InvoiceSort`)None
    """

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
    """Retrieve a paginated and filterable list of user groups

    Arguments:

    * `filters` (`UserGroupFilter`)None
    """


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
    """Unique identifier for the push notification"""

    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="title")
    """Title of the push notification"""

    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="body")
    """Body of the push notification"""

    extended_body = sgqlc.types.Field(String, graphql_name="extendedBody")
    """Extended (HTML formatted) body of the push notification"""

    created_at = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="createdAt"
    )
    """Date and time the push notification was created in ISO 8601 format"""

    type = sgqlc.types.Field(PushNotificationType, graphql_name="type")
    """Type of the push notification"""


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
    """Arguments:

    * `id` (`String!`)None
    """

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
    """Arguments:

    * `filters` (`MapLocationsFiltersInput`)None
    * `bounds` (`LocationBoundsInput!`)None
    """

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
    """Arguments:

    * `id` (`String!`)None
    """

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
    """Arguments:

    * `filters` (`LocationsFiltersInput`)None
    * `sort` (`String!`)None
    * `end_result` (`Float!`)None
    * `start_result` (`Float!`)None
    * `radius` (`Float`)None
    * `ref_longitude` (`Float!`)None
    * `ref_latitude` (`Float!`)None
    """

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
    """Arguments:

    * `end_result` (`Float!`)None
    * `start_result` (`Float!`)None
    """

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
    """Arguments:

    * `id` (`String!`)None
    """

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
    """Arguments:

    * `id` (`String!`)None
    """

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
    """Arguments:

    * `ids` (`[ID!]!`)None
    """

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
    """Arguments:

    * `tariff_id` (`String!`)None
    * `vat` (`Float!`)None
    """

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
    """Arguments:

    * `connector_id` (`String!`)None
    * `evse_id` (`String!`)None
    * `location_id` (`String!`)None
    """

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
    """Arguments:

    * `end_result` (`Float!`)None
    * `start_result` (`Float!`)None
    """

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
    """Arguments:

    * `email` (`String!`)None
    """

    get_tokens = sgqlc.types.Field(
        sgqlc.types.list_of("TokenResponse"), graphql_name="getTokens"
    )
    """Retrieve all customer tokens (charge cards). Returns a collection
    of tokens.
    """

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
    """Retrieve one or more tokens by their unique token IDs. Returns a
    collection of tokens.

    Arguments:

    * `id` (`[ID]!`)None
    """

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
    """Retrieve tokens by their internal system token IDs. Returns a
    collection of tokens.

    Arguments:

    * `id` (`[ID]!`)None
    """

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
    """Retrieve tokens by their external token IDs (from external
    systems). Returns a collection of tokens.

    Arguments:

    * `id` (`[ID]!`)None
    """

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
    """Retrieve tokens by their contract token IDs. Returns a collection
    of tokens.

    Arguments:

    * `id` (`[ID]!`)None
    """

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
    """Retrieve roaming token by its internal token ID, external token
    ID, or contract ID. Returns roaming-specific card details.

    Arguments:

    * `internal_id` (`ID`)None
    * `external_id` (`ID`)None
    * `contract_id` (`ID`)None
    """

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
    """Retrieve charge stations with optional detailed filters and
    sorting. Returns a collection of charge stations.

    Arguments:

    * `filters` (`ChargeStationFilter`)None
    * `sort` (`ChargeStationSort`)None
    """

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
    """Retrieve charge stations by a list of IDs. Returns a collection of
    charge stations.

    Arguments:

    * `id` (`[ID]!`)None
    """

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
    """Retrieve a single charge station by charge station ID. Returns a
    charge station.

    Arguments:

    * `id` (`ID!`)None
    """

    get_customer_by_id = sgqlc.types.Field(
        Customer,
        graphql_name="getCustomerById",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(ID, graphql_name="id", default=None)),)
        ),
    )
    """Retrieve a customer by ID. Returns a customer.

    Arguments:

    * `id` (`ID`)None
    """

    get_customer_bank_accounts = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of(BankAccount)),
        graphql_name="getCustomerBankAccounts",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(ID, graphql_name="id", default=None)),)
        ),
    )
    """Retrieve all bank accounts associated with the specific customer
    ID. Returns a collection of bank accounts.

    Arguments:

    * `id` (`ID`)None
    """

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
    """Retrieve all charge stations owned by a specific customer ID.
    Returns a collection of charge stations.

    Arguments:

    * `customer_id` (`ID`)None
    """

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
    """Retrieve invoices with pagination, detailed filters, and sorting.
    Returns a collection of invoices.

    Arguments:

    * `page` (`Int`)None
    * `items_per_page` (`Int`)None
    * `filters` (`InvoiceFilter`)None
    * `sort` (`InvoiceSort`)None
    """

    get_invoice_by_id = sgqlc.types.Field(
        Invoice,
        graphql_name="getInvoiceById",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(ID, graphql_name="id", default=None)),)
        ),
    )
    """Retrieve a single invoice by invoice ID. Returns a invoice.

    Arguments:

    * `id` (`ID`)None
    """

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
    """Retrieve a specific charge station channel by charge station ID
    and  charge station channel ID. Returns a charge station channel.

    Arguments:

    * `charge_station_id` (`ID!`)None
    * `channel_id` (`ID!`)None
    """

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
    """Retrieve tickets with optional detailed filters and sorting.
    Returns a collection of tickets.

    Arguments:

    * `filters` (`TicketFilter`)None
    * `sort` (`TicketSort`)None
    """

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
    """Retrieve all app features by app identifier. Returns a collection
    of features.

    Arguments:

    * `app_id` (`String!`)None
    """

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
    """Retrieve all customer features by app identifier. Returns a
    collection of features.

    Arguments:

    * `customer_id` (`String!`)None
    * `app_id` (`String!`)None
    """

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
    """Retrieves whether HCC is allowed for the card.

    Arguments:

    * `id` (`ID!`)None
    """

    reimbursement_tariff_range = sgqlc.types.Field(
        "TariffRange", graphql_name="reimbursementTariffRange"
    )
    """Retrieves the range of tariffs allowed for reimbursement, if
    available
    """

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
    """Retrieve the solar charging availability of a charge station

    Arguments:

    * `charge_station_id` (`ID!`)None
    """

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
    """Retrieve the charging mode of a charge station

    Arguments:

    * `charge_station_id` (`ID!`)None
    """

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
    """Retrieve a currency by its code.

    Arguments:

    * `code` (`ID!`)None
    """

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
    """Retrieve a collection of currencies.

    Arguments:

    * `filters` (`CurrencyFilter`)None
    """

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
    """Retrieve a country by its code.

    Arguments:

    * `code` (`ID!`)None
    """

    get_countries = sgqlc.types.Field(CountryCollection, graphql_name="getCountries")
    """Retrieve a collection of countries."""

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
    """Retrieve a language by its code.

    Arguments:

    * `code` (`ID!`)None
    """

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
    """Retrieve a collection of languages.

    Arguments:

    * `filters` (`LanguageFilter`)None
    """

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
    """Retrieve a paginated and filterable list of charge cards with
    optional detailed filters and sorting. Returns a collection of
    charge cards.

    Arguments:

    * `filters` (`CardFilter`)None
    * `sort` (`CardSort`)None
    """

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
    """Lists transactions. All pagination keys (itemsPerPage, page) go in
    the filters object. Specify one or more query parameters to filter
    the transaction that appear in the response. Each item in the list
    includes basic transaction details.  This API requires either a
    dateFrom, the invoice.id or, card.id and startDateFrom to be
    provided. If card.id is provided, startDateFrom is required. Use
    dateFrom and dateTo to define the range to filter results, based
    on lastUpdatedDate. Difference between dates is not allowed to
    exceed 1 month.

    Arguments:

    * `filters` (`TransactionFilter`)None
    * `sort` (`TransactionSort`)None
    """

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
    """Get a transaction by ID

    Arguments:

    * `id` (`ID!`)None
    """

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
    """Retrieve a charge group by its unique identifier.

    Arguments:

    * `id` (`ID!`)None
    """

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
    """Retrieve charge groups across the entire system.   Supports
    filtering by ID, type, tariff, or user group, and sorting by
    multiple attributes.   Useful for listing available charging
    groups for admin portals, mobile apps, or roaming integrations.

    Arguments:

    * `filters` (`ChargeGroupFilter`)None
    * `sort` (`ChargeGroupSort`)None
    """

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
    """Retrieve a paginated and filterable list of user groups

    Arguments:

    * `filters` (`UserGroupFilter`)None
    """

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
    """Retrieve a user group by its unique identifier

    Arguments:

    * `id` (`ID!`)None
    """

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
    """Retrieve a paginated and filterable list of customers with
    optional detailed filters and sorting. Returns a collection of
    customers.

    Arguments:

    * `filters` (`CustomerFilter`)None
    * `sort` (`CustomerSort`)None
    """

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
    """Retrieve all chargestation schedules. Returns all set schedules.

    Arguments:

    * `chargepoint_id` (`ID!`)None
    """

    schedules_simple = sgqlc.types.Field(
        sgqlc.types.non_null(sgqlc.types.list_of("ScheduleSimple")),
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
    """Retrieve all chargestation schedules in a simplified format.
    Returns all set schedules.

    Arguments:

    * `chargepoint_id` (`ID!`)None
    """

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
    """Retrieve all chargestation schedules in a complex (blocks) format.
    Returns all set schedules.

    Arguments:

    * `chargepoint_id` (`ID!`)None
    """

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
    """Retrieve the net balanced charging status. Returns true if net
    balanced charging is active, false otherwise.

    Arguments:

    * `chargepoint_id` (`ID!`)None
    """

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
    """Arguments:

    * `uid` (`String!`)None
    """

    push_notifications = sgqlc.types.Field(
        sgqlc.types.list_of(PushNotification),
        graphql_name="pushNotifications",
        args=sgqlc.types.ArgDict(
            (("id", sgqlc.types.Arg(ID, graphql_name="id", default=None)),)
        ),
    )
    """List of push notifications. If ID is provided, returns
    notification for that ID

    Arguments:

    * `id` (`ID`)None
    """

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
    """Arguments:

    * `ticket_id` (`Int!`)None
    """

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
    """Arguments:

    * `partner_id` (`Int!`)None
    """

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
    """Arguments:

    * `ticket_id` (`Int!`)None
    """

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
    """Arguments:

    * `email` (`String!`)None
    """


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
    """A roaming profile defines how and where the card is allowed to
    roam across networks.
    """

    __schema__ = schema
    __field_names__ = ("id", "name")
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Unique identifier of the roaming profile."""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Display name of the roaming profile."""


class RoamingProfileHub(sgqlc.types.Type):
    """Roaming profile hub configuration, connecting this card to a
    roaming hub with a defined role.
    """

    __schema__ = schema
    __field_names__ = ("id", "role", "roaming_hub")
    id = sgqlc.types.Field(ID, graphql_name="id")
    """Unique identifier of the roaming profile hub configuration."""

    role = sgqlc.types.Field(RoamingRole, graphql_name="role")
    """Role this card plays in the roaming hub (e.g. MSP, CPO)."""

    roaming_hub = sgqlc.types.Field(RoamingProfile, graphql_name="roamingHub")
    """The roaming hub profile assigned to this card."""


class Schedule(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("weekday", "start_time", "stop_time")
    weekday = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="weekday")
    """The weekday, 1-7 being Monday-Sunday"""

    start_time = sgqlc.types.Field(
        sgqlc.types.non_null(String), graphql_name="startTime"
    )
    """The start time of the schedule in UTC"""

    stop_time = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name="stopTime")
    """The stop time of the schedule in UTC"""


class ScheduleBlock(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("block", "charge")
    block = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name="block")
    """The block number of the schedule (0-671)"""

    charge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name="charge")
    """The charge status of the schedule block"""


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
    """The weekday, 1-7 being Monday-Sunday"""

    times = sgqlc.types.Field(ChargeTimes, graphql_name="times")
    """The chargetimes of the schedule. Takes precedence over charge
    status.
    """

    charge = sgqlc.types.Field(Boolean, graphql_name="charge")
    """The charge status of weekday - either charge all day or not."""


class Tariff(sgqlc.types.Type):
    """Represents a pricing tariff for charging."""

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
    """Unique identifier of the tariff."""

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
    """Detailed tariff information including VAT."""

    __schema__ = schema
    __field_names__ = ("id", "energy", "flat", "parking_time", "time", "vat")
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name="id")
    """Unique identifier of the tariff."""

    energy = sgqlc.types.Field(Float, graphql_name="energy")

    flat = sgqlc.types.Field(Float, graphql_name="flat")

    parking_time = sgqlc.types.Field(Float, graphql_name="parkingTime")

    time = sgqlc.types.Field(Float, graphql_name="time")

    vat = sgqlc.types.Field(Float, graphql_name="vat")
    """Applicable VAT rate as a decimal (e.g. 0.21 for 21%)."""


class TariffTimeslot(sgqlc.types.Type):
    """Tariff timeslot grouping"""

    __schema__ = schema
    __field_names__ = ("timeslot_number", "items")
    timeslot_number = sgqlc.types.Field(Int, graphql_name="timeslotNumber")
    """Number of the timeslot"""

    items = sgqlc.types.Field(
        sgqlc.types.list_of("TariffTimeslotItem"), graphql_name="items"
    )
    """List of items for this timeslot"""


class TariffTimeslotItem(sgqlc.types.Type):
    """Tariff item within a timeslot"""

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
    """Type of tariff item"""

    start_price = sgqlc.types.Field(Float, graphql_name="startPrice")
    """Fixed start price"""

    energy_price = sgqlc.types.Field(Float, graphql_name="energyPrice")
    """Energy price"""

    minute_price = sgqlc.types.Field(Float, graphql_name="minutePrice")
    """Price per minute"""

    idle_minute_price = sgqlc.types.Field(Float, graphql_name="idleMinutePrice")
    """Idle price per minute"""

    source = sgqlc.types.Field(TransactionPeriodItemSource, graphql_name="source")
    """Source of the charge/cost"""

    additional_provider = sgqlc.types.Field(Provider, graphql_name="additionalProvider")
    """Provider responsible for additional charges"""

    vat_type = sgqlc.types.Field(InvoiceVatType, graphql_name="vatType")
    """VAT type for this tariff item"""


class Ticket(sgqlc.types.Type):
    """Represents a support ticket created for a customer, charge
    station, or user group
    """

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
    """Unique identifier of the support ticket"""

    sign_on_date = sgqlc.types.Field(String, graphql_name="signOnDate")
    """Date and time when the ticket was signed on/created"""

    last_action_date = sgqlc.types.Field(String, graphql_name="lastActionDate")
    """Date and time of the most recent action on this ticket"""

    creator = sgqlc.types.Field(String, graphql_name="creator")
    """Name or ID of the person who created the ticket"""

    creator_company = sgqlc.types.Field(String, graphql_name="creatorCompany")
    """Company of the creator, if applicable"""

    reported_by = sgqlc.types.Field(String, graphql_name="reportedBy")
    """Name of the individual who reported the issue"""

    customer = sgqlc.types.Field(Customer, graphql_name="customer")
    """Customer associated with the ticket"""

    customer_name = sgqlc.types.Field(String, graphql_name="customerName")
    """Name of the customer associated with the ticket"""

    user_group = sgqlc.types.Field("UserGroup", graphql_name="userGroup")
    """User group associated with the ticket"""

    status = sgqlc.types.Field(TicketStatus, graphql_name="status")
    """Current status of the ticket"""

    charge_station = sgqlc.types.Field(ChargeStation, graphql_name="chargeStation")
    """Charge station associated with the ticket"""

    charge_station_name = sgqlc.types.Field(String, graphql_name="chargeStationName")
    """Name of the charge station associated with the ticket"""

    type = sgqlc.types.Field(TicketType, graphql_name="type")
    """Type or category of the ticket"""

    source = sgqlc.types.Field(TicketSource, graphql_name="source")
    """Source/origin from which the ticket was submitted"""

    description = sgqlc.types.Field(String, graphql_name="description")
    """Detailed description of the ticket content"""

    extra_info = sgqlc.types.Field(String, graphql_name="extraInfo")
    """Additional information related to the ticket"""

    action_holder = sgqlc.types.Field(String, graphql_name="actionHolder")
    """Person currently responsible for taking action on the ticket"""

    action_taken = sgqlc.types.Field(String, graphql_name="actionTaken")
    """Description of the action taken on the ticket"""


class TicketCollection(sgqlc.types.Type):
    """Collection of support tickets with pagination information"""

    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(Ticket), graphql_name="items")
    """List of tickets returned in the collection"""

    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")
    """Total number of tickets available in the collection"""


class TokenResponse(sgqlc.types.Type):
    """Represents a token (RFID card, contract ID, or digital credential)
    used to authorize charging sessions.
    """

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
    """Unique identifier of the token."""

    owner_person = sgqlc.types.Field(Person, graphql_name="ownerPerson")
    """Person associated with this token."""

    transaction_customer = sgqlc.types.Field(
        Customer, graphql_name="transactionCustomer"
    )
    """Customer account linked to transactions made with this token."""

    customer = sgqlc.types.Field(Customer, graphql_name="customer")
    """Customer account owning this token."""

    product_customer = sgqlc.types.Field(Customer, graphql_name="productCustomer")
    """Customer responsible for the product this token is tied to."""

    usergroup_id = sgqlc.types.Field(ID, graphql_name="usergroupId")
    """ID of the user group associated with this token."""

    usergroup = sgqlc.types.Field("UserGroup", graphql_name="usergroup")
    """User group object associated with this token."""

    token_issuer_id = sgqlc.types.Field(Int, graphql_name="tokenIssuerId")
    """ID of the issuer that created this token."""

    expiry_date = sgqlc.types.Field(String, graphql_name="expiryDate")
    """Expiry date of the token (ISO8601 string)."""

    external_id = sgqlc.types.Field(String, graphql_name="externalId")
    """External identifier of the token (e.g. roaming reference)."""

    internal_id = sgqlc.types.Field(String, graphql_name="internalId")
    """Internal identifier of the token (platform-specific)."""

    info = sgqlc.types.Field(String, graphql_name="info")
    """Additional information or description for the token."""

    status = sgqlc.types.Field(String, graphql_name="status")
    """Current operational status of the token (e.g. Active, Blocked)."""

    roaming = sgqlc.types.Field(Boolean, graphql_name="roaming")
    """Whether the token can be used for roaming sessions."""

    payer_transactions = sgqlc.types.Field(Int, graphql_name="payerTransactions")
    """Number of transactions paid by this token."""

    payer_subscriptions = sgqlc.types.Field(Int, graphql_name="payerSubscriptions")
    """Number of subscriptions paid by this token."""

    reference = sgqlc.types.Field(String, graphql_name="reference")
    """Reference identifier for accounting or reporting."""

    remote_password = sgqlc.types.Field(String, graphql_name="remotePassword")
    """Remote password or credential tied to the token (if applicable)."""

    roaming_home_charging_enabled = sgqlc.types.Field(
        Boolean, graphql_name="roamingHomeChargingEnabled"
    )
    """Whether roaming can also be used for home charging sessions."""

    type = sgqlc.types.Field(String, graphql_name="type")
    """Type of token (RFID, remote, etc)."""

    global_ = sgqlc.types.Field(Boolean, graphql_name="global")
    """Whether the token is global (usable in multiple networks)."""

    contract_id = sgqlc.types.Field(String, graphql_name="contractId")
    """Contract ID tied to this token (e.g. EMI3 format)."""

    emi3_id = sgqlc.types.Field(String, graphql_name="emi3Id")
    """Deprecated: old EMI3 ID. Use contractId instead."""

    roaming_hub_status = sgqlc.types.Field(CardState, graphql_name="roamingHubStatus")
    """Current roaming state of the charge card. Will return inactive if
    the card is not found in the roaming network.
    """


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
    """Transaction card snapshot"""

    __schema__ = schema
    __field_names__ = ("internal_id", "external_id", "contract_id", "type", "is_global")
    internal_id = sgqlc.types.Field(String, graphql_name="internalId")
    """Internal system ID of the card"""

    external_id = sgqlc.types.Field(String, graphql_name="externalId")
    """External/third-party ID of the card"""

    contract_id = sgqlc.types.Field(String, graphql_name="contractId")
    """Contract ID associated with the card"""

    type = sgqlc.types.Field(CardType, graphql_name="type")
    """Type of card"""

    is_global = sgqlc.types.Field(Boolean, graphql_name="isGlobal")
    """True if card is usable globally"""


class TransactionCollection(sgqlc.types.Type):
    """Collection wrapper for transaction queries"""

    __schema__ = schema
    __field_names__ = ("items", "has_next")
    items = sgqlc.types.Field(sgqlc.types.list_of(LmsTransaction), graphql_name="items")
    """List of transactions in this collection"""

    has_next = sgqlc.types.Field(Boolean, graphql_name="hasNext")
    """True if there are more transactions to fetch"""


class TransactionLocation(sgqlc.types.Type):
    """Location snapshot for a transaction"""

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
    """Street address of the charge point"""

    city = sgqlc.types.Field(String, graphql_name="city")
    """City of the charge point"""

    country = sgqlc.types.Field(Country, graphql_name="country")
    """Country of the charge point"""

    postal_code = sgqlc.types.Field(String, graphql_name="postalCode")
    """Postal/zip code of the charge point"""

    charge_station_id = sgqlc.types.Field(ID, graphql_name="chargeStationId")
    """Associated charge station ID"""

    charge_station_name = sgqlc.types.Field(String, graphql_name="chargeStationName")
    """Charge station name"""

    timezone = sgqlc.types.Field(String, graphql_name="timezone")
    """Timezone of the charge point"""

    evse = sgqlc.types.Field("TransactionLocationEvse", graphql_name="evse")
    """EVSE information for this location"""


class TransactionLocationEvse(sgqlc.types.Type):
    """EVSE (Electric Vehicle Supply Equipment) snapshot for transaction"""

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
    """Internal ID of the EVSE"""

    channel_no = sgqlc.types.Field(Int, graphql_name="channelNo")
    """Channel number within the charge station"""

    meter_id = sgqlc.types.Field(String, graphql_name="meterId")
    """Meter ID associated with this EVSE"""

    obis_code = sgqlc.types.Field(String, graphql_name="obisCode")
    """OBIS code for energy metering"""

    power = sgqlc.types.Field(Int, graphql_name="power")
    """Maximum power of the EVSE in kW"""

    connector_type = sgqlc.types.Field(
        TransactionConnectorType, graphql_name="connectorType"
    )
    """Connector type of this EVSE"""

    connector_format = sgqlc.types.Field(
        TransactionConnectorFormat, graphql_name="connectorFormat"
    )
    """Connector format (socket/cable)"""

    current_type = sgqlc.types.Field(TransactionCurrentType, graphql_name="currentType")
    """Current type (AC/DC)"""


class TransactionPeriod(sgqlc.types.Type):
    """Period of a transaction, can contain multiple items"""

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
    """Unique ID of the period"""

    timeslot_number = sgqlc.types.Field(Int, graphql_name="timeslotNumber")
    """Timeslot number associated"""

    start_date = sgqlc.types.Field(String, graphql_name="startDate")
    """Start date/time of period"""

    end_date = sgqlc.types.Field(String, graphql_name="endDate")
    """End date/time of period"""

    remote_last_update_date = sgqlc.types.Field(
        String, graphql_name="remoteLastUpdateDate"
    )
    """Last remote update date"""

    energy_start = sgqlc.types.Field(Float, graphql_name="energyStart")
    """Energy at start of period"""

    energy_consumed = sgqlc.types.Field(Float, graphql_name="energyConsumed")
    """Energy consumed during period"""

    start_used = sgqlc.types.Field(Boolean, graphql_name="startUsed")
    """Flag indicating if period start was used"""

    duration_charging = sgqlc.types.Field(Int, graphql_name="durationCharging")
    """Charging duration in minutes"""

    duration_idle = sgqlc.types.Field(Int, graphql_name="durationIdle")
    """Idle duration in minutes"""

    period_items = sgqlc.types.Field(
        sgqlc.types.list_of("TransactionPeriodItem"), graphql_name="periodItems"
    )
    """List of period items"""


class TransactionPeriodItem(sgqlc.types.Type):
    """Individual transaction period item representing cost/revenue"""

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
    """Unique ID of the period item"""

    type = sgqlc.types.Field(TransactionPeriodItemType, graphql_name="type")
    """Type of period item"""

    start_cost = sgqlc.types.Field(Float, graphql_name="startCost")
    """Fixed start cost"""

    energy_cost = sgqlc.types.Field(Float, graphql_name="energyCost")
    """Energy-based cost"""

    minute_cost = sgqlc.types.Field(Float, graphql_name="minuteCost")
    """Minute-based cost"""

    idle_minute_cost = sgqlc.types.Field(Float, graphql_name="idleMinuteCost")
    """Idle minute cost"""

    total_cost = sgqlc.types.Field(Float, graphql_name="totalCost")
    """Total cost for this item"""

    source = sgqlc.types.Field(TransactionPeriodItemSource, graphql_name="source")
    """Source of this cost"""

    additional_provider = sgqlc.types.Field(Provider, graphql_name="additionalProvider")
    """Additional provider contributing to this item"""

    vat_type = sgqlc.types.Field(InvoiceVatType, graphql_name="vatType")
    """VAT type applied"""


class TransactionPrice(sgqlc.types.Type):
    """Pricing breakdown for a transaction"""

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
    """Type of price component"""

    start_cost = sgqlc.types.Field(Float, graphql_name="startCost")
    """Fixed start cost"""

    energy_cost = sgqlc.types.Field(Float, graphql_name="energyCost")
    """Energy consumed cost"""

    minute_cost = sgqlc.types.Field(Float, graphql_name="minuteCost")
    """Time-based cost per minute"""

    idle_minute_cost = sgqlc.types.Field(Float, graphql_name="idleMinuteCost")
    """Idle time cost per minute"""

    total_cost = sgqlc.types.Field(Float, graphql_name="totalCost")
    """Total aggregated cost"""

    vat_percentage = sgqlc.types.Field(Float, graphql_name="vatPercentage")
    """VAT percentage applied"""

    vat_type = sgqlc.types.Field(TransactionVatType, graphql_name="vatType")
    """VAT type applied"""

    vat_country = sgqlc.types.Field(Country, graphql_name="vatCountry")
    """Country for VAT calculation"""

    currency = sgqlc.types.Field(Currency, graphql_name="currency")
    """Currency of the price"""

    customer_currency = sgqlc.types.Field(Currency, graphql_name="customerCurrency")
    """Customer-specific currency"""

    exchange_rate = sgqlc.types.Field(Float, graphql_name="exchangeRate")
    """Exchange rate applied"""

    conversion_fee = sgqlc.types.Field(Float, graphql_name="conversionFee")
    """Conversion fee applied"""

    conversion_amount = sgqlc.types.Field(Float, graphql_name="conversionAmount")
    """Conversion amount applied"""

    customer = sgqlc.types.Field(Customer, graphql_name="customer")
    """Customer associated with this price"""

    provider = sgqlc.types.Field(Provider, graphql_name="provider")
    """Provider associated with this price"""

    roaming_profile = sgqlc.types.Field(String, graphql_name="roamingProfile")
    """Roaming profile applied"""

    billing_type = sgqlc.types.Field(TransactionBillingType, graphql_name="billingType")
    """Billing type for this transaction price"""

    invoice = sgqlc.types.Field(Invoice, graphql_name="invoice")
    """Invoice related to this price"""


class UserGroup(sgqlc.types.Type):
    """Represents a group of users within the system, associated with a
    provider and profiles
    """

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
    """Unique identifier for the user group"""

    name = sgqlc.types.Field(String, graphql_name="name")
    """Display name of the user group"""

    provider = sgqlc.types.Field(Provider, graphql_name="provider")
    """Provider that owns or manages this user group"""

    user_group_profile = sgqlc.types.Field(String, graphql_name="userGroupProfile")
    """Role or profile designation of the user group (for permissions or
    access)
    """

    default_app_profile = sgqlc.types.Field(String, graphql_name="defaultAppProfile")
    """Default app profile assigned when users in this group use the app"""

    full_path = sgqlc.types.Field(String, graphql_name="fullPath")
    """Full hierarchical path of the user group (e.g., 'Provider /
    Department / Team')
    """

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
    """List of charge cards associated with this user group with optional
    detailed filters and sorting. Returns a collection of charge
    cards.

    Arguments:

    * `filters` (`CardFilter`)None
    * `sort` (`CardSort`)None
    """

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
    """Retrieve a paginated collection of invoices for this user group,
    with filtering and sorting options. Returns a collection of
    invoices.

    Arguments:

    * `page` (`Int`)None
    * `items_per_page` (`Int`)None
    * `filters` (`InvoiceFilter`)None
    * `sort` (`InvoiceSort`)None
    """

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
    """Retrieve tickets associated with this user group, supporting
    filters and sorting. Returns a collection of tickets.

    Arguments:

    * `filters` (`TicketFilter`)None
    * `sort` (`TicketSort`)None
    """

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
    """Retrieve charge groups associated with this user group.   Allows
    filtering and sorting by group-level attributes such as tariffs,
    type, and name.

    Arguments:

    * `filters` (`ChargeGroupFilter`)None
    * `sort` (`ChargeGroupSort`)None
    """


class UserGroupCollection(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ("items", "total_items")
    items = sgqlc.types.Field(sgqlc.types.list_of(UserGroup), graphql_name="items")
    """List of user group items for the current page"""

    total_items = sgqlc.types.Field(Int, graphql_name="totalItems")
    """Total number of matching user groups across all pages"""


########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = None
