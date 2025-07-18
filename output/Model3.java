package com.example.models;

import java.time.LocalDate;

/**
 * Model3 - Auto-generated model class
 * Generated from CSV schema definition
 */
public class Model3 {

    /**
     * xpath: /root/person/id
     * required/optional: required
     * data_type: Integer
     * model_value: entityId
     * additional_info: validation_rules: min:1 max:999999
     * default_value: entityId
     */
    private Integer id;

    /**
     * xpath: /root/person/name/last
     * required/optional: required
     * data_type: String
     * model_value: surname
     * additional_info: validation_rules: minLength:1 maxLength:50
     * default_value: surname
     */
    private String last = "surname";

    /**
     * xpath: /root/person/email
     * required/optional: optional
     * data_type: String
     * model_value: email
     * additional_info: validation_rules: pattern:email format
     */
    private String email;

    /**
     * xpath: /root/person/address/street
     * required/optional: optional
     * data_type: String
     * model_value: street
     * additional_info: validation_rules: maxLength:100
     */
    private String street;

    /**
     * xpath: /root/person/address/city
     * required/optional: optional
     * data_type: String
     * model_value: cityName
     * additional_info: validation_rules: maxLength:50
     * default_value: cityName
     */
    private String city = "cityName";

    /**
     * xpath: /root/person/address/zipcode
     * required/optional: optional
     * data_type: String
     * model_value: zip
     * additional_info: validation_rules: pattern:postal code
     * default_value: zip
     */
    private String zipcode = "zip";

    /**
     * xpath: /root/person/active
     * required/optional: optional
     * data_type: Boolean
     * model_value: status
     * additional_info: validation_rules: default:true
     * default_value: status
     */
    private Boolean active;

    /**
     * xpath: /root/person/hire_date
     * required/optional: optional
     * data_type: LocalDate
     * model_value: employmentDate
     * additional_info: validation_rules: format:YYYY-MM-DD
     * default_value: employmentDate
     */
    private LocalDate hireDate;

    /**
     * Default constructor
     */
    public Model3() {
    }

    /**
     * Parameterized constructor
     * @param id Field mapped from XPath: /root/person/id
     * @param last Field mapped from XPath: /root/person/name/last
     * @param email Field mapped from XPath: /root/person/email
     * @param street Field mapped from XPath: /root/person/address/street
     * @param city Field mapped from XPath: /root/person/address/city
     * @param zipcode Field mapped from XPath: /root/person/address/zipcode
     * @param active Field mapped from XPath: /root/person/active
     * @param hireDate Field mapped from XPath: /root/person/hire_date
     */
    public Model3(Integer id, String last, String email, String street, String city, String zipcode, Boolean active, LocalDate hireDate) {
        this.id = id;
        this.last = last;
        this.email = email;
        this.street = street;
        this.city = city;
        this.zipcode = zipcode;
        this.active = active;
        this.hireDate = hireDate;
    }

    /**
     * Get id
     * @return Integer
     */
    public Integer getId() {
        return id;
    }

    /**
     * Set id
     * @param id Integer
     */
    public void setId(Integer id) {
        this.id = id;
    }

    /**
     * Get last
     * @return String
     */
    public String getLast() {
        return last;
    }

    /**
     * Set last
     * @param last String
     */
    public void setLast(String last) {
        this.last = last;
    }

    /**
     * Get email
     * @return String
     */
    public String getEmail() {
        return email;
    }

    /**
     * Set email
     * @param email String
     */
    public void setEmail(String email) {
        this.email = email;
    }

    /**
     * Get street
     * @return String
     */
    public String getStreet() {
        return street;
    }

    /**
     * Set street
     * @param street String
     */
    public void setStreet(String street) {
        this.street = street;
    }

    /**
     * Get city
     * @return String
     */
    public String getCity() {
        return city;
    }

    /**
     * Set city
     * @param city String
     */
    public void setCity(String city) {
        this.city = city;
    }

    /**
     * Get zipcode
     * @return String
     */
    public String getZipcode() {
        return zipcode;
    }

    /**
     * Set zipcode
     * @param zipcode String
     */
    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }

    /**
     * Get active
     * @return Boolean
     */
    public Boolean getActive() {
        return active;
    }

    /**
     * Set active
     * @param active Boolean
     */
    public void setActive(Boolean active) {
        this.active = active;
    }

    /**
     * Get hireDate
     * @return LocalDate
     */
    public LocalDate getHiredate() {
        return hireDate;
    }

    /**
     * Set hireDate
     * @param hireDate LocalDate
     */
    public void setHiredate(LocalDate hireDate) {
        this.hireDate = hireDate;
    }

    /**
     * String representation of the object
     * @return String
     */
    @Override
    public String toString() {
        return "Model3{" + "id=" + id + ", " + "last=" + last + ", " + "email=" + email + ", " + "street=" + street + ", " + "city=" + city + ", " + "zipcode=" + zipcode + ", " + "active=" + active + ", " + "hireDate=" + hireDate + "}";
    }

    /**
     * Check equality with another object
     * @param obj Object to compare
     * @return boolean
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Model3 that = (Model3) obj;
        return java.util.Objects.equals(id, that.id) && java.util.Objects.equals(last, that.last) && java.util.Objects.equals(email, that.email) && java.util.Objects.equals(street, that.street) && java.util.Objects.equals(city, that.city) && java.util.Objects.equals(zipcode, that.zipcode) && java.util.Objects.equals(active, that.active) && java.util.Objects.equals(hireDate, that.hireDate);
    }

    /**
     * Generate hash code
     * @return int
     */
    @Override
    public int hashCode() {
        return java.util.Objects.hash(id, last, email, street, city, zipcode, active, hireDate);
    }

}