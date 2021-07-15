@team
Feature: A registered user can add a team member
  Background:
    Given a registered user is successfully logged in
    And user moves to settings menu by clicking on Settings option from left menu


  @positive
  Scenario: Adding a team member
    Given user moves to team information page by clicking on Team option from left menu
    And user opens a page of new team member data by clicking Add Team Member button
    When user fills corresponding fields with first name, second name and email of the new team member
    And user selects level of access of the new team member in Role dropdown
    And user clicks Send Invite button
    Then user is back on updated team information page, the new team member appears in the team list as invited

