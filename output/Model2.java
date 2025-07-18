package com.example.models;

import java.math.BigDecimal;
import java.time.LocalDate;

/**
 * Model2 - Auto-generated model class
 * Generated from CSV schema definition
 */
public class Model2 {

    /**
     * xpath: /root/person/id
     * required/optional: required
     * data_type: Integer
     * model_value: userId
     * additional_info: validation_rules: min:1 max:999999
     * default_value: userId
     */
    private Integer id;

    /**
     * xpath: /root/person/name/first
     * required/optional: required
     * data_type: String
     * model_value: givenName
     * additional_info: validation_rules: minLength:1 maxLength:50
     * default_value: givenName
     */
    private String first = "givenName";

    /**
     * xpath: /root/person/name/last
     * required/optional: required
     * data_type: String
     * model_value: familyName
     * additional_info: validation_rules: minLength:1 maxLength:50
     * default_value: familyName
     */
    private String last = "familyName";

    /**
     * xpath: /root/person/email
     * required/optional: optional
     * data_type: String
     * model_value: contactEmail
     * additional_info: validation_rules: pattern:email format
     * default_value: contactEmail
     */
    private String email = "contactEmail";

    /**
     * xpath: /root/person/age
     * required/optional: optional
     * data_type: Integer
     * model_value: yearsOld
     * additional_info: validation_rules: min:0 max:150
     * default_value: yearsOld
     */
    private Integer age;

    /**
     * xpath: /root/person/address/street
     * required/optional: optional
     * data_type: String
     * model_value: addressLine1
     * additional_info: validation_rules: maxLength:100
     * default_value: addressLine1
     */
    private String street = "addressLine1";

    /**
     * xpath: /root/person/address/city
     * required/optional: optional
     * data_type: String
     * model_value: locality
     * additional_info: validation_rules: maxLength:50
     * default_value: locality
     */
    private String city = "locality";

    /**
     * xpath: /root/person/address/zipcode
     * required/optional: optional
     * data_type: String
     * model_value: postalCode
     * additional_info: validation_rules: pattern:postal code
     * default_value: postalCode
     */
    private String zipcode = "postalCode";

    /**
     * xpath: /root/person/phone
     * required/optional: optional
     * data_type: String
     * model_value: contactNumber
     * additional_info: validation_rules: pattern:phone format
     * default_value: contactNumber
     */
    private String phone = "contactNumber";

    /**
     * xpath: /root/person/active
     * required/optional: optional
     * data_type: Boolean
     * model_value: enabled
     * additional_info: validation_rules: default:true
     * default_value: enabled
     */
    private Boolean active;

    /**
     * xpath: /root/person/salary
     * required/optional: optional
     * data_type: BigDecimal
     * model_value: compensation
     * additional_info: validation_rules: min:0 precision:2
     * default_value: compensation
     */
    private BigDecimal salary;

    /**
     * xpath: /root/person/hire_date
     * required/optional: optional
     * data_type: LocalDate
     * model_value: startDate
     * additional_info: validation_rules: format:YYYY-MM-DD
     * default_value: startDate
     */
    private LocalDate hireDate;

    /**
     * Default constructor
     */
    public Model2() {
    }

    /**
     * Parameterized constructor
     * @param id Field mapped from XPath: /root/person/id
     * @param first Field mapped from XPath: /root/person/name/first
     * @param last Field mapped from XPath: /root/person/name/last
     * @param email Field mapped from XPath: /root/person/email
     * @param age Field mapped from XPath: /root/person/age
     * @param street Field mapped from XPath: /root/person/address/street
     * @param city Field mapped from XPath: /root/person/address/city
     * @param zipcode Field mapped from XPath: /root/person/address/zipcode
     * @param phone Field mapped from XPath: /root/person/phone
     * @param active Field mapped from XPath: /root/person/active
     * @param salary Field mapped from XPath: /root/person/salary
     * @param hireDate Field mapped from XPath: /root/person/hire_date
     */
    public Model2(Integer id, String first, String last, String email, Integer age, String street, String city, String zipcode, String phone, Boolean active, BigDecimal salary, LocalDate hireDate) {
        this.id = id;
        this.first = first;
        this.last = last;
        this.email = email;
        this.age = age;
        this.street = street;
        this.city = city;
        this.zipcode = zipcode;
        this.phone = phone;
        this.active = active;
        this.salary = salary;
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
     * Get first
     * @return String
     */
    public String getFirst() {
        return first;
    }

    /**
     * Set first
     * @param first String
     */
    public void setFirst(String first) {
        this.first = first;
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
     * Get age
     * @return Integer
     */
    public Integer getAge() {
        return age;
    }

    /**
     * Set age
     * @param age Integer
     */
    public void setAge(Integer age) {
        this.age = age;
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
     * Get phone
     * @return String
     */
    public String getPhone() {
        return phone;
    }

    /**
     * Set phone
     * @param phone String
     */
    public void setPhone(String phone) {
        this.phone = phone;
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
     * Get salary
     * @return BigDecimal
     */
    public BigDecimal getSalary() {
        return salary;
    }

    /**
     * Set salary
     * @param salary BigDecimal
     */
    public void setSalary(BigDecimal salary) {
        this.salary = salary;
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
        return "Model2{" + "id=" + id + ", " + "first=" + first + ", " + "last=" + last + ", " + "email=" + email + ", " + "age=" + age + ", " + "street=" + street + ", " + "city=" + city + ", " + "zipcode=" + zipcode + ", " + "phone=" + phone + ", " + "active=" + active + ", " + "salary=" + salary + ", " + "hireDate=" + hireDate + "}";
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
        Model2 that = (Model2) obj;
        return java.util.Objects.equals(id, that.id) && java.util.Objects.equals(first, that.first) && java.util.Objects.equals(last, that.last) && java.util.Objects.equals(email, that.email) && java.util.Objects.equals(age, that.age) && java.util.Objects.equals(street, that.street) && java.util.Objects.equals(city, that.city) && java.util.Objects.equals(zipcode, that.zipcode) && java.util.Objects.equals(phone, that.phone) && java.util.Objects.equals(active, that.active) && java.util.Objects.equals(salary, that.salary) && java.util.Objects.equals(hireDate, that.hireDate);
    }

    /**
     * Generate hash code
     * @return int
     */
    @Override
    public int hashCode() {
        return java.util.Objects.hash(id, first, last, email, age, street, city, zipcode, phone, active, salary, hireDate);
    }

}