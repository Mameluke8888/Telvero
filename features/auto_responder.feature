@auto-responder
Feature: A registered user can set an Auto-Responder
  Background:
    Given a registered user opens home page in a browser
    And user clicks Login button
    And user types in correct email and password in corresponding fields
    And user moves to user's account by clicking Sign In
    And user moved to settings menu by clicking on Settings option from left menu
    And user moves to auto-responder settings page by clicking on Auto-Responder option from left menu
    And user clicks Create New Auto-Responder button
    And user fills Responder Name and Message fields
    And user selects applying active phone numbers by checking corresponding checkboxes


  @positive @create
  Scenario: Create a Single Auto-Responder
    Given user selects to set a single auto-responder by checking Single checkbox
    And user sets start and end date and time using popup calendars/clocks pops up by clicking calendar pictograms
    And user selects time zone using corresponding dropdown
    And user clicks Create button
    Then user is back on auto-responder settings page and the new auto-responder appears in the list of auto-responders

  @positive @create
  Scenario: Create an Auto-Responder Recurring Weekly
    Given user selects to set a weekly auto-responder by checking Weekly checkbox
    And user sets start and end time using popup clocks pops up by clicking calendar pictograms
    And user adds extra time range by clicking Add another time range link
    And user sets extra start and end time using popup clocks pops up by clicking calendar pictograms
    And user selects time zone using corresponding dropdown
    And user selects week days auto-responder is required to be active by clicking corresponding checkboxes
    And user clicks Create button
    Then user is back on auto-responder settings page and the new auto-responder appears in the list of auto-responders