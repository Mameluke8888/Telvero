@account
Feature: A registered user can change information the personal account
  Background:
    Given a registered user opens home page in a browser
    And user clicks Login button
    And user types in correct email and password in corresponding fields
    And user moves to user's account by clicking Sign In
    And user moved to settings menu by clicking on Settings option from left menu


  @positive @update
  Scenario: Updating account information
    Given user moves to account information page by clicking on Your Profile option from left menu
    When user clicks Edit button
    And user types in new first name, last name, email in corresponding fields
    And user clicks Done button
    Then user is back on updated account information page, color of logo is changed
