@login
Feature: User can access his account through login page
  Background:
    Given registered user who is not logged in has home page opened in a browser

    @positive
    Scenario: accessing user's account with correct credentials
      Given user clicks Login button on home page
      When user enters correct both email address and password in the corresponding fields
      And user clicks Sign In button
      Then user account page is open

    @negative
    Scenario: accessing user's account with unregistered email
      Given user clicks Login button on home page
      When user enters unregistered but valid email address and correct password in the corresponding fields
      And user clicks Sign In button
      Then general message "The credentials you provided appear to be invalid. Try again?" appears

    @negative
    Scenario: accessing user's account with incorrect password
      Given user clicks Login button on home page
      When user enters registered email address but incorrect password in the corresponding fields
      And user clicks Sign In button
      Then general message "The credentials you provided appear to be invalid. Try again?" appears

    @negative
    Scenario: accessing user's account with invalid email
      Given user clicks Login button on home page
      When user enters invalid email address and correct password in the corresponding fields
      And user clicks Sign In button
      Then message under email field "Invalid email address" appears

    @negative
    Scenario: accessing user's account with empty email field
      Given user clicks Login button on home page
      When user enters incorrect email address and correct password in the corresponding fields
      And user clicks Sign In button
      Then message under email field "Email field shouldn’t be empty" appears