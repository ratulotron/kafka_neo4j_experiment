from __future__ import annotations

from pydantic import BaseModel, Field, model_validator
from typing import Any


class Model(BaseModel):
    class Config:
        populate_by_name = True
        use_enum_values = True

    @model_validator(mode="before")
    @classmethod
    def check_empty_string(cls, data: Any) -> Any:
        for key, value in data.items():
            if value == "":
                data[key] = None
        return data


class Registration(Model):
    initial_registration_date: str | None = Field(None, alias="Registration.InitialRegistrationDate")
    last_update_date: str | None = Field(None, alias="Registration.LastUpdateDate")
    registration_status: str | None = Field(None, alias="Registration.RegistrationStatus")
    next_renewal_date: str | None = Field(None, alias="Registration.NextRenewalDate")
    managing_lou: str | None = Field(None, alias="Registration.ManagingLOU")
    validation_sources: str | None = Field(None, alias="Registration.ValidationSources")
    validation_authority_validation_authority_id: str | None = Field(
        ..., alias="Registration.ValidationAuthority.ValidationAuthorityID"
    )
    validation_authority_other_validation_authority_id: str | None = Field(
        ..., alias="Registration.ValidationAuthority.OtherValidationAuthorityID"
    )
    validation_authority_validation_authority_entity_id: str | None = Field(
        ..., alias="Registration.ValidationAuthority.ValidationAuthorityEntityID"
    )
    other_validation_authorities_other_validation_authority1_validation_authority_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.1.ValidationAuthorityID",
    )
    other_validation_authorities_other_validation_authority1_other_validation_authority_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.1.OtherValidationAuthorityID",
    )
    other_validation_authorities_other_validation_authority1_validation_authority_entity_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.1.ValidationAuthorityEntityID",
    )
    other_validation_authorities_other_validation_authority2_validation_authority_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.2.ValidationAuthorityID",
    )
    other_validation_authorities_other_validation_authority2_other_validation_authority_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.2.OtherValidationAuthorityID",
    )
    other_validation_authorities_other_validation_authority2_validation_authority_entity_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.2.ValidationAuthorityEntityID",
    )
    other_validation_authorities_other_validation_authority3_validation_authority_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.3.ValidationAuthorityID",
    )
    other_validation_authorities_other_validation_authority3_other_validation_authority_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.3.OtherValidationAuthorityID",
    )
    other_validation_authorities_other_validation_authority3_validation_authority_entity_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.3.ValidationAuthorityEntityID",
    )
    other_validation_authorities_other_validation_authority4_validation_authority_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.4.ValidationAuthorityID",
    )
    other_validation_authorities_other_validation_authority4_other_validation_authority_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.4.OtherValidationAuthorityID",
    )
    other_validation_authorities_other_validation_authority4_validation_authority_entity_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.4.ValidationAuthorityEntityID",
    )
    other_validation_authorities_other_validation_authority5_validation_authority_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.5.ValidationAuthorityID",
    )
    other_validation_authorities_other_validation_authority5_other_validation_authority_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.5.OtherValidationAuthorityID",
    )
    other_validation_authorities_other_validation_authority5_validation_authority_entity_id: str | None = Field(
        ...,
        alias="Registration.OtherValidationAuthorities.OtherValidationAuthority.5.ValidationAuthorityEntityID",
    )


class Names(Model):
    entity_legal_name: str | None = Field(None, alias="Entity.LegalName")
    entity_legal_name_xmllang: str | None = Field(None, alias="Entity.LegalName.xmllang")
    entity_other_entity_names_other_entity_name1: str | None = Field(
        None, alias="Entity.OtherEntityNames.OtherEntityName.1"
    )
    entity_other_entity_names_other_entity_name1_xmllang: str | None = Field(
        ..., alias="Entity.OtherEntityNames.OtherEntityName.1.xmllang"
    )
    entity_other_entity_names_other_entity_name1_type: str | None = Field(
        ..., alias="Entity.OtherEntityNames.OtherEntityName.1.type"
    )
    entity_other_entity_names_other_entity_name2: str | None = Field(
        None, alias="Entity.OtherEntityNames.OtherEntityName.2"
    )
    entity_other_entity_names_other_entity_name2_xmllang: str | None = Field(
        ..., alias="Entity.OtherEntityNames.OtherEntityName.2.xmllang"
    )
    entity_other_entity_names_other_entity_name2_type: str | None = Field(
        ..., alias="Entity.OtherEntityNames.OtherEntityName.2.type"
    )
    entity_other_entity_names_other_entity_name3: str | None = Field(
        None, alias="Entity.OtherEntityNames.OtherEntityName.3"
    )
    entity_other_entity_names_other_entity_name3_xmllang: str | None = Field(
        ..., alias="Entity.OtherEntityNames.OtherEntityName.3.xmllang"
    )
    entity_other_entity_names_other_entity_name3_type: str | None = Field(
        ..., alias="Entity.OtherEntityNames.OtherEntityName.3.type"
    )
    entity_other_entity_names_other_entity_name4: str | None = Field(
        None, alias="Entity.OtherEntityNames.OtherEntityName.4"
    )
    entity_other_entity_names_other_entity_name4_xmllang: str | None = Field(
        ..., alias="Entity.OtherEntityNames.OtherEntityName.4.xmllang"
    )
    entity_other_entity_names_other_entity_name4_type: str | None = Field(
        ..., alias="Entity.OtherEntityNames.OtherEntityName.4.type"
    )
    entity_other_entity_names_other_entity_name5: str | None = Field(
        None, alias="Entity.OtherEntityNames.OtherEntityName.5"
    )
    entity_other_entity_names_other_entity_name5_xmllang: str | None = Field(
        ..., alias="Entity.OtherEntityNames.OtherEntityName.5.xmllang"
    )
    entity_other_entity_names_other_entity_name5_type: str | None = Field(
        ..., alias="Entity.OtherEntityNames.OtherEntityName.5.type"
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name1: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.1"),
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name1_xmllang: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.1.xmllang",
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name1_type: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.1.type"),
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name2: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.2"),
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name2_xmllang: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.2.xmllang",
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name2_type: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.2.type"),
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name3: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.3"),
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name3_xmllang: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.3.xmllang",
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name3_type: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.3.type"),
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name4: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.4"),
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name4_xmllang: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.4.xmllang",
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name4_type: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.4.type"),
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name5: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.5"),
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name5_xmllang: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.5.xmllang",
    )
    entity_transliterated_other_entity_names_transliterated_other_entity_name5_type: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherEntityNames.TransliteratedOtherEntityName.5.type"),
    )


class Addresses(Model):
    entity_legal_address_xmllang: str | None = Field(None, alias="Entity.LegalAddress.xmllang")
    entity_legal_address_first_address_line: str | None = Field(None, alias="Entity.LegalAddress.FirstAddressLine")
    entity_legal_address_address_number: str | None = Field(None, alias="Entity.LegalAddress.AddressNumber")
    entity_legal_address_address_number_within_building: str | None = Field(
        ..., alias="Entity.LegalAddress.AddressNumberWithinBuilding"
    )
    entity_legal_address_mail_routing: str | None = Field(None, alias="Entity.LegalAddress.MailRouting")
    entity_legal_address_additional_address_line1: str | None = Field(
        None, alias="Entity.LegalAddress.AdditionalAddressLine.1"
    )
    entity_legal_address_additional_address_line2: str | None = Field(
        None, alias="Entity.LegalAddress.AdditionalAddressLine.2"
    )
    entity_legal_address_additional_address_line3: str | None = Field(
        None, alias="Entity.LegalAddress.AdditionalAddressLine.3"
    )
    entity_legal_address_city: str | None = Field(None, alias="Entity.LegalAddress.City")
    entity_legal_address_region: str | None = Field(None, alias="Entity.LegalAddress.Region")
    entity_legal_address_country: str | None = Field(None, alias="Entity.LegalAddress.Country")
    entity_legal_address_postal_code: str | None = Field(None, alias="Entity.LegalAddress.PostalCode")
    entity_headquarters_address_xmllang: str | None = Field(None, alias="Entity.HeadquartersAddress.xmllang")
    entity_headquarters_address_first_address_line: str | None = Field(
        ..., alias="Entity.HeadquartersAddress.FirstAddressLine"
    )
    entity_headquarters_address_address_number: str | None = Field(
        None, alias="Entity.HeadquartersAddress.AddressNumber"
    )
    entity_headquarters_address_address_number_within_building: str | None = Field(
        ..., alias="Entity.HeadquartersAddress.AddressNumberWithinBuilding"
    )
    entity_headquarters_address_mail_routing: str | None = Field(None, alias="Entity.HeadquartersAddress.MailRouting")
    entity_headquarters_address_additional_address_line1: str | None = Field(
        ..., alias="Entity.HeadquartersAddress.AdditionalAddressLine.1"
    )
    entity_headquarters_address_additional_address_line2: str | None = Field(
        ..., alias="Entity.HeadquartersAddress.AdditionalAddressLine.2"
    )
    entity_headquarters_address_additional_address_line3: str | None = Field(
        ..., alias="Entity.HeadquartersAddress.AdditionalAddressLine.3"
    )
    entity_headquarters_address_city: str | None = Field(None, alias="Entity.HeadquartersAddress.City")
    entity_headquarters_address_region: str | None = Field(None, alias="Entity.HeadquartersAddress.Region")
    entity_headquarters_address_country: str | None = Field(None, alias="Entity.HeadquartersAddress.Country")
    entity_headquarters_address_postal_code: str | None = Field(None, alias="Entity.HeadquartersAddress.PostalCode")
    entity_other_addresses_other_address1_xmllang: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.1.xmllang"
    )
    entity_other_addresses_other_address1_type: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.1.type"
    )
    entity_other_addresses_other_address1_first_address_line: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.1.FirstAddressLine"
    )
    entity_other_addresses_other_address1_address_number: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.1.AddressNumber"
    )
    entity_other_addresses_other_address1_address_number_within_building: str | None = Field(
        ...,
        alias="Entity.OtherAddresses.OtherAddress.1.AddressNumberWithinBuilding",
    )
    entity_other_addresses_other_address1_mail_routing: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.1.MailRouting"
    )
    entity_other_addresses_other_address1_additional_address_line1: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.1.AdditionalAddressLine.1"
    )
    entity_other_addresses_other_address1_additional_address_line2: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.1.AdditionalAddressLine.2"
    )
    entity_other_addresses_other_address1_additional_address_line3: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.1.AdditionalAddressLine.3"
    )
    entity_other_addresses_other_address1_city: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.1.City"
    )
    entity_other_addresses_other_address1_region: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.1.Region"
    )
    entity_other_addresses_other_address1_country: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.1.Country"
    )
    entity_other_addresses_other_address1_postal_code: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.1.PostalCode"
    )
    entity_other_addresses_other_address2_xmllang: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.2.xmllang"
    )
    entity_other_addresses_other_address2_type: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.2.type"
    )
    entity_other_addresses_other_address2_first_address_line: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.2.FirstAddressLine"
    )
    entity_other_addresses_other_address2_address_number: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.2.AddressNumber"
    )
    entity_other_addresses_other_address2_address_number_within_building: str | None = Field(
        ...,
        alias="Entity.OtherAddresses.OtherAddress.2.AddressNumberWithinBuilding",
    )
    entity_other_addresses_other_address2_mail_routing: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.2.MailRouting"
    )
    entity_other_addresses_other_address2_additional_address_line1: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.2.AdditionalAddressLine.1"
    )
    entity_other_addresses_other_address2_additional_address_line2: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.2.AdditionalAddressLine.2"
    )
    entity_other_addresses_other_address2_additional_address_line3: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.2.AdditionalAddressLine.3"
    )
    entity_other_addresses_other_address2_city: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.2.City"
    )
    entity_other_addresses_other_address2_region: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.2.Region"
    )
    entity_other_addresses_other_address2_country: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.2.Country"
    )
    entity_other_addresses_other_address2_postal_code: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.2.PostalCode"
    )
    entity_other_addresses_other_address3_xmllang: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.3.xmllang"
    )
    entity_other_addresses_other_address3_type: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.3.type"
    )
    entity_other_addresses_other_address3_first_address_line: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.3.FirstAddressLine"
    )
    entity_other_addresses_other_address3_address_number: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.3.AddressNumber"
    )
    entity_other_addresses_other_address3_address_number_within_building: str | None = Field(
        ...,
        alias="Entity.OtherAddresses.OtherAddress.3.AddressNumberWithinBuilding",
    )
    entity_other_addresses_other_address3_mail_routing: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.3.MailRouting"
    )
    entity_other_addresses_other_address3_additional_address_line1: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.3.AdditionalAddressLine.1"
    )
    entity_other_addresses_other_address3_additional_address_line2: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.3.AdditionalAddressLine.2"
    )
    entity_other_addresses_other_address3_additional_address_line3: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.3.AdditionalAddressLine.3"
    )
    entity_other_addresses_other_address3_city: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.3.City"
    )
    entity_other_addresses_other_address3_region: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.3.Region"
    )
    entity_other_addresses_other_address3_country: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.3.Country"
    )
    entity_other_addresses_other_address3_postal_code: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.3.PostalCode"
    )
    entity_other_addresses_other_address4_xmllang: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.4.xmllang"
    )
    entity_other_addresses_other_address4_type: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.4.type"
    )
    entity_other_addresses_other_address4_first_address_line: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.4.FirstAddressLine"
    )
    entity_other_addresses_other_address4_address_number: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.4.AddressNumber"
    )
    entity_other_addresses_other_address4_address_number_within_building: str | None = Field(
        ...,
        alias="Entity.OtherAddresses.OtherAddress.4.AddressNumberWithinBuilding",
    )
    entity_other_addresses_other_address4_mail_routing: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.4.MailRouting"
    )
    entity_other_addresses_other_address4_additional_address_line1: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.4.AdditionalAddressLine.1"
    )
    entity_other_addresses_other_address4_additional_address_line2: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.4.AdditionalAddressLine.2"
    )
    entity_other_addresses_other_address4_additional_address_line3: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.4.AdditionalAddressLine.3"
    )
    entity_other_addresses_other_address4_city: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.4.City"
    )
    entity_other_addresses_other_address4_region: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.4.Region"
    )
    entity_other_addresses_other_address4_country: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.4.Country"
    )
    entity_other_addresses_other_address4_postal_code: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.4.PostalCode"
    )
    entity_other_addresses_other_address5_xmllang: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.5.xmllang"
    )
    entity_other_addresses_other_address5_type: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.5.type"
    )
    entity_other_addresses_other_address5_first_address_line: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.5.FirstAddressLine"
    )
    entity_other_addresses_other_address5_address_number: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.5.AddressNumber"
    )
    entity_other_addresses_other_address5_address_number_within_building: str | None = Field(
        ...,
        alias="Entity.OtherAddresses.OtherAddress.5.AddressNumberWithinBuilding",
    )
    entity_other_addresses_other_address5_mail_routing: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.5.MailRouting"
    )
    entity_other_addresses_other_address5_additional_address_line1: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.5.AdditionalAddressLine.1"
    )
    entity_other_addresses_other_address5_additional_address_line2: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.5.AdditionalAddressLine.2"
    )
    entity_other_addresses_other_address5_additional_address_line3: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.5.AdditionalAddressLine.3"
    )
    entity_other_addresses_other_address5_city: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.5.City"
    )
    entity_other_addresses_other_address5_region: str | None = Field(
        None, alias="Entity.OtherAddresses.OtherAddress.5.Region"
    )
    entity_other_addresses_other_address5_country: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.5.Country"
    )
    entity_other_addresses_other_address5_postal_code: str | None = Field(
        ..., alias="Entity.OtherAddresses.OtherAddress.5.PostalCode"
    )
    entity_transliterated_other_addresses_transliterated_other_address1_xmllang: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.xmllang"),
    )
    entity_transliterated_other_addresses_transliterated_other_address1_type: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.type"),
    )
    entity_transliterated_other_addresses_transliterated_other_address1_first_address_line: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.FirstAddressLine",
    )
    entity_transliterated_other_addresses_transliterated_other_address1_address_number: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.AddressNumber",
    )
    entity_transliterated_other_addresses_transliterated_other_address1_address_number_within_building: str | None = (
        Field(
            ...,
            alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.AddressNumberWithinBuilding",
        )
    )
    entity_transliterated_other_addresses_transliterated_other_address1_mail_routing: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.MailRouting",
    )
    entity_transliterated_other_addresses_transliterated_other_address1_additional_address_line1: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.AdditionalAddressLine.1",
    )
    entity_transliterated_other_addresses_transliterated_other_address1_additional_address_line2: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.AdditionalAddressLine.2",
    )
    entity_transliterated_other_addresses_transliterated_other_address1_additional_address_line3: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.AdditionalAddressLine.3",
    )
    entity_transliterated_other_addresses_transliterated_other_address1_city: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.City"),
    )
    entity_transliterated_other_addresses_transliterated_other_address1_region: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.Region",
    )
    entity_transliterated_other_addresses_transliterated_other_address1_country: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.Country"),
    )
    entity_transliterated_other_addresses_transliterated_other_address1_postal_code: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.1.PostalCode",
    )
    entity_transliterated_other_addresses_transliterated_other_address2_xmllang: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.xmllang"),
    )
    entity_transliterated_other_addresses_transliterated_other_address2_type: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.type"),
    )
    entity_transliterated_other_addresses_transliterated_other_address2_first_address_line: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.FirstAddressLine",
    )
    entity_transliterated_other_addresses_transliterated_other_address2_address_number: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.AddressNumber",
    )
    entity_transliterated_other_addresses_transliterated_other_address2_address_number_within_building: str | None = (
        Field(
            ...,
            alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.AddressNumberWithinBuilding",
        )
    )
    entity_transliterated_other_addresses_transliterated_other_address2_mail_routing: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.MailRouting",
    )
    entity_transliterated_other_addresses_transliterated_other_address2_additional_address_line1: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.AdditionalAddressLine.1",
    )
    entity_transliterated_other_addresses_transliterated_other_address2_additional_address_line2: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.AdditionalAddressLine.2",
    )
    entity_transliterated_other_addresses_transliterated_other_address2_additional_address_line3: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.AdditionalAddressLine.3",
    )
    entity_transliterated_other_addresses_transliterated_other_address2_city: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.City"),
    )
    entity_transliterated_other_addresses_transliterated_other_address2_region: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.Region",
    )
    entity_transliterated_other_addresses_transliterated_other_address2_country: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.Country"),
    )
    entity_transliterated_other_addresses_transliterated_other_address2_postal_code: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.2.PostalCode",
    )
    entity_transliterated_other_addresses_transliterated_other_address3_xmllang: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.xmllang"),
    )
    entity_transliterated_other_addresses_transliterated_other_address3_type: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.type"),
    )
    entity_transliterated_other_addresses_transliterated_other_address3_first_address_line: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.FirstAddressLine",
    )
    entity_transliterated_other_addresses_transliterated_other_address3_address_number: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.AddressNumber",
    )
    entity_transliterated_other_addresses_transliterated_other_address3_address_number_within_building: str | None = (
        Field(
            ...,
            alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.AddressNumberWithinBuilding",
        )
    )
    entity_transliterated_other_addresses_transliterated_other_address3_mail_routing: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.MailRouting",
    )
    entity_transliterated_other_addresses_transliterated_other_address3_additional_address_line1: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.AdditionalAddressLine.1",
    )
    entity_transliterated_other_addresses_transliterated_other_address3_additional_address_line2: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.AdditionalAddressLine.2",
    )
    entity_transliterated_other_addresses_transliterated_other_address3_additional_address_line3: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.AdditionalAddressLine.3",
    )
    entity_transliterated_other_addresses_transliterated_other_address3_city: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.City"),
    )
    entity_transliterated_other_addresses_transliterated_other_address3_region: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.Region",
    )
    entity_transliterated_other_addresses_transliterated_other_address3_country: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.Country"),
    )
    entity_transliterated_other_addresses_transliterated_other_address3_postal_code: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.3.PostalCode",
    )
    entity_transliterated_other_addresses_transliterated_other_address4_xmllang: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.xmllang"),
    )
    entity_transliterated_other_addresses_transliterated_other_address4_type: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.type"),
    )
    entity_transliterated_other_addresses_transliterated_other_address4_first_address_line: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.FirstAddressLine",
    )
    entity_transliterated_other_addresses_transliterated_other_address4_address_number: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.AddressNumber",
    )
    entity_transliterated_other_addresses_transliterated_other_address4_address_number_within_building: str | None = (
        Field(
            ...,
            alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.AddressNumberWithinBuilding",
        )
    )
    entity_transliterated_other_addresses_transliterated_other_address4_mail_routing: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.MailRouting",
    )
    entity_transliterated_other_addresses_transliterated_other_address4_additional_address_line1: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.AdditionalAddressLine.1",
    )
    entity_transliterated_other_addresses_transliterated_other_address4_additional_address_line2: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.AdditionalAddressLine.2",
    )
    entity_transliterated_other_addresses_transliterated_other_address4_additional_address_line3: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.AdditionalAddressLine.3",
    )
    entity_transliterated_other_addresses_transliterated_other_address4_city: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.City"),
    )
    entity_transliterated_other_addresses_transliterated_other_address4_region: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.Region",
    )
    entity_transliterated_other_addresses_transliterated_other_address4_country: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.Country"),
    )
    entity_transliterated_other_addresses_transliterated_other_address4_postal_code: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.4.PostalCode",
    )
    entity_transliterated_other_addresses_transliterated_other_address5_xmllang: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.xmllang"),
    )
    entity_transliterated_other_addresses_transliterated_other_address5_type: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.type"),
    )
    entity_transliterated_other_addresses_transliterated_other_address5_first_address_line: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.FirstAddressLine",
    )
    entity_transliterated_other_addresses_transliterated_other_address5_address_number: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.AddressNumber",
    )
    entity_transliterated_other_addresses_transliterated_other_address5_address_number_within_building: str | None = (
        Field(
            ...,
            alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.AddressNumberWithinBuilding",
        )
    )
    entity_transliterated_other_addresses_transliterated_other_address5_mail_routing: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.MailRouting",
    )
    entity_transliterated_other_addresses_transliterated_other_address5_additional_address_line1: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.AdditionalAddressLine.1",
    )
    entity_transliterated_other_addresses_transliterated_other_address5_additional_address_line2: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.AdditionalAddressLine.2",
    )
    entity_transliterated_other_addresses_transliterated_other_address5_additional_address_line3: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.AdditionalAddressLine.3",
    )
    entity_transliterated_other_addresses_transliterated_other_address5_city: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.City"),
    )
    entity_transliterated_other_addresses_transliterated_other_address5_region: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.Region",
    )
    entity_transliterated_other_addresses_transliterated_other_address5_country: str | None = Field(
        ...,
        alias=("Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.Country"),
    )
    entity_transliterated_other_addresses_transliterated_other_address5_postal_code: str | None = Field(
        ...,
        alias="Entity.TransliteratedOtherAddresses.TransliteratedOtherAddress.5.PostalCode",
    )


class Successor(Model):
    entity_successor_entity1_successor_lei: str | None = Field(None, alias="Entity.SuccessorEntity.1.SuccessorLEI")
    entity_successor_entity1_successor_entity_name: str | None = Field(
        ..., alias="Entity.SuccessorEntity.1.SuccessorEntityName"
    )
    entity_successor_entity1_successor_entity_xmllang: str | None = Field(
        ..., alias="Entity.SuccessorEntity.1.SuccessorEntity.xmllang"
    )
    entity_successor_entity2_successor_lei: str | None = Field(None, alias="Entity.SuccessorEntity.2.SuccessorLEI")
    entity_successor_entity2_successor_entity_name: str | None = Field(
        ..., alias="Entity.SuccessorEntity.2.SuccessorEntityName"
    )
    entity_successor_entity2_successor_entity_xmllang: str | None = Field(
        ..., alias="Entity.SuccessorEntity.2.SuccessorEntity.xmllang"
    )
    entity_successor_entity3_successor_lei: str | None = Field(None, alias="Entity.SuccessorEntity.3.SuccessorLEI")
    entity_successor_entity3_successor_entity_name: str | None = Field(
        ..., alias="Entity.SuccessorEntity.3.SuccessorEntityName"
    )
    entity_successor_entity3_successor_entity_xmllang: str | None = Field(
        ..., alias="Entity.SuccessorEntity.3.SuccessorEntity.xmllang"
    )
    entity_successor_entity4_successor_lei: str | None = Field(None, alias="Entity.SuccessorEntity.4.SuccessorLEI")
    entity_successor_entity4_successor_entity_name: str | None = Field(
        ..., alias="Entity.SuccessorEntity.4.SuccessorEntityName"
    )
    entity_successor_entity4_successor_entity_xmllang: str | None = Field(
        ..., alias="Entity.SuccessorEntity.4.SuccessorEntity.xmllang"
    )
    entity_successor_entity5_successor_lei: str | None = Field(None, alias="Entity.SuccessorEntity.5.SuccessorLEI")
    entity_successor_entity5_successor_entity_name: str | None = Field(
        ..., alias="Entity.SuccessorEntity.5.SuccessorEntityName"
    )
    entity_successor_entity5_successor_entity_xmllang: str | None = Field(
        ..., alias="Entity.SuccessorEntity.5.SuccessorEntity.xmllang"
    )


class LegalEntityEvents(Model):
    entity_legal_entity_events_legal_entity_event1_group_type: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.1.group_type"
    )
    entity_legal_entity_events_legal_entity_event1_event_status: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.1.event_status"
    )
    entity_legal_entity_events_legal_entity_event1_group_id: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.1.group_id"
    )
    entity_legal_entity_events_legal_entity_event1_group_sequence_no: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.1.group_sequence_no"
    )
    entity_legal_entity_events_legal_entity_event1_legal_entity_event_type: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.1.LegalEntityEventType"
    )
    entity_legal_entity_events_legal_entity_event1_legal_entity_event_effective_date: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.1.LegalEntityEventEffectiveDate"),
    )
    entity_legal_entity_events_legal_entity_event1_legal_entity_event_recorded_date: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.1.LegalEntityEventRecordedDate"),
    )
    entity_legal_entity_events_legal_entity_event1_validation_documents: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.1.ValidationDocuments"
    )
    entity_legal_entity_events_legal_entity_event1_validation_reference: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.1.ValidationReference"
    )
    entity_legal_entity_events_legal_entity_event1_affected_fields1_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.1.AffectedFields.1.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event1_affected_fields1_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.1.AffectedFields.1.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event1_affected_fields2_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.1.AffectedFields.2.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event1_affected_fields2_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.1.AffectedFields.2.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event1_affected_fields3_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.1.AffectedFields.3.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event1_affected_fields3_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.1.AffectedFields.3.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event1_affected_fields4_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.1.AffectedFields.4.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event1_affected_fields4_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.1.AffectedFields.4.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event1_affected_fields5_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.1.AffectedFields.5.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event1_affected_fields5_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.1.AffectedFields.5.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event2_group_type: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.2.group_type"
    )
    entity_legal_entity_events_legal_entity_event2_event_status: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.2.event_status"
    )
    entity_legal_entity_events_legal_entity_event2_group_id: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.2.group_id"
    )
    entity_legal_entity_events_legal_entity_event2_group_sequence_no: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.2.group_sequence_no"
    )
    entity_legal_entity_events_legal_entity_event2_legal_entity_event_type: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.2.LegalEntityEventType"
    )
    entity_legal_entity_events_legal_entity_event2_legal_entity_event_effective_date: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.2.LegalEntityEventEffectiveDate"),
    )
    entity_legal_entity_events_legal_entity_event2_legal_entity_event_recorded_date: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.2.LegalEntityEventRecordedDate"),
    )
    entity_legal_entity_events_legal_entity_event2_validation_documents: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.2.ValidationDocuments"
    )
    entity_legal_entity_events_legal_entity_event2_validation_reference: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.2.ValidationReference"
    )
    entity_legal_entity_events_legal_entity_event2_affected_fields1_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.2.AffectedFields.1.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event2_affected_fields1_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.2.AffectedFields.1.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event2_affected_fields2_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.2.AffectedFields.2.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event2_affected_fields2_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.2.AffectedFields.2.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event2_affected_fields3_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.2.AffectedFields.3.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event2_affected_fields3_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.2.AffectedFields.3.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event2_affected_fields4_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.2.AffectedFields.4.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event2_affected_fields4_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.2.AffectedFields.4.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event2_affected_fields5_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.2.AffectedFields.5.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event2_affected_fields5_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.2.AffectedFields.5.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event3_group_type: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.3.group_type"
    )
    entity_legal_entity_events_legal_entity_event3_event_status: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.3.event_status"
    )
    entity_legal_entity_events_legal_entity_event3_group_id: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.3.group_id"
    )
    entity_legal_entity_events_legal_entity_event3_group_sequence_no: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.3.group_sequence_no"
    )
    entity_legal_entity_events_legal_entity_event3_legal_entity_event_type: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.3.LegalEntityEventType"
    )
    entity_legal_entity_events_legal_entity_event3_legal_entity_event_effective_date: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.3.LegalEntityEventEffectiveDate"),
    )
    entity_legal_entity_events_legal_entity_event3_legal_entity_event_recorded_date: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.3.LegalEntityEventRecordedDate"),
    )
    entity_legal_entity_events_legal_entity_event3_validation_documents: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.3.ValidationDocuments"
    )
    entity_legal_entity_events_legal_entity_event3_validation_reference: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.3.ValidationReference"
    )
    entity_legal_entity_events_legal_entity_event3_affected_fields1_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.3.AffectedFields.1.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event3_affected_fields1_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.3.AffectedFields.1.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event3_affected_fields2_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.3.AffectedFields.2.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event3_affected_fields2_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.3.AffectedFields.2.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event3_affected_fields3_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.3.AffectedFields.3.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event3_affected_fields3_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.3.AffectedFields.3.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event3_affected_fields4_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.3.AffectedFields.4.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event3_affected_fields4_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.3.AffectedFields.4.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event3_affected_fields5_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.3.AffectedFields.5.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event3_affected_fields5_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.3.AffectedFields.5.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event4_group_type: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.4.group_type"
    )
    entity_legal_entity_events_legal_entity_event4_event_status: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.4.event_status"
    )
    entity_legal_entity_events_legal_entity_event4_group_id: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.4.group_id"
    )
    entity_legal_entity_events_legal_entity_event4_group_sequence_no: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.4.group_sequence_no"
    )
    entity_legal_entity_events_legal_entity_event4_legal_entity_event_type: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.4.LegalEntityEventType"
    )
    entity_legal_entity_events_legal_entity_event4_legal_entity_event_effective_date: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.4.LegalEntityEventEffectiveDate"),
    )
    entity_legal_entity_events_legal_entity_event4_legal_entity_event_recorded_date: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.4.LegalEntityEventRecordedDate"),
    )
    entity_legal_entity_events_legal_entity_event4_validation_documents: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.4.ValidationDocuments"
    )
    entity_legal_entity_events_legal_entity_event4_validation_reference: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.4.ValidationReference"
    )
    entity_legal_entity_events_legal_entity_event4_affected_fields1_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.4.AffectedFields.1.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event4_affected_fields1_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.4.AffectedFields.1.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event4_affected_fields2_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.4.AffectedFields.2.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event4_affected_fields2_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.4.AffectedFields.2.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event4_affected_fields3_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.4.AffectedFields.3.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event4_affected_fields3_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.4.AffectedFields.3.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event4_affected_fields4_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.4.AffectedFields.4.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event4_affected_fields4_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.4.AffectedFields.4.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event4_affected_fields5_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.4.AffectedFields.5.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event4_affected_fields5_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.4.AffectedFields.5.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event5_group_type: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.5.group_type"
    )
    entity_legal_entity_events_legal_entity_event5_event_status: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.5.event_status"
    )
    entity_legal_entity_events_legal_entity_event5_group_id: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.5.group_id"
    )
    entity_legal_entity_events_legal_entity_event5_group_sequence_no: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.5.group_sequence_no"
    )
    entity_legal_entity_events_legal_entity_event5_legal_entity_event_type: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.5.LegalEntityEventType"
    )
    entity_legal_entity_events_legal_entity_event5_legal_entity_event_effective_date: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.5.LegalEntityEventEffectiveDate"),
    )
    entity_legal_entity_events_legal_entity_event5_legal_entity_event_recorded_date: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.5.LegalEntityEventRecordedDate"),
    )
    entity_legal_entity_events_legal_entity_event5_validation_documents: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.5.ValidationDocuments"
    )
    entity_legal_entity_events_legal_entity_event5_validation_reference: str | None = Field(
        ..., alias="Entity.LegalEntityEvents.LegalEntityEvent.5.ValidationReference"
    )
    entity_legal_entity_events_legal_entity_event5_affected_fields1_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.5.AffectedFields.1.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event5_affected_fields1_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.5.AffectedFields.1.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event5_affected_fields2_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.5.AffectedFields.2.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event5_affected_fields2_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.5.AffectedFields.2.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event5_affected_fields3_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.5.AffectedFields.3.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event5_affected_fields3_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.5.AffectedFields.3.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event5_affected_fields4_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.5.AffectedFields.4.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event5_affected_fields4_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.5.AffectedFields.4.field_xpath"),
    )
    entity_legal_entity_events_legal_entity_event5_affected_fields5_affected_field: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.5.AffectedFields.5.AffectedField"),
    )
    entity_legal_entity_events_legal_entity_event5_affected_fields5_field_xpath: str | None = Field(
        ...,
        alias=("Entity.LegalEntityEvents.LegalEntityEvent.5.AffectedFields.5.field_xpath"),
    )


class RegistrationAuthority(Model):
    entity_registration_authority_registration_authority_id: str | None = Field(
        ..., alias="Entity.RegistrationAuthority.RegistrationAuthorityID"
    )
    entity_registration_authority_other_registration_authority_id: str | None = Field(
        ..., alias="Entity.RegistrationAuthority.OtherRegistrationAuthorityID"
    )
    entity_registration_authority_registration_authority_entity_id: str | None = Field(
        ..., alias="Entity.RegistrationAuthority.RegistrationAuthorityEntityID"
    )


class AssociatedEntity(Model):
    entity_associated_entity_type: str | None = Field(None, alias="Entity.AssociatedEntity.type")
    entity_associated_entity_associated_lei: str | None = Field(None, alias="Entity.AssociatedEntity.AssociatedLEI")
    entity_associated_entity_associated_entity_name: str | None = Field(
        ..., alias="Entity.AssociatedEntity.AssociatedEntityName"
    )
    entity_associated_entity_associated_entity_name_xmllang: str | None = Field(
        ..., alias="Entity.AssociatedEntity.AssociatedEntityName.xmllang"
    )


class LEICompany(Model):
    lei: str | None = Field(None, alias="LEI")

    entity_legal_jurisdiction: str | None = Field(None, alias="Entity.LegalJurisdiction")
    entity_entity_category: str | None = Field(None, alias="Entity.EntityCategory")
    entity_entity_sub_category: str | None = Field(None, alias="Entity.EntitySubCategory")
    entity_legal_form_entity_legal_form_code: str | None = Field(None, alias="Entity.LegalForm.EntityLegalFormCode")
    entity_legal_form_other_legal_form: str | None = Field(None, alias="Entity.LegalForm.OtherLegalForm")

    entity_entity_status: str | None = Field(None, alias="Entity.EntityStatus")
    entity_entity_creation_date: str | None = Field(None, alias="Entity.EntityCreationDate")
    entity_entity_expiration_date: str | None = Field(None, alias="Entity.EntityExpirationDate")
    entity_entity_expiration_reason: str | None = Field(None, alias="Entity.EntityExpirationReason")
