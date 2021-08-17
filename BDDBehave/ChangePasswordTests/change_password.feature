@password
Feature: A registered user can change the password
  Background:
    Given a registered user is successfully logged in
    And user moves to settings menu by clicking on Settings option from left menu


  @positive
  Scenario: Changing a password with correct data
    Given user moves to password update page by clicking on Change Password option from left menu
    When user types in current password, new password at least 8 symbols long, matched new password confirmation
    And user clicks Update button
    Then message "Password changed successfully" appears

  @negative
  Scenario: Changing a password with incorrect data
    Given user moves to password update page by clicking on Change Password option from left menu
    When user types in current password, new password at least 8 symbols long, unmatched new password confirmation
    And user clicks Update button
    Then message "Passwords do not match" appears

  @negative
  Scenario: Changing a password with too short password
    Given user moves to password update page by clicking on Change Password option from left menu
    When user types in current password, new password shorter than 8 symbols long, matched new password confirmation
    And user clicks Update button
    Then message "The password is too short" appears

  @negative
  Scenario: Changing a password with no confirmation of password
    Given user moves to password update page by clicking on Change Password option from left menu
    When user types in current password, new password at least 8 symbols long, no new password confirmation
    And user clicks Update button
    Then message "Confirm Password field shouldn’t be empty" appears

  @negative
  Scenario: Changing a password with no new password and no confirmation of password
    Given user moves to password update page by clicking on Change Password option from left menu
    When user types in current password, no new password, no new password confirmation
    And user clicks Update button
    Then message "Password field shouldn’t be empty" appears

  @negative
  Scenario: Changing a password with incorrect current password
    Given user moves to password update page by clicking on Change Password option from left menu
    When user types incorrect current password, new password at least 8 symbols long, matched new password confirmation
    And user clicks Update button
    Then message "Your current password is incorrect, please enter correct password." appears